#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Sphinx configuration for the oarepo-config API documentation."""

from __future__ import annotations

import sys
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as get_version
from pathlib import Path

# Make sure the package can be imported even if it was not pip-installed
# (e.g. when running sphinx-build directly against a checkout).
sys.path.insert(0, str(Path("..").resolve()))

# -- Project information -----------------------------------------------

project = "oarepo-config"
copyright = "2026, CESNET z.s.p.o."  # noqa: A001
author = "CESNET z.s.p.o."

try:
    release = get_version("oarepo-config")
except PackageNotFoundError:
    release = "0.0.0"
version = release

# -- General configuration -----------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # understands the Google-style docstrings used in this package
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "myst_parser",  # lets docs/index.md include the Markdown README
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# README.md (included as docs/index.md) uses GitHub-style "[text](#heading)"
# links between its own sections. This makes MyST auto-generate a matching
# heading-anchor for every section (up to h4), so those links resolve here
# as well as they do on GitHub.
myst_heading_anchors = 4

master_doc = "index"

# -- Napoleon (Google-style docstrings) -----------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_use_ivar = True

# -- Autodoc ---------------------------------------------------------------

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# oarepo_config functions do most of their heavy imports (Invenio/OARepo
# submodules) lazily, inside the function body, specifically so that this
# module can be imported - and documented - without every optional
# dependency installed. If autodoc still fails to import an optional
# integration, add its top-level package name here to have it mocked out
# instead of failing the whole documentation build.
autodoc_mock_imports: list[str] = []

# -- Intersphinx -------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- HTML output -------------------------------------------------------

html_theme = "furo"
html_title = f"{project} {version}"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
