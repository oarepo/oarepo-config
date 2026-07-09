#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for datastreams."""

from __future__ import annotations

from typing import Any

from invenio_base.utils import obj_or_import_string

from .base import (
    merge_with_caller,
    set_constants_in_caller,
)


def configure_datastreams(
    readers: dict[str, Any] | None = None,
    writers: dict[str, Any] | None = None,
    transformers: dict[str, Any] | None = None,
) -> None:
    """Register custom sources for importing vocabularies (fixtures) into the repository.

    Vocabularies (controlled lists such as languages, resource types or
    licenses) can be loaded from files or external services using
    "datastreams" - a reader that fetches/reads the raw data, an
    optional transformer that converts it, and a writer that stores it.
    Invenio already ships with a set of built-in readers/writers/
    transformers; use this function only if you need to add your own
    (for example, a reader that pulls a vocabulary from a custom REST
    API).

    Args:
        readers: Extra readers to make available, as a mapping of a
            short name to either an import path string
            (``"my_package.readers:MyReader"``) or the class/object
            itself.
        writers: Extra writers to make available, in the same format as
            ``readers``.
        transformers: Extra transformers to make available, in the same
            format as ``readers``.

    Any readers/writers/transformers already registered (for example by
    :func:`configure_generic_parameters`) are kept; the ones passed here
    are added on top.

    Invenio configuration variables set:

    * ``VOCABULARIES_DATASTREAM_READERS`` - only if ``readers`` is
      given; merged with any existing value.
    * ``VOCABULARIES_DATASTREAM_WRITERS`` - only if ``writers`` is
      given; merged with any existing value.
    * ``VOCABULARIES_DATASTREAM_TRANSFORMERS`` - only if
      ``transformers`` is given; merged with any existing value.

    Example:

    .. code-block:: python

        config.configure_datastreams(
            readers={
                "myreader": "my_package:MyReader"
            },
            writers={
                "mywriter": "my_package:MyWriter"
            },
        )

    """
    # can't move into a function cause of constant_from_caller methods
    if readers:
        objs = {k: obj_or_import_string(v) for k, v in readers.items()}
        VOCABULARIES_DATASTREAM_READERS = merge_with_caller("VOCABULARIES_DATASTREAM_READERS", objs)

    if writers:
        objs = {k: obj_or_import_string(v) for k, v in writers.items()}
        VOCABULARIES_DATASTREAM_WRITERS = merge_with_caller("VOCABULARIES_DATASTREAM_WRITERS", objs)

    if transformers:
        objs = {k: obj_or_import_string(v) for k, v in transformers.items()}
        VOCABULARIES_DATASTREAM_TRANSFORMERS = merge_with_caller("VOCABULARIES_DATASTREAM_TRANSFORMERS", objs)
    set_constants_in_caller(locals())
