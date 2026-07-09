#!/usr/bin/env python3
"""Generate variables.md documentation from oarepo-config functions and Flask app config.

This script:
1. Loads a Flask app to get all configuration variables
2. Analyzes oarepo_config/* modules to find which configure_* functions reference which variables
3. Generates a markdown file with:
   - A summary table of all variables and their referencing functions
   - Alphabetically sorted sections for each variable with docstrings and references

Usage:
    python mkvars.py

The output is written to docs/variables.md in the same directory as this script.
"""

import ast
import sys
from collections import defaultdict
from pathlib import Path


def load_flask_app():
    """Load the Flask application to access its configuration."""
    try:
        from invenio_app.factory import create_app

        return create_app()
    except OSError as e:
        sys.stderr.write(f"Warning: Could not load Flask app: {e}\n")
        sys.stderr.write("Using empty config as fallback.\n")
        return None


def get_extension_configs(app):
    """Get all configuration modules from installed extensions.

    Looks for invenio_ and oarepo_ packages with config.py or initial_config.py files.
    """
    config_modules = {}

    if app is None:
        return config_modules

    # Get the site-packages directory from the Flask app's path
    try:
        import inspect
        from pathlib import Path

        # Get a known module path to find site-packages
        import flask

        flask_path = Path(inspect.getfile(flask)).parent
        # Navigate up to site-packages
        site_packages = flask_path.parent

        # Scan for invenio_ and oarepo_ directories
        for item in site_packages.iterdir():
            if item.is_dir() and (item.name.startswith("invenio_") or item.name.startswith("oarepo_")):
                package_name = item.name

                # Check for config.py
                config_py = item / "config.py"
                if config_py.exists():
                    config_modules[package_name] = {
                        "path": str(config_py),
                        "type": "config.py",
                    }

                # Check for initial_config.py
                initial_config_py = item / "initial_config.py"
                if initial_config_py.exists():
                    config_modules[package_name] = {
                        "path": str(initial_config_py),
                        "type": "initial_config.py",
                    }
    except OSError as e:
        sys.stderr.write(f"Warning: Could not scan site-packages: {e}\n")

    return config_modules


def extract_config_variables_from_file(file_path):  # noqa: C901
    """Extract configuration variables and their docstrings from a config file using AST.

    Looks for:
    - Module-level assignments with uppercase variable names
    - Docstrings (triple-quoted strings) following the assignment
    - Inline comments after assignments
    - Line numbers where variables are defined
    """
    variables = {}

    try:
        with Path(file_path).open(encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source)
        lines = source.split("\n")

        for node in ast.walk(tree):
            # Look for assignments at module level
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.isupper():
                        var_name = target.id
                        docstring = None
                        line_number = node.lineno

                        # Get value representation
                        try:
                            value_repr = ast.unparse(node.value) if hasattr(ast, "unparse") else repr(node.value)
                            if len(value_repr) > 100:
                                value_repr = value_repr[:100] + "..."
                        except OSError:
                            value_repr = "<value>"

                        # Look for docstring on following lines
                        line_num = node.lineno - 1

                        # Check if next non-empty line is a string literal (docstring)
                        for i in range(line_num + 1, min(line_num + 10, len(lines))):
                            line = lines[i].strip()

                            # Skip empty lines and comments
                            if not line or line.startswith("#"):
                                continue

                            # Check for triple-quoted string
                            if line.startswith(('"""', "'''")):
                                quote = line[:3]
                                # Check if it's a single-line docstring
                                if line.count(quote) >= 2 and len(line) > 6:
                                    docstring = line[3:-3].strip()
                                else:
                                    # Multi-line docstring
                                    docstring_lines = []
                                    if len(line) > 3:
                                        docstring_lines.append(line[3:])
                                    for j in range(i + 1, len(lines)):
                                        if quote in lines[j]:
                                            end_idx = lines[j].index(quote)
                                            docstring_lines.append(lines[j][:end_idx])
                                            break
                                        docstring_lines.append(lines[j])
                                    # Keep original line breaks/indentation - these
                                    # docstrings are reST (directives, code-blocks,
                                    # ...) and need it to parse correctly later.
                                    docstring = "\n".join(docstring_lines).strip()
                                break

                            # If we hit any other code, stop looking
                            break

                        # Also check for inline comment on the same line
                        if docstring is None:
                            assign_line = lines[line_num]
                            if "#" in assign_line:
                                comment_start = assign_line.index("#")
                                comment = assign_line[comment_start + 1 :].strip()
                                if comment:
                                    docstring = comment

                        variables[var_name] = {
                            "docstring": docstring,
                            "file": str(file_path),
                            "value": value_repr,
                            "line": line_number,
                        }

    except OSError as e:
        sys.stderr.write(f"Warning: Could not parse {file_path}: {e}\n")

    return variables


