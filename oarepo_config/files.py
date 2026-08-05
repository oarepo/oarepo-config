#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for record files and upload quotas."""

from __future__ import annotations

from datetime import timedelta

from invenio_rdm_records.services.request_policies import (  # type: ignore[reportMissingImports]
    FileModificationAdminPolicy,
    FileModificationGracePeriodPolicy,
    QuotaIncreaseAdminPolicy,
    QuotaIncreasePolicy,
)

from .base import set_constants_in_caller


def configure_files(  # noqa: PLR0913, PLR0917
    max_file_size: int = 1 * 10**9,
    max_files_count: int = 100,
    max_total_size: int = 5 * 10**9,
    allow_metadata_only_records: bool = True,
    allow_empty_files: bool | None = None,
    file_modification_grace_period: timedelta = timedelta(days=45),
    allow_immediate_file_modification: bool = True,
    allow_immediate_quota_increase: bool = True,
) -> None:
    """Set up file upload quotas and file-related toggles.

    Controls how many files users may attach to a record deposition, how
    large each individual file may be, the total storage budget for the
    deposition, whether a deposition can be published without any files
    at all, and whether uploaded files may have zero bytes.

    Args:
        max_file_size: Maximum size of a single uploaded file in bytes.
            Defaults to 1 GB (``1 * 10**9``).
        max_files_count: Maximum number of files allowed per record
            deposition. Defaults to ``100``.
        max_total_size: Maximum combined size of all files in a single
            record deposition, in bytes. Defaults to 5 GB
            (``5 * 10**9``).
        allow_metadata_only_records: When ``False``, users must upload
            at least one file before they can publish a record
            deposition. When ``True`` (the default), metadata-only
            records are allowed.
        allow_empty_files: When ``False``, zero-byte files are rejected.
            When ``True``, they are allowed. Defaults to the value of
            ``allow_metadata_only_records`` so that requiring files also
            prevents users from satisfying the requirement with an empty
            file.
        file_modification_grace_period: Grace period after a record is
            published during which its files can still be modified without
            creating a new version. Checked at publish time. Defaults to
            45 days (``timedelta(days=45)``).
        allow_immediate_file_modification: When ``True`` (the default),
            record owners may unlock and edit their published files
            themselves within ``file_modification_grace_period``, while
            admins and system processes may do so at any time. When
            ``False``, the default Invenio policy (admin-only) is left in
            place.
        allow_immediate_quota_increase: When ``True`` (the default), users
            may immediately raise a draft's storage quota from their
            additional allowance (this surfaces the "Manage storage" UI in
            the file uploader); admins may do so for any record. When
            ``False``, immediate quota increases stay disabled.

    Invenio configuration variables set:

    * ``RDM_FILES_DEFAULT_MAX_FILE_SIZE`` - backend limit on the size of
      a single file.
    * ``RDM_FILES_DEFAULT_QUOTA_SIZE`` - backend limit on the total size
      of all files in a record deposition.
    * ``RDM_RECORDS_MAX_FILES_COUNT`` - backend limit on the number of
      files per record.
    * ``RDM_ALLOW_METADATA_ONLY_RECORDS`` - whether metadata-only
      records are allowed.
    * ``RECORDS_RESOURCES_ALLOW_EMPTY_FILES`` - whether zero-byte files
      may be uploaded.
    * ``RDM_FILE_MODIFICATION_PERIOD`` - time window after record
      creation during which modified files may be published.
    * ``RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED`` - whether published
      files may be edited immediately; set to
      ``allow_immediate_file_modification``.
    * ``RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES`` - ordered list of
      policies deciding who may edit published files immediately (only
      set when ``allow_immediate_file_modification`` is ``True``).
    * ``RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED`` - whether users may
      immediately raise a draft's quota; set to
      ``allow_immediate_quota_increase``.
    * ``RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES`` - ordered list of policies
      deciding who may raise a draft's quota (only set when
      ``allow_immediate_quota_increase`` is ``True``).
    * ``APP_RDM_DEPOSIT_FORM_QUOTA`` - deposit-form UI quota object with
      ``maxFiles`` and ``maxStorage``.
    * ``FILES_REST_DEFAULT_MAX_FILE_SIZE`` and
      ``FILES_REST_DEFAULT_QUOTA_SIZE`` - fallback variables used by
      the lower-level file storage layer.

    Example:

    .. code-block:: python

        # Use the default file quotas and toggles. All parameters below
        # match the helper's built-in defaults and are shown explicitly
        # for reference; they can be omitted when calling the helper.
        config.configure_files(
            max_file_size=1 * 10**9,
            max_files_count=100,
            max_total_size=5 * 10**9,
            allow_metadata_only_records=True,
        )

    """
    RDM_FILES_DEFAULT_MAX_FILE_SIZE = max_file_size
    FILES_REST_DEFAULT_MAX_FILE_SIZE = max_file_size

    RDM_FILES_DEFAULT_QUOTA_SIZE = max_total_size
    FILES_REST_DEFAULT_QUOTA_SIZE = max_total_size

    RDM_RECORDS_MAX_FILES_COUNT = max_files_count

    APP_RDM_DEPOSIT_FORM_QUOTA = {
        "maxFiles": max_files_count,
        "maxStorage": max_total_size,
    }

    RDM_ALLOW_METADATA_ONLY_RECORDS = allow_metadata_only_records
    RECORDS_RESOURCES_ALLOW_EMPTY_FILES = (
        allow_empty_files if allow_empty_files is not None else allow_metadata_only_records
    )

    RDM_FILE_MODIFICATION_PERIOD = file_modification_grace_period

    RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED = allow_immediate_file_modification
    if allow_immediate_file_modification:
        # Let record owners unlock/edit their published files themselves within
        # the grace period; admins/system may do so at any time. Policies are
        # evaluated in order, most to least specific.
        RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES = [
            FileModificationGracePeriodPolicy(grace_period=file_modification_grace_period),
            FileModificationAdminPolicy(),
        ]

    RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED = allow_immediate_quota_increase
    if allow_immediate_quota_increase:
        # Let users raise a draft's quota from their additional allowance
        # immediately (surfaces the "Manage storage" UI); admins for any record.
        RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES = [
            QuotaIncreasePolicy(),
            QuotaIncreaseAdminPolicy(),
        ]

    set_constants_in_caller(locals())
