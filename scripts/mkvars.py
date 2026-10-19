#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Generate variables.md documentation from oarepo-config functions and Flask app config.

This script:

1. Loads a Flask app to get all configuration variables
2. Analyzes `oarepo_config/*` modules to find which `configure_*` functions reference which variables
3. Generates a markdown file with:
    - A summary table of all variables and their referencing functions
    - Alphabetically sorted sections for each variable with docstrings and references

Usage:
    python scripts/mkvars.py

The output is written to docs/variables.md.
"""

from __future__ import annotations

import ast
import inspect
import pprint
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, Any

import flask

if TYPE_CHECKING:
    from flask import Flask

type VarInfo = dict[str, Any]

# Longest value shown inline in a table cell before it gets cut off with "...".
VALUE_PREVIEW_LENGTH = 100
# Longest function docstring kept per function reference.
DOCSTRING_PREVIEW_LENGTH = 500
# Number of referencing functions listed in the summary table before "(+N more)".
SUMMARY_MAX_FUNCTIONS = 3
# How many lines after an assignment to look for its docstring.
DOCSTRING_LOOKAHEAD_LINES = 10

# Docstring section of configure_* functions that lists the variables they set.
VARIABLES_SECTION_HEADER = "Invenio configuration variables set:"

# Object reprs embed memory addresses ("<function <lambda> at 0x1118...>"),
# which change on every run; dropping them keeps regenerated output stable.
_MEMORY_ADDRESS = re.compile(r" at 0x[0-9a-f]+")

# AST node types whose source is collapsed to a "<type>" placeholder in the
# summary/detail tables, with the full literal shown separately underneath -
# these can be arbitrarily long/nested and don't read well truncated mid-way.
_AST_COMPLEX_LITERAL_TYPES = {
    ast.Dict: "dict",
    ast.List: "list",
    ast.Tuple: "tuple",
    ast.Set: "set",
}

# Container node types pretty_unparse() indents one entry per line; anything
# else (calls, names, constants, ...) is rendered as-is via ast.unparse().
_AST_CONTAINER_BRACKETS = {
    ast.Dict: ("{", "}"),
    ast.List: ("[", "]"),
    ast.Set: ("{", "}"),
    ast.Tuple: ("(", ")"),
}

_HEADER = """\
# Configuration Variables Reference
This document lists all configuration variables used by oarepo-config and related extensions.
It is automatically generated from:
- The Flask application's configuration (via `invenio_app.factory.create_app()`)
- The docstrings in `oarepo_config/*` modules
- Configuration files from installed invenio_ and oarepo_ extensions

## How to Use This Document

1. **Summary Table**: Quickly find which configure_* functions set each variable.
2. **Detailed Reference**: For each variable, see its default value, type, source, and which \
configure_* functions reference it.

---

