#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Community workflow configuration for OARepo."""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

from invenio_rdm_records.requests.community_submission import CommunitySubmission
from invenio_rdm_records.requests.file_modification import FileModification
from invenio_rdm_records.requests.quota_increase import QuotaIncrease
from invenio_rdm_records.services.generators import (
    IfNewRecord,
    RecordCommunitiesAction,
    RecordOwners,
)
from oarepo_communities.services.permissions.generators import (
    CommunityRole,
    InAnyCommunity,
    PrimaryCommunityRole,
)
from oarepo_requests.services.permissions.generators import RequestActive
from oarepo_requests.types import (
    PublishChangedMetadataRequestType,
    PublishNewVersionRequestType,
)
from oarepo_workflows.requests import WorkflowRequest, WorkflowTransitions
from oarepo_workflows.requests.generators.record_owners import RecordOwnersForRecipients
from oarepo_workflows.services.permissions import IfInState, IfRDMRecordPassed
from oarepo_workflows.services.permissions.composite import (
    BooleanPermissionPolicyMixin,
    RequireAll,
)

if TYPE_CHECKING:
    from invenio_records_permissions.generators import Generator
    from invenio_records_permissions.policies.base import BasePermissionPolicy
    from oarepo_workflows.requests.policy import WorkflowRequestPolicy

from .base import BaseWorkflowSettings


