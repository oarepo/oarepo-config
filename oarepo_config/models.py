#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for models."""

from __future__ import annotations

import logging

from .base import get_constant_from_caller, set_constants_in_caller

log = logging.getLogger("config.models")


def add_model(model_package_name: str) -> None:
    """Include a data model in the repository's global (cross-model) search.

    Repositories can host several different kinds of records (models),
    e.g. "datasets" and "publications". Call this once per model package
    to make its records show up in searches that span all models at
    once (as opposed to searching within just one model). This does not
    register the model itself (its API endpoints, forms, etc.) - that is
    normally done separately, by calling that model package's own
    ``register()`` function.

    Args:
        model_package_name: The Python import path of the generated
            model package to add, e.g. ``"datasets"`` for a model built
            from a ``datasets`` model package. If the package cannot be
            found or has not been built yet, this is only logged as an
            error - it does not stop the repository from starting.

    Invenio configuration variables set:

    * ``GLOBAL_SEARCH_MODELS`` - the model's ``MODEL_DEFINITION`` is
      appended to this list; any models already registered (by earlier
      calls, or by other packages) are kept.

    Example:

    .. code-block:: python

        from datasets import datasets_model

        datasets_model.register()
        config.add_model("datasets")

    """
    from invenio_base.utils import obj_or_import_string

    model = obj_or_import_string(f"runtime_models_{model_package_name}")
    if hasattr(model, "record_error_handlers"):
        RDM_RECORDS_ERROR_HANDLERS = (
            get_constant_from_caller("RDM_RECORDS_ERROR_HANDLERS") | model.record_error_handlers  # type: ignore[reportOptionalMemberAccess]
        )
        set_constants_in_caller({"RDM_RECORDS_ERROR_HANDLERS": RDM_RECORDS_ERROR_HANDLERS})
