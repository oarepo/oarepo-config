#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for the Jobs feature."""

from __future__ import annotations

from typing import Any

from oarepo.config.base import set_constants_in_caller


def configure_jobs(
    permission_policy: str | type | None = None,
    logging_level: str | None = None,
) -> None:
    """Set up the "Jobs" feature (manually or automatically run administrative tasks).

    Invenio-jobs lets administrators run and monitor maintenance tasks
    (such as re-indexing or fixing up data) from the admin panel, and
    view their logs. This decides who is allowed to view those job logs
    and how detailed the logs are.

    Args:
        permission_policy: Who is allowed to view job logs. By default,
            only administrators can. Pass your own permission policy
            class (or its import path as a string) to change this.
        logging_level: How detailed the job logs should be, e.g.
            ``"DEBUG"``, ``"INFO"`` (the default), ``"WARNING"``.

    Invenio configuration variables set:

    * ``APP_LOGS_PERMISSION_POLICY`` - the ``permission_policy`` above.
    * ``JOBS_LOGGING_LEVEL`` - the ``logging_level`` above.

    Example:
    ```python
    config.configure_jobs()
    # or with custom settings:
    config.configure_jobs(
        permission_policy="my_package:policies:MyJobPolicy",
        logging_level="DEBUG",
    )
    ```

    """
    from invenio_jobs.services.permissions import (
        JobLogsPermissionPolicy as InvenioJobLogsPermissionPolicy,
    )
    from oarepo_runtime.services.generators import AdministrationWithQueryFilter

    class JobLogsPermissionPolicy(InvenioJobLogsPermissionPolicy):
        """Permission policy for job logs."""

        can_read: tuple[Any] = (AdministrationWithQueryFilter(),)

    # invenio-jobs configuration
    APP_LOGS_PERMISSION_POLICY = permission_policy or JobLogsPermissionPolicy
    JOBS_LOGGING_LEVEL = logging_level or "INFO"
    set_constants_in_caller(locals())
