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
import importlib
import inspect
import os
import sys
from collections import defaultdict
from pathlib import Path


def load_flask_app():
    """Load the Flask application to access its configuration."""
    try:
        from invenio_app.factory import create_app

        app = create_app()
        return app
    except Exception as e:
        print(f"Warning: Could not load Flask app: {e}", file=sys.stderr)
        print("Using empty config as fallback.", file=sys.stderr)
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
            if item.is_dir() and (
                item.name.startswith("invenio_") or item.name.startswith("oarepo_")
            ):
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
    except Exception as e:
        print(f"Warning: Could not scan site-packages: {e}", file=sys.stderr)

    return config_modules


def extract_config_variables_from_file(file_path):
    """Extract configuration variables and their docstrings from a config file using AST.

    Looks for:
    - Module-level assignments with uppercase variable names
    - Docstrings (triple-quoted strings) following the assignment
    - Inline comments after assignments
    """
    variables = {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source)
        lines = source.split("\n")

        # Build a map of line numbers to nodes for easier lookup
        node_by_line = {}
        for node in ast.walk(tree):
            if hasattr(node, "lineno"):
                node_by_line[node.lineno] = node

        for node in ast.walk(tree):
            # Look for assignments at module level
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.isupper():
                        var_name = target.id
                        docstring = None

                        # Get value representation
                        try:
                            value_repr = (
                                ast.unparse(node.value)
                                if hasattr(ast, "unparse")
                                else repr(node.value)
                            )
                            if len(value_repr) > 100:
                                value_repr = value_repr[:100] + "..."
                        except Exception:
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
                            if line.startswith('"""') or line.startswith("'''"):
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
                                    docstring = " ".join(docstring_lines).strip()
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
                        }

    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}", file=sys.stderr)

    return variables