"""


def _truncate(text: str, limit: int) -> str:
    """Cut `text` to `limit` characters, marking the cut with "..."."""
    return text[:limit] + "..." if len(text) > limit else text


def pretty_unparse(node: ast.expr, indent: int = 0) -> str:
    """Render a dict/list/tuple/set literal AST node as indented multi-line source.

    Unlike `ast.literal_eval` + `pprint`, this doesn't require the value to
    be a pure literal - non-literal leaves (e.g. `_("JSON")` calls, which
    are common in these config docstrings/defaults) are kept as-is via
    `ast.unparse`, only the surrounding containers get indented.
    """
    brackets = _AST_CONTAINER_BRACKETS.get(type(node))
    if brackets is None:
        return ast.unparse(node)

    open_bracket, close_bracket = brackets
    pad = "    " * indent
    pad_inner = "    " * (indent + 1)

    if isinstance(node, ast.Dict):
        if not node.keys:
            return open_bracket + close_bracket
        lines = []
        for key, value in zip(node.keys, node.values, strict=True):
            value_src = pretty_unparse(value, indent + 1)
            if key is None:  # a "**other_dict" unpacking entry
                lines.append(f"{pad_inner}**{value_src}")
            else:
                lines.append(f"{pad_inner}{pretty_unparse(key, indent + 1)}: {value_src}")
    else:
        elts = node.elts  # ty: ignore[unresolved-attribute] - List/Set/Tuple per _AST_CONTAINER_BRACKETS
        if not elts:
            return open_bracket + close_bracket
        lines = [f"{pad_inner}{pretty_unparse(elt, indent + 1)}" for elt in elts]

    return open_bracket + "\n" + ",\n".join(lines) + ",\n" + pad + close_bracket


def load_flask_app() -> Flask:
    """Load the Flask application to access its configuration."""
    try:
        from invenio_app.factory import create_app

        return create_app()
    except OSError as e:
        raise RuntimeError("Could not load Flask app") from e


def get_extension_configs() -> dict[str, dict[str, str]]:
    """Get all configuration modules from installed extensions.

    Looks for invenio_ and oarepo_ packages with config.py or initial_config.py files.
    """
    config_modules: dict[str, dict[str, str]] = {}
    # flask lives directly in site-packages, next to every extension
    site_packages = Path(inspect.getfile(flask)).parent.parent
    try:
        for item in site_packages.iterdir():
            if not (item.is_dir() and item.name.startswith(("invenio_", "oarepo_"))):
                continue
            # initial_config.py wins over config.py when a package has both
            for filename in ("config.py", "initial_config.py"):
                if (item / filename).exists():
                    config_modules[item.name] = {"path": str(item / filename), "type": filename}
    except OSError as e:
        sys.stderr.write(f"Warning: Could not scan site-packages: {e}\n")
    return config_modules


def _value_repr(value: ast.expr) -> tuple[str, str | None]:
    """Return the table-cell representation of an assigned value and, for literals, its full source.

    dict/list/tuple/set literals collapse to a "<type>" placeholder in the
    table (their full source is shown separately, below it) rather than
    being cut off mid-structure by the length truncation.
    """
    complex_type_name = _AST_COMPLEX_LITERAL_TYPES.get(type(value))
    if complex_type_name:
        return f"<{complex_type_name}>", pretty_unparse(value)
    return _truncate(ast.unparse(value), VALUE_PREVIEW_LENGTH), None


def _triple_quoted_text(lines: list[str], start: int) -> str:
    """Read the triple-quoted string starting on `lines[start]`.

    Original line breaks/indentation are kept - these docstrings are reST
    (directives, code-blocks, ...) and lose their structure otherwise.
    """
    line = lines[start].strip()
    quote = line[: len('"""')]
    if quote in line[len(quote) :] and len(line) > 2 * len(quote):
        return line[len(quote) : -len(quote)].strip()

    docstring_lines = [line[len(quote) :]] if len(line) > len(quote) else []
    for following in lines[start + 1 :]:
        if quote in following:
            docstring_lines.append(following[: following.index(quote)])
            break
        docstring_lines.append(following)
    return "\n".join(docstring_lines).strip()


def _variable_docstring(lines: list[str], line_index: int) -> str | None:
    """Find the docstring of the assignment on `lines[line_index]`.

    That is the first triple-quoted string following the assignment (only
    blank lines and comments may sit in between), falling back to an inline
    comment on the assignment line itself.
    """
    for i in range(line_index + 1, min(line_index + DOCSTRING_LOOKAHEAD_LINES, len(lines))):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(('"""', "'''")):
            return _triple_quoted_text(lines, i)
        break

    assign_line = lines[line_index]
    if "#" in assign_line:
        return assign_line[assign_line.index("#") + 1 :].strip() or None
    return None


def extract_config_variables_from_file(file_path: str) -> dict[str, VarInfo]:
    """Extract configuration variables and their docstrings from a config file using AST.

    Looks for:

    - Module-level assignments with uppercase variable names
    - Docstrings (triple-quoted strings) following the assignment
    - Inline comments after assignments
    - Line numbers where variables are defined
    """
    try:
        source = Path(file_path).read_text(encoding="utf-8")
    except OSError as e:
        sys.stderr.write(f"Warning: Could not parse {file_path}: {e}\n")
        return {}

    lines = source.split("\n")
    variables: dict[str, VarInfo] = {}
    for node in ast.walk(ast.parse(source)):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id.isupper():
                value_repr, full_value = _value_repr(node.value)
                variables[target.id] = {
                    "docstring": _variable_docstring(lines, node.lineno - 1),
                    "file": file_path,
                    "value": value_repr,
                    "full_value": full_value,
                    "line": node.lineno,
                }
    return variables


def convert_path_to_github_link(file_path: str, line_number: int | None) -> str:
    """Convert a file path to a GitHub link.

    - invenio_* packages: `https://github.com/inveniosoftware/{package}/blob/master/{relative_path}#L{line}`
    - oarepo_* packages: `https://github.com/oarepo/{package}/blob/master/{relative_path}#L{line}`
    - other paths: the file name with the line number
    """
    path = Path(file_path)
    package_name = path.parent.name
    for prefix, organization in (("invenio_", "inveniosoftware"), ("oarepo_", "oarepo")):
        if package_name.startswith(prefix):
            # GitHub repositories use dashes where package names use underscores
            repo_name = package_name.replace("_", "-")
            return (
                f"[{repo_name}](https://github.com/{organization}/{repo_name}"
                f"/blob/master/{package_name}/{path.name}#L{line_number})"
            )
    return f"{path.name} (line {line_number})"


