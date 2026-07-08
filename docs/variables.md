# Configuration Variables Reference
This document lists all configuration variables used by oarepo-config and related extensions.
It is automatically generated from:
- The Flask application's configuration (via `invenio_app.factory.create_app()`)
- The docstrings in `oarepo_config/*` modules
- Configuration files from installed invenio_ and oarepo_ extensions

## How to Use This Document

1. **Summary Table**: Quickly find which configure_* functions set each variable.
2. **Detailed Reference**: For each variable, see its default value, type, source, and which configure_* functions reference it.

---

## Summary Table
| Variable Name | Type | Referenced By |
|---------------|------|---------------|
| `ACCESS_ACTION_CACHE_PREFIX` | str | - |
| `ACCESS_CACHE` | NoneType | - |
| `ACCESS_LOAD_SYSTEM_ROLE_NEEDS` | bool | - |
| `ACCOUNTS` | bool | - |
| `ACCOUNTS_BASE_TEMPLATE` | str | - |
| `ACCOUNTS_CONFIRM_EMAIL_ENDPOINT` | NoneType | - |
| `ACCOUNTS_COVER_TEMPLATE` | str | - |
| `ACCOUNTS_DEFAULT_EMAIL_VISIBILITY` | str | - |
| `ACCOUNTS_DEFAULT_USERS_VERIFIED` | bool | - |
| `ACCOUNTS_DEFAULT_USER_VISIBILITY` | str | - |
| `ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT` | NoneType | - |
| `ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_KEY_PREFIX` | str | - |
| `ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_MSG` | LazyString | - |
| `ACCOUNTS_JWT_ALOGORITHM` | str | - |
| `ACCOUNTS_JWT_CREATION_FACTORY` | str | - |
| `ACCOUNTS_JWT_DECODE_FACTORY` | str | - |
| `ACCOUNTS_JWT_DOM_TOKEN` | bool | - |
| `ACCOUNTS_JWT_DOM_TOKEN_TEMPLATE` | str | - |
| `ACCOUNTS_JWT_ENABLE` | bool | - |
| `ACCOUNTS_JWT_EXPIRATION_DELTA` | timedelta | - |
| `ACCOUNTS_JWT_SECRET_KEY` | str | - |
| `ACCOUNTS_LOCAL_LOGIN_ENABLED` | bool | `configure_generic_parameters` |
| `ACCOUNTS_LOGIN_RATELIMIT` | NoneType | - |
| `ACCOUNTS_LOGIN_RATELIMIT_KEY_PREFIX` | str | - |
| `ACCOUNTS_LOGIN_RATELIMIT_MSG` | LazyString | - |
| `ACCOUNTS_LOGIN_VIEW_FUNCTION` | unknown | `configure_generic_parameters` |
| `ACCOUNTS_REGISTER_BLUEPRINT` | NoneType | - |
| `ACCOUNTS_RESET_PASSWORD_ENDPOINT` | NoneType | - |
| `ACCOUNTS_REST_AUTH_VIEWS` | dict | - |
| `ACCOUNTS_REST_CONFIRM_EMAIL_ENDPOINT` | str | - |
| `ACCOUNTS_REST_RESET_PASSWORD_ENDPOINT` | str | - |
| `ACCOUNTS_RETENTION_PERIOD` | timedelta | - |
| `ACCOUNTS_SEND_CONFIRMATION_RATELIMIT` | NoneType | - |
| `ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_KEY_PREFIX` | str | - |
| `ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_MSG` | LazyString | - |
| `ACCOUNTS_SESSION_ACTIVITY_ENABLED` | bool | - |
| `ACCOUNTS_SESSION_REDIS_URL` | NoneType | `configure_generic_parameters` |
| `ACCOUNTS_SESSION_STORE_FACTORY` | str | - |
| `ACCOUNTS_SETTINGS_SECURITY_TEMPLATE` | str | - |
| `ACCOUNTS_SETTINGS_TEMPLATE` | str | - |
| `ACCOUNTS_SITENAME` | LazyString | - |
| `ACCOUNTS_USERINFO_HEADERS` | bool | - |
| `ACCOUNTS_USERNAME_REGEX` | str | - |
| `ACCOUNTS_USERNAME_RULES_TEXT` | LazyString | - |
| `ACCOUNTS_USER_PREFERENCES_SCHEMA` | UserPreferencesSchema | - |
| `ACCOUNTS_USER_PROFILE_SCHEMA` | UserProfileSchema | - |
| `ACCOUNTS_USE_CELERY` | bool | - |
| `ADMINISTRATION_APPNAME` | str | - |
| `ADMINISTRATION_BASE_TEMPLATE` | str | - |
| `ADMINISTRATION_DASHBOARD_VIEW` | str | - |
| `ADMINISTRATION_DISPLAY_VERSIONS` | list | - |
| `ADMINISTRATION_THEME_BASE_TEMPLATE` | str | `configure_ui` |
| `ADMIN_BASE_TEMPLATE` | str | - |
| `ALEMBIC` | dict | - |
| `ALEMBIC_CONTEXT` | dict | - |
| `ALLOWED_HTML_ATTRS` | dict | - |
| `ALLOWED_HTML_TAGS` | list | - |
| `APPLICATION_ROOT` | str | - |
| `APP_ALLOWED_HOSTS` | configured by function | `configure_generic_parameters` |
| `APP_DEFAULT_SECURE_HEADERS` | dict | `configure_ui`, `configure_generic_parameters` |
| `APP_ENABLE_SECURE_HEADERS` | bool | - |
| `APP_HEALTH_BLUEPRINT_ENABLED` | bool | - |
| `APP_LOGS_PERMISSION_POLICY` | unknown | `configure_jobs` |
| `APP_RDM_ADMIN_EMAIL_RECIPIENT` | unknown | - |
| `APP_RDM_DEPOSIT_FORM_AUTOCOMPLETE_NAMES` | unknown | - |
| `APP_RDM_DEPOSIT_FORM_CUSTOM_FIELD_DEFAULTS` | unknown | - |
| `APP_RDM_DEPOSIT_FORM_DEFAULTS` | unknown | - |
| `APP_RDM_DEPOSIT_FORM_PUBLISH_MODAL_EXTRA` | unknown | - |
| `APP_RDM_DEPOSIT_FORM_QUOTA` | unknown | `configure_generic_parameters` |
| `APP_RDM_DEPOSIT_FORM_TEMPLATE` | unknown | - |
| `APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED` | unknown | `configure_ui` |
| `APP_RDM_DETAIL_SIDE_BAR_TEMPLATES` | unknown | `configure_ui` |
| `APP_RDM_DISPLAY_DECIMAL_FILE_SIZES` | unknown | - |
| `APP_RDM_FILES_INTEGRITY_REPORT_SUBJECT` | unknown | - |
| `APP_RDM_FILES_INTEGRITY_REPORT_TEMPLATE` | unknown | - |
| `APP_RDM_IDENTIFIER_SCHEMES_UI` | unknown | `configure_generic_parameters` |
| `APP_RDM_MODERATION_REQUEST_FACETS` | dict | - |
| `APP_RDM_MODERATION_REQUEST_SEARCH` | dict | - |
| `APP_RDM_MODERATION_REQUEST_SORT_OPTIONS` | dict | - |
| `APP_RDM_PAGES` | unknown | - |
| `APP_RDM_RECORDS_EXPORT_URL` | unknown | - |
| `APP_RDM_RECORD_EXPORTERS` | unknown | - |
| `APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS` | list | - |
| `APP_RDM_RECORD_LANDING_PAGE_FAIR_SIGNPOSTING_LEVEL_1_ENABLED` | unknown | - |
| `APP_RDM_RECORD_LANDING_PAGE_TEMPLATE` | unknown | - |
| `APP_RDM_RECORD_THUMBNAIL_SIZES` | unknown | - |
| `APP_RDM_ROUTES` | dict | - |
| `APP_RDM_SUBCOMMUNITIES_LABEL` | unknown | - |
| `APP_RDM_USER_DASHBOARD_ROUTES` | dict | - |
| `APP_REQUESTID_HEADER` | str | - |
| `APP_THEME` | NoneType | `configure_ui` |
| `ASSETS_BUILDER` | configured by function | `configure_ui` |
| `AUDIT_LOGS_DISABLED_ACTIONS` | set | - |
| `AUDIT_LOGS_ENABLED` | bool | - |
| `AUDIT_LOGS_FACETS` | dict | - |
| `AUDIT_LOGS_SEARCH` | dict | - |
| `AUDIT_LOGS_SORT_OPTIONS` | dict | - |
| `BABEL_DEFAULT_LOCALE` | str | `configure_generic_parameters` |
| `BABEL_DEFAULT_TIMEZONE` | unknown | `configure_generic_parameters` |
| `BANNERS_CATEGORIES` | list | - |
| `BANNERS_CATEGORIES_TO_STYLE` | unknown | - |
| `BANNERS_SEARCH` | dict | - |
| `BANNERS_SORT_OPTIONS` | dict | - |
| `BASE_TEMPLATE` | str | `configure_ui` |
| `BROKER_URL` | str | `configure_generic_parameters` |
| `CACHE_IS_AUTHENTICATED_CALLBACK` | NoneType | - |
| `CACHE_KEY_PREFIX` | str | - |
| `CACHE_REDIS_URL` | str | `configure_generic_parameters` |
| `CACHE_TYPE` | str | - |
| `CELERY_ACCEPT_CONTENT` | list | - |
| `CELERY_ALWAYS_EAGER` | bool | - |
| `CELERY_BEAT_SCHEDULE` | unknown | `configure_cron` |
| `CELERY_BROKER_URL` | str | `configure_generic_parameters` |
| `CELERY_RESULT_BACKEND` | str | `configure_generic_parameters` |
| `CELERY_RESULT_SERIALIZER` | str | - |
| `CELERY_TASK_SERIALIZER` | str | - |
| `CELERY_WORKER_CONCURRENCY` | int | - |
| `CELERY_WORKER_POOL` | str | - |
| `CHECKS_ENABLED` | bool | - |
| `COLLECTIONS_MAX_COLLECTIONS_PER_TREE` | int | - |
| `COLLECTIONS_MAX_DEPTH` | int | - |
| `COLLECTIONS_MAX_TREES` | int | - |
| `COLLECTIONS_PERMISSION_POLICY` | unknown | - |
| `COLLECT_STATIC_ROOT` | str | - |
| `COLLECT_STORAGE` | str | `configure_generic_parameters` |
| `COMMUNITIES_ALLOW_MEMBERSHIP_REQUESTS` | bool | - |
| `COMMUNITIES_ALLOW_RESTRICTED` | bool | - |
| `COMMUNITIES_ALWAYS_SHOW_CREATE_LINK` | bool | - |
| `COMMUNITIES_COLLECTIONS_ENABLED` | bool | - |
| `COMMUNITIES_CUSTOM_FIELDS` | list | - |
| `COMMUNITIES_CUSTOM_FIELDS_UI` | list | - |
| `COMMUNITIES_DEFAULT_RECORD_SUBMISSION_POLICY` | RecordSubmissionPolicyEnum | - |
| `COMMUNITIES_ERROR_HANDLERS` | unknown | - |
| `COMMUNITIES_FACETS` | dict | - |
| `COMMUNITIES_IDENTITIES_CACHE_HANDLER` | str | - |
| `COMMUNITIES_IDENTITIES_CACHE_REDIS_URL` | str | `configure_generic_parameters` |
| `COMMUNITIES_IDENTITIES_CACHE_TIME` | int | - |
| `COMMUNITIES_INVITATIONS_EXPIRES_IN` | timedelta | - |
| `COMMUNITIES_INVITATIONS_SEARCH` | dict | - |
| `COMMUNITIES_INVITATIONS_SORT_OPTIONS` | dict | - |
| `COMMUNITIES_LOGO_MAX_FILE_SIZE` | int | - |
| `COMMUNITIES_MEMBERSHIP_REQUESTS_EXPIRES_IN` | timedelta | - |
| `COMMUNITIES_MEMBERSHIP_REQUESTS_FACETS` | dict | - |
| `COMMUNITIES_MEMBERSHIP_REQUESTS_SEARCH` | dict | - |
| `COMMUNITIES_MEMBERS_FACETS` | dict | - |
| `COMMUNITIES_MEMBERS_SEARCH` | dict | - |
| `COMMUNITIES_MEMBERS_SORT_OPTIONS` | dict | - |
| `COMMUNITIES_NAMESPACES` | dict | - |
| `COMMUNITIES_OAI_SETS_PREFIX` | str | - |
| `COMMUNITIES_PERMISSION_POLICY` | configured by function | `configure_communities` |
| `COMMUNITIES_RECORDS_SEARCH` | dict | - |
| `COMMUNITIES_REGISTER_UI_BLUEPRINT` | configured by function | `configure_communities` |
| `COMMUNITIES_REQUESTS_SEARCH` | dict | - |
| `COMMUNITIES_ROLES` | list | `configure_communities` |
| `COMMUNITIES_ROUTES` | dict | - |
| `COMMUNITIES_SEARCH` | dict | - |
| `COMMUNITIES_SEARCH_SORT_BY_VERIFIED` | bool | - |
| `COMMUNITIES_SERVICE_COMPONENTS` | unknown | - |
| `COMMUNITIES_SORT_OPTIONS` | dict | - |
| `COMMUNITIES_SUBCOMMUNITIES_FACETS` | dict | - |
| `COMMUNITIES_SUBCOMMUNITIES_SEARCH` | dict | - |
| `COMMUNITIES_SUB_INVITATION_REQUEST_CLS` | unknown | - |
| `COMMUNITIES_SUB_REQUEST_CLS` | unknown | - |
| `CORS_EXPOSE_HEADERS` | unknown | - |
| `CORS_RESOURCES` | unknown | - |
| `CORS_SEND_WILDCARD` | unknown | - |
| `COVER_TEMPLATE` | str | `configure_ui` |
| `CROSSREF_ADDITIONAL_PREFIXES` | list | - |
| `CROSSREF_DEPOSITOR` | str | - |
| `CROSSREF_EMAIL` | str | - |
| `CROSSREF_ENABLED` | bool | - |
| `CROSSREF_FORMAT` | str | - |
| `CROSSREF_PASSWORD` | str | - |
| `CROSSREF_PREFIX` | str | - |
| `CROSSREF_REGISTRANT` | str | - |
| `CROSSREF_TEST_MODE` | bool | - |
| `CROSSREF_USERNAME` | str | - |
| `CSRF_ALLOWED_CHARS` | str | - |
| `CSRF_COOKIE_NAME` | str | - |
| `CSRF_COOKIE_SAMESITE` | str | - |
| `CSRF_FORCE_SECURE_REFERER` | bool | - |
| `CSRF_HEADER` | str | - |
| `CSRF_METHODS` | list | - |
| `CSRF_SECRET_SALT` | str | - |
| `CSRF_TOKEN_EXPIRES_IN` | int | - |
| `CSRF_TOKEN_GRACE_PERIOD` | int | - |
| `CSRF_TOKEN_LENGTH` | int | - |
| `DASHBOARD_RECORD_CREATE_URL` | configured by function | `configure_ui`, `configure_generic_parameters` |
| `DATACITE_ADDITIONAL_PREFIXES` | list | - |
| `DATACITE_DATACENTER_SYMBOL` | str | - |
| `DATACITE_ENABLED` | bool | - |
| `DATACITE_FORMAT` | str | - |
| `DATACITE_PASSWORD` | str | - |
| `DATACITE_PREFIX` | str | - |
| `DATACITE_TEST_MODE` | bool | `configure_generic_parameters` |
| `DATACITE_USERNAME` | str | - |
| `DB_VERSIONING` | bool | - |
| `DB_VERSIONING_USER_MODEL` | unknown | - |
| `DEBUG` | bool | - |
| `DEBUG_TB_INTERCEPT_REDIRECTS` | unknown | - |
| `DEPLOYMENT_VERSION` | configured by function | `configure_ui` |
| `EINFRA` | configured by function | `configure_einfra_oidc` |
| `EINFRA_LOGIN_APP` | configured by function | `configure_einfra_oidc` |
| `EXPLAIN_TEMPLATE_LOADING` | bool | - |
| `FILES_REST_ALLOW_RANGE_REQUESTS` | bool | - |
| `FILES_REST_CHECKSUM_VERIFICATION_URI_PREFIXES` | unknown | - |
| `FILES_REST_DEFAULT_MAX_FILE_SIZE` | NoneType | - |
| `FILES_REST_DEFAULT_QUOTA_SIZE` | NoneType | `configure_generic_parameters` |
| `FILES_REST_DEFAULT_STORAGE_CLASS` | str | `configure_generic_parameters` |
| `FILES_REST_FILE_TAGS_HEADER` | str | - |
| `FILES_REST_FILE_URI_MAX_LEN` | int | - |
| `FILES_REST_MIN_FILE_SIZE` | int | - |
| `FILES_REST_MULTIPART_CHUNKSIZE_MAX` | int | - |
| `FILES_REST_MULTIPART_CHUNKSIZE_MIN` | int | - |
| `FILES_REST_MULTIPART_EXPIRES` | timedelta | - |
| `FILES_REST_MULTIPART_MAX_PARTS` | int | - |
| `FILES_REST_MULTIPART_PART_FACTORIES` | list | - |
| `FILES_REST_OBJECT_KEY_MAX_LEN` | int | - |
| `FILES_REST_PERMISSION_FACTORY` | str | - |
| `FILES_REST_SIZE_LIMITERS` | str | - |
| `FILES_REST_STORAGE_CLASS_LIST` | dict | `configure_generic_parameters` |
| `FILES_REST_STORAGE_FACTORY` | str | `configure_generic_parameters` |
| `FILES_REST_STORAGE_PATH_DIMENSIONS` | int | - |
| `FILES_REST_STORAGE_PATH_SPLIT_LENGTH` | int | - |
| `FILES_REST_TASK_WAIT_INTERVAL` | int | - |
| `FILES_REST_TASK_WAIT_MAX_SECONDS` | int | - |
| `FILES_REST_UPLOAD_FACTORIES` | list | - |
| `FILES_REST_XSENDFILE_ENABLED` | bool | - |
| `FILES_REST_XSENDFILE_RESPONSE_FUNC` | unknown | - |
| `FORMATTER_BADGES_ALLOWED_TITLES` | list | - |
| `FORMATTER_BADGES_ENABLE` | bool | - |
| `FORMATTER_BADGES_MAX_CACHE_AGE` | int | - |
| `FORMATTER_BADGES_TITLE_MAPPING` | dict | - |
| `GLOBAL_SEARCH_MODELS` | configured by function | `add_model` |
| `HEADER_TEMPLATE` | unknown | `configure_ui` |
| `I18N_DEFAULT_REDIRECT_ENDPOINT` | NoneType | - |
| `I18N_JS_DISTR_EXCEPTIONAL_PACKAGE_MAP` | dict | - |
| `I18N_LANGUAGES` | list | `configure_generic_parameters` |
| `I18N_SESSION_KEY` | str | - |
| `I18N_SET_LANGUAGE_URL` | str | - |
| `I18N_TRANSIFEX_JS_RESOURCES_MAP` | dict | - |
| `I18N_TRANSLATIONS_PATHS` | list | - |
| `I18N_USER_LANG_ATTR` | str | - |
| `IIIF_API_DECORATOR_HANDLER` | unknown | - |
| `IIIF_API_INFO_RESPONSE_SKELETON` | dict | - |
| `IIIF_CACHE_HANDLER` | str | - |
| `IIIF_CACHE_IGNORE_ERRORS` | bool | - |
| `IIIF_CACHE_REDIS_URL` | str | - |
| `IIIF_CACHE_TIME` | int | - |
| `IIIF_CONVERTERS` | tuple | - |
| `IIIF_FORMATS` | dict | - |
| `IIIF_FORMATS_PIL_MAP` | dict | - |
| `IIIF_GIF_TEMP_FOLDER_PATH` | str | - |
| `IIIF_MODE` | dict | - |
| `IIIF_PREVIEW_TEMPLATE` | str | - |
| `IIIF_QUALITIES` | tuple | - |
| `IIIF_SIMPLE_PREVIEWER_NATIVE_EXTENSIONS` | list | - |
| `IIIF_SIMPLE_PREVIEWER_SIZE` | str | - |
| `IIIF_TILES_CONVERTER_PARAMS` | dict | - |
| `IIIF_TILES_GENERATION_ENABLED` | bool | - |
| `IIIF_TILES_STORAGE_BASE_PATH` | str | - |
| `IIIF_TILES_VALID_EXTENSIONS` | list | - |
| `IIIF_VALIDATIONS` | dict | - |
| `INDEXER_BEFORE_INDEX_HOOKS` | list | - |
| `INDEXER_BULK_REQUEST_TIMEOUT` | int | - |
| `INDEXER_DEFAULT_INDEX` | NoneType | - |
| `INDEXER_MAX_BULK_CONSUMERS` | int | - |
| `INDEXER_MQ_EXCHANGE` | unknown | - |
| `INDEXER_MQ_PUBLISH_KWARGS` | dict | - |
| `INDEXER_MQ_QUEUE` | unknown | - |
| `INDEXER_MQ_ROUTING_KEY` | str | - |
| `INDEXER_RECORD_TO_INDEX` | str | - |
| `INDEXER_REPLACE_REFS` | bool | - |
| `INSTANCE_THEME_FILE` | configured by function | `configure_ui` |
| `INVENIO_CACHE_TYPE` | configured by function | `configure_generic_parameters` |
| `INVENIO_RDM_ENABLED` | bool | - |
| `INVENIO_VOCABULARY_TYPE_METADATA` | configured by function | `configure_vocabulary` |
| `JAVASCRIPT_PACKAGES_MANAGER` | configured by function | `configure_ui` |
| `JOBS_DEFAULT_QUEUE` | NoneType | - |
| `JOBS_FACETS` | dict | - |
| `JOBS_LOGGING` | bool | - |
| `JOBS_LOGGING_INDEX` | str | - |
| `JOBS_LOGGING_LEVEL` | str | `configure_jobs` |
| `JOBS_LOGGING_RETENTION_DAYS` | int | - |
| `JOBS_LOGS_BATCH_SIZE` | int | - |
| `JOBS_LOGS_MAX_RESULTS` | int | - |
| `JOBS_PERMISSION_POLICY` | unknown | - |
| `JOBS_QUEUES` | dict | - |
| `JOBS_RUNS_PERMISSION_POLICY` | unknown | - |
| `JOBS_SEARCH` | dict | - |
| `JOBS_SORT_OPTIONS` | dict | - |
| `JOBS_TASKS_PERMISSION_POLICY` | unknown | - |
| `JSONSCHEMAS_ENDPOINT` | str | - |
| `JSONSCHEMAS_HOST` | str | `configure_generic_parameters` |
| `JSONSCHEMAS_LOADER_CLS` | NoneType | - |
| `JSONSCHEMAS_LOCAL_REFRESOLVER_URI_SCHEME` | str | - |
| `JSONSCHEMAS_REGISTER_ENDPOINTS_API` | bool | - |
| `JSONSCHEMAS_REGISTER_ENDPOINTS_UI` | bool | - |
| `JSONSCHEMAS_REPLACE_REFS` | bool | - |
| `JSONSCHEMAS_RESOLVER_CLS` | str | - |
| `JSONSCHEMAS_RESOLVE_SCHEMA` | bool | - |
| `JSONSCHEMAS_SCHEMAS` | NoneType | - |
| `JSONSCHEMAS_URL_SCHEME` | str | - |
| `LOGGING_CONSOLE` | bool | - |
| `LOGGING_CONSOLE_LEVEL` | NoneType | - |
| `LOGGING_CONSOLE_PYWARNINGS` | bool | - |
| `LOGGING_FS_BACKUPCOUNT` | int | - |
| `LOGGING_FS_LEVEL` | str | - |
| `LOGGING_FS_LOGFILE` | NoneType | - |
| `LOGGING_FS_MAXBYTES` | int | - |
| `LOGGING_FS_PYWARNINGS` | bool | - |
| `LOGGING_SENTRY_CELERY` | bool | - |
| `LOGGING_SENTRY_CLASS` | NoneType | - |
| `LOGGING_SENTRY_INIT_KWARGS` | NoneType | - |
| `LOGGING_SENTRY_LEVEL` | str | - |
| `LOGGING_SENTRY_PYWARNINGS` | bool | - |
| `LOGGING_SENTRY_REDIS` | bool | - |
| `LOGGING_SENTRY_SQLALCHEMY` | bool | - |
| `MAIL_DEBUG` | bool | - |
| `MAIL_DEFAULT_REPLY_TO` | NoneType | - |
| `MAIL_DEFAULT_SENDER` | unknown | `configure_generic_parameters` |
| `MAIL_MAX_ATTACHMENT_SIZE` | int | - |
| `MAIL_MAX_RETRIES` | int | - |
| `MAIL_MIN_LOGGING_LEVEL` | int | - |
| `MAIL_SUPPRESS_SEND` | bool | `configure_generic_parameters` |
| `MATOMO_ANALYTICS_SITE_ID` | configured by function | `configure_ui` |
| `MATOMO_ANALYTICS_TEMPLATE` | configured by function | `configure_ui` |
| `MATOMO_ANALYTICS_URL` | configured by function | `configure_ui` |
| `MAX_CONTENT_LENGTH` | NoneType | - |
| `MAX_COOKIE_SIZE` | int | - |
| `MAX_FORM_MEMORY_SIZE` | int | - |
| `MAX_FORM_PARTS` | int | - |
| `MULTIPROFILER_BASE_TEMPLATE` | unknown | - |
| `MULTIPROFILER_IGNORED_ENDPOINTS` | unknown | - |
| `MULTIPROFILER_PERMISSION` | unknown | - |
| `NOTIFICATIONS_BACKENDS` | dict | - |
| `NOTIFICATIONS_BUILDERS` | dict | - |
| `NOTIFICATIONS_ENTITY_RESOLVERS` | list | - |
| `NOTIFICATIONS_GROUP_EMAIL_DOMAIN` | NoneType | - |
| `NOTIFICATIONS_SETTINGS_VIEW_FUNCTION` | NoneType | - |
| `OAISERVER_ADMIN_EMAILS` | list | - |
| `OAISERVER_BASE_TEMPLATE` | str | - |
| `OAISERVER_CACHE_KEY` | str | - |
| `OAISERVER_CELERY_TASK_CHUNK_SIZE` | int | - |
| `OAISERVER_COMPRESSIONS` | list | - |
| `OAISERVER_CONTROL_NUMBER_FETCHER` | str | - |
| `OAISERVER_CREATED_KEY` | str | - |
| `OAISERVER_DELETE_PERCOLATOR_FUNCTION` | str | - |
| `OAISERVER_DESCRIPTIONS` | list | - |
| `OAISERVER_GETRECORD_FETCHER` | str | - |
| `OAISERVER_GRANULARITY` | str | - |
| `OAISERVER_ID_FETCHER` | str | - |
| `OAISERVER_ID_PREFIX` | str | `configure_generic_parameters` |
| `OAISERVER_LAST_UPDATE_KEY` | str | - |
| `OAISERVER_METADATA_FORMATS` | dict | - |
| `OAISERVER_NEW_PERCOLATOR_FUNCTION` | str | - |
| `OAISERVER_PAGE_SIZE` | int | - |
| `OAISERVER_PERCOLATOR_DEDICATED_INDEX` | bool | - |
| `OAISERVER_PROTOCOL_VERSION` | str | - |
| `OAISERVER_QUERY_PARSER` | unknown | - |
| `OAISERVER_QUERY_PARSER_FIELDS` | list | - |
| `OAISERVER_RECORD_CLS` | str | - |
| `OAISERVER_RECORD_INDEX` | str | - |
| `OAISERVER_RECORD_LIST_SETS_FETCHER` | str | - |
| `OAISERVER_RECORD_SETS_FETCHER` | str | - |
| `OAISERVER_REGISTER_RECORD_SIGNALS` | bool | - |
| `OAISERVER_REGISTER_SET_SIGNALS` | bool | - |
| `OAISERVER_REPOSITORY_NAME` | str | `configure_oai` |
| `OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME` | int | - |
| `OAISERVER_SEARCH_CLS` | str | - |
| `OAISERVER_SET_RECORDS_QUERY_FETCHER` | str | - |
| `OAISERVER_XSL_URL` | NoneType | - |
| `OAUTH2SERVER_ALLOWED_GRANT_TYPES` | set | - |
| `OAUTH2SERVER_ALLOWED_RESPONSE_TYPES` | set | - |
| `OAUTH2SERVER_ALLOWED_URLENCODE_CHARACTERS` | str | - |
| `OAUTH2SERVER_BASE_TEMPLATE` | str | - |
| `OAUTH2SERVER_CLIENT_ID_SALT_LEN` | int | - |
| `OAUTH2SERVER_CLIENT_SECRET_SALT_LEN` | int | - |
| `OAUTH2SERVER_COVER_TEMPLATE` | str | - |
| `OAUTH2SERVER_JWT_AUTH_HEADER` | str | - |
| `OAUTH2SERVER_JWT_AUTH_HEADER_TYPE` | str | - |
| `OAUTH2SERVER_JWT_VERIFICATION_FACTORY` | str | - |
| `OAUTH2SERVER_SETTINGS_TEMPLATE` | str | - |
| `OAUTH2SERVER_TOKEN_PERSONAL_SALT_LEN` | int | - |
| `OAUTH2_CACHE_TYPE` | str | - |
| `OAUTH2_PROVIDER_ERROR_ENDPOINT` | str | - |
| `OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN` | bool | `configure_generic_parameters` |
| `OAUTHCLIENT_BASE_TEMPLATE` | str | - |
| `OAUTHCLIENT_COVER_TEMPLATE` | str | - |
| `OAUTHCLIENT_LOGIN_USER_TEMPLATE_PARENT` | str | - |
| `OAUTHCLIENT_REMOTE_APPS` | dict | `configure_generic_parameters`, `configure_einfra_oidc` |
| `OAUTHCLIENT_REST_DEFAULT_ERROR_REDIRECT_URL` | str | - |
| `OAUTHCLIENT_REST_DEFAULT_RESPONSE_HANDLER` | NoneType | - |
| `OAUTHCLIENT_REST_REMOTE_APPS` | dict | - |
| `OAUTHCLIENT_SESSION_KEY_PREFIX` | str | - |
| `OAUTHCLIENT_SETTINGS_TEMPLATE` | str | - |
| `OAUTHCLIENT_SIGNUP_FORM` | unknown | - |
| `OAUTHCLIENT_SIGNUP_TEMPLATE` | str | - |
| `OAUTHCLIENT_SITENAME` | LazyString | - |
| `OAUTHCLIENT_STATE_ENABLED` | bool | - |
| `OAUTHCLIENT_STATE_EXPIRES` | int | - |
| `OAUTHCLIENT_TOKEN_EXPIRES_LEEWAY` | int | - |
| `PAGES_ALLOWED_EXTRA_HTML_ATTRS` | dict | - |
| `PAGES_ALLOWED_EXTRA_HTML_TAGS` | list | - |
| `PAGES_BASE_TEMPLATE` | str | - |
| `PAGES_DEFAULT_TEMPLATE` | str | - |
| `PAGES_FACETS` | dict | - |
| `PAGES_SEARCH` | dict | - |
| `PAGES_SORT_OPTIONS` | dict | - |
| `PAGES_TEMPLATES` | list | - |
| `PAGES_WHITELIST_CONFIG_KEYS` | list | - |
| `PERMANENT_SESSION_LIFETIME` | timedelta | - |
| `PIDSTORE_APP_LOGGER_HANDLERS` | bool | - |
| `PIDSTORE_DATACITE_DOI_PREFIX` | str | - |
| `PIDSTORE_OBJECT_ENDPOINTS` | dict | - |
| `PIDSTORE_RECID_FIELD` | str | - |
| `PIDSTORE_RECORDID_OPTIONS` | dict | - |
| `PREFERRED_URL_SCHEME` | str | - |
| `PREVIEWABLE_ZIP_PREVIEWER_NATIVE_EXTENSIONS` | list | - |
| `PREVIEWER_ABSTRACT_TEMPLATE` | str | - |
| `PREVIEWER_BASE_CSS_BUNDLES` | list | - |
| `PREVIEWER_BASE_JS_BUNDLES` | list | - |
| `PREVIEWER_BASE_TEMPLATE` | str | - |
| `PREVIEWER_CHARDET_BYTES` | int | - |
| `PREVIEWER_CHARDET_CONFIDENCE` | float | - |
| `PREVIEWER_CONTAINER_ITEM_PREFERENCE` | list | - |
| `PREVIEWER_CSV_MAX_BYTES` | int | - |
| `PREVIEWER_CSV_SNIFFER_ALLOWED_DELIMITERS` | NoneType | - |
| `PREVIEWER_CSV_VALIDATION_BYTES` | int | - |
| `PREVIEWER_MAX_FILE_SIZE_BYTES` | int | - |
| `PREVIEWER_MAX_IMAGE_SIZE_BYTES` | float | - |
| `PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS` | NoneType | - |
| `PREVIEWER_PDF_JS_ENABLE_SCRIPTING` | bool | - |
| `PREVIEWER_PREFERENCE` | list | - |
| `PREVIEWER_RECORD_FILE_FACOTRY` | NoneType | - |
| `PREVIEWER_TXT_MAX_BYTES` | int | - |
| `PREVIEWER_WEB_ARCHIVE_RANGE_REQUESTS` | bool | - |
| `PREVIEWER_ZIP_MAX_FILES` | int | - |
| `PROPAGATE_EXCEPTIONS` | NoneType | - |
| `PROVIDE_AUTOMATIC_OPTIONS` | bool | - |
| `QUEUES_BROKER_URL` | NoneType | - |
| `QUEUES_CONNECTION_POOL` | unknown | - |
| `QUEUES_DEFINITIONS` | list | - |
| `RATELIMIT_APPLICATION` | unknown | - |
| `RATELIMIT_AUTHENTICATED_USER` | str | `configure_generic_parameters` |
| `RATELIMIT_ENABLED` | bool | - |
| `RATELIMIT_GUEST_USER` | str | `configure_generic_parameters` |
| `RATELIMIT_HEADERS_ENABLED` | bool | - |
| `RATELIMIT_KEY_FUNC` | NoneType | - |
| `RATELIMIT_PER_ENDPOINT` | dict | - |
| `RATELIMIT_STORAGE_URI` | str | - |
| `RATELIMIT_STRATEGY` | str | - |
| `RDM_ALLOW_EXTERNAL_DOI_VERSIONING` | bool | - |
| `RDM_ALLOW_METADATA_ONLY_RECORDS` | bool | - |
| `RDM_ALLOW_OWNERS_REMOVE_COMMUNITY_FROM_RECORD` | bool | - |
| `RDM_ALLOW_RESTRICTED_RECORDS` | bool | - |
| `RDM_ARCHIVE_DOWNLOAD_ENABLED` | bool | - |
| `RDM_CITATION_STYLES` | list | - |
| `RDM_CITATION_STYLES_DEFAULT` | str | - |
| `RDM_COMMUNITIES_ROUTES` | dict | - |
| `RDM_COMMUNITY_CONTENT_MODERATION_HANDLERS` | list | - |
| `RDM_COMMUNITY_INCLUSION_REQUEST_CLS` | unknown | - |
| `RDM_COMMUNITY_REQUIRED_TO_PUBLISH` | bool | - |
| `RDM_COMMUNITY_SUBMISSION_REQUEST_CLS` | unknown | - |
| `RDM_CONTENT_MODERATION_HANDLERS` | list | - |
| `RDM_CUSTOM_FIELDS` | list | - |
| `RDM_CUSTOM_FIELDS_UI` | list | - |
| `RDM_DATACITE_DUMP_OPENAIRE_ACCESS_RIGHTS` | bool | - |
| `RDM_DATACITE_FUNDER_IDENTIFIERS_PRIORITY` | tuple | - |
| `RDM_DEFAULT_FILES_ENABLED` | bool | - |
| `RDM_DETAIL_SIDE_BAR_MANAGE_ATTRIBUTES_EXTENSION_TEMPLATE` | unknown | - |
| `RDM_FACETS` | dict | - |
| `RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE` | int | - |
| `RDM_FILES_DEFAULT_MAX_FILE_SIZE` | int | - |
| `RDM_FILES_DEFAULT_QUOTA_SIZE` | int | - |
| `RDM_FILE_MODIFICATION_PERIOD` | timedelta | - |
| `RDM_FILE_MODIFICATION_POLICY` | unknown | - |
| `RDM_IIIF_MANIFEST_FORMATS` | list | - |
| `RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED` | bool | - |
| `RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES` | list | - |
| `RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED` | bool | - |
| `RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES` | list | - |
| `RDM_IMMEDIATE_RECORD_DELETION_CHECKLIST` | list | - |
| `RDM_IMMEDIATE_RECORD_DELETION_ENABLED` | bool | - |
| `RDM_IMMEDIATE_RECORD_DELETION_POLICIES` | list | - |
| `RDM_LOCK_EDIT_PUBLISHED_FILES` | unknown | - |
| `RDM_MEDIA_FILES_DEFAULT_MAX_FILE_SIZE` | int | - |
| `RDM_MEDIA_FILES_DEFAULT_QUOTA_SIZE` | int | - |
| `RDM_NAMESPACES` | dict | - |
| `RDM_NEW_RECORD_VERSION_REVIEW_POLICY` | unknown | - |
| `RDM_OAI_PMH_FACETS` | dict | - |
| `RDM_OAI_PMH_SEARCH` | dict | - |
| `RDM_OAI_PMH_SORT_OPTIONS` | dict | - |
| `RDM_OPTIONAL_DOI_VALIDATOR` | unknown | - |
| `RDM_PARENT_PERSISTENT_IDENTIFIERS` | dict | - |
| `RDM_PARENT_PERSISTENT_IDENTIFIER_PROVIDERS` | list | - |
| `RDM_PERMISSION_POLICY` | unknown | - |
| `RDM_PERSISTENT_IDENTIFIERS` | dict | - |
| `RDM_PERSISTENT_IDENTIFIER_PROVIDERS` | list | - |
| `RDM_QUOTA_INCREASE_POLICY` | unknown | - |
| `RDM_RECORDS_ALLOW_RESTRICTION_AFTER_GRACE_PERIOD` | bool | - |
| `RDM_RECORDS_CONTAINER_EXTENSIONS` | list | - |
| `RDM_RECORDS_IDENTIFIERS_SCHEMES` | dict | - |
| `RDM_RECORDS_LOCATION_SCHEMES` | dict | - |
| `RDM_RECORDS_MAX_FILES_COUNT` | int | - |
| `RDM_RECORDS_MAX_MEDIA_FILES_COUNT` | int | - |
| `RDM_RECORDS_PERSONORG_SCHEMES` | dict | - |
| `RDM_RECORDS_RELATED_IDENTIFIERS_SCHEMES` | dict | - |
| `RDM_RECORDS_REQUIRE_SECRET_LINKS_EXPIRATION` | bool | - |
| `RDM_RECORDS_RESTRICTION_GRACE_PERIOD` | timedelta | - |
| `RDM_RECORDS_REVIEWS` | list | - |
| `RDM_RECORDS_UI_EDIT_URL` | str | - |
| `RDM_RECORDS_USER_FIXTURE_PASSWORDS` | dict | - |
| `RDM_RECORD_DELETION_POLICY` | unknown | - |
| `RDM_RECORD_FILE_EXTRACTORS` | list | - |
| `RDM_REQUESTS_ROUTES` | dict | - |
| `RDM_REQUEST_RECORD_DELETION_CHECKLIST` | list | - |
| `RDM_REQUEST_RECORD_DELETION_ENABLED` | bool | - |
| `RDM_REQUEST_RECORD_DELETION_POLICIES` | list | - |
| `RDM_RESOURCE_ACCESS_TOKENS_ENABLED` | bool | - |
| `RDM_RESOURCE_ACCESS_TOKENS_JWT_LIFETIME` | timedelta | - |
| `RDM_RESOURCE_ACCESS_TOKENS_SUBJECT_SCHEMA` | unknown | - |
| `RDM_RESOURCE_ACCESS_TOKENS_WHITELISTED_JWT_ALGORITHMS` | list | - |
| `RDM_RESOURCE_ACCESS_TOKEN_REQUEST_ARG` | str | - |
| `RDM_SEARCH` | dict | - |
| `RDM_SEARCH_DRAFTS` | dict | - |
| `RDM_SEARCH_SORT_BY_VERIFIED` | bool | - |
| `RDM_SEARCH_USER_COMMUNITIES` | dict | - |
| `RDM_SEARCH_USER_REQUESTS` | dict | - |
| `RDM_SEARCH_VERSIONING` | dict | - |
| `RDM_SORT_OPTIONS` | dict | - |
| `RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS` | bool | - |
| `RDM_USER_MODERATION_ENABLED` | bool | - |
| `RECAPTCHA_PRIVATE_KEY` | unknown | - |
| `RECAPTCHA_PUBLIC_KEY` | unknown | - |
| `RECORDS_FILES_REST_ENDPOINTS` | dict | - |
| `RECORDS_PERMISSIONS_RECORD_POLICY` | str | - |
| `RECORDS_REFRESOLVER_CLS` | NoneType | `configure_generic_parameters` |
| `RECORDS_REFRESOLVER_STORE` | NoneType | `configure_generic_parameters` |
| `RECORDS_RESOURCES_ALLOW_EMPTY_FILES` | bool | - |
| `RECORDS_RESOURCES_ARCHIVE_DOWNLOAD_MAX_SIZE` | NoneType | - |
| `RECORDS_RESOURCES_DEFAULT_TRANSFER_TYPE` | str | - |
| `RECORDS_RESOURCES_EXTRACTED_STREAM_CHUNK_SIZE` | int | - |
| `RECORDS_RESOURCES_FILES_ALLOWED_DOMAINS` | list | - |
| `RECORDS_RESOURCES_IMAGE_FORMATS` | list | - |
| `RECORDS_RESOURCES_TRANSFERS` | list | - |
| `RECORDS_RESOURCES_ZIP_FORMATS` | list | - |
| `RECORDS_RESOURCES_ZIP_MAX_ENTRIES` | int | - |
| `RECORDS_RESOURCES_ZIP_MAX_HEADER_SIZE` | int | - |
| `RECORDS_RESOURCES_ZIP_MAX_LISTING_ENTRIES` | int | - |
| `RECORDS_RESOURCES_ZIP_MAX_RATIO` | float | - |
| `RECORDS_RESOURCES_ZIP_MAX_TOTAL_UNCOMPRESSED` | int | - |
| `RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY` | unknown | - |
| `RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY` | unknown | - |
| `RECORDS_REST_DEFAULT_LIST_PERMISSION_FACTORY` | unknown | - |
| `RECORDS_REST_DEFAULT_LOADERS` | unknown | - |
| `RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY` | unknown | - |
| `RECORDS_REST_DEFAULT_RESULTS_SIZE` | unknown | - |
| `RECORDS_REST_DEFAULT_SORT` | unknown | - |
| `RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY` | unknown | - |
| `RECORDS_REST_ENDPOINTS` | list | `configure_generic_parameters` |
| `RECORDS_REST_FACETS` | unknown | - |
| `RECORDS_REST_FACETS_POST_FILTERS_PROPAGATE` | unknown | - |
| `RECORDS_REST_SEARCH_ERROR_HANDLERS` | unknown | - |
| `RECORDS_REST_SORT_OPTIONS` | unknown | - |
| `RECORDS_UI_BASE_TEMPLATE` | str | - |
| `RECORDS_UI_DEFAULT_PERMISSION_FACTORY` | NoneType | - |
| `RECORDS_UI_ENDPOINTS` | dict | `configure_ui` |
| `RECORDS_UI_EXPORT_FORMATS` | dict | - |
| `RECORDS_UI_LOGIN_ENDPOINT` | str | - |
| `RECORDS_UI_TOMBSTONE_TEMPLATE` | str | - |
| `RECORDS_VALIDATION_TYPES` | dict | - |
| `RECORD_ROUTES` | configured by function | `configure_generic_parameters` |
| `REMEMBER_COOKIE_DURATION` | unknown | - |
| `REPOSITORY_DESCRIPTION` | configured by function | `configure_ui` |
| `REPOSITORY_KEYWORDS` | configured by function | `configure_ui` |
| `REPOSITORY_NAME` | configured by function | `configure_ui` |
| `REPOSITORY_SUBTITLE` | configured by function | `configure_ui` |
| `REPOSITORY_SUPPORT_CONTACT` | configured by function | `configure_ui` |
| `REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_ATTRS` | dict | - |
| `REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_TAGS` | list | - |
| `REQUESTS_COMMENT_PREVIEW_LIMIT` | int | - |
| `REQUESTS_ENTITY_RESOLVERS` | list | - |
| `REQUESTS_ERROR_HANDLERS` | unknown | - |
| `REQUESTS_EVENTS_SERVICE_COMPONENTS` | list | - |
| `REQUESTS_FACETS` | dict | - |
| `REQUESTS_FILES_DEFAULT_MAX_FILE_SIZE` | int | - |
| `REQUESTS_FILES_DEFAULT_QUOTA_SIZE` | int | - |
| `REQUESTS_LOCKING_ENABLED` | bool | - |
| `REQUESTS_MODERATION_ROLE` | str | - |
| `REQUESTS_PERMISSION_POLICY` | unknown | `register_workflow` |
| `REQUESTS_REGISTERED_EVENT_TYPES` | list | - |
| `REQUESTS_REGISTERED_TYPES` | list | - |
| `REQUESTS_REVIEWERS_ENABLED` | bool | - |
| `REQUESTS_REVIEWERS_MAX_NUMBER` | int | - |
| `REQUESTS_ROUTES` | dict | - |
| `REQUESTS_SEARCH` | dict | - |
| `REQUESTS_SORT_OPTIONS` | dict | - |
| `REQUESTS_TIMELINE_PAGE_SIZE` | int | - |
| `REQUESTS_USER_MODERATION_FACETS` | dict | - |
| `REQUESTS_USER_MODERATION_SEARCH` | dict | - |
| `REQUESTS_USER_MODERATION_SORT_OPTIONS` | dict | - |
| `REST_CSRF_ENABLED` | unknown | - |
| `REST_ENABLE_CORS` | unknown | - |
| `REST_MIMETYPE_QUERY_ARG_NAME` | unknown | - |
| `ROR_CLIENT_ID` | configured by function | `configure_generic_parameters` |
| `S3_ACCESS_KEY_ID` | NoneType | `configure_generic_parameters` |
| `S3_CONFIG_EXTRA` | dict | - |
| `S3_DEFAULT_BLOCK_SIZE` | int | - |
| `S3_ENDPOINT_URL` | NoneType | `configure_generic_parameters` |
| `S3_MAXIMUM_NUMBER_OF_PARTS` | int | - |
| `S3_REGION_NAME` | NoneType | - |
| `S3_SECRET_ACCESS_KEY` | NoneType | `configure_generic_parameters` |
| `S3_SIGNATURE_VERSION` | str | - |
| `S3_UPLOAD_URL_EXPIRATION` | int | - |
| `S3_URL_EXPIRATION` | int | - |
| `SEARCH_CLIENT_CONFIG` | NoneType | `configure_generic_parameters` |
| `SEARCH_ELASTIC_HOSTS` | NoneType | - |
| `SEARCH_HOSTS` | NoneType | `configure_generic_parameters` |
| `SEARCH_INDEX_PREFIX` | str | `configure_generic_parameters` |
| `SEARCH_MAPPINGS` | NoneType | - |
| `SEARCH_RESULTS_MIN_SCORE` | NoneType | - |
| `SEARCH_UI_BASE_TEMPLATE` | NoneType | - |
| `SEARCH_UI_HEADER_TEMPLATE` | NoneType | - |
| `SEARCH_UI_JSTEMPLATE_COUNT` | str | - |
| `SEARCH_UI_JSTEMPLATE_ERROR` | str | - |
| `SEARCH_UI_JSTEMPLATE_FACETS` | str | - |
| `SEARCH_UI_JSTEMPLATE_LOADING` | str | - |
| `SEARCH_UI_JSTEMPLATE_PAGINATION` | str | - |
| `SEARCH_UI_JSTEMPLATE_RANGE` | str | - |
| `SEARCH_UI_JSTEMPLATE_RANGE_OPTIONS` | dict | - |
| `SEARCH_UI_JSTEMPLATE_RESULTS` | str | - |
| `SEARCH_UI_JSTEMPLATE_SELECT_BOX` | str | - |
| `SEARCH_UI_JSTEMPLATE_SORT_ORDER` | str | - |
| `SEARCH_UI_SEARCH_API` | str | - |
| `SEARCH_UI_SEARCH_CONFIG_GEN` | dict | - |
| `SEARCH_UI_SEARCH_INDEX` | str | - |
| `SEARCH_UI_SEARCH_TEMPLATE` | str | `configure_ui` |
| `SEARCH_UI_SEARCH_VIEW` | unknown | `configure_ui` |
| `SECRET_KEY` | str | `configure_generic_parameters` |
| `SECRET_KEY_FALLBACKS` | NoneType | - |
| `SECURITY_AUTO_LOGIN_AFTER_CONFIRM` | bool | - |
| `SECURITY_BLUEPRINT_NAME` | str | - |
| `SECURITY_CHANGEABLE` | bool | `configure_generic_parameters` |
| `SECURITY_CHANGE_PASSWORD_TEMPLATE` | str | - |
| `SECURITY_CHANGE_SALT` | str | - |
| `SECURITY_CHANGE_URL` | str | - |
| `SECURITY_CLI_ROLES_NAME` | str | - |
| `SECURITY_CLI_USERS_NAME` | str | - |
| `SECURITY_CONFIRMABLE` | bool | `configure_generic_parameters` |
| `SECURITY_CONFIRM_EMAIL_WITHIN` | str | - |
| `SECURITY_CONFIRM_ERROR_VIEW` | NoneType | - |
| `SECURITY_CONFIRM_SALT` | str | - |
| `SECURITY_CONFIRM_URL` | str | - |
| `SECURITY_DEFAULT_HTTP_AUTH_REALM` | str | - |
| `SECURITY_DEFAULT_REMEMBER_ME` | bool | - |
| `SECURITY_DEPRECATED_HASHING_SCHEMES` | list | - |
| `SECURITY_DEPRECATED_PASSWORD_SCHEMES` | list | - |
| `SECURITY_EMAIL_HTML` | bool | - |
| `SECURITY_EMAIL_PLAINTEXT` | bool | - |
| `SECURITY_EMAIL_SUBJECT_CONFIRM` | str | - |
| `SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE` | str | - |
| `SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE` | str | - |
| `SECURITY_EMAIL_SUBJECT_PASSWORD_RESET` | str | - |
| `SECURITY_EMAIL_SUBJECT_REGISTER` | str | - |
| `SECURITY_FLASH_MESSAGES` | bool | - |
| `SECURITY_FORGOT_PASSWORD_TEMPLATE` | str | - |
| `SECURITY_HASHING_SCHEMES` | list | - |
| `SECURITY_I18N_DIRNAME` | str | - |
| `SECURITY_I18N_DOMAIN` | str | - |
| `SECURITY_LOGIN_SALT` | str | - |
| `SECURITY_LOGIN_URL` | str | - |
| `SECURITY_LOGIN_USER_TEMPLATE` | str | - |
| `SECURITY_LOGIN_WITHIN` | str | - |
| `SECURITY_LOGIN_WITHOUT_CONFIRMATION` | bool | `configure_generic_parameters` |
| `SECURITY_LOGOUT_URL` | str | - |
| `SECURITY_MSG_ALREADY_CONFIRMED` | tuple | - |
| `SECURITY_MSG_CONFIRMATION_EXPIRED` | tuple | - |
| `SECURITY_MSG_CONFIRMATION_REQUEST` | tuple | - |
| `SECURITY_MSG_CONFIRMATION_REQUIRED` | tuple | - |
| `SECURITY_MSG_CONFIRM_REGISTRATION` | tuple | - |
| `SECURITY_MSG_DISABLED_ACCOUNT` | tuple | - |
| `SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED` | tuple | - |
| `SECURITY_MSG_EMAIL_CONFIRMED` | tuple | - |
| `SECURITY_MSG_EMAIL_NOT_PROVIDED` | tuple | - |
| `SECURITY_MSG_FORGOT_PASSWORD` | tuple | - |
| `SECURITY_MSG_INVALID_CONFIRMATION_TOKEN` | tuple | - |
| `SECURITY_MSG_INVALID_EMAIL_ADDRESS` | tuple | - |
| `SECURITY_MSG_INVALID_LOGIN_TOKEN` | tuple | - |
| `SECURITY_MSG_INVALID_PASSWORD` | tuple | - |
| `SECURITY_MSG_INVALID_REDIRECT` | tuple | - |
| `SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN` | tuple | - |
| `SECURITY_MSG_LOCAL_LOGIN_DISABLED` | tuple | - |
| `SECURITY_MSG_LOGIN` | tuple | - |
| `SECURITY_MSG_LOGIN_EMAIL_SENT` | tuple | - |
| `SECURITY_MSG_LOGIN_EXPIRED` | tuple | - |
| `SECURITY_MSG_PASSWORD_BREACHED` | tuple | - |
| `SECURITY_MSG_PASSWORD_BREACHED_SITE_ERROR` | tuple | - |
| `SECURITY_MSG_PASSWORD_CHANGE` | tuple | - |
| `SECURITY_MSG_PASSWORD_CHANGE_DISABLED` | tuple | - |
| `SECURITY_MSG_PASSWORD_INVALID_LENGTH` | tuple | - |
| `SECURITY_MSG_PASSWORD_IS_THE_SAME` | tuple | - |
| `SECURITY_MSG_PASSWORD_MISMATCH` | tuple | - |
| `SECURITY_MSG_PASSWORD_NOT_PROVIDED` | tuple | - |
| `SECURITY_MSG_PASSWORD_NOT_SET` | tuple | - |
| `SECURITY_MSG_PASSWORD_RECOVERY_DISABLED` | tuple | - |
| `SECURITY_MSG_PASSWORD_RESET` | tuple | - |
| `SECURITY_MSG_PASSWORD_RESET_DISABLED` | tuple | - |
| `SECURITY_MSG_PASSWORD_RESET_EXPIRED` | tuple | - |
| `SECURITY_MSG_PASSWORD_RESET_REQUEST` | tuple | - |
| `SECURITY_MSG_PASSWORD_TOO_SIMPLE` | tuple | - |
| `SECURITY_MSG_REFRESH` | tuple | - |
| `SECURITY_MSG_REGISTRATION_DISABLED` | tuple | - |
| `SECURITY_MSG_RETYPE_PASSWORD_MISMATCH` | tuple | - |
| `SECURITY_MSG_UNAUTHORIZED` | tuple | - |
| `SECURITY_MSG_USER_DOES_NOT_EXIST` | tuple | - |
| `SECURITY_PASSWORD_BREACHED_COUNT` | int | - |
| `SECURITY_PASSWORD_CHECK_BREACHED` | bool | - |
| `SECURITY_PASSWORD_COMPLEXITY_CHECKER` | NoneType | - |
| `SECURITY_PASSWORD_HASH` | str | - |
| `SECURITY_PASSWORD_LENGTH_MIN` | int | - |
| `SECURITY_PASSWORD_SALT` | str | - |
| `SECURITY_PASSWORD_SCHEMES` | list | - |
| `SECURITY_PASSWORD_SINGLE_HASH` | list | - |
| `SECURITY_POST_CHANGE_VIEW` | NoneType | - |
| `SECURITY_POST_CONFIRM_VIEW` | NoneType | - |
| `SECURITY_POST_LOGIN_VIEW` | str | - |
| `SECURITY_POST_LOGOUT_VIEW` | str | - |
| `SECURITY_POST_REGISTER_VIEW` | NoneType | - |
| `SECURITY_POST_RESET_VIEW` | NoneType | - |
| `SECURITY_RECOVERABLE` | bool | `configure_generic_parameters` |
| `SECURITY_REGISTERABLE` | bool | `configure_generic_parameters` |
| `SECURITY_REGISTER_URL` | str | - |
| `SECURITY_REGISTER_USER_TEMPLATE` | str | - |
| `SECURITY_RESET_PASSWORD_TEMPLATE` | str | - |
| `SECURITY_RESET_PASSWORD_WITHIN` | str | - |
| `SECURITY_RESET_SALT` | str | - |
| `SECURITY_RESET_URL` | str | - |
| `SECURITY_SEND_CONFIRMATION_TEMPLATE` | str | - |
| `SECURITY_SEND_LOGIN_TEMPLATE` | str | - |
| `SECURITY_SEND_PASSWORD_CHANGE_EMAIL` | bool | - |
| `SECURITY_SEND_PASSWORD_RESET_EMAIL` | bool | - |
| `SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL` | bool | - |
| `SECURITY_SEND_REGISTER_EMAIL` | bool | - |
| `SECURITY_SUBDOMAIN` | NoneType | - |
| `SECURITY_TOKEN_AUTHENTICATION_HEADER` | str | - |
| `SECURITY_TOKEN_AUTHENTICATION_KEY` | str | - |
| `SECURITY_TOKEN_MAX_AGE` | NoneType | - |
| `SECURITY_TRACKABLE` | bool | - |
| `SECURITY_URL_PREFIX` | NoneType | - |
| `SECURITY_USER_IDENTITY_ATTRIBUTES` | list | - |
| `SECURITY_ZXCVBN_MINIMUM_SCORE` | int | - |
| `SEND_FILE_MAX_AGE_DEFAULT` | NoneType | `configure_generic_parameters` |
| `SENTRY_DSN` | NoneType | - |
| `SERVER_NAME` | NoneType | - |
| `SESSION_COOKIE_DOMAIN` | NoneType | `configure_generic_parameters` |
| `SESSION_COOKIE_HTTPONLY` | bool | - |
| `SESSION_COOKIE_NAME` | str | - |
| `SESSION_COOKIE_PARTITIONED` | bool | - |
| `SESSION_COOKIE_PATH` | NoneType | - |
| `SESSION_COOKIE_SAMESITE` | str | - |
| `SESSION_COOKIE_SECURE` | bool | `configure_generic_parameters` |
| `SESSION_KEY_BITS` | int | - |
| `SESSION_RANDOM_SOURCE` | SystemRandom | - |
| `SESSION_REFRESH_EACH_REQUEST` | bool | - |
| `SETTINGS_TEMPLATE` | str | `configure_ui` |
| `SITEMAP_MAX_ENTRY_COUNT` | int | - |
| `SITEMAP_ROOT_VIEW_ENABLED` | bool | - |
| `SITEMAP_SECTIONS` | list | - |
| `SITE_API_URL` | str | `configure_generic_parameters` |
| `SITE_UI_URL` | str | `configure_generic_parameters` |
| `SQLALCHEMY_BINDS` | dict | - |
| `SQLALCHEMY_DATABASE_URI` | str | `configure_generic_parameters` |
| `SQLALCHEMY_ECHO` | bool | - |
| `SQLALCHEMY_ENGINE_OPTIONS` | dict | - |
| `SQLALCHEMY_RECORD_QUERIES` | bool | - |
| `SQLALCHEMY_TRACK_MODIFICATIONS` | bool | - |
| `STATS_AGGREGATIONS` | dict | - |
| `STATS_EVENTS` | dict | - |
| `STATS_EVENTS_UTC_DATETIME_ENABLED` | bool | - |
| `STATS_MQ_EXCHANGE` | unknown | - |
| `STATS_PERMISSION_FACTORY` | unknown | - |
| `STATS_QUERIES` | dict | - |
| `STATS_REGISTER_INDEX_TEMPLATES` | bool | - |
| `STATS_REGISTER_RECEIVERS` | bool | `configure_stats` |
| `TEMPLATES_AUTO_RELOAD` | NoneType | - |
| `TESTING` | bool | - |
| `THEME_401_TEMPLATE` | str | - |
| `THEME_403_TEMPLATE` | str | - |
| `THEME_404_TEMPLATE` | str | - |
| `THEME_429_TEMPLATE` | str | - |
| `THEME_500_TEMPLATE` | str | - |
| `THEME_BASE_TEMPLATE` | str | - |
| `THEME_COVER_TEMPLATE` | str | - |
| `THEME_CSS_TEMPLATE` | configured by function | `configure_ui` |
| `THEME_ERROR_TEMPLATE` | str | - |
| `THEME_FOOTER_TEMPLATE` | str | `configure_ui` |
| `THEME_FRONTPAGE` | bool | `configure_ui` |
| `THEME_FRONTPAGE_LOGO` | configured by function | `configure_ui` |
| `THEME_FRONTPAGE_TEMPLATE` | str | `configure_ui` |
| `THEME_FRONTPAGE_TITLE` | LazyString | `configure_ui` |
| `THEME_GENERATOR` | str | - |
| `THEME_GOOGLE_SITE_VERIFICATION` | list | - |
| `THEME_HEADER_LOGIN_TEMPLATE` | str | `configure_ui` |
| `THEME_HEADER_TEMPLATE` | str | `configure_ui` |
| `THEME_ICONS` | dict | - |
| `THEME_JAVASCRIPT_TEMPLATE` | str | `configure_ui` |
| `THEME_LOGO` | str | `configure_ui` |
| `THEME_LOGO_ADMIN` | str | - |
| `THEME_MATHJAX_CDN` | str | - |
| `THEME_META_ROBOT_TAGS` | list | - |
| `THEME_SEARCHBAR` | bool | - |
| `THEME_SEARCH_ENDPOINT` | str | `configure_ui` |
| `THEME_SETTINGS_TEMPLATE` | str | - |
| `THEME_SHOW_FRONTPAGE_INTRO_SECTION` | unknown | `configure_ui` |
| `THEME_SITENAME` | LazyString | `configure_ui` |
| `THEME_SITEURL` | str | - |
| `THEME_TRACKINGCODE_TEMPLATE` | str | `configure_ui` |
| `THEME_TWITTERHANDLE` | unknown | - |
| `TRAP_BAD_REQUEST_ERRORS` | NoneType | - |
| `TRAP_HTTP_EXCEPTIONS` | bool | - |
| `TRUSTED_HOSTS` | NoneType | - |
| `TYPE_CHECKING` | bool | - |
| `USERPROFILES` | bool | - |
| `USERPROFILES_BASE_TEMPLATE` | str | - |
| `USERPROFILES_EMAIL_ENABLED` | bool | - |
| `USERPROFILES_EXTEND_SECURITY_FORMS` | bool | - |
| `USERPROFILES_PROFILE_TEMPLATE` | str | - |
| `USERPROFILES_PROFILE_URL` | str | - |
| `USERPROFILES_READ_ONLY` | bool | `configure_generic_parameters`, `configure_einfra_oidc` |
| `USERPROFILES_SETTINGS_TEMPLATE` | str | - |
| `USERS_RESOURCES_AVATAR_COLORS` | list | - |
| `USERS_RESOURCES_DOMAINS_ORG_SCHEMA` | unknown | - |
| `USERS_RESOURCES_DOMAINS_SEARCH` | dict | - |
| `USERS_RESOURCES_DOMAINS_SEARCH_FACETS` | dict | - |
| `USERS_RESOURCES_DOMAINS_SORT_OPTIONS` | dict | - |
| `USERS_RESOURCES_GROUPS_ADMIN_FACETS` | dict | - |
| `USERS_RESOURCES_GROUPS_ADMIN_SEARCH` | dict | - |
| `USERS_RESOURCES_GROUPS_ADMIN_SORT_OPTIONS` | dict | - |
| `USERS_RESOURCES_GROUPS_ENABLED` | bool | - |
| `USERS_RESOURCES_MODERATION_LOCK_DEFAULT_TIMEOUT` | int | - |
| `USERS_RESOURCES_MODERATION_LOCK_RENEWAL_TIMEOUT` | int | - |
| `USERS_RESOURCES_PROTECTED_GROUP_NAMES` | list | - |
| `USERS_RESOURCES_SEARCH` | dict | - |
| `USERS_RESOURCES_SEARCH_FACETS` | dict | - |
| `USERS_RESOURCES_SERVICE_SCHEMA` | unknown | - |
| `USERS_RESOURCES_SORT_OPTIONS` | dict | - |
| `USER_DASHBOARD_MENU_OVERRIDES` | dict | - |
| `USE_X_SENDFILE` | bool | - |
| `VCS_TEMPLATE_INDEX` | unknown | - |
| `VCS_TEMPLATE_INDEX_ITEM` | unknown | - |
| `VCS_TEMPLATE_RELEASE_ITEM` | unknown | - |
| `VCS_TEMPLATE_REPO_SWITCH` | unknown | - |
| `VCS_TEMPLATE_VIEW` | unknown | - |
| `VOCABULARIES_AFFILIATIONS_EDMO_COUNTRY_MAPPING` | dict | - |
| `VOCABULARIES_AFFILIATION_SCHEMES` | dict | `configure_generic_parameters` |
| `VOCABULARIES_AWARDS_EC_ROR_ID` | str | - |
| `VOCABULARIES_AWARDS_OPENAIRE_FUNDERS` | dict | - |
| `VOCABULARIES_AWARD_SCHEMES` | dict | - |
| `VOCABULARIES_CUSTOM_VOCABULARY_TYPES` | list | - |
| `VOCABULARIES_DATASTREAM_READERS` | dict | `configure_datastreams`, `configure_generic_parameters` |
| `VOCABULARIES_DATASTREAM_TRANSFORMERS` | dict | `configure_datastreams`, `configure_generic_parameters` |
| `VOCABULARIES_DATASTREAM_WRITERS` | dict | `configure_datastreams`, `configure_generic_parameters` |
| `VOCABULARIES_FUNDER_DOI_PREFIX` | str | - |
| `VOCABULARIES_FUNDER_SCHEMES` | dict | `configure_generic_parameters` |
| `VOCABULARIES_IDENTIFIER_SCHEMES` | dict | - |
| `VOCABULARIES_NAMES_SCHEMES` | dict | `configure_generic_parameters` |
| `VOCABULARIES_ORCID_ACCESS_KEY` | str | - |
| `VOCABULARIES_ORCID_ORG_IDS_MAPPING_PATH` | NoneType | - |
| `VOCABULARIES_ORCID_SECRET_KEY` | str | - |
| `VOCABULARIES_ORCID_SUMMARIES_BUCKET` | str | - |
| `VOCABULARIES_ORCID_SYNC_MAX_WORKERS` | int | - |
| `VOCABULARIES_ORCID_SYNC_SINCE` | dict | - |
| `VOCABULARIES_RESOURCE_CONFIG` | unknown | `configure_generic_parameters` |
| `VOCABULARIES_SERVICE_CONFIG` | unknown | `configure_generic_parameters` |
| `VOCABULARIES_SUBJECTS_EUROSCIVOC_FILE_URL` | str | - |
| `VOCABULARIES_SUBJECTS_GEMET_FILE_URL` | str | - |
| `VOCABULARIES_SUBJECTS_NVS_FILE_URL` | str | - |
| `VOCABULARIES_SUBJECTS_SCHEMES` | dict | - |
| `VOCABULARIES_TYPES_SEARCH` | dict | - |
| `VOCABULARIES_TYPES_SORT_OPTIONS` | dict | - |
| `WEBPACKEXT_MANIFEST_PATH` | str | - |
| `WEBPACKEXT_NPM_PKG_CLS` | configured by function | `configure_ui` |
| `WEBPACKEXT_PROJECT` | str | `configure_ui` |
| `WEBPACKEXT_PROJECT_BUILDDIR` | str | - |
| `WEBPACKEXT_PROJECT_DISTDIR` | str | - |
| `WEBPACKEXT_PROJECT_DISTURL` | str | - |
| `WORKFLOWS` | configured by function | `register_workflow` |

