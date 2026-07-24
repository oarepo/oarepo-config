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

from .base import set_constants_in_caller


def configure_files(
    max_file_size: int = 1 * 10**9,
    max_files_count: int = 100,
    max_total_size: int = 5 * 10**9,
    allow_metadata_only_records: bool = True,
    allow_empty_files: bool | None = None,
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
        allow_empty_files
        if allow_empty_files is not None
        else allow_metadata_only_records
    )

    set_constants_in_caller(locals())