def convert_path_to_github_link(file_path, line_number):
    """Convert a file path to a GitHub link.

    For invenio_* packages: https://github.com/inveniosoftware/{package}/blob/master/{relative_path}#L{line}
    For oarepo_* packages: https://github.com/oarepo/{package}/blob/master/{relative_path}#L{line}
    For other paths: return as-is with line number
    """
    from pathlib import Path

    path = Path(file_path)

    # Check if it's an invenio_ package
    if path.parent.name.startswith("invenio_"):
        package_name = path.parent.name
        # Convert underscore to dash for GitHub repo name
        repo_name = package_name.replace("_", "-")
        relative_path = path.name
        link_template = (
            f"[{repo_name}]({{base_url}}/{repo_name}/blob/master/{package_name}/{relative_path}#L{line_number})"
        )
        return link_template.replace("{base_url}", "https://github.com/inveniosoftware")

    # Check if it's an oarepo_ package
    if path.parent.name.startswith("oarepo_"):
        package_name = path.parent.name
        # Convert underscore to dash for GitHub repo name
        repo_name = package_name.replace("_", "-")
        relative_path = path.name
        return f"[{repo_name}](https://github.com/oarepo/{repo_name}/blob/master/{package_name}/{relative_path}#L{line_number})"

    # For other paths, just show the filename with line number
    return f"{path.name} (line {line_number})"


def analyze_oarepo_config_functions(oarepo_config_dir):  # noqa: C901
    """Analyze oarepo_config/* modules to find which variables are referenced in each function."""
    function_variables = defaultdict(list)  # function_name -> list of (variable_name, docstring)

    oarepo_config_path = Path(oarepo_config_dir)

    if not oarepo_config_path.exists():
        sys.stderr.write(f"Warning: oarepo_config directory not found at {oarepo_config_path}\n")
        return function_variables

    # Get all Python files in oarepo_config (excluding __init__.py and __pycache__)
    py_files = list(oarepo_config_path.glob("*.py"))

    for py_file in py_files:
        if py_file.name.startswith("__"):
            continue

        try:
            with Path(py_file).open(encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

            # Find all top-level configure/register-style functions (e.g.
            # configure_ui, initialize_i18n, register_workflow, add_model)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name.startswith(
                    ("configure_", "initialize_", "register_", "add_")
                ):
                    func_name = node.name

                    # Extract docstring
                    docstring = ast.get_docstring(node) or ""

                    # Find all uppercase variable assignments in this function
                    func_vars = set()
                    for stmt in ast.walk(node):
                        if isinstance(stmt, ast.Assign):
                            for target in stmt.targets:
                                if isinstance(target, ast.Name) and target.id.isupper():
                                    func_vars.add(target.id)

                        # Also look for references to uppercase variables (not just assignments)
                        elif (
                            isinstance(stmt, ast.Name)
                            and stmt.id.isupper()
                            and stmt.id
                            not in (
                                "locals",
                                "globals",
                                "dict",
                                "list",
                                "str",
                                "int",
                                "float",
                                "bool",
                            )
                        ):
                            # Check if it's being used (not just defined)
                            func_vars.add(stmt.id)

                    # Get docstring for each variable from the function's docstring
                    # We'll extract variable names mentioned under "Invenio configuration variables set:"
                    if "Invenio configuration variables set:" in docstring:
                        # Parse the docstring to find variable names
                        lines = docstring.split("\n")
                        in_vars_section = False
                        for line in lines:
                            if "Invenio configuration variables set:" in line:
                                in_vars_section = True
                                continue

                            if in_vars_section:
                                if (
                                    line.strip()
                                    and not line.startswith(" ")
                                    and not line.startswith("\t")
                                    and ":" not in line
                                ):
                                    # End of section
                                    break

                                # Look for variable names (uppercase with backticks)
                                import re

                                matches = re.findall(r"`(`?[A-Z_][A-Z0-9_]*`?)`", line)
                                for match in matches:
                                    var_name = match.strip("`")
                                    if var_name.isupper():
                                        func_vars.add(var_name)

                    # Store the function with its variables
                    for var_name in func_vars:
                        function_variables[var_name].append(
                            {
                                "function": func_name,
                                "file": str(py_file),
                                "line": node.lineno,
                                "docstring": docstring[:500] + "..." if len(docstring) > 500 else docstring,
                            }
                        )

        except OSError as e:
            sys.stderr.write(f"Warning: Could not analyze {py_file}: {e}\n")

    return function_variables


