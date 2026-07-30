#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Individual (non-community) workflow configuration for OARepo."""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

from invenio_i18n import LazyString
from invenio_i18n import lazy_gettext as _
from invenio_rdm_records.requests.file_modification import FileModification
from invenio_rdm_records.requests.quota_increase import QuotaIncrease
from invenio_rdm_records.services.generators import RecordOwners
from invenio_requests.customizations import CommentEventType
from oarepo_requests.services.permissions.generators import RequestActive
from oarepo_requests.types import (
    PublishChangedMetadataRequestType,
    PublishDraftRequestType,
    PublishNewVersionRequestType,
)
from oarepo_workflows.requests import WorkflowRequest, WorkflowTransitions
from oarepo_workflows.requests.events import WorkflowEvent, WorkflowEvents
from oarepo_workflows.requests.generators.record_owners import RecordOwnersForRecipients
from oarepo_workflows.services.permissions import IfInState
from oarepo_workflows.services.permissions.composite import (
    BooleanPermissionPolicyMixin,
    RequireAll,
)
from oarepo_workflows.services.permissions.generators import (
    HasActionNeed,
    UserWithRole,
)

if TYPE_CHECKING:
    from invenio_records_permissions.generators import Generator
    from invenio_records_permissions.policies.base import BasePermissionPolicy
    from oarepo_workflows.requests.policy import WorkflowRequestPolicy

from .base import BaseWorkflowSettings, add_if_in_state


