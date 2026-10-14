#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Tests for standalone configuration helpers."""

from __future__ import annotations

from oarepo_config.communities import configure_communities
from oarepo_config.cron import configure_cron
from oarepo_config.datastreams import configure_datastreams
from oarepo_config.jobs import configure_jobs
from oarepo_config.oai import configure_oai
from oarepo_config.vocabulary import configure_vocabulary


def test_communities():
    """Community defaults and explicit roles are stored in configuration."""
    configure_communities()
    assert COMMUNITIES_REGISTER_UI_BLUEPRINT is True  # noqa: F821
    assert [role["name"] for role in COMMUNITIES_ROLES] == ["owner", "curator", "member"]  # noqa: F821

    configure_communities([{"name": "reviewer"}])
    assert COMMUNITIES_ROLES == [{"name": "reviewer"}]  # noqa: F821


def test_cron():
    """Built-in jobs remain present and extra jobs are added."""
    configure_cron(custom={"task": "example.task"})

    assert CELERY_BEAT_SCHEDULE["custom"]["task"] == "example.task"  # noqa: F821
    assert "indexer" in CELERY_BEAT_SCHEDULE  # noqa: F821


def test_datastreams():
    """Custom datastream implementations are merged into existing ones."""
    global VOCABULARIES_DATASTREAM_READERS
    VOCABULARIES_DATASTREAM_READERS = {"old": str}

    configure_datastreams(readers={"new": int}, writers={"write": list}, transformers={"transform": dict})

    assert VOCABULARIES_DATASTREAM_READERS == {"old": str, "new": int}  # noqa: F821
    assert VOCABULARIES_DATASTREAM_WRITERS == {"write": list}  # noqa: F821
    assert VOCABULARIES_DATASTREAM_TRANSFORMERS == {"transform": dict}  # noqa: F821


def test_jobs():
    """Custom job settings override the helper defaults."""
    configure_jobs(permission_policy="example.Policy", logging_level="DEBUG")

    assert APP_LOGS_PERMISSION_POLICY == "example.Policy"  # noqa: F821
    assert JOBS_LOGGING_LEVEL == "DEBUG"  # noqa: F821


def test_oai():
    """OAI uses the configured repository name."""
    global REPOSITORY_NAME
    REPOSITORY_NAME = "Repository"

    configure_oai()

    assert OAISERVER_REPOSITORY_NAME == "Repository"  # noqa: F821


def test_vocabulary():
    """Several vocabulary definitions are retained."""
    global INVENIO_VOCABULARY_TYPE_METADATA
    INVENIO_VOCABULARY_TYPE_METADATA = {}

    configure_vocabulary("subjects", name="Subjects")
    configure_vocabulary("funders", name="Funders")

    assert INVENIO_VOCABULARY_TYPE_METADATA == {  # noqa: F821
        "subjects": {"name": "Subjects"},
        "funders": {"name": "Funders"},
    }