def analyze_oarepo_config_functions(oarepo_config_dir):
    """Analyze oarepo_config/* modules to find which variables are referenced in each function."""
    function_variables = defaultdict(
        list
    )  # function_name -> list of (variable_name, docstring)

    oarepo_config_path = Path(oarepo_config_dir)

    if not oarepo_config_path.exists():
        print(
            f"Warning: oarepo_config directory not found at {oarepo_config_path}",
            file=sys.stderr,
        )
        return function_variables

    # Get all Python files in oarepo_config (excluding __init__.py and __pycache__)
    py_files = list(oarepo_config_path.glob("*.py"))

    for py_file in py_files:
        if py_file.name.startswith("__"):
            continue

        try:
            with open(py_file, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

            # Find all functions that start with configure_ or initialize_
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if node.name.startswith(
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
                                    if (
                                        isinstance(target, ast.Name)
                                        and target.id.isupper()
                                    ):
                                        func_vars.add(target.id)

                            # Also look for references to uppercase variables (not just assignments)
                            elif isinstance(stmt, ast.Name):
                                if stmt.id.isupper() and stmt.id not in [
                                    "locals",
                                    "globals",
                                    "dict",
                                    "list",
                                    "str",
                                    "int",
                                    "float",
                                    "bool",
                                ]:
                                    # Check if it's being used (not just defined)
                                    func_vars.add(stmt.id)

                        # Get docstring for each variable from the function's docstring
                        # We'll extract variable names mentioned in the docstring under "Invenio configuration variables set:"
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

                                    matches = re.findall(
                                        r"`(`?[A-Z_][A-Z0-9_]*`?)`", line
                                    )
                                    for match in matches:
                                        var_name = match.strip("`")
                                        if var_name.isupper():
                                            func_vars.add(var_name)

                        # Store the function with its variables
                        for var_name in func_vars:
                            function_variables[var_name].append(
                                {
                                    "function": func_name,
                                    "file": py_file.name,
                                    "docstring": docstring[:500] + "..."
                                    if len(docstring) > 500
                                    else docstring,
                                }
                            )

        except Exception as e:
            print(f"Warning: Could not analyze {py_file}: {e}", file=sys.stderr)

    return function_variables


def generate_markdown(app, extension_configs, oarepo_function_vars):
    """Generate the markdown documentation."""
    lines = []

    lines.append("# Configuration Variables Reference\n")
    lines.append(
        "This document lists all configuration variables used by oarepo-config and related extensions.\n"
    )
    lines.append("It is automatically generated from:\n")
    lines.append(
        "- The Flask application's configuration (via `invenio_app.factory.create_app()`)\n"
    )
    lines.append("- The docstrings in `oarepo_config/*` modules\n")
    lines.append(
        "- Configuration files from installed invenio_ and oarepo_ extensions\n"
    )
    lines.append("\n")
    lines.append("## How to Use This Document\n")
    lines.append("\n")
    lines.append(
        "1. **Summary Table**: Quickly find which configure_* functions set each variable.\n"
    )
    lines.append(
        "2. **Detailed Reference**: For each variable, see its default value, type, source, and which configure_* functions reference it.\n"
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
                if not callable(value) and not isinstance(
                    value, (type, dict, list, tuple, set)
                ):
                    all_variables[key] = {
                        "value": repr(value)[:100] + "..."
                        if len(repr(value)) > 100
                        else repr(value),
                        "type": type(value).__name__,
                        "docstring": None,
                        "source": "app.config",
                    }
                elif isinstance(value, (dict, list, tuple, set)):
                    all_variables[key] = {
                        "value": f"<{type(value).__name__}>",
                        "type": type(value).__name__,
                        "docstring": None,
                        "source": "app.config",
                    }

    # Add variables from extension config files
    for package_name, info in extension_configs.items():
        file_vars = extract_config_variables_from_file(info["path"])
        for var_name, var_info in file_vars.items():
            if var_name not in all_variables:
                all_variables[var_name] = {
                    "value": var_info.get("value", ""),
                    "type": "unknown",
                    "docstring": var_info.get("docstring"),
                    "source": info["path"],
                }
            else:
                # If the variable already exists (from app.config),
                # update it with the docstring from the config file if available
                if var_info.get("docstring") and not all_variables[var_name].get(
                    "docstring"
                ):
                    all_variables[var_name]["docstring"] = var_info["docstring"]
                    # Also update source to indicate it comes from extension config
                    if all_variables[var_name].get("source") == "app.config":
                        all_variables[var_name]["source"] = (
                            f"{info['path']} (via app.config)"
                        )

    # Merge with oarepo_config function references
    variables_with_functions = defaultdict(list)
    for var_name, funcs in oarepo_function_vars.items():
        variables_with_functions[var_name].extend(funcs)
        if var_name not in all_variables:
            all_variables[var_name] = {
                "value": "",
                "type": "configured by function",
                "docstring": None,
                "source": "oarepo_config",
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
        lines.append(f"| `{var_name}` | {var_type} | {ref_names} |\n")

    # Generate detailed sections
    lines.append("\n## Detailed Variable Reference\n")

    for var_name in sorted(all_variables.keys()):
        var_info = all_variables[var_name]
        ref_funcs = variables_with_functions.get(var_name, [])

        lines.append(f"### `{var_name}`\n")

        # Build table rows without header
        table_rows = []

        # Description (if available)
        if var_info.get("docstring"):
            docstring = var_info["docstring"].replace("|", "\\|").replace("\n", " ")
            if len(docstring) > 100:
                docstring = docstring[:100] + "..."
            table_rows.append(f"| **Description** | {docstring} |")

        # Default Value (if available and not empty)
        if var_info.get("value"):
            value = var_info["value"].replace("|", "\\|")
            table_rows.append(f"| **Default Value** | `{value}` |")

        # Type
        if var_info.get("type"):
            table_rows.append(f"| **Type** | {var_info['type']} |")

        # Source
        if var_info.get("source"):
            source = var_info["source"].replace("|", "\\|")
            table_rows.append(f"| **Source** | {source} |")

        # Add table with separator after first row
        if table_rows:
            lines.append(table_rows[0] + "\n")
            lines.append("|--------------|-----------|\n")
            for row in table_rows[1:]:
                lines.append(row + "\n")
            lines.append("\n")

        # Referencing functions
        if ref_funcs:
            lines.append("**Set/Referenced by:**\n")
            seen_funcs = set()
            for func in ref_funcs:
                if func["function"] not in seen_funcs:
                    seen_funcs.add(func["function"])
                    lines.append(f"- [`{func['function']}`](#) in `{func['file']}`\n")
                    if func.get("docstring"):
                        doc = func["docstring"].replace("\n", " ").strip()
                        if len(doc) > 200:
                            doc = doc[:200] + "..."
                        # Escape pipe characters
                        doc = doc.replace("|", "\\|")
                        lines.append(f"  > {doc}\n")

        lines.append("---\n\n")

    return "".join(lines)


def main():
    """Main entry point."""
    print("Loading Flask application...", file=sys.stderr)
    app = load_flask_app()

    print("Getting extension configurations...", file=sys.stderr)
    extension_configs = get_extension_configs(app)
    print(f"Found {len(extension_configs)} extension config files", file=sys.stderr)

    # Determine oarepo_config directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    oarepo_config_dir = repo_root / "oarepo_config"

    print(
        f"Analyzing oarepo_config functions in {oarepo_config_dir}...", file=sys.stderr
    )
    oarepo_function_vars = analyze_oarepo_config_functions(oarepo_config_dir)
    print(
        f"Found {len(oarepo_function_vars)} variables referenced across {len(set(f['function'] for vars in oarepo_function_vars.values() for f in vars))} functions",
        file=sys.stderr,
    )

    print("Generating markdown...", file=sys.stderr)
    markdown = generate_markdown(app, extension_configs, oarepo_function_vars)

    output_file = script_dir / "variables.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Documentation written to {output_file}", file=sys.stderr)


if __name__ == "__main__":
    main()
