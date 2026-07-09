#
# Copyright (C) 2024 CESNET z.s.p.o.
#
# oarepo-workflows is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
#
"""Definition of workflow permissions.

The definitions below (one for rdm-based records and one for generic records)
are based on the following record states:

* draft - the record is being created
* submitted - the record is submitted for review
* approved - the record is approved by the reviewers
* published - the record is published
* revision_requested - the record is requested for revision by the reviewers
"""

from __future__ import annotations

from typing import Any

from invenio_rdm_records.services.generators import (
    AccessGrant,
    CommunityInclusionReviewers,
    IfDeleted,
    IfNewRecord,
    IfRecordDeleted,
    IfRestricted,
    RecordCommunitiesAction,
    RecordOwners,
    RequestReviewers,
    ResourceAccessToken,
    SecretLinks,
    SubmissionReviewer,
)
from invenio_records_permissions.generators import (
    AnyUser,
    AuthenticatedUser,
    Disable,
    IfConfig,
    SameAs,
    SystemProcess,
)
from invenio_users_resources.services.permissions import UserManager
from oarepo_workflows.services.permissions import BaseWorkflowPermissionPolicy
from oarepo_workflows.services.permissions.generators import IfInState


class DefaultWorkflowPermissions(BaseWorkflowPermissionPolicy):
    """Base class for workflow permissions, subclass from it and put the result to Workflow constructor.

    Example:
        class MyWorkflowPermissions(DefaultWorkflowPermissions):
            can_read = [AnyUser()]
    in invenio.cfg
    WORKFLOWS = {
        'default': Workflow(
            permission_policy_cls = MyWorkflowPermissions, ...
        )
    }

    """

    files_edit = (
        IfInState(["draft", "revision_requested"], [RecordOwners()]),
        IfInState(["submitted", "approved", "published"], [Disable()]),
    )

    system_process = SystemProcess()

    def __init__(self, action_name: str, **over: Any) -> None:
        """Initialize the workflow permissions."""
        if hasattr(
            self, f"can_{action_name}"
        ):  # edge case in FromRecordWorkflow; request action doesn't have to be defined if it's not in workflow
            can = getattr(self, f"can_{action_name}")
            if self.system_process not in can:
                can = (*can, self.system_process)
                setattr(self.__class__, f"can_{action_name}", can)
        over["policy"] = self
        super().__init__(action_name, **over)

    can_read = (
        IfInState(
            ["draft", "submitted", "approved", "revision_requested"],
            [RecordOwners()],
        ),
        IfInState("published", [AuthenticatedUser()]),
    )

    # from RDM
    can_read_deleted = (IfRecordDeleted(then_=[UserManager, SystemProcess()], else_=[SameAs("can_read")]),)
    can_update = (IfInState(["draft", "revision_requested"], [RecordOwners()]),)
    can_delete = (IfInState(["draft", "revision_requested"], [RecordOwners()]),)
    can_create = (AuthenticatedUser(),)
    can_publish = (IfInState("draft", [RecordOwners()]),)
    can_new_version = (IfInState("published", [RecordOwners()]),)
    can_edit = (IfInState("published", [RecordOwners()]),)

    can_create_files = (SameAs("files_edit"),)
    can_set_content_files = (SameAs("files_edit"),)
    can_commit_files = (SameAs("files_edit"),)
    can_update_files = (SameAs("files_edit"),)
    can_delete_files = (SameAs("files_edit"),)
    can_read_files = (SameAs("can_read"),)
    can_get_content_files = (SameAs("can_read"),)
    can_list_files = (SameAs("can_read"),)
    can_manage_files = (Disable(),)

    can_read_draft = (SameAs("can_read"),)
    can_update_draft = (SameAs("can_update"),)
    can_delete_draft = (SameAs("can_delete"),)

    # RDM records permissions
    can_bulk_add = (Disable(),)

    # draft files
    can_draft_commit_files = (SameAs("can_update_draft"),)
    can_draft_delete_files = (SameAs("can_update_draft"),)
    can_draft_get_content_files = (SameAs("can_read_draft"),)
    can_draft_read_files = (SameAs("can_read_draft"),)
    can_draft_set_content_files = (SameAs("can_update_draft"),)
    can_draft_update_files = (SameAs("can_update_draft"),)
    can_draft_create_files = (SameAs("files_edit"),)

    # draft media files
    can_draft_media_commit_files = (SameAs("can_update_draft"),)
    can_draft_media_create_files = (SameAs("can_update_draft"),)
    can_draft_media_delete_files = (SameAs("can_update_draft"),)
    can_draft_media_get_content_files = (SameAs("can_read_draft"),)
    can_draft_media_read_files = (SameAs("can_read_draft"),)
    can_draft_media_set_content_files = (SameAs("can_update_draft"),)
    can_draft_media_update_files = (SameAs("can_update_draft"),)

    # published media files
    can_media_commit_files = (Disable(),)
    can_media_create_files = (Disable(),)
    can_media_delete_files = (Disable(),)
    can_media_get_content_files = (SameAs("can_read_files"),)
    can_media_read_deleted_files = (Disable(),)
    can_media_read_files = (SameAs("can_read_files"),)
    can_media_set_content_files = (Disable(),)
    can_media_update_files = (Disable(),)

    # record
    can_lift_embargo = (IfInState("published", [SameAs("can_manage")]),)

    # record management
    can_manage = (RecordOwners(),)

    can_manage_internal = (SystemProcess(),)

    can_manage_quota = (SystemProcess(),)
    can_manage_record_access = (SystemProcess(),)

    can_moderate = (Disable(),)

    can_preview = (SameAs("can_read"),)
    can_review = (Disable(),)
    can_view = (SameAs("can_read"),)
    can_purge = (SystemProcess(),)

    can_pid_create = (SameAs("can_update"),)
    can_pid_delete = (SameAs("can_update"),)
    can_pid_discard = (SameAs("can_update"),)
    can_pid_manage = (SameAs("can_update"),)
    can_pid_register = (SameAs("can_update"),)
    can_pid_update = (SameAs("can_update"),)

    # stats
    can_query_stats = (Disable(),)


