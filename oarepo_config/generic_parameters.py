#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Generic configuration parameters for oarepo-config."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from flask import current_app
from invenio_oauthclient.views.client import auto_redirect_login
from werkzeug.local import LocalProxy

from .base import (
    load_configuration_variables,
    merge_with_caller,
    set_constants_in_caller,
)


def configure_global_logging() -> None:
    """Configure global logging settings."""
    import logging
    import os

    log_level = os.environ.get("PYTHON_DEFAULT_LOG_LEVEL", None)
    if log_level is not None:
        try:
            normalized_log_level = log_level.upper().strip()
            logging.basicConfig(level=normalized_log_level)
            logging.getLogger().setLevel(normalized_log_level)
        except ValueError:
            logging.basicConfig(level=logging.INFO)
            logging.getLogger().setLevel(logging.INFO)
            logging.getLogger().exception("Invalid log level: %s, setting to INFO", log_level)


def configure_generic_parameters(  # noqa PLR0915
    languages: tuple[tuple[str, str], ...] = (("en", "English"),),
    use_path_pid_ids: bool = False,
) -> None:
    """Set up the core, infrastructure-level configuration of the repository.

    This is the main "plumbing" function that should normally be called
    first, before any of the other ``configure_*`` functions. It reads
    most of its values from the deployment's environment configuration
    (the ``variables``/``.env`` files or process environment variables,
    all prefixed with ``INVENIO_``) and uses them to configure:

    * the site's public URLs, and allowed security headers
    * whether local login/registration/password-reset is available
    * the database, search engine (OpenSearch), file storage (S3),
      cache and message queue (Redis/RabbitMQ) connections
    * translation/locale and file-upload defaults
    * default identifier schemes recognised for names, funders and
      affiliations (e.g. ORCID, ROR, VEDIDK, Scopus author ID)

    Because most values come from the environment, this function will
    fail to start the application if a required ``INVENIO_...`` variable
    is missing from the deployment's configuration - see the project's
    README for the full list of variables it expects.

    Args:
        languages: Extra UI languages to offer, as a tuple of
            ``(language_code, label)`` pairs, e.g.
            ``(("cs", _("Czech")), ("de", _("German")))``. English is
            always available and does not need to be listed.
        use_path_pid_ids: Set this to ``True`` only if your repository
            uses record identifiers that themselves contain a slash
            (``/``); it adjusts the URLs used for managing record access
            so that such identifiers keep working.

    Invenio configuration variables set, grouped by area:

    Public URLs & security headers
        * ``APP_ALLOWED_HOSTS``
        * ``SITE_UI_URL``, ``SITE_API_URL``
        * ``APP_DEFAULT_SECURE_HEADERS``

    Local login & accounts
        * ``ACCOUNTS_LOCAL_LOGIN_ENABLED``, ``SECURITY_REGISTERABLE``,
          ``SECURITY_RECOVERABLE``, ``SECURITY_CHANGEABLE``,
          ``SECURITY_CONFIRMABLE``,
          ``SECURITY_LOGIN_WITHOUT_CONFIRMATION``
        * ``SESSION_COOKIE_SECURE``
        * ``RATELIMIT_GUEST_USER``, ``RATELIMIT_AUTHENTICATED_USER``
        * ``OAUTHCLIENT_REMOTE_APPS`` - starts out empty here; extended
          by :func:`configure_einfra_oidc` if used.
        * ``ACCOUNTS_LOGIN_VIEW_FUNCTION``,
          ``OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN``

    Database
        * ``SQLALCHEMY_DATABASE_URI``

    Translation/locale
        * ``BABEL_DEFAULT_LOCALE``, ``BABEL_DEFAULT_TIMEZONE``,
          ``I18N_LANGUAGES``

    Files & storage
        * ``SEND_FILE_MAX_AGE_DEFAULT``, ``FILES_REST_STORAGE_FACTORY``
        * ``S3_ENDPOINT_URL``, ``S3_ACCESS_KEY_ID``,
          ``S3_SECRET_ACCESS_KEY``
        * ``FILES_REST_STORAGE_CLASS_LIST``,
          ``FILES_REST_DEFAULT_STORAGE_CLASS``,
          ``FILES_REST_DEFAULT_QUOTA_SIZE``
        * ``APP_RDM_DEPOSIT_FORM_QUOTA``

    User profiles
        * ``USERPROFILES_READ_ONLY``

    OAI-PMH
        * ``OAISERVER_ID_PREFIX``

    Search (OpenSearch)
        * ``SEARCH_INDEX_PREFIX``, ``SEARCH_HOSTS``,
          ``SEARCH_CLIENT_CONFIG``
        * ``VOCABULARIES_SERVICE_CONFIG``,
          ``VOCABULARIES_RESOURCE_CONFIG`` - only if the optional
          ``oarepo_vocabularies`` package is installed.

    Caches (Redis)
        * ``INVENIO_CACHE_TYPE``, ``CACHE_REDIS_URL``,
          ``ACCOUNTS_SESSION_REDIS_URL``,
          ``COMMUNITIES_IDENTITIES_CACHE_REDIS_URL``

    Background jobs (Celery/RabbitMQ)
        * ``CELERY_BROKER_URL``, ``BROKER_URL``,
          ``CELERY_RESULT_BACKEND``

    JSON schemas
        * ``RECORDS_REFRESOLVER_CLS``, ``RECORDS_REFRESOLVER_STORE``,
          ``JSONSCHEMAS_HOST``

    Secrets
        * ``SECRET_KEY``

    Records/REST compatibility
        * ``DASHBOARD_RECORD_CREATE_URL``, ``RECORD_ROUTES``,
          ``RECORDS_REST_ENDPOINTS``

    DataCite/DOIs
        * ``DATACITE_TEST_MODE``

    Mail
        * ``MAIL_DEFAULT_SENDER``
        * ``MAIL_SUPPRESS_SEND`` - only if ``INVENIO_MAIL_SUPPRESS_SEND``
          is set in the environment.

    Identifier/name/funder/affiliation vocabularies
        * ``VOCABULARIES_NAMES_SCHEMES``, ``VOCABULARIES_FUNDER_SCHEMES``,
          ``VOCABULARIES_AFFILIATION_SCHEMES`` - merged with any
          existing value.
        * ``APP_RDM_IDENTIFIER_SCHEMES_UI``
        * ``VOCABULARIES_DATASTREAM_READERS``,
          ``VOCABULARIES_DATASTREAM_WRITERS``,
          ``VOCABULARIES_DATASTREAM_TRANSFORMERS`` - seeded from
          ``invenio-app-rdm``'s defaults, merged with any existing
          value; see :func:`configure_datastreams` to add your own.

    Miscellaneous
        * ``ROR_CLIENT_ID``, ``SESSION_COOKIE_DOMAIN``,
          ``COLLECT_STORAGE``

    In addition, if ``use_path_pid_ids`` is ``True``, this patches the
    ``url_prefix`` of ``RDMParentRecordLinksResourceConfig``,
    ``RDMParentGrantsResourceConfig``, ``RDMGrantUserAccessResourceConfig``
    and ``RDMGrantGroupAccessResourceConfig`` directly - this is a class
    attribute change, not a new ``invenio.cfg`` variable.

    Example:

    .. code-block:: python

        config.configure_generic_parameters(
            languages=(
                ("cs", _("Czech")),
                ("de", _("German")),
            ),
        )

    """
    # see https://inveniordm.docs.cern.ch/install/configuration/ for the meaning
    # of the variables here

    env = load_configuration_variables()
    configure_global_logging()

    # generic
    APP_ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1"]  # noqa S104
    SITE_UI_URL = env.get("INVENIO_SITE_UI_URL", None) or f"https://{env.INVENIO_UI_HOST}:{env.INVENIO_UI_PORT}"
    SITE_API_URL = env.get("INVENIO_SITE_API_URL", None) or f"https://{env.INVENIO_API_HOST}:{env.INVENIO_API_PORT}/api"

    # security
    APP_DEFAULT_SECURE_HEADERS: dict[str, Any] = {
        "content_security_policy": {
            "default-src": [
                "'self'",
                "fonts.googleapis.com",  # for fonts
                "*.gstatic.com",  # for fonts
                "data:",  # for fonts
                "'unsafe-inline'",  # for inline scripts and styles
                "blob:",  # for pdf preview
                # Add your own policies here (e.g. analytics)
            ],
            "script-src": [
                "'self'",
                "blob:",
                "'wasm-unsafe-eval'",  # for WASM-based workers and file uploads
                # Multipart file uploads use a Web Worker running `hash-wasm` to compute content checksums
                # (e.g., MD5) of uploaded parts. This requires both 'blob:' and 'wasm-unsafe-eval'
                # enabled in `script-src`.
            ],
        },
        "content_security_policy_report_only": False,
        "content_security_policy_report_uri": None,
        "force_file_save": False,
        "force_https": True,
        "force_https_permanent": False,
        "frame_options": "sameorigin",
        "frame_options_allow_from": None,
        "session_cookie_http_only": True,
        "session_cookie_secure": True,
        "strict_transport_security": True,
        "strict_transport_security_include_subdomains": True,
        "strict_transport_security_max_age": 31556926,  # One year in seconds
        "strict_transport_security_preload": False,
    }
    # enable local login
    ACCOUNTS_LOCAL_LOGIN_ENABLED = env.INVENIO_ACCOUNTS_LOCAL_LOGIN_ENABLED
    # local login: allow users to register
    SECURITY_REGISTERABLE = env.INVENIO_SECURITY_REGISTERABLE
    # local login: allow users to reset the password
    SECURITY_RECOVERABLE = env.INVENIO_SECURITY_RECOVERABLE
    # local login: allow users to change psw
    SECURITY_CHANGEABLE = env.INVENIO_SECURITY_CHANGEABLE
    # local login: users can confirm e-mail address
    SECURITY_CONFIRMABLE = env.INVENIO_SECURITY_CONFIRMABLE
    # require users to confirm email before being able to login
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = env.INVENIO_SECURITY_LOGIN_WITHOUT_CONFIRMATION
    SESSION_COOKIE_SECURE = True

    # user security settings
    RATELIMIT_GUEST_USER = "5000 per hour;500 per minute"
    RATELIMIT_AUTHENTICATED_USER = "20000 per hour;2000 per minute"
    OAUTHCLIENT_REMOTE_APPS: dict[str, Any] = {}  # configure external login providers
    ACCOUNTS_LOGIN_VIEW_FUNCTION = auto_redirect_login  # autoredirect to external login if enabled
    OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN = True  # autoredirect to external login

    # database
    SQLALCHEMY_DATABASE_URI = env.get("INVENIO_SQLALCHEMY_DATABASE_URI", None) or (
        "postgresql+psycopg2://"
        f"{env.INVENIO_DATABASE_USER}:{env.INVENIO_DATABASE_PASSWORD}"
        f"@{env.INVENIO_DATABASE_HOST}:{env.INVENIO_DATABASE_PORT}"
        f"/{env.INVENIO_DATABASE_DBNAME}"
    )

    # i18n
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "Europe/Prague"
    I18N_LANGUAGES = list(languages)

    # files
    SEND_FILE_MAX_AGE_DEFAULT = 300
    FILES_REST_STORAGE_FACTORY = "invenio_s3.s3fs_storage_factory"
    S3_ENDPOINT_URL = env.get("INVENIO_S3_ENDPOINT_URL", None) or (
        f"{env.INVENIO_S3_PROTOCOL}://{env.INVENIO_S3_HOST}:{env.INVENIO_S3_PORT}/"
    )
    S3_ACCESS_KEY_ID = env.INVENIO_S3_ACCESS_KEY
    S3_SECRET_ACCESS_KEY = env.INVENIO_S3_SECRET_KEY
    APP_DEFAULT_SECURE_HEADERS["content_security_policy"]["default-src"].append(S3_ENDPOINT_URL)
    FILES_REST_STORAGE_CLASS_LIST = {
        "L": "Local",
    }
    FILES_REST_DEFAULT_STORAGE_CLASS = "L"

    # user profiles
    USERPROFILES_READ_ONLY = False  # allow users to change profile info (name, email, etc...)

    OAISERVER_ID_PREFIX = LocalProxy(lambda: urlparse(current_app.config["SITE_UI_URL"]).hostname or "")

    # search
    SEARCH_INDEX_PREFIX = env.INVENIO_SEARCH_INDEX_PREFIX
    SEARCH_HOSTS = [
        {"host": env.INVENIO_OPENSEARCH_HOST, "port": env.INVENIO_OPENSEARCH_PORT},
    ]
    SEARCH_CLIENT_CONFIG = {
        "use_ssl": env.INVENIO_OPENSEARCH_USE_SSL,
        "verify_certs": env.INVENIO_OPENSEARCH_VERIFY_CERTS,
        "ssl_assert_hostname": env.INVENIO_OPENSEARCH_ASSERT_HOSTNAME,
        "ssl_show_warn": env.INVENIO_OPENSEARCH_SHOW_WARN,
        "ca_certs": env.get("INVENIO_OPENSEARCH_CA_CERTS_PATH", None),
    }

    # caches
    INVENIO_CACHE_TYPE = "redis"
    CACHE_REDIS_URL = env.get("INVENIO_CACHE_REDIS_URL", None) or (
        f"redis://{env.INVENIO_REDIS_HOST}:{env.INVENIO_REDIS_PORT}/{env.INVENIO_REDIS_CACHE_DB}"
    )
    ACCOUNTS_SESSION_REDIS_URL = env.get("INVENIO_ACCOUNTS_SESSION_REDIS_URL", None) or (
        f"redis://{env.INVENIO_REDIS_HOST}:{env.INVENIO_REDIS_PORT}/{env.INVENIO_REDIS_SESSION_DB}"
    )
    COMMUNITIES_IDENTITIES_CACHE_REDIS_URL = env.get("INVENIO_COMMUNITIES_IDENTITIES_CACHE_REDIS_URL", None) or (
        f"redis://{env.INVENIO_REDIS_HOST}:{env.INVENIO_REDIS_PORT}/{env.INVENIO_REDIS_COMMUNITIES_CACHE_DB}"
    )

    # json schemas for validation
    RECORDS_REFRESOLVER_CLS = "invenio_records.resolver.InvenioRefResolver"
    RECORDS_REFRESOLVER_STORE = "invenio_jsonschemas.proxies.current_refresolver_store"
    JSONSCHEMAS_HOST = SITE_UI_URL

    # vocabularies
    try:
        from oarepo_vocabularies.resources.config import VocabulariesResourceConfig
        from oarepo_vocabularies.services.config import VocabulariesConfig

        VOCABULARIES_SERVICE_CONFIG = VocabulariesConfig
        VOCABULARIES_RESOURCE_CONFIG = VocabulariesResourceConfig
    except ImportError:
        # keep the default Invenio vocabularies config
        pass

    # Redis port redirection
    # ---------------------
    CELERY_BROKER_URL = env.get("INVENIO_CELERY_BROKER_URL", None) or (
        f"amqp://{env.INVENIO_RABBIT_USER}:{env.INVENIO_RABBIT_PASSWORD}"
        f"@{env.INVENIO_RABBIT_HOST}:{env.INVENIO_RABBIT_PORT}/"
    )
    BROKER_URL = CELERY_BROKER_URL
    CELERY_RESULT_BACKEND = env.get("INVENIO_CELERY_RESULT_BACKEND", None) or (
        f"redis://{env.INVENIO_REDIS_HOST}:{env.INVENIO_REDIS_PORT}/{env.INVENIO_REDIS_CELERY_RESULT_DB}"
    )

    # Instance secret key, used to encrypt stuff (for example, access tokens) inside database
    SECRET_KEY = env.INVENIO_SECRET_KEY

    DASHBOARD_RECORD_CREATE_URL = None

    # Do not add default records as we provide our own compatibility layer
    RECORD_ROUTES: dict = {}  # type: ignore[var-annotated]
    RECORDS_REST_ENDPOINTS: dict = {}  # type: ignore[var-annotated]

    # datacite & dois default
    DATACITE_TEST_MODE = True

    MAIL_DEFAULT_SENDER = env.get(
        "INVENIO_MAIL_DEFAULT_SENDER",
        "please-set-invenio_mail_default_sender@test.com",
    )

    if env.get("INVENIO_MAIL_SUPPRESS_SEND", None) is not None:
        MAIL_SUPPRESS_SEND = env.get("INVENIO_MAIL_SUPPRESS_SEND", True)

    # default schemes for identifiers
    from invenio_vocabularies import config as vocab_config

    from .initial_rdm_config import is_researcher_id, is_scopus_id, is_vedidk

    VOCABULARIES_NAMES_SCHEMES = merge_with_caller(
        "VOCABULARIES_NAMES_SCHEMES",
        {
            **vocab_config.VOCABULARIES_NAMES_SCHEMES,
            "vedidk": {"label": "VEDIDK", "validator": is_vedidk},
            "scopusId": {"label": "Scopus ID", "validator": is_scopus_id},
            "researcherId": {"label": "Researcher ID", "validator": is_researcher_id},
        },
    )

    # adding crossrefFunderId to funder schemes
    VOCABULARIES_FUNDER_SCHEMES = merge_with_caller(
        "VOCABULARIES_FUNDER_SCHEMES",
        {
            **vocab_config.VOCABULARIES_FUNDER_SCHEMES,
            "crossrefFunderId": {
                "label": "CrossrefFunderID",
                "validator": lambda _: True,
            },
        },
    )

    # List of affiliations is curated, validators are not needed.
    VOCABULARIES_AFFILIATION_SCHEMES = merge_with_caller(
        "VOCABULARIES_AFFILIATION_SCHEMES",
        {
            **vocab_config.VOCABULARIES_AFFILIATION_SCHEMES,
            "ico": {"label": "ICO", "validator": lambda _: True},
            "url": {"label": "URL", "validator": lambda _: True},
        },
    )

    from invenio_app_rdm import config as app_rdm_config

    FILES_REST_DEFAULT_QUOTA_SIZE = 10**10

    APP_RDM_DEPOSIT_FORM_QUOTA = {
        "maxFiles": 10,
        "maxStorage": FILES_REST_DEFAULT_QUOTA_SIZE,
    }

    APP_RDM_IDENTIFIER_SCHEMES_UI = {
        "orcid": {
            "url_prefix": "http://orcid.org/",
            "icon": "images/orcid.svg",
            "label": "ORCID",
        },
        "ror": {
            "url_prefix": "https://ror.org/",
            "icon": "images/ror-icon.svg",
            "label": "ROR",
        },
        "gnd": {
            "url_prefix": "http://d-nb.info/gnd/",
            "icon": "images/gnd-icon.svg",
            "label": "GND",
        },
    }

    VOCABULARIES_DATASTREAM_READERS = merge_with_caller(
        "VOCABULARIES_DATASTREAM_READERS",
        app_rdm_config.VOCABULARIES_DATASTREAM_READERS,
    )
    VOCABULARIES_DATASTREAM_WRITERS = merge_with_caller(
        "VOCABULARIES_DATASTREAM_WRITERS",
        app_rdm_config.VOCABULARIES_DATASTREAM_WRITERS,
    )
    VOCABULARIES_DATASTREAM_TRANSFORMERS = merge_with_caller(
        "VOCABULARIES_DATASTREAM_TRANSFORMERS",
        app_rdm_config.VOCABULARIES_DATASTREAM_TRANSFORMERS,
    )

    if use_path_pid_ids:
        from invenio_rdm_records.resources.config import (
            RDMGrantGroupAccessResourceConfig,
            RDMGrantUserAccessResourceConfig,
            RDMParentGrantsResourceConfig,
            RDMParentRecordLinksResourceConfig,
        )

        RDMParentRecordLinksResourceConfig.url_prefix = "/records/<path:pid_value>/access"
        RDMParentGrantsResourceConfig.url_prefix = "/records/<path:pid_value>/access"
        RDMGrantUserAccessResourceConfig.url_prefix = "/records/<path:pid_value>/access"
        RDMGrantGroupAccessResourceConfig.url_prefix = "/records/<path:pid_value>/access"

    OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN = False

    # ROR client id - not used for authentication, just to increase rate limits
    ROR_CLIENT_ID = "3764CLXJ4R9GT9L496QSKU2G3ZWVF71A"
    SESSION_COOKIE_DOMAIN = None
    # Flask-Collect configured to not use symlinks, as they can break the build due to duplicate static assets.
    COLLECT_STORAGE = "flask_collect.storage.file"

    import os
    import platform

    if Path("/opt/homebrew/lib").exists() and platform.system() == "Darwin":
        os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib"
    set_constants_in_caller(locals())
