#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for i18n."""

from __future__ import annotations


def initialize_i18n() -> None:
    """Enable translated validation error messages.

    Makes sure that when a user submits invalid data (for example, a
    required field is missing), the error message shown to them is
    translated into their chosen language instead of always being shown
    in English. Takes no parameters; call it once, near the top of
    ``invenio.cfg``.

    Invenio configuration variables set: none - this only patches
    Marshmallow's error-message machinery in memory.

    Example:
    ```python
    config.initialize_i18n()
    ```

    """
    from flask_babel import lazy_gettext as _
    from marshmallow_i18n_messages import add_i18n_to_marshmallow

    add_i18n_to_marshmallow(_)
