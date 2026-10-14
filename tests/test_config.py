# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Tests for standalone configuration helpers."""

from __future__ import annotations

import sys

from oarepo_config.communities import configure_communities
from oarepo_config.cron import configure_cron
from oarepo_config.datastreams import configure_datastreams
from oarepo_config import generic_parameters, ui
from oarepo_config.base import DictWithGetAttr
from oarepo_config.i18n import initialize_i18n
from oarepo_config.jobs import configure_jobs
from oarepo_config.llm import configure_llm
from oarepo_config.models import add_model
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


def test_generic(monkeypatch):
    """Generic parameters build service URLs from deployment values."""
    env = DictWithGetAttr(
        INVENIO_UI_HOST="ui.example",
        INVENIO_UI_PORT=443,
        INVENIO_API_HOST="api.example",
        INVENIO_API_PORT=443,
        INVENIO_ACCOUNTS_LOCAL_LOGIN_ENABLED=True,
        INVENIO_SECURITY_REGISTERABLE=True,
        INVENIO_SECURITY_RECOVERABLE=True,
        INVENIO_SECURITY_CHANGEABLE=True,
        INVENIO_SECURITY_CONFIRMABLE=False,
        INVENIO_SECURITY_LOGIN_WITHOUT_CONFIRMATION=True,
        INVENIO_DATABASE_USER="user",
        INVENIO_DATABASE_PASSWORD="password",
        INVENIO_DATABASE_HOST="db",
        INVENIO_DATABASE_PORT=5432,
        INVENIO_DATABASE_DBNAME="repo",
        INVENIO_S3_PROTOCOL="https",
        INVENIO_S3_HOST="s3",
        INVENIO_S3_PORT=9000,
        INVENIO_S3_ACCESS_KEY="access",
        INVENIO_S3_SECRET_KEY="secret",
        INVENIO_SEARCH_INDEX_PREFIX="repo",
        INVENIO_OPENSEARCH_HOST="search",
        INVENIO_OPENSEARCH_PORT=9200,
        INVENIO_OPENSEARCH_USE_SSL=False,
        INVENIO_OPENSEARCH_VERIFY_CERTS=False,
        INVENIO_OPENSEARCH_ASSERT_HOSTNAME=False,
        INVENIO_OPENSEARCH_SHOW_WARN=False,
        INVENIO_REDIS_HOST="redis",
        INVENIO_REDIS_PORT=6379,
        INVENIO_REDIS_CACHE_DB=0,
        INVENIO_REDIS_SESSION_DB=1,
        INVENIO_REDIS_COMMUNITIES_CACHE_DB=2,
        INVENIO_REDIS_CELERY_RESULT_DB=3,
        INVENIO_RABBIT_USER="guest",
        INVENIO_RABBIT_PASSWORD="guest",
        INVENIO_RABBIT_HOST="rabbit",
        INVENIO_RABBIT_PORT=5672,
        INVENIO_SECRET_KEY="secret",
    )
    monkeypatch.setattr(generic_parameters, "load_configuration_variables", lambda: env)

    generic_parameters.configure_generic_parameters(languages=(("cs", "Czech"),))

    assert SITE_UI_URL == "https://ui.example:443"  # noqa: F821
    assert SQLALCHEMY_DATABASE_URI.endswith("@db:5432/repo")  # noqa: F821
    assert CACHE_REDIS_URL == "redis://redis:6379/0"  # noqa: F821
    assert I18N_LANGUAGES == [("cs", "Czech")]  # noqa: F821


def test_ui(monkeypatch):
    """UI configuration stores the supplied branding values."""
    global APP_DEFAULT_SECURE_HEADERS
    APP_DEFAULT_SECURE_HEADERS = {"content_security_policy": {"default-src": []}}
    monkeypatch.setattr(
        ui,
        "load_configuration_variables",
        lambda: DictWithGetAttr(INVENIO_DEPLOYMENT_VERSION="test"),
    )

    ui.configure_ui(code="demo", name="Demo", description="Description", use_default_frontpage=True)

    assert APP_THEME == ["demo", "oarepo", "semantic-ui"]  # noqa: F821
    assert REPOSITORY_NAME == "Demo"  # noqa: F821
    assert REPOSITORY_DESCRIPTION == "Description"  # noqa: F821
    assert THEME_FRONTPAGE is True  # noqa: F821


def test_i18n():
    """I18n initialization can be enabled repeatedly."""
    initialize_i18n()


def test_llm():
    """LLM setup records the configured client without calling it."""
    global OAREPO_CHECKS_LLM_CLIENTS
    OAREPO_CHECKS_LLM_CLIENTS = {}

    configure_llm(api_token="token", client_name="test", fallback_community="checks")

    assert CHECKS_ENABLED is True  # noqa: F821
    assert OAREPO_CHECKS_DEFAULT_LLM_CLIENT == "test"  # noqa: F821
    assert CHECKS_GENERIC_COMMUNITY == "checks"  # noqa: F821
    assert "test" in OAREPO_CHECKS_LLM_CLIENTS  # noqa: F821


def test_model(tmp_path, monkeypatch):
    """Models contribute their record error handlers."""
    (tmp_path / "runtime_models_demo.py").write_text("record_error_handlers = {'demo'}\n")
    monkeypatch.syspath_prepend(str(tmp_path))
    sys.modules.pop("runtime_models_demo", None)
    global RDM_RECORDS_ERROR_HANDLERS
    RDM_RECORDS_ERROR_HANDLERS = {"existing"}

    add_model("demo")

    assert RDM_RECORDS_ERROR_HANDLERS == {"existing", "demo"}  # noqa: F821
