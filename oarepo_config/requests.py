#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Requests permission policy for oarepo-config.

By default oarepo-workflows replaces invenio's request-create permission with a
workflow-driven one (``CreatorsFromWorkflowRequestsPermissionPolicy`` -> the
``FromRecordWorkflow`` generator), which resolves the governing workflow from the
request topic's ``parent.workflow``. That works for record-topic requests (publish,
new version, secondary-community submission, ...), but a handful of core
invenio/RDM request types have a *community* as their topic:

* ``community-membership-request`` (a user asks to join a community)
* ``community-invitation`` (a community invites a user)
* ``subcommunity`` (a community asks to become a sub-community of another)
* ``subcommunity-invitation`` (a community invites another as its sub-community)

A community has no ``parent.workflow`` (its workflow lives in
``custom_fields.workflow``), so ``FromRecordWorkflow`` can never resolve a workflow
for these and their creation is *always* denied. These request types already gate
themselves in their own services (e.g. the members service's ``request_membership``
/ ``members_invite`` checks), so for them we fall back to invenio's default
behaviour -- any authenticated user may create the request -- while every other
(record-topic) request type keeps the workflow-driven check unchanged.
"""

from __future__ import annotations

# Core invenio/RDM request types whose topic is a community (not a
# workflow-governed record) and which gate creation in their own service layer.
COMMUNITY_TOPIC_REQUEST_TYPES = frozenset(
    {
        "community-membership-request",
        "community-invitation",
        "subcommunity",
        "subcommunity-invitation",
    }
)

try:
    from invenio_records_permissions.generators import (
        AuthenticatedUser,
        ConditionalGenerator,
    )
    from oarepo_workflows.requests.permissions import (
        CreatorsFromWorkflowRequestsPermissionPolicy,
    )

    class IfRequestType(ConditionalGenerator):
        """Choose generators based on the ``type_id`` of the request being created."""

        def __init__(self, type_ids: frozenset[str], then_: list, else_: list) -> None:
            """Store the matching type ids and the two generator branches."""
            self.type_ids = frozenset(type_ids)
            super().__init__(then_=then_, else_=else_)

        def _condition(self, request_type=None, **kwargs) -> bool:  # type: ignore[no-untyped-def]  # noqa: ANN001, ANN003, ARG002
            """Return True when the request being created is one of ``type_ids``."""
            return request_type is not None and request_type.type_id in self.type_ids

    class RequestsPermissionPolicy(CreatorsFromWorkflowRequestsPermissionPolicy):
        """Requests permission policy that also allows community-topic requests.

        Extends the workflow-based policy so the four community-topic request
        types (which have no resolvable workflow) can still be created.
        """

        # For community-topic types, mirror invenio's default (AuthenticatedUser);
        # for everything else, defer to the parent policy verbatim (so we inherit
        # whatever it defines instead of duplicating it).
        can_create = (
            IfRequestType(
                COMMUNITY_TOPIC_REQUEST_TYPES,
                then_=[AuthenticatedUser()],
                else_=list(CreatorsFromWorkflowRequestsPermissionPolicy.can_create),
            ),
        )

except ImportError:
    # oarepo_workflows / oarepo_requests not installed; nothing to configure.
    RequestsPermissionPolicy = None  # type: ignore[assignment,misc]
