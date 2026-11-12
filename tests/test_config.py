# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Tests for standalone configuration helpers."""

from __future__ import annotations

import sys

from oarepo_config import generic_parameters, ui
from oarepo_config.base import DictWithGetAttr
from oarepo_config.communities import configure_communities
from oarepo_config.cron import configure_cron
from oarepo_config.datastreams import configure_datastreams
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
    globals().pop("CELERY_BEAT_SCHEDULE", None)
    globals().pop("COMMUNITIES_COLLECTIONS_ENABLED", None)

    configure_cron(custom={"task": "example.task"})

    assert CELERY_BEAT_SCHEDULE["custom"]["task"] == "example.task"  # noqa: F821
    assert "indexer" in CELERY_BEAT_SCHEDULE  # noqa: F821
    # opt-in jobs stay off
    assert "file-checks" not in CELERY_BEAT_SCHEDULE  # noqa: F821
    assert "file-integrity-report" not in CELERY_BEAT_SCHEDULE  # noqa: F821
    assert "update-collections-size" not in CELERY_BEAT_SCHEDULE  # noqa: F821


def test_cron_matches_upstream_schedule():
    """Every job InvenioRDM schedules is scheduled here too, unless deliberately left out."""
    from invenio_app_rdm.config import CELERY_BEAT_SCHEDULE as upstream_schedule

    globals().pop("CELERY_BEAT_SCHEDULE", None)
    globals()["COMMUNITIES_COLLECTIONS_ENABLED"] = True
    try:
        configure_cron(file_integrity_check_days=14)
    finally:
        globals().pop("COMMUNITIES_COLLECTIONS_ENABLED", None)

    scheduled_tasks = {job["task"] for job in CELERY_BEAT_SCHEDULE.values()}  # noqa: F821
    upstream_tasks = {job["task"] for job in upstream_schedule.values()}
    # OARepo models do not index usage statistics into record documents
    deliberately_left_out = {"invenio_rdm_records.services.tasks.reindex_stats"}

    assert upstream_tasks - scheduled_tasks == deliberately_left_out
    assert CELERY_BEAT_SCHEDULE["file-checks"] == upstream_schedule["file-checks"]  # noqa: F821


def test_cron_file_integrity_checks():
    """Fixity checking is spread over the requested number of days."""
    import pytest

    globals().pop("CELERY_BEAT_SCHEDULE", None)

    configure_cron(file_integrity_check_days=180)

    assert CELERY_BEAT_SCHEDULE["file-checks"]["kwargs"]["frequency"] == {"days": 180}  # noqa: F821
    assert "file-integrity-report" in CELERY_BEAT_SCHEDULE  # noqa: F821

    with pytest.raises(ValueError, match="file_integrity_check_days"):
        configure_cron(file_integrity_check_days=0)


def test_cron_all_tasks_importable():
    """A typo in a task path would only surface as a silently skipped beat job."""
    from importlib import import_module

    globals().pop("CELERY_BEAT_SCHEDULE", None)
    globals()["COMMUNITIES_COLLECTIONS_ENABLED"] = True
    try:
        configure_cron(file_integrity_check_days=14)
    finally:
        globals().pop("COMMUNITIES_COLLECTIONS_ENABLED", None)

    for name, job in CELERY_BEAT_SCHEDULE.items():  # noqa: F821
        module_name, _, task_name = job["task"].rpartition(".")
        assert hasattr(import_module(module_name), task_name), name


def test_datastreams():
    """Custom datastream implementations are merged into existing ones."""
    globals()["VOCABULARIES_DATASTREAM_READERS"] = {"old": str}

    configure_datastreams(readers={"new": int}, writers={"write": list}, transformers={"transform": dict})

    assert {"old": str, "new": int} == globals()["VOCABULARIES_DATASTREAM_READERS"]
    assert {"write": list} == VOCABULARIES_DATASTREAM_WRITERS  # noqa: F821
    assert {"transform": dict} == VOCABULARIES_DATASTREAM_TRANSFORMERS  # noqa: F821


def test_jobs():
    """Custom job settings override the helper defaults."""
    import json

    # for test reasons something that can be imported
    configure_jobs(permission_policy="json.dumps", logging_level="DEBUG")

    assert json.dumps == APP_LOGS_PERMISSION_POLICY  # noqa: F821
    assert JOBS_LOGGING_LEVEL == "DEBUG"  # noqa: F821


def test_oai():
    """OAI uses the configured repository name."""
    globals()["REPOSITORY_NAME"] = "Repository"
    globals().pop("REPOSITORY_SUPPORT_CONTACT", None)
    globals().pop("OAISERVER_ADMIN_EMAILS", None)

    configure_oai()

    assert globals()["OAISERVER_REPOSITORY_NAME"] == "Repository"
    assert OAISERVER_PAGE_SIZE == 50  # noqa: F821
    assert OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME == 120  # noqa: F821
    # no contact known: invenio-oaiserver's own value is left untouched
    assert "OAISERVER_ADMIN_EMAILS" not in globals()


