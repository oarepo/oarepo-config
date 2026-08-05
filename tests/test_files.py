#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Tests for file quota configuration."""

from __future__ import annotations

from datetime import timedelta

from invenio_rdm_records.services.request_policies import (
    FileModificationAdminPolicy,
    FileModificationGracePeriodPolicy,
    QuotaIncreaseAdminPolicy,
    QuotaIncreasePolicy,
)

from oarepo_config.files import configure_files


def test_configure_files_defaults():
    """Default quotas and file-related toggles are written to globals."""
    configure_files()

    assert RDM_FILES_DEFAULT_MAX_FILE_SIZE == 1 * 10**9  # noqa: F821
    assert FILES_REST_DEFAULT_MAX_FILE_SIZE == 1 * 10**9  # noqa: F821
    assert RDM_FILES_DEFAULT_QUOTA_SIZE == 5 * 10**9  # noqa: F821
    assert FILES_REST_DEFAULT_QUOTA_SIZE == 5 * 10**9  # noqa: F821
    assert RDM_RECORDS_MAX_FILES_COUNT == 100  # noqa: F821
    assert APP_RDM_DEPOSIT_FORM_QUOTA == {  # noqa: F821
        "maxFiles": 100,
        "maxStorage": 5 * 10**9,
    }
    assert RDM_ALLOW_METADATA_ONLY_RECORDS is True  # noqa: F821
    assert RECORDS_RESOURCES_ALLOW_EMPTY_FILES is True  # noqa: F821
    assert timedelta(days=45) == RDM_FILE_MODIFICATION_PERIOD  # noqa: F821

    assert RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED is True  # noqa: F821
    file_policies = RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES  # noqa: F821
    assert [type(p) for p in file_policies] == [
        FileModificationGracePeriodPolicy,
        FileModificationAdminPolicy,
    ]
    assert file_policies[0].grace_period == timedelta(days=45)

    assert RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED is True  # noqa: F821
    assert [type(p) for p in RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES] == [  # noqa: F821
        QuotaIncreasePolicy,
        QuotaIncreaseAdminPolicy,
    ]


def test_configure_files_immediate_features_disabled():
    """Disabling the features turns off the ENABLED flags and skips the policies."""
    # configure_files injects into this module's globals, which persist across
    # tests, so clear any policy lists a previous test may have set first.
    for name in (
        "RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES",
        "RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES",
    ):
        globals().pop(name, None)

    configure_files(
        allow_immediate_file_modification=False,
        allow_immediate_quota_increase=False,
    )

    assert RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED is False  # noqa: F821
    assert RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED is False  # noqa: F821
    assert "RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES" not in globals()
    assert "RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES" not in globals()


def test_configure_files_custom_values():
    """Custom quotas and metadata-only requirement are written to globals."""
    configure_files(
        max_file_size=1 * 10**9,
        max_files_count=20,
        max_total_size=5 * 10**9,
        allow_metadata_only_records=False,
    )

    assert RDM_FILES_DEFAULT_MAX_FILE_SIZE == 1 * 10**9  # noqa: F821
    assert FILES_REST_DEFAULT_MAX_FILE_SIZE == 1 * 10**9  # noqa: F821
    assert RDM_FILES_DEFAULT_QUOTA_SIZE == 5 * 10**9  # noqa: F821
    assert FILES_REST_DEFAULT_QUOTA_SIZE == 5 * 10**9  # noqa: F821
    assert RDM_RECORDS_MAX_FILES_COUNT == 20  # noqa: F821
    assert APP_RDM_DEPOSIT_FORM_QUOTA == {  # noqa: F821
        "maxFiles": 20,
        "maxStorage": 5 * 10**9,
    }
    assert RDM_ALLOW_METADATA_ONLY_RECORDS is False  # noqa: F821
    assert RECORDS_RESOURCES_ALLOW_EMPTY_FILES is False  # noqa: F821


def test_configure_files_allow_empty_files_override():
    """Empty files can be allowed even when metadata-only records are not."""
    configure_files(
        allow_metadata_only_records=False,
        allow_empty_files=True,
    )

    assert RDM_ALLOW_METADATA_ONLY_RECORDS is False  # noqa: F821
    assert RECORDS_RESOURCES_ALLOW_EMPTY_FILES is True  # noqa: F821
