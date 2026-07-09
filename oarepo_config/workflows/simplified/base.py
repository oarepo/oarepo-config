#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Base workflow settings and helpers for OARepo workflow configuration."""

from __future__ import annotations

import abc
import dataclasses
from typing import TYPE_CHECKING, Any

from invenio_i18n import LazyString
from invenio_i18n import lazy_gettext as _
from invenio_records_permissions.generators import AuthenticatedUser, Generator
from oarepo_workflows.base import Workflow

if TYPE_CHECKING:
    from collections.abc import Callable

    from invenio_records_permissions.policies.base import BasePermissionPolicy

from oarepo_workflows.requests.policy import WorkflowRequestPolicy
from oarepo_workflows.services.permissions import IfInState
from oarepo_workflows.services.permissions.generators import HasActionNeed, UserWithRole

from .workflow_permissions import DefaultRDMWorkflowPermissions


def add_if_in_state(
    states: list[str],
    generators: tuple[Generator, ...] | list[Generator],
) -> list[Generator]:
    """Wrap generators in an :class:`IfInState` constraint when states are provided.

    If *states* is non-empty, returns a single-element list containing an
    :class:`~oarepo_workflows.services.permissions.IfInState` generator that
    activates *generators* only when the record is in one of the listed states.
    If *states* is empty the generators are returned unchanged as a plain list.

    Args:
        states: Workflow state names that gate the generators.  Pass an empty
            list to apply the generators unconditionally.
        generators: Permission generators to conditionally wrap.

    Returns:
        A list of generators, optionally wrapped in an :class:`IfInState`
        constraint.

    """
    if not states:
        return list(generators)
    return [IfInState(states, then_=generators)]


