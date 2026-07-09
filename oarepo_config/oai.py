#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for OAI-PMH."""

from __future__ import annotations

from .base import get_constant_from_caller, set_constants_in_caller


def configure_oai() -> None:
    """Set up OAI-PMH, the protocol other systems use to harvest records from this repository.

    OAI-PMH is a standard way for external services (e.g. national
    aggregators, other repositories) to regularly fetch a list of
    published records. This announces the repository's name over that
    protocol, using the name already set via :func:`configure_ui`.

    Takes no parameters. Must be called *after* :func:`configure_ui`,
    since it needs the repository name that function sets up; calling it
    earlier raises an error explaining this.

    Invenio configuration variables set:

    * ``OAISERVER_REPOSITORY_NAME`` - copied from ``REPOSITORY_NAME``
      (set by :func:`configure_ui`).

    Example:

    .. code-block:: python

        config.configure_oai()

    """
    repo_name = get_constant_from_caller("REPOSITORY_NAME")
    if not repo_name:
        raise ValueError("REPOSITORY_NAME must be set, please configure UI before configuring OAI.")
    OAISERVER_REPOSITORY_NAME = str(repo_name)

    set_constants_in_caller(locals())