@dataclasses.dataclass
class CommunityWorkflow(BaseWorkflowSettings):
    """Workflow configuration for deposits inside communities."""

    draft_creation_community_roles: list[str] = dataclasses.field(
        default_factory=lambda: ["submitter", "curator", "owner"]
    )
    """Restrict draft creation to community members with at least one of these roles.

    If not specified (empty list), any member of the community can create a
    draft.  Used in addition to the site-wide
    :attr:`~BaseWorkflowSettings.draft_creation_roles` /
    :attr:`~BaseWorkflowSettings.draft_creation_needs` restrictions.
    """

    read_restricted_community_roles: list[str] = dataclasses.field(default_factory=lambda: ["curator", "owner"])
    """Community roles that may read restricted (published) records without requesting access.

    If empty, only the record owner can read the content after publishing. By default allowing curators
    and community owners to access restricted records.

    Note:
        Community roles are used instead of
        :class:`~invenio_rdm_records.services.generators.RecordCommunitiesAction`
        so that each workflow can have independent read/draft/manage permissions.
    """

    read_draft_community_roles: list[str] = dataclasses.field(default_factory=list)
    """Community roles that may read draft records without requesting access.

    If empty, only the record owner can read the content of a draft.  Curators
    can always read draft records when the record is submitted for review.

    Note:
        Community roles are used instead of
        :class:`~invenio_rdm_records.services.generators.RecordCommunitiesAction`
        so that each workflow can have independent read/draft/manage permissions.
    """

    record_manage_community_roles: list[str] = dataclasses.field(default_factory=lambda: ["curator", "owner"])
    """Community roles that may manage (edit, delete, publish) records.

    If empty, only the record owner can manage the record. By default allowing curators
    and community owners to manage all records.

    Note:
        Community roles are used instead of
        :class:`~invenio_rdm_records.services.generators.RecordCommunitiesAction`
        so that each workflow can have independent read/draft/manage permissions.
    """

    community_curator_roles: list[str] = dataclasses.field(default_factory=lambda: ["curator"])
    """Community roles that allow users to review and curate records."""

    # --- permission policy ----------------------------------------------------

    def _build_permission_policy(self) -> type[BasePermissionPolicy]:
        class PermissionPolicy(BooleanPermissionPolicyMixin, self.base_permission_policy):  # type: ignore[name-defined]
            """A permission policy for the workflow."""

            can_create = self._build_record_create_generators()
            can_read = self.base_permission_policy.can_read + self._build_record_view_permissions()
            can_rdm_manage = self._build_record_rdm_manage_generators(self.base_permission_policy.can_rdm_manage)  # type: ignore[attr-defined]
            can_rdm_view = self._build_record_rdm_view_permissions(self.base_permission_policy.can_rdm_view)  # type: ignore[attr-defined]
            can_rdm_preview = self._build_record_rdm_preview_generators(self.base_permission_policy.can_rdm_preview)  # type: ignore[attr-defined]
            can_publish = (*self.base_permission_policy.can_publish, RequestActive())  # type: ignore[attr-defined]

        return PermissionPolicy

    def _build_record_create_generators(self) -> tuple[Generator, ...]:
        """Extend base create generators with community membership constraints.

        Calls :meth:`~BaseWorkflowSettings._build_record_create_generators` to
        resolve site-wide role- and need-based restrictions, then appends an
        :class:`~oarepo_communities.services.permissions.generators.InAnyCommunity`
        generator for each role listed in :attr:`draft_creation_community_roles`.

        Returns:
            A tuple of permission generators for the ``can_create`` policy action.

        """
        create_generators = list(super()._build_record_create_generators())
        for role in self.draft_creation_community_roles:
            # TODO: this needs optimisation - cost grows with the number of communities
            create_generators += [InAnyCommunity(PrimaryCommunityRole(role))]
        return tuple(create_generators)

    # --- RDM permission helpers -----------------------------------------------

    def _replace_communities_action_with_roles(
        self,
        original_permissions: list[Generator],
        community_roles: list[str],
    ) -> list[Generator]:
        """Replace :class:`RecordCommunitiesAction` with explicit community-role generators.

        Filters *original_permissions* to remove any
        :class:`~invenio_rdm_records.services.generators.RecordCommunitiesAction`
        instance (which grants access to *all* community members), then appends a
        :class:`~oarepo_communities.services.permissions.generators.CommunityRole`
        generator for each role in *community_roles*.

        This lets each workflow define fine-grained, role-scoped access instead of
        the blanket community-wide access granted by
        :class:`RecordCommunitiesAction`.

        Args:
            original_permissions: The existing generator list from the base
                permission policy (e.g. ``can_rdm_view``).
            community_roles: Community role names to grant access to.

        Returns:
            An updated generator list.

        """
        result = [gen for gen in original_permissions if not isinstance(gen, RecordCommunitiesAction)]
        result.extend(CommunityRole(role) for role in community_roles)
        return result

    def _build_record_rdm_view_permissions(self, original_rdm_permissions: list[Generator]) -> list[Generator]:
        """Build ``can_rdm_view`` generators for this workflow.

        Replaces :class:`RecordCommunitiesAction` with
        :attr:`read_restricted_community_roles`-scoped generators so that only
        the listed community roles (rather than all community members) can read
        restricted records.

        Args:
            original_rdm_permissions: The existing ``can_rdm_view`` generators
                from the base permission policy.

        Returns:
            Updated generator list.

        """
        return self._replace_communities_action_with_roles(
            original_rdm_permissions, self.read_restricted_community_roles
        )

    def _build_record_rdm_preview_generators(self, original_rdm_permissions: list[Generator]) -> list[Generator]:
        """Build ``can_rdm_preview`` generators for this workflow.

        Replaces :class:`RecordCommunitiesAction` with
        :attr:`read_draft_community_roles`-scoped generators so that only the
        listed community roles (rather than all community members) can preview
        draft records.

        Args:
            original_rdm_permissions: The existing ``can_rdm_preview`` generators
                from the base permission policy.

        Returns:
            Updated generator list.

        """
        return self._replace_communities_action_with_roles(original_rdm_permissions, self.read_draft_community_roles)

    def _build_record_rdm_manage_generators(self, original_rdm_permissions: list[Generator]) -> list[Generator]:
        """Build ``can_rdm_manage`` generators for this workflow.

        Replaces :class:`RecordCommunitiesAction` with
        :attr:`record_manage_community_roles`-scoped generators so that only
        the listed community roles (rather than all community members) can
        manage records.

        Args:
            original_rdm_permissions: The existing ``can_rdm_manage`` generators
                from the base permission policy.

        Returns:
            Updated generator list.

        """
        return self._replace_communities_action_with_roles(original_rdm_permissions, self.record_manage_community_roles)

    # --- request policy -------------------------------------------------------

    def _build_request_policy(self) -> type[WorkflowRequestPolicy]:
        curator_generators: list[PrimaryCommunityRole] = [
            PrimaryCommunityRole(role) for role in self.community_curator_roles
        ]

        requests = {
            # File modification requests let record owners unlock a published
            # record's files (grace-period feature). Created and accepted by
            # invenio's file_modification service (owner submits, system accepts),
            # so no reviewer and no record state transition.
            FileModification.type_id: WorkflowRequest(
                requesters=[RecordOwners()],
                recipients=[RecordOwnersForRecipients()],
                transitions=WorkflowTransitions(),
            ),
            # Quota increase requests let record owners raise a draft's storage
            # quota from their additional allowance. Created and accepted by
            # invenio's quota_increase service (owner submits, system accepts),
            # so no reviewer and no record state transition.
            QuotaIncrease.type_id: WorkflowRequest(
                requesters=[RecordOwners()],
                recipients=[RecordOwnersForRecipients()],
                transitions=WorkflowTransitions(),
            ),
            CommunitySubmission.type_id: WorkflowRequest(
                requesters=[
                    IfNewRecord(
                        then_=self._build_record_create_generators(),
                        else_=[
                            # Note: this permission check can be called from /review url, that is
                            # inside review service's create method. The problem is that review
                            # service does not pass the original record - it fills the "record"
                            # parameter with a community. That's why we can not use IfInState
                            # and similar permission generators that depend on the record.
                            *[
                                IfRDMRecordPassed(
                                    # the user has called the requests' create method directly
                                    then_=[RequireAll(RecordOwners(), PrimaryCommunityRole(role))],
                                    # the user went through the review flow which did not pass the record
                                    else_=[PrimaryCommunityRole(role)],
                                )
                                for role in self.draft_creation_community_roles
                            ],
                            *curator_generators,
                        ],
                    )
                ],
                recipients=curator_generators,
                transitions=WorkflowTransitions(
                    submitted="submitted",
                    accepted="published",
                    declined="review_requested",
                ),
            ),
            PublishChangedMetadataRequestType.type_id: WorkflowRequest(
                requesters=[
                    IfInState(
                        ["draft", "revision_requested"],
                        [
                            RecordOwners(),
                            *curator_generators,
                        ],
                    )
                ],
                recipients=curator_generators,
                transitions=WorkflowTransitions(
                    submitted="submitted",
                    accepted="published",
                    declined="revision_requested",
                ),
            ),
            PublishNewVersionRequestType.type_id: WorkflowRequest(
                requesters=[
                    IfInState(
                        ["draft", "revision_requested"],
                        [
                            RecordOwners(),
                            *curator_generators,
                        ],
                    )
                ],
                recipients=curator_generators,
                transitions=WorkflowTransitions(
                    submitted="submitted",
                    accepted="published",
                    declined="revision_requested",
                ),
            ),
        }

        return self._create_request_policy("CommunityReviewRequestPolicy", requests)