@dataclasses.dataclass
class BaseWorkflowSettings:
    """Shared configuration common to all workflow types."""

    code: str = "undefined"
    """The code of the workflow type."""

    label: LazyString = _("Undefined policy")  # noqa: RUF009
    """The label of the workflow type."""

    base_permission_policy: type[BasePermissionPolicy] = DefaultRDMWorkflowPermissions
    """The base permission policy class for this workflow that will be configured."""

    base_request_policy: type[WorkflowRequestPolicy] = WorkflowRequestPolicy
    """The base requests policy class for this workflow that will be configured."""

    review_request_states: list[str] = dataclasses.field(default_factory=lambda: ["draft"])
    """Record workflow states in which a review request may be submitted."""

    record_view_permissions: dict[str, list[Generator]] = dataclasses.field(default_factory=dict)
    """View permissions for records in this workflow.

    It is a dictionary, the key is record state and the value is a list of generators.
    """

    publish_after_review: bool = True
    """Publish immediately after reviewer approves the review request."""

    extra_permissions: (
        type[BasePermissionPolicy] | Callable[[type[BasePermissionPolicy]], type[BasePermissionPolicy]] | None
    ) = None
    """Extra permissions to apply to the record permission policy.

    If a callable is provided, it will be called with the generated permission policy
    as an argument and should return a modified permission policy. If a class is provided,
    it will be used as a mixin for the generated permission policy.
    """

    extra_requests: (
        type[WorkflowRequestPolicy] | Callable[[type[WorkflowRequestPolicy]], type[WorkflowRequestPolicy]] | None
    ) = None
    """Extra requests to apply to the workflow request policy.

    If a callable is provided, it will be called with the generated request policy
    as an argument and should return a modified request policy. If a class is provided,
    it will be used as a mixin for the generated request policy.
    """

    authenticated_draft_creation: bool = False
    """Allow authenticated users to create draft records.

    When enabled and no role- or need-based restrictions are configured, any
    authenticated user may create a draft.  Subclasses may override this
    default (e.g. :class:`IndividualWorkflow` sets it to ``True``).
    """

    draft_creation_roles: list[str] = dataclasses.field(default_factory=list)
    """Restrict draft creation to users who hold at least one of these site-wide roles.

    When non-empty, takes priority over :attr:`authenticated_draft_creation`.
    """

    draft_creation_needs: list[str] = dataclasses.field(default_factory=list)
    """Restrict draft creation to users who hold at least one of these permission needs.

    When non-empty, takes priority over :attr:`authenticated_draft_creation`.
    """

    # --- public API -----------------------------------------------------------

    def build_workflow(self) -> Workflow:
        """Build and return the workflow instance."""
        permissions: type[BasePermissionPolicy] = self._build_permission_policy()
        request_policy: type[WorkflowRequestPolicy] = self._build_request_policy()
        if self.extra_permissions:
            if isinstance(self.extra_permissions, type):
                permissions = type(permissions.__name__, (self.extra_permissions, permissions), {})
            elif callable(self.extra_permissions):
                permissions = self.extra_permissions(permissions)
        if self.extra_requests:
            if isinstance(self.extra_requests, type):
                request_policy = type(request_policy.__name__, (self.extra_requests, request_policy), {})
            elif callable(self.extra_requests):
                request_policy = self.extra_requests(request_policy)

        return Workflow(
            code=self.code,
            label=self.label,
            permission_policy_cls=permissions,
            request_policy_cls=request_policy,
        )

    # --- protected helpers ----------------------------------------------------

    def _build_record_view_permissions(self) -> tuple[Generator, ...]:
        """Build per-state view permission generators from :attr:`record_view_permissions`.

        Returns:
            A tuple of :class:`~oarepo_workflows.services.permissions.IfInState`
            generators - one per entry in :attr:`record_view_permissions` - or
            an empty tuple when no overrides are configured.

        """
        if not self.record_view_permissions:
            return ()
        return tuple(IfInState(state, then_=generators) for state, generators in self.record_view_permissions.items())

    def _build_record_create_generators(self) -> tuple[Generator, ...]:
        """Build generators that control who may create a new draft record.

        Applies the following priority order:

        1. **Role-based** - :attr:`draft_creation_roles`: users holding any of
           these site-wide roles are allowed.
        2. **Need-based** - :attr:`draft_creation_needs`: users possessing any
           of these permission needs are allowed.
        3. **Authenticated fallback** - when neither (1) nor (2) are set and
           :attr:`authenticated_draft_creation` is ``True``, any authenticated
           user is allowed.

        Subclasses may call ``super()._build_record_create_generators()`` and
        extend the returned tuple with additional generators.

        Returns:
            A tuple of permission generators for the ``can_create`` policy action.

        """
        create_generators: list[Generator] = []
        if self.draft_creation_roles:
            create_generators += [UserWithRole(role) for role in self.draft_creation_roles]
        if self.draft_creation_needs:
            create_generators += [HasActionNeed(action) for action in self.draft_creation_needs]
        if not create_generators and self.authenticated_draft_creation:
            create_generators = [AuthenticatedUser()]
        return tuple(create_generators)

    def _create_request_policy(
        self,
        class_name: str,
        requests: dict[str, Any],
    ) -> type[WorkflowRequestPolicy]:
        """Dynamically create a named :class:`WorkflowRequestPolicy` subclass.

        This is a thin convenience wrapper around :func:`type` that removes the
        boilerplate of repeating ``(self.base_request_policy,)`` in every
        ``_build_request_policy`` override.

        Args:
            class_name: The ``__name__`` to assign to the generated class.
            requests: A mapping of request-type IDs to
                :class:`~oarepo_workflows.requests.WorkflowRequest` instances
                that will become class-level attributes of the new policy.

        Returns:
            A freshly created subclass of :attr:`base_request_policy` with
            *requests* merged in as class attributes.

        """
        return type(class_name, (self.base_request_policy,), requests)

    @abc.abstractmethod
    def _build_permission_policy(self) -> type[BasePermissionPolicy]:
        """Build and return the permission policy class for this workflow."""
        raise NotImplementedError

    @abc.abstractmethod
    def _build_request_policy(self) -> type[WorkflowRequestPolicy]:
        """Build and return the request policy class for this workflow."""
        raise NotImplementedError
