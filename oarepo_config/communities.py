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

    class DefaultCommunitiesPermissionPolicy(
        BooleanPermissionPolicyMixin, CommunityPermissionPolicy
    ):
        """Default Permissions for Community CRUD operations for workflow scenarios."""

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

    DefaultCommunitiesPermissionPolicy = CommunityPermissionPolicy


def configure_communities(communities_roles=None):
    """Set up communities: who can do what inside a community.

    Communities are the groups records can be submitted to (for example
    a department or a project). This sets the roles a member of a
    community can have (such as "owner", "curator", "member") and what
    each role is allowed to do.

    Args:
        communities_roles: The list of roles available in every
            community, as a list of dictionaries. If omitted, three
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
    * ``COMMUNITIES_PERMISSION_POLICY`` - who can create, manage, curate
      and join communities.
    * ``COMMUNITIES_ROLES`` - the ``communities_roles`` list described
      above.

    Example, adding a fourth "submitter" role below "owner"/"curator":

    ```python
    config.configure_communities(
        communities_roles=[
            dict(
                name="owner",
                title=_("Community owner"),
                is_owner=True,
                can_manage=True,
                can_manage_roles=["owner", "curator", "member", "submitter"],
            ),
            dict(
                name="curator",
                title=_("Curator"),
                can_manage=True,
                can_manage_roles=["member", "submitter"],
            ),
            dict(name="submitter", title=_("Submitter"), can_manage=True),
            dict(name="member", title=_("Member")),
        ]
    )
    ```
    """
    COMMUNITIES_REGISTER_UI_BLUEPRINT = True
    COMMUNITIES_PERMISSION_POLICY = DefaultCommunitiesPermissionPolicy
    COMMUNITIES_ROLES = communities_roles or [
        # note: order matters, roles should be sorted by importance
        # from the most important to the least
        dict(
            name="owner",
            title=_("Community owner"),
            description=_("Can manage community."),
            is_owner=True,
            can_manage=True,
            can_manage_roles=["owner", "curator", "member"],
        ),
        dict(
            name="curator",
            title=_("Curator"),
            description=_("Can curate records."),
            can_manage=True,
            # NTK decision: curator should NOT be able to manage curators
            can_manage_roles=["member"],
        ),
        dict(
            name="member",
            title=_("Member"),
            description=_("Community member with read permissions."),
        ),
    ]
    set_constants_in_caller(locals())
