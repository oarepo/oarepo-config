# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""InvenioRDM flavour defaults that only make sense for a deployed repository.

Upstream InvenioRDM ships its instance-wide defaults in
`invenio_app_rdm.config`, which is registered as an `invenio_config.module`
entry point and therefore loaded into every InvenioRDM instance. OARepo does
not load that module (it would also drag in the stock RDM record UI, routes
and templates that OARepo replaces), so every setting from it that OARepo
still relies on has to be re-applied explicitly:

* inert and corrective defaults (error handlers, schemas, thumbnail sizes,
  per-endpoint rate limits, ...) live in `oarepo.initial_rdm_config`, and the
  sitemap of OARepo records in `oarepo_rdm.initial_config`. Both are entry
  point configuration modules, so every OARepo application gets them;
* this module carries the rest - defaults that **switch on enforcement**
  (CSRF protection, permission caching, account rate limits, database pool
  limits) or that **depend on the deployment's environment** (where the rate
  limiter keeps its counters). Applying those to every application would
  change the behaviour of each OARepo library's test suite, so they are
  applied by [`configure_generic_parameters`][oarepo_config.configure_generic_parameters],
  which only a repository's `invenio.cfg` calls.

Kept deliberately different from upstream (do not "fix" this):

* `DB_VERSIONING_USER_MODEL` - upstream sets it to `None`. It decides
  whether the SQLAlchemy-Continuum `transaction` table carries a `user_id`
  column, i.e. it is baked into the database schema of existing
  deployments and must not be flipped by a library upgrade.
"""

from __future__ import annotations

import socket
from typing import TYPE_CHECKING, Any
from urllib.parse import urlparse, urlunparse

if TYPE_CHECKING:
    from collections.abc import Mapping

# Redis database used for rate limiting counters when nothing else is
# configured. 0-3 are taken by the cache, sessions, Celery results and the
# communities identity cache in the default OARepo deployment layout.
DEFAULT_REDIS_RATELIMIT_DB = 4


def _redis_url_with_db(redis_url: str, db: Any) -> str:
    """Swap only the database number of a Redis URL, keeping scheme/auth/host/port/query."""
    return urlunparse(urlparse(redis_url)._replace(path=f"/{db}"))


def ratelimit_storage_uri(env: Mapping[str, Any]) -> str:
    """Return the Redis URL the rate limiter should keep its counters in.

    Resolution order:

    1. `INVENIO_RATELIMIT_STORAGE_URI` - used verbatim;
    2. `INVENIO_CACHE_REDIS_URL` (an externally managed Redis) - same server,
       with the database swapped for `INVENIO_REDIS_RATELIMIT_DB`;
    3. `INVENIO_REDIS_HOST`/`INVENIO_REDIS_PORT` and
       `INVENIO_REDIS_RATELIMIT_DB`.

    `INVENIO_REDIS_RATELIMIT_DB` defaults to `4`.
    """
    explicit = env.get("INVENIO_RATELIMIT_STORAGE_URI")
    if explicit:
        return str(explicit)
    db = env.get("INVENIO_REDIS_RATELIMIT_DB", DEFAULT_REDIS_RATELIMIT_DB)
    external_cache_url = env.get("INVENIO_CACHE_REDIS_URL")
    if external_cache_url:
        return _redis_url_with_db(str(external_cache_url), db)
    return f"redis://{env['INVENIO_REDIS_HOST']}:{env['INVENIO_REDIS_PORT']}/{db}"


def sqlalchemy_engine_options(env: Mapping[str, Any]) -> dict[str, Any]:
    """Return the database connection (pool) options.

    Mirrors upstream InvenioRDM, plus two things taken from Zenodo's
    production configuration: the connection is labelled with the host name
    (so that it can be told apart in `pg_stat_activity`) and connection
    pooling can be handed over to PgBouncer.

    * `INVENIO_PGBOUNCER_ENABLED=True` - do not pool connections in the
      application at all (`NullPool`), PgBouncer does it.
    * `INVENIO_SQLALCHEMY_ENGINE_OPTIONS` - a JSON object merged over the
      result, e.g. `{"pool_size": 10, "pool_pre_ping": true}`. Its
      `connect_args` are merged key by key.
    """
    options: dict[str, Any] = {
        "connect_args": {
            # Invenio expects to exchange UTC timestamps with the database in all cases
            "options": "-c timezone=UTC",
            "application_name": socket.gethostname(),
        },
    }
    if env.get("INVENIO_PGBOUNCER_ENABLED", False) is True:
        from sqlalchemy.pool import NullPool

        options["poolclass"] = NullPool
    else:
        options.update(
            {
                "pool_pre_ping": False,
                "pool_recycle": 3600,
                # fail fast rather than letting HTTP requests queue for a connection
                "pool_timeout": 10,
            }
        )

    overrides = env.get("INVENIO_SQLALCHEMY_ENGINE_OPTIONS")
    if isinstance(overrides, dict):
        overrides = dict(overrides)
        options["connect_args"].update(overrides.pop("connect_args", {}))
        options.update(overrides)
    return options


def rdm_defaults(env: Mapping[str, Any]) -> dict[str, Any]:
    """Return the InvenioRDM flavour defaults a deployed repository should run with.

    Called by [`configure_generic_parameters`][oarepo_config.configure_generic_parameters];
    anything returned here can still be overridden by a plain assignment
    further down in `invenio.cfg`.
    """
    # REST security
    # -------------
    # CSRF protection of the REST API for cookie (browser session)
    # authenticated requests. Requests carrying an API token are exempt.
    # invenio-rest leaves this off unless the flavour turns it on.
    REST_CSRF_ENABLED = True

    # Cache resolved action permissions instead of querying the database on
    # every permission check.
    ACCESS_CACHE = "invenio_cache:current_cache"

    # Rate limiting
    # -------------
    # The invenio-app default is "memory://", i.e. every web worker process
    # keeps its own counters, which multiplies the effective limits by the
    # number of processes/pods and forgets them on every restart.
    RATELIMIT_STORAGE_URI = ratelimit_storage_uri(env)

    # brute-force protection of the local account forms
    ACCOUNTS_LOGIN_RATELIMIT = "5 per minute; 30 per day"
    ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT = "3 per minute; 10 per day"  # noqa: S105
    ACCOUNTS_SEND_CONFIRMATION_RATELIMIT = "3 per minute; 10 per day"

    # Database
    # --------
    SQLALCHEMY_ENGINE_OPTIONS = sqlalchemy_engine_options(env)

    # File integrity report (see configure_cron(file_integrity_check_days=...))
    # -------------------------------------------------------------------------
    APP_RDM_ADMIN_EMAIL_RECIPIENT = env.get("INVENIO_APP_RDM_ADMIN_EMAIL_RECIPIENT", None)

    return {name: value for name, value in locals().items() if name.isupper()}
