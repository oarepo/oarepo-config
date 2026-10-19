# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Tests for the simplified community workflow configuration."""

from __future__ import annotations

from invenio_rdm_records.requests.access.requests import UserAccessRequest
from invenio_rdm_records.requests.community_submission import CommunitySubmission
from invenio_rdm_records.requests.file_modification import FileModification
from invenio_rdm_records.requests.quota_increase import QuotaIncrease
from invenio_rdm_records.services.generators import RecordCommunitiesAction
from invenio_records_permissions.generators import AuthenticatedUser
from oarepo_communities.services.permissions.generators import CommunityRole, InAnyCommunity
from oarepo_requests.types import (
    PublishChangedMetadataRequestType,
    PublishNewVersionRequestType,
)

from oarepo_config.workflows.simplified.community import CommunityWorkflow


def test_create():
    """Draft creation gets one community constraint for each configured role."""
    workflow = CommunityWorkflow(
        authenticated_draft_creation=True,
        draft_creation_community_roles=["submitter", "reviewer"],
    )

    generators = workflow._build_record_create_generators()

    assert len(generators) == 3
    assert isinstance(generators[0], AuthenticatedUser)
    assert all(isinstance(generator, InAnyCommunity) for generator in generators[1:])


def test_replace():
    """Only the configured roles replace broad community access."""
    workflow = CommunityWorkflow()

    permissions = workflow._replace_communities_action_with_roles(
        [AuthenticatedUser(), RecordCommunitiesAction("view")],
        ["curator", "owner"],
    )

    assert not any(isinstance(generator, RecordCommunitiesAction) for generator in permissions)
    assert isinstance(permissions[0], AuthenticatedUser)
    assert [type(generator) for generator in permissions[1:]] == [CommunityRole, CommunityRole]


def test_roles():
    """View, preview and manage actions each use their own role settings."""
    workflow = CommunityWorkflow(
        read_restricted_community_roles=["reader"],
        read_draft_community_roles=["reviewer"],
        record_manage_community_roles=["owner", "curator"],
    )
    original_permissions = [AuthenticatedUser(), RecordCommunitiesAction("view")]

    view_permissions = workflow._build_record_rdm_view_permissions(original_permissions)
    preview_permissions = workflow._build_record_rdm_preview_generators(original_permissions)
    manage_permissions = workflow._build_record_rdm_manage_generators(original_permissions)

    assert [type(generator) for generator in view_permissions] == [AuthenticatedUser, CommunityRole]
    assert [type(generator) for generator in preview_permissions] == [AuthenticatedUser, CommunityRole]
    assert [type(generator) for generator in manage_permissions] == [
        AuthenticatedUser,
        CommunityRole,
        CommunityRole,
    ]


def test_requests():
    """The generated request policy exposes all supported workflow requests."""
    workflow = CommunityWorkflow()

    request_policy = workflow._build_request_policy()

    for request_type in (
        FileModification.type_id,
        QuotaIncrease.type_id,
        CommunitySubmission.type_id,
        PublishChangedMetadataRequestType.type_id,
        PublishNewVersionRequestType.type_id,
        UserAccessRequest.type_id,
    ):
        request = getattr(request_policy, request_type)
        assert request.requesters

    submission = getattr(request_policy, CommunitySubmission.type_id)
    assert submission.recipients
    assert submission.transitions.submitted == "submitted"
    assert submission.transitions.accepted == "published"
    assert submission.transitions.declined == "review_requested"


def test_workflow():
    """The public builder combines generated policies into a workflow."""
    workflow_settings = CommunityWorkflow(code="community-review")

    permission_policy = workflow_settings._build_permission_policy()
    workflow = workflow_settings.build_workflow()

    assert len(permission_policy.can_create) == 3
    assert workflow.code == "community-review"
    assert workflow.permission_policy_cls is not None
    assert workflow.request_policy_cls is not None