def test_oai_admin_emails():
    """The administrator contact comes from the argument or from the support contact."""
    globals()["REPOSITORY_NAME"] = "Repository"

    globals()["REPOSITORY_SUPPORT_CONTACT"] = "support@example.com"
    configure_oai()
    assert globals()["OAISERVER_ADMIN_EMAILS"] == ["support@example.com"]

    # a support contact that is not a bare e-mail address is not announced
    globals().pop("OAISERVER_ADMIN_EMAILS")
    globals()["REPOSITORY_SUPPORT_CONTACT"] = "Call us or write to support@example.com"
    configure_oai()
    assert "OAISERVER_ADMIN_EMAILS" not in globals()

    configure_oai(admin_emails="admin@example.com", page_size=10, resumption_token_expire_time=60)
    assert globals()["OAISERVER_ADMIN_EMAILS"] == ["admin@example.com"]
    assert OAISERVER_PAGE_SIZE == 10  # noqa: F821
    assert OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME == 60  # noqa: F821

    configure_oai(admin_emails=("a@example.com", "b@example.com"))
    assert globals()["OAISERVER_ADMIN_EMAILS"] == ["a@example.com", "b@example.com"]


def test_oai_repository_name():
    """An explicit name wins and does not need configure_ui to have run."""
    globals().pop("REPOSITORY_NAME", None)

    configure_oai(repository_name="Harvestable Repository", admin_emails=["admin@example.com"])

    assert globals()["OAISERVER_REPOSITORY_NAME"] == "Harvestable Repository"


def test_vocabulary():
    """Several vocabulary definitions are retained."""
    configure_vocabulary("subjects", name="Subjects")
    configure_vocabulary("funders", name="Funders")

    assert globals()["INVENIO_VOCABULARY_TYPE_METADATA"] == {
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
        INVENIO_DATABASE_PASSWORD="password",  # noqa: S106
        INVENIO_DATABASE_HOST="db",
        INVENIO_DATABASE_PORT=5432,
        INVENIO_DATABASE_DBNAME="repo",
        INVENIO_S3_PROTOCOL="https",
        INVENIO_S3_HOST="s3",
        INVENIO_S3_PORT=9000,
        INVENIO_S3_ACCESS_KEY="access",
        INVENIO_S3_SECRET_KEY="secret",  # noqa: S106
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
        INVENIO_RABBIT_PASSWORD="guest",  # noqa: S106
        INVENIO_RABBIT_HOST="rabbit",
        INVENIO_RABBIT_PORT=5672,
        INVENIO_SECRET_KEY="secret",  # noqa: S106
    )
    monkeypatch.setattr(generic_parameters, "load_configuration_variables", lambda: env)

    generic_parameters.configure_generic_parameters(languages=(("cs", "Czech"),))

    assert SITE_UI_URL == "https://ui.example:443"  # noqa: F821
    assert SQLALCHEMY_DATABASE_URI.endswith("@db:5432/repo")  # noqa: F821
    assert CACHE_REDIS_URL == "redis://redis:6379/0"  # noqa: F821
    assert I18N_LANGUAGES == [("cs", "Czech")]  # noqa: F821
    # the client's own timeout applies unless the deployment asks for another one
    assert "timeout" not in SEARCH_CLIENT_CONFIG  # noqa: F821

    # InvenioRDM flavour defaults are applied along the way
    assert REST_CSRF_ENABLED is True  # noqa: F821
    assert RATELIMIT_STORAGE_URI == "redis://redis:6379/4"  # noqa: F821
    assert ACCESS_CACHE == "invenio_cache:current_cache"  # noqa: F821
    assert SQLALCHEMY_ENGINE_OPTIONS["pool_recycle"] == 3600  # noqa: F821
    # ... without clobbering what this function sets itself
    assert RATELIMIT_GUEST_USER == "5000 per hour;500 per minute"  # noqa: F821

    env["INVENIO_OPENSEARCH_TIMEOUT"] = 60
    generic_parameters.configure_generic_parameters()
    assert SEARCH_CLIENT_CONFIG["timeout"] == 60  # noqa: F821


def test_ui(monkeypatch):
    """UI configuration stores the supplied branding values."""
    global APP_DEFAULT_SECURE_HEADERS  # noqa: PLW0603
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
    global OAREPO_CHECKS_LLM_CLIENTS  # noqa: PLW0603
    OAREPO_CHECKS_LLM_CLIENTS = {}

    configure_llm(api_token="token", client_name="test", fallback_community="checks")  # noqa: S106

    assert CHECKS_ENABLED is True  # noqa: F821
    assert OAREPO_CHECKS_DEFAULT_LLM_CLIENT == "test"  # noqa: F821
    assert CHECKS_GENERIC_COMMUNITY == "checks"  # noqa: F821
    assert "test" in OAREPO_CHECKS_LLM_CLIENTS


def test_model(tmp_path, monkeypatch):
    """Models contribute their record error handlers."""
    (tmp_path / "runtime_models_demo.py").write_text("record_error_handlers = {'demo'}\n")
    monkeypatch.syspath_prepend(str(tmp_path))
    sys.modules.pop("runtime_models_demo", None)
    global RDM_RECORDS_ERROR_HANDLERS  # noqa: PLW0603
    RDM_RECORDS_ERROR_HANDLERS = {"existing"}

    add_model("demo")

    assert {"existing", "demo"} == RDM_RECORDS_ERROR_HANDLERS