def variable_anchor(var_name):
    """Return the section id Sphinx/docutils will assign to a variable's heading.

    Variable names are plain ``[A-Z0-9_]`` identifiers, so this just mirrors
    docutils' own heading-id slugification (lowercase, underscores to hyphens)
    rather than inventing a separate anchor scheme.
    """
    return var_name.lower().replace("_", "-")


def default_value_label(var_info):
    """Return the "Default Value" row label, naming the package family it comes from."""
    paths = [path for path, _line in var_info.get("sources", [])] or [var_info.get("source")]
    package_names = {Path(path).parent.name for path in paths if path}
    if any(name.startswith("oarepo_") for name in package_names):
        return "OARepo Default Value"
    if any(name.startswith("invenio_") for name in package_names):
        return "Invenio RDM Default Value"
    return "Default Value"


def generate_markdown(app, extension_configs, oarepo_function_vars):  # noqa: C901
    """Generate the markdown documentation."""
    lines = []

    lines.append("# Configuration Variables Reference\n")
    lines.append("This document lists all configuration variables used by oarepo-config and related extensions.\n")
    lines.append("It is automatically generated from:\n")
    lines.append("- The Flask application's configuration (via `invenio_app.factory.create_app()`)\n")
    lines.append("- The docstrings in `oarepo_config/*` modules\n")
    lines.append("- Configuration files from installed invenio_ and oarepo_ extensions\n")
    lines.append("\n")
    lines.append("## How to Use This Document\n")
    lines.append("\n")
    lines.append("1. **Summary Table**: Quickly find which configure_* functions set each variable.\n")
    lines.append(
        "2. **Detailed Reference**: For each variable, see its default value, type, source, and which"
        " configure_* functions reference it.\n"
    )
    lines.append("\n")
    lines.append("---\n")
    lines.append("\n")

    # Collect all variables from app.config
    all_variables = {}

    if app:
        # Get all uppercase config keys from the app
        for key in sorted(app.config.keys()):
            if key.isupper() and not key.startswith("_"):
                value = app.config[key]
                # Skip complex objects that can't be easily represented
                if not callable(value) and not isinstance(value, (type, dict, list, tuple, set)):
                    all_variables[key] = {
                        "value": repr(value)[:100] + "..." if len(repr(value)) > 100 else repr(value),
                        "type": type(value).__name__,
                        "docstring": None,
                        "source": "unknown",
                    }
                elif isinstance(value, (dict, list, tuple, set)):
                    all_variables[key] = {
                        "value": f"<{type(value).__name__}>",
                        "type": type(value).__name__,
                        "docstring": None,
                        "source": "unknown",
                    }

    # Add variables from extension config files
    for info in extension_configs.values():
        file_vars = extract_config_variables_from_file(info["path"])
        for var_name, var_info in file_vars.items():
            if var_name not in all_variables:
                all_variables[var_name] = {
                    "value": var_info.get("value", ""),
                    "type": "unknown",
                    "docstring": var_info.get("docstring"),
                    "source": info["path"],
                    "line": var_info.get("line"),
                    "sources": [(info["path"], var_info.get("line"))],  # Track all sources
                }
            else:
                # If the variable already exists, add this source to the list
                if "sources" not in all_variables[var_name]:
                    # Initialize sources list with the existing source if it's from a file
                    if all_variables[var_name].get("source") and not all_variables[var_name]["source"].startswith("/"):
                        # Source is not a file path (e.g., "unknown"), so don't add it
                        all_variables[var_name]["sources"] = []
                    else:
                        # Source is a file path, add it to the list
                        line = all_variables[var_name].get("line")
                        all_variables[var_name]["sources"] = [(all_variables[var_name]["source"], line)]

                all_variables[var_name]["sources"].append((info["path"], var_info.get("line")))

                # Update docstring if available and not already set
                if var_info.get("docstring") and not all_variables[var_name].get("docstring"):
                    all_variables[var_name]["docstring"] = var_info["docstring"]

                # Update line number if available (use first one found)
                if var_info.get("line") and not all_variables[var_name].get("line"):
                    all_variables[var_name]["line"] = var_info["line"]

                # Update source to the current file (for backward compatibility)
                all_variables[var_name]["source"] = info["path"]

    # Merge with oarepo_config function references
    variables_with_functions = defaultdict(list)
    for var_name, funcs in oarepo_function_vars.items():
        variables_with_functions[var_name].extend(funcs)
        if var_name not in all_variables:
            first_func = funcs[0]
            all_variables[var_name] = {
                "value": "",
                "type": "configured by function",
                "docstring": None,
                "source": first_func["file"],
                "line": first_func.get("line"),
            }

    # Generate summary table
    lines.append("## Summary Table\n")
    lines.append("| Variable Name | Type | Referenced By |\n")
    lines.append("|---------------|------|---------------|\n")

    for var_name in sorted(all_variables.keys()):
        var_info = all_variables[var_name]
        ref_funcs = variables_with_functions.get(var_name, [])
        ref_names = ", ".join(f"`{f['function']}`" for f in ref_funcs[:3])
        if len(ref_funcs) > 3:
            ref_names += f" (+{len(ref_funcs) - 3} more)"
        if not ref_names:
            ref_names = "-"

        var_type = var_info.get("type", "unknown")
        # Create a link from the variable name to its detailed section. This must
        # match the section id Sphinx/docutils auto-generates from the heading
        # below (lowercased, underscores turned into hyphens) - a hand-rolled
        # "<a id=...>" anchor instead of relying on that auto id gets duplicated
        # into the "On this page" sidebar, producing invalid nested <a> tags that
        # silently break those links.
        # Sphinx hard-codes code spans to "white-space: nowrap" (overridden back
        # to wrappable in custom.css), and browsers otherwise never treat "_" as
        # a break opportunity - insert a zero-width space after each one so long
        # names wrap at underscores instead of overflowing the table.
        display_name = var_name.replace("_", "_\u200b")
        lines.append(f"| [`{display_name}`](#{variable_anchor(var_name)}) | {var_type} | {ref_names} |\n")

    # Generate detailed sections
    lines.append("\n## Detailed Variable Reference\n")

    for var_name in sorted(all_variables.keys()):
        var_info = all_variables[var_name]
        ref_funcs = variables_with_functions.get(var_name, [])

        # Star the name if one of our own configure_*/register_*/add_* functions sets it
        star = "*" if ref_funcs else ""
        # Explicit MyST target matching the heading's auto-generated id: without
        # it, MyST can't verify "#anchor" links against its own target registry
        # (only Sphinx/docutils' unrelated auto-id mechanism knows about it) and
        # logs a spurious "cross-reference target not found" warning for every
        # variable, even though the link itself works fine.
        lines.append(f"({variable_anchor(var_name)})=\n")
        # Lead with the star and bold the name for variables one of our own
        # functions sets, so they stand out from the (much larger) set of
        # plain Invenio/extension variables listed here purely for reference.
        heading_name = f"**{star}{var_name}**" if star else var_name
        lines.append(f"### {heading_name}\n")

        # Description as a plain paragraph, not a table row, so it reads
        # like prose instead of being squeezed into a table cell. These
        # docstrings are reST (Sphinx directives, ``code-block``, inline
        # markup, ...), so run them through docutils via an "eval-rst"
        # fence instead of dumping them as inert Markdown text.
        if var_info.get("docstring"):
            docstring = var_info["docstring"].strip()
            lines.append("\n```{eval-rst}\n")
            lines.append(docstring + "\n")
            lines.append("```\n\n")

        # Build table rows without header
        table_rows = []

        # Default Value (if available and not empty)
        if var_info.get("value"):
            value = var_info["value"].replace("|", "\\|")
            label = default_value_label(var_info)
            table_rows.append(f"| **{label}** | `{value}` |")

        # Type
        if var_info.get("type"):
            table_rows.append(f"| **Type** | {var_info['type']} |")

        # Source
        if var_info.get("source"):
            source = var_info["source"]
            # Check if there are multiple sources
            if var_info.get("sources") and len(var_info["sources"]) > 1:
                # Show all sources as GitHub links
                sources_list = []
                for path, line in var_info["sources"]:
                    github_link = convert_path_to_github_link(path, line)
                    sources_list.append(github_link)
                sources_str = "; ".join(sources_list)
                table_rows.append(f"| **Sources** | {sources_str} |")
            elif var_info.get("line"):
                # Single source with line number - convert to GitHub link
                github_link = convert_path_to_github_link(source, var_info["line"])
                table_rows.append(f"| **Source** | {github_link} |")
            else:
                table_rows.append(f"| **Source** | {source.replace('|', '\\|')} |")

        # Set by functions
        if ref_funcs:
            # Get unique function names
            seen_funcs = set()
            func_links = []
            for func in ref_funcs:
                if func["function"] not in seen_funcs:
                    seen_funcs.add(func["function"])
                    # Use a MyST/Sphinx python xref role so this resolves against
                    # the autodoc-generated target regardless of which anchor
                    # Sphinx assigns it (a plain "api.html#..." link doesn't
                    # resolve, since myst only matches its own doctree targets).
                    func_link = f"{{py:func}}`~oarepo_config.{func['function']}`"
                    func_links.append(func_link)
            if func_links:
                funcs_str = ", ".join(func_links)
                table_rows.append(f"| **Set by** | {funcs_str} |")

        # Add table with separator after first row
        if table_rows:
            lines.append(table_rows[0] + "\n")
            lines.append("|--------------|-----------|\n")
            lines.extend(row + "\n" for row in table_rows[1:])
            lines.append("\n---\n\n")
        else:
            # No table rows, just add a blank line and separator
            lines.append("\n---\n\n")

    return "".join(lines)


def main():
    """Run the script to generate documentation."""
    sys.stderr.write("Loading Flask application...\n")
    app = load_flask_app()

    sys.stderr.write("Getting extension configurations...\n")
    extension_configs = get_extension_configs(app)
    sys.stderr.write(f"Found {len(extension_configs)} extension config files\n")

    # Determine oarepo_config directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    oarepo_config_dir = repo_root / "oarepo_config"

    sys.stderr.write(f"Analyzing oarepo_config functions in {oarepo_config_dir}...\n")
    oarepo_function_vars = analyze_oarepo_config_functions(oarepo_config_dir)
    unique_functions = {f["function"] for vars_list in oarepo_function_vars.values() for f in vars_list}
    sys.stderr.write(
        f"Found {len(oarepo_function_vars)} variables referenced across {len(unique_functions)} functions\n"
    )

    sys.stderr.write("Generating markdown...\n")
    markdown = generate_markdown(app, extension_configs, oarepo_function_vars)

    output_file = script_dir / "variables.md"
    output_file.write_text(markdown, encoding="utf-8")

    sys.stderr.write(f"Documentation written to {output_file}\n")


if __name__ == "__main__":
    main()