def _referenced_variables(function: ast.FunctionDef) -> set[str]:
    """Collect uppercase names a function assigns to or reads."""
    names: set[str] = set()
    for stmt in ast.walk(function):
        if isinstance(stmt, ast.Assign):
            names.update(t.id for t in stmt.targets if isinstance(t, ast.Name) and t.id.isupper())
        elif isinstance(stmt, ast.Name) and stmt.id.isupper():
            names.add(stmt.id)
    return names


def _documented_variables(docstring: str) -> set[str]:
    """Collect variable names listed in a docstring's "Invenio configuration variables set:" section."""
    names: set[str] = set()
    in_section = False
    for line in docstring.split("\n"):
        if VARIABLES_SECTION_HEADER in line:
            in_section = True
            continue
        if not in_section:
            continue
        if line.strip() and not line.startswith((" ", "\t")) and ":" not in line:
            break  # end of section
        names.update(
            name for match in re.findall(r"`(`?[A-Z_][A-Z0-9_]*`?)`", line) if (name := match.strip("`")).isupper()
        )
    return names


def analyze_oarepo_config_functions(oarepo_config_dir: Path) -> dict[str, list[VarInfo]]:
    """Analyze oarepo_config/* modules to find which variables are referenced in each function."""
    function_variables: dict[str, list[VarInfo]] = defaultdict(list)
    if not oarepo_config_dir.exists():
        sys.stderr.write(f"Warning: oarepo_config directory not found at {oarepo_config_dir}\n")
        return function_variables

    for py_file in oarepo_config_dir.glob("*.py"):
        if py_file.name.startswith("__"):
            continue
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
        except OSError as e:
            sys.stderr.write(f"Warning: Could not analyze {py_file}: {e}\n")
            continue

        # Top-level configure/register-style functions (e.g. configure_ui,
        # initialize_i18n, register_workflow, add_model)
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.FunctionDef)
                and node.name.startswith(("configure_", "initialize_", "register_", "add_"))
            ):
                continue
            docstring = ast.get_docstring(node) or ""
            for var_name in _referenced_variables(node) | _documented_variables(docstring):
                function_variables[var_name].append(
                    {
                        "function": node.name,
                        "file": str(py_file),
                        "line": node.lineno,
                        "docstring": _truncate(docstring, DOCSTRING_PREVIEW_LENGTH),
                    }
                )
    return function_variables


def variable_anchor(var_name: str) -> str:
    """Return the id the Markdown toc extension assigns to a variable's heading.

    Variable names are plain `[A-Z0-9_]` identifiers, and the toc slugifier
    keeps word characters (including `_`) as-is, so this is just lowercase.
    """
    return var_name.lower()


def default_value_label(var_info: VarInfo) -> str:
    """Return the "Default Value" row label, naming the package family it comes from."""
    paths = [path for path, _line in var_info.get("sources", [])] or [var_info.get("source")]
    package_names = {Path(path).parent.name for path in paths if path}
    if any(name.startswith("oarepo_") for name in package_names):
        return "OARepo Default Value"
    if any(name.startswith("invenio_") for name in package_names):
        return "Invenio RDM Default Value"
    return "Default Value"


def _stable_pformat(value: Any) -> str:
    """Pretty-print a config value in the same order on every run.

    pprint orders set elements and dict keys that don't compare (e.g.
    exception classes) by `id()`, and string sets by per-process hash;
    dicts keep their insertion order instead and sets are sorted by repr.
    """
    if isinstance(value, set):
        as_list = pprint.pformat(sorted(value, key=repr), width=88, sort_dicts=False)
        return "{" + as_list[1:-1] + "}" if value else "set()"
    return pprint.pformat(value, width=88, sort_dicts=False)