@dataclasses.dataclass
class IndividualWorkflow(BaseWorkflowSettings):
    """Workflow configuration for deposits outside of communities."""

    code: str = "individual"
    """Unique code identifier for this workflow."""

    label: LazyString = _("Individual Submission Workflow")  # noqa: RUF009
    """Human-readable label for this workflow."""

    authenticated_draft_creation: bool = True
    """Allow authenticated users to create drafts in this workflow.

    Overrides the base-class default of ``False``; any authenticated user can
    create a draft unless more-specific role or need restrictions are configured
    via :attr:`~BaseWorkflowSettings.draft_creation_roles` or
    :attr:`~BaseWorkflowSettings.draft_creation_needs`.
    """

    publish_without_review: bool = False
    """Allow draft owners to publish without submitting a review request.

    When enabled, draft owners can publish directly, subject to
    :attr:`publish_without_review_states`.
    """

    publish_without_review_roles: list[str] = dataclasses.field(default_factory=list)
    """Roles that allow a draft owner to publish without a review request.

    Users must still be owners of the draft record. If the list is non-empty,
    :attr:`publish_without_review` is ignored.
    """

    publish_without_review_needs: list[str] = dataclasses.field(default_factory=list)
    """Permission needs that allow a draft owner to publish without a review request.

    Users must still be owners of the draft record. If the list is non-empty,
    :attr:`publish_without_review` is ignored.
    """

    publish_without_review_states: list[str] = dataclasses.field(default_factory=lambda: ["draft"])
    """Record workflow states in which publication without review is allowed."""

    review_required: bool = False
    """Require a review request before publication.

    If :attr:`publish_without_review` is ``False`` and :attr:`review_required`
    is ``False``, records can only be published through a community workflow.
    """

    reviewer_roles: list[str] = dataclasses.field(default_factory=list)
    """Roles that allow users to review and curate records.

    Users with these roles are also granted read access to draft records.
    """

    reviewer_needs: list[str] = dataclasses.field(default_factory=list)
    """Permission needs that allow users to review and curate records.

    Users with these needs are also granted read access to draft records.
    """

    self_review_enabled: bool = False
    """Allow the record owner to approve their own review request.

    Normally, submitting a record for review prevents the owner from approving it
    themselves. When set to ``True``, the review request is still created on
    submission, but the owner is permitted to accept it.

    This is primarily useful when ``invenio-checks`` is active: checks are tied
    to an open request, so the request must exist even when no external reviewer
    is needed. With this option the owner can see and act on the check results
    without waiting for a curator.

    Has no effect when :attr:`publish_without_review` is ``True``, because in
    that case user can bypass the review request and publish the record directly.
    """

    def _build_permission_policy(self) -> type[BasePermissionPolicy]:
        class PermissionPolicy(BooleanPermissionPolicyMixin, self.base_permission_policy):  # type: ignore[name-defined]
            """A permission policy for the workflow."""

            can_create = self._build_record_create_generators()
            can_publish = (
                *add_if_in_state(
                    self.publish_without_review_states,
                    self._build_record_publish_generators(),
                ),
                IfInState("submitted", then_=[RequestActive()]),
            )
            can_read = self.base_permission_policy.can_read + self._build_record_view_permissions()

        return PermissionPolicy

    def _build_record_publish_generators(self) -> tuple[Generator, ...]:
        """Build generators that control who may publish a draft without a review request.

        Applies the following priority order:

        1. **Role-based** - :attr:`publish_without_review_roles`: owners who also
           hold any of these roles may publish directly.
        2. **Need-based** - :attr:`publish_without_review_needs`: owners who also
           possess any of these permission needs may publish directly.
        3. **Owner fallback** - when neither (1) nor (2) are set and
           :attr:`publish_without_review` is ``True``, the draft owner may publish
           directly.

        Note:
            ``SystemProcess`` is added automatically by the base policy; it does
            not need to be included here.

        Returns:
            A tuple of permission generators for the ``can_publish`` policy action.

        """
        publish_generators: list[Generator] = []
        if self.publish_without_review_roles:
            publish_generators += [
                RequireAll(RecordOwners(), UserWithRole(role_name)) for role_name in self.publish_without_review_roles
            ]
        if self.publish_without_review_needs:
            publish_generators += [
                RequireAll(RecordOwners(), HasActionNeed(action)) for action in self.publish_without_review_needs
            ]
        if not publish_generators and self.publish_without_review:
            publish_generators = [RecordOwners()]
        return tuple(publish_generators)

    def _build_request_policy(self) -> type[WorkflowRequestPolicy]:
        # File modification requests let record owners unlock a published record's
        # files (grace-period feature). Available regardless of review, since it is
        # created and accepted by invenio's file_modification service (owner submits,
        # system accepts) -- no reviewer and no record state transition.
        base_requests = {
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
        }

        if not self.review_required:
            return self._create_request_policy("IndividualRequestPolicy", base_requests)

        reviewer_generators: list[UserWithRole | HasActionNeed] = []
        if self.reviewer_roles:
            reviewer_generators = [UserWithRole(role) for role in self.reviewer_roles]
        if self.reviewer_needs:
            reviewer_generators.extend([HasActionNeed(need) for need in self.reviewer_needs])
        if self.self_review_enabled:
            reviewer_generators.extend(self.record_owners_with_correct_roles(RecordOwnersForRecipients()))  # type: ignore[arg-type]
        if not self.publish_after_review:
            raise NotImplementedError(
                "Disabling publish_after_review is not supported in this version, "
                "please ask the maintainers to enable it"
            )
        requestors = [*reviewer_generators]
        if not self.self_review_enabled:
            requestors.extend(self.record_owners_with_correct_roles(RecordOwners()))  # type: ignore[arg-type]

        requests = {
            **base_requests,
            PublishDraftRequestType.type_id: WorkflowRequest(
                requesters=[
                    IfInState(
                        ["draft", "revision_requested"],
                        requestors,
                    )
                ],
                recipients=reviewer_generators,
                transitions=WorkflowTransitions(
                    submitted="submitted",
                    accepted="published",
                    declined="revision_requested",
                ),
                events=WorkflowEvents(
                    {CommentEventType.type_id or "C": WorkflowEvent(submitters=[*requestors, *reviewer_generators])}
                ),
            ),
            PublishChangedMetadataRequestType.type_id: WorkflowRequest(
                requesters=[
                    IfInState(
                        ["draft", "revision_requested"],
                        requestors,
                    )
                ],
                recipients=reviewer_generators,
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
                        requestors,
                    )
                ],
                recipients=reviewer_generators,
                transitions=WorkflowTransitions(
                    submitted="submitted",
                    accepted="published",
                    declined="revision_requested",
                ),
            ),
        }

        return self._create_request_policy("GlobalReviewRequestPolicy", requests)

    def record_owners_with_correct_roles(self, record_owner_generator: RecordOwners) -> list[Generator]:
        """Return the record owner generator with the correct roles/needs."""
        generators: list[Generator] = []
        if self.draft_creation_roles:
            generators += [
                RequireAll(record_owner_generator, UserWithRole(role_name)) for role_name in self.draft_creation_roles
            ]
        if self.draft_creation_needs:
            generators += [RequireAll(RecordOwners(), HasActionNeed(action)) for action in self.draft_creation_needs]
        if not generators:
            generators = [record_owner_generator]
        return generators
