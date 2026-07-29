#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for communities."""

from __future__ import annotations

from invenio_administration.generators import Administration
from invenio_communities.generators import (
    CommunityManagersForRole,
)
from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_i18n import lazy_gettext as _
from invenio_records_permissions.generators import Disable, SystemProcess

from .base import set_constants_in_caller

try:
    from oarepo_communities.services.permissions.generators import (
        CanSubmitRecordInCommunity,
        PrimaryCommunityRole,
    )
    from oarepo_workflows.services.permissions.composite import (
        BooleanPermissionPolicyMixin,
    )

    class DefaultCommunitiesPermissionPolicy(BooleanPermissionPolicyMixin, CommunityPermissionPolicy):  # type: ignore[reportIncompatibleVariableOverride]
        """Default permission policy for communities."""

        can_create = (Administration(), SystemProcess())
        can_submit_record = (CanSubmitRecordInCommunity(), SystemProcess())
        can_include_directly = (SystemProcess(),)
        can_members_add = (SystemProcess(),)
        can_members_search = (
            PrimaryCommunityRole("owner"),
            PrimaryCommunityRole("curator"),
            SystemProcess(),
        )
        can_members_search_public = (
            PrimaryCommunityRole("owner"),
            PrimaryCommunityRole("curator"),
            SystemProcess(),
        )
        can_members_update = (
            CommunityManagersForRole(),
            SystemProcess(),
        )
        can_members_delete = can_members_update
        can_request_membership = (Disable(),)

except ImportError:
    from invenio_communities.permissions import CommunityPermissionPolicy

    DefaultCommunitiesPermissionPolicy = CommunityPermissionPolicy  # type: ignore[misc,assignment]


def configure_communities(
    communities_roles: list | None = None,
) -> None:
    """Set up the configuration for communities.

    Communities let you organize records into collections with their own
    managers and settings. This function configures who can do what in
    each community (the roles), how records are submitted to communities,
    and other community-related settings.

    Args:
        communities_roles: Custom role definitions for communities. If not
            provided, defaults to owner/curator/member roles. If omitted, three
            default roles are used: "owner" (can manage the community
            and its members), "curator" (can review/curate submitted
            records) and "member" (can only view). Pass your own list to
            replace the defaults, e.g. to add a "submitter" role. Each
            role dictionary understands the keys ``name``, ``title``,
            ``description``, ``is_owner``, ``can_manage``,
            ``can_curate`` and ``can_manage_roles`` (the names of the
            roles this role is allowed to add/remove).

    Invenio configuration variables set:

    * ``COMMUNITIES_REGISTER_UI_BLUEPRINT`` - always ``True``; enables
      the communities UI.
    * ``COMMUNITIES_PERMISSION_POLICY`` - the permission policy class for
      communities.
    * ``COMMUNITIES_ROLES`` - the list of available roles in communities.

    Example:

    .. code-block:: python

        config.configure_communities()
        # or with custom settings:

        config.configure_communities(
            communities_roles=[
                dict(
                    name="owner",
                    title=_("Community owner"),
                    is_owner=True,
                    can_manage=True,
                    can_manage_roles=[
                        "owner",
                        "curator",
                        "member",
                        "submitter",
                    ],
                ),
                dict(
                    name="curator",
                    title=_("Curator"),
                    can_manage=True,
                    can_manage_roles=[
                        "member",
                        "submitter",
                    ],
                ),
                dict(
                    name="submitter",
                    title=_("Submitter"),
                    can_manage=False,
                ),
                dict(
                    name="member",
                    title=_("Member"),
                ),
            ]
        )

    """
    COMMUNITIES_REGISTER_UI_BLUEPRINT = True
    COMMUNITIES_PERMISSION_POLICY = DefaultCommunitiesPermissionPolicy
    COMMUNITIES_ROLES = communities_roles or [
        # note: order matters, roles should be sorted by importance
        # from the most important to the least
        {
            "name": "owner",
            "title": _("Community owner"),
            "description": _("Can manage community."),
            "is_owner": True,
            "can_manage": True,
            "can_manage_roles": ["owner", "curator", "member"],
        },
        {
            "name": "curator",
            "title": _("Curator"),
            "description": _("Can curate records."),
            "can_manage": True,
            "can_manage_roles": ["member"],
        },
        {
            "name": "member",
            "title": _("Member"),
            "description": _("Community member with read permissions."),
        },
    ]

    set_constants_in_caller(locals())