def _app_config_variables(app: Flask) -> dict[str, VarInfo]:
    """Collect uppercase variables from the live app config."""
    variables: dict[str, VarInfo] = {}
    for key in sorted(app.config.keys()):
        if not key.isupper() or key.startswith("_"):
            continue
        value = app.config[key]
        try:
            # Some config values are lazy proxies (e.g. Werkzeug
            # LocalProxy/cached_property-backed settings computed from
            # other extensions) that only resolve correctly inside a
            # request/app context, and can raise arbitrary errors -
            # not just on repr/pprint, but even from isinstance()
            # forcing the proxy to resolve - when poked at here.
            # Skipping that one key is better than crashing doc
            # generation over an unrelated extension's app-state bug.
            is_complex = isinstance(value, (dict, list, tuple, set))
            is_representable = not callable(value) and not isinstance(value, (type, dict, list, tuple, set))
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(f"Warning: Could not inspect app.config[{key!r}]: {e}\n")
            continue

        # Skip complex objects that can't be easily represented
        if is_representable:
            variables[key] = {
                "value": _truncate(_MEMORY_ADDRESS.sub("", repr(value)), VALUE_PREVIEW_LENGTH),
                "type": type(value).__name__,
                "docstring": None,
                "source": "unknown",
            }
        elif is_complex:
            try:
                full_value = _MEMORY_ADDRESS.sub("", _stable_pformat(value))
            except Exception as e:  # noqa: BLE001 - see above
                sys.stderr.write(f"Warning: Could not format app.config[{key!r}]: {e}\n")
                full_value = None
            variables[key] = {
                "value": f"<{type(value).__name__}>",
                "full_value": full_value,
                "type": type(value).__name__,
                "docstring": None,
                "source": "unknown",
            }
    return variables


def _merge_file_variable(existing: VarInfo, path: str, var_info: VarInfo) -> None:
    """Record another config file defining an already known variable."""
    if "sources" not in existing:
        source = existing.get("source")
        # A non-path source (e.g. "unknown" for app-config-only variables)
        # is not listed among the sources
        existing["sources"] = [] if source and not source.startswith("/") else [(source, existing.get("line"))]
    existing["sources"].append((path, var_info.get("line")))

    # First docstring and line number found win
    if var_info.get("docstring") and not existing.get("docstring"):
        existing["docstring"] = var_info["docstring"]
    if var_info.get("line") and not existing.get("line"):
        existing["line"] = var_info["line"]
    existing["source"] = path


def _collect_variables(
    app: Flask, extension_configs: dict[str, dict[str, str]], oarepo_function_vars: dict[str, list[VarInfo]]
) -> dict[str, VarInfo]:
    """Merge app config, extension config files and oarepo_config function references into one mapping."""
    all_variables = _app_config_variables(app)

    for info in extension_configs.values():
        path = info["path"]
        for var_name, var_info in extract_config_variables_from_file(path).items():
            if var_name in all_variables:
                _merge_file_variable(all_variables[var_name], path, var_info)
            else:
                all_variables[var_name] = {
                    "value": var_info.get("value", ""),
                    "full_value": var_info.get("full_value"),
                    "type": "unknown",
                    "docstring": var_info.get("docstring"),
                    "source": path,
                    "line": var_info.get("line"),
                    "sources": [(path, var_info.get("line"))],
                }

    for var_name, funcs in oarepo_function_vars.items():
        if var_name not in all_variables:
            all_variables[var_name] = {
                "value": "",
                "type": "configured by function",
                "docstring": None,
                "source": funcs[0]["file"],
                "line": funcs[0].get("line"),
            }
    return all_variables


def _summary_row(var_name: str, var_info: VarInfo, ref_funcs: list[VarInfo]) -> str:
    """Render one row of the summary table."""
    ref_names = ", ".join(f"`{f['function']}`" for f in ref_funcs[:SUMMARY_MAX_FUNCTIONS])
    if len(ref_funcs) > SUMMARY_MAX_FUNCTIONS:
        ref_names += f" (+{len(ref_funcs) - SUMMARY_MAX_FUNCTIONS} more)"
    # Links to the detail heading below, whose id the toc extension
    # generates. Browsers never treat "_" as a break opportunity - a
    # zero-width space after each one lets long names wrap at underscores
    # instead of overflowing the table.
    display_name = var_name.replace("_", "_\u200b")
    var_type = var_info.get("type", "unknown")
    return f"| [`{display_name}`](#{variable_anchor(var_name)}) | {var_type} | {ref_names or '-'} |\n"


def _source_row(var_info: VarInfo) -> str | None:
    """Render the Source(s) table row, linking to GitHub where possible."""
    source = var_info.get("source")
    if not source:
        return None
    sources = var_info.get("sources") or []
    if len(sources) > 1:
        return f"| **Sources** | {'; '.join(convert_path_to_github_link(p, line) for p, line in sources)} |"
    if var_info.get("line"):
        return f"| **Source** | {convert_path_to_github_link(source, var_info['line'])} |"
    return f"| **Source** | {source.replace('|', '\\|')} |"


