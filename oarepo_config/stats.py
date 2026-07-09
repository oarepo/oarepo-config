#!/usr/bin/env python3
#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-rdm (see https://github.com/oarepo/oarepo-rdm).
#
# oarepo is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for invenio-stats module."""

from __future__ import annotations

from .base import set_constants_in_caller

# Invenio-Stats
# =============
# See https://invenio-stats.readthedocs.io/en/latest/configuration.html
#     https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L120


def configure_stats(
    enable: bool = True,
) -> None:
    """Set up usage statistics (record views, downloads, etc.).

    Enables the collection and aggregation of usage events, such as how
    many times a record was viewed or a file was downloaded, so this
    data can later be shown to users and curators.

    Args:
        enable: Set to ``False`` to turn off collecting new usage
            statistics events (for example on a staging/test instance).
            Defaults to ``True``.

    Invenio configuration variables set:

    * ``STATS_REGISTER_RECEIVERS`` - the ``enable`` argument above.
    * ``STATS_EVENTS``, ``STATS_AGGREGATIONS``, ``STATS_QUERIES``,
      ``STATS_PERMISSION_FACTORY`` - always set to ``invenio-app-rdm``'s
      defaults, regardless of ``enable``.

    Example:
    ```python
    config.configure_stats()
    # or on a test instance:
    config.configure_stats(enable=False)
    ```

    """
    STATS_REGISTER_RECEIVERS = enable

    set_constants_in_caller(locals())
