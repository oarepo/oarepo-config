#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Initial configuration module."""

from __future__ import annotations

"""This module provides initial configuration for OARepo-based repositories.
It is registered as invenio_config.module entrypoint so is loaded early in
the application initialization. This allows other modules to access/modify its
configuration options.
"""

THEME_FRONTPAGE = False
"""Enable frontpage theme."""