## Detailed Variable Reference
### `ACCESS_ACTION_CACHE_PREFIX`
| **Description** | Prefix for actions cached when used in dynamic permissions. |
|--------------|-----------|
| **Default Value** | `'Permission::action::'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_access/config.py (via app.config) |

---

### `ACCESS_CACHE`
| **Description** | A cache instance or an importable string pointing to the cache instance. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_access/config.py (via app.config) |

---

### `ACCESS_LOAD_SYSTEM_ROLE_NEEDS`
| **Description** | Enables the loading of system role needs when users' identity change. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_access/config.py (via app.config) |

---

### `ACCOUNTS`
| **Description** | Tells if the templates should use the accounts module.  If False, you won't be able to login via the... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_BASE_TEMPLATE`
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `ACCOUNTS_CONFIRM_EMAIL_ENDPOINT`
| **Description** | Value to be used for the confirmation email link in the UI application. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_COVER_TEMPLATE`
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `ACCOUNTS_DEFAULT_EMAIL_VISIBILITY`
| **Description** | Default Email visibility value can be set to either 'restricted' or 'public'. |
|--------------|-----------|
| **Default Value** | `'restricted'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_DEFAULT_USERS_VERIFIED`
| **Description** | Default verified status: if set to 'True', users are verified by default. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_DEFAULT_USER_VISIBILITY`
| **Description** | Default User visibility value can be set to either 'restricted' or 'public'. |
|--------------|-----------|
| **Default Value** | `'restricted'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT`
| **Description** | Flask-Limiter rate limit string for forgot-password requests per account.  Example: ``"3 per hour"``... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_KEY_PREFIX`
| **Description** | Prefix used to namespace forgot-password per-account limiter keys. |
|--------------|-----------|
| **Default Value** | `'accounts.fp_email'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_MSG`
| **Default Value** | `l'Too many password-reset requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | app.config |

