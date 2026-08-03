#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for workflows."""

from __future__ import annotations

import inspect
import warnings
from typing import TYPE_CHECKING, Any

from flask_babel import LazyString
from invenio_base.utils import obj_or_import_string
from invenio_i18n import gettext as _

if TYPE_CHECKING:
    try:
        from oarepo_workflows import WorkflowRequestPolicy
        from oarepo_workflows.services.permissions import DefaultWorkflowPermissions
    except ImportError:
        WorkflowRequestPolicy = None  # type: ignore[assignment]
        DefaultWorkflowPermissions = None  # type: ignore[assignment]

    from flask_babel import LazyString
else:
    LazyString = Any  # type: ignore[assignment]

from ..base import get_constant_from_caller, set_constants_in_caller


def register_workflow(
    workflow_code: str,
    workflow_name: str | LazyString,
    permissions_policy: str | type,
    requests_policy: str | type,
    use_low_level_workflows: bool = False,
) -> None:
    """Register a submission/review workflow that records can go through.

    A workflow defines the path a record takes from being created to
    being published - for example, who may create it, whether it needs
    review/approval before publishing, and who may perform each of those
    steps. This adds one such workflow to the repository, so that it can
    be selected when configuring where records may be submitted (e.g. a
    community).

    This is a low-level, single-workflow building block. Repositories
    that use the community-based workflow shape provided by the
    ``oarepo_app`` package typically use its higher-level
    ``configure_workflows(IndividualWorkflow(...), CommunityWorkflow(...))``
    helper instead - see this package's README for the difference.

    Args:
        workflow_code: A short, unique identifier for the workflow, e.g.
            ``"default"``.
        workflow_name: The human-readable name of the workflow, shown to
            users, e.g. ``_("Default workflow")``.
        permissions_policy: Who is allowed to do what with records that
            use this workflow (create, edit, delete, publish, ...). Pass
            either a permissions policy class or its import path as a
            string.
        requests_policy: What review/approval requests are available for
            records using this workflow (e.g. a publish request that
            needs a curator's approval). Pass either a request policy
            class or its import path as a string.
        use_low_level_workflows: Set to ``True`` to silence the warning
            recommending :func:`configure_workflows` instead, for the
            (uncommon) cases that genuinely need this low-level,
            single-workflow API.

    Requires the optional ``oarepo_workflows`` (and, for its defaults,
    ``oarepo_requests``) package to be installed.

    Invenio configuration variables set:

    * ``WORKFLOWS`` - the new workflow is appended; workflows already
      registered (by earlier calls) are kept.
    * ``REQUESTS_PERMISSION_POLICY`` - only if not already set by an
      earlier call; defaults to :class:`oarepo_config.requests.RequestsPermissionPolicy`
      (workflow-based, plus creation of community-topic request types).

    Example:

    .. code-block:: python

        from oarepo_workflows.services.permissions import (
            DefaultWorkflowPermissions,
        )
        from oarepo_requests.services.permissions.workflow_policies import (
            CreatorsFromWorkflowRequestsPermissionPolicy,
        )

        config.register_workflow(
            workflow_code="default",
            workflow_name=_("Default workflow"),
            permissions_policy=DefaultWorkflowPermissions,
            requests_policy=CreatorsFromWorkflowRequestsPermissionPolicy,
        )

    """
    if not use_low_level_workflows:
        warnings.warn(
            "register_workflow() is a low-level, single-workflow building block. "
            "configure_workflows(IndividualWorkflow(...), CommunityWorkflow(...)) is a "
            "simplified solution that should be used instead for the common case. Pass "
            "use_low_level_workflows=True if you intentionally need the low-level API.",
            stacklevel=2,
        )

    try:
        from oarepo_workflows import Workflow, WorkflowRequestPolicy
        from oarepo_workflows.services.permissions import DefaultWorkflowPermissions
    except ImportError as e:
        raise ImportError("oarepo_workflows package is required for workflow registration.") from e

    WORKFLOWS = get_constant_from_caller("WORKFLOWS", [])
    permission_policy_cls = obj_or_import_string(permissions_policy)
    if not (inspect.isclass(permission_policy_cls) and issubclass(permission_policy_cls, DefaultWorkflowPermissions)):
        raise TypeError("permissions_policy must be a subclass of DefaultWorkflowPermissions")

    requests_policy_cls = obj_or_import_string(requests_policy)
    if not (inspect.isclass(requests_policy_cls) and issubclass(requests_policy_cls, WorkflowRequestPolicy)):
        raise TypeError("requests_policy must be a subclass of WorkflowRequestPolicy")

    WORKFLOWS.append(
        Workflow(
            code=workflow_code,
            label=_(workflow_name),
            permission_policy_cls=permission_policy_cls,
            request_policy_cls=requests_policy_cls,
        )
    )
    from ..requests import RequestsPermissionPolicy

    REQUESTS_PERMISSION_POLICY = get_constant_from_caller("REQUESTS_PERMISSION_POLICY", RequestsPermissionPolicy)
    set_constants_in_caller(locals())
