# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Tests for the deployment-level InvenioRDM flavour defaults and the stats helper."""

from __future__ import annotations

from invenio_app_rdm import config as app_rdm_config

from oarepo_config.rdm_defaults import (
    ratelimit_storage_uri,
    rdm_defaults,
    sqlalchemy_engine_options,
)
from oarepo_config.stats import configure_stats

REDIS_ENV = {"INVENIO_REDIS_HOST": "redis", "INVENIO_REDIS_PORT": 6379}


def test_ratelimit_storage_defaults_to_own_redis_db():
    """Rate limit counters live in Redis, away from the databases used for other things."""
    assert ratelimit_storage_uri(REDIS_ENV) == "redis://redis:6379/4"
    assert ratelimit_storage_uri({**REDIS_ENV, "INVENIO_REDIS_RATELIMIT_DB": 7}) == "redis://redis:6379/7"


def test_ratelimit_storage_follows_external_redis():
    """An externally managed Redis keeps its credentials, TLS scheme and query string."""
    env = {**REDIS_ENV, "INVENIO_CACHE_REDIS_URL": "rediss://:pass@redis.example:6380/0?ssl_cert_reqs=required"}

    assert ratelimit_storage_uri(env) == "rediss://:pass@redis.example:6380/4?ssl_cert_reqs=required"


def test_ratelimit_storage_explicit_uri_wins():
    """INVENIO_RATELIMIT_STORAGE_URI is used verbatim."""
    env = {
        **REDIS_ENV,
        "INVENIO_CACHE_REDIS_URL": "redis://other:6379/0",
        "INVENIO_RATELIMIT_STORAGE_URI": "memory://",
    }

    assert ratelimit_storage_uri(env) == "memory://"


def test_engine_options_match_upstream():
    """The pool options are the upstream ones; only the connection label is added."""
    options = sqlalchemy_engine_options({})

    connect_args = options.pop("connect_args")
    upstream = dict(app_rdm_config.SQLALCHEMY_ENGINE_OPTIONS)
    assert connect_args.pop("application_name")
    assert connect_args == upstream.pop("connect_args")
    assert options == upstream


def test_engine_options_pgbouncer():
    """With PgBouncer the application must not pool, nor pass pool-only arguments."""
    from sqlalchemy.pool import NullPool

    options = sqlalchemy_engine_options({"INVENIO_PGBOUNCER_ENABLED": True})

    assert options["poolclass"] is NullPool
    assert not {"pool_timeout", "pool_recycle", "pool_pre_ping"} & set(options)
    assert options["connect_args"]["options"] == "-c timezone=UTC"


def test_engine_options_overrides():
    """Deployment overrides are merged, connect_args key by key."""
    options = sqlalchemy_engine_options(
        {
            "INVENIO_SQLALCHEMY_ENGINE_OPTIONS": {
                "pool_pre_ping": True,
                "pool_size": 10,
                "connect_args": {"sslmode": "require"},
            }
        }
    )

    assert options["pool_pre_ping"] is True
    assert options["pool_size"] == 10
    assert options["pool_recycle"] == 3600
    assert options["connect_args"]["sslmode"] == "require"
    assert options["connect_args"]["options"] == "-c timezone=UTC"


def test_rdm_defaults():
    """Only the enforcing and deployment-dependent defaults are applied here."""
    defaults = rdm_defaults(REDIS_ENV)

    assert set(defaults) == {
        "REST_CSRF_ENABLED",
        "ACCESS_CACHE",
        "RATELIMIT_STORAGE_URI",
        "ACCOUNTS_LOGIN_RATELIMIT",
        "ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT",
        "ACCOUNTS_SEND_CONFIRMATION_RATELIMIT",
        "SQLALCHEMY_ENGINE_OPTIONS",
        "APP_RDM_ADMIN_EMAIL_RECIPIENT",
    }
    assert defaults["REST_CSRF_ENABLED"] is app_rdm_config.REST_CSRF_ENABLED is True
    assert defaults["ACCESS_CACHE"] == app_rdm_config.ACCESS_CACHE
    assert defaults["RATELIMIT_STORAGE_URI"].startswith("redis://")
    assert defaults["APP_RDM_ADMIN_EMAIL_RECIPIENT"] is None


def test_rdm_defaults_admin_recipient():
    """The integrity report recipient comes from the deployment's environment."""
    defaults = rdm_defaults({**REDIS_ENV, "INVENIO_APP_RDM_ADMIN_EMAIL_RECIPIENT": "admin@example.com"})

    assert defaults["APP_RDM_ADMIN_EMAIL_RECIPIENT"] == "admin@example.com"


def test_stats_preview_downloads():
    """Preview downloads are counted unless asked otherwise."""
    configure_stats()
    assert STATS_REGISTER_RECEIVERS is True  # noqa: F821
    assert RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS is False  # noqa: F821

    configure_stats(count_preview_downloads=False)
    assert RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS is True  # noqa: F821