---

### `ACCOUNTS_JWT_ALOGORITHM`
| **Description** | Set JWT encryption alogirthm.  .. note::     `Available aglorithms    <https://pyjwt.readthedocs.io/... |
|--------------|-----------|
| **Default Value** | `'HS256'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_JWT_CREATION_FACTORY`
| **Description** | Import path of factory used to generate JWT. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts.utils:jwt_create_token'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_JWT_DECODE_FACTORY`
| **Description** | Import path of factory used to decode JWT. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts.utils:jwt_decode_token'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_JWT_DOM_TOKEN`
| **Description** | Register JWT context processor.  .. code-block:: html      {% if current_user.is_authenticated %}   ... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_JWT_DOM_TOKEN_TEMPLATE`
| **Description** | Template for the context processor. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/jwt.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_JWT_ENABLE`
| **Description** | Enable JWT support.  .. note::      More details about `JWT <https://jwt.io>`_ |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_JWT_EXPIRATION_DELTA`
| **Description** | Token expiration period for JWT. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=1)` |
| **Type** | timedelta |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_JWT_SECRET_KEY`
| **Description** | Secret key for JWT.  .. note::      If is set to ``None`` it will use the ``SECRET_KEY``. |
|--------------|-----------|
| **Default Value** | `'CHANGE_ME'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_LOCAL_LOGIN_ENABLED`
| **Description** | Whether or not login with local account credentials should be enabled. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `ACCOUNTS_LOGIN_RATELIMIT`
| **Description** | Flask-Limiter rate limit string for login requests per account.  Example: ``"5 per 15 minutes"``. Di... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_LOGIN_RATELIMIT_KEY_PREFIX`
| **Description** | Prefix used to namespace login per-account limiter keys. |
|--------------|-----------|
| **Default Value** | `'accounts.login'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_LOGIN_RATELIMIT_MSG`
| **Default Value** | `l'Too many login attempts for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | app.config |

---

### `ACCOUNTS_LOGIN_VIEW_FUNCTION`
| **Description** | The view function to use for the login endpoint.  This can be either an import string, or the view f... |
|--------------|-----------|
| **Default Value** | `login` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `ACCOUNTS_REGISTER_BLUEPRINT`
| **Description** | Register the Security blueprint or not.  It can be used to override the ``register_blueprint`` optio... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_RESET_PASSWORD_ENDPOINT`
| **Description** | Value to be used for the confirmation email link in the UI application. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_REST_AUTH_VIEWS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `ACCOUNTS_REST_CONFIRM_EMAIL_ENDPOINT`
| **Description** | Value to be used for the confirmation email link in the API application.  Can be a Flask endpoint (e... |
|--------------|-----------|
| **Default Value** | `'/confirm/{token}'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_REST_RESET_PASSWORD_ENDPOINT`
| **Description** | Value to be used for the reset password link in the API application.  Can be a Flask endpoint (e.g. ... |
|--------------|-----------|
| **Default Value** | `'/lost-password/{token}'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_RETENTION_PERIOD`
| **Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | app.config |

---

### `ACCOUNTS_SEND_CONFIRMATION_RATELIMIT`
| **Description** | Flask-Limiter rate limit string for send-confirmation requests per account.  Example: ``"3 per hour"... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_KEY_PREFIX`
| **Description** | Prefix used to namespace send-confirmation per-account limiter keys. |
|--------------|-----------|
| **Default Value** | `'accounts.cf_email'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_MSG`
| **Default Value** | `l'Too many confirmation-email requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | app.config |

---

### `ACCOUNTS_SESSION_ACTIVITY_ENABLED`
| **Description** | Enable session activity tracking. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_SESSION_REDIS_URL`
| **Description** | Redis URL used by the module as a cache system for sessions. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `ACCOUNTS_SESSION_STORE_FACTORY`
| **Default Value** | `'invenio_accounts.sessions:default_session_store_factory'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `ACCOUNTS_SETTINGS_SECURITY_TEMPLATE`
| **Description** | Template for the account security page. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/settings/security.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_SETTINGS_TEMPLATE`
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `ACCOUNTS_SITENAME`
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | app.config |

---

### `ACCOUNTS_USERINFO_HEADERS`
| **Description** | If True, add X-Session-ID and X-User-ID to the HTTP response. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_USERNAME_REGEX`
| **Description** | The regular expression used for validating usernames.  .. note:: When this configuration value is ov... |
|--------------|-----------|
| **Default Value** | `'^[a-zA-Z][a-zA-Z0-9-_]{2,255}$'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_USERNAME_RULES_TEXT`
| **Default Value** | `l'Username must start with a letter, be at least three characters long and only contain alphanumeric...` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | app.config |

---

### `ACCOUNTS_USER_PREFERENCES_SCHEMA`
| **Description** | The schema to use for validation of the user preferences. |
|--------------|-----------|
| **Default Value** | `<UserPreferencesSchema(many=False)>` |
| **Type** | UserPreferencesSchema |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_USER_PROFILE_SCHEMA`
| **Description** | The schema to use for validation of the user profile. |
|--------------|-----------|
| **Default Value** | `<UserProfileSchema(many=False)>` |
| **Type** | UserProfileSchema |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ACCOUNTS_USE_CELERY`
| **Description** | Tells if the module should use Celery or not.  By default, it uses Celery if it can find it. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `ADMINISTRATION_APPNAME`
| **Description** | Name of the Flask-Admin app (also the page title of admin panel). |
|--------------|-----------|
| **Default Value** | `'Invenio-Administration'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_administration/config.py (via app.config) |

---

### `ADMINISTRATION_BASE_TEMPLATE`
| **Description** | Admin panel base template. By default (``None``) uses the Flask-Admin template. |
|--------------|-----------|
| **Default Value** | `'invenio_administration/base.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_administration/config.py (via app.config) |

---

### `ADMINISTRATION_DASHBOARD_VIEW`
| **Default Value** | `'invenio_administration.views.dashboard.AdminDashboardView'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `ADMINISTRATION_DISPLAY_VERSIONS`
| **Description** | Display packages versions in the admin panel side bar.  Accepts a list of tuples in the format (pack... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_administration/config.py (via app.config) |

---

### `ADMINISTRATION_THEME_BASE_TEMPLATE`
| **Description** | Administration base template. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_administration/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `ADMIN_BASE_TEMPLATE`
| **Description** | Base template for the administration interface.  The template changes the administration interface f... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_admin.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `ALEMBIC`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `ALEMBIC_CONTEXT`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `ALLOWED_HTML_ATTRS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `ALLOWED_HTML_TAGS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `APPLICATION_ROOT`
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `APP_ALLOWED_HOSTS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `APP_DEFAULT_SECURE_HEADERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `APP_ENABLE_SECURE_HEADERS`
| **Description** | Enable Secure Headers. (Default: ``True``)  In case you want to disable completely `Talisman`, you c... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `APP_HEALTH_BLUEPRINT_ENABLED`
| **Description** | Enable the ping (healthcheck) blueprint. (Default: ``False``) |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `APP_LOGS_PERMISSION_POLICY`
| **Description** | Permission policy for job logs. |
|--------------|-----------|
| **Default Value** | `JobLogsPermissionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py |

**Set/Referenced by:**
- [`configure_jobs`](#) in `jobs.py`
  > Set up the "Jobs" feature (manually or automatically run administrative tasks).  Invenio-jobs lets administrators run and monitor maintenance tasks (such as re-indexing or fixing up data) from the adm...
---

### `APP_RDM_ADMIN_EMAIL_RECIPIENT`
| **Description** | Admin e-mail |
|--------------|-----------|
| **Default Value** | `'info@inveniosoftware.org'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_DEPOSIT_FORM_AUTOCOMPLETE_NAMES`
| **Description** | Behavior for autocomplete names search field for creators/contributors.  Available options:  - ``sea... |
|--------------|-----------|
| **Default Value** | `'search'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_DEPOSIT_FORM_CUSTOM_FIELD_DEFAULTS`
| **Description** | Default values for custom fields in new records in the deposit UI.  The keys denote the dot-separate... |
|--------------|-----------|
| **Default Value** | `{}` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_DEPOSIT_FORM_DEFAULTS`
| **Default Value** | `{'publication_date': lambda: datetime.now().strftime('%Y-%m-%d'), 'rights': [{'id': 'cc-by-4.0', 'ti...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_DEPOSIT_FORM_PUBLISH_MODAL_EXTRA`
| **Description** | Additional text/html to be displayed in the publish and submit for review modal. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_DEPOSIT_FORM_QUOTA`
| **Default Value** | `{'maxFiles': 100, 'maxStorage': RDM_FILES_DEFAULT_QUOTA_SIZE}` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `APP_RDM_DEPOSIT_FORM_TEMPLATE`
| **Description** | Deposit page's form template. |
|--------------|-----------|
| **Default Value** | `'invenio_app_rdm/records/deposit.html'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED`
| **Description** | Feature toggle to enable the next-generation (NG) file uploader UI in the deposit form.  When enable... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `APP_RDM_DETAIL_SIDE_BAR_TEMPLATES`
| **Default Value** | `['invenio_app_rdm/records/details/side_bar/manage_menu.html', 'invenio_app_rdm/records/details/side_...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `APP_RDM_DISPLAY_DECIMAL_FILE_SIZES`
| **Description** | Display the file sizes in powers of 1000 (KB, ...) or 1024 (KiB, ...). |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_FILES_INTEGRITY_REPORT_SUBJECT`
| **Description** | Files integrity report subject |
|--------------|-----------|
| **Default Value** | `_('Files integrity report')` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_FILES_INTEGRITY_REPORT_TEMPLATE`
| **Default Value** | `'invenio_app_rdm/files_integrity_report/email/files_integrity_report.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_IDENTIFIER_SCHEMES_UI`
| **Default Value** | `{'orcid': {'url_prefix': 'http://orcid.org/', 'icon': 'images/orcid.svg', 'label': 'ORCID'}, 'ror': ...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `APP_RDM_MODERATION_REQUEST_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `APP_RDM_MODERATION_REQUEST_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `APP_RDM_MODERATION_REQUEST_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `APP_RDM_PAGES`
| **Description** | Register static pages with predefined initial content from 'pages.yaml' file.  Example: {     "about... |
|--------------|-----------|
| **Default Value** | `{}` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_RECORDS_EXPORT_URL`
| **Default Value** | `'/records/<pid_value>/export/<export_format>'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_RECORD_EXPORTERS`
| **Default Value** | `{'json': {'name': _('JSON'), 'serializer': 'flask_resources.serializers:JSONSerializer', 'params': {...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS`
| **Description** | Default format used for adding badges to a record.  Make sure the 'render' field points to a valid r... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `APP_RDM_RECORD_LANDING_PAGE_FAIR_SIGNPOSTING_LEVEL_1_ENABLED`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_RECORD_LANDING_PAGE_TEMPLATE`
| **Default Value** | `'invenio_app_rdm/records/detail.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_RECORD_THUMBNAIL_SIZES`
| **Description** | Allowed record thumbnail sizes. |
|--------------|-----------|
| **Default Value** | `[10, 50, 100, 250, 750, 1200]` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `APP_RDM_SUBCOMMUNITIES_LABEL`
| **Description** | Label for the subcommunities in the community browse page. |
|--------------|-----------|
| **Default Value** | `_('Subcommunities')` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `APP_RDM_USER_DASHBOARD_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `APP_REQUESTID_HEADER`
| **Description** | Name of header containing a request id (max length 200 characters).  If set, the request id will be ... |
|--------------|-----------|
| **Default Value** | `'X-Request-Id'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `APP_THEME`
| **Description** | Application-wide themes list used for template and assets lookup.  The value is a list of theme stri... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `ASSETS_BUILDER`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `AUDIT_LOGS_DISABLED_ACTIONS`
| **Description** | Disabled actions to be excluded from the audit logs. To find all the available actions, check the en... |
|--------------|-----------|
| **Default Value** | `<set>` |
| **Type** | set |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_audit_logs/config.py (via app.config) |

---

### `AUDIT_LOGS_ENABLED`
| **Description** | Feature flag. Disabled by default. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_audit_logs/config.py (via app.config) |

---

### `AUDIT_LOGS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `AUDIT_LOGS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `AUDIT_LOGS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `BABEL_DEFAULT_LOCALE`
| **Description** | Default locale (language). |
|--------------|-----------|
| **Default Value** | `'en'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `BABEL_DEFAULT_TIMEZONE`
| **Description** | Default time zone. |
|--------------|-----------|
| **Default Value** | `'Europe/Zurich'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `BANNERS_CATEGORIES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `BANNERS_CATEGORIES_TO_STYLE`
| **Description** | Function to transform the banner category to a specific Semantic-UI class. |
|--------------|-----------|
| **Default Value** | `style_category` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_banners/config.py |

---

### `BANNERS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `BANNERS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `BASE_TEMPLATE`
| **Description** | Base template for user facing pages.  The template provides a basic skeleton which takes care of loa... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `BROKER_URL`
| **Description** | URL of message broker for Celery 3 (default is RabbitMQ). |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/0'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `CACHE_IS_AUTHENTICATED_CALLBACK`
| **Description** | Import path to callback.  Callback is executed to determine if request is authenticated. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_cache/config.py (via app.config) |

---

### `CACHE_KEY_PREFIX`
| **Description** | Cache key prefix. |
|--------------|-----------|
| **Default Value** | `'cache::'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_cache/config.py (via app.config) |

---

### `CACHE_REDIS_URL`
| **Description** | Redis location and database. |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/0'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_cache/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `CACHE_TYPE`
| **Description** | Cache type.  Please refer to Flask-Caching documentation for other cache types. |
|--------------|-----------|
| **Default Value** | `'flask_caching.backends.redis'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_cache/config.py (via app.config) |

---

### `CELERY_ACCEPT_CONTENT`
| **Description** | A whitelist of content-types/serializers. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_celery/config.py (via app.config) |

---

### `CELERY_ALWAYS_EAGER`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `CELERY_BEAT_SCHEDULE`
| **Default Value** | `{'indexer': {'task': 'invenio_records_resources.tasks.manage_indexer_queues', 'schedule': timedelta(...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_cron`](#) in `cron.py`
  > Set up the periodic (scheduled) background tasks the repository needs.  The repository relies on a number of jobs that must run automatically in the background on a regular basis - for example, cleani...
---

### `CELERY_BROKER_URL`
| **Description** | Same as BROKER_URL to support Celery 4. |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/0'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `CELERY_RESULT_BACKEND`
| **Description** | URL of backend for result storage (default is Redis). |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/1'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `CELERY_RESULT_SERIALIZER`
| **Description** | Result serialization format. Default is ``msgpack``. |
|--------------|-----------|
| **Default Value** | `'msgpack'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_celery/config.py (via app.config) |

---

### `CELERY_TASK_SERIALIZER`
| **Description** | The default serialization method to use. Default is ``msgpack``. |
|--------------|-----------|
| **Default Value** | `'msgpack'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_celery/config.py (via app.config) |

---

### `CELERY_WORKER_CONCURRENCY`
| **Default Value** | `16` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `CELERY_WORKER_POOL`
| **Default Value** | `'threads'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `CHECKS_ENABLED`
| **Description** | Enable checks. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_checks/config.py (via app.config) |

---

### `COLLECTIONS_MAX_COLLECTIONS_PER_TREE`
| **Description** | Maximum number of collections allowed per tree.  This counts all collections in a tree, regardless o... |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_collections/config.py (via app.config) |

---

### `COLLECTIONS_MAX_DEPTH`
| **Description** | Maximum depth for collection hierarchies.  Depth 0 = root collections Depth 1 = children of root Dep... |
|--------------|-----------|
| **Default Value** | `1` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_collections/config.py (via app.config) |

---

### `COLLECTIONS_MAX_TREES`
| **Description** | Maximum number of collection trees allowed per namespace.  Set to 0 for unlimited trees. Default: 10 |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_collections/config.py (via app.config) |

---

### `COLLECTIONS_PERMISSION_POLICY`
| **Description** | Permission policy used by invenio-collections for managing collection trees. |
|--------------|-----------|
| **Default Value** | `CommunityPermissionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py |

---

### `COLLECT_STATIC_ROOT`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `COLLECT_STORAGE`
| **Description** | Static files collection method (defaults to copying files). |
|--------------|-----------|
| **Default Value** | `'flask_collect.storage.link'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `COMMUNITIES_ALLOW_MEMBERSHIP_REQUESTS`
| **Description** | Feature flag for membership request. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_ALLOW_RESTRICTED`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `COMMUNITIES_ALWAYS_SHOW_CREATE_LINK`
| **Description** | Controls visibility of 'New Community' btn based on user's permission when set to True. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_COLLECTIONS_ENABLED`
| **Description** | Feature flag to enable/disable collections feature. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_CUSTOM_FIELDS`
| **Description** | Communities custom fields definition.  Of the shape:  .. code-block:: python      [         <custom-... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_CUSTOM_FIELDS_UI`
| **Description** | Communities custom fields UI configuration.  Of the shape:  .. code-block:: python      [{         s... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_DEFAULT_RECORD_SUBMISSION_POLICY`
| **Description** | Default value of record submission policy community access setting. |
|--------------|-----------|
| **Default Value** | `<RecordSubmissionPolicyEnum.OPEN: 'open'>` |
| **Type** | RecordSubmissionPolicyEnum |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_ERROR_HANDLERS`
| **Default Value** | `{**community_error_handlers, InvalidCommunityVisibility: create_error_handler(lambda e: HTTPJSONExce...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `COMMUNITIES_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_IDENTITIES_CACHE_HANDLER`
| **Default Value** | `'invenio_communities.cache.redis:IdentityRedisCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `COMMUNITIES_IDENTITIES_CACHE_REDIS_URL`
| **Default Value** | `'redis://localhost:6379/4'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `COMMUNITIES_IDENTITIES_CACHE_TIME`
| **Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `COMMUNITIES_INVITATIONS_EXPIRES_IN`
| **Description** | Default amount of time before an invitation expires. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=30)` |
| **Type** | timedelta |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_INVITATIONS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_INVITATIONS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_LOGO_MAX_FILE_SIZE`
| **Description** | Community logo size quota, in bytes. |
|--------------|-----------|
| **Default Value** | `1000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_MEMBERSHIP_REQUESTS_EXPIRES_IN`
| **Description** | Default amount of time before a membership request expires. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=30)` |
| **Type** | timedelta |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_MEMBERSHIP_REQUESTS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_MEMBERSHIP_REQUESTS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_MEMBERS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_MEMBERS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_MEMBERS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_NAMESPACES`
| **Description** | Custom fields namespaces.  .. code-block:: python     {<namespace>: <uri>, ...}  For example:  .. co... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_OAI_SETS_PREFIX`
| **Default Value** | `'community-'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `COMMUNITIES_PERMISSION_POLICY`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_communities`](#) in `communities.py`
  > Set up communities: who can do what inside a community.  Communities are the groups records can be submitted to (for example a department or a project). This sets the roles a member of a community can...
---

### `COMMUNITIES_RECORDS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_REGISTER_UI_BLUEPRINT`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_communities`](#) in `communities.py`
  > Set up communities: who can do what inside a community.  Communities are the groups records can be submitted to (for example a department or a project). This sets the roles a member of a community can...
---

### `COMMUNITIES_REQUESTS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_ROLES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_communities`](#) in `communities.py`
  > Set up communities: who can do what inside a community.  Communities are the groups records can be submitted to (for example a department or a project). This sets the roles a member of a community can...
---

### `COMMUNITIES_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_SEARCH_SORT_BY_VERIFIED`
| **Description** | Sort communities by 'verified' first. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/config.py (via app.config) |

---

### `COMMUNITIES_SERVICE_COMPONENTS`
| **Default Value** | `CommunityServiceComponents` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `COMMUNITIES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_SUBCOMMUNITIES_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_SUBCOMMUNITIES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `COMMUNITIES_SUB_INVITATION_REQUEST_CLS`
| **Description** | RDM specific request type for subcommunity invitations. |
|--------------|-----------|
| **Default Value** | `RDMSubCommunityInvitationRequest` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `COMMUNITIES_SUB_REQUEST_CLS`
| **Description** | RDM specific request type for subcommunities. |
|--------------|-----------|
| **Default Value** | `RDMSubCommunityRequest` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `CORS_EXPOSE_HEADERS`
| **Default Value** | `['ETag', 'Link', 'X-RateLimit-Limit', 'X-RateLimit-Remaining', 'X-RateLimit-Reset', 'Content-Type']` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rest/config.py |

---

### `CORS_RESOURCES`
| **Description** | Dictionary for configuring CORS for endpoints.     See Flask-CORS for further details.  .. note:: Ov... |
|--------------|-----------|
| **Default Value** | `'*'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rest/config.py |

---

### `CORS_SEND_WILDCARD`
| **Description** | Sending wildcard CORS header.  .. note:: Overwrites    `Flask-CORS    <https://flask-cors.readthedoc... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rest/config.py |

---

### `COVER_TEMPLATE`
| **Description** | Cover page template normally used e.g. for login and sign up pages. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_cover.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `CROSSREF_ADDITIONAL_PREFIXES`
| **Description** | List of additional Crossref DOI prefixes supported for registration. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_DEPOSITOR`
| **Description** | Crossref depositor name. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_EMAIL`
| **Description** | Crossref depositor email. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_ENABLED`
| **Description** | Flag to enable/disable Crossref DOI registration. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_FORMAT`
| **Description** | A string used for formatting the DOI or a callable.  If set to a string, you can used ``{prefix}`` a... |
|--------------|-----------|
| **Default Value** | `'{prefix}/{id}'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_PASSWORD`
| **Description** | Crossref password. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_PREFIX`
| **Description** | Crossref DOI prefix. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_REGISTRANT`
| **Description** | Crossref registrant. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_TEST_MODE`
| **Description** | Crossref test mode enabled. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CROSSREF_USERNAME`
| **Description** | Crossref username. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `CSRF_ALLOWED_CHARS`
| **Default Value** | `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `CSRF_COOKIE_NAME`
| **Default Value** | `'csrftoken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `CSRF_COOKIE_SAMESITE`
| **Default Value** | `'Lax'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `CSRF_FORCE_SECURE_REFERER`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `CSRF_HEADER`
| **Default Value** | `'X-CSRFToken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `CSRF_METHODS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `CSRF_SECRET_SALT`
| **Default Value** | `'invenio-csrf-token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `CSRF_TOKEN_EXPIRES_IN`
| **Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `CSRF_TOKEN_GRACE_PERIOD`
| **Default Value** | `604800` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `CSRF_TOKEN_LENGTH`
| **Default Value** | `32` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `DASHBOARD_RECORD_CREATE_URL`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `DATACITE_ADDITIONAL_PREFIXES`
| **Description** | List of additional DataCite DOI prefixes supported for registration. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `DATACITE_DATACENTER_SYMBOL`
| **Description** | DataCite data center symbol.  This is only required if you want your records to be harvestable (OAI-... |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `DATACITE_ENABLED`
| **Description** | Flag to enable/disable DataCite DOI registration. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `DATACITE_FORMAT`
| **Description** | A string used for formatting the DOI or a callable.  If set to a string, you can used ``{prefix}`` a... |
|--------------|-----------|
| **Default Value** | `'{prefix}/{id}'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `DATACITE_PASSWORD`
| **Description** | DataCite password. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `DATACITE_PREFIX`
| **Description** | DataCite DOI prefix. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `DATACITE_TEST_MODE`
| **Description** | DataCite test mode enabled. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `DATACITE_USERNAME`
| **Description** | DataCite username. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `DB_VERSIONING`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `DB_VERSIONING_USER_MODEL`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `DEBUG`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `DEBUG_TB_INTERCEPT_REDIRECTS`
| **Description** | Switches off incept of redirects by Flask-DebugToolbar. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `DEPLOYMENT_VERSION`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `EINFRA`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_einfra_oidc`](#) in `einfra.py`
  > Set up "Log in with e-INFRA" (CESNET/Perun) for the repository.  This enables single sign-on through the CESNET e-INFRA identity provider, so users can log in with their e-INFRA/Perun account instead ...
---

### `EINFRA_LOGIN_APP`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_einfra_oidc`](#) in `einfra.py`
  > Set up "Log in with e-INFRA" (CESNET/Perun) for the repository.  This enables single sign-on through the CESNET e-INFRA identity provider, so users can log in with their e-INFRA/Perun account instead ...
---

### `EXPLAIN_TEMPLATE_LOADING`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `FILES_REST_ALLOW_RANGE_REQUESTS`
| **Description** | Enable support for HTTP Range Requests. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_CHECKSUM_VERIFICATION_URI_PREFIXES`
| **Description** | URI prefixes of files their checksums should be verified |
|--------------|-----------|
| **Default Value** | `[]` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `FILES_REST_DEFAULT_MAX_FILE_SIZE`
| **Description** | Default maximum file size for a bucket in bytes. `None` if unlimited. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_DEFAULT_QUOTA_SIZE`
| **Description** | Default quota size for a bucket in bytes. `None` if unlimited. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `FILES_REST_DEFAULT_STORAGE_CLASS`
| **Description** | Default storage class. Must be one of `FILES_REST_STORAGE_CLASS_LIST`. |
|--------------|-----------|
| **Default Value** | `'S'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `FILES_REST_FILE_TAGS_HEADER`
| **Description** | Header for updating file tags. |
|--------------|-----------|
| **Default Value** | `'X-Invenio-File-Tags'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_FILE_URI_MAX_LEN`
| **Description** | Maximum length of the FileInstance.uri field.  .. warning::    Setting this variable to anything hig... |
|--------------|-----------|
| **Default Value** | `255` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_MIN_FILE_SIZE`
| **Description** | Minimum file size when uploading, in bytes (do not allow empty files). |
|--------------|-----------|
| **Default Value** | `1` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_MULTIPART_CHUNKSIZE_MAX`
| **Description** | Maximum chunk size in bytes of multipart objects. |
|--------------|-----------|
| **Default Value** | `5368709120` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_MULTIPART_CHUNKSIZE_MIN`
| **Description** | Minimum chunk size in bytes of multipart objects. |
|--------------|-----------|
| **Default Value** | `5242880` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_MULTIPART_EXPIRES`
| **Description** | Time delta after which a multipart upload is considered expired. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=4)` |
| **Type** | timedelta |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_MULTIPART_MAX_PARTS`
| **Description** | Maximum number of parts when uploading files with multipart uploads. |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_MULTIPART_PART_FACTORIES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `FILES_REST_OBJECT_KEY_MAX_LEN`
| **Description** | Maximum length of the ObjectVersion.key field.  .. warning::    Setting this variable to anything hi... |
|--------------|-----------|
| **Default Value** | `255` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_PERMISSION_FACTORY`
| **Description** | Permission factory to control the files access from the REST interface. |
|--------------|-----------|
| **Default Value** | `'invenio_files_rest.permissions.permission_factory'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_SIZE_LIMITERS`
| **Description** | Import path of file size limiters factory to control bucket size limits. |
|--------------|-----------|
| **Default Value** | `'invenio_files_rest.limiters.file_size_limiters'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_STORAGE_CLASS_LIST`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `FILES_REST_STORAGE_FACTORY`
| **Description** | Import path of factory used to create a storage instance. |
|--------------|-----------|
| **Default Value** | `'invenio_files_rest.storage.pyfs_storage_factory'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `FILES_REST_STORAGE_PATH_DIMENSIONS`
| **Description** | Number of directory levels created when generating the path of a file.     For example, if split len... |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_STORAGE_PATH_SPLIT_LENGTH`
| **Description** | Number of chars to use as folder name when generating the path of a file.     For example, if split ... |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_TASK_WAIT_INTERVAL`
| **Description** | Interval in seconds between sending a whitespace to not close connection. |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_TASK_WAIT_MAX_SECONDS`
| **Description** | Maximum number of seconds to wait for a task to finish. |
|--------------|-----------|
| **Default Value** | `600` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_UPLOAD_FACTORIES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `FILES_REST_XSENDFILE_ENABLED`
| **Description** | Use the X-Accel-Redirect header to stream the file through a reverse proxy(     e.g NGINX). |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `FILES_REST_XSENDFILE_RESPONSE_FUNC`
| **Description** | Function for the creation of a file streaming redirect response. |
|--------------|-----------|
| **Default Value** | `create_file_streaming_redirect_response` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py |

---

### `FORMATTER_BADGES_ALLOWED_TITLES`
| **Description** | List of allowed titles in badges. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `FORMATTER_BADGES_ENABLE`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `FORMATTER_BADGES_MAX_CACHE_AGE`
| **Description** | The maximum amount of time a badge will be considered fresh. |
|--------------|-----------|
| **Default Value** | `0` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_formatter/config.py (via app.config) |

---

### `FORMATTER_BADGES_TITLE_MAPPING`
| **Description** | Mapping of titles. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `GLOBAL_SEARCH_MODELS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`add_model`](#) in `models.py`
  > Include a data model in the repository's global (cross-model) search.  Repositories can host several different kinds of records (models), e.g. "datasets" and "publications". Call this once per model p...
---

### `HEADER_TEMPLATE`
| **Description** | Base header template to be extended on custom headers. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/header.html'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `I18N_DEFAULT_REDIRECT_ENDPOINT`
| **Description** | Endpoint to redirect if no next parameter is provided. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

---

### `I18N_JS_DISTR_EXCEPTIONAL_PACKAGE_MAP`
| **Description** | Exceptional package name mapper for JS/React localization distribution.  Webpack entrypoints are use... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

---

### `I18N_LANGUAGES`
| **Description** | List of tuples of available languages.  Example configuration with english and danish with english a... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `I18N_SESSION_KEY`
| **Description** | Key to retrieve language identifier from the current session object. |
|--------------|-----------|
| **Default Value** | `'language'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

---

### `I18N_SET_LANGUAGE_URL`
| **Description** | URL prefix for set language view.  Set to ``None`` to prevent view from being installed. |
|--------------|-----------|
| **Default Value** | `'/lang'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

---

### `I18N_TRANSIFEX_JS_RESOURCES_MAP`
| **Description** | Mapping of transifex resource names to invenioRDM package names.  All resources/packages that should... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

---

### `I18N_TRANSLATIONS_PATHS`
| **Description** | List of paths to load message catalogs from. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

---

### `I18N_USER_LANG_ATTR`
| **Description** | Attribute name which contains language identifier on the User object.  It is used only when the logi... |
|--------------|-----------|
| **Default Value** | `'prefered_language'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_i18n/config.py (via app.config) |

---

### `IIIF_API_DECORATOR_HANDLER`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `IIIF_API_INFO_RESPONSE_SKELETON`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `IIIF_CACHE_HANDLER`
| **Default Value** | `'flask_iiif.cache.simple:ImageSimpleCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `IIIF_CACHE_IGNORE_ERRORS`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `IIIF_CACHE_REDIS_URL`
| **Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `IIIF_CACHE_TIME`
| **Default Value** | `172800` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `IIIF_CONVERTERS`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `IIIF_FORMATS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `IIIF_FORMATS_PIL_MAP`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `IIIF_GIF_TEMP_FOLDER_PATH`
| **Default Value** | `'/tmp'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `IIIF_MODE`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `IIIF_PREVIEW_TEMPLATE`
| **Description** | Template for IIIF image preview. |
|--------------|-----------|
| **Default Value** | `'invenio_app_rdm/records/iiif_preview.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `IIIF_QUALITIES`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `IIIF_SIMPLE_PREVIEWER_NATIVE_EXTENSIONS`
| **Description** | Images are converted to JPEG for preview, unless listed here. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `IIIF_SIMPLE_PREVIEWER_SIZE`
| **Description** | Size of image in IIIF preview window. Must be a valid IIIF Image API size parameter. |
|--------------|-----------|
| **Default Value** | `'!800,800'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `IIIF_TILES_CONVERTER_PARAMS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `IIIF_TILES_GENERATION_ENABLED`
| **Description** | Enable generating pyramidal TIFF tiles for uploaded images. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `IIIF_TILES_STORAGE_BASE_PATH`
| **Description** | Base path for storing IIIF tiles.  Relative paths are resolved against the application instance path... |
|--------------|-----------|
| **Default Value** | `'images/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `IIIF_TILES_VALID_EXTENSIONS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `IIIF_VALIDATIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `INDEXER_BEFORE_INDEX_HOOKS`
| **Description** | List of automatically connected hooks (function or importable string). |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INDEXER_BULK_REQUEST_TIMEOUT`
| **Description** | Request timeout to use in Bulk indexing. |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INDEXER_DEFAULT_INDEX`
| **Description** | Default index to use if no schema is defined. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INDEXER_MAX_BULK_CONSUMERS`
| **Description** | Maximum number of concurrent consumers for bulk indexing.  This threshold is applied per queue, so e... |
|--------------|-----------|
| **Default Value** | `5` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INDEXER_MQ_EXCHANGE`
| **Description** | Default exchange for message queue. |
|--------------|-----------|
| **Default Value** | `Exchange('indexer', type='direct')` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py |

---

### `INDEXER_MQ_PUBLISH_KWARGS`
| **Description** | Default message queue producer publishing kwargs.  Passed to ``kombu.Producer:publish``.  .. code-bl... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INDEXER_MQ_QUEUE`
| **Description** | Default queue for message queue. |
|--------------|-----------|
| **Default Value** | `Queue('indexer', exchange=INDEXER_MQ_EXCHANGE, routing_key='indexer')` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py |

---

### `INDEXER_MQ_ROUTING_KEY`
| **Description** | Default routing key for message queue. |
|--------------|-----------|
| **Default Value** | `'indexer'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INDEXER_RECORD_TO_INDEX`
| **Description** | Provide an implementation of record_to_index function |
|--------------|-----------|
| **Default Value** | `'invenio_indexer.utils.default_record_to_index'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INDEXER_REPLACE_REFS`
| **Description** | Whether to replace JSONRefs prior to indexing record. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_indexer/config.py (via app.config) |

---

### `INSTANCE_THEME_FILE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `INVENIO_CACHE_TYPE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `INVENIO_RDM_ENABLED`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `INVENIO_VOCABULARY_TYPE_METADATA`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_vocabulary`](#) in `vocabulary.py`
  > Declare a custom controlled vocabulary (a fixed list of allowed values).  Vocabularies are controlled lists of values that records can pick from, such as languages, resource types or licenses. Call th...
---

### `JAVASCRIPT_PACKAGES_MANAGER`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `JOBS_DEFAULT_QUEUE`
| **Description** | Default Celery queue. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

---

### `JOBS_FACETS`
| **Description** | Facets/aggregations for Jobs results. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

---

### `JOBS_LOGGING`
| **Description** | Enable logging for jobs. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

---

### `JOBS_LOGGING_INDEX`
| **Description** | "Index name for job logs. |
|--------------|-----------|
| **Default Value** | `'job-logs'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

---

### `JOBS_LOGGING_LEVEL`
| **Description** | Logging level for jobs. |
|--------------|-----------|
| **Default Value** | `'DEBUG'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_jobs`](#) in `jobs.py`
  > Set up the "Jobs" feature (manually or automatically run administrative tasks).  Invenio-jobs lets administrators run and monitor maintenance tasks (such as re-indexing or fixing up data) from the adm...
---

### `JOBS_LOGGING_RETENTION_DAYS`
| **Description** | Retention period for job logs in days. |
|--------------|-----------|
| **Default Value** | `90` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

---

### `JOBS_LOGS_BATCH_SIZE`
| **Description** | Number of log results to fetch per batch from the search backend. |
|--------------|-----------|
| **Default Value** | `500` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

---

### `JOBS_LOGS_MAX_RESULTS`
| **Description** | Maximum total number of log results to return in a single search request. |
|--------------|-----------|
| **Default Value** | `2000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py (via app.config) |

---

### `JOBS_PERMISSION_POLICY`
| **Description** | Permission policy for jobs. |
|--------------|-----------|
| **Default Value** | `JobPermissionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py |

---

### `JOBS_QUEUES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `JOBS_RUNS_PERMISSION_POLICY`
| **Description** | Permission policy for job runs. |
|--------------|-----------|
| **Default Value** | `RunPermissionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py |

---

### `JOBS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `JOBS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `JOBS_TASKS_PERMISSION_POLICY`
| **Description** | Permission policy for tasks. |
|--------------|-----------|
| **Default Value** | `TasksPermissionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/config.py |

---

### `JSONSCHEMAS_ENDPOINT`
| **Description** | Default schema endpoint. |
|--------------|-----------|
| **Default Value** | `'/schemas'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_HOST`
| **Description** | Default json schema host. |
|--------------|-----------|
| **Default Value** | `'localhost'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `JSONSCHEMAS_LOADER_CLS`
| **Description** | Loader class used in ``JSONRef`` when replacing ``$ref``. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_LOCAL_REFRESOLVER_URI_SCHEME`
| **Description** | Non-standard URI scheme to reference local schemas. |
|--------------|-----------|
| **Default Value** | `'local://'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_REGISTER_ENDPOINTS_API`
| **Description** | Register the endpoints on the API app. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_REGISTER_ENDPOINTS_UI`
| **Description** | Register the endpoints on the UI app. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_REPLACE_REFS`
| **Description** | Whether to resolve $ref before serving a schema. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_RESOLVER_CLS`
| **Description** | Resolver used to resolve the schema.  if :py:const:`invenio_jsonschemas.config.JSONSCHEMAS_RESOLVE_S... |
|--------------|-----------|
| **Default Value** | `'invenio_jsonschemas.utils.resolve_schema'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_RESOLVE_SCHEMA`
| **Description** | Whether to resolve schema using the Resolver Class.  If is ``True``, will replace $ref and run the :... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_SCHEMAS`
| **Description** | List of entrypoint names to register JSON Schemas for.  If `None`, all JSON Schemas defined through ... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `JSONSCHEMAS_URL_SCHEME`
| **Description** | Default url scheme for schemas. |
|--------------|-----------|
| **Default Value** | `'https'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jsonschemas/config.py (via app.config) |

---

### `LOGGING_CONSOLE`
| **Description** | Enable logging to the console. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_CONSOLE_LEVEL`
| **Description** | Console logging level.  Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``, `... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_CONSOLE_PYWARNINGS`
| **Description** | Enable logging of Python warnings to the console.  By default, warnings are logged to the console if... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_FS_BACKUPCOUNT`
| **Description** | Number of rotated log files to keep. |
|--------------|-----------|
| **Default Value** | `5` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_FS_LEVEL`
| **Description** | Filesystem logging level.  Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``... |
|--------------|-----------|
| **Default Value** | `'WARNING'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_FS_LOGFILE`
| **Description** | Enable logging to the filesystem. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_FS_MAXBYTES`
| **Description** | Maximum size of logging file. Default: 100MB. |
|--------------|-----------|
| **Default Value** | `104857600` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_FS_PYWARNINGS`
| **Description** | Enable logging of Python warnings to filesystem logging. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_SENTRY_CELERY`
| **Description** | Configure Celery to send logging to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_SENTRY_CLASS`
| **Description** | Import path of sentry Flask extension class.  This allows you to customize the Sentry extension clas... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_SENTRY_INIT_KWARGS`
| **Description** | Pass extra options when initializing Sentry instance. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_SENTRY_LEVEL`
| **Description** | Sentry logging level.  Defaults to only reporting errors and warnings. |
|--------------|-----------|
| **Default Value** | `'WARNING'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_SENTRY_PYWARNINGS`
| **Description** | Enable logging of Python warnings to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_SENTRY_REDIS`
| **Description** | Configure REDIS to send logging to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `LOGGING_SENTRY_SQLALCHEMY`
| **Description** | Configure SQL Alchemy to send logging to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `MAIL_DEBUG`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `MAIL_DEFAULT_REPLY_TO`
| **Description** | Reply to mail address for e-mails. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_mail/config.py (via app.config) |

---

### `MAIL_DEFAULT_SENDER`
| **Description** | Email address used as sender of account registration emails.  `SECURITY_EMAIL_SENDER` will default t... |
|--------------|-----------|
| **Default Value** | `'info@inveniosoftware.org'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `MAIL_MAX_ATTACHMENT_SIZE`
| **Description** | Max size of inline attachments, in bytes. |
|--------------|-----------|
| **Default Value** | `1000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_mail/config.py (via app.config) |

---

### `MAIL_MAX_RETRIES`
| **Description** | How often will we repeat if a problem occurred. |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_mail/config.py (via app.config) |

---

### `MAIL_MIN_LOGGING_LEVEL`
| **Description** | Minimum logging level for the mail logger. |
|--------------|-----------|
| **Default Value** | `40` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_mail/config.py (via app.config) |

---

### `MAIL_SUPPRESS_SEND`
| **Description** | Disable email sending by default. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `MATOMO_ANALYTICS_SITE_ID`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `MATOMO_ANALYTICS_TEMPLATE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `MATOMO_ANALYTICS_URL`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `MAX_CONTENT_LENGTH`
| **Description** | Maximum allowed content length for form data.  This value limits the maximum file upload size via mu... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/config.py (via app.config) |

---

### `MAX_COOKIE_SIZE`
| **Default Value** | `4093` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `MAX_FORM_MEMORY_SIZE`
| **Default Value** | `500000` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `MAX_FORM_PARTS`
| **Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `MULTIPROFILER_BASE_TEMPLATE`
| **Description** | Base template for the profiler page. |
|--------------|-----------|
| **Default Value** | `'flask_multiprofiler/index.html'` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `MULTIPROFILER_IGNORED_ENDPOINTS`
| **Default Value** | `['static', '_debug_toolbar.static', 'profiler\\..+', 'invenio_formatter_badges.badge']` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `MULTIPROFILER_PERMISSION`
| **Description** | Function to check for permissions to access the profiler. |
|--------------|-----------|
| **Default Value** | `administration_permission.can` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `NOTIFICATIONS_BACKENDS`
| **Description** | Notification backends.  .. code-block::python      NOTIFICATIONS_BACKENDS = {         "email": Email... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_notifications/config.py (via app.config) |

---

### `NOTIFICATIONS_BUILDERS`
| **Description** | Notification builders.  .. code-block::python      NOTIFICATIONS_BUILDERS = {         "community_sub... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_notifications/config.py (via app.config) |

---

### `NOTIFICATIONS_ENTITY_RESOLVERS`
| **Description** | List of entity resolvers used by notification builders.  .. code-block::python      NOTIFICATIONS_EN... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_notifications/config.py (via app.config) |

---

### `NOTIFICATIONS_GROUP_EMAIL_DOMAIN`
| **Description** | Domain suffix to append to group names when email is not provided.  When a recipient is a group and ... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_notifications/config.py (via app.config) |

---

### `NOTIFICATIONS_SETTINGS_VIEW_FUNCTION`
| **Description** | View function for notification settings.  This should be set higher up in the module hierarchy (e.g.... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_notifications/config.py (via app.config) |

---

### `OAISERVER_ADMIN_EMAILS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `OAISERVER_BASE_TEMPLATE`
| **Default Value** | `'invenio_oaiserver/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAISERVER_CACHE_KEY`
| **Description** | Key prefix added before all keys in cache server. |
|--------------|-----------|
| **Default Value** | `'DynamicOAISets::'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_CELERY_TASK_CHUNK_SIZE`
| **Description** | Specify the maximum number of records each task will update. |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_COMPRESSIONS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `OAISERVER_CONTROL_NUMBER_FETCHER`
| **Description** | PIDStore fetcher for the OAI ID control number. |
|--------------|-----------|
| **Default Value** | `'recid'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_CREATED_KEY`
| **Description** | Record created key. |
|--------------|-----------|
| **Default Value** | `'created'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `OAISERVER_DELETE_PERCOLATOR_FUNCTION`
| **Default Value** | `'invenio_oaiserver.percolator:_delete_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAISERVER_DESCRIPTIONS`
| **Description** | Specify the optional description containers that can be used to express properties of the repository... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_GETRECORD_FETCHER`
| **Description** | Record data fetcher for serialization. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.oai:getrecord_fetcher'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `OAISERVER_GRANULARITY`
| **Description** | The finest harvesting granularity supported by the repository.  The legitimate values are ``YYYY-MM-... |
|--------------|-----------|
| **Default Value** | `'YYYY-MM-DDThh:mm:ssZ'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_ID_FETCHER`
| **Description** | OAI ID fetcher function. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.oai:oaiid_fetcher'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `OAISERVER_ID_PREFIX`
| **Description** | The prefix that will be applied to the generated OAI-PMH ids. |
|--------------|-----------|
| **Default Value** | `'oai:Mac.localdomain:'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `OAISERVER_LAST_UPDATE_KEY`
| **Description** | Record update key. |
|--------------|-----------|
| **Default Value** | `'updated'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `OAISERVER_METADATA_FORMATS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `OAISERVER_NEW_PERCOLATOR_FUNCTION`
| **Default Value** | `'invenio_oaiserver.percolator:_new_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAISERVER_PAGE_SIZE`
| **Description** | Define maximum length of list responses.  Request with verbs ``ListRecords``, ``ListIdentifiers``, a... |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_PERCOLATOR_DEDICATED_INDEX`
| **Description** | Create a dedicated index for the percolators, instead of storing them in the same index as the recor... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_PROTOCOL_VERSION`
| **Default Value** | `'2.0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAISERVER_QUERY_PARSER`
| **Description** | Define query parser for OIASet definition. |
|--------------|-----------|
| **Default Value** | `invenio_search.engine.dsl.Q` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py |

---

### `OAISERVER_QUERY_PARSER_FIELDS`
| **Description** | Define query parser search fields list for OIASet definition. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_RECORD_CLS`
| **Description** | Record retrieval class. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.records.api:RDMRecord'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `OAISERVER_RECORD_INDEX`
| **Description** | Specify a search index with records that should be exposed via OAI-PMH. |
|--------------|-----------|
| **Default Value** | `'oaisource'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_RECORD_LIST_SETS_FETCHER`
| **Description** | Record's list OAI sets function. |
|--------------|-----------|
| **Default Value** | `'invenio_oaiserver.percolator:sets_search_all'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_RECORD_SETS_FETCHER`
| **Description** | Record's OAI sets function. |
|--------------|-----------|
| **Default Value** | `'invenio_oaiserver.percolator:find_sets_for_record'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `OAISERVER_REGISTER_RECORD_SIGNALS`
| **Description** | Catch record/set insert/update/delete signals and update the `_oai` field. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_REGISTER_SET_SIGNALS`
| **Description** | Catch set insert/update/delete signals and update the `_oai` record field. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_REPOSITORY_NAME`
| **Default Value** | `'Invenio-OAIServer'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_oai`](#) in `oai.py`
  > Set up OAI-PMH, the protocol other systems use to harvest records from this repository.  OAI-PMH is a standard way for external services (e.g. national aggregators, other repositories) to regularly fe...
---

### `OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME`
| **Description** | The expiration time of a resumption token in seconds.  **Default: 60 seconds = 1 minute**.  .. note:... |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAISERVER_SEARCH_CLS`
| **Description** | Class for record search. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.oai:OAIRecordSearch'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `OAISERVER_SET_RECORDS_QUERY_FETCHER`
| **Default Value** | `'invenio_oaiserver.fetchers:set_records_query_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAISERVER_XSL_URL`
| **Description** | Specify the url (relative or absolute) to the XML Stylesheet file to transform XML OAI 2.0 responses... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/config.py (via app.config) |

---

### `OAUTH2SERVER_ALLOWED_GRANT_TYPES`
| **Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | app.config |

---

### `OAUTH2SERVER_ALLOWED_RESPONSE_TYPES`
| **Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | app.config |

---

### `OAUTH2SERVER_ALLOWED_URLENCODE_CHARACTERS`
| **Description** | A string of special characters that should be valid inside a query string.  .. seealso::      See :p... |
|--------------|-----------|
| **Default Value** | `'=&;:%+~,*@!()/?'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2SERVER_BASE_TEMPLATE`
| **Default Value** | `'invenio_oauth2server/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAUTH2SERVER_CLIENT_ID_SALT_LEN`
| **Description** | Length of client id. |
|--------------|-----------|
| **Default Value** | `40` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2SERVER_CLIENT_SECRET_SALT_LEN`
| **Description** | Length of the client secret. |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2SERVER_COVER_TEMPLATE`
| **Default Value** | `'invenio_oauth2server/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAUTH2SERVER_JWT_AUTH_HEADER`
| **Description** | Header for the JWT.  .. note::      Authorization: Bearer xxx |
|--------------|-----------|
| **Default Value** | `'Authorization'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2SERVER_JWT_AUTH_HEADER_TYPE`
| **Description** | Header Authorization type.  .. note::      By default the authorization type is ``Bearer`` as recomm... |
|--------------|-----------|
| **Default Value** | `'Bearer'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2SERVER_JWT_VERIFICATION_FACTORY`
| **Description** | Import path of factory used to verify JWT.  The ``request.headers`` should be passed as parameter. |
|--------------|-----------|
| **Default Value** | `'invenio_oauth2server.utils:jwt_verify_token'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2SERVER_SETTINGS_TEMPLATE`
| **Default Value** | `'invenio_oauth2server/settings/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAUTH2SERVER_TOKEN_PERSONAL_SALT_LEN`
| **Description** | Length of the personal access token. |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2_CACHE_TYPE`
| **Description** | Type of cache to use for storing the temporary grant token. |
|--------------|-----------|
| **Default Value** | `'redis'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTH2_PROVIDER_ERROR_ENDPOINT`
| **Description** | Error view endpoint. |
|--------------|-----------|
| **Default Value** | `'invenio_oauth2server.errors'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/config.py (via app.config) |

---

### `OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN`
| **Description** | Redirect to the only external login service under specific conditions.  If this option is enabled an... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `OAUTHCLIENT_BASE_TEMPLATE`
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAUTHCLIENT_COVER_TEMPLATE`
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAUTHCLIENT_LOGIN_USER_TEMPLATE_PARENT`
| **Default Value** | `'invenio_accounts/login_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAUTHCLIENT_REMOTE_APPS`
| **Description** | Configuration of remote applications. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
- [`configure_einfra_oidc`](#) in `einfra.py`
  > Set up "Log in with e-INFRA" (CESNET/Perun) for the repository.  This enables single sign-on through the CESNET e-INFRA identity provider, so users can log in with their e-INFRA/Perun account instead ...
---

### `OAUTHCLIENT_REST_DEFAULT_ERROR_REDIRECT_URL`
| **Description** | Configuration of default error redirect URL. |
|--------------|-----------|
| **Default Value** | `'/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `OAUTHCLIENT_REST_DEFAULT_RESPONSE_HANDLER`
| **Description** | Default REST response handler. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `OAUTHCLIENT_REST_REMOTE_APPS`
| **Description** | Configuration of remote rest applications. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `OAUTHCLIENT_SESSION_KEY_PREFIX`
| **Description** | Session key prefix used when storing the access token for a remote app. |
|--------------|-----------|
| **Default Value** | `'oauth_token'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `OAUTHCLIENT_SETTINGS_TEMPLATE`
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `OAUTHCLIENT_SIGNUP_FORM`
| **Description** | Function called to render the sign up form after authorization succeeded. |
|--------------|-----------|
| **Default Value** | `_create_registrationform` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py |

---

### `OAUTHCLIENT_SIGNUP_TEMPLATE`
| **Description** | Template for the signup page. |
|--------------|-----------|
| **Default Value** | `'invenio_oauthclient/signup.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `OAUTHCLIENT_SITENAME`
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | app.config |

---

### `OAUTHCLIENT_STATE_ENABLED`
| **Description** | Internal variable used to disable state validation during tests. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `OAUTHCLIENT_STATE_EXPIRES`
| **Description** | Number of seconds after which the state token expires. |
|--------------|-----------|
| **Default Value** | `300` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `OAUTHCLIENT_TOKEN_EXPIRES_LEEWAY`
| **Description** | The number of seconds before the actual expiration of an access token from which it is considered ex... |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/config.py (via app.config) |

---

### `PAGES_ALLOWED_EXTRA_HTML_ATTRS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `PAGES_ALLOWED_EXTRA_HTML_TAGS`
| **Description** | Extend allowed HTML tags list for static pages content. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pages/config.py (via app.config) |

---

### `PAGES_BASE_TEMPLATE`
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `PAGES_DEFAULT_TEMPLATE`
| **Description** | Default template to render. |
|--------------|-----------|
| **Default Value** | `'invenio_pages/default.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `PAGES_FACETS`
| **Description** | Available facets defined for this module. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pages/config.py (via app.config) |

---

### `PAGES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `PAGES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `PAGES_TEMPLATES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `PAGES_WHITELIST_CONFIG_KEYS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `PERMANENT_SESSION_LIFETIME`
| **Default Value** | `datetime.timedelta(days=31)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | app.config |

---

### `PIDSTORE_APP_LOGGER_HANDLERS`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `PIDSTORE_DATACITE_DOI_PREFIX`
| **Description** | Provide a DOI prefix here. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pidstore/config.py (via app.config) |

---

### `PIDSTORE_OBJECT_ENDPOINTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `PIDSTORE_RECID_FIELD`
| **Description** | Default record id field inside the json data.  This name will be used by the fetcher, to retrieve th... |
|--------------|-----------|
| **Default Value** | `'control_number'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pidstore/config.py (via app.config) |

---

### `PIDSTORE_RECORDID_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `PREFERRED_URL_SCHEME`
| **Default Value** | `'http'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `PREVIEWABLE_ZIP_PREVIEWER_NATIVE_EXTENSIONS`
| **Description** | Extensions for previewable zip. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `PREVIEWER_ABSTRACT_TEMPLATE`
| **Description** | Parent template used by the available previewers. |
|--------------|-----------|
| **Default Value** | `'invenio_previewer/abstract_previewer.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_BASE_CSS_BUNDLES`
| **Description** | Basic bundle which includes Font-Awesome/Bootstrap. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_BASE_JS_BUNDLES`
| **Description** | Basic bundle which includes Bootstrap/jQuery. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_BASE_TEMPLATE`
| **Default Value** | `'invenio_previewer/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `PREVIEWER_CHARDET_BYTES`
| **Description** | Number of bytes to read for character encoding detection by `cchardet`. |
|--------------|-----------|
| **Default Value** | `1024` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_CHARDET_CONFIDENCE`
| **Description** | Confidence threshold for character encoding detection by `cchardet`. |
|--------------|-----------|
| **Default Value** | `0.9` |
| **Type** | float |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_CONTAINER_ITEM_PREFERENCE`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `PREVIEWER_CSV_MAX_BYTES`
| **Description** | Maximum file size in bytes for CSV files. |
|--------------|-----------|
| **Default Value** | `104857600` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_CSV_SNIFFER_ALLOWED_DELIMITERS`
| **Description** | Allowed delimiter characters passed to the ``csv.Sniffer.sniff`` method. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_CSV_VALIDATION_BYTES`
| **Description** | Number of bytes read by CSV previewer to validate the file. |
|--------------|-----------|
| **Default Value** | `1024` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_MAX_FILE_SIZE_BYTES`
| **Description** | Maximum file size in bytes for JSON/XML files. |
|--------------|-----------|
| **Default Value** | `1048576` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_MAX_IMAGE_SIZE_BYTES`
| **Description** | Maximum file size in bytes for image files. |
|--------------|-----------|
| **Default Value** | `524288.0` |
| **Type** | float |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS`
| **Description** | Additional DocumentInitParameters passed to pdfjsLib.getDocument().  See https://mozilla.github.io/p... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_PDF_JS_ENABLE_SCRIPTING`
| **Description** | Enable JavaScript execution in PDF files (disabled by default for security). |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_PREFERENCE`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `PREVIEWER_RECORD_FILE_FACOTRY`
| **Description** | Factory for extracting files from records. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_TXT_MAX_BYTES`
| **Description** | Maximum number of .txt file bytes to preview before truncated. |
|--------------|-----------|
| **Default Value** | `1048576` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_WEB_ARCHIVE_RANGE_REQUESTS`
| **Description** | Whether the file server supports range requests or not. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PREVIEWER_ZIP_MAX_FILES`
| **Description** | Max number of files showed in the ZIP previewer. |
|--------------|-----------|
| **Default Value** | `1000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_previewer/config.py (via app.config) |

---

### `PROPAGATE_EXCEPTIONS`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `PROVIDE_AUTOMATIC_OPTIONS`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `QUEUES_BROKER_URL`
| **Description** | Broker URL for queues.  If the variable is not configured it falls back to the default ``BROKER_URL`... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_queues/config.py (via app.config) |

---

### `QUEUES_CONNECTION_POOL`
| **Description** | Default queues connection pool. |
|--------------|-----------|
| **Default Value** | `get_connection_pool` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_queues/config.py |

---

### `QUEUES_DEFINITIONS`
| **Description** | Static queue definitions. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_queues/config.py (via app.config) |

---

### `RATELIMIT_APPLICATION`
| **Description** | Global rate limit. |
|--------------|-----------|
| **Default Value** | `set_rate_limit` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py |

---

### `RATELIMIT_AUTHENTICATED_USER`
| **Description** | Rate limit for logged in users. |
|--------------|-----------|
| **Default Value** | `'5000 per hour;100 per minute'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `RATELIMIT_ENABLED`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `RATELIMIT_GUEST_USER`
| **Description** | Rate limit for non logged in users. |
|--------------|-----------|
| **Default Value** | `'1000 per hour;60 per minute'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `RATELIMIT_HEADERS_ENABLED`
| **Description** | Enable rate limit headers. (Default: ``True``) |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `RATELIMIT_KEY_FUNC`
| **Description** | Define custom key function.  This config is not part of Flask-Limiter.  This function is used to gen... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `RATELIMIT_PER_ENDPOINT`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RATELIMIT_STORAGE_URI`
| **Description** | Storage backend to store rate-limiting information.      Memory is used by default if no value is pr... |
|--------------|-----------|
| **Default Value** | `'memory://'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `RATELIMIT_STRATEGY`
| **Description** | The rate limiting strategy to use.  The strategy used here is the most consistant but also expensive... |
|--------------|-----------|
| **Default Value** | `'moving-window'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `RDM_ALLOW_EXTERNAL_DOI_VERSIONING`
| **Description** | Allow records with external DOIs to be versioned. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_ALLOW_METADATA_ONLY_RECORDS`
| **Description** | Allow users to publish metadata-only records. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_ALLOW_OWNERS_REMOVE_COMMUNITY_FROM_RECORD`
| **Description** | Allow record owners to remove communities from records.  When set to False, only community curators,... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_ALLOW_RESTRICTED_RECORDS`
| **Description** | Allow users to set restricted/private records. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_ARCHIVE_DOWNLOAD_ENABLED`
| **Description** | Flag to enable/disable the all-in-one download endpoint. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_CITATION_STYLES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_CITATION_STYLES_DEFAULT`
| **Description** | Default citation style |
|--------------|-----------|
| **Default Value** | `'iso690-author-date-cs'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `RDM_COMMUNITIES_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_COMMUNITY_CONTENT_MODERATION_HANDLERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_COMMUNITY_INCLUSION_REQUEST_CLS`
| **Description** | Request type for record inclusion requests. |
|--------------|-----------|
| **Default Value** | `CommunityInclusion` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_COMMUNITY_REQUIRED_TO_PUBLISH`
| **Description** | Enforces at least one community per record. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_COMMUNITY_SUBMISSION_REQUEST_CLS`
| **Description** | Request type for community submission requests. |
|--------------|-----------|
| **Default Value** | `CommunitySubmission` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_CONTENT_MODERATION_HANDLERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_CUSTOM_FIELDS`
| **Description** | Records custom fields definition.  .. code-block:: python      [<custom-field-class-type>, <custom-f... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_CUSTOM_FIELDS_UI`
| **Description** | Upload form custom fields UI configuration.  Of the shape:  .. code-block:: python      [{         s... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_DATACITE_DUMP_OPENAIRE_ACCESS_RIGHTS`
| **Description** | Flag to control dumping DataCite OpenAIRE access rights.  See https://guidelines.openaire.eu/en/late... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_DATACITE_FUNDER_IDENTIFIERS_PRIORITY`
| **Description** | Priority of funder identifiers types to be used for DataCite serialization. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_DEFAULT_FILES_ENABLED`
| **Description** | Deposit page files enabled value on new records. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_DETAIL_SIDE_BAR_MANAGE_ATTRIBUTES_EXTENSION_TEMPLATE`
| **Description** | Side bar manage attributes extension template. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `RDM_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE`
| **Description** | Default additional quota size for a bucket in bytes for files. |
|--------------|-----------|
| **Default Value** | `0` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_FILES_DEFAULT_MAX_FILE_SIZE`
| **Description** | Default maximum file size for a bucket in bytes for files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_FILES_DEFAULT_QUOTA_SIZE`
| **Description** | Default size for a bucket in bytes for files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_FILE_MODIFICATION_PERIOD`
| **Description** | Time period after creation during which modified files can be published. 30 + 30 denotes grace perio... |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=45)` |
| **Type** | timedelta |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_FILE_MODIFICATION_POLICY`
| **Description** | Policy class which evaluates whether published files can be modified by a user. |
|--------------|-----------|
| **Default Value** | `FileModificationPolicyEvaluator` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_IIIF_MANIFEST_FORMATS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED`
| **Description** | Allow editing of published files (by default by admins only). |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES`
| **Description** | List of policies for editing published files immediately.  To enable users to modify the files of th... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED`
| **Description** | Allow increasing of draft's quota from a user's additional quota.  RDM_FILES_DEFAULT_MAX_ADDITIONAL_... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES`
| **Description** | List of policies for user's increasing their quota for a draft.  To enable users and admins to incre... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_IMMEDIATE_RECORD_DELETION_CHECKLIST`
| **Description** | Checklist which appears on the modal to redirect user from immediate record deletion if possible.  T... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_IMMEDIATE_RECORD_DELETION_ENABLED`
| **Description** | Allow users to immediately delete records. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_IMMEDIATE_RECORD_DELETION_POLICIES`
| **Description** | List of policies for immediate record deletion.  Policies are executed in order and the first one to... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_LOCK_EDIT_PUBLISHED_FILES`
| **Description** | Lock editing already published files (enforce record versioning).     signature to implement:    def... |
|--------------|-----------|
| **Default Value** | `lock_edit_published_files` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_MEDIA_FILES_DEFAULT_MAX_FILE_SIZE`
| **Description** | Default maximum file size for a bucket in bytes for media files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_MEDIA_FILES_DEFAULT_QUOTA_SIZE`
| **Description** | Default size for a bucket in bytes for media files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_NAMESPACES`
| **Description** | Custom fields namespaces.  .. code-block:: python      {<namespace>: <uri>, ...}  For example:  .. c... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_NEW_RECORD_VERSION_REVIEW_POLICY`
| **Description** | Policy for when to require a community review for new record versions. |
|--------------|-----------|
| **Default Value** | `NewRecordVersionReviewPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_OAI_PMH_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_OAI_PMH_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_OAI_PMH_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_OPTIONAL_DOI_VALIDATOR`
| **Description** | Optional DOI transitions validate method.  Check the signature of validate_optional_doi for more inf... |
|--------------|-----------|
| **Default Value** | `validate_optional_doi` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_PARENT_PERSISTENT_IDENTIFIERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_PARENT_PERSISTENT_IDENTIFIER_PROVIDERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_PERMISSION_POLICY`
| **Description** | Override the default record permission policy. |
|--------------|-----------|
| **Default Value** | `RDMRecordPermissionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_PERSISTENT_IDENTIFIERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_PERSISTENT_IDENTIFIER_PROVIDERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_QUOTA_INCREASE_POLICY`
| **Description** | Policy class which evaluates whether the quota for drafts can be increased. |
|--------------|-----------|
| **Default Value** | `QuotaIncreasePolicyEvaluator` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_RECORDS_ALLOW_RESTRICTION_AFTER_GRACE_PERIOD`
| **Description** | Whether record access restriction is allowed after the grace period or not. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_CONTAINER_EXTENSIONS`
| **Description** | List of file extensions for container files. Experimental, this config can later be removed. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_IDENTIFIERS_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_RECORDS_LOCATION_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_RECORDS_MAX_FILES_COUNT`
| **Description** | Max amount of files allowed to upload in the deposit form. |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_MAX_MEDIA_FILES_COUNT`
| **Description** | Max amount of media files allowed to upload in the deposit form. |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_PERSONORG_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_RECORDS_RELATED_IDENTIFIERS_SCHEMES`
| **Description** | This variable is used to separate related identifiers. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_REQUIRE_SECRET_LINKS_EXPIRATION`
| **Description** | Whether share access links require an expiration date to be set or not. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_RESTRICTION_GRACE_PERIOD`
| **Description** | Grace period for changing record access to restricted. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=30)` |
| **Type** | timedelta |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_REVIEWS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_RECORDS_UI_EDIT_URL`
| **Description** | Default UI URL for the edit page of a Bibliographic Record. |
|--------------|-----------|
| **Default Value** | `'/uploads/<pid_value>'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORDS_USER_FIXTURE_PASSWORDS`
| **Description** | Overrides for the user fixtures' passwords.  The password set for a user fixture in this dictionary ... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RECORD_DELETION_POLICY`
| **Description** | Policy class which evaluates whether a record can be deleted by a user. |
|--------------|-----------|
| **Default Value** | `RDMRecordDeletionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_RECORD_FILE_EXTRACTORS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RDM_REQUESTS_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_REQUEST_RECORD_DELETION_CHECKLIST`
| **Description** | Checklist which appears on the modal to redirect user from record deletion request if possible. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_REQUEST_RECORD_DELETION_ENABLED`
| **Description** | Allow users to request record deletion. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_REQUEST_RECORD_DELETION_POLICIES`
| **Description** | List of policies for record deletion requests. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RESOURCE_ACCESS_TOKENS_ENABLED`
| **Description** | Flag to show whether RATs feature should be enabled. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RESOURCE_ACCESS_TOKENS_JWT_LIFETIME`
| **Description** | Maximum tokens lifetime. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(seconds=1800)` |
| **Type** | timedelta |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RESOURCE_ACCESS_TOKENS_SUBJECT_SCHEMA`
| **Description** | Resource access token Marshmallow schema for parsing JWT subject. |
|--------------|-----------|
| **Default Value** | `tokens.resource_access.SubjectSchema` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py |

---

### `RDM_RESOURCE_ACCESS_TOKENS_WHITELISTED_JWT_ALGORITHMS`
| **Description** | Accepted JWT algorithms for decoding the RAT. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_RESOURCE_ACCESS_TOKEN_REQUEST_ARG`
| **Description** | URL argument to provide resource access token. |
|--------------|-----------|
| **Default Value** | `'resource_access_token'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_SEARCH_DRAFTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_SEARCH_SORT_BY_VERIFIED`
| **Description** | Sort records by 'verified' first. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_SEARCH_USER_COMMUNITIES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_SEARCH_USER_REQUESTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_SEARCH_VERSIONING`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS`
| **Description** | Exclude file-download stats events whose Referer is the file's own preview page. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RDM_USER_MODERATION_ENABLED`
| **Description** | Flag to enable creation of user moderation requests on specific user actions. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/config.py (via app.config) |

---

### `RECAPTCHA_PRIVATE_KEY`
| **Description** | reCAPTCHA private key. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py |

---

### `RECAPTCHA_PUBLIC_KEY`
| **Description** | reCAPTCHA public key. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py |

---

### `RECORDS_FILES_REST_ENDPOINTS`
| **Description** | REST endpoints configuration.  You can configure the REST API endpoint to access the record's files ... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_files/config.py (via app.config) |

---

### `RECORDS_PERMISSIONS_RECORD_POLICY`
| **Default Value** | `'invenio_records_permissions.policies.RecordPermissionPolicy'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `RECORDS_REFRESOLVER_CLS`
| **Description** | Custom JSONSchemas ref resolver class.  Note that when using a custom ref resolver class you should ... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `RECORDS_REFRESOLVER_STORE`
| **Description** | JSONSchemas ref resolver store.  Used together with ``RECORDS_REFRESOLVER_CLS`` to provide a specifi... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `RECORDS_RESOURCES_ALLOW_EMPTY_FILES`
| **Description** | Allow empty files to be uploaded. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_ARCHIVE_DOWNLOAD_MAX_SIZE`
| **Description** | Max total file size (bytes) for archive download. ``None`` disables the cap. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_DEFAULT_TRANSFER_TYPE`
| **Description** | Default transfer class to use. One of 'L' (local), 'F' (fetch), 'R' (point to remote), 'M' (multipar... |
|--------------|-----------|
| **Default Value** | `'L'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_EXTRACTED_STREAM_CHUNK_SIZE`
| **Description** | Chunk size of extracted stream used in ContainerItemResult.send_file(). |
|--------------|-----------|
| **Default Value** | `65536` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_FILES_ALLOWED_DOMAINS`
| **Description** | Explicitly allowed domains for external file fetching.  Only file URLs from these domains will be al... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_IMAGE_FORMATS`
| **Description** | Which image formats to extract metadata for. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_TRANSFERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `RECORDS_RESOURCES_ZIP_FORMATS`
| **Description** | File extensions interpreted as ZIP files. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_ZIP_MAX_ENTRIES`
| **Description** | Max allowed entries inside ZIP file. |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_ZIP_MAX_HEADER_SIZE`
| **Description** | Max header size of ZIP file that can be preloaded. |
|--------------|-----------|
| **Default Value** | `65536` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_ZIP_MAX_LISTING_ENTRIES`
| **Description** | Max entries returned by the container listing API. |
|--------------|-----------|
| **Default Value** | `1000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_ZIP_MAX_RATIO`
| **Description** | Max allowed compression ratio of an entry inside ZIP file. |
|--------------|-----------|
| **Default Value** | `200.0` |
| **Type** | float |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_RESOURCES_ZIP_MAX_TOTAL_UNCOMPRESSED`
| **Description** | Max allowed uncompressed size of ZIP. |
|--------------|-----------|
| **Default Value** | `524288000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_resources/config.py (via app.config) |

---

### `RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY`
| **Description** | Default create permission factory: reject any request. |
|--------------|-----------|
| **Default Value** | `deny_all` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY`
| **Description** | Default delete permission factory: reject any request. |
|--------------|-----------|
| **Default Value** | `deny_all` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_DEFAULT_LIST_PERMISSION_FACTORY`
| **Description** | Default list permission factory: allow all requests |
|--------------|-----------|
| **Default Value** | `allow_all` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_DEFAULT_LOADERS`
| **Default Value** | `{'application/json': lambda: request.get_json(), 'application/json-patch+json': lambda: request.get_...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY`
| **Description** | Default read permission factory: check if the record exists. |
|--------------|-----------|
| **Default Value** | `check_search` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_DEFAULT_RESULTS_SIZE`
| **Description** | Default search results size. |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_DEFAULT_SORT`
| **Default Value** | `dict(records=dict(query='bestmatch', noquery='mostrecent'))` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY`
| **Description** | Default update permission factory: reject any request. |
|--------------|-----------|
| **Default Value** | `deny_all` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_ENDPOINTS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `RECORDS_REST_FACETS`
| **Default Value** | `dict(records=dict(aggs=dict(type=dict(terms=dict(field='type'))), post_filters=dict(type=terms_filte...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_FACETS_POST_FILTERS_PROPAGATE`
| **Description** | Define if the post_filters facets in one category should be applied as filters to all the other cate... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_SEARCH_ERROR_HANDLERS`
| **Default Value** | `{'query_parsing_exception': 'invenio_records_rest.views:search_query_parsing_exception_handler', 'qu...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_REST_SORT_OPTIONS`
| **Default Value** | `dict(records=dict(bestmatch=dict(title=_('Best match'), fields=['_score'], default_order='desc', ord...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_rest/config.py |

---

### `RECORDS_UI_BASE_TEMPLATE`
| **Default Value** | `'invenio_records_ui/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `RECORDS_UI_DEFAULT_PERMISSION_FACTORY`
| **Description** | Configure the default permission factory. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_ui/config.py (via app.config) |

---

### `RECORDS_UI_ENDPOINTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `RECORDS_UI_EXPORT_FORMATS`
| **Description** | Defaut record serialization views.  The structure of the dictionary is as follows:  .. code-block:: ... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_ui/config.py (via app.config) |

---

### `RECORDS_UI_LOGIN_ENDPOINT`
| **Description** | Endpoint where redirect the user if login is required. |
|--------------|-----------|
| **Default Value** | `'security.login'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_ui/config.py (via app.config) |

---

### `RECORDS_UI_TOMBSTONE_TEMPLATE`
| **Description** | Configure the tombstone template. |
|--------------|-----------|
| **Default Value** | `'invenio_records_ui/tombstone.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_ui/config.py (via app.config) |

---

### `RECORDS_VALIDATION_TYPES`
| **Description** | Pass additional types when validating a record against a schema. For more details, see: `<https://py... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records/config.py (via app.config) |

---

### `RECORD_ROUTES`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `REMEMBER_COOKIE_DURATION`
| **Description** | Remember me cookie life time changed to 90 days instead of 365 days. |
|--------------|-----------|
| **Default Value** | `timedelta(days=90)` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py |

---

### `REPOSITORY_DESCRIPTION`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `REPOSITORY_KEYWORDS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `REPOSITORY_NAME`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `REPOSITORY_SUBTITLE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `REPOSITORY_SUPPORT_CONTACT`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_ATTRS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_TAGS`
| **Description** | Extend allowed HTML tags list for requests comments content. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_COMMENT_PREVIEW_LIMIT`
| **Description** | Number of most recent child comments to inline in parent's search index.  This limits the size of in... |
|--------------|-----------|
| **Default Value** | `5` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_ENTITY_RESOLVERS`
| **Description** | Registered resolvers for resolving/creating references in request metadata. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_ERROR_HANDLERS`
| **Default Value** | `{**request_error_handlers, InvalidAccessRestrictions: create_error_handler(lambda e: HTTPJSONExcepti...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `REQUESTS_EVENTS_SERVICE_COMPONENTS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `REQUESTS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REQUESTS_FILES_DEFAULT_MAX_FILE_SIZE`
| **Description** | 10MB |
|--------------|-----------|
| **Default Value** | `10000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_FILES_DEFAULT_QUOTA_SIZE`
| **Description** | 100MB |
|--------------|-----------|
| **Default Value** | `100000000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_LOCKING_ENABLED`
| **Description** | Enable locking/unlocking for request conversations. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_MODERATION_ROLE`
| **Description** | ID of the Role used for moderation. |
|--------------|-----------|
| **Default Value** | `'administration-moderation'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_PERMISSION_POLICY`
| **Description** | The requests permission policy, extended to work with guest access requests. |
|--------------|-----------|
| **Default Value** | `RDMRequestsPermissionPolicy` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`register_workflow`](#) in `workflows.py`
  > Register a submission/review workflow that records can go through.  A workflow defines the path a record takes from being created to being published - for example, who may create it, whether it needs ...
---

### `REQUESTS_REGISTERED_EVENT_TYPES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `REQUESTS_REGISTERED_TYPES`
| **Description** | Configuration for registered Request Types. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_REVIEWERS_ENABLED`
| **Description** | Enable reviewers for requests. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_REVIEWERS_MAX_NUMBER`
| **Description** | Maximum number of reviewers allowed for a request. |
|--------------|-----------|
| **Default Value** | `15` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REQUESTS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REQUESTS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REQUESTS_TIMELINE_PAGE_SIZE`
| **Description** | Amount of items per page on the request details timeline |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/config.py (via app.config) |

---

### `REQUESTS_USER_MODERATION_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REQUESTS_USER_MODERATION_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REQUESTS_USER_MODERATION_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `REST_CSRF_ENABLED`
| **Description** | Enable CSRF middleware. (Default: ``False``).  .. note::    The CSRF middleware accepts some configu... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `REST_ENABLE_CORS`
| **Description** | Enable CORS configuration. (Default: ``False``). |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rest/config.py |

---

### `REST_MIMETYPE_QUERY_ARG_NAME`
| **Description** | Name of the query argument to specify the mimetype wanted for the output.    Set it to None to disab... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rest/config.py |

---

### `ROR_CLIENT_ID`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `S3_ACCESS_KEY_ID`
| **Description** | The access key to use when creating the client.  This is entirely optional, and if not provided, the... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `S3_CONFIG_EXTRA`
| **Description** | Additional configuration to be passed to S3f3. In some cases, specially those not using AWS S3, some... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

---

### `S3_DEFAULT_BLOCK_SIZE`
| **Description** | Default block size value used to send multi-part uploads to S3. Typically 5Mb is minimum allowed by ... |
|--------------|-----------|
| **Default Value** | `5242880` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

---

### `S3_ENDPOINT_URL`
| **Description** | S3 server URL endpoint.  If using Amazon AWS S3 service this config variable can be set to None as t... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `S3_MAXIMUM_NUMBER_OF_PARTS`
| **Description** | Maximum number of parts to be used. See `AWS Multipart Upload Overview <https://docs.aws.amazon.com/... |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

---

### `S3_REGION_NAME`
| **Description** | S3 region name  This is entirely optional, and if not provided, the region name will be automaticall... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

---

### `S3_SECRET_ACCESS_KEY`
| **Description** | The secret key to use when creating the client.  This is entirely optional, and if not provided, the... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `S3_SIGNATURE_VERSION`
| **Description** | Version of the S3 signature algorithm. Can be 's3' (v2) or 's3v4' (v4). See `Amazon Boto3 documentat... |
|--------------|-----------|
| **Default Value** | `'s3v4'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

---

### `S3_UPLOAD_URL_EXPIRATION`
| **Description** | Number of seconds the file upload URL will be valid. The default here is 7 days to allow large file ... |
|--------------|-----------|
| **Default Value** | `604800` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

---

### `S3_URL_EXPIRATION`
| **Description** | Number of seconds the file serving URL will be valid.  See `Amazon Boto3 documentation on presigned ... |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_s3/config.py (via app.config) |

---

### `SEARCH_CLIENT_CONFIG`
| **Description** | Dictionary of options for the Elasticsearch/OpenSearch client.  The value of this variable is passed... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SEARCH_ELASTIC_HOSTS`
| **Description** | Deprecated alias for ``SEARCH_HOSTS``. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search/config.py (via app.config) |

---

### `SEARCH_HOSTS`
| **Description** | Search hosts. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SEARCH_INDEX_PREFIX`
| **Description** | Any index, alias and templates will be prefixed with this string.  Useful to host multiple instances... |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SEARCH_MAPPINGS`
| **Description** | List of aliases for which, their search mappings should be created.  - If `None` all aliases (and th... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search/config.py (via app.config) |

---

### `SEARCH_RESULTS_MIN_SCORE`
| **Description** | If set, the `min_score` parameter is added to each search request body.  The `min_score` parameter e... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search/config.py (via app.config) |

---

### `SEARCH_UI_BASE_TEMPLATE`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SEARCH_UI_HEADER_TEMPLATE`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SEARCH_UI_JSTEMPLATE_COUNT`
| **Description** | Configure the count template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/count.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_ERROR`
| **Description** | Configure the error page template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/error.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_FACETS`
| **Description** | Configure the facets template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/facets.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_LOADING`
| **Description** | Configure the loading template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/loading.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_PAGINATION`
| **Description** | Configure the pagination template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/pagination.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_RANGE`
| **Description** | Configure the range template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/range.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_RANGE_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `SEARCH_UI_JSTEMPLATE_RESULTS`
| **Description** | Configure the results template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/results.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_SELECT_BOX`
| **Description** | Configure the select box template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/selectbox.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_JSTEMPLATE_SORT_ORDER`
| **Description** | Configure the toggle button template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/togglebutton.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_SEARCH_API`
| **Description** | Configure the search engine endpoint. |
|--------------|-----------|
| **Default Value** | `'/api/records/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_SEARCH_CONFIG_GEN`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `SEARCH_UI_SEARCH_INDEX`
| **Description** | Name of the search index used. |
|--------------|-----------|
| **Default Value** | `'records'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

---

### `SEARCH_UI_SEARCH_TEMPLATE`
| **Description** | Configure the search page template. |
|--------------|-----------|
| **Default Value** | `'invenio_search_ui/search.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `SEARCH_UI_SEARCH_VIEW`
| **Description** | Default funtion to do the `search` route. |
|--------------|-----------|
| **Default Value** | `search` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_search_ui/config.py |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `SECRET_KEY`
| **Description** | Flask secret key.  Each installation (dev, production, ...) needs a separate key.  SECURITY WARNING:... |
|--------------|-----------|
| **Default Value** | `'CHANGE_ME'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SECRET_KEY_FALLBACKS`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_AUTO_LOGIN_AFTER_CONFIRM`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_BLUEPRINT_NAME`
| **Default Value** | `'security'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_CHANGEABLE`
| **Description** | Allow password change by users. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SECURITY_CHANGE_PASSWORD_TEMPLATE`
| **Description** | Default template for change password. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/change_password.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_CHANGE_SALT`
| **Default Value** | `'change-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_CHANGE_URL`
| **Description** | URL endpoint for password change. |
|--------------|-----------|
| **Default Value** | `'/account/settings/password/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_CLI_ROLES_NAME`
| **Default Value** | `'roles'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_CLI_USERS_NAME`
| **Default Value** | `'users'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_CONFIRMABLE`
| **Description** | Allow user to confirm their email address. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SECURITY_CONFIRM_EMAIL_WITHIN`
| **Description** | Amount of time the email confirmation link is active.  Note, since the confirmation link will also l... |
|--------------|-----------|
| **Default Value** | `'30 minutes'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_CONFIRM_ERROR_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_CONFIRM_SALT`
| **Default Value** | `'confirm-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_CONFIRM_URL`
| **Default Value** | `'/confirm'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_DEFAULT_HTTP_AUTH_REALM`
| **Default Value** | `'Login Required'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_DEFAULT_REMEMBER_ME`
| **Description** | "Remember me" default value in login form.  This is only the default value in the login form. A user... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_DEPRECATED_HASHING_SCHEMES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `SECURITY_DEPRECATED_PASSWORD_SCHEMES`
| **Description** | Deprecated password hashing algorithms.  Password hashes in a deprecated scheme are automatically mi... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_EMAIL_HTML`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_EMAIL_PLAINTEXT`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_EMAIL_SUBJECT_CONFIRM`
| **Default Value** | `'Please confirm your email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE`
| **Default Value** | `'Your password has been changed'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE`
| **Default Value** | `'Your password has been reset'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_EMAIL_SUBJECT_PASSWORD_RESET`
| **Default Value** | `'Password reset instructions'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_EMAIL_SUBJECT_REGISTER`
| **Description** | Email subject for account registration emails. |
|--------------|-----------|
| **Default Value** | `'Welcome'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `SECURITY_FLASH_MESSAGES`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_FORGOT_PASSWORD_TEMPLATE`
| **Description** | Default template for password recovery (asking for email). |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/forgot_password.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_HASHING_SCHEMES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `SECURITY_I18N_DIRNAME`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-...` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_I18N_DOMAIN`
| **Default Value** | `'flask_security'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_LOGIN_SALT`
| **Default Value** | `'login-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_LOGIN_URL`
| **Description** | URL endpoint for login. |
|--------------|-----------|
| **Default Value** | `'/login/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_LOGIN_USER_TEMPLATE`
| **Description** | Default template for login. |
|--------------|-----------|
| **Default Value** | `'invenio_oauthclient/login_user.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_LOGIN_WITHIN`
| **Default Value** | `'1 days'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_LOGIN_WITHOUT_CONFIRMATION`
| **Description** | Allow users to login without first confirming their email address. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SECURITY_LOGOUT_URL`
| **Description** | URL endpoint for logout. |
|--------------|-----------|
| **Default Value** | `'/logout/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_MSG_ALREADY_CONFIRMED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_CONFIRMATION_EXPIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_CONFIRMATION_REQUEST`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_CONFIRMATION_REQUIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_CONFIRM_REGISTRATION`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_DISABLED_ACCOUNT`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_EMAIL_CONFIRMED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_EMAIL_NOT_PROVIDED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_FORGOT_PASSWORD`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_INVALID_CONFIRMATION_TOKEN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_INVALID_EMAIL_ADDRESS`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_INVALID_LOGIN_TOKEN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_INVALID_PASSWORD`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_INVALID_REDIRECT`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_LOCAL_LOGIN_DISABLED`
| **Description** | The error to be displayed in REST login when local login is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_MSG_LOGIN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_LOGIN_EMAIL_SENT`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_LOGIN_EXPIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_BREACHED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_BREACHED_SITE_ERROR`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_CHANGE`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_CHANGE_DISABLED`
| **Description** | The error to be displayed in REST password change when it is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_MSG_PASSWORD_INVALID_LENGTH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_IS_THE_SAME`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_MISMATCH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_NOT_PROVIDED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_NOT_SET`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_RECOVERY_DISABLED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_RESET`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_RESET_DISABLED`
| **Description** | The error to be displayed in REST password reset when it is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_MSG_PASSWORD_RESET_EXPIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_RESET_REQUEST`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_PASSWORD_TOO_SIMPLE`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_REFRESH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_REGISTRATION_DISABLED`
| **Description** | The error to be displayed in REST registration when it is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_MSG_RETYPE_PASSWORD_MISMATCH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_UNAUTHORIZED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_MSG_USER_DOES_NOT_EXIST`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | app.config |

---

### `SECURITY_PASSWORD_BREACHED_COUNT`
| **Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `SECURITY_PASSWORD_CHECK_BREACHED`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_PASSWORD_COMPLEXITY_CHECKER`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_PASSWORD_HASH`
| **Description** | Default password hashing algorithm for new passwords. |
|--------------|-----------|
| **Default Value** | `'pbkdf2_sha512'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_PASSWORD_LENGTH_MIN`
| **Default Value** | `6` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `SECURITY_PASSWORD_SALT`
| **Description** | Salt for storing passwords. |
|--------------|-----------|
| **Default Value** | `'CHANGE_ME'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_PASSWORD_SCHEMES`
| **Description** | Supported password hashing algorithms (for passwords already stored).  You should include both the d... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_PASSWORD_SINGLE_HASH`
| **Description** | Password hashing algorithms requiring single hasing only. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_POST_CHANGE_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_POST_CONFIRM_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_POST_LOGIN_VIEW`
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_POST_LOGOUT_VIEW`
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_POST_REGISTER_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_POST_RESET_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_RECOVERABLE`
| **Description** | Allow password recovery by users. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SECURITY_REGISTERABLE`
| **Description** | Allow users to register. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SECURITY_REGISTER_URL`
| **Description** | URL endpoint for user registation. |
|--------------|-----------|
| **Default Value** | `'/signup/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_REGISTER_USER_TEMPLATE`
| **Description** | Default template for user registration. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/register_user.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_RESET_PASSWORD_TEMPLATE`
| **Description** | Default template for password recovery (reset of the password). |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/reset_password.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_RESET_PASSWORD_WITHIN`
| **Description** | Amount of time the password reset link is active.  Note, since the confirmation link will also login... |
|--------------|-----------|
| **Default Value** | `'30 minutes'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_RESET_SALT`
| **Default Value** | `'reset-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_RESET_URL`
| **Description** | URL endpoint for password recovery. |
|--------------|-----------|
| **Default Value** | `'/lost-password/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_SEND_CONFIRMATION_TEMPLATE`
| **Description** | Default template for email confirmation. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/send_confirmation.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_SEND_LOGIN_TEMPLATE`
| **Description** | Default template for email confirmation. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/send_login.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_SEND_PASSWORD_CHANGE_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_SEND_PASSWORD_RESET_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_SEND_REGISTER_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SECURITY_SUBDOMAIN`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_TOKEN_AUTHENTICATION_HEADER`
| **Default Value** | `'Authentication-Token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_TOKEN_AUTHENTICATION_KEY`
| **Default Value** | `'auth_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SECURITY_TOKEN_MAX_AGE`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_TRACKABLE`
| **Description** | Enable user tracking on login. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/config.py (via app.config) |

---

### `SECURITY_URL_PREFIX`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SECURITY_USER_IDENTITY_ATTRIBUTES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `SECURITY_ZXCVBN_MINIMUM_SCORE`
| **Default Value** | `3` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `SEND_FILE_MAX_AGE_DEFAULT`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SENTRY_DSN`
| **Description** | Set SENTRY_DSN environment variable. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_logging/config.py (via app.config) |

---

### `SERVER_NAME`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SESSION_COOKIE_DOMAIN`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SESSION_COOKIE_HTTPONLY`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SESSION_COOKIE_NAME`
| **Default Value** | `'session'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `SESSION_COOKIE_PARTITIONED`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SESSION_COOKIE_PATH`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `SESSION_COOKIE_SAMESITE`
| **Description** | Restricts how cookies are sent with requests from external sites. |
|--------------|-----------|
| **Default Value** | `'Lax'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `SESSION_COOKIE_SECURE`
| **Description** | Sets cookie with the secure flag by default. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SESSION_KEY_BITS`
| **Default Value** | `64` |
|--------------|-----------|
| **Type** | int |
| **Source** | app.config |

---

### `SESSION_RANDOM_SOURCE`
| **Default Value** | `<random.SystemRandom object at 0x753c2cc20>` |
|--------------|-----------|
| **Type** | SystemRandom |
| **Source** | app.config |

---

### `SESSION_REFRESH_EACH_REQUEST`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SETTINGS_TEMPLATE`
| **Description** | Settings page template used for e.g. display user settings views. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_settings.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `SITEMAP_MAX_ENTRY_COUNT`
| **Description** | Maximum number of entries (<url> or <sitemap>) per file.  The Sitemap protocol sets it at 50_000, bu... |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_sitemap/config.py (via app.config) |

---

### `SITEMAP_ROOT_VIEW_ENABLED`
| **Description** | Enable the `/sitemap.xml` endpoint serving the first sitemap index. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_sitemap/config.py (via app.config) |

---

### `SITEMAP_SECTIONS`
| **Description** | Instances of `sitemap.SitemapSection` that will populate the Sitemap files. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_sitemap/config.py (via app.config) |

---

### `SITE_API_URL`
| **Default Value** | `'https://127.0.0.1:5000/api'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SITE_UI_URL`
| **Default Value** | `'https://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SQLALCHEMY_BINDS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `SQLALCHEMY_DATABASE_URI`
| **Default Value** | `'sqlite:////Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instan...` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `SQLALCHEMY_ECHO`
| **Description** | Enable to see all SQL queries. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `SQLALCHEMY_ENGINE_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `SQLALCHEMY_RECORD_QUERIES`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `SQLALCHEMY_TRACK_MODIFICATIONS`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `STATS_AGGREGATIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `STATS_EVENTS`
| **Description** | Enabled Events.  Each key is the name of an event. A queue will be created for each event.  If the d... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_stats/config.py (via app.config) |

---

### `STATS_EVENTS_UTC_DATETIME_ENABLED`
| **Description** | Enable timezone-aware UTC datetimes for event timestamps.  When set to ``False`` (default), naive UT... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_stats/config.py (via app.config) |

---

### `STATS_MQ_EXCHANGE`
| **Default Value** | `Exchange('events', type='direct', delivery_mode='transient')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_stats/config.py |

---

### `STATS_PERMISSION_FACTORY`
| **Description** | Permission factory used by the statistics REST API.  This is a function which returns a permission g... |
|--------------|-----------|
| **Default Value** | `permissions_policy_lookup_factory` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `STATS_QUERIES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `STATS_REGISTER_INDEX_TEMPLATES`
| **Description** | Register templates as index templates.  Default behaviour will register the templates as search temp... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_stats/config.py (via app.config) |

---

### `STATS_REGISTER_RECEIVERS`
| **Description** | Enable the registration of signal receivers.  Default is ``True``. The signal receivers are function... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_stats/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_stats`](#) in `stats.py`
  > Set up usage statistics (record views, downloads, etc.).  Enables the collection and aggregation of usage events, such as how many times a record was viewed or a file was downloaded, so this data can ...
---

### `TEMPLATES_AUTO_RELOAD`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `TESTING`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `THEME_401_TEMPLATE`
| **Description** | The template used for 401 Unauthorized errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/401.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_403_TEMPLATE`
| **Description** | The template used for 403 Forbidden errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/403.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_404_TEMPLATE`
| **Description** | The template used for 404 Not Found errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/404.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_429_TEMPLATE`
| **Description** | The template used for 429 Too Many Requests errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/429.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_500_TEMPLATE`
| **Description** | The template used for 500 Internal Server Error errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/500.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_BASE_TEMPLATE`
| **Description** | Template which all templates in Invenio-Theme all extends from.  Defaults to value of :const:`BASE_T... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_COVER_TEMPLATE`
| **Description** | Template which all cover templates in Invenio-Theme all extends from.  Defaults to value of :const:`... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_cover.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_CSS_TEMPLATE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_ERROR_TEMPLATE`
| **Description** | Base template for error pages. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_error.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_FOOTER_TEMPLATE`
| **Description** | Footer template which is normally included in :data:`BASE_TEMPLATE`. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/footer.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_FRONTPAGE`
| **Description** | Enable or disable basic frontpage view. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_FRONTPAGE_LOGO`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_FRONTPAGE_TEMPLATE`
| **Description** | Template for front page. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/frontpage.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_FRONTPAGE_TITLE`
| **Description** | The title shown on the frontpage. |
|--------------|-----------|
| **Default Value** | `l'Invenio'` |
| **Type** | LazyString |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_GENERATOR`
| **Description** | Generator meta tag to identify the software that generated the page.  Accepts a string or a func ret... |
|--------------|-----------|
| **Default Value** | `'Invenio'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_GOOGLE_SITE_VERIFICATION`
| **Description** | List of Google Site Verification tokens to be used.  This adds the Google Site Verification into the... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_HEADER_LOGIN_TEMPLATE`
| **Description** | Header login template, included in :data:`THEME_HEADER_TEMPLATE`. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/header_login.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_HEADER_TEMPLATE`
| **Description** | Header template which is normally included in :data:`BASE_TEMPLATE`. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/header.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_ICONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `THEME_JAVASCRIPT_TEMPLATE`
| **Description** | Javascript assets template, normally included in :data:`BASE_TEMPLATE`.  The default template just i... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/javascript.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_LOGO`
| **Description** | The logo to be used on the header and on the cover. |
|--------------|-----------|
| **Default Value** | `'images/invenio-white.svg'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_LOGO_ADMIN`
| **Description** | The logo to be used on the admin views header. |
|--------------|-----------|
| **Default Value** | `'images/invenio-white.svg'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_MATHJAX_CDN`
| **Description** | MathJax configuration for rendering mathematical formulas. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_META_ROBOT_TAGS`
| **Description** | Robots meta tag to control indexing of the page.  Accepts a list of dicts that will be converted int... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_SEARCHBAR`
| **Description** | Enable or disable the header search bar. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_SEARCH_ENDPOINT`
| **Description** | The endpoint for the search bar. |
|--------------|-----------|
| **Default Value** | `'/search'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_SETTINGS_TEMPLATE`
| **Description** | Template which all settings templates in Invenio-Theme all extends from.  Defaults to value of :cons... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_settings.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

---

### `THEME_SHOW_FRONTPAGE_INTRO_SECTION`
| **Description** | Front page intro section visibility |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_SITENAME`
| **Description** | The name of the site to be used on the header and as a title. |
|--------------|-----------|
| **Default Value** | `l'Invenio'` |
| **Type** | LazyString |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_SITEURL`
| **Default Value** | `'http://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `THEME_TRACKINGCODE_TEMPLATE`
| **Description** | Template for including a tracking code for web analytics.  The default template does not include any... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/trackingcode.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_theme/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `THEME_TWITTERHANDLE`
| **Description** | Twitter handle. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `TRAP_BAD_REQUEST_ERRORS`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | app.config |

---

### `TRAP_HTTP_EXCEPTIONS`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `TRUSTED_HOSTS`
| **Description** | A list of host/domain names that can be served.  This is a security measure to prevent HTTP Host hea... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app/config.py (via app.config) |

---

### `TYPE_CHECKING`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `USERPROFILES`
| **Description** | Enable or disable module extensions. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

---

### `USERPROFILES_BASE_TEMPLATE`
| **Description** | Base templates for user profile module. |
|--------------|-----------|
| **Default Value** | `'invenio_userprofiles/base.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

---

### `USERPROFILES_EMAIL_ENABLED`
| **Description** | Include the user email in the profile form. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

---

### `USERPROFILES_EXTEND_SECURITY_FORMS`
| **Description** | Extend the Invenio-Accounts user registration forms. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

---

### `USERPROFILES_PROFILE_TEMPLATE`
| **Description** | Default profile template. |
|--------------|-----------|
| **Default Value** | `'invenio_userprofiles/settings/profile.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

---

### `USERPROFILES_PROFILE_URL`
| **Description** | Default profile URL endpoint. |
|--------------|-----------|
| **Default Value** | `'/account/settings/profile/'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

---

### `USERPROFILES_READ_ONLY`
| **Description** | Make the user profiles read-only. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
- [`configure_einfra_oidc`](#) in `einfra.py`
  > Set up "Log in with e-INFRA" (CESNET/Perun) for the repository.  This enables single sign-on through the CESNET e-INFRA identity provider, so users can log in with their e-INFRA/Perun account instead ...
---

### `USERPROFILES_SETTINGS_TEMPLATE`
| **Description** | Settings base templates for user profile module. |
|--------------|-----------|
| **Default Value** | `'invenio_userprofiles/settings/base.html'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/config.py (via app.config) |

---

### `USERS_RESOURCES_AVATAR_COLORS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `USERS_RESOURCES_DOMAINS_ORG_SCHEMA`
| **Description** | Domains organisation schema config. |
|--------------|-----------|
| **Default Value** | `OrgPropsSchema` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_users_resources/config.py |

---

### `USERS_RESOURCES_DOMAINS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_DOMAINS_SEARCH_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_DOMAINS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_GROUPS_ADMIN_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_GROUPS_ADMIN_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_GROUPS_ADMIN_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_GROUPS_ENABLED`
| **Description** | Config to enable features related to existence of groups. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_users_resources/config.py (via app.config) |

---

### `USERS_RESOURCES_MODERATION_LOCK_DEFAULT_TIMEOUT`
| **Description** | Default timeout, in seconds, to lock a user when moderating. |
|--------------|-----------|
| **Default Value** | `30` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_users_resources/config.py (via app.config) |

---

### `USERS_RESOURCES_MODERATION_LOCK_RENEWAL_TIMEOUT`
| **Description** | Renewal timeout, in seconds, to increase the lock time for a user when moderating. |
|--------------|-----------|
| **Default Value** | `120` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_users_resources/config.py (via app.config) |

---

### `USERS_RESOURCES_PROTECTED_GROUP_NAMES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `USERS_RESOURCES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_SEARCH_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USERS_RESOURCES_SERVICE_SCHEMA`
| **Description** | Schema used by the users service. |
|--------------|-----------|
| **Default Value** | `NotificationsUserSchema` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `USERS_RESOURCES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `USER_DASHBOARD_MENU_OVERRIDES`
| **Description** | Overrides for "dashboard" menu. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py (via app.config) |

---

### `USE_X_SENDFILE`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | app.config |

---

### `VCS_TEMPLATE_INDEX`
| **Default Value** | `'invenio_vcs/rdm-index.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `VCS_TEMPLATE_INDEX_ITEM`
| **Default Value** | `'invenio_vcs/rdm-index-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `VCS_TEMPLATE_RELEASE_ITEM`
| **Default Value** | `'invenio_vcs/rdm-release-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `VCS_TEMPLATE_REPO_SWITCH`
| **Default Value** | `'invenio_vcs/rdm-repo-switch.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `VCS_TEMPLATE_VIEW`
| **Default Value** | `'invenio_vcs/rdm-view.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_app_rdm/config.py |

---

### `VOCABULARIES_AFFILIATIONS_EDMO_COUNTRY_MAPPING`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `VOCABULARIES_AFFILIATION_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_AWARDS_EC_ROR_ID`
| **Description** | ROR ID for EC funder. |
|--------------|-----------|
| **Default Value** | `'00k4n6c32'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_AWARDS_OPENAIRE_FUNDERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `VOCABULARIES_AWARD_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `VOCABULARIES_CUSTOM_VOCABULARY_TYPES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | app.config |

---

### `VOCABULARIES_DATASTREAM_READERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_datastreams`](#) in `datastreams.py`
  > Register custom sources for importing vocabularies (fixtures) into the repository.  Vocabularies (controlled lists such as languages, resource types or licenses) can be loaded from files or external s...
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_DATASTREAM_TRANSFORMERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_datastreams`](#) in `datastreams.py`
  > Register custom sources for importing vocabularies (fixtures) into the repository.  Vocabularies (controlled lists such as languages, resource types or licenses) can be loaded from files or external s...
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_DATASTREAM_WRITERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_datastreams`](#) in `datastreams.py`
  > Register custom sources for importing vocabularies (fixtures) into the repository.  Vocabularies (controlled lists such as languages, resource types or licenses) can be loaded from files or external s...
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_FUNDER_DOI_PREFIX`
| **Description** | DOI prefix for the identifier formed with the FundRef id. |
|--------------|-----------|
| **Default Value** | `'10.13039'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_FUNDER_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_IDENTIFIER_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `VOCABULARIES_NAMES_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_ORCID_ACCESS_KEY`
| **Description** | ORCID access key to access the s3 bucket. |
|--------------|-----------|
| **Default Value** | `'CHANGEME'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_ORCID_ORG_IDS_MAPPING_PATH`
| **Description** | Path to the CSV file for mapping ORCiD organization IDs to affiliation IDs.  The path can be specifi... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_ORCID_SECRET_KEY`
| **Description** | ORCID secret key to access the s3 bucket. |
|--------------|-----------|
| **Default Value** | `'CHANGEME'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_ORCID_SUMMARIES_BUCKET`
| **Description** | ORCID summaries bucket name. |
|--------------|-----------|
| **Default Value** | `'v3.0-summaries'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_ORCID_SYNC_MAX_WORKERS`
| **Description** | ORCID max number of simultaneous workers/connections. |
|--------------|-----------|
| **Default Value** | `32` |
| **Type** | int |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_ORCID_SYNC_SINCE`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `VOCABULARIES_RESOURCE_CONFIG`
| **Description** | Configure the resource. |
|--------------|-----------|
| **Default Value** | `VocabulariesResourceConfig` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_SERVICE_CONFIG`
| **Description** | Configure the service. |
|--------------|-----------|
| **Default Value** | `VocabulariesServiceConfig` |
| **Type** | unknown |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py |

**Set/Referenced by:**
- [`configure_generic_parameters`](#) in `generic_parameters.py`
  > Set up the core, infrastructure-level configuration of the repository.  This is the main "plumbing" function that should normally be called first, before any of the other ``configure_*`` functions. It...
---

### `VOCABULARIES_SUBJECTS_EUROSCIVOC_FILE_URL`
| **Description** | Subject EuroSciVoc file download link. |
|--------------|-----------|
| **Default Value** | `'https://publications.europa.eu/resource/distribution/euroscivoc/rdf/skos_ap_eu/EuroSciVoc-skos-ap-e...` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_SUBJECTS_GEMET_FILE_URL`
| **Default Value** | `'https://www.eionet.europa.eu/gemet/latest/gemet.rdf.gz'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `VOCABULARIES_SUBJECTS_NVS_FILE_URL`
| **Description** | Subject NVS-P02 file download link. |
|--------------|-----------|
| **Default Value** | `'http://vocab.nerc.ac.uk/collection/P02/current/?_profile=nvs&_mediatype=application/rdf+xml'` |
| **Type** | str |
| **Source** | /Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/config.py (via app.config) |

---

### `VOCABULARIES_SUBJECTS_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `VOCABULARIES_TYPES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `VOCABULARIES_TYPES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | app.config |

---

### `WEBPACKEXT_MANIFEST_PATH`
| **Default Value** | `'dist/manifest.json'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `WEBPACKEXT_NPM_PKG_CLS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `WEBPACKEXT_PROJECT`
| **Default Value** | `'invenio_assets.webpack:webpack_project'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

**Set/Referenced by:**
- [`configure_ui`](#) in `ui.py`
  > Set up the repository's branding, name and general look-and-feel.  Configures what visitors see: the repository's name and description shown in the browser tab/search results/front page, the theme, th...
---

### `WEBPACKEXT_PROJECT_BUILDDIR`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/assets'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `WEBPACKEXT_PROJECT_DISTDIR`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static/...` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `WEBPACKEXT_PROJECT_DISTURL`
| **Default Value** | `'/static/dist'` |
|--------------|-----------|
| **Type** | str |
| **Source** | app.config |

---

### `WORKFLOWS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |

**Set/Referenced by:**
- [`register_workflow`](#) in `workflows.py`
  > Register a submission/review workflow that records can go through.  A workflow defines the path a record takes from being created to being published - for example, who may create it, whether it needs ...
---

