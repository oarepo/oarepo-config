#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""OARepo application workflow configuration package."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ...base import get_constant_from_caller, set_constants_in_caller
from ...requests import RequestsPermissionPolicy
from .base import BaseWorkflowSettings, add_if_in_state

if TYPE_CHECKING:
    from oarepo_workflows import Workflow

from .community import CommunityWorkflow
from .individual import IndividualWorkflow


def configure_workflows(
    *workflow_definitions: BaseWorkflowSettings,
    default_individual_workflow: str = "individual",
    default_community_workflow: str = "community",
    context: dict | None = None,
) -> list[Workflow]:
    """Set up workflows based on the provided workflow definitions.

    This function is intended to be called from within invenio.cfg and will create
    a "WORKFLOWS" entry in the invenio.cfg context (in the caller's globals).

    Example:

        .. code-block:: python

            # invenio.cfg
            from oarepo_app.config import (
                configure_workflows,
                IndividualWorkflow,
                CommunityWorkflow,
            )

            configure_workflows(
                IndividualWorkflow(
                    authenticated_draft_creation=False,
                    review_required=True,
                    publish_without_review=False,
                ),
                CommunityWorkflow(),
            )
            # no need to assign the result to WORKFLOWS, that is done automatically


    If the workflow definitions are empty, a permissive IndividualWorkflow will be created
    (authenticated draft creation, publish without review allowed).

    If there is no IndividualWorkflow definition in the workflow definitions (but there are other workflow types), a
    restricted IndividualWorkflow (no deposition allowed) will be created with default settings.

    The default_individual_workflow parameter should be the code of the workflow to use
    as the default one for individual deposits, where no community is involved and the
    workflow code is not provided by the caller.

    If the context is provided, the "WORKFLOWS" entry will be added to it instead of
    the caller's globals.

    See https://nrp-cz.github.io/docs/customize/workflows for more information on how to customize the workflows.

    """
    if not workflow_definitions:
        workflow_definitions = (
            IndividualWorkflow(
                code=default_individual_workflow,
                authenticated_draft_creation=True,
                review_required=False,
                publish_without_review=True,
            ),
        )
    elif not any(isinstance(workflow, IndividualWorkflow) for workflow in workflow_definitions):
        workflow_definitions = (
            *workflow_definitions,
            IndividualWorkflow(
                code=default_individual_workflow,
                authenticated_draft_creation=False,
                review_required=False,
                publish_without_review=False,
            ),
        )
    built_workflows = [workflow.build_workflow() for workflow in workflow_definitions]
    if not any(workflow.code == default_individual_workflow for workflow in workflow_definitions):
        raise ValueError(f"No workflow with code '{default_individual_workflow}' found in workflow definitions")
    # check for duplicated codes
    if len(workflow_definitions) != len({workflow.code for workflow in workflow_definitions}):
        raise ValueError("Duplicate workflow codes found in workflow definitions")

    constants: dict[str, Any] = {
        "WORKFLOWS": built_workflows,
        "WORKFLOWS_DEFAULT_WORKFLOW": default_individual_workflow,
        "OAREPO_COMMUNITIES_DEFAULT_WORKFLOW": default_community_workflow,
    }

    # Default the requests permission policy to the one that also allows creating
    # community-topic request types (membership / invitation / sub-community), which
    # otherwise cannot resolve a workflow and are always denied. Respect an explicit
    # REQUESTS_PERMISSION_POLICY set by the caller.
    if RequestsPermissionPolicy is not None:
        if context:
            constants["REQUESTS_PERMISSION_POLICY"] = context.get(
                "REQUESTS_PERMISSION_POLICY", RequestsPermissionPolicy
            )
        else:
            constants["REQUESTS_PERMISSION_POLICY"] = get_constant_from_caller(
                "REQUESTS_PERMISSION_POLICY", RequestsPermissionPolicy
            )

    if context:
        context.update(constants)
    else:
        set_constants_in_caller(constants)
    return built_workflows


__all__ = [
    "BaseWorkflowSettings",
    "CommunityWorkflow",
    "IndividualWorkflow",
    "add_if_in_state",
    "configure_workflows",
]