def _variable_section(var_name: str, var_info: VarInfo, ref_funcs: list[VarInfo]) -> list[str]:
    """Render the detailed reference section of one variable."""
    # Lead with a star and bold the name for variables one of our own
    # functions sets, so they stand out from the (much larger) set of
    # plain Invenio/extension variables listed here purely for reference.
    # The star is escaped so Markdown doesn't read it as emphasis; the
    # toc slugifier drops it, so the anchor stays variable_anchor().
    heading_name = f"**\\*{var_name}**" if ref_funcs else var_name
    lines = [f"\n### {heading_name}\n"]

    # Description as a plain paragraph, not a table row, so it reads
    # like prose instead of being squeezed into a table cell. Docstrings
    # of third-party (Invenio) config modules are reST we can't rewrite;
    # they are included as-is, which reads fine for the plain-prose
    # majority.
    if var_info.get("docstring"):
        lines.append("\n" + var_info["docstring"].strip() + "\n\n")

    table_rows = []
    if var_info.get("value"):
        value = var_info["value"].replace("|", "\\|")
        table_rows.append(f"| **{default_value_label(var_info)}** | `{value}` |")
    if var_info.get("type"):
        table_rows.append(f"| **Type** | {var_info['type']} |")
    if source_row := _source_row(var_info):
        table_rows.append(source_row)
    if ref_funcs:
        # mkdocstrings anchors every re-exported function by its dotted
        # path on the package's reference page.
        func_names = dict.fromkeys(f["function"] for f in ref_funcs)
        func_links = ", ".join(f"[`{name}`](reference/index.md#oarepo_config.{name})" for name in func_names)
        table_rows.append(f"| **Set by** | {func_links} |")

    # The first row doubles as the (headerless) table's header
    if table_rows:
        lines.append(table_rows[0] + "\n")
        lines.append("|--------------|-----------|\n")
        lines.extend(row + "\n" for row in table_rows[1:])
    lines.append("\n")

    # dict/list/tuple/set defaults are collapsed to a "<type>" placeholder
    # in the table above (long/nested values don't fit a cell); show the
    # full value underneath instead of just losing it. Left unlabelled
    # (not a ```python fence) since values pulled from the live app config
    # are a pprint() of the real objects, which often contain reprs like
    # "<class 'invenio_foo.Bar'>" that aren't actually valid Python syntax
    # and make the Pygments Python lexer choke.
    if var_info.get("full_value"):
        lines.append("```\n")
        lines.append(var_info["full_value"].rstrip("\n") + "\n")
        lines.append("```\n\n")

    lines.append("---\n\n")
    return lines


def generate_markdown(
    app: Flask, extension_configs: dict[str, dict[str, str]], oarepo_function_vars: dict[str, list[VarInfo]]
) -> str:
    """Generate the markdown documentation."""
    all_variables = _collect_variables(app, extension_configs, oarepo_function_vars)
    var_names = sorted(all_variables)

    lines = [_HEADER, "## Summary Table\n", "| Variable Name | Type | Referenced By |\n"]
    lines.append("|---------------|------|---------------|\n")
    lines.extend(_summary_row(name, all_variables[name], oarepo_function_vars.get(name, [])) for name in var_names)

    lines.append("\n## Detailed Variable Reference\n")
    for name in var_names:
        lines.extend(_variable_section(name, all_variables[name], oarepo_function_vars.get(name, [])))
    return "".join(lines)


def main() -> None:
    """Run the script to generate documentation."""
    sys.stderr.write("Loading Flask application...\n")
    app = load_flask_app()
    with app.app_context():
        sys.stderr.write("Getting extension configurations...\n")
        extension_configs = get_extension_configs()
        sys.stderr.write(f"Found {len(extension_configs)} extension config files\n")

        repo_root = Path(__file__).parent.parent
        oarepo_config_dir = repo_root / "oarepo_config"

        sys.stderr.write(f"Analyzing oarepo_config functions in {oarepo_config_dir}...\n")
        oarepo_function_vars = analyze_oarepo_config_functions(oarepo_config_dir)
        unique_functions = {f["function"] for vars_list in oarepo_function_vars.values() for f in vars_list}
        sys.stderr.write(
            f"Found {len(oarepo_function_vars)} variables referenced across {len(unique_functions)} functions\n"
        )

        sys.stderr.write("Generating markdown...\n")
        markdown = generate_markdown(app, extension_configs, oarepo_function_vars)

        output_file = repo_root / "docs" / "variables.md"
        output_file.write_text(markdown, encoding="utf-8")

        sys.stderr.write(f"Documentation written to {output_file}\n")


if __name__ == "__main__":
    main()
