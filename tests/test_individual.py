# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Tests for the individual workflow configuration."""

from __future__ import annotations

import pytest
from invenio_rdm_records.requests.file_modification import FileModification
from invenio_rdm_records.requests.quota_increase import QuotaIncrease
from invenio_rdm_records.services.generators import RecordOwners
from oarepo_requests.types import PublishDraftRequestType
from oarepo_workflows.services.permissions.composite import RequireAll

from oarepo_config.workflows.simplified.base import add_if_in_state
from oarepo_config.workflows.simplified.individual import IndividualWorkflow


def test_publish():
    """Direct publishing supports owner, role and need variants."""
    assert isinstance(
        IndividualWorkflow(publish_without_review=True)._build_record_publish_generators()[0], RecordOwners
    )

    generators = IndividualWorkflow(
        publish_without_review_roles=["editor"],
        publish_without_review_needs=["publish"],
    )._build_record_publish_generators()
    assert [type(generator) for generator in generators] == [RequireAll, RequireAll]


def test_requests():
    """The small policy is used without review and the full one with it."""
    direct = IndividualWorkflow()._build_request_policy()
    assert hasattr(direct, FileModification.type_id)
    assert hasattr(direct, QuotaIncrease.type_id)

    review = IndividualWorkflow(review_required=True, reviewer_roles=["curator"])._build_request_policy()
    assert hasattr(review, PublishDraftRequestType.type_id)
    assert getattr(review, PublishDraftRequestType.type_id).recipients


def test_invalid_review():
    """A disabled post-review publication mode is rejected explicitly."""
    with pytest.raises(NotImplementedError):
        IndividualWorkflow(review_required=True, publish_after_review=False)._build_request_policy()


def test_policy():
    """Permission policy contains state-aware publish rules."""
    policy = IndividualWorkflow(publish_without_review=True)._build_permission_policy()
    assert policy.can_create
    assert len(policy.can_publish) == 2


def test_state():
    """State wrapper is omitted when no states were configured."""
    generators = [RecordOwners()]
    assert add_if_in_state([], generators) == generators
    assert len(add_if_in_state(["draft"], generators)) == 1
