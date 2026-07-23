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

from oarepo_config.files import configure_files


def test_configure_files_defaults():
    """Default quotas and metadata-only toggle are written to globals."""
    configure_files()

    assert RDM_FILES_DEFAULT_MAX_FILE_SIZE == 10 * 10**9  # noqa: F821
    assert FILES_REST_DEFAULT_MAX_FILE_SIZE == 10 * 10**9  # noqa: F821
    assert RDM_FILES_DEFAULT_QUOTA_SIZE == 10 * 10**9  # noqa: F821
    assert FILES_REST_DEFAULT_QUOTA_SIZE == 10 * 10**9  # noqa: F821
    assert RDM_RECORDS_MAX_FILES_COUNT == 100  # noqa: F821
    assert APP_RDM_DEPOSIT_FORM_QUOTA == {  # noqa: F821
        "maxFiles": 100,
        "maxStorage": 10 * 10**9,
    }
    assert RDM_ALLOW_METADATA_ONLY_RECORDS is True  # noqa: F821


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