class DefaultRDMWorkflowPermissions(BaseWorkflowPermissionPolicy):
    """RDM-aligned workflow permissions; subclass and pass to the Workflow constructor.

    This policy mirrors RDMRecordPermissionPolicy but uses IfInState to unify
    draft and published permissions into single ``can_*`` attributes, and uses
    IfRestricted to correctly gate restricted and embargoed records.

    Example::

        class MyWorkflowPermissions(
            DefaultRDMWorkflowPermissions
        ):
            can_read = [AnyUser()]

    in ``invenio.cfg``::

        WORKFLOWS = {
            'default': Workflow(
                permission_policy_cls=MyWorkflowPermissions, ...
            )
        }
    """

    # ------------------------------------------------------------------
    # RDM permission hierarchy.
    # Mirrors can_manage / can_curate / can_review / can_preview / can_view
    # from RDMRecordPermissionPolicy. Each level references the one below
    # via SameAs so that a subclass can override any single level and have
    # the change propagate up the entire chain.
    # SystemProcess is NOT included here; __init__ appends it automatically
    # to every top-level can_* attribute.
    # ------------------------------------------------------------------
    can_rdm_manage = (
        RecordOwners(),
        RecordCommunitiesAction("curate"),
        AccessGrant("manage"),
    )
    can_rdm_curate = (
        SameAs("can_rdm_manage"),
        AccessGrant("edit"),
        SecretLinks("edit"),
    )
    can_rdm_review = (
        SameAs("can_rdm_curate"),
        SubmissionReviewer(),
    )
    can_rdm_preview = (
        SameAs("can_rdm_curate"),
        AccessGrant("preview"),
        SecretLinks("preview"),
        SubmissionReviewer(),
        RequestReviewers(),
        UserManager,
    )
    can_rdm_view = (
        SameAs("can_rdm_preview"),
        AccessGrant("view"),
        SecretLinks("view"),
        CommunityInclusionReviewers(),
        RecordCommunitiesAction("view"),
    )

    # Draft files are writable by reviewers; revision_requested files by curators;
    # all other states are immutable.
    files_edit = (
        IfInState("draft", [SameAs("can_rdm_review")]),
        IfInState("revision_requested", [SameAs("can_rdm_curate")]),
        IfInState(["submitted", "approved", "published"], [Disable()]),
    )

    system_process = SystemProcess()

    def __init__(self, action_name: str, **over: Any) -> None:
        """Initialize the workflow permissions."""
        if hasattr(
            self, f"can_{action_name}"
        ):  # edge case in FromRecordWorkflow; request action doesn't have to be defined if it's not in workflow
            can = getattr(self, f"can_{action_name}")
            if self.system_process not in can:
                can = (*can, self.system_process)
                setattr(self.__class__, f"can_{action_name}", can)
        over["policy"] = self
        super().__init__(action_name, **over)

    # ------------------------------------------------------------------
    # Records
    # ------------------------------------------------------------------

    # draft / submitted / approved / revision_requested: preview hierarchy
    # (owners, curators, access grants, secret links, reviewers, …).
    # Published open records: any user.
    # Published restricted/embargoed records: view hierarchy only.
    can_read = (
        IfInState(
            ["draft", "submitted", "approved", "revision_requested"],
            [SameAs("can_rdm_preview")],
        ),
        IfInState(
            "published",
            [IfRestricted("record", then_=[SameAs("can_rdm_view")], else_=[AnyUser()])],
        ),
    )
    can_read_draft = (SameAs("can_read"),)

    can_read_deleted = (IfRecordDeleted(then_=[UserManager, SystemProcess()], else_=[SameAs("can_read")]),)
    can_read_deleted_files = (SameAs("can_read_deleted"),)

    # draft: review hierarchy; revision_requested: curate hierarchy (no external reviewers);
    # submitted / approved / published: immutable.
    can_update = (
        IfInState(["draft", "submitted"], [SameAs("can_rdm_review")]),
        IfInState("revision_requested", [SameAs("can_rdm_review")]),
        # IfInState(["approved", "published"], [Disable()]), # noqa: ERA001 # keeping as a reminder
    )
    # the update draft for whatever reason is used as the source of truth for the "share" button
    # - so even if it does not make sense to have this on a published record, we need to have
    # the permission open so that sharing works.
    can_update_draft = (SameAs("can_rdm_review"),)

    # Curators may delete a draft or a revision_requested record; all other states deny.
    can_delete = (
        IfInState(
            [
                "draft",
                "revision_requested",
                "submitted",
                "approved",
            ],
            [SameAs("can_rdm_curate")],
        ),
        IfInState(["published"], [Disable()]),
    )
    can_delete_draft = (SameAs("can_delete"),)

    can_create = (AuthenticatedUser(),)
    # Publishing is only possible from the approved state (review workflow).
    can_publish = (IfInState("approved", [SameAs("can_rdm_review")]),)
    can_new_version = (IfInState("published", [SameAs("can_rdm_curate")]),)
    # Editing (draft-from-record) is only possible for published, non-deleted records.
    can_edit = (
        IfDeleted(
            then_=[Disable()],
            # Note: RDM calls can_edit both on the published and draft versions of a record.
            # that is why we can not use IfInState("published"), because then the "Edit" button
            # will be visible but clicking on it will end up with an error.
            # else_=[IfInState("published", [SameAs("can_rdm_curate")])],  # noqa: ERA001 # keeping as a reminder
            else_=[SameAs("can_rdm_curate")],
        ),
    )

    # ------------------------------------------------------------------
    # High-level permission groups (also exposed as actions)
    # ------------------------------------------------------------------
    can_manage = (SameAs("can_rdm_manage"),)
    can_review = (SameAs("can_rdm_review"),)
    can_preview = (SameAs("can_rdm_preview"),)
    can_view = (SameAs("can_rdm_view"),)

    # ------------------------------------------------------------------
    # Published record file permissions
    # ------------------------------------------------------------------
    # Files in a record have their own restriction level, independent of
    # the record-level restriction.
    can_read_files = (
        IfInState(
            ["draft", "submitted", "approved", "revision_requested"],
            [SameAs("can_rdm_preview"), ResourceAccessToken("read")],
        ),
        IfInState(
            "published",
            [
                IfRestricted("files", then_=[SameAs("can_rdm_view")], else_=[AnyUser()]),
                ResourceAccessToken("read"),
            ],
        ),
    )
    can_get_content_files = (SameAs("can_read_files"),)
    can_list_files = (SameAs("can_read_files"),)

    # These actions are disabled for published records; changes go through drafts.
    can_create_files = (SameAs("files_edit"),)
    can_set_content_files = (SameAs("files_edit"),)
    can_commit_files = (SameAs("files_edit"),)
    can_update_files = (SameAs("files_edit"),)
    can_delete_files = (SameAs("files_edit"),)

    can_manage_files = (
        IfConfig(
            "RDM_ALLOW_METADATA_ONLY_RECORDS",
            then_=[IfNewRecord(then_=[AuthenticatedUser()], else_=[SameAs("can_rdm_review")])],
            else_=[],
        ),
    )

    # ------------------------------------------------------------------
    # Draft file permissions (unified via IfInState in the parent can_*)
    # ------------------------------------------------------------------
    can_draft_create_files = (SameAs("files_edit"),)
    can_draft_set_content_files = (SameAs("files_edit"),)
    can_draft_commit_files = (SameAs("can_update"),)
    can_draft_update_files = (SameAs("can_update"),)
    can_draft_delete_files = (SameAs("can_update"),)
    can_draft_read_files = (SameAs("can_read_files"),)
    can_draft_get_content_files = (SameAs("can_read_files"),)

    # ------------------------------------------------------------------
    # Media files — published record
    # Media files use record-level restriction (not file-level).
    # ------------------------------------------------------------------
    can_media_read_files = (
        IfInState(
            ["draft", "submitted", "approved", "revision_requested"],
            [SameAs("can_rdm_review")],
        ),
        IfInState(
            "published",
            [
                IfRestricted("record", then_=[SameAs("can_rdm_view")], else_=[AnyUser()]),
                ResourceAccessToken("read"),
            ],
        ),
    )
    can_media_get_content_files = (SameAs("can_media_read_files"),)
    can_media_read_deleted_files = (SameAs("can_read_deleted"),)
    can_media_commit_files = (Disable(),)
    can_media_create_files = (Disable(),)
    can_media_delete_files = (Disable(),)
    can_media_set_content_files = (Disable(),)
    can_media_update_files = (Disable(),)

    # ------------------------------------------------------------------
    # Media files — draft (unified via IfInState in the parent can_*)
    # ------------------------------------------------------------------
    can_draft_media_read_files = (SameAs("can_media_read_files"),)
    can_draft_media_get_content_files = (SameAs("can_media_read_files"),)
    can_draft_media_create_files = (SameAs("can_update"),)
    can_draft_media_set_content_files = (SameAs("can_update"),)
    can_draft_media_commit_files = (SameAs("can_update"),)
    can_draft_media_update_files = (SameAs("can_update"),)
    can_draft_media_delete_files = (SameAs("can_update"),)

    # ------------------------------------------------------------------
    # Record management
    # ------------------------------------------------------------------
    can_lift_embargo = (IfInState("published", [SameAs("can_manage")]),)

    can_manage_internal = (SystemProcess(),)

    # UserManager + SystemProcess (added by __init__)
    can_manage_quota = (UserManager,)

    can_manage_record_access = (
        IfConfig(
            "RDM_ALLOW_RESTRICTED_RECORDS",
            then_=[IfNewRecord(then_=[AuthenticatedUser()], else_=[SameAs("can_rdm_review")])],
            else_=[],
        ),
    )

    can_moderate = (SystemProcess(),)
    can_purge = (SystemProcess(),)

    # ------------------------------------------------------------------
    # PIDs
    # ------------------------------------------------------------------
    # PIDs may only be managed while the record is actively being prepared;
    # they are frozen once submitted for review.
    can_pid_create = (IfInState(["draft", "revision_requested"], [SameAs("can_rdm_review")]),)
    can_pid_register = (IfInState(["draft", "revision_requested"], [SameAs("can_rdm_review")]),)
    can_pid_update = (IfInState(["draft", "revision_requested"], [SameAs("can_rdm_review")]),)
    can_pid_discard = (IfInState(["draft", "revision_requested"], [SameAs("can_rdm_review")]),)
    can_pid_delete = (IfInState(["draft", "revision_requested"], [SameAs("can_rdm_review")]),)
    can_pid_manage = (SystemProcess(),)

    # ------------------------------------------------------------------
    # Miscellaneous
    # ------------------------------------------------------------------
    can_bulk_add = (SystemProcess(),)
    can_query_stats = (Disable(),)
