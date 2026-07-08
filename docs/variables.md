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
| [`ACCESS_ACTION_CACHE_PREFIX`](#access_action_cache_prefix) | str | - |
| [`ACCESS_CACHE`](#access_cache) | NoneType | - |
| [`ACCESS_LOAD_SYSTEM_ROLE_NEEDS`](#access_load_system_role_needs) | bool | - |
| [`ACCOUNTS`](#accounts) | bool | - |
| [`ACCOUNTS_BASE_TEMPLATE`](#accounts_base_template) | str | - |
| [`ACCOUNTS_CONFIRM_EMAIL_ENDPOINT`](#accounts_confirm_email_endpoint) | NoneType | - |
| [`ACCOUNTS_COVER_TEMPLATE`](#accounts_cover_template) | str | - |
| [`ACCOUNTS_DEFAULT_EMAIL_VISIBILITY`](#accounts_default_email_visibility) | str | - |
| [`ACCOUNTS_DEFAULT_USERS_VERIFIED`](#accounts_default_users_verified) | bool | - |
| [`ACCOUNTS_DEFAULT_USER_VISIBILITY`](#accounts_default_user_visibility) | str | - |
| [`ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT`](#accounts_forgot_password_email_ratelimit) | NoneType | - |
| [`ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_KEY_PREFIX`](#accounts_forgot_password_email_ratelimit_key_prefix) | str | - |
| [`ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_MSG`](#accounts_forgot_password_email_ratelimit_msg) | LazyString | - |
| [`ACCOUNTS_JWT_ALOGORITHM`](#accounts_jwt_alogorithm) | str | - |
| [`ACCOUNTS_JWT_CREATION_FACTORY`](#accounts_jwt_creation_factory) | str | - |
| [`ACCOUNTS_JWT_DECODE_FACTORY`](#accounts_jwt_decode_factory) | str | - |
| [`ACCOUNTS_JWT_DOM_TOKEN`](#accounts_jwt_dom_token) | bool | - |
| [`ACCOUNTS_JWT_DOM_TOKEN_TEMPLATE`](#accounts_jwt_dom_token_template) | str | - |
| [`ACCOUNTS_JWT_ENABLE`](#accounts_jwt_enable) | bool | - |
| [`ACCOUNTS_JWT_EXPIRATION_DELTA`](#accounts_jwt_expiration_delta) | timedelta | - |
| [`ACCOUNTS_JWT_SECRET_KEY`](#accounts_jwt_secret_key) | str | - |
| [`ACCOUNTS_LOCAL_LOGIN_ENABLED`](#accounts_local_login_enabled) | bool | `configure_generic_parameters` |
| [`ACCOUNTS_LOGIN_RATELIMIT`](#accounts_login_ratelimit) | NoneType | - |
| [`ACCOUNTS_LOGIN_RATELIMIT_KEY_PREFIX`](#accounts_login_ratelimit_key_prefix) | str | - |
| [`ACCOUNTS_LOGIN_RATELIMIT_MSG`](#accounts_login_ratelimit_msg) | LazyString | - |
| [`ACCOUNTS_LOGIN_VIEW_FUNCTION`](#accounts_login_view_function) | unknown | `configure_generic_parameters` |
| [`ACCOUNTS_REGISTER_BLUEPRINT`](#accounts_register_blueprint) | NoneType | - |
| [`ACCOUNTS_RESET_PASSWORD_ENDPOINT`](#accounts_reset_password_endpoint) | NoneType | - |
| [`ACCOUNTS_REST_AUTH_VIEWS`](#accounts_rest_auth_views) | dict | - |
| [`ACCOUNTS_REST_CONFIRM_EMAIL_ENDPOINT`](#accounts_rest_confirm_email_endpoint) | str | - |
| [`ACCOUNTS_REST_RESET_PASSWORD_ENDPOINT`](#accounts_rest_reset_password_endpoint) | str | - |
| [`ACCOUNTS_RETENTION_PERIOD`](#accounts_retention_period) | timedelta | - |
| [`ACCOUNTS_SEND_CONFIRMATION_RATELIMIT`](#accounts_send_confirmation_ratelimit) | NoneType | - |
| [`ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_KEY_PREFIX`](#accounts_send_confirmation_ratelimit_key_prefix) | str | - |
| [`ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_MSG`](#accounts_send_confirmation_ratelimit_msg) | LazyString | - |
| [`ACCOUNTS_SESSION_ACTIVITY_ENABLED`](#accounts_session_activity_enabled) | bool | - |
| [`ACCOUNTS_SESSION_REDIS_URL`](#accounts_session_redis_url) | NoneType | `configure_generic_parameters` |
| [`ACCOUNTS_SESSION_STORE_FACTORY`](#accounts_session_store_factory) | str | - |
| [`ACCOUNTS_SETTINGS_SECURITY_TEMPLATE`](#accounts_settings_security_template) | str | - |
| [`ACCOUNTS_SETTINGS_TEMPLATE`](#accounts_settings_template) | str | - |
| [`ACCOUNTS_SITENAME`](#accounts_sitename) | LazyString | - |
| [`ACCOUNTS_USERINFO_HEADERS`](#accounts_userinfo_headers) | bool | - |
| [`ACCOUNTS_USERNAME_REGEX`](#accounts_username_regex) | str | - |
| [`ACCOUNTS_USERNAME_RULES_TEXT`](#accounts_username_rules_text) | LazyString | - |
| [`ACCOUNTS_USER_PREFERENCES_SCHEMA`](#accounts_user_preferences_schema) | UserPreferencesSchema | - |
| [`ACCOUNTS_USER_PROFILE_SCHEMA`](#accounts_user_profile_schema) | UserProfileSchema | - |
| [`ACCOUNTS_USE_CELERY`](#accounts_use_celery) | bool | - |
| [`ADMINISTRATION_APPNAME`](#administration_appname) | str | - |
| [`ADMINISTRATION_BASE_TEMPLATE`](#administration_base_template) | str | - |
| [`ADMINISTRATION_DASHBOARD_VIEW`](#administration_dashboard_view) | str | - |
| [`ADMINISTRATION_DISPLAY_VERSIONS`](#administration_display_versions) | list | - |
| [`ADMINISTRATION_THEME_BASE_TEMPLATE`](#administration_theme_base_template) | str | `configure_ui` |
| [`ADMIN_BASE_TEMPLATE`](#admin_base_template) | str | - |
| [`ALEMBIC`](#alembic) | dict | - |
| [`ALEMBIC_CONTEXT`](#alembic_context) | dict | - |
| [`ALLOWED_HTML_ATTRS`](#allowed_html_attrs) | dict | - |
| [`ALLOWED_HTML_TAGS`](#allowed_html_tags) | list | - |
| [`APPLICATION_ROOT`](#application_root) | str | - |
| [`APP_ALLOWED_HOSTS`](#app_allowed_hosts) | configured by function | `configure_generic_parameters` |
| [`APP_DEFAULT_SECURE_HEADERS`](#app_default_secure_headers) | dict | `configure_ui`, `configure_generic_parameters` |
| [`APP_ENABLE_SECURE_HEADERS`](#app_enable_secure_headers) | bool | - |
| [`APP_HEALTH_BLUEPRINT_ENABLED`](#app_health_blueprint_enabled) | bool | - |
| [`APP_LOGS_PERMISSION_POLICY`](#app_logs_permission_policy) | unknown | `configure_jobs` |
| [`APP_RDM_ADMIN_EMAIL_RECIPIENT`](#app_rdm_admin_email_recipient) | unknown | - |
| [`APP_RDM_DEPOSIT_FORM_AUTOCOMPLETE_NAMES`](#app_rdm_deposit_form_autocomplete_names) | unknown | - |
| [`APP_RDM_DEPOSIT_FORM_CUSTOM_FIELD_DEFAULTS`](#app_rdm_deposit_form_custom_field_defaults) | unknown | - |
| [`APP_RDM_DEPOSIT_FORM_DEFAULTS`](#app_rdm_deposit_form_defaults) | unknown | - |
| [`APP_RDM_DEPOSIT_FORM_PUBLISH_MODAL_EXTRA`](#app_rdm_deposit_form_publish_modal_extra) | unknown | - |
| [`APP_RDM_DEPOSIT_FORM_QUOTA`](#app_rdm_deposit_form_quota) | unknown | `configure_generic_parameters` |
| [`APP_RDM_DEPOSIT_FORM_TEMPLATE`](#app_rdm_deposit_form_template) | unknown | - |
| [`APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED`](#app_rdm_deposit_ng_files_ui_enabled) | unknown | `configure_ui` |
| [`APP_RDM_DETAIL_SIDE_BAR_TEMPLATES`](#app_rdm_detail_side_bar_templates) | unknown | `configure_ui` |
| [`APP_RDM_DISPLAY_DECIMAL_FILE_SIZES`](#app_rdm_display_decimal_file_sizes) | unknown | - |
| [`APP_RDM_FILES_INTEGRITY_REPORT_SUBJECT`](#app_rdm_files_integrity_report_subject) | unknown | - |
| [`APP_RDM_FILES_INTEGRITY_REPORT_TEMPLATE`](#app_rdm_files_integrity_report_template) | unknown | - |
| [`APP_RDM_IDENTIFIER_SCHEMES_UI`](#app_rdm_identifier_schemes_ui) | unknown | `configure_generic_parameters` |
| [`APP_RDM_MODERATION_REQUEST_FACETS`](#app_rdm_moderation_request_facets) | dict | - |
| [`APP_RDM_MODERATION_REQUEST_SEARCH`](#app_rdm_moderation_request_search) | dict | - |
| [`APP_RDM_MODERATION_REQUEST_SORT_OPTIONS`](#app_rdm_moderation_request_sort_options) | dict | - |
| [`APP_RDM_PAGES`](#app_rdm_pages) | unknown | - |
| [`APP_RDM_RECORDS_EXPORT_URL`](#app_rdm_records_export_url) | unknown | - |
| [`APP_RDM_RECORD_EXPORTERS`](#app_rdm_record_exporters) | unknown | - |
| [`APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS`](#app_rdm_record_landing_page_external_links) | list | - |
| [`APP_RDM_RECORD_LANDING_PAGE_FAIR_SIGNPOSTING_LEVEL_1_ENABLED`](#app_rdm_record_landing_page_fair_signposting_level_1_enabled) | unknown | - |
| [`APP_RDM_RECORD_LANDING_PAGE_TEMPLATE`](#app_rdm_record_landing_page_template) | unknown | - |
| [`APP_RDM_RECORD_THUMBNAIL_SIZES`](#app_rdm_record_thumbnail_sizes) | unknown | - |
| [`APP_RDM_ROUTES`](#app_rdm_routes) | dict | - |
| [`APP_RDM_SUBCOMMUNITIES_LABEL`](#app_rdm_subcommunities_label) | unknown | - |
| [`APP_RDM_USER_DASHBOARD_ROUTES`](#app_rdm_user_dashboard_routes) | dict | - |
| [`APP_REQUESTID_HEADER`](#app_requestid_header) | str | - |
| [`APP_THEME`](#app_theme) | NoneType | `configure_ui` |
| [`ASSETS_BUILDER`](#assets_builder) | configured by function | `configure_ui` |
| [`AUDIT_LOGS_DISABLED_ACTIONS`](#audit_logs_disabled_actions) | set | - |
| [`AUDIT_LOGS_ENABLED`](#audit_logs_enabled) | bool | - |
| [`AUDIT_LOGS_FACETS`](#audit_logs_facets) | dict | - |
| [`AUDIT_LOGS_SEARCH`](#audit_logs_search) | dict | - |
| [`AUDIT_LOGS_SORT_OPTIONS`](#audit_logs_sort_options) | dict | - |
| [`BABEL_DEFAULT_LOCALE`](#babel_default_locale) | str | `configure_generic_parameters` |
| [`BABEL_DEFAULT_TIMEZONE`](#babel_default_timezone) | unknown | `configure_generic_parameters` |
| [`BANNERS_CATEGORIES`](#banners_categories) | list | - |
| [`BANNERS_CATEGORIES_TO_STYLE`](#banners_categories_to_style) | unknown | - |
| [`BANNERS_SEARCH`](#banners_search) | dict | - |
| [`BANNERS_SORT_OPTIONS`](#banners_sort_options) | dict | - |
| [`BASE_TEMPLATE`](#base_template) | str | `configure_ui` |
| [`BROKER_URL`](#broker_url) | str | `configure_generic_parameters` |
| [`CACHE_IS_AUTHENTICATED_CALLBACK`](#cache_is_authenticated_callback) | NoneType | - |
| [`CACHE_KEY_PREFIX`](#cache_key_prefix) | str | - |
| [`CACHE_REDIS_URL`](#cache_redis_url) | str | `configure_generic_parameters` |
| [`CACHE_TYPE`](#cache_type) | str | - |
| [`CELERY_ACCEPT_CONTENT`](#celery_accept_content) | list | - |
| [`CELERY_ALWAYS_EAGER`](#celery_always_eager) | bool | - |
| [`CELERY_BEAT_SCHEDULE`](#celery_beat_schedule) | unknown | `configure_cron` |
| [`CELERY_BROKER_URL`](#celery_broker_url) | str | `configure_generic_parameters` |
| [`CELERY_RESULT_BACKEND`](#celery_result_backend) | str | `configure_generic_parameters` |
| [`CELERY_RESULT_SERIALIZER`](#celery_result_serializer) | str | - |
| [`CELERY_TASK_SERIALIZER`](#celery_task_serializer) | str | - |
| [`CELERY_WORKER_CONCURRENCY`](#celery_worker_concurrency) | int | - |
| [`CELERY_WORKER_POOL`](#celery_worker_pool) | str | - |
| [`CHECKS_ENABLED`](#checks_enabled) | bool | - |
| [`COLLECTIONS_MAX_COLLECTIONS_PER_TREE`](#collections_max_collections_per_tree) | int | - |
| [`COLLECTIONS_MAX_DEPTH`](#collections_max_depth) | int | - |
| [`COLLECTIONS_MAX_TREES`](#collections_max_trees) | int | - |
| [`COLLECTIONS_PERMISSION_POLICY`](#collections_permission_policy) | unknown | - |
| [`COLLECT_STATIC_ROOT`](#collect_static_root) | str | - |
| [`COLLECT_STORAGE`](#collect_storage) | str | `configure_generic_parameters` |
| [`COMMUNITIES_ALLOW_MEMBERSHIP_REQUESTS`](#communities_allow_membership_requests) | bool | - |
| [`COMMUNITIES_ALLOW_RESTRICTED`](#communities_allow_restricted) | bool | - |
| [`COMMUNITIES_ALWAYS_SHOW_CREATE_LINK`](#communities_always_show_create_link) | bool | - |
| [`COMMUNITIES_COLLECTIONS_ENABLED`](#communities_collections_enabled) | bool | - |
| [`COMMUNITIES_CUSTOM_FIELDS`](#communities_custom_fields) | list | - |
| [`COMMUNITIES_CUSTOM_FIELDS_UI`](#communities_custom_fields_ui) | list | - |
| [`COMMUNITIES_DEFAULT_RECORD_SUBMISSION_POLICY`](#communities_default_record_submission_policy) | RecordSubmissionPolicyEnum | - |
| [`COMMUNITIES_ERROR_HANDLERS`](#communities_error_handlers) | unknown | - |
| [`COMMUNITIES_FACETS`](#communities_facets) | dict | - |
| [`COMMUNITIES_IDENTITIES_CACHE_HANDLER`](#communities_identities_cache_handler) | str | - |
| [`COMMUNITIES_IDENTITIES_CACHE_REDIS_URL`](#communities_identities_cache_redis_url) | str | `configure_generic_parameters` |
| [`COMMUNITIES_IDENTITIES_CACHE_TIME`](#communities_identities_cache_time) | int | - |
| [`COMMUNITIES_INVITATIONS_EXPIRES_IN`](#communities_invitations_expires_in) | timedelta | - |
| [`COMMUNITIES_INVITATIONS_SEARCH`](#communities_invitations_search) | dict | - |
| [`COMMUNITIES_INVITATIONS_SORT_OPTIONS`](#communities_invitations_sort_options) | dict | - |
| [`COMMUNITIES_LOGO_MAX_FILE_SIZE`](#communities_logo_max_file_size) | int | - |
| [`COMMUNITIES_MEMBERSHIP_REQUESTS_EXPIRES_IN`](#communities_membership_requests_expires_in) | timedelta | - |
| [`COMMUNITIES_MEMBERSHIP_REQUESTS_FACETS`](#communities_membership_requests_facets) | dict | - |
| [`COMMUNITIES_MEMBERSHIP_REQUESTS_SEARCH`](#communities_membership_requests_search) | dict | - |
| [`COMMUNITIES_MEMBERS_FACETS`](#communities_members_facets) | dict | - |
| [`COMMUNITIES_MEMBERS_SEARCH`](#communities_members_search) | dict | - |
| [`COMMUNITIES_MEMBERS_SORT_OPTIONS`](#communities_members_sort_options) | dict | - |
| [`COMMUNITIES_NAMESPACES`](#communities_namespaces) | dict | - |
| [`COMMUNITIES_OAI_SETS_PREFIX`](#communities_oai_sets_prefix) | str | - |
| [`COMMUNITIES_PERMISSION_POLICY`](#communities_permission_policy) | configured by function | `configure_communities` |
| [`COMMUNITIES_RECORDS_SEARCH`](#communities_records_search) | dict | - |
| [`COMMUNITIES_REGISTER_UI_BLUEPRINT`](#communities_register_ui_blueprint) | configured by function | `configure_communities` |
| [`COMMUNITIES_REQUESTS_SEARCH`](#communities_requests_search) | dict | - |
| [`COMMUNITIES_ROLES`](#communities_roles) | list | `configure_communities` |
| [`COMMUNITIES_ROUTES`](#communities_routes) | dict | - |
| [`COMMUNITIES_SEARCH`](#communities_search) | dict | - |
| [`COMMUNITIES_SEARCH_SORT_BY_VERIFIED`](#communities_search_sort_by_verified) | bool | - |
| [`COMMUNITIES_SERVICE_COMPONENTS`](#communities_service_components) | unknown | - |
| [`COMMUNITIES_SORT_OPTIONS`](#communities_sort_options) | dict | - |
| [`COMMUNITIES_SUBCOMMUNITIES_FACETS`](#communities_subcommunities_facets) | dict | - |
| [`COMMUNITIES_SUBCOMMUNITIES_SEARCH`](#communities_subcommunities_search) | dict | - |
| [`COMMUNITIES_SUB_INVITATION_REQUEST_CLS`](#communities_sub_invitation_request_cls) | unknown | - |
| [`COMMUNITIES_SUB_REQUEST_CLS`](#communities_sub_request_cls) | unknown | - |
| [`CORS_EXPOSE_HEADERS`](#cors_expose_headers) | unknown | - |
| [`CORS_RESOURCES`](#cors_resources) | unknown | - |
| [`CORS_SEND_WILDCARD`](#cors_send_wildcard) | unknown | - |
| [`COVER_TEMPLATE`](#cover_template) | str | `configure_ui` |
| [`CROSSREF_ADDITIONAL_PREFIXES`](#crossref_additional_prefixes) | list | - |
| [`CROSSREF_DEPOSITOR`](#crossref_depositor) | str | - |
| [`CROSSREF_EMAIL`](#crossref_email) | str | - |
| [`CROSSREF_ENABLED`](#crossref_enabled) | bool | - |
| [`CROSSREF_FORMAT`](#crossref_format) | str | - |
| [`CROSSREF_PASSWORD`](#crossref_password) | str | - |
| [`CROSSREF_PREFIX`](#crossref_prefix) | str | - |
| [`CROSSREF_REGISTRANT`](#crossref_registrant) | str | - |
| [`CROSSREF_TEST_MODE`](#crossref_test_mode) | bool | - |
| [`CROSSREF_USERNAME`](#crossref_username) | str | - |
| [`CSRF_ALLOWED_CHARS`](#csrf_allowed_chars) | str | - |
| [`CSRF_COOKIE_NAME`](#csrf_cookie_name) | str | - |
| [`CSRF_COOKIE_SAMESITE`](#csrf_cookie_samesite) | str | - |
| [`CSRF_FORCE_SECURE_REFERER`](#csrf_force_secure_referer) | bool | - |
| [`CSRF_HEADER`](#csrf_header) | str | - |
| [`CSRF_METHODS`](#csrf_methods) | list | - |
| [`CSRF_SECRET_SALT`](#csrf_secret_salt) | str | - |
| [`CSRF_TOKEN_EXPIRES_IN`](#csrf_token_expires_in) | int | - |
| [`CSRF_TOKEN_GRACE_PERIOD`](#csrf_token_grace_period) | int | - |
| [`CSRF_TOKEN_LENGTH`](#csrf_token_length) | int | - |
| [`DASHBOARD_RECORD_CREATE_URL`](#dashboard_record_create_url) | configured by function | `configure_ui`, `configure_generic_parameters` |
| [`DATACITE_ADDITIONAL_PREFIXES`](#datacite_additional_prefixes) | list | - |
| [`DATACITE_DATACENTER_SYMBOL`](#datacite_datacenter_symbol) | str | - |
| [`DATACITE_ENABLED`](#datacite_enabled) | bool | - |
| [`DATACITE_FORMAT`](#datacite_format) | str | - |
| [`DATACITE_PASSWORD`](#datacite_password) | str | - |
| [`DATACITE_PREFIX`](#datacite_prefix) | str | - |
| [`DATACITE_TEST_MODE`](#datacite_test_mode) | bool | `configure_generic_parameters` |
| [`DATACITE_USERNAME`](#datacite_username) | str | - |
| [`DB_VERSIONING`](#db_versioning) | bool | - |
| [`DB_VERSIONING_USER_MODEL`](#db_versioning_user_model) | unknown | - |
| [`DEBUG`](#debug) | bool | - |
| [`DEBUG_TB_INTERCEPT_REDIRECTS`](#debug_tb_intercept_redirects) | unknown | - |
| [`DEPLOYMENT_VERSION`](#deployment_version) | configured by function | `configure_ui` |
| [`EINFRA`](#einfra) | configured by function | `configure_einfra_oidc` |
| [`EINFRA_LOGIN_APP`](#einfra_login_app) | configured by function | `configure_einfra_oidc` |
| [`EXPLAIN_TEMPLATE_LOADING`](#explain_template_loading) | bool | - |
| [`FILES_REST_ALLOW_RANGE_REQUESTS`](#files_rest_allow_range_requests) | bool | - |
| [`FILES_REST_CHECKSUM_VERIFICATION_URI_PREFIXES`](#files_rest_checksum_verification_uri_prefixes) | unknown | - |
| [`FILES_REST_DEFAULT_MAX_FILE_SIZE`](#files_rest_default_max_file_size) | NoneType | - |
| [`FILES_REST_DEFAULT_QUOTA_SIZE`](#files_rest_default_quota_size) | NoneType | `configure_generic_parameters` |
| [`FILES_REST_DEFAULT_STORAGE_CLASS`](#files_rest_default_storage_class) | str | `configure_generic_parameters` |
| [`FILES_REST_FILE_TAGS_HEADER`](#files_rest_file_tags_header) | str | - |
| [`FILES_REST_FILE_URI_MAX_LEN`](#files_rest_file_uri_max_len) | int | - |
| [`FILES_REST_MIN_FILE_SIZE`](#files_rest_min_file_size) | int | - |
| [`FILES_REST_MULTIPART_CHUNKSIZE_MAX`](#files_rest_multipart_chunksize_max) | int | - |
| [`FILES_REST_MULTIPART_CHUNKSIZE_MIN`](#files_rest_multipart_chunksize_min) | int | - |
| [`FILES_REST_MULTIPART_EXPIRES`](#files_rest_multipart_expires) | timedelta | - |
| [`FILES_REST_MULTIPART_MAX_PARTS`](#files_rest_multipart_max_parts) | int | - |
| [`FILES_REST_MULTIPART_PART_FACTORIES`](#files_rest_multipart_part_factories) | list | - |
| [`FILES_REST_OBJECT_KEY_MAX_LEN`](#files_rest_object_key_max_len) | int | - |
| [`FILES_REST_PERMISSION_FACTORY`](#files_rest_permission_factory) | str | - |
| [`FILES_REST_SIZE_LIMITERS`](#files_rest_size_limiters) | str | - |
| [`FILES_REST_STORAGE_CLASS_LIST`](#files_rest_storage_class_list) | dict | `configure_generic_parameters` |
| [`FILES_REST_STORAGE_FACTORY`](#files_rest_storage_factory) | str | `configure_generic_parameters` |
| [`FILES_REST_STORAGE_PATH_DIMENSIONS`](#files_rest_storage_path_dimensions) | int | - |
| [`FILES_REST_STORAGE_PATH_SPLIT_LENGTH`](#files_rest_storage_path_split_length) | int | - |
| [`FILES_REST_TASK_WAIT_INTERVAL`](#files_rest_task_wait_interval) | int | - |
| [`FILES_REST_TASK_WAIT_MAX_SECONDS`](#files_rest_task_wait_max_seconds) | int | - |
| [`FILES_REST_UPLOAD_FACTORIES`](#files_rest_upload_factories) | list | - |
| [`FILES_REST_XSENDFILE_ENABLED`](#files_rest_xsendfile_enabled) | bool | - |
| [`FILES_REST_XSENDFILE_RESPONSE_FUNC`](#files_rest_xsendfile_response_func) | unknown | - |
| [`FORMATTER_BADGES_ALLOWED_TITLES`](#formatter_badges_allowed_titles) | list | - |
| [`FORMATTER_BADGES_ENABLE`](#formatter_badges_enable) | bool | - |
| [`FORMATTER_BADGES_MAX_CACHE_AGE`](#formatter_badges_max_cache_age) | int | - |
| [`FORMATTER_BADGES_TITLE_MAPPING`](#formatter_badges_title_mapping) | dict | - |
| [`GLOBAL_SEARCH_MODELS`](#global_search_models) | configured by function | `add_model` |
| [`HEADER_TEMPLATE`](#header_template) | unknown | `configure_ui` |
| [`I18N_DEFAULT_REDIRECT_ENDPOINT`](#i18n_default_redirect_endpoint) | NoneType | - |
| [`I18N_JS_DISTR_EXCEPTIONAL_PACKAGE_MAP`](#i18n_js_distr_exceptional_package_map) | dict | - |
| [`I18N_LANGUAGES`](#i18n_languages) | list | `configure_generic_parameters` |
| [`I18N_SESSION_KEY`](#i18n_session_key) | str | - |
| [`I18N_SET_LANGUAGE_URL`](#i18n_set_language_url) | str | - |
| [`I18N_TRANSIFEX_JS_RESOURCES_MAP`](#i18n_transifex_js_resources_map) | dict | - |
| [`I18N_TRANSLATIONS_PATHS`](#i18n_translations_paths) | list | - |
| [`I18N_USER_LANG_ATTR`](#i18n_user_lang_attr) | str | - |
| [`IIIF_API_DECORATOR_HANDLER`](#iiif_api_decorator_handler) | unknown | - |
| [`IIIF_API_INFO_RESPONSE_SKELETON`](#iiif_api_info_response_skeleton) | dict | - |
| [`IIIF_CACHE_HANDLER`](#iiif_cache_handler) | str | - |
| [`IIIF_CACHE_IGNORE_ERRORS`](#iiif_cache_ignore_errors) | bool | - |
| [`IIIF_CACHE_REDIS_URL`](#iiif_cache_redis_url) | str | - |
| [`IIIF_CACHE_TIME`](#iiif_cache_time) | int | - |
| [`IIIF_CONVERTERS`](#iiif_converters) | tuple | - |
| [`IIIF_FORMATS`](#iiif_formats) | dict | - |
| [`IIIF_FORMATS_PIL_MAP`](#iiif_formats_pil_map) | dict | - |
| [`IIIF_GIF_TEMP_FOLDER_PATH`](#iiif_gif_temp_folder_path) | str | - |
| [`IIIF_MODE`](#iiif_mode) | dict | - |
| [`IIIF_PREVIEW_TEMPLATE`](#iiif_preview_template) | str | - |
| [`IIIF_QUALITIES`](#iiif_qualities) | tuple | - |
| [`IIIF_SIMPLE_PREVIEWER_NATIVE_EXTENSIONS`](#iiif_simple_previewer_native_extensions) | list | - |
| [`IIIF_SIMPLE_PREVIEWER_SIZE`](#iiif_simple_previewer_size) | str | - |
| [`IIIF_TILES_CONVERTER_PARAMS`](#iiif_tiles_converter_params) | dict | - |
| [`IIIF_TILES_GENERATION_ENABLED`](#iiif_tiles_generation_enabled) | bool | - |
| [`IIIF_TILES_STORAGE_BASE_PATH`](#iiif_tiles_storage_base_path) | str | - |
| [`IIIF_TILES_VALID_EXTENSIONS`](#iiif_tiles_valid_extensions) | list | - |
| [`IIIF_VALIDATIONS`](#iiif_validations) | dict | - |
| [`INDEXER_BEFORE_INDEX_HOOKS`](#indexer_before_index_hooks) | list | - |
| [`INDEXER_BULK_REQUEST_TIMEOUT`](#indexer_bulk_request_timeout) | int | - |
| [`INDEXER_DEFAULT_INDEX`](#indexer_default_index) | NoneType | - |
| [`INDEXER_MAX_BULK_CONSUMERS`](#indexer_max_bulk_consumers) | int | - |
| [`INDEXER_MQ_EXCHANGE`](#indexer_mq_exchange) | unknown | - |
| [`INDEXER_MQ_PUBLISH_KWARGS`](#indexer_mq_publish_kwargs) | dict | - |
| [`INDEXER_MQ_QUEUE`](#indexer_mq_queue) | unknown | - |
| [`INDEXER_MQ_ROUTING_KEY`](#indexer_mq_routing_key) | str | - |
| [`INDEXER_RECORD_TO_INDEX`](#indexer_record_to_index) | str | - |
| [`INDEXER_REPLACE_REFS`](#indexer_replace_refs) | bool | - |
| [`INSTANCE_THEME_FILE`](#instance_theme_file) | configured by function | `configure_ui` |
| [`INVENIO_CACHE_TYPE`](#invenio_cache_type) | configured by function | `configure_generic_parameters` |
| [`INVENIO_RDM_ENABLED`](#invenio_rdm_enabled) | bool | - |
| [`INVENIO_VOCABULARY_TYPE_METADATA`](#invenio_vocabulary_type_metadata) | configured by function | `configure_vocabulary` |
| [`JAVASCRIPT_PACKAGES_MANAGER`](#javascript_packages_manager) | configured by function | `configure_ui` |
| [`JOBS_DEFAULT_QUEUE`](#jobs_default_queue) | NoneType | - |
| [`JOBS_FACETS`](#jobs_facets) | dict | - |
| [`JOBS_LOGGING`](#jobs_logging) | bool | - |
| [`JOBS_LOGGING_INDEX`](#jobs_logging_index) | str | - |
| [`JOBS_LOGGING_LEVEL`](#jobs_logging_level) | str | `configure_jobs` |
| [`JOBS_LOGGING_RETENTION_DAYS`](#jobs_logging_retention_days) | int | - |
| [`JOBS_LOGS_BATCH_SIZE`](#jobs_logs_batch_size) | int | - |
| [`JOBS_LOGS_MAX_RESULTS`](#jobs_logs_max_results) | int | - |
| [`JOBS_PERMISSION_POLICY`](#jobs_permission_policy) | unknown | - |
| [`JOBS_QUEUES`](#jobs_queues) | dict | - |
| [`JOBS_RUNS_PERMISSION_POLICY`](#jobs_runs_permission_policy) | unknown | - |
| [`JOBS_SEARCH`](#jobs_search) | dict | - |
| [`JOBS_SORT_OPTIONS`](#jobs_sort_options) | dict | - |
| [`JOBS_TASKS_PERMISSION_POLICY`](#jobs_tasks_permission_policy) | unknown | - |
| [`JSONSCHEMAS_ENDPOINT`](#jsonschemas_endpoint) | str | - |
| [`JSONSCHEMAS_HOST`](#jsonschemas_host) | str | `configure_generic_parameters` |
| [`JSONSCHEMAS_LOADER_CLS`](#jsonschemas_loader_cls) | NoneType | - |
| [`JSONSCHEMAS_LOCAL_REFRESOLVER_URI_SCHEME`](#jsonschemas_local_refresolver_uri_scheme) | str | - |
| [`JSONSCHEMAS_REGISTER_ENDPOINTS_API`](#jsonschemas_register_endpoints_api) | bool | - |
| [`JSONSCHEMAS_REGISTER_ENDPOINTS_UI`](#jsonschemas_register_endpoints_ui) | bool | - |
| [`JSONSCHEMAS_REPLACE_REFS`](#jsonschemas_replace_refs) | bool | - |
| [`JSONSCHEMAS_RESOLVER_CLS`](#jsonschemas_resolver_cls) | str | - |
| [`JSONSCHEMAS_RESOLVE_SCHEMA`](#jsonschemas_resolve_schema) | bool | - |
| [`JSONSCHEMAS_SCHEMAS`](#jsonschemas_schemas) | NoneType | - |
| [`JSONSCHEMAS_URL_SCHEME`](#jsonschemas_url_scheme) | str | - |
| [`LOGGING_CONSOLE`](#logging_console) | bool | - |
| [`LOGGING_CONSOLE_LEVEL`](#logging_console_level) | NoneType | - |
| [`LOGGING_CONSOLE_PYWARNINGS`](#logging_console_pywarnings) | bool | - |
| [`LOGGING_FS_BACKUPCOUNT`](#logging_fs_backupcount) | int | - |
| [`LOGGING_FS_LEVEL`](#logging_fs_level) | str | - |
| [`LOGGING_FS_LOGFILE`](#logging_fs_logfile) | NoneType | - |
| [`LOGGING_FS_MAXBYTES`](#logging_fs_maxbytes) | int | - |
| [`LOGGING_FS_PYWARNINGS`](#logging_fs_pywarnings) | bool | - |
| [`LOGGING_SENTRY_CELERY`](#logging_sentry_celery) | bool | - |
| [`LOGGING_SENTRY_CLASS`](#logging_sentry_class) | NoneType | - |
| [`LOGGING_SENTRY_INIT_KWARGS`](#logging_sentry_init_kwargs) | NoneType | - |
| [`LOGGING_SENTRY_LEVEL`](#logging_sentry_level) | str | - |
| [`LOGGING_SENTRY_PYWARNINGS`](#logging_sentry_pywarnings) | bool | - |
| [`LOGGING_SENTRY_REDIS`](#logging_sentry_redis) | bool | - |
| [`LOGGING_SENTRY_SQLALCHEMY`](#logging_sentry_sqlalchemy) | bool | - |
| [`MAIL_DEBUG`](#mail_debug) | bool | - |
| [`MAIL_DEFAULT_REPLY_TO`](#mail_default_reply_to) | NoneType | - |
| [`MAIL_DEFAULT_SENDER`](#mail_default_sender) | unknown | `configure_generic_parameters` |
| [`MAIL_MAX_ATTACHMENT_SIZE`](#mail_max_attachment_size) | int | - |
| [`MAIL_MAX_RETRIES`](#mail_max_retries) | int | - |
| [`MAIL_MIN_LOGGING_LEVEL`](#mail_min_logging_level) | int | - |
| [`MAIL_SUPPRESS_SEND`](#mail_suppress_send) | bool | `configure_generic_parameters` |
| [`MATOMO_ANALYTICS_SITE_ID`](#matomo_analytics_site_id) | configured by function | `configure_ui` |
| [`MATOMO_ANALYTICS_TEMPLATE`](#matomo_analytics_template) | configured by function | `configure_ui` |
| [`MATOMO_ANALYTICS_URL`](#matomo_analytics_url) | configured by function | `configure_ui` |
| [`MAX_CONTENT_LENGTH`](#max_content_length) | NoneType | - |
| [`MAX_COOKIE_SIZE`](#max_cookie_size) | int | - |
| [`MAX_FORM_MEMORY_SIZE`](#max_form_memory_size) | int | - |
| [`MAX_FORM_PARTS`](#max_form_parts) | int | - |
| [`MULTIPROFILER_BASE_TEMPLATE`](#multiprofiler_base_template) | unknown | - |
| [`MULTIPROFILER_IGNORED_ENDPOINTS`](#multiprofiler_ignored_endpoints) | unknown | - |
| [`MULTIPROFILER_PERMISSION`](#multiprofiler_permission) | unknown | - |
| [`NOTIFICATIONS_BACKENDS`](#notifications_backends) | dict | - |
| [`NOTIFICATIONS_BUILDERS`](#notifications_builders) | dict | - |
| [`NOTIFICATIONS_ENTITY_RESOLVERS`](#notifications_entity_resolvers) | list | - |
| [`NOTIFICATIONS_GROUP_EMAIL_DOMAIN`](#notifications_group_email_domain) | NoneType | - |
| [`NOTIFICATIONS_SETTINGS_VIEW_FUNCTION`](#notifications_settings_view_function) | NoneType | - |
| [`OAISERVER_ADMIN_EMAILS`](#oaiserver_admin_emails) | list | - |
| [`OAISERVER_BASE_TEMPLATE`](#oaiserver_base_template) | str | - |
| [`OAISERVER_CACHE_KEY`](#oaiserver_cache_key) | str | - |
| [`OAISERVER_CELERY_TASK_CHUNK_SIZE`](#oaiserver_celery_task_chunk_size) | int | - |
| [`OAISERVER_COMPRESSIONS`](#oaiserver_compressions) | list | - |
| [`OAISERVER_CONTROL_NUMBER_FETCHER`](#oaiserver_control_number_fetcher) | str | - |
| [`OAISERVER_CREATED_KEY`](#oaiserver_created_key) | str | - |
| [`OAISERVER_DELETE_PERCOLATOR_FUNCTION`](#oaiserver_delete_percolator_function) | str | - |
| [`OAISERVER_DESCRIPTIONS`](#oaiserver_descriptions) | list | - |
| [`OAISERVER_GETRECORD_FETCHER`](#oaiserver_getrecord_fetcher) | str | - |
| [`OAISERVER_GRANULARITY`](#oaiserver_granularity) | str | - |
| [`OAISERVER_ID_FETCHER`](#oaiserver_id_fetcher) | str | - |
| [`OAISERVER_ID_PREFIX`](#oaiserver_id_prefix) | str | `configure_generic_parameters` |
| [`OAISERVER_LAST_UPDATE_KEY`](#oaiserver_last_update_key) | str | - |
| [`OAISERVER_METADATA_FORMATS`](#oaiserver_metadata_formats) | dict | - |
| [`OAISERVER_NEW_PERCOLATOR_FUNCTION`](#oaiserver_new_percolator_function) | str | - |
| [`OAISERVER_PAGE_SIZE`](#oaiserver_page_size) | int | - |
| [`OAISERVER_PERCOLATOR_DEDICATED_INDEX`](#oaiserver_percolator_dedicated_index) | bool | - |
| [`OAISERVER_PROTOCOL_VERSION`](#oaiserver_protocol_version) | str | - |
| [`OAISERVER_QUERY_PARSER`](#oaiserver_query_parser) | unknown | - |
| [`OAISERVER_QUERY_PARSER_FIELDS`](#oaiserver_query_parser_fields) | list | - |
| [`OAISERVER_RECORD_CLS`](#oaiserver_record_cls) | str | - |
| [`OAISERVER_RECORD_INDEX`](#oaiserver_record_index) | str | - |
| [`OAISERVER_RECORD_LIST_SETS_FETCHER`](#oaiserver_record_list_sets_fetcher) | str | - |
| [`OAISERVER_RECORD_SETS_FETCHER`](#oaiserver_record_sets_fetcher) | str | - |
| [`OAISERVER_REGISTER_RECORD_SIGNALS`](#oaiserver_register_record_signals) | bool | - |
| [`OAISERVER_REGISTER_SET_SIGNALS`](#oaiserver_register_set_signals) | bool | - |
| [`OAISERVER_REPOSITORY_NAME`](#oaiserver_repository_name) | str | `configure_oai` |
| [`OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME`](#oaiserver_resumption_token_expire_time) | int | - |
| [`OAISERVER_SEARCH_CLS`](#oaiserver_search_cls) | str | - |
| [`OAISERVER_SET_RECORDS_QUERY_FETCHER`](#oaiserver_set_records_query_fetcher) | str | - |
| [`OAISERVER_XSL_URL`](#oaiserver_xsl_url) | NoneType | - |
| [`OAUTH2SERVER_ALLOWED_GRANT_TYPES`](#oauth2server_allowed_grant_types) | set | - |
| [`OAUTH2SERVER_ALLOWED_RESPONSE_TYPES`](#oauth2server_allowed_response_types) | set | - |
| [`OAUTH2SERVER_ALLOWED_URLENCODE_CHARACTERS`](#oauth2server_allowed_urlencode_characters) | str | - |
| [`OAUTH2SERVER_BASE_TEMPLATE`](#oauth2server_base_template) | str | - |
| [`OAUTH2SERVER_CLIENT_ID_SALT_LEN`](#oauth2server_client_id_salt_len) | int | - |
| [`OAUTH2SERVER_CLIENT_SECRET_SALT_LEN`](#oauth2server_client_secret_salt_len) | int | - |
| [`OAUTH2SERVER_COVER_TEMPLATE`](#oauth2server_cover_template) | str | - |
| [`OAUTH2SERVER_JWT_AUTH_HEADER`](#oauth2server_jwt_auth_header) | str | - |
| [`OAUTH2SERVER_JWT_AUTH_HEADER_TYPE`](#oauth2server_jwt_auth_header_type) | str | - |
| [`OAUTH2SERVER_JWT_VERIFICATION_FACTORY`](#oauth2server_jwt_verification_factory) | str | - |
| [`OAUTH2SERVER_SETTINGS_TEMPLATE`](#oauth2server_settings_template) | str | - |
| [`OAUTH2SERVER_TOKEN_PERSONAL_SALT_LEN`](#oauth2server_token_personal_salt_len) | int | - |
| [`OAUTH2_CACHE_TYPE`](#oauth2_cache_type) | str | - |
| [`OAUTH2_PROVIDER_ERROR_ENDPOINT`](#oauth2_provider_error_endpoint) | str | - |
| [`OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN`](#oauthclient_auto_redirect_to_external_login) | bool | `configure_generic_parameters` |
| [`OAUTHCLIENT_BASE_TEMPLATE`](#oauthclient_base_template) | str | - |
| [`OAUTHCLIENT_COVER_TEMPLATE`](#oauthclient_cover_template) | str | - |
| [`OAUTHCLIENT_LOGIN_USER_TEMPLATE_PARENT`](#oauthclient_login_user_template_parent) | str | - |
| [`OAUTHCLIENT_REMOTE_APPS`](#oauthclient_remote_apps) | dict | `configure_generic_parameters`, `configure_einfra_oidc` |
| [`OAUTHCLIENT_REST_DEFAULT_ERROR_REDIRECT_URL`](#oauthclient_rest_default_error_redirect_url) | str | - |
| [`OAUTHCLIENT_REST_DEFAULT_RESPONSE_HANDLER`](#oauthclient_rest_default_response_handler) | NoneType | - |
| [`OAUTHCLIENT_REST_REMOTE_APPS`](#oauthclient_rest_remote_apps) | dict | - |
| [`OAUTHCLIENT_SESSION_KEY_PREFIX`](#oauthclient_session_key_prefix) | str | - |
| [`OAUTHCLIENT_SETTINGS_TEMPLATE`](#oauthclient_settings_template) | str | - |
| [`OAUTHCLIENT_SIGNUP_FORM`](#oauthclient_signup_form) | unknown | - |
| [`OAUTHCLIENT_SIGNUP_TEMPLATE`](#oauthclient_signup_template) | str | - |
| [`OAUTHCLIENT_SITENAME`](#oauthclient_sitename) | LazyString | - |
| [`OAUTHCLIENT_STATE_ENABLED`](#oauthclient_state_enabled) | bool | - |
| [`OAUTHCLIENT_STATE_EXPIRES`](#oauthclient_state_expires) | int | - |
| [`OAUTHCLIENT_TOKEN_EXPIRES_LEEWAY`](#oauthclient_token_expires_leeway) | int | - |
| [`PAGES_ALLOWED_EXTRA_HTML_ATTRS`](#pages_allowed_extra_html_attrs) | dict | - |
| [`PAGES_ALLOWED_EXTRA_HTML_TAGS`](#pages_allowed_extra_html_tags) | list | - |
| [`PAGES_BASE_TEMPLATE`](#pages_base_template) | str | - |
| [`PAGES_DEFAULT_TEMPLATE`](#pages_default_template) | str | - |
| [`PAGES_FACETS`](#pages_facets) | dict | - |
| [`PAGES_SEARCH`](#pages_search) | dict | - |
| [`PAGES_SORT_OPTIONS`](#pages_sort_options) | dict | - |
| [`PAGES_TEMPLATES`](#pages_templates) | list | - |
| [`PAGES_WHITELIST_CONFIG_KEYS`](#pages_whitelist_config_keys) | list | - |
| [`PERMANENT_SESSION_LIFETIME`](#permanent_session_lifetime) | timedelta | - |
| [`PIDSTORE_APP_LOGGER_HANDLERS`](#pidstore_app_logger_handlers) | bool | - |
| [`PIDSTORE_DATACITE_DOI_PREFIX`](#pidstore_datacite_doi_prefix) | str | - |
| [`PIDSTORE_OBJECT_ENDPOINTS`](#pidstore_object_endpoints) | dict | - |
| [`PIDSTORE_RECID_FIELD`](#pidstore_recid_field) | str | - |
| [`PIDSTORE_RECORDID_OPTIONS`](#pidstore_recordid_options) | dict | - |
| [`PREFERRED_URL_SCHEME`](#preferred_url_scheme) | str | - |
| [`PREVIEWABLE_ZIP_PREVIEWER_NATIVE_EXTENSIONS`](#previewable_zip_previewer_native_extensions) | list | - |
| [`PREVIEWER_ABSTRACT_TEMPLATE`](#previewer_abstract_template) | str | - |
| [`PREVIEWER_BASE_CSS_BUNDLES`](#previewer_base_css_bundles) | list | - |
| [`PREVIEWER_BASE_JS_BUNDLES`](#previewer_base_js_bundles) | list | - |
| [`PREVIEWER_BASE_TEMPLATE`](#previewer_base_template) | str | - |
| [`PREVIEWER_CHARDET_BYTES`](#previewer_chardet_bytes) | int | - |
| [`PREVIEWER_CHARDET_CONFIDENCE`](#previewer_chardet_confidence) | float | - |
| [`PREVIEWER_CONTAINER_ITEM_PREFERENCE`](#previewer_container_item_preference) | list | - |
| [`PREVIEWER_CSV_MAX_BYTES`](#previewer_csv_max_bytes) | int | - |
| [`PREVIEWER_CSV_SNIFFER_ALLOWED_DELIMITERS`](#previewer_csv_sniffer_allowed_delimiters) | NoneType | - |
| [`PREVIEWER_CSV_VALIDATION_BYTES`](#previewer_csv_validation_bytes) | int | - |
| [`PREVIEWER_MAX_FILE_SIZE_BYTES`](#previewer_max_file_size_bytes) | int | - |
| [`PREVIEWER_MAX_IMAGE_SIZE_BYTES`](#previewer_max_image_size_bytes) | float | - |
| [`PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS`](#previewer_pdf_js_document_init_params) | NoneType | - |
| [`PREVIEWER_PDF_JS_ENABLE_SCRIPTING`](#previewer_pdf_js_enable_scripting) | bool | - |
| [`PREVIEWER_PREFERENCE`](#previewer_preference) | list | - |
| [`PREVIEWER_RECORD_FILE_FACOTRY`](#previewer_record_file_facotry) | NoneType | - |
| [`PREVIEWER_TXT_MAX_BYTES`](#previewer_txt_max_bytes) | int | - |
| [`PREVIEWER_WEB_ARCHIVE_RANGE_REQUESTS`](#previewer_web_archive_range_requests) | bool | - |
| [`PREVIEWER_ZIP_MAX_FILES`](#previewer_zip_max_files) | int | - |
| [`PROPAGATE_EXCEPTIONS`](#propagate_exceptions) | NoneType | - |
| [`PROVIDE_AUTOMATIC_OPTIONS`](#provide_automatic_options) | bool | - |
| [`QUEUES_BROKER_URL`](#queues_broker_url) | NoneType | - |
| [`QUEUES_CONNECTION_POOL`](#queues_connection_pool) | unknown | - |
| [`QUEUES_DEFINITIONS`](#queues_definitions) | list | - |
| [`RATELIMIT_APPLICATION`](#ratelimit_application) | unknown | - |
| [`RATELIMIT_AUTHENTICATED_USER`](#ratelimit_authenticated_user) | str | `configure_generic_parameters` |
| [`RATELIMIT_ENABLED`](#ratelimit_enabled) | bool | - |
| [`RATELIMIT_GUEST_USER`](#ratelimit_guest_user) | str | `configure_generic_parameters` |
| [`RATELIMIT_HEADERS_ENABLED`](#ratelimit_headers_enabled) | bool | - |
| [`RATELIMIT_KEY_FUNC`](#ratelimit_key_func) | NoneType | - |
| [`RATELIMIT_PER_ENDPOINT`](#ratelimit_per_endpoint) | dict | - |
| [`RATELIMIT_STORAGE_URI`](#ratelimit_storage_uri) | str | - |
| [`RATELIMIT_STRATEGY`](#ratelimit_strategy) | str | - |
| [`RDM_ALLOW_EXTERNAL_DOI_VERSIONING`](#rdm_allow_external_doi_versioning) | bool | - |
| [`RDM_ALLOW_METADATA_ONLY_RECORDS`](#rdm_allow_metadata_only_records) | bool | - |
| [`RDM_ALLOW_OWNERS_REMOVE_COMMUNITY_FROM_RECORD`](#rdm_allow_owners_remove_community_from_record) | bool | - |
| [`RDM_ALLOW_RESTRICTED_RECORDS`](#rdm_allow_restricted_records) | bool | - |
| [`RDM_ARCHIVE_DOWNLOAD_ENABLED`](#rdm_archive_download_enabled) | bool | - |
| [`RDM_CITATION_STYLES`](#rdm_citation_styles) | list | - |
| [`RDM_CITATION_STYLES_DEFAULT`](#rdm_citation_styles_default) | str | - |
| [`RDM_COMMUNITIES_ROUTES`](#rdm_communities_routes) | dict | - |
| [`RDM_COMMUNITY_CONTENT_MODERATION_HANDLERS`](#rdm_community_content_moderation_handlers) | list | - |
| [`RDM_COMMUNITY_INCLUSION_REQUEST_CLS`](#rdm_community_inclusion_request_cls) | unknown | - |
| [`RDM_COMMUNITY_REQUIRED_TO_PUBLISH`](#rdm_community_required_to_publish) | bool | - |
| [`RDM_COMMUNITY_SUBMISSION_REQUEST_CLS`](#rdm_community_submission_request_cls) | unknown | - |
| [`RDM_CONTENT_MODERATION_HANDLERS`](#rdm_content_moderation_handlers) | list | - |
| [`RDM_CUSTOM_FIELDS`](#rdm_custom_fields) | list | - |
| [`RDM_CUSTOM_FIELDS_UI`](#rdm_custom_fields_ui) | list | - |
| [`RDM_DATACITE_DUMP_OPENAIRE_ACCESS_RIGHTS`](#rdm_datacite_dump_openaire_access_rights) | bool | - |
| [`RDM_DATACITE_FUNDER_IDENTIFIERS_PRIORITY`](#rdm_datacite_funder_identifiers_priority) | tuple | - |
| [`RDM_DEFAULT_FILES_ENABLED`](#rdm_default_files_enabled) | bool | - |
| [`RDM_DETAIL_SIDE_BAR_MANAGE_ATTRIBUTES_EXTENSION_TEMPLATE`](#rdm_detail_side_bar_manage_attributes_extension_template) | unknown | - |
| [`RDM_FACETS`](#rdm_facets) | dict | - |
| [`RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE`](#rdm_files_default_max_additional_quota_size) | int | - |
| [`RDM_FILES_DEFAULT_MAX_FILE_SIZE`](#rdm_files_default_max_file_size) | int | - |
| [`RDM_FILES_DEFAULT_QUOTA_SIZE`](#rdm_files_default_quota_size) | int | - |
| [`RDM_FILE_MODIFICATION_PERIOD`](#rdm_file_modification_period) | timedelta | - |
| [`RDM_FILE_MODIFICATION_POLICY`](#rdm_file_modification_policy) | unknown | - |
| [`RDM_IIIF_MANIFEST_FORMATS`](#rdm_iiif_manifest_formats) | list | - |
| [`RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED`](#rdm_immediate_file_modification_enabled) | bool | - |
| [`RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES`](#rdm_immediate_file_modification_policies) | list | - |
| [`RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED`](#rdm_immediate_quota_increase_enabled) | bool | - |
| [`RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES`](#rdm_immediate_quota_increase_policies) | list | - |
| [`RDM_IMMEDIATE_RECORD_DELETION_CHECKLIST`](#rdm_immediate_record_deletion_checklist) | list | - |
| [`RDM_IMMEDIATE_RECORD_DELETION_ENABLED`](#rdm_immediate_record_deletion_enabled) | bool | - |
| [`RDM_IMMEDIATE_RECORD_DELETION_POLICIES`](#rdm_immediate_record_deletion_policies) | list | - |
| [`RDM_LOCK_EDIT_PUBLISHED_FILES`](#rdm_lock_edit_published_files) | unknown | - |
| [`RDM_MEDIA_FILES_DEFAULT_MAX_FILE_SIZE`](#rdm_media_files_default_max_file_size) | int | - |
| [`RDM_MEDIA_FILES_DEFAULT_QUOTA_SIZE`](#rdm_media_files_default_quota_size) | int | - |
| [`RDM_NAMESPACES`](#rdm_namespaces) | dict | - |
| [`RDM_NEW_RECORD_VERSION_REVIEW_POLICY`](#rdm_new_record_version_review_policy) | unknown | - |
| [`RDM_OAI_PMH_FACETS`](#rdm_oai_pmh_facets) | dict | - |
| [`RDM_OAI_PMH_SEARCH`](#rdm_oai_pmh_search) | dict | - |
| [`RDM_OAI_PMH_SORT_OPTIONS`](#rdm_oai_pmh_sort_options) | dict | - |
| [`RDM_OPTIONAL_DOI_VALIDATOR`](#rdm_optional_doi_validator) | unknown | - |
| [`RDM_PARENT_PERSISTENT_IDENTIFIERS`](#rdm_parent_persistent_identifiers) | dict | - |
| [`RDM_PARENT_PERSISTENT_IDENTIFIER_PROVIDERS`](#rdm_parent_persistent_identifier_providers) | list | - |
| [`RDM_PERMISSION_POLICY`](#rdm_permission_policy) | unknown | - |
| [`RDM_PERSISTENT_IDENTIFIERS`](#rdm_persistent_identifiers) | dict | - |
| [`RDM_PERSISTENT_IDENTIFIER_PROVIDERS`](#rdm_persistent_identifier_providers) | list | - |
| [`RDM_QUOTA_INCREASE_POLICY`](#rdm_quota_increase_policy) | unknown | - |
| [`RDM_RECORDS_ALLOW_RESTRICTION_AFTER_GRACE_PERIOD`](#rdm_records_allow_restriction_after_grace_period) | bool | - |
| [`RDM_RECORDS_CONTAINER_EXTENSIONS`](#rdm_records_container_extensions) | list | - |
| [`RDM_RECORDS_IDENTIFIERS_SCHEMES`](#rdm_records_identifiers_schemes) | dict | - |
| [`RDM_RECORDS_LOCATION_SCHEMES`](#rdm_records_location_schemes) | dict | - |
| [`RDM_RECORDS_MAX_FILES_COUNT`](#rdm_records_max_files_count) | int | - |
| [`RDM_RECORDS_MAX_MEDIA_FILES_COUNT`](#rdm_records_max_media_files_count) | int | - |
| [`RDM_RECORDS_PERSONORG_SCHEMES`](#rdm_records_personorg_schemes) | dict | - |
| [`RDM_RECORDS_RELATED_IDENTIFIERS_SCHEMES`](#rdm_records_related_identifiers_schemes) | dict | - |
| [`RDM_RECORDS_REQUIRE_SECRET_LINKS_EXPIRATION`](#rdm_records_require_secret_links_expiration) | bool | - |
| [`RDM_RECORDS_RESTRICTION_GRACE_PERIOD`](#rdm_records_restriction_grace_period) | timedelta | - |
| [`RDM_RECORDS_REVIEWS`](#rdm_records_reviews) | list | - |
| [`RDM_RECORDS_UI_EDIT_URL`](#rdm_records_ui_edit_url) | str | - |
| [`RDM_RECORDS_USER_FIXTURE_PASSWORDS`](#rdm_records_user_fixture_passwords) | dict | - |
| [`RDM_RECORD_DELETION_POLICY`](#rdm_record_deletion_policy) | unknown | - |
| [`RDM_RECORD_FILE_EXTRACTORS`](#rdm_record_file_extractors) | list | - |
| [`RDM_REQUESTS_ROUTES`](#rdm_requests_routes) | dict | - |
| [`RDM_REQUEST_RECORD_DELETION_CHECKLIST`](#rdm_request_record_deletion_checklist) | list | - |
| [`RDM_REQUEST_RECORD_DELETION_ENABLED`](#rdm_request_record_deletion_enabled) | bool | - |
| [`RDM_REQUEST_RECORD_DELETION_POLICIES`](#rdm_request_record_deletion_policies) | list | - |
| [`RDM_RESOURCE_ACCESS_TOKENS_ENABLED`](#rdm_resource_access_tokens_enabled) | bool | - |
| [`RDM_RESOURCE_ACCESS_TOKENS_JWT_LIFETIME`](#rdm_resource_access_tokens_jwt_lifetime) | timedelta | - |
| [`RDM_RESOURCE_ACCESS_TOKENS_SUBJECT_SCHEMA`](#rdm_resource_access_tokens_subject_schema) | unknown | - |
| [`RDM_RESOURCE_ACCESS_TOKENS_WHITELISTED_JWT_ALGORITHMS`](#rdm_resource_access_tokens_whitelisted_jwt_algorithms) | list | - |
| [`RDM_RESOURCE_ACCESS_TOKEN_REQUEST_ARG`](#rdm_resource_access_token_request_arg) | str | - |
| [`RDM_SEARCH`](#rdm_search) | dict | - |
| [`RDM_SEARCH_DRAFTS`](#rdm_search_drafts) | dict | - |
| [`RDM_SEARCH_SORT_BY_VERIFIED`](#rdm_search_sort_by_verified) | bool | - |
| [`RDM_SEARCH_USER_COMMUNITIES`](#rdm_search_user_communities) | dict | - |
| [`RDM_SEARCH_USER_REQUESTS`](#rdm_search_user_requests) | dict | - |
| [`RDM_SEARCH_VERSIONING`](#rdm_search_versioning) | dict | - |
| [`RDM_SORT_OPTIONS`](#rdm_sort_options) | dict | - |
| [`RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS`](#rdm_stats_exclude_preview_file_download_events) | bool | - |
| [`RDM_USER_MODERATION_ENABLED`](#rdm_user_moderation_enabled) | bool | - |
| [`RECAPTCHA_PRIVATE_KEY`](#recaptcha_private_key) | unknown | - |
| [`RECAPTCHA_PUBLIC_KEY`](#recaptcha_public_key) | unknown | - |
| [`RECORDS_FILES_REST_ENDPOINTS`](#records_files_rest_endpoints) | dict | - |
| [`RECORDS_PERMISSIONS_RECORD_POLICY`](#records_permissions_record_policy) | str | - |
| [`RECORDS_REFRESOLVER_CLS`](#records_refresolver_cls) | NoneType | `configure_generic_parameters` |
| [`RECORDS_REFRESOLVER_STORE`](#records_refresolver_store) | NoneType | `configure_generic_parameters` |
| [`RECORDS_RESOURCES_ALLOW_EMPTY_FILES`](#records_resources_allow_empty_files) | bool | - |
| [`RECORDS_RESOURCES_ARCHIVE_DOWNLOAD_MAX_SIZE`](#records_resources_archive_download_max_size) | NoneType | - |
| [`RECORDS_RESOURCES_DEFAULT_TRANSFER_TYPE`](#records_resources_default_transfer_type) | str | - |
| [`RECORDS_RESOURCES_EXTRACTED_STREAM_CHUNK_SIZE`](#records_resources_extracted_stream_chunk_size) | int | - |
| [`RECORDS_RESOURCES_FILES_ALLOWED_DOMAINS`](#records_resources_files_allowed_domains) | list | - |
| [`RECORDS_RESOURCES_IMAGE_FORMATS`](#records_resources_image_formats) | list | - |
| [`RECORDS_RESOURCES_TRANSFERS`](#records_resources_transfers) | list | - |
| [`RECORDS_RESOURCES_ZIP_FORMATS`](#records_resources_zip_formats) | list | - |
| [`RECORDS_RESOURCES_ZIP_MAX_ENTRIES`](#records_resources_zip_max_entries) | int | - |
| [`RECORDS_RESOURCES_ZIP_MAX_HEADER_SIZE`](#records_resources_zip_max_header_size) | int | - |
| [`RECORDS_RESOURCES_ZIP_MAX_LISTING_ENTRIES`](#records_resources_zip_max_listing_entries) | int | - |
| [`RECORDS_RESOURCES_ZIP_MAX_RATIO`](#records_resources_zip_max_ratio) | float | - |
| [`RECORDS_RESOURCES_ZIP_MAX_TOTAL_UNCOMPRESSED`](#records_resources_zip_max_total_uncompressed) | int | - |
| [`RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY`](#records_rest_default_create_permission_factory) | unknown | - |
| [`RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY`](#records_rest_default_delete_permission_factory) | unknown | - |
| [`RECORDS_REST_DEFAULT_LIST_PERMISSION_FACTORY`](#records_rest_default_list_permission_factory) | unknown | - |
| [`RECORDS_REST_DEFAULT_LOADERS`](#records_rest_default_loaders) | unknown | - |
| [`RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY`](#records_rest_default_read_permission_factory) | unknown | - |
| [`RECORDS_REST_DEFAULT_RESULTS_SIZE`](#records_rest_default_results_size) | unknown | - |
| [`RECORDS_REST_DEFAULT_SORT`](#records_rest_default_sort) | unknown | - |
| [`RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY`](#records_rest_default_update_permission_factory) | unknown | - |
| [`RECORDS_REST_ENDPOINTS`](#records_rest_endpoints) | list | `configure_generic_parameters` |
| [`RECORDS_REST_FACETS`](#records_rest_facets) | unknown | - |
| [`RECORDS_REST_FACETS_POST_FILTERS_PROPAGATE`](#records_rest_facets_post_filters_propagate) | unknown | - |
| [`RECORDS_REST_SEARCH_ERROR_HANDLERS`](#records_rest_search_error_handlers) | unknown | - |
| [`RECORDS_REST_SORT_OPTIONS`](#records_rest_sort_options) | unknown | - |
| [`RECORDS_UI_BASE_TEMPLATE`](#records_ui_base_template) | str | - |
| [`RECORDS_UI_DEFAULT_PERMISSION_FACTORY`](#records_ui_default_permission_factory) | NoneType | - |
| [`RECORDS_UI_ENDPOINTS`](#records_ui_endpoints) | dict | `configure_ui` |
| [`RECORDS_UI_EXPORT_FORMATS`](#records_ui_export_formats) | dict | - |
| [`RECORDS_UI_LOGIN_ENDPOINT`](#records_ui_login_endpoint) | str | - |
| [`RECORDS_UI_TOMBSTONE_TEMPLATE`](#records_ui_tombstone_template) | str | - |
| [`RECORDS_VALIDATION_TYPES`](#records_validation_types) | dict | - |
| [`RECORD_ROUTES`](#record_routes) | configured by function | `configure_generic_parameters` |
| [`REMEMBER_COOKIE_DURATION`](#remember_cookie_duration) | unknown | - |
| [`REPOSITORY_DESCRIPTION`](#repository_description) | configured by function | `configure_ui` |
| [`REPOSITORY_KEYWORDS`](#repository_keywords) | configured by function | `configure_ui` |
| [`REPOSITORY_NAME`](#repository_name) | configured by function | `configure_ui` |
| [`REPOSITORY_SUBTITLE`](#repository_subtitle) | configured by function | `configure_ui` |
| [`REPOSITORY_SUPPORT_CONTACT`](#repository_support_contact) | configured by function | `configure_ui` |
| [`REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_ATTRS`](#requests_comments_allowed_extra_html_attrs) | dict | - |
| [`REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_TAGS`](#requests_comments_allowed_extra_html_tags) | list | - |
| [`REQUESTS_COMMENT_PREVIEW_LIMIT`](#requests_comment_preview_limit) | int | - |
| [`REQUESTS_ENTITY_RESOLVERS`](#requests_entity_resolvers) | list | - |
| [`REQUESTS_ERROR_HANDLERS`](#requests_error_handlers) | unknown | - |
| [`REQUESTS_EVENTS_SERVICE_COMPONENTS`](#requests_events_service_components) | list | - |
| [`REQUESTS_FACETS`](#requests_facets) | dict | - |
| [`REQUESTS_FILES_DEFAULT_MAX_FILE_SIZE`](#requests_files_default_max_file_size) | int | - |
| [`REQUESTS_FILES_DEFAULT_QUOTA_SIZE`](#requests_files_default_quota_size) | int | - |
| [`REQUESTS_LOCKING_ENABLED`](#requests_locking_enabled) | bool | - |
| [`REQUESTS_MODERATION_ROLE`](#requests_moderation_role) | str | - |
| [`REQUESTS_PERMISSION_POLICY`](#requests_permission_policy) | unknown | `register_workflow` |
| [`REQUESTS_REGISTERED_EVENT_TYPES`](#requests_registered_event_types) | list | - |
| [`REQUESTS_REGISTERED_TYPES`](#requests_registered_types) | list | - |
| [`REQUESTS_REVIEWERS_ENABLED`](#requests_reviewers_enabled) | bool | - |
| [`REQUESTS_REVIEWERS_MAX_NUMBER`](#requests_reviewers_max_number) | int | - |
| [`REQUESTS_ROUTES`](#requests_routes) | dict | - |
| [`REQUESTS_SEARCH`](#requests_search) | dict | - |
| [`REQUESTS_SORT_OPTIONS`](#requests_sort_options) | dict | - |
| [`REQUESTS_TIMELINE_PAGE_SIZE`](#requests_timeline_page_size) | int | - |
| [`REQUESTS_USER_MODERATION_FACETS`](#requests_user_moderation_facets) | dict | - |
| [`REQUESTS_USER_MODERATION_SEARCH`](#requests_user_moderation_search) | dict | - |
| [`REQUESTS_USER_MODERATION_SORT_OPTIONS`](#requests_user_moderation_sort_options) | dict | - |
| [`REST_CSRF_ENABLED`](#rest_csrf_enabled) | unknown | - |
| [`REST_ENABLE_CORS`](#rest_enable_cors) | unknown | - |
| [`REST_MIMETYPE_QUERY_ARG_NAME`](#rest_mimetype_query_arg_name) | unknown | - |
| [`ROR_CLIENT_ID`](#ror_client_id) | configured by function | `configure_generic_parameters` |
| [`S3_ACCESS_KEY_ID`](#s3_access_key_id) | NoneType | `configure_generic_parameters` |
| [`S3_CONFIG_EXTRA`](#s3_config_extra) | dict | - |
| [`S3_DEFAULT_BLOCK_SIZE`](#s3_default_block_size) | int | - |
| [`S3_ENDPOINT_URL`](#s3_endpoint_url) | NoneType | `configure_generic_parameters` |
| [`S3_MAXIMUM_NUMBER_OF_PARTS`](#s3_maximum_number_of_parts) | int | - |
| [`S3_REGION_NAME`](#s3_region_name) | NoneType | - |
| [`S3_SECRET_ACCESS_KEY`](#s3_secret_access_key) | NoneType | `configure_generic_parameters` |
| [`S3_SIGNATURE_VERSION`](#s3_signature_version) | str | - |
| [`S3_UPLOAD_URL_EXPIRATION`](#s3_upload_url_expiration) | int | - |
| [`S3_URL_EXPIRATION`](#s3_url_expiration) | int | - |
| [`SEARCH_CLIENT_CONFIG`](#search_client_config) | NoneType | `configure_generic_parameters` |
| [`SEARCH_ELASTIC_HOSTS`](#search_elastic_hosts) | NoneType | - |
| [`SEARCH_HOSTS`](#search_hosts) | NoneType | `configure_generic_parameters` |
| [`SEARCH_INDEX_PREFIX`](#search_index_prefix) | str | `configure_generic_parameters` |
| [`SEARCH_MAPPINGS`](#search_mappings) | NoneType | - |
| [`SEARCH_RESULTS_MIN_SCORE`](#search_results_min_score) | NoneType | - |
| [`SEARCH_UI_BASE_TEMPLATE`](#search_ui_base_template) | NoneType | - |
| [`SEARCH_UI_HEADER_TEMPLATE`](#search_ui_header_template) | NoneType | - |
| [`SEARCH_UI_JSTEMPLATE_COUNT`](#search_ui_jstemplate_count) | str | - |
| [`SEARCH_UI_JSTEMPLATE_ERROR`](#search_ui_jstemplate_error) | str | - |
| [`SEARCH_UI_JSTEMPLATE_FACETS`](#search_ui_jstemplate_facets) | str | - |
| [`SEARCH_UI_JSTEMPLATE_LOADING`](#search_ui_jstemplate_loading) | str | - |
| [`SEARCH_UI_JSTEMPLATE_PAGINATION`](#search_ui_jstemplate_pagination) | str | - |
| [`SEARCH_UI_JSTEMPLATE_RANGE`](#search_ui_jstemplate_range) | str | - |
| [`SEARCH_UI_JSTEMPLATE_RANGE_OPTIONS`](#search_ui_jstemplate_range_options) | dict | - |
| [`SEARCH_UI_JSTEMPLATE_RESULTS`](#search_ui_jstemplate_results) | str | - |
| [`SEARCH_UI_JSTEMPLATE_SELECT_BOX`](#search_ui_jstemplate_select_box) | str | - |
| [`SEARCH_UI_JSTEMPLATE_SORT_ORDER`](#search_ui_jstemplate_sort_order) | str | - |
| [`SEARCH_UI_SEARCH_API`](#search_ui_search_api) | str | - |
| [`SEARCH_UI_SEARCH_CONFIG_GEN`](#search_ui_search_config_gen) | dict | - |
| [`SEARCH_UI_SEARCH_INDEX`](#search_ui_search_index) | str | - |
| [`SEARCH_UI_SEARCH_TEMPLATE`](#search_ui_search_template) | str | `configure_ui` |
| [`SEARCH_UI_SEARCH_VIEW`](#search_ui_search_view) | unknown | `configure_ui` |
| [`SECRET_KEY`](#secret_key) | str | `configure_generic_parameters` |
| [`SECRET_KEY_FALLBACKS`](#secret_key_fallbacks) | NoneType | - |
| [`SECURITY_AUTO_LOGIN_AFTER_CONFIRM`](#security_auto_login_after_confirm) | bool | - |
| [`SECURITY_BLUEPRINT_NAME`](#security_blueprint_name) | str | - |
| [`SECURITY_CHANGEABLE`](#security_changeable) | bool | `configure_generic_parameters` |
| [`SECURITY_CHANGE_PASSWORD_TEMPLATE`](#security_change_password_template) | str | - |
| [`SECURITY_CHANGE_SALT`](#security_change_salt) | str | - |
| [`SECURITY_CHANGE_URL`](#security_change_url) | str | - |
| [`SECURITY_CLI_ROLES_NAME`](#security_cli_roles_name) | str | - |
| [`SECURITY_CLI_USERS_NAME`](#security_cli_users_name) | str | - |
| [`SECURITY_CONFIRMABLE`](#security_confirmable) | bool | `configure_generic_parameters` |
| [`SECURITY_CONFIRM_EMAIL_WITHIN`](#security_confirm_email_within) | str | - |
| [`SECURITY_CONFIRM_ERROR_VIEW`](#security_confirm_error_view) | NoneType | - |
| [`SECURITY_CONFIRM_SALT`](#security_confirm_salt) | str | - |
| [`SECURITY_CONFIRM_URL`](#security_confirm_url) | str | - |
| [`SECURITY_DEFAULT_HTTP_AUTH_REALM`](#security_default_http_auth_realm) | str | - |
| [`SECURITY_DEFAULT_REMEMBER_ME`](#security_default_remember_me) | bool | - |
| [`SECURITY_DEPRECATED_HASHING_SCHEMES`](#security_deprecated_hashing_schemes) | list | - |
| [`SECURITY_DEPRECATED_PASSWORD_SCHEMES`](#security_deprecated_password_schemes) | list | - |
| [`SECURITY_EMAIL_HTML`](#security_email_html) | bool | - |
| [`SECURITY_EMAIL_PLAINTEXT`](#security_email_plaintext) | bool | - |
| [`SECURITY_EMAIL_SUBJECT_CONFIRM`](#security_email_subject_confirm) | str | - |
| [`SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE`](#security_email_subject_password_change_notice) | str | - |
| [`SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE`](#security_email_subject_password_notice) | str | - |
| [`SECURITY_EMAIL_SUBJECT_PASSWORD_RESET`](#security_email_subject_password_reset) | str | - |
| [`SECURITY_EMAIL_SUBJECT_REGISTER`](#security_email_subject_register) | str | - |
| [`SECURITY_FLASH_MESSAGES`](#security_flash_messages) | bool | - |
| [`SECURITY_FORGOT_PASSWORD_TEMPLATE`](#security_forgot_password_template) | str | - |
| [`SECURITY_HASHING_SCHEMES`](#security_hashing_schemes) | list | - |
| [`SECURITY_I18N_DIRNAME`](#security_i18n_dirname) | str | - |
| [`SECURITY_I18N_DOMAIN`](#security_i18n_domain) | str | - |
| [`SECURITY_LOGIN_SALT`](#security_login_salt) | str | - |
| [`SECURITY_LOGIN_URL`](#security_login_url) | str | - |
| [`SECURITY_LOGIN_USER_TEMPLATE`](#security_login_user_template) | str | - |
| [`SECURITY_LOGIN_WITHIN`](#security_login_within) | str | - |
| [`SECURITY_LOGIN_WITHOUT_CONFIRMATION`](#security_login_without_confirmation) | bool | `configure_generic_parameters` |
| [`SECURITY_LOGOUT_URL`](#security_logout_url) | str | - |
| [`SECURITY_MSG_ALREADY_CONFIRMED`](#security_msg_already_confirmed) | tuple | - |
| [`SECURITY_MSG_CONFIRMATION_EXPIRED`](#security_msg_confirmation_expired) | tuple | - |
| [`SECURITY_MSG_CONFIRMATION_REQUEST`](#security_msg_confirmation_request) | tuple | - |
| [`SECURITY_MSG_CONFIRMATION_REQUIRED`](#security_msg_confirmation_required) | tuple | - |
| [`SECURITY_MSG_CONFIRM_REGISTRATION`](#security_msg_confirm_registration) | tuple | - |
| [`SECURITY_MSG_DISABLED_ACCOUNT`](#security_msg_disabled_account) | tuple | - |
| [`SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED`](#security_msg_email_already_associated) | tuple | - |
| [`SECURITY_MSG_EMAIL_CONFIRMED`](#security_msg_email_confirmed) | tuple | - |
| [`SECURITY_MSG_EMAIL_NOT_PROVIDED`](#security_msg_email_not_provided) | tuple | - |
| [`SECURITY_MSG_FORGOT_PASSWORD`](#security_msg_forgot_password) | tuple | - |
| [`SECURITY_MSG_INVALID_CONFIRMATION_TOKEN`](#security_msg_invalid_confirmation_token) | tuple | - |
| [`SECURITY_MSG_INVALID_EMAIL_ADDRESS`](#security_msg_invalid_email_address) | tuple | - |
| [`SECURITY_MSG_INVALID_LOGIN_TOKEN`](#security_msg_invalid_login_token) | tuple | - |
| [`SECURITY_MSG_INVALID_PASSWORD`](#security_msg_invalid_password) | tuple | - |
| [`SECURITY_MSG_INVALID_REDIRECT`](#security_msg_invalid_redirect) | tuple | - |
| [`SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN`](#security_msg_invalid_reset_password_token) | tuple | - |
| [`SECURITY_MSG_LOCAL_LOGIN_DISABLED`](#security_msg_local_login_disabled) | tuple | - |
| [`SECURITY_MSG_LOGIN`](#security_msg_login) | tuple | - |
| [`SECURITY_MSG_LOGIN_EMAIL_SENT`](#security_msg_login_email_sent) | tuple | - |
| [`SECURITY_MSG_LOGIN_EXPIRED`](#security_msg_login_expired) | tuple | - |
| [`SECURITY_MSG_PASSWORD_BREACHED`](#security_msg_password_breached) | tuple | - |
| [`SECURITY_MSG_PASSWORD_BREACHED_SITE_ERROR`](#security_msg_password_breached_site_error) | tuple | - |
| [`SECURITY_MSG_PASSWORD_CHANGE`](#security_msg_password_change) | tuple | - |
| [`SECURITY_MSG_PASSWORD_CHANGE_DISABLED`](#security_msg_password_change_disabled) | tuple | - |
| [`SECURITY_MSG_PASSWORD_INVALID_LENGTH`](#security_msg_password_invalid_length) | tuple | - |
| [`SECURITY_MSG_PASSWORD_IS_THE_SAME`](#security_msg_password_is_the_same) | tuple | - |
| [`SECURITY_MSG_PASSWORD_MISMATCH`](#security_msg_password_mismatch) | tuple | - |
| [`SECURITY_MSG_PASSWORD_NOT_PROVIDED`](#security_msg_password_not_provided) | tuple | - |
| [`SECURITY_MSG_PASSWORD_NOT_SET`](#security_msg_password_not_set) | tuple | - |
| [`SECURITY_MSG_PASSWORD_RECOVERY_DISABLED`](#security_msg_password_recovery_disabled) | tuple | - |
| [`SECURITY_MSG_PASSWORD_RESET`](#security_msg_password_reset) | tuple | - |
| [`SECURITY_MSG_PASSWORD_RESET_DISABLED`](#security_msg_password_reset_disabled) | tuple | - |
| [`SECURITY_MSG_PASSWORD_RESET_EXPIRED`](#security_msg_password_reset_expired) | tuple | - |
| [`SECURITY_MSG_PASSWORD_RESET_REQUEST`](#security_msg_password_reset_request) | tuple | - |
| [`SECURITY_MSG_PASSWORD_TOO_SIMPLE`](#security_msg_password_too_simple) | tuple | - |
| [`SECURITY_MSG_REFRESH`](#security_msg_refresh) | tuple | - |
| [`SECURITY_MSG_REGISTRATION_DISABLED`](#security_msg_registration_disabled) | tuple | - |
| [`SECURITY_MSG_RETYPE_PASSWORD_MISMATCH`](#security_msg_retype_password_mismatch) | tuple | - |
| [`SECURITY_MSG_UNAUTHORIZED`](#security_msg_unauthorized) | tuple | - |
| [`SECURITY_MSG_USER_DOES_NOT_EXIST`](#security_msg_user_does_not_exist) | tuple | - |
| [`SECURITY_PASSWORD_BREACHED_COUNT`](#security_password_breached_count) | int | - |
| [`SECURITY_PASSWORD_CHECK_BREACHED`](#security_password_check_breached) | bool | - |
| [`SECURITY_PASSWORD_COMPLEXITY_CHECKER`](#security_password_complexity_checker) | NoneType | - |
| [`SECURITY_PASSWORD_HASH`](#security_password_hash) | str | - |
| [`SECURITY_PASSWORD_LENGTH_MIN`](#security_password_length_min) | int | - |
| [`SECURITY_PASSWORD_SALT`](#security_password_salt) | str | - |
| [`SECURITY_PASSWORD_SCHEMES`](#security_password_schemes) | list | - |
| [`SECURITY_PASSWORD_SINGLE_HASH`](#security_password_single_hash) | list | - |
| [`SECURITY_POST_CHANGE_VIEW`](#security_post_change_view) | NoneType | - |
| [`SECURITY_POST_CONFIRM_VIEW`](#security_post_confirm_view) | NoneType | - |
| [`SECURITY_POST_LOGIN_VIEW`](#security_post_login_view) | str | - |
| [`SECURITY_POST_LOGOUT_VIEW`](#security_post_logout_view) | str | - |
| [`SECURITY_POST_REGISTER_VIEW`](#security_post_register_view) | NoneType | - |
| [`SECURITY_POST_RESET_VIEW`](#security_post_reset_view) | NoneType | - |
| [`SECURITY_RECOVERABLE`](#security_recoverable) | bool | `configure_generic_parameters` |
| [`SECURITY_REGISTERABLE`](#security_registerable) | bool | `configure_generic_parameters` |
| [`SECURITY_REGISTER_URL`](#security_register_url) | str | - |
| [`SECURITY_REGISTER_USER_TEMPLATE`](#security_register_user_template) | str | - |
| [`SECURITY_RESET_PASSWORD_TEMPLATE`](#security_reset_password_template) | str | - |
| [`SECURITY_RESET_PASSWORD_WITHIN`](#security_reset_password_within) | str | - |
| [`SECURITY_RESET_SALT`](#security_reset_salt) | str | - |
| [`SECURITY_RESET_URL`](#security_reset_url) | str | - |
| [`SECURITY_SEND_CONFIRMATION_TEMPLATE`](#security_send_confirmation_template) | str | - |
| [`SECURITY_SEND_LOGIN_TEMPLATE`](#security_send_login_template) | str | - |
| [`SECURITY_SEND_PASSWORD_CHANGE_EMAIL`](#security_send_password_change_email) | bool | - |
| [`SECURITY_SEND_PASSWORD_RESET_EMAIL`](#security_send_password_reset_email) | bool | - |
| [`SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL`](#security_send_password_reset_notice_email) | bool | - |
| [`SECURITY_SEND_REGISTER_EMAIL`](#security_send_register_email) | bool | - |
| [`SECURITY_SUBDOMAIN`](#security_subdomain) | NoneType | - |
| [`SECURITY_TOKEN_AUTHENTICATION_HEADER`](#security_token_authentication_header) | str | - |
| [`SECURITY_TOKEN_AUTHENTICATION_KEY`](#security_token_authentication_key) | str | - |
| [`SECURITY_TOKEN_MAX_AGE`](#security_token_max_age) | NoneType | - |
| [`SECURITY_TRACKABLE`](#security_trackable) | bool | - |
| [`SECURITY_URL_PREFIX`](#security_url_prefix) | NoneType | - |
| [`SECURITY_USER_IDENTITY_ATTRIBUTES`](#security_user_identity_attributes) | list | - |
| [`SECURITY_ZXCVBN_MINIMUM_SCORE`](#security_zxcvbn_minimum_score) | int | - |
| [`SEND_FILE_MAX_AGE_DEFAULT`](#send_file_max_age_default) | NoneType | `configure_generic_parameters` |
| [`SENTRY_DSN`](#sentry_dsn) | NoneType | - |
| [`SERVER_NAME`](#server_name) | NoneType | - |
| [`SESSION_COOKIE_DOMAIN`](#session_cookie_domain) | NoneType | `configure_generic_parameters` |
| [`SESSION_COOKIE_HTTPONLY`](#session_cookie_httponly) | bool | - |
| [`SESSION_COOKIE_NAME`](#session_cookie_name) | str | - |
| [`SESSION_COOKIE_PARTITIONED`](#session_cookie_partitioned) | bool | - |
| [`SESSION_COOKIE_PATH`](#session_cookie_path) | NoneType | - |
| [`SESSION_COOKIE_SAMESITE`](#session_cookie_samesite) | str | - |
| [`SESSION_COOKIE_SECURE`](#session_cookie_secure) | bool | `configure_generic_parameters` |
| [`SESSION_KEY_BITS`](#session_key_bits) | int | - |
| [`SESSION_RANDOM_SOURCE`](#session_random_source) | SystemRandom | - |
| [`SESSION_REFRESH_EACH_REQUEST`](#session_refresh_each_request) | bool | - |
| [`SETTINGS_TEMPLATE`](#settings_template) | str | `configure_ui` |
| [`SITEMAP_MAX_ENTRY_COUNT`](#sitemap_max_entry_count) | int | - |
| [`SITEMAP_ROOT_VIEW_ENABLED`](#sitemap_root_view_enabled) | bool | - |
| [`SITEMAP_SECTIONS`](#sitemap_sections) | list | - |
| [`SITE_API_URL`](#site_api_url) | str | `configure_generic_parameters` |
| [`SITE_UI_URL`](#site_ui_url) | str | `configure_generic_parameters` |
| [`SQLALCHEMY_BINDS`](#sqlalchemy_binds) | dict | - |
| [`SQLALCHEMY_DATABASE_URI`](#sqlalchemy_database_uri) | str | `configure_generic_parameters` |
| [`SQLALCHEMY_ECHO`](#sqlalchemy_echo) | bool | - |
| [`SQLALCHEMY_ENGINE_OPTIONS`](#sqlalchemy_engine_options) | dict | - |
| [`SQLALCHEMY_RECORD_QUERIES`](#sqlalchemy_record_queries) | bool | - |
| [`SQLALCHEMY_TRACK_MODIFICATIONS`](#sqlalchemy_track_modifications) | bool | - |
| [`STATS_AGGREGATIONS`](#stats_aggregations) | dict | - |
| [`STATS_EVENTS`](#stats_events) | dict | - |
| [`STATS_EVENTS_UTC_DATETIME_ENABLED`](#stats_events_utc_datetime_enabled) | bool | - |
| [`STATS_MQ_EXCHANGE`](#stats_mq_exchange) | unknown | - |
| [`STATS_PERMISSION_FACTORY`](#stats_permission_factory) | unknown | - |
| [`STATS_QUERIES`](#stats_queries) | dict | - |
| [`STATS_REGISTER_INDEX_TEMPLATES`](#stats_register_index_templates) | bool | - |
| [`STATS_REGISTER_RECEIVERS`](#stats_register_receivers) | bool | `configure_stats` |
| [`TEMPLATES_AUTO_RELOAD`](#templates_auto_reload) | NoneType | - |
| [`TESTING`](#testing) | bool | - |
| [`THEME_401_TEMPLATE`](#theme_401_template) | str | - |
| [`THEME_403_TEMPLATE`](#theme_403_template) | str | - |
| [`THEME_404_TEMPLATE`](#theme_404_template) | str | - |
| [`THEME_429_TEMPLATE`](#theme_429_template) | str | - |
| [`THEME_500_TEMPLATE`](#theme_500_template) | str | - |
| [`THEME_BASE_TEMPLATE`](#theme_base_template) | str | - |
| [`THEME_COVER_TEMPLATE`](#theme_cover_template) | str | - |
| [`THEME_CSS_TEMPLATE`](#theme_css_template) | configured by function | `configure_ui` |
| [`THEME_ERROR_TEMPLATE`](#theme_error_template) | str | - |
| [`THEME_FOOTER_TEMPLATE`](#theme_footer_template) | str | `configure_ui` |
| [`THEME_FRONTPAGE`](#theme_frontpage) | bool | `configure_ui` |
| [`THEME_FRONTPAGE_LOGO`](#theme_frontpage_logo) | configured by function | `configure_ui` |
| [`THEME_FRONTPAGE_TEMPLATE`](#theme_frontpage_template) | str | `configure_ui` |
| [`THEME_FRONTPAGE_TITLE`](#theme_frontpage_title) | LazyString | `configure_ui` |
| [`THEME_GENERATOR`](#theme_generator) | str | - |
| [`THEME_GOOGLE_SITE_VERIFICATION`](#theme_google_site_verification) | list | - |
| [`THEME_HEADER_LOGIN_TEMPLATE`](#theme_header_login_template) | str | `configure_ui` |
| [`THEME_HEADER_TEMPLATE`](#theme_header_template) | str | `configure_ui` |
| [`THEME_ICONS`](#theme_icons) | dict | - |
| [`THEME_JAVASCRIPT_TEMPLATE`](#theme_javascript_template) | str | `configure_ui` |
| [`THEME_LOGO`](#theme_logo) | str | `configure_ui` |
| [`THEME_LOGO_ADMIN`](#theme_logo_admin) | str | - |
| [`THEME_MATHJAX_CDN`](#theme_mathjax_cdn) | str | - |
| [`THEME_META_ROBOT_TAGS`](#theme_meta_robot_tags) | list | - |
| [`THEME_SEARCHBAR`](#theme_searchbar) | bool | - |
| [`THEME_SEARCH_ENDPOINT`](#theme_search_endpoint) | str | `configure_ui` |
| [`THEME_SETTINGS_TEMPLATE`](#theme_settings_template) | str | - |
| [`THEME_SHOW_FRONTPAGE_INTRO_SECTION`](#theme_show_frontpage_intro_section) | unknown | `configure_ui` |
| [`THEME_SITENAME`](#theme_sitename) | LazyString | `configure_ui` |
| [`THEME_SITEURL`](#theme_siteurl) | str | - |
| [`THEME_TRACKINGCODE_TEMPLATE`](#theme_trackingcode_template) | str | `configure_ui` |
| [`THEME_TWITTERHANDLE`](#theme_twitterhandle) | unknown | - |
| [`TRAP_BAD_REQUEST_ERRORS`](#trap_bad_request_errors) | NoneType | - |
| [`TRAP_HTTP_EXCEPTIONS`](#trap_http_exceptions) | bool | - |
| [`TRUSTED_HOSTS`](#trusted_hosts) | NoneType | - |
| [`TYPE_CHECKING`](#type_checking) | bool | - |
| [`USERPROFILES`](#userprofiles) | bool | - |
| [`USERPROFILES_BASE_TEMPLATE`](#userprofiles_base_template) | str | - |
| [`USERPROFILES_EMAIL_ENABLED`](#userprofiles_email_enabled) | bool | - |
| [`USERPROFILES_EXTEND_SECURITY_FORMS`](#userprofiles_extend_security_forms) | bool | - |
| [`USERPROFILES_PROFILE_TEMPLATE`](#userprofiles_profile_template) | str | - |
| [`USERPROFILES_PROFILE_URL`](#userprofiles_profile_url) | str | - |
| [`USERPROFILES_READ_ONLY`](#userprofiles_read_only) | bool | `configure_generic_parameters`, `configure_einfra_oidc` |
| [`USERPROFILES_SETTINGS_TEMPLATE`](#userprofiles_settings_template) | str | - |
| [`USERS_RESOURCES_AVATAR_COLORS`](#users_resources_avatar_colors) | list | - |
| [`USERS_RESOURCES_DOMAINS_ORG_SCHEMA`](#users_resources_domains_org_schema) | unknown | - |
| [`USERS_RESOURCES_DOMAINS_SEARCH`](#users_resources_domains_search) | dict | - |
| [`USERS_RESOURCES_DOMAINS_SEARCH_FACETS`](#users_resources_domains_search_facets) | dict | - |
| [`USERS_RESOURCES_DOMAINS_SORT_OPTIONS`](#users_resources_domains_sort_options) | dict | - |
| [`USERS_RESOURCES_GROUPS_ADMIN_FACETS`](#users_resources_groups_admin_facets) | dict | - |
| [`USERS_RESOURCES_GROUPS_ADMIN_SEARCH`](#users_resources_groups_admin_search) | dict | - |
| [`USERS_RESOURCES_GROUPS_ADMIN_SORT_OPTIONS`](#users_resources_groups_admin_sort_options) | dict | - |
| [`USERS_RESOURCES_GROUPS_ENABLED`](#users_resources_groups_enabled) | bool | - |
| [`USERS_RESOURCES_MODERATION_LOCK_DEFAULT_TIMEOUT`](#users_resources_moderation_lock_default_timeout) | int | - |
| [`USERS_RESOURCES_MODERATION_LOCK_RENEWAL_TIMEOUT`](#users_resources_moderation_lock_renewal_timeout) | int | - |
| [`USERS_RESOURCES_PROTECTED_GROUP_NAMES`](#users_resources_protected_group_names) | list | - |
| [`USERS_RESOURCES_SEARCH`](#users_resources_search) | dict | - |
| [`USERS_RESOURCES_SEARCH_FACETS`](#users_resources_search_facets) | dict | - |
| [`USERS_RESOURCES_SERVICE_SCHEMA`](#users_resources_service_schema) | unknown | - |
| [`USERS_RESOURCES_SORT_OPTIONS`](#users_resources_sort_options) | dict | - |
| [`USER_DASHBOARD_MENU_OVERRIDES`](#user_dashboard_menu_overrides) | dict | - |
| [`USE_X_SENDFILE`](#use_x_sendfile) | bool | - |
| [`VCS_TEMPLATE_INDEX`](#vcs_template_index) | unknown | - |
| [`VCS_TEMPLATE_INDEX_ITEM`](#vcs_template_index_item) | unknown | - |
| [`VCS_TEMPLATE_RELEASE_ITEM`](#vcs_template_release_item) | unknown | - |
| [`VCS_TEMPLATE_REPO_SWITCH`](#vcs_template_repo_switch) | unknown | - |
| [`VCS_TEMPLATE_VIEW`](#vcs_template_view) | unknown | - |
| [`VOCABULARIES_AFFILIATIONS_EDMO_COUNTRY_MAPPING`](#vocabularies_affiliations_edmo_country_mapping) | dict | - |
| [`VOCABULARIES_AFFILIATION_SCHEMES`](#vocabularies_affiliation_schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_AWARDS_EC_ROR_ID`](#vocabularies_awards_ec_ror_id) | str | - |
| [`VOCABULARIES_AWARDS_OPENAIRE_FUNDERS`](#vocabularies_awards_openaire_funders) | dict | - |
| [`VOCABULARIES_AWARD_SCHEMES`](#vocabularies_award_schemes) | dict | - |
| [`VOCABULARIES_CUSTOM_VOCABULARY_TYPES`](#vocabularies_custom_vocabulary_types) | list | - |
| [`VOCABULARIES_DATASTREAM_READERS`](#vocabularies_datastream_readers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_DATASTREAM_TRANSFORMERS`](#vocabularies_datastream_transformers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_DATASTREAM_WRITERS`](#vocabularies_datastream_writers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_FUNDER_DOI_PREFIX`](#vocabularies_funder_doi_prefix) | str | - |
| [`VOCABULARIES_FUNDER_SCHEMES`](#vocabularies_funder_schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_IDENTIFIER_SCHEMES`](#vocabularies_identifier_schemes) | dict | - |
| [`VOCABULARIES_NAMES_SCHEMES`](#vocabularies_names_schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_ORCID_ACCESS_KEY`](#vocabularies_orcid_access_key) | str | - |
| [`VOCABULARIES_ORCID_ORG_IDS_MAPPING_PATH`](#vocabularies_orcid_org_ids_mapping_path) | NoneType | - |
| [`VOCABULARIES_ORCID_SECRET_KEY`](#vocabularies_orcid_secret_key) | str | - |
| [`VOCABULARIES_ORCID_SUMMARIES_BUCKET`](#vocabularies_orcid_summaries_bucket) | str | - |
| [`VOCABULARIES_ORCID_SYNC_MAX_WORKERS`](#vocabularies_orcid_sync_max_workers) | int | - |
| [`VOCABULARIES_ORCID_SYNC_SINCE`](#vocabularies_orcid_sync_since) | dict | - |
| [`VOCABULARIES_RESOURCE_CONFIG`](#vocabularies_resource_config) | unknown | `configure_generic_parameters` |
| [`VOCABULARIES_SERVICE_CONFIG`](#vocabularies_service_config) | unknown | `configure_generic_parameters` |
| [`VOCABULARIES_SUBJECTS_EUROSCIVOC_FILE_URL`](#vocabularies_subjects_euroscivoc_file_url) | str | - |
| [`VOCABULARIES_SUBJECTS_GEMET_FILE_URL`](#vocabularies_subjects_gemet_file_url) | str | - |
| [`VOCABULARIES_SUBJECTS_NVS_FILE_URL`](#vocabularies_subjects_nvs_file_url) | str | - |
| [`VOCABULARIES_SUBJECTS_SCHEMES`](#vocabularies_subjects_schemes) | dict | - |
| [`VOCABULARIES_TYPES_SEARCH`](#vocabularies_types_search) | dict | - |
| [`VOCABULARIES_TYPES_SORT_OPTIONS`](#vocabularies_types_sort_options) | dict | - |
| [`WEBPACKEXT_MANIFEST_PATH`](#webpackext_manifest_path) | str | - |
| [`WEBPACKEXT_NPM_PKG_CLS`](#webpackext_npm_pkg_cls) | configured by function | `configure_ui` |
| [`WEBPACKEXT_PROJECT`](#webpackext_project) | str | `configure_ui` |
| [`WEBPACKEXT_PROJECT_BUILDDIR`](#webpackext_project_builddir) | str | - |
| [`WEBPACKEXT_PROJECT_DISTDIR`](#webpackext_project_distdir) | str | - |
| [`WEBPACKEXT_PROJECT_DISTURL`](#webpackext_project_disturl) | str | - |
| [`WORKFLOWS`](#workflows) | configured by function | `register_workflow` |

## Detailed Variable Reference
### <a id='access_action_cache_prefix'></a>`ACCESS_ACTION_CACHE_PREFIX`
| **Description** | Prefix for actions cached when used in dynamic permissions. |
|--------------|-----------|
| **Default Value** | `'Permission::action::'` |
| **Type** | str |
| **Source** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L21) |

---

### <a id='access_cache'></a>`ACCESS_CACHE`
| **Description** | A cache instance or an importable string pointing to the cache instance. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L18); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L729) |

---

### <a id='access_load_system_role_needs'></a>`ACCESS_LOAD_SYSTEM_ROLE_NEEDS`
| **Description** | Enables the loading of system role needs when users' identity change. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L24) |

---

### <a id='accounts'></a>`ACCOUNTS`
| **Description** | Tells if the templates should use the accounts module.  If False, you won't be able to login via the... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L21) |

---

### <a id='accounts_base_template'></a>`ACCOUNTS_BASE_TEMPLATE`
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='accounts_confirm_email_endpoint'></a>`ACCOUNTS_CONFIRM_EMAIL_ENDPOINT`
| **Description** | Value to be used for the confirmation email link in the UI application. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L62) |

---

### <a id='accounts_cover_template'></a>`ACCOUNTS_COVER_TEMPLATE`
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='accounts_default_email_visibility'></a>`ACCOUNTS_DEFAULT_EMAIL_VISIBILITY`
| **Description** | Default Email visibility value can be set to either 'restricted' or 'public'. |
|--------------|-----------|
| **Default Value** | `'restricted'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L65) |

---

### <a id='accounts_default_users_verified'></a>`ACCOUNTS_DEFAULT_USERS_VERIFIED`
| **Description** | Default verified status: if set to 'True', users are verified by default. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L384) |

---

### <a id='accounts_default_user_visibility'></a>`ACCOUNTS_DEFAULT_USER_VISIBILITY`
| **Description** | Default User visibility value can be set to either 'restricted' or 'public'. |
|--------------|-----------|
| **Default Value** | `'restricted'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L364) |

---

### <a id='accounts_forgot_password_email_ratelimit'></a>`ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT`
| **Description** | Flask-Limiter rate limit string for forgot-password requests per account.  Example: ``"3 per hour"``... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L91) |

---

### <a id='accounts_forgot_password_email_ratelimit_key_prefix'></a>`ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_KEY_PREFIX`
| **Description** | Prefix used to namespace forgot-password per-account limiter keys. |
|--------------|-----------|
| **Default Value** | `'accounts.fp_email'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L97) |

---

### <a id='accounts_forgot_password_email_ratelimit_msg'></a>`ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_MSG`
| **Default Value** | `l'Too many password-reset requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L100) |

---

### <a id='accounts_jwt_alogorithm'></a>`ACCOUNTS_JWT_ALOGORITHM`
| **Description** | Set JWT encryption alogirthm.  .. note::     `Available aglorithms    <https://pyjwt.readthedocs.io/... |
|--------------|-----------|
| **Default Value** | `'HS256'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L323) |

---

### <a id='accounts_jwt_creation_factory'></a>`ACCOUNTS_JWT_CREATION_FACTORY`
| **Description** | Import path of factory used to generate JWT. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts.utils:jwt_create_token'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L335) |

---

### <a id='accounts_jwt_decode_factory'></a>`ACCOUNTS_JWT_DECODE_FACTORY`
| **Description** | Import path of factory used to decode JWT. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts.utils:jwt_decode_token'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L332) |

---

### <a id='accounts_jwt_dom_token'></a>`ACCOUNTS_JWT_DOM_TOKEN`
| **Description** | Register JWT context processor.  .. code-block:: html      {% if current_user.is_authenticated %}   ... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L277) |

---

### <a id='accounts_jwt_dom_token_template'></a>`ACCOUNTS_JWT_DOM_TOKEN_TEMPLATE`
| **Description** | Template for the context processor. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/jwt.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L309) |

---

### <a id='accounts_jwt_enable'></a>`ACCOUNTS_JWT_ENABLE`
| **Description** | Enable JWT support.  .. note::      More details about `JWT <https://jwt.io>`_ |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L269) |

---

### <a id='accounts_jwt_expiration_delta'></a>`ACCOUNTS_JWT_EXPIRATION_DELTA`
| **Description** | Token expiration period for JWT. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=1)` |
| **Type** | timedelta |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L320) |

---

### <a id='accounts_jwt_secret_key'></a>`ACCOUNTS_JWT_SECRET_KEY`
| **Description** | Secret key for JWT.  .. note::      If is set to ``None`` it will use the ``SECRET_KEY``. |
|--------------|-----------|
| **Default Value** | `'CHANGE_ME'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L312) |

---

### <a id='accounts_local_login_enabled'></a>`ACCOUNTS_LOCAL_LOGIN_ENABLED`
| **Description** | Whether or not login with local account credentials should be enabled. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L355) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='accounts_login_ratelimit'></a>`ACCOUNTS_LOGIN_RATELIMIT`
| **Description** | Flask-Limiter rate limit string for login requests per account.  Example: ``"5 per 15 minutes"``. Di... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L105) |

---

### <a id='accounts_login_ratelimit_key_prefix'></a>`ACCOUNTS_LOGIN_RATELIMIT_KEY_PREFIX`
| **Description** | Prefix used to namespace login per-account limiter keys. |
|--------------|-----------|
| **Default Value** | `'accounts.login'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L111) |

---

### <a id='accounts_login_ratelimit_msg'></a>`ACCOUNTS_LOGIN_RATELIMIT_MSG`
| **Default Value** | `l'Too many login attempts for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L114) |

---

### <a id='accounts_login_view_function'></a>`ACCOUNTS_LOGIN_VIEW_FUNCTION`
| **Description** | The view function to use for the login endpoint.  This can be either an import string, or the view f... |
|--------------|-----------|
| **Default Value** | `login` |
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L347) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='accounts_register_blueprint'></a>`ACCOUNTS_REGISTER_BLUEPRINT`
| **Description** | Register the Security blueprint or not.  It can be used to override the ``register_blueprint`` optio... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L42) |

---

### <a id='accounts_reset_password_endpoint'></a>`ACCOUNTS_RESET_PASSWORD_ENDPOINT`
| **Description** | Value to be used for the confirmation email link in the UI application. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L78) |

---

### <a id='accounts_rest_auth_views'></a>`ACCOUNTS_REST_AUTH_VIEWS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L133) |

---

### <a id='accounts_rest_confirm_email_endpoint'></a>`ACCOUNTS_REST_CONFIRM_EMAIL_ENDPOINT`
| **Description** | Value to be used for the confirmation email link in the API application.  Can be a Flask endpoint (e... |
|--------------|-----------|
| **Default Value** | `'/confirm/{token}'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L68) |

---

### <a id='accounts_rest_reset_password_endpoint'></a>`ACCOUNTS_REST_RESET_PASSWORD_ENDPOINT`
| **Description** | Value to be used for the reset password link in the API application.  Can be a Flask endpoint (e.g. ... |
|--------------|-----------|
| **Default Value** | `'/lost-password/{token}'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L81) |

---

### <a id='accounts_retention_period'></a>`ACCOUNTS_RETENTION_PERIOD`
| **Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L27) |

---

### <a id='accounts_send_confirmation_ratelimit'></a>`ACCOUNTS_SEND_CONFIRMATION_RATELIMIT`
| **Description** | Flask-Limiter rate limit string for send-confirmation requests per account.  Example: ``"3 per hour"... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L119) |

---

### <a id='accounts_send_confirmation_ratelimit_key_prefix'></a>`ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_KEY_PREFIX`
| **Description** | Prefix used to namespace send-confirmation per-account limiter keys. |
|--------------|-----------|
| **Default Value** | `'accounts.cf_email'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L125) |

---

### <a id='accounts_send_confirmation_ratelimit_msg'></a>`ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_MSG`
| **Default Value** | `l'Too many confirmation-email requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L128) |

---

### <a id='accounts_session_activity_enabled'></a>`ACCOUNTS_SESSION_ACTIVITY_ENABLED`
| **Description** | Enable session activity tracking. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L56) |

---

### <a id='accounts_session_redis_url'></a>`ACCOUNTS_SESSION_REDIS_URL`
| **Description** | Redis URL used by the module as a cache system for sessions. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L39); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L395) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='accounts_session_store_factory'></a>`ACCOUNTS_SESSION_STORE_FACTORY`
| **Default Value** | `'invenio_accounts.sessions:default_session_store_factory'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L29) |

---

### <a id='accounts_settings_security_template'></a>`ACCOUNTS_SETTINGS_SECURITY_TEMPLATE`
| **Description** | Template for the account security page. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/settings/security.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L59) |

---

### <a id='accounts_settings_template'></a>`ACCOUNTS_SETTINGS_TEMPLATE`
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='accounts_sitename'></a>`ACCOUNTS_SITENAME`
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | unknown |

---

### <a id='accounts_userinfo_headers'></a>`ACCOUNTS_USERINFO_HEADERS`
| **Description** | If True, add X-Session-ID and X-User-ID to the HTTP response. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L344); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L398) |

---

### <a id='accounts_username_regex'></a>`ACCOUNTS_USERNAME_REGEX`
| **Description** | The regular expression used for validating usernames.  .. note:: When this configuration value is ov... |
|--------------|-----------|
| **Default Value** | `'^[a-zA-Z][a-zA-Z0-9-_]{2,255}$'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L367) |

---

### <a id='accounts_username_rules_text'></a>`ACCOUNTS_USERNAME_RULES_TEXT`
| **Default Value** | `l'Username must start with a letter, be at least three characters long and only contain alphanumeric...` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L375) |

---

### <a id='accounts_user_preferences_schema'></a>`ACCOUNTS_USER_PREFERENCES_SCHEMA`
| **Description** | The schema to use for validation of the user preferences. |
|--------------|-----------|
| **Default Value** | `<UserPreferencesSchema(many=False)>` |
| **Type** | UserPreferencesSchema |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L358); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L407) |

---

### <a id='accounts_user_profile_schema'></a>`ACCOUNTS_USER_PROFILE_SCHEMA`
| **Description** | The schema to use for validation of the user profile. |
|--------------|-----------|
| **Default Value** | `<UserProfileSchema(many=False)>` |
| **Type** | UserProfileSchema |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L361) |

---

### <a id='accounts_use_celery'></a>`ACCOUNTS_USE_CELERY`
| **Description** | Tells if the module should use Celery or not.  By default, it uses Celery if it can find it. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L50) |

---

### <a id='administration_appname'></a>`ADMINISTRATION_APPNAME`
| **Description** | Name of the Flask-Admin app (also the page title of admin panel). |
|--------------|-----------|
| **Default Value** | `'Invenio-Administration'` |
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L15) |

---

### <a id='administration_base_template'></a>`ADMINISTRATION_BASE_TEMPLATE`
| **Description** | Admin panel base template. By default (``None``) uses the Flask-Admin template. |
|--------------|-----------|
| **Default Value** | `'invenio_administration/base.html'` |
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L11) |

---

### <a id='administration_dashboard_view'></a>`ADMINISTRATION_DASHBOARD_VIEW`
| **Default Value** | `'invenio_administration.views.dashboard.AdminDashboardView'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L18) |

---

### <a id='administration_display_versions'></a>`ADMINISTRATION_DISPLAY_VERSIONS`
| **Description** | Display packages versions in the admin panel side bar.  Accepts a list of tuples in the format (pack... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Sources** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L26); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1540) |

---

### <a id='administration_theme_base_template'></a>`ADMINISTRATION_THEME_BASE_TEMPLATE`
| **Description** | Administration base template. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page.html'` |
| **Type** | str |
| **Sources** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L23); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1543) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='admin_base_template'></a>`ADMIN_BASE_TEMPLATE`
| **Description** | Base template for the administration interface.  The template changes the administration interface f... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_admin.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L27) |

---

### <a id='alembic'></a>`ALEMBIC`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='alembic_context'></a>`ALEMBIC_CONTEXT`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='allowed_html_attrs'></a>`ALLOWED_HTML_ATTRS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='allowed_html_tags'></a>`ALLOWED_HTML_TAGS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

---

### <a id='application_root'></a>`APPLICATION_ROOT`
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='app_allowed_hosts'></a>`APP_ALLOWED_HOSTS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='app_default_secure_headers'></a>`APP_DEFAULT_SECURE_HEADERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L125) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui), [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='app_enable_secure_headers'></a>`APP_ENABLE_SECURE_HEADERS`
| **Description** | Enable Secure Headers. (Default: ``True``)  In case you want to disable completely `Talisman`, you c... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L112) |

---

### <a id='app_health_blueprint_enabled'></a>`APP_HEALTH_BLUEPRINT_ENABLED`
| **Description** | Enable the ping (healthcheck) blueprint. (Default: ``False``) |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L188) |

---

### <a id='app_logs_permission_policy'></a>`APP_LOGS_PERMISSION_POLICY`
| **Description** | Permission policy for job logs. |
|--------------|-----------|
| **Default Value** | `JobLogsPermissionPolicy` |
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L29) |
| **Set by** | [`configure_jobs`](api.html#oarepo_config.configure_jobs) |

---

### <a id='app_rdm_admin_email_recipient'></a>`APP_RDM_ADMIN_EMAIL_RECIPIENT`
| **Description** | Admin e-mail |
|--------------|-----------|
| **Default Value** | `'info@inveniosoftware.org'` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1042) |

---

### <a id='app_rdm_deposit_form_autocomplete_names'></a>`APP_RDM_DEPOSIT_FORM_AUTOCOMPLETE_NAMES`
| **Description** | Behavior for autocomplete names search field for creators/contributors.  Available options:  - ``sea... |
|--------------|-----------|
| **Default Value** | `'search'` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L988) |

---

### <a id='app_rdm_deposit_form_custom_field_defaults'></a>`APP_RDM_DEPOSIT_FORM_CUSTOM_FIELD_DEFAULTS`
| **Description** | Default values for custom fields in new records in the deposit UI.  The keys denote the dot-separate... |
|--------------|-----------|
| **Default Value** | `{}` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L979) |

---

### <a id='app_rdm_deposit_form_defaults'></a>`APP_RDM_DEPOSIT_FORM_DEFAULTS`
| **Default Value** | `{'publication_date': lambda: datetime.now().strftime('%Y-%m-%d'), 'rights': [{'id': 'cc-by-4.0', 'ti...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L954) |

---

### <a id='app_rdm_deposit_form_publish_modal_extra'></a>`APP_RDM_DEPOSIT_FORM_PUBLISH_MODAL_EXTRA`
| **Description** | Additional text/html to be displayed in the publish and submit for review modal. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1008) |

---

### <a id='app_rdm_deposit_form_quota'></a>`APP_RDM_DEPOSIT_FORM_QUOTA`
| **Default Value** | `{'maxFiles': 100, 'maxStorage': RDM_FILES_DEFAULT_QUOTA_SIZE}` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L999) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='app_rdm_deposit_form_template'></a>`APP_RDM_DEPOSIT_FORM_TEMPLATE`
| **Description** | Deposit page's form template. |
|--------------|-----------|
| **Default Value** | `'invenio_app_rdm/records/deposit.html'` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L792) |

---

### <a id='app_rdm_deposit_ng_files_ui_enabled'></a>`APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED`
| **Description** | Feature toggle to enable the next-generation (NG) file uploader UI in the deposit form.  When enable... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L947) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='app_rdm_detail_side_bar_templates'></a>`APP_RDM_DETAIL_SIDE_BAR_TEMPLATES`
| **Default Value** | `['invenio_app_rdm/records/details/side_bar/manage_menu.html', 'invenio_app_rdm/records/details/side_...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1018) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='app_rdm_display_decimal_file_sizes'></a>`APP_RDM_DISPLAY_DECIMAL_FILE_SIZES`
| **Description** | Display the file sizes in powers of 1000 (KB, ...) or 1024 (KiB, ...). |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1005) |

---

### <a id='app_rdm_files_integrity_report_subject'></a>`APP_RDM_FILES_INTEGRITY_REPORT_SUBJECT`
| **Description** | Files integrity report subject |
|--------------|-----------|
| **Default Value** | `_('Files integrity report')` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1039) |

---

### <a id='app_rdm_files_integrity_report_template'></a>`APP_RDM_FILES_INTEGRITY_REPORT_TEMPLATE`
| **Default Value** | `'invenio_app_rdm/files_integrity_report/email/files_integrity_report.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1034) |

---

### <a id='app_rdm_identifier_schemes_ui'></a>`APP_RDM_IDENTIFIER_SCHEMES_UI`
| **Default Value** | `{'orcid': {'url_prefix': 'http://orcid.org/', 'icon': 'images/orcid.svg', 'label': 'ORCID'}, 'ror': ...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1045) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='app_rdm_moderation_request_facets'></a>`APP_RDM_MODERATION_REQUEST_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1595) |

---

### <a id='app_rdm_moderation_request_search'></a>`APP_RDM_MODERATION_REQUEST_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1564) |

---

### <a id='app_rdm_moderation_request_sort_options'></a>`APP_RDM_MODERATION_REQUEST_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1570) |

---

### <a id='app_rdm_pages'></a>`APP_RDM_PAGES`
| **Description** | Register static pages with predefined initial content from 'pages.yaml' file.  Example: {     "about... |
|--------------|-----------|
| **Default Value** | `{}` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1232) |

---

### <a id='app_rdm_records_export_url'></a>`APP_RDM_RECORDS_EXPORT_URL`
| **Default Value** | `'/records/<pid_value>/export/<export_format>'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L945) |

---

### <a id='app_rdm_record_exporters'></a>`APP_RDM_RECORD_EXPORTERS`
| **Default Value** | `{'json': {'name': _('JSON'), 'serializer': 'flask_resources.serializers:JSONSerializer', 'params': {...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L823) |

---

### <a id='app_rdm_record_landing_page_external_links'></a>`APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS`
| **Description** | Default format used for adding badges to a record.  Make sure the 'render' field points to a valid r... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L924) |

---

### <a id='app_rdm_record_landing_page_fair_signposting_level_1_enabled'></a>`APP_RDM_RECORD_LANDING_PAGE_FAIR_SIGNPOSTING_LEVEL_1_ENABLED`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1013) |

---

### <a id='app_rdm_record_landing_page_template'></a>`APP_RDM_RECORD_LANDING_PAGE_TEMPLATE`
| **Default Value** | `'invenio_app_rdm/records/detail.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1011) |

---

### <a id='app_rdm_record_thumbnail_sizes'></a>`APP_RDM_RECORD_THUMBNAIL_SIZES`
| **Description** | Allowed record thumbnail sizes. |
|--------------|-----------|
| **Default Value** | `[10, 50, 100, 250, 750, 1200]` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1015) |

---

### <a id='app_rdm_routes'></a>`APP_RDM_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L801) |

---

### <a id='app_rdm_subcommunities_label'></a>`APP_RDM_SUBCOMMUNITIES_LABEL`
| **Description** | Label for the subcommunities in the community browse page. |
|--------------|-----------|
| **Default Value** | `_('Subcommunities')` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1547) |

---

### <a id='app_rdm_user_dashboard_routes'></a>`APP_RDM_USER_DASHBOARD_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L795) |

---

### <a id='app_requestid_header'></a>`APP_REQUESTID_HEADER`
| **Description** | Name of header containing a request id (max length 200 characters).  If set, the request id will be ... |
|--------------|-----------|
| **Default Value** | `'X-Request-Id'` |
| **Type** | str |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L192) |

---

### <a id='app_theme'></a>`APP_THEME`
| **Description** | Application-wide themes list used for template and assets lookup.  The value is a list of theme stri... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L97); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L267) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='assets_builder'></a>`ASSETS_BUILDER`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='audit_logs_disabled_actions'></a>`AUDIT_LOGS_DISABLED_ACTIONS`
| **Description** | Disabled actions to be excluded from the audit logs. To find all the available actions, check the en... |
|--------------|-----------|
| **Default Value** | `<set>` |
| **Type** | set |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L52) |

---

### <a id='audit_logs_enabled'></a>`AUDIT_LOGS_ENABLED`
| **Description** | Feature flag. Disabled by default. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L49) |

---

### <a id='audit_logs_facets'></a>`AUDIT_LOGS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L24) |

---

### <a id='audit_logs_search'></a>`AUDIT_LOGS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L14) |

---

### <a id='audit_logs_sort_options'></a>`AUDIT_LOGS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L42) |

---

### <a id='babel_default_locale'></a>`BABEL_DEFAULT_LOCALE`
| **Description** | Default locale (language). |
|--------------|-----------|
| **Default Value** | `'en'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L247) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='babel_default_timezone'></a>`BABEL_DEFAULT_TIMEZONE`
| **Description** | Default time zone. |
|--------------|-----------|
| **Default Value** | `'Europe/Zurich'` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L250) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='banners_categories'></a>`BANNERS_CATEGORIES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L15) |

---

### <a id='banners_categories_to_style'></a>`BANNERS_CATEGORIES_TO_STYLE`
| **Description** | Function to transform the banner category to a specific Semantic-UI class. |
|--------------|-----------|
| **Default Value** | `style_category` |
| **Type** | unknown |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L22) |

---

### <a id='banners_search'></a>`BANNERS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L25) |

---

### <a id='banners_sort_options'></a>`BANNERS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L36) |

---

### <a id='base_template'></a>`BASE_TEMPLATE`
| **Description** | Base template for user facing pages.  The template provides a basic skeleton which takes care of loa... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L14); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L270) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='broker_url'></a>`BROKER_URL`
| **Description** | URL of message broker for Celery 3 (default is RabbitMQ). |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/0'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L428); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L16) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='cache_is_authenticated_callback'></a>`CACHE_IS_AUTHENTICATED_CALLBACK`
| **Description** | Import path to callback.  Callback is executed to determine if request is authenticated. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L34) |

---

### <a id='cache_key_prefix'></a>`CACHE_KEY_PREFIX`
| **Description** | Cache key prefix. |
|--------------|-----------|
| **Default Value** | `'cache::'` |
| **Type** | str |
| **Source** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L20) |

---

### <a id='cache_redis_url'></a>`CACHE_REDIS_URL`
| **Description** | Redis location and database. |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/0'` |
| **Type** | str |
| **Sources** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L30); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L719) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='cache_type'></a>`CACHE_TYPE`
| **Description** | Cache type.  Please refer to Flask-Caching documentation for other cache types. |
|--------------|-----------|
| **Default Value** | `'flask_caching.backends.redis'` |
| **Type** | str |
| **Sources** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L24); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L722) |

---

### <a id='celery_accept_content'></a>`CELERY_ACCEPT_CONTENT`
| **Description** | A whitelist of content-types/serializers. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L23) |

---

### <a id='celery_always_eager'></a>`CELERY_ALWAYS_EAGER`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='celery_beat_schedule'></a>`CELERY_BEAT_SCHEDULE`
| **Default Value** | `{'indexer': {'task': 'invenio_records_resources.tasks.manage_indexer_queues', 'schedule': timedelta(...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L431) |
| **Set by** | [`configure_cron`](api.html#oarepo_config.configure_cron) |

---

### <a id='celery_broker_url'></a>`CELERY_BROKER_URL`
| **Description** | Same as BROKER_URL to support Celery 4. |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/0'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L511); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L17) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='celery_result_backend'></a>`CELERY_RESULT_BACKEND`
| **Description** | URL of backend for result storage (default is Redis). |
|--------------|-----------|
| **Default Value** | `'redis://localhost:6379/1'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L514); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L20) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='celery_result_serializer'></a>`CELERY_RESULT_SERIALIZER`
| **Description** | Result serialization format. Default is ``msgpack``. |
|--------------|-----------|
| **Default Value** | `'msgpack'` |
| **Type** | str |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L26) |

---

### <a id='celery_task_serializer'></a>`CELERY_TASK_SERIALIZER`
| **Description** | The default serialization method to use. Default is ``msgpack``. |
|--------------|-----------|
| **Default Value** | `'msgpack'` |
| **Type** | str |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L29) |

---

### <a id='celery_worker_concurrency'></a>`CELERY_WORKER_CONCURRENCY`
| **Default Value** | `16` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='celery_worker_pool'></a>`CELERY_WORKER_POOL`
| **Default Value** | `'threads'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='checks_enabled'></a>`CHECKS_ENABLED`
| **Description** | Enable checks. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-checks](https://github.com/inveniosoftware/invenio-checks/blob/master/invenio_checks/config.py#L10) |

---

### <a id='collections_max_collections_per_tree'></a>`COLLECTIONS_MAX_COLLECTIONS_PER_TREE`
| **Description** | Maximum number of collections allowed per tree.  This counts all collections in a tree, regardless o... |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L25) |

---

### <a id='collections_max_depth'></a>`COLLECTIONS_MAX_DEPTH`
| **Description** | Maximum depth for collection hierarchies.  Depth 0 = root collections Depth 1 = children of root Dep... |
|--------------|-----------|
| **Default Value** | `1` |
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L7) |

---

### <a id='collections_max_trees'></a>`COLLECTIONS_MAX_TREES`
| **Description** | Maximum number of collection trees allowed per namespace.  Set to 0 for unlimited trees. Default: 10 |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L18) |

---

### <a id='collections_permission_policy'></a>`COLLECTIONS_PERMISSION_POLICY`
| **Description** | Permission policy used by invenio-collections for managing collection trees. |
|--------------|-----------|
| **Default Value** | `CommunityPermissionPolicy` |
| **Type** | unknown |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L25) |

---

### <a id='collect_static_root'></a>`COLLECT_STATIC_ROOT`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='collect_storage'></a>`COLLECT_STORAGE`
| **Description** | Static files collection method (defaults to copying files). |
|--------------|-----------|
| **Default Value** | `'flask_collect.storage.link'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L386) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='communities_allow_membership_requests'></a>`COMMUNITIES_ALLOW_MEMBERSHIP_REQUESTS`
| **Description** | Feature flag for membership request. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L370) |

---

### <a id='communities_allow_restricted'></a>`COMMUNITIES_ALLOW_RESTRICTED`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L351) |

---

### <a id='communities_always_show_create_link'></a>`COMMUNITIES_ALWAYS_SHOW_CREATE_LINK`
| **Description** | Controls visibility of 'New Community' btn based on user's permission when set to True. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L367) |

---

### <a id='communities_collections_enabled'></a>`COMMUNITIES_COLLECTIONS_ENABLED`
| **Description** | Feature flag to enable/disable collections feature. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L376) |

---

### <a id='communities_custom_fields'></a>`COMMUNITIES_CUSTOM_FIELDS`
| **Description** | Communities custom fields definition.  Of the shape:  .. code-block:: python      [         <custom-... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L283) |

---

### <a id='communities_custom_fields_ui'></a>`COMMUNITIES_CUSTOM_FIELDS_UI`
| **Description** | Communities custom fields UI configuration.  Of the shape:  .. code-block:: python      [{         s... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L306) |

---

### <a id='communities_default_record_submission_policy'></a>`COMMUNITIES_DEFAULT_RECORD_SUBMISSION_POLICY`
| **Description** | Default value of record submission policy community access setting. |
|--------------|-----------|
| **Default Value** | `<RecordSubmissionPolicyEnum.OPEN: 'open'>` |
| **Type** | RecordSubmissionPolicyEnum |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L373) |

---

### <a id='communities_error_handlers'></a>`COMMUNITIES_ERROR_HANDLERS`
| **Default Value** | `{**community_error_handlers, InvalidCommunityVisibility: create_error_handler(lambda e: HTTPJSONExce...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1075) |

---

### <a id='communities_facets'></a>`COMMUNITIES_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L52) |

---

### <a id='communities_identities_cache_handler'></a>`COMMUNITIES_IDENTITIES_CACHE_HANDLER`
| **Default Value** | `'invenio_communities.cache.redis:IdentityRedisCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L361) |

---

### <a id='communities_identities_cache_redis_url'></a>`COMMUNITIES_IDENTITIES_CACHE_REDIS_URL`
| **Default Value** | `'redis://localhost:6379/4'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L358) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='communities_identities_cache_time'></a>`COMMUNITIES_IDENTITIES_CACHE_TIME`
| **Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L355) |

---

### <a id='communities_invitations_expires_in'></a>`COMMUNITIES_INVITATIONS_EXPIRES_IN`
| **Description** | Default amount of time before an invitation expires. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=30)` |
| **Type** | timedelta |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L236) |

---

### <a id='communities_invitations_search'></a>`COMMUNITIES_INVITATIONS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L210) |

---

### <a id='communities_invitations_sort_options'></a>`COMMUNITIES_INVITATIONS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L216) |

---

### <a id='communities_logo_max_file_size'></a>`COMMUNITIES_LOGO_MAX_FILE_SIZE`
| **Description** | Community logo size quota, in bytes. |
|--------------|-----------|
| **Default Value** | `1000000` |
| **Type** | int |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L264) |

---

### <a id='communities_membership_requests_expires_in'></a>`COMMUNITIES_MEMBERSHIP_REQUESTS_EXPIRES_IN`
| **Description** | Default amount of time before a membership request expires. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=30)` |
| **Type** | timedelta |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L261) |

---

### <a id='communities_membership_requests_facets'></a>`COMMUNITIES_MEMBERSHIP_REQUESTS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L245) |

---

### <a id='communities_membership_requests_search'></a>`COMMUNITIES_MEMBERSHIP_REQUESTS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L239) |

---

### <a id='communities_members_facets'></a>`COMMUNITIES_MEMBERS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L194) |

---

### <a id='communities_members_search'></a>`COMMUNITIES_MEMBERS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L168) |

---

### <a id='communities_members_sort_options'></a>`COMMUNITIES_MEMBERS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L174) |

---

### <a id='communities_namespaces'></a>`COMMUNITIES_NAMESPACES`
| **Description** | Custom fields namespaces.  .. code-block:: python     {<namespace>: <uri>, ...}  For example:  .. co... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L267) |

---

### <a id='communities_oai_sets_prefix'></a>`COMMUNITIES_OAI_SETS_PREFIX`
| **Default Value** | `'community-'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L365) |

---

### <a id='communities_permission_policy'></a>`COMMUNITIES_PERMISSION_POLICY`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_communities`](api.html#oarepo_config.configure_communities) |

---

### <a id='communities_records_search'></a>`COMMUNITIES_RECORDS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1085) |

---

### <a id='communities_register_ui_blueprint'></a>`COMMUNITIES_REGISTER_UI_BLUEPRINT`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_communities`](api.html#oarepo_config.configure_communities) |

---

### <a id='communities_requests_search'></a>`COMMUNITIES_REQUESTS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L162) |

---

### <a id='communities_roles'></a>`COMMUNITIES_ROLES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L109) |
| **Set by** | [`configure_communities`](api.html#oarepo_config.configure_communities) |

---

### <a id='communities_routes'></a>`COMMUNITIES_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L28) |

---

### <a id='communities_search'></a>`COMMUNITIES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L147) |

---

### <a id='communities_search_sort_by_verified'></a>`COMMUNITIES_SEARCH_SORT_BY_VERIFIED`
| **Description** | Sort communities by 'verified' first. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L153) |

---

### <a id='communities_service_components'></a>`COMMUNITIES_SERVICE_COMPONENTS`
| **Default Value** | `CommunityServiceComponents` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1067) |

---

### <a id='communities_sort_options'></a>`COMMUNITIES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L72) |

---

### <a id='communities_subcommunities_facets'></a>`COMMUNITIES_SUBCOMMUNITIES_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L69) |

---

### <a id='communities_subcommunities_search'></a>`COMMUNITIES_SUBCOMMUNITIES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L156) |

---

### <a id='communities_sub_invitation_request_cls'></a>`COMMUNITIES_SUB_INVITATION_REQUEST_CLS`
| **Description** | RDM specific request type for subcommunity invitations. |
|--------------|-----------|
| **Default Value** | `RDMSubCommunityInvitationRequest` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1072) |

---

### <a id='communities_sub_request_cls'></a>`COMMUNITIES_SUB_REQUEST_CLS`
| **Description** | RDM specific request type for subcommunities. |
|--------------|-----------|
| **Default Value** | `RDMSubCommunityRequest` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1069) |

---

### <a id='cors_expose_headers'></a>`CORS_EXPOSE_HEADERS`
| **Default Value** | `['ETag', 'Link', 'X-RateLimit-Limit', 'X-RateLimit-Remaining', 'X-RateLimit-Reset', 'Content-Type']` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L38) |

---

### <a id='cors_resources'></a>`CORS_RESOURCES`
| **Description** | Dictionary for configuring CORS for endpoints.     See Flask-CORS for further details.  .. note:: Ov... |
|--------------|-----------|
| **Default Value** | `'*'` |
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L18) |

---

### <a id='cors_send_wildcard'></a>`CORS_SEND_WILDCARD`
| **Description** | Sending wildcard CORS header.  .. note:: Overwrites    `Flask-CORS    <https://flask-cors.readthedoc... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L29) |

---

### <a id='cover_template'></a>`COVER_TEMPLATE`
| **Description** | Cover page template normally used e.g. for login and sign up pages. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_cover.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L38); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L273) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='crossref_additional_prefixes'></a>`CROSSREF_ADDITIONAL_PREFIXES`
| **Description** | List of additional Crossref DOI prefixes supported for registration. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L724) |

---

### <a id='crossref_depositor'></a>`CROSSREF_DEPOSITOR`
| **Description** | Crossref depositor name. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L727) |

---

### <a id='crossref_email'></a>`CROSSREF_EMAIL`
| **Description** | Crossref depositor email. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L730) |

---

### <a id='crossref_enabled'></a>`CROSSREF_ENABLED`
| **Description** | Flag to enable/disable Crossref DOI registration. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L712) |

---

### <a id='crossref_format'></a>`CROSSREF_FORMAT`
| **Description** | A string used for formatting the DOI or a callable.  If set to a string, you can used ``{prefix}`` a... |
|--------------|-----------|
| **Default Value** | `'{prefix}/{id}'` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L739) |

---

### <a id='crossref_password'></a>`CROSSREF_PASSWORD`
| **Description** | Crossref password. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L718) |

---

### <a id='crossref_prefix'></a>`CROSSREF_PREFIX`
| **Description** | Crossref DOI prefix. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L721) |

---

### <a id='crossref_registrant'></a>`CROSSREF_REGISTRANT`
| **Description** | Crossref registrant. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L733) |

---

### <a id='crossref_test_mode'></a>`CROSSREF_TEST_MODE`
| **Description** | Crossref test mode enabled. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L736) |

---

### <a id='crossref_username'></a>`CROSSREF_USERNAME`
| **Description** | Crossref username. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L715) |

---

### <a id='csrf_allowed_chars'></a>`CSRF_ALLOWED_CHARS`
| **Default Value** | `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='csrf_cookie_name'></a>`CSRF_COOKIE_NAME`
| **Default Value** | `'csrftoken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='csrf_cookie_samesite'></a>`CSRF_COOKIE_SAMESITE`
| **Default Value** | `'Lax'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='csrf_force_secure_referer'></a>`CSRF_FORCE_SECURE_REFERER`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='csrf_header'></a>`CSRF_HEADER`
| **Default Value** | `'X-CSRFToken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='csrf_methods'></a>`CSRF_METHODS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

---

### <a id='csrf_secret_salt'></a>`CSRF_SECRET_SALT`
| **Default Value** | `'invenio-csrf-token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='csrf_token_expires_in'></a>`CSRF_TOKEN_EXPIRES_IN`
| **Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='csrf_token_grace_period'></a>`CSRF_TOKEN_GRACE_PERIOD`
| **Default Value** | `604800` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='csrf_token_length'></a>`CSRF_TOKEN_LENGTH`
| **Default Value** | `32` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='dashboard_record_create_url'></a>`DASHBOARD_RECORD_CREATE_URL`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui), [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='datacite_additional_prefixes'></a>`DATACITE_ADDITIONAL_PREFIXES`
| **Description** | List of additional DataCite DOI prefixes supported for registration. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L682) |

---

### <a id='datacite_datacenter_symbol'></a>`DATACITE_DATACENTER_SYMBOL`
| **Description** | DataCite data center symbol.  This is only required if you want your records to be harvestable (OAI-... |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L703) |

---

### <a id='datacite_enabled'></a>`DATACITE_ENABLED`
| **Description** | Flag to enable/disable DataCite DOI registration. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L670) |

---

### <a id='datacite_format'></a>`DATACITE_FORMAT`
| **Description** | A string used for formatting the DOI or a callable.  If set to a string, you can used ``{prefix}`` a... |
|--------------|-----------|
| **Default Value** | `'{prefix}/{id}'` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L688) |

---

### <a id='datacite_password'></a>`DATACITE_PASSWORD`
| **Description** | DataCite password. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L676) |

---

### <a id='datacite_prefix'></a>`DATACITE_PREFIX`
| **Description** | DataCite DOI prefix. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L679) |

---

### <a id='datacite_test_mode'></a>`DATACITE_TEST_MODE`
| **Description** | DataCite test mode enabled. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L685) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='datacite_username'></a>`DATACITE_USERNAME`
| **Description** | DataCite username. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L673) |

---

### <a id='db_versioning'></a>`DB_VERSIONING`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='db_versioning_user_model'></a>`DB_VERSIONING_USER_MODEL`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L597) |

---

### <a id='debug'></a>`DEBUG`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='debug_tb_intercept_redirects'></a>`DEBUG_TB_INTERCEPT_REDIRECTS`
| **Description** | Switches off incept of redirects by Flask-DebugToolbar. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L712) |

---

### <a id='deployment_version'></a>`DEPLOYMENT_VERSION`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='einfra'></a>`EINFRA`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_einfra_oidc`](api.html#oarepo_config.configure_einfra_oidc) |

---

### <a id='einfra_login_app'></a>`EINFRA_LOGIN_APP`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_einfra_oidc`](api.html#oarepo_config.configure_einfra_oidc) |

---

### <a id='explain_template_loading'></a>`EXPLAIN_TEMPLATE_LOADING`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='files_rest_allow_range_requests'></a>`FILES_REST_ALLOW_RANGE_REQUESTS`
| **Description** | Enable support for HTTP Range Requests. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L136) |

---

### <a id='files_rest_checksum_verification_uri_prefixes'></a>`FILES_REST_CHECKSUM_VERIFICATION_URI_PREFIXES`
| **Description** | URI prefixes of files their checksums should be verified |
|--------------|-----------|
| **Default Value** | `[]` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L348) |

---

### <a id='files_rest_default_max_file_size'></a>`FILES_REST_DEFAULT_MAX_FILE_SIZE`
| **Description** | Default maximum file size for a bucket in bytes. `None` if unlimited. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L48) |

---

### <a id='files_rest_default_quota_size'></a>`FILES_REST_DEFAULT_QUOTA_SIZE`
| **Description** | Default quota size for a bucket in bytes. `None` if unlimited. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L45) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='files_rest_default_storage_class'></a>`FILES_REST_DEFAULT_STORAGE_CLASS`
| **Description** | Default storage class. Must be one of `FILES_REST_STORAGE_CLASS_LIST`. |
|--------------|-----------|
| **Default Value** | `'S'` |
| **Type** | str |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L42); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L358) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='files_rest_file_tags_header'></a>`FILES_REST_FILE_TAGS_HEADER`
| **Description** | Header for updating file tags. |
|--------------|-----------|
| **Default Value** | `'X-Invenio-File-Tags'` |
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L129) |

---

### <a id='files_rest_file_uri_max_len'></a>`FILES_REST_FILE_URI_MAX_LEN`
| **Description** | Maximum length of the FileInstance.uri field.  .. warning::    Setting this variable to anything hig... |
|--------------|-----------|
| **Default Value** | `255` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L71) |

---

### <a id='files_rest_min_file_size'></a>`FILES_REST_MIN_FILE_SIZE`
| **Description** | Minimum file size when uploading, in bytes (do not allow empty files). |
|--------------|-----------|
| **Default Value** | `1` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L51) |

---

### <a id='files_rest_multipart_chunksize_max'></a>`FILES_REST_MULTIPART_CHUNKSIZE_MAX`
| **Description** | Maximum chunk size in bytes of multipart objects. |
|--------------|-----------|
| **Default Value** | `5368709120` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L117) |

---

### <a id='files_rest_multipart_chunksize_min'></a>`FILES_REST_MULTIPART_CHUNKSIZE_MIN`
| **Description** | Minimum chunk size in bytes of multipart objects. |
|--------------|-----------|
| **Default Value** | `5242880` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L114) |

---

### <a id='files_rest_multipart_expires'></a>`FILES_REST_MULTIPART_EXPIRES`
| **Description** | Time delta after which a multipart upload is considered expired. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=4)` |
| **Type** | timedelta |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L120) |

---

### <a id='files_rest_multipart_max_parts'></a>`FILES_REST_MULTIPART_MAX_PARTS`
| **Description** | Maximum number of parts when uploading files with multipart uploads. |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L111) |

---

### <a id='files_rest_multipart_part_factories'></a>`FILES_REST_MULTIPART_PART_FACTORIES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L93) |

---

### <a id='files_rest_object_key_max_len'></a>`FILES_REST_OBJECT_KEY_MAX_LEN`
| **Description** | Maximum length of the ObjectVersion.key field.  .. warning::    Setting this variable to anything hi... |
|--------------|-----------|
| **Default Value** | `255` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L63) |

---

### <a id='files_rest_permission_factory'></a>`FILES_REST_PERMISSION_FACTORY`
| **Description** | Permission factory to control the files access from the REST interface. |
|--------------|-----------|
| **Default Value** | `'invenio_files_rest.permissions.permission_factory'` |
| **Type** | str |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L60); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L345) |

---

### <a id='files_rest_size_limiters'></a>`FILES_REST_SIZE_LIMITERS`
| **Description** | Import path of file size limiters factory to control bucket size limits. |
|--------------|-----------|
| **Default Value** | `'invenio_files_rest.limiters.file_size_limiters'` |
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L54) |

---

### <a id='files_rest_storage_class_list'></a>`FILES_REST_STORAGE_CLASS_LIST`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L31); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L352) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='files_rest_storage_factory'></a>`FILES_REST_STORAGE_FACTORY`
| **Description** | Import path of factory used to create a storage instance. |
|--------------|-----------|
| **Default Value** | `'invenio_files_rest.storage.pyfs_storage_factory'` |
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L57) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='files_rest_storage_path_dimensions'></a>`FILES_REST_STORAGE_PATH_DIMENSIONS`
| **Description** | Number of directory levels created when generating the path of a file.     For example, if split len... |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L86) |

---

### <a id='files_rest_storage_path_split_length'></a>`FILES_REST_STORAGE_PATH_SPLIT_LENGTH`
| **Description** | Number of chars to use as folder name when generating the path of a file.     For example, if split ... |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L79) |

---

### <a id='files_rest_task_wait_interval'></a>`FILES_REST_TASK_WAIT_INTERVAL`
| **Description** | Interval in seconds between sending a whitespace to not close connection. |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L123) |

---

### <a id='files_rest_task_wait_max_seconds'></a>`FILES_REST_TASK_WAIT_MAX_SECONDS`
| **Description** | Maximum number of seconds to wait for a task to finish. |
|--------------|-----------|
| **Default Value** | `600` |
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L126) |

---

### <a id='files_rest_upload_factories'></a>`FILES_REST_UPLOAD_FACTORIES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L99) |

---

### <a id='files_rest_xsendfile_enabled'></a>`FILES_REST_XSENDFILE_ENABLED`
| **Description** | Use the X-Accel-Redirect header to stream the file through a reverse proxy(     e.g NGINX). |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L132) |

---

### <a id='files_rest_xsendfile_response_func'></a>`FILES_REST_XSENDFILE_RESPONSE_FUNC`
| **Description** | Function for the creation of a file streaming redirect response. |
|--------------|-----------|
| **Default Value** | `create_file_streaming_redirect_response` |
| **Type** | unknown |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L139) |

---

### <a id='formatter_badges_allowed_titles'></a>`FORMATTER_BADGES_ALLOWED_TITLES`
| **Description** | List of allowed titles in badges. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L363); [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L11) |

---

### <a id='formatter_badges_enable'></a>`FORMATTER_BADGES_ENABLE`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='formatter_badges_max_cache_age'></a>`FORMATTER_BADGES_MAX_CACHE_AGE`
| **Description** | The maximum amount of time a badge will be considered fresh. |
|--------------|-----------|
| **Default Value** | `0` |
| **Type** | int |
| **Source** | [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L17) |

---

### <a id='formatter_badges_title_mapping'></a>`FORMATTER_BADGES_TITLE_MAPPING`
| **Description** | Mapping of titles. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L366); [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L14) |

---

### <a id='global_search_models'></a>`GLOBAL_SEARCH_MODELS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`add_model`](api.html#oarepo_config.add_model) |

---

### <a id='header_template'></a>`HEADER_TEMPLATE`
| **Description** | Base header template to be extended on custom headers. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/header.html'` |
| **Type** | unknown |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L23) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='i18n_default_redirect_endpoint'></a>`I18N_DEFAULT_REDIRECT_ENDPOINT`
| **Description** | Endpoint to redirect if no next parameter is provided. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L41) |

---

### <a id='i18n_js_distr_exceptional_package_map'></a>`I18N_JS_DISTR_EXCEPTIONAL_PACKAGE_MAP`
| **Description** | Exceptional package name mapper for JS/React localization distribution.  Webpack entrypoints are use... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L53) |

---

### <a id='i18n_languages'></a>`I18N_LANGUAGES`
| **Description** | List of tuples of available languages.  Example configuration with english and danish with english a... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L21) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='i18n_session_key'></a>`I18N_SESSION_KEY`
| **Description** | Key to retrieve language identifier from the current session object. |
|--------------|-----------|
| **Default Value** | `'language'` |
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L44) |

---

### <a id='i18n_set_language_url'></a>`I18N_SET_LANGUAGE_URL`
| **Description** | URL prefix for set language view.  Set to ``None`` to prevent view from being installed. |
|--------------|-----------|
| **Default Value** | `'/lang'` |
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L35) |

---

### <a id='i18n_transifex_js_resources_map'></a>`I18N_TRANSIFEX_JS_RESOURCES_MAP`
| **Description** | Mapping of transifex resource names to invenioRDM package names.  All resources/packages that should... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L61) |

---

### <a id='i18n_translations_paths'></a>`I18N_TRANSLATIONS_PATHS`
| **Description** | List of paths to load message catalogs from. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L18) |

---

### <a id='i18n_user_lang_attr'></a>`I18N_USER_LANG_ATTR`
| **Description** | Attribute name which contains language identifier on the User object.  It is used only when the logi... |
|--------------|-----------|
| **Default Value** | `'prefered_language'` |
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L47) |

---

### <a id='iiif_api_decorator_handler'></a>`IIIF_API_DECORATOR_HANDLER`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1144) |

---

### <a id='iiif_api_info_response_skeleton'></a>`IIIF_API_INFO_RESPONSE_SKELETON`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='iiif_cache_handler'></a>`IIIF_CACHE_HANDLER`
| **Default Value** | `'flask_iiif.cache.simple:ImageSimpleCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='iiif_cache_ignore_errors'></a>`IIIF_CACHE_IGNORE_ERRORS`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='iiif_cache_redis_url'></a>`IIIF_CACHE_REDIS_URL`
| **Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='iiif_cache_time'></a>`IIIF_CACHE_TIME`
| **Default Value** | `172800` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='iiif_converters'></a>`IIIF_CONVERTERS`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='iiif_formats'></a>`IIIF_FORMATS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1152) |

---

### <a id='iiif_formats_pil_map'></a>`IIIF_FORMATS_PIL_MAP`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1164) |

---

### <a id='iiif_gif_temp_folder_path'></a>`IIIF_GIF_TEMP_FOLDER_PATH`
| **Default Value** | `'/tmp'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='iiif_mode'></a>`IIIF_MODE`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='iiif_preview_template'></a>`IIIF_PREVIEW_TEMPLATE`
| **Description** | Template for IIIF image preview. |
|--------------|-----------|
| **Default Value** | `'invenio_app_rdm/records/iiif_preview.html'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1141) |

---

### <a id='iiif_qualities'></a>`IIIF_QUALITIES`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='iiif_simple_previewer_native_extensions'></a>`IIIF_SIMPLE_PREVIEWER_NATIVE_EXTENSIONS`
| **Description** | Images are converted to JPEG for preview, unless listed here. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1146) |

---

### <a id='iiif_simple_previewer_size'></a>`IIIF_SIMPLE_PREVIEWER_SIZE`
| **Description** | Size of image in IIIF preview window. Must be a valid IIIF Image API size parameter. |
|--------------|-----------|
| **Default Value** | `'!800,800'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1149) |

---

### <a id='iiif_tiles_converter_params'></a>`IIIF_TILES_CONVERTER_PARAMS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L939) |

---

### <a id='iiif_tiles_generation_enabled'></a>`IIIF_TILES_GENERATION_ENABLED`
| **Description** | Enable generating pyramidal TIFF tiles for uploaded images. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L918) |

---

### <a id='iiif_tiles_storage_base_path'></a>`IIIF_TILES_STORAGE_BASE_PATH`
| **Description** | Base path for storing IIIF tiles.  Relative paths are resolved against the application instance path... |
|--------------|-----------|
| **Default Value** | `'images/'` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L933) |

---

### <a id='iiif_tiles_valid_extensions'></a>`IIIF_TILES_VALID_EXTENSIONS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L921) |

---

### <a id='iiif_validations'></a>`IIIF_VALIDATIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='indexer_before_index_hooks'></a>`INDEXER_BEFORE_INDEX_HOOKS`
| **Description** | List of automatically connected hooks (function or importable string). |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L59) |

---

### <a id='indexer_bulk_request_timeout'></a>`INDEXER_BULK_REQUEST_TIMEOUT`
| **Description** | Request timeout to use in Bulk indexing. |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L46) |

---

### <a id='indexer_default_index'></a>`INDEXER_DEFAULT_INDEX`
| **Description** | Default index to use if no schema is defined. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L13) |

---

### <a id='indexer_max_bulk_consumers'></a>`INDEXER_MAX_BULK_CONSUMERS`
| **Description** | Maximum number of concurrent consumers for bulk indexing.  This threshold is applied per queue, so e... |
|--------------|-----------|
| **Default Value** | `5` |
| **Type** | int |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L49) |

---

### <a id='indexer_mq_exchange'></a>`INDEXER_MQ_EXCHANGE`
| **Description** | Default exchange for message queue. |
|--------------|-----------|
| **Default Value** | `Exchange('indexer', type='direct')` |
| **Type** | unknown |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L16) |

---

### <a id='indexer_mq_publish_kwargs'></a>`INDEXER_MQ_PUBLISH_KWARGS`
| **Description** | Default message queue producer publishing kwargs.  Passed to ``kombu.Producer:publish``.  .. code-bl... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L25) |

---

### <a id='indexer_mq_queue'></a>`INDEXER_MQ_QUEUE`
| **Description** | Default queue for message queue. |
|--------------|-----------|
| **Default Value** | `Queue('indexer', exchange=INDEXER_MQ_EXCHANGE, routing_key='indexer')` |
| **Type** | unknown |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L19) |

---

### <a id='indexer_mq_routing_key'></a>`INDEXER_MQ_ROUTING_KEY`
| **Description** | Default routing key for message queue. |
|--------------|-----------|
| **Default Value** | `'indexer'` |
| **Type** | str |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L22) |

---

### <a id='indexer_record_to_index'></a>`INDEXER_RECORD_TO_INDEX`
| **Description** | Provide an implementation of record_to_index function |
|--------------|-----------|
| **Default Value** | `'invenio_indexer.utils.default_record_to_index'` |
| **Type** | str |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L56) |

---

### <a id='indexer_replace_refs'></a>`INDEXER_REPLACE_REFS`
| **Description** | Whether to replace JSONRefs prior to indexing record. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L43) |

---

### <a id='instance_theme_file'></a>`INSTANCE_THEME_FILE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='invenio_cache_type'></a>`INVENIO_CACHE_TYPE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='invenio_rdm_enabled'></a>`INVENIO_RDM_ENABLED`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='invenio_vocabulary_type_metadata'></a>`INVENIO_VOCABULARY_TYPE_METADATA`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_vocabulary`](api.html#oarepo_config.configure_vocabulary) |

---

### <a id='javascript_packages_manager'></a>`JAVASCRIPT_PACKAGES_MANAGER`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='jobs_default_queue'></a>`JOBS_DEFAULT_QUEUE`
| **Description** | Default Celery queue. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L53) |

---

### <a id='jobs_facets'></a>`JOBS_FACETS`
| **Description** | Facets/aggregations for Jobs results. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L32) |

---

### <a id='jobs_logging'></a>`JOBS_LOGGING`
| **Description** | Enable logging for jobs. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L85) |

---

### <a id='jobs_logging_index'></a>`JOBS_LOGGING_INDEX`
| **Description** | "Index name for job logs. |
|--------------|-----------|
| **Default Value** | `'job-logs'` |
| **Type** | str |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L88) |

---

### <a id='jobs_logging_level'></a>`JOBS_LOGGING_LEVEL`
| **Description** | Logging level for jobs. |
|--------------|-----------|
| **Default Value** | `'DEBUG'` |
| **Type** | str |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L82) |
| **Set by** | [`configure_jobs`](api.html#oarepo_config.configure_jobs) |

---

### <a id='jobs_logging_retention_days'></a>`JOBS_LOGGING_RETENTION_DAYS`
| **Description** | Retention period for job logs in days. |
|--------------|-----------|
| **Default Value** | `90` |
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L91) |

---

### <a id='jobs_logs_batch_size'></a>`JOBS_LOGS_BATCH_SIZE`
| **Description** | Number of log results to fetch per batch from the search backend. |
|--------------|-----------|
| **Default Value** | `500` |
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L97) |

---

### <a id='jobs_logs_max_results'></a>`JOBS_LOGS_MAX_RESULTS`
| **Description** | Maximum total number of log results to return in a single search request. |
|--------------|-----------|
| **Default Value** | `2000` |
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L94) |

---

### <a id='jobs_permission_policy'></a>`JOBS_PERMISSION_POLICY`
| **Description** | Permission policy for jobs. |
|--------------|-----------|
| **Default Value** | `JobPermissionPolicy` |
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L23) |

---

### <a id='jobs_queues'></a>`JOBS_QUEUES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L35) |

---

### <a id='jobs_runs_permission_policy'></a>`JOBS_RUNS_PERMISSION_POLICY`
| **Description** | Permission policy for job runs. |
|--------------|-----------|
| **Default Value** | `RunPermissionPolicy` |
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L26) |

---

### <a id='jobs_search'></a>`JOBS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L76) |

---

### <a id='jobs_sort_options'></a>`JOBS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L56) |

---

### <a id='jobs_tasks_permission_policy'></a>`JOBS_TASKS_PERMISSION_POLICY`
| **Description** | Permission policy for tasks. |
|--------------|-----------|
| **Default Value** | `TasksPermissionPolicy` |
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L20) |

---

### <a id='jsonschemas_endpoint'></a>`JSONSCHEMAS_ENDPOINT`
| **Description** | Default schema endpoint. |
|--------------|-----------|
| **Default Value** | `'/schemas'` |
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L14) |

---

### <a id='jsonschemas_host'></a>`JSONSCHEMAS_HOST`
| **Description** | Default json schema host. |
|--------------|-----------|
| **Default Value** | `'localhost'` |
| **Type** | str |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L11); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L609) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='jsonschemas_loader_cls'></a>`JSONSCHEMAS_LOADER_CLS`
| **Description** | Loader class used in ``JSONRef`` when replacing ``$ref``. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L31) |

---

### <a id='jsonschemas_local_refresolver_uri_scheme'></a>`JSONSCHEMAS_LOCAL_REFRESOLVER_URI_SCHEME`
| **Description** | Non-standard URI scheme to reference local schemas. |
|--------------|-----------|
| **Default Value** | `'local://'` |
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L70) |

---

### <a id='jsonschemas_register_endpoints_api'></a>`JSONSCHEMAS_REGISTER_ENDPOINTS_API`
| **Description** | Register the endpoints on the API app. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L42); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L603) |

---

### <a id='jsonschemas_register_endpoints_ui'></a>`JSONSCHEMAS_REGISTER_ENDPOINTS_UI`
| **Description** | Register the endpoints on the UI app. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L45); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L606) |

---

### <a id='jsonschemas_replace_refs'></a>`JSONSCHEMAS_REPLACE_REFS`
| **Description** | Whether to resolve $ref before serving a schema. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L20) |

---

### <a id='jsonschemas_resolver_cls'></a>`JSONSCHEMAS_RESOLVER_CLS`
| **Description** | Resolver used to resolve the schema.  if :py:const:`invenio_jsonschemas.config.JSONSCHEMAS_RESOLVE_S... |
|--------------|-----------|
| **Default Value** | `'invenio_jsonschemas.utils.resolve_schema'` |
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L34) |

---

### <a id='jsonschemas_resolve_schema'></a>`JSONSCHEMAS_RESOLVE_SCHEMA`
| **Description** | Whether to resolve schema using the Resolver Class.  If is ``True``, will replace $ref and run the :... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L23) |

---

### <a id='jsonschemas_schemas'></a>`JSONSCHEMAS_SCHEMAS`
| **Description** | List of entrypoint names to register JSON Schemas for.  If `None`, all JSON Schemas defined through ... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L48) |

---

### <a id='jsonschemas_url_scheme'></a>`JSONSCHEMAS_URL_SCHEME`
| **Description** | Default url scheme for schemas. |
|--------------|-----------|
| **Default Value** | `'https'` |
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L17) |

---

### <a id='logging_console'></a>`LOGGING_CONSOLE`
| **Description** | Enable logging to the console. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L27) |

---

### <a id='logging_console_level'></a>`LOGGING_CONSOLE_LEVEL`
| **Description** | Console logging level.  Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``, `... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L37) |

---

### <a id='logging_console_pywarnings'></a>`LOGGING_CONSOLE_PYWARNINGS`
| **Description** | Enable logging of Python warnings to the console.  By default, warnings are logged to the console if... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L30) |

---

### <a id='logging_fs_backupcount'></a>`LOGGING_FS_BACKUPCOUNT`
| **Description** | Number of rotated log files to keep. |
|--------------|-----------|
| **Default Value** | `5` |
| **Type** | int |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L54) |

---

### <a id='logging_fs_level'></a>`LOGGING_FS_LEVEL`
| **Description** | Filesystem logging level.  Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``... |
|--------------|-----------|
| **Default Value** | `'WARNING'` |
| **Type** | str |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L60) |

---

### <a id='logging_fs_logfile'></a>`LOGGING_FS_LOGFILE`
| **Description** | Enable logging to the filesystem. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L48) |

---

### <a id='logging_fs_maxbytes'></a>`LOGGING_FS_MAXBYTES`
| **Description** | Maximum size of logging file. Default: 100MB. |
|--------------|-----------|
| **Default Value** | `104857600` |
| **Type** | int |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L57) |

---

### <a id='logging_fs_pywarnings'></a>`LOGGING_FS_PYWARNINGS`
| **Description** | Enable logging of Python warnings to filesystem logging. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L51) |

---

### <a id='logging_sentry_celery'></a>`LOGGING_SENTRY_CELERY`
| **Description** | Configure Celery to send logging to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L81) |

---

### <a id='logging_sentry_class'></a>`LOGGING_SENTRY_CLASS`
| **Description** | Import path of sentry Flask extension class.  This allows you to customize the Sentry extension clas... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L90) |

---

### <a id='logging_sentry_init_kwargs'></a>`LOGGING_SENTRY_INIT_KWARGS`
| **Description** | Pass extra options when initializing Sentry instance. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L95) |

---

### <a id='logging_sentry_level'></a>`LOGGING_SENTRY_LEVEL`
| **Description** | Sentry logging level.  Defaults to only reporting errors and warnings. |
|--------------|-----------|
| **Default Value** | `'WARNING'` |
| **Type** | str |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L72) |

---

### <a id='logging_sentry_pywarnings'></a>`LOGGING_SENTRY_PYWARNINGS`
| **Description** | Enable logging of Python warnings to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L78) |

---

### <a id='logging_sentry_redis'></a>`LOGGING_SENTRY_REDIS`
| **Description** | Configure REDIS to send logging to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L87) |

---

### <a id='logging_sentry_sqlalchemy'></a>`LOGGING_SENTRY_SQLALCHEMY`
| **Description** | Configure SQL Alchemy to send logging to Sentry. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L84) |

---

### <a id='mail_debug'></a>`MAIL_DEBUG`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='mail_default_reply_to'></a>`MAIL_DEFAULT_REPLY_TO`
| **Description** | Reply to mail address for e-mails. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L19) |

---

### <a id='mail_default_sender'></a>`MAIL_DEFAULT_SENDER`
| **Description** | Email address used as sender of account registration emails.  `SECURITY_EMAIL_SENDER` will default t... |
|--------------|-----------|
| **Default Value** | `'info@inveniosoftware.org'` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L376) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='mail_max_attachment_size'></a>`MAIL_MAX_ATTACHMENT_SIZE`
| **Description** | Max size of inline attachments, in bytes. |
|--------------|-----------|
| **Default Value** | `1000000` |
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L22) |

---

### <a id='mail_max_retries'></a>`MAIL_MAX_RETRIES`
| **Description** | How often will we repeat if a problem occurred. |
|--------------|-----------|
| **Default Value** | `2` |
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L25) |

---

### <a id='mail_min_logging_level'></a>`MAIL_MIN_LOGGING_LEVEL`
| **Description** | Minimum logging level for the mail logger. |
|--------------|-----------|
| **Default Value** | `40` |
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L28) |

---

### <a id='mail_suppress_send'></a>`MAIL_SUPPRESS_SEND`
| **Description** | Disable email sending by default. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L373) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='matomo_analytics_site_id'></a>`MATOMO_ANALYTICS_SITE_ID`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='matomo_analytics_template'></a>`MATOMO_ANALYTICS_TEMPLATE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='matomo_analytics_url'></a>`MATOMO_ANALYTICS_URL`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='max_content_length'></a>`MAX_CONTENT_LENGTH`
| **Description** | Maximum allowed content length for form data.  This value limits the maximum file upload size via mu... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L15); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L214) |

---

### <a id='max_cookie_size'></a>`MAX_COOKIE_SIZE`
| **Default Value** | `4093` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='max_form_memory_size'></a>`MAX_FORM_MEMORY_SIZE`
| **Default Value** | `500000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='max_form_parts'></a>`MAX_FORM_PARTS`
| **Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='multiprofiler_base_template'></a>`MULTIPROFILER_BASE_TEMPLATE`
| **Description** | Base template for the profiler page. |
|--------------|-----------|
| **Default Value** | `'flask_multiprofiler/index.html'` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1620) |

---

### <a id='multiprofiler_ignored_endpoints'></a>`MULTIPROFILER_IGNORED_ENDPOINTS`
| **Default Value** | `['static', '_debug_toolbar.static', 'profiler\\..+', 'invenio_formatter_badges.badge']` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1623) |

---

### <a id='multiprofiler_permission'></a>`MULTIPROFILER_PERMISSION`
| **Description** | Function to check for permissions to access the profiler. |
|--------------|-----------|
| **Default Value** | `administration_permission.can` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1631) |

---

### <a id='notifications_backends'></a>`NOTIFICATIONS_BACKENDS`
| **Description** | Notification backends.  .. code-block::python      NOTIFICATIONS_BACKENDS = {         "email": Email... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L12); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1426) |

---

### <a id='notifications_builders'></a>`NOTIFICATIONS_BUILDERS`
| **Description** | Notification builders.  .. code-block::python      NOTIFICATIONS_BUILDERS = {         "community_sub... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L24); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1432) |

---

### <a id='notifications_entity_resolvers'></a>`NOTIFICATIONS_ENTITY_RESOLVERS`
| **Description** | List of entity resolvers used by notification builders.  .. code-block::python      NOTIFICATIONS_EN... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L40); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1485) |

---

### <a id='notifications_group_email_domain'></a>`NOTIFICATIONS_GROUP_EMAIL_DOMAIN`
| **Description** | Domain suffix to append to group names when email is not provided.  When a recipient is a group and ... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L61) |

---

### <a id='notifications_settings_view_function'></a>`NOTIFICATIONS_SETTINGS_VIEW_FUNCTION`
| **Description** | View function for notification settings.  This should be set higher up in the module hierarchy (e.g.... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L54); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1496) |

---

### <a id='oaiserver_admin_emails'></a>`OAISERVER_ADMIN_EMAILS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L37) |

---

### <a id='oaiserver_base_template'></a>`OAISERVER_BASE_TEMPLATE`
| **Default Value** | `'invenio_oaiserver/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oaiserver_cache_key'></a>`OAISERVER_CACHE_KEY`
| **Description** | Key prefix added before all keys in cache server. |
|--------------|-----------|
| **Default Value** | `'DynamicOAISets::'` |
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L162) |

---

### <a id='oaiserver_celery_task_chunk_size'></a>`OAISERVER_CELERY_TASK_CHUNK_SIZE`
| **Description** | Specify the maximum number of records each task will update. |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L165) |

---

### <a id='oaiserver_compressions'></a>`OAISERVER_COMPRESSIONS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L46) |

---

### <a id='oaiserver_control_number_fetcher'></a>`OAISERVER_CONTROL_NUMBER_FETCHER`
| **Description** | PIDStore fetcher for the OAI ID control number. |
|--------------|-----------|
| **Default Value** | `'recid'` |
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L168) |

---

### <a id='oaiserver_created_key'></a>`OAISERVER_CREATED_KEY`
| **Description** | Record created key. |
|--------------|-----------|
| **Default Value** | `'created'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L688); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L132) |

---

### <a id='oaiserver_delete_percolator_function'></a>`OAISERVER_DELETE_PERCOLATOR_FUNCTION`
| **Default Value** | `'invenio_oaiserver.percolator:_delete_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L113) |

---

### <a id='oaiserver_descriptions'></a>`OAISERVER_DESCRIPTIONS`
| **Description** | Specify the optional description containers that can be used to express properties of the repository... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L171) |

---

### <a id='oaiserver_getrecord_fetcher'></a>`OAISERVER_GETRECORD_FETCHER`
| **Description** | Record data fetcher for serialization. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.oai:getrecord_fetcher'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L703); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L153) |

---

### <a id='oaiserver_granularity'></a>`OAISERVER_GRANULARITY`
| **Description** | The finest harvesting granularity supported by the repository.  The legitimate values are ``YYYY-MM-... |
|--------------|-----------|
| **Default Value** | `'YYYY-MM-DDThh:mm:ssZ'` |
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L50) |

---

### <a id='oaiserver_id_fetcher'></a>`OAISERVER_ID_FETCHER`
| **Description** | OAI ID fetcher function. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.oai:oaiid_fetcher'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L639); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L126) |

---

### <a id='oaiserver_id_prefix'></a>`OAISERVER_ID_PREFIX`
| **Description** | The prefix that will be applied to the generated OAI-PMH ids. |
|--------------|-----------|
| **Default Value** | `'oai:Mac.localdomain:'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L633); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L24) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='oaiserver_last_update_key'></a>`OAISERVER_LAST_UPDATE_KEY`
| **Description** | Record update key. |
|--------------|-----------|
| **Default Value** | `'updated'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L685); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L129) |

---

### <a id='oaiserver_metadata_formats'></a>`OAISERVER_METADATA_FORMATS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L642); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L70) |

---

### <a id='oaiserver_new_percolator_function'></a>`OAISERVER_NEW_PERCOLATOR_FUNCTION`
| **Default Value** | `'invenio_oaiserver.percolator:_new_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L111) |

---

### <a id='oaiserver_page_size'></a>`OAISERVER_PAGE_SIZE`
| **Description** | Define maximum length of list responses.  Request with verbs ``ListRecords``, ``ListIdentifiers``, a... |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L17) |

---

### <a id='oaiserver_percolator_dedicated_index'></a>`OAISERVER_PERCOLATOR_DEDICATED_INDEX`
| **Description** | Create a dedicated index for the percolators, instead of storing them in the same index as the recor... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L141) |

---

### <a id='oaiserver_protocol_version'></a>`OAISERVER_PROTOCOL_VERSION`
| **Default Value** | `'2.0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L35) |

---

### <a id='oaiserver_query_parser'></a>`OAISERVER_QUERY_PARSER`
| **Description** | Define query parser for OIASet definition. |
|--------------|-----------|
| **Default Value** | `invenio_search.engine.dsl.Q` |
| **Type** | unknown |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L156) |

---

### <a id='oaiserver_query_parser_fields'></a>`OAISERVER_QUERY_PARSER_FIELDS`
| **Description** | Define query parser search fields list for OIASet definition. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L159) |

---

### <a id='oaiserver_record_cls'></a>`OAISERVER_RECORD_CLS`
| **Description** | Record retrieval class. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.records.api:RDMRecord'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L691); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L150) |

---

### <a id='oaiserver_record_index'></a>`OAISERVER_RECORD_INDEX`
| **Description** | Specify a search index with records that should be exposed via OAI-PMH. |
|--------------|-----------|
| **Default Value** | `'oaisource'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L697); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L31) |

---

### <a id='oaiserver_record_list_sets_fetcher'></a>`OAISERVER_RECORD_LIST_SETS_FETCHER`
| **Description** | Record's list OAI sets function. |
|--------------|-----------|
| **Default Value** | `'invenio_oaiserver.percolator:sets_search_all'` |
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L138) |

---

### <a id='oaiserver_record_sets_fetcher'></a>`OAISERVER_RECORD_SETS_FETCHER`
| **Description** | Record's OAI sets function. |
|--------------|-----------|
| **Default Value** | `'invenio_oaiserver.percolator:find_sets_for_record'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L694); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L135) |

---

### <a id='oaiserver_register_record_signals'></a>`OAISERVER_REGISTER_RECORD_SIGNALS`
| **Description** | Catch record/set insert/update/delete signals and update the `_oai` field. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L115) |

---

### <a id='oaiserver_register_set_signals'></a>`OAISERVER_REGISTER_SET_SIGNALS`
| **Description** | Catch set insert/update/delete signals and update the `_oai` record field. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L119) |

---

### <a id='oaiserver_repository_name'></a>`OAISERVER_REPOSITORY_NAME`
| **Default Value** | `'Invenio-OAIServer'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |
| **Set by** | [`configure_oai`](api.html#oarepo_config.configure_oai) |

---

### <a id='oaiserver_resumption_token_expire_time'></a>`OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME`
| **Description** | The expiration time of a resumption token in seconds.  **Default: 60 seconds = 1 minute**.  .. note:... |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L57) |

---

### <a id='oaiserver_search_cls'></a>`OAISERVER_SEARCH_CLS`
| **Description** | Class for record search. |
|--------------|-----------|
| **Default Value** | `'invenio_rdm_records.oai:OAIRecordSearch'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L636); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L123) |

---

### <a id='oaiserver_set_records_query_fetcher'></a>`OAISERVER_SET_RECORDS_QUERY_FETCHER`
| **Default Value** | `'invenio_oaiserver.fetchers:set_records_query_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L146) |

---

### <a id='oaiserver_xsl_url'></a>`OAISERVER_XSL_URL`
| **Description** | Specify the url (relative or absolute) to the XML Stylesheet file to transform XML OAI 2.0 responses... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L222) |

---

### <a id='oauth2server_allowed_grant_types'></a>`OAUTH2SERVER_ALLOWED_GRANT_TYPES`
| **Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L27) |

---

### <a id='oauth2server_allowed_response_types'></a>`OAUTH2SERVER_ALLOWED_RESPONSE_TYPES`
| **Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L40) |

---

### <a id='oauth2server_allowed_urlencode_characters'></a>`OAUTH2SERVER_ALLOWED_URLENCODE_CHARACTERS`
| **Description** | A string of special characters that should be valid inside a query string.  .. seealso::      See :p... |
|--------------|-----------|
| **Default Value** | `'=&;:%+~,*@!()/?'` |
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L52) |

---

### <a id='oauth2server_base_template'></a>`OAUTH2SERVER_BASE_TEMPLATE`
| **Default Value** | `'invenio_oauth2server/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oauth2server_client_id_salt_len'></a>`OAUTH2SERVER_CLIENT_ID_SALT_LEN`
| **Description** | Length of client id. |
|--------------|-----------|
| **Default Value** | `40` |
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L18) |

---

### <a id='oauth2server_client_secret_salt_len'></a>`OAUTH2SERVER_CLIENT_SECRET_SALT_LEN`
| **Description** | Length of the client secret. |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L21) |

---

### <a id='oauth2server_cover_template'></a>`OAUTH2SERVER_COVER_TEMPLATE`
| **Default Value** | `'invenio_oauth2server/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oauth2server_jwt_auth_header'></a>`OAUTH2SERVER_JWT_AUTH_HEADER`
| **Description** | Header for the JWT.  .. note::      Authorization: Bearer xxx |
|--------------|-----------|
| **Default Value** | `'Authorization'` |
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L62) |

---

### <a id='oauth2server_jwt_auth_header_type'></a>`OAUTH2SERVER_JWT_AUTH_HEADER_TYPE`
| **Description** | Header Authorization type.  .. note::      By default the authorization type is ``Bearer`` as recomm... |
|--------------|-----------|
| **Default Value** | `'Bearer'` |
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L70) |

---

### <a id='oauth2server_jwt_verification_factory'></a>`OAUTH2SERVER_JWT_VERIFICATION_FACTORY`
| **Description** | Import path of factory used to verify JWT.  The ``request.headers`` should be passed as parameter. |
|--------------|-----------|
| **Default Value** | `'invenio_oauth2server.utils:jwt_verify_token'` |
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L79) |

---

### <a id='oauth2server_settings_template'></a>`OAUTH2SERVER_SETTINGS_TEMPLATE`
| **Default Value** | `'invenio_oauth2server/settings/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oauth2server_token_personal_salt_len'></a>`OAUTH2SERVER_TOKEN_PERSONAL_SALT_LEN`
| **Description** | Length of the personal access token. |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L24) |

---

### <a id='oauth2_cache_type'></a>`OAUTH2_CACHE_TYPE`
| **Description** | Type of cache to use for storing the temporary grant token. |
|--------------|-----------|
| **Default Value** | `'redis'` |
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L12) |

---

### <a id='oauth2_provider_error_endpoint'></a>`OAUTH2_PROVIDER_ERROR_ENDPOINT`
| **Description** | Error view endpoint. |
|--------------|-----------|
| **Default Value** | `'invenio_oauth2server.errors'` |
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L15) |

---

### <a id='oauthclient_auto_redirect_to_external_login'></a>`OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN`
| **Description** | Redirect to the only external login service under specific conditions.  If this option is enabled an... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L352) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='oauthclient_base_template'></a>`OAUTHCLIENT_BASE_TEMPLATE`
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oauthclient_cover_template'></a>`OAUTHCLIENT_COVER_TEMPLATE`
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oauthclient_login_user_template_parent'></a>`OAUTHCLIENT_LOGIN_USER_TEMPLATE_PARENT`
| **Default Value** | `'invenio_accounts/login_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oauthclient_remote_apps'></a>`OAUTHCLIENT_REMOTE_APPS`
| **Description** | Configuration of remote applications. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L325) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters), [`configure_einfra_oidc`](api.html#oarepo_config.configure_einfra_oidc) |

---

### <a id='oauthclient_rest_default_error_redirect_url'></a>`OAUTHCLIENT_REST_DEFAULT_ERROR_REDIRECT_URL`
| **Description** | Configuration of default error redirect URL. |
|--------------|-----------|
| **Default Value** | `'/'` |
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L346) |

---

### <a id='oauthclient_rest_default_response_handler'></a>`OAUTHCLIENT_REST_DEFAULT_RESPONSE_HANDLER`
| **Description** | Default REST response handler. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L349) |

---

### <a id='oauthclient_rest_remote_apps'></a>`OAUTHCLIENT_REST_REMOTE_APPS`
| **Description** | Configuration of remote rest applications. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L343) |

---

### <a id='oauthclient_session_key_prefix'></a>`OAUTHCLIENT_SESSION_KEY_PREFIX`
| **Description** | Session key prefix used when storing the access token for a remote app. |
|--------------|-----------|
| **Default Value** | `'oauth_token'` |
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L328) |

---

### <a id='oauthclient_settings_template'></a>`OAUTHCLIENT_SETTINGS_TEMPLATE`
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='oauthclient_signup_form'></a>`OAUTHCLIENT_SIGNUP_FORM`
| **Description** | Function called to render the sign up form after authorization succeeded. |
|--------------|-----------|
| **Default Value** | `_create_registrationform` |
| **Type** | unknown |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L337) |

---

### <a id='oauthclient_signup_template'></a>`OAUTHCLIENT_SIGNUP_TEMPLATE`
| **Description** | Template for the signup page. |
|--------------|-----------|
| **Default Value** | `'invenio_oauthclient/signup.html'` |
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L340) |

---

### <a id='oauthclient_sitename'></a>`OAUTHCLIENT_SITENAME`
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | unknown |

---

### <a id='oauthclient_state_enabled'></a>`OAUTHCLIENT_STATE_ENABLED`
| **Description** | Internal variable used to disable state validation during tests. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L334) |

---

### <a id='oauthclient_state_expires'></a>`OAUTHCLIENT_STATE_EXPIRES`
| **Description** | Number of seconds after which the state token expires. |
|--------------|-----------|
| **Default Value** | `300` |
| **Type** | int |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L331) |

---

### <a id='oauthclient_token_expires_leeway'></a>`OAUTHCLIENT_TOKEN_EXPIRES_LEEWAY`
| **Description** | The number of seconds before the actual expiration of an access token from which it is considered ex... |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L361) |

---

### <a id='pages_allowed_extra_html_attrs'></a>`PAGES_ALLOWED_EXTRA_HTML_ATTRS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L61) |

---

### <a id='pages_allowed_extra_html_tags'></a>`PAGES_ALLOWED_EXTRA_HTML_TAGS`
| **Description** | Extend allowed HTML tags list for static pages content. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L58) |

---

### <a id='pages_base_template'></a>`PAGES_BASE_TEMPLATE`
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='pages_default_template'></a>`PAGES_DEFAULT_TEMPLATE`
| **Description** | Default template to render. |
|--------------|-----------|
| **Default Value** | `'invenio_pages/default.html'` |
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1223); [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L14) |

---

### <a id='pages_facets'></a>`PAGES_FACETS`
| **Description** | Available facets defined for this module. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L54) |

---

### <a id='pages_search'></a>`PAGES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L28) |

---

### <a id='pages_sort_options'></a>`PAGES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L34) |

---

### <a id='pages_templates'></a>`PAGES_TEMPLATES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1226); [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L17) |

---

### <a id='pages_whitelist_config_keys'></a>`PAGES_WHITELIST_CONFIG_KEYS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L23) |

---

### <a id='permanent_session_lifetime'></a>`PERMANENT_SESSION_LIFETIME`
| **Default Value** | `datetime.timedelta(days=31)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | unknown |

---

### <a id='pidstore_app_logger_handlers'></a>`PIDSTORE_APP_LOGGER_HANDLERS`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='pidstore_datacite_doi_prefix'></a>`PIDSTORE_DATACITE_DOI_PREFIX`
| **Description** | Provide a DOI prefix here. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L19) |

---

### <a id='pidstore_object_endpoints'></a>`PIDSTORE_OBJECT_ENDPOINTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='pidstore_recid_field'></a>`PIDSTORE_RECID_FIELD`
| **Description** | Default record id field inside the json data.  This name will be used by the fetcher, to retrieve th... |
|--------------|-----------|
| **Default Value** | `'control_number'` |
| **Type** | str |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L11) |

---

### <a id='pidstore_recordid_options'></a>`PIDSTORE_RECORDID_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L22) |

---

### <a id='preferred_url_scheme'></a>`PREFERRED_URL_SCHEME`
| **Default Value** | `'http'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='previewable_zip_previewer_native_extensions'></a>`PREVIEWABLE_ZIP_PREVIEWER_NATIVE_EXTENSIONS`
| **Description** | Extensions for previewable zip. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1176) |

---

### <a id='previewer_abstract_template'></a>`PREVIEWER_ABSTRACT_TEMPLATE`
| **Description** | Parent template used by the available previewers. |
|--------------|-----------|
| **Default Value** | `'invenio_previewer/abstract_previewer.html'` |
| **Type** | str |
| **Sources** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L72); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1199) |

---

### <a id='previewer_base_css_bundles'></a>`PREVIEWER_BASE_CSS_BUNDLES`
| **Description** | Basic bundle which includes Font-Awesome/Bootstrap. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L75) |

---

### <a id='previewer_base_js_bundles'></a>`PREVIEWER_BASE_JS_BUNDLES`
| **Description** | Basic bundle which includes Bootstrap/jQuery. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L78) |

---

### <a id='previewer_base_template'></a>`PREVIEWER_BASE_TEMPLATE`
| **Default Value** | `'invenio_previewer/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='previewer_chardet_bytes'></a>`PREVIEWER_CHARDET_BYTES`
| **Description** | Number of bytes to read for character encoding detection by `cchardet`. |
|--------------|-----------|
| **Default Value** | `1024` |
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L17) |

---

### <a id='previewer_chardet_confidence'></a>`PREVIEWER_CHARDET_CONFIDENCE`
| **Description** | Confidence threshold for character encoding detection by `cchardet`. |
|--------------|-----------|
| **Default Value** | `0.9` |
| **Type** | float |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L20) |

---

### <a id='previewer_container_item_preference'></a>`PREVIEWER_CONTAINER_ITEM_PREFERENCE`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1202) |

---

### <a id='previewer_csv_max_bytes'></a>`PREVIEWER_CSV_MAX_BYTES`
| **Description** | Maximum file size in bytes for CSV files. |
|--------------|-----------|
| **Default Value** | `104857600` |
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L32) |

---

### <a id='previewer_csv_sniffer_allowed_delimiters'></a>`PREVIEWER_CSV_SNIFFER_ALLOWED_DELIMITERS`
| **Description** | Allowed delimiter characters passed to the ``csv.Sniffer.sniff`` method. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L14) |

---

### <a id='previewer_csv_validation_bytes'></a>`PREVIEWER_CSV_VALIDATION_BYTES`
| **Description** | Number of bytes read by CSV previewer to validate the file. |
|--------------|-----------|
| **Default Value** | `1024` |
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L11) |

---

### <a id='previewer_max_file_size_bytes'></a>`PREVIEWER_MAX_FILE_SIZE_BYTES`
| **Description** | Maximum file size in bytes for JSON/XML files. |
|--------------|-----------|
| **Default Value** | `1048576` |
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L23) |

---

### <a id='previewer_max_image_size_bytes'></a>`PREVIEWER_MAX_IMAGE_SIZE_BYTES`
| **Description** | Maximum file size in bytes for image files. |
|--------------|-----------|
| **Default Value** | `524288.0` |
| **Type** | float |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L26) |

---

### <a id='previewer_pdf_js_document_init_params'></a>`PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS`
| **Description** | Additional DocumentInitParameters passed to pdfjsLib.getDocument().  See https://mozilla.github.io/p... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L41) |

---

### <a id='previewer_pdf_js_enable_scripting'></a>`PREVIEWER_PDF_JS_ENABLE_SCRIPTING`
| **Description** | Enable JavaScript execution in PDF files (disabled by default for security). |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L38) |

---

### <a id='previewer_preference'></a>`PREVIEWER_PREFERENCE`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L56); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1183) |

---

### <a id='previewer_record_file_facotry'></a>`PREVIEWER_RECORD_FILE_FACOTRY`
| **Description** | Factory for extracting files from records. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L81) |

---

### <a id='previewer_txt_max_bytes'></a>`PREVIEWER_TXT_MAX_BYTES`
| **Description** | Maximum number of .txt file bytes to preview before truncated. |
|--------------|-----------|
| **Default Value** | `1048576` |
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L29) |

---

### <a id='previewer_web_archive_range_requests'></a>`PREVIEWER_WEB_ARCHIVE_RANGE_REQUESTS`
| **Description** | Whether the file server supports range requests or not. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L84) |

---

### <a id='previewer_zip_max_files'></a>`PREVIEWER_ZIP_MAX_FILES`
| **Description** | Max number of files showed in the ZIP previewer. |
|--------------|-----------|
| **Default Value** | `1000` |
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L35) |

---

### <a id='propagate_exceptions'></a>`PROPAGATE_EXCEPTIONS`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='provide_automatic_options'></a>`PROVIDE_AUTOMATIC_OPTIONS`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='queues_broker_url'></a>`QUEUES_BROKER_URL`
| **Description** | Broker URL for queues.  If the variable is not configured it falls back to the default ``BROKER_URL`... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L13) |

---

### <a id='queues_connection_pool'></a>`QUEUES_CONNECTION_POOL`
| **Description** | Default queues connection pool. |
|--------------|-----------|
| **Default Value** | `get_connection_pool` |
| **Type** | unknown |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L21) |

---

### <a id='queues_definitions'></a>`QUEUES_DEFINITIONS`
| **Description** | Static queue definitions. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L24) |

---

### <a id='ratelimit_application'></a>`RATELIMIT_APPLICATION`
| **Description** | Global rate limit. |
|--------------|-----------|
| **Default Value** | `set_rate_limit` |
| **Type** | unknown |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L24) |

---

### <a id='ratelimit_authenticated_user'></a>`RATELIMIT_AUTHENTICATED_USER`
| **Description** | Rate limit for logged in users. |
|--------------|-----------|
| **Default Value** | `'5000 per hour;100 per minute'` |
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L91); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L239) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='ratelimit_enabled'></a>`RATELIMIT_ENABLED`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='ratelimit_guest_user'></a>`RATELIMIT_GUEST_USER`
| **Description** | Rate limit for non logged in users. |
|--------------|-----------|
| **Default Value** | `'1000 per hour;60 per minute'` |
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L94); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L241) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='ratelimit_headers_enabled'></a>`RATELIMIT_HEADERS_ENABLED`
| **Description** | Enable rate limit headers. (Default: ``True``) |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L37) |

---

### <a id='ratelimit_key_func'></a>`RATELIMIT_KEY_FUNC`
| **Description** | Define custom key function.  This config is not part of Flask-Limiter.  This function is used to gen... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L54) |

---

### <a id='ratelimit_per_endpoint'></a>`RATELIMIT_PER_ENDPOINT`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L68) |

---

### <a id='ratelimit_storage_uri'></a>`RATELIMIT_STORAGE_URI`
| **Description** | Storage backend to store rate-limiting information.      Memory is used by default if no value is pr... |
|--------------|-----------|
| **Default Value** | `'memory://'` |
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L40); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L235) |

---

### <a id='ratelimit_strategy'></a>`RATELIMIT_STRATEGY`
| **Description** | The rate limiting strategy to use.  The strategy used here is the most consistant but also expensive... |
|--------------|-----------|
| **Default Value** | `'moving-window'` |
| **Type** | str |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L27) |

---

### <a id='rdm_allow_external_doi_versioning'></a>`RDM_ALLOW_EXTERNAL_DOI_VERSIONING`
| **Description** | Allow records with external DOIs to be versioned. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L657) |

---

### <a id='rdm_allow_metadata_only_records'></a>`RDM_ALLOW_METADATA_ONLY_RECORDS`
| **Description** | Allow users to publish metadata-only records. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L164) |

---

### <a id='rdm_allow_owners_remove_community_from_record'></a>`RDM_ALLOW_OWNERS_REMOVE_COMMUNITY_FROM_RECORD`
| **Description** | Allow record owners to remove communities from records.  When set to False, only community curators,... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L324) |

---

### <a id='rdm_allow_restricted_records'></a>`RDM_ALLOW_RESTRICTED_RECORDS`
| **Description** | Allow users to set restricted/private records. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L173) |

---

### <a id='rdm_archive_download_enabled'></a>`RDM_ARCHIVE_DOWNLOAD_ENABLED`
| **Description** | Flag to enable/disable the all-in-one download endpoint. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L64) |

---

### <a id='rdm_citation_styles'></a>`RDM_CITATION_STYLES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1124) |

---

### <a id='rdm_citation_styles_default'></a>`RDM_CITATION_STYLES_DEFAULT`
| **Description** | Default citation style |
|--------------|-----------|
| **Default Value** | `'iso690-author-date-cs'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1134) |

---

### <a id='rdm_communities_routes'></a>`RDM_COMMUNITIES_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1102) |

---

### <a id='rdm_community_content_moderation_handlers'></a>`RDM_COMMUNITY_CONTENT_MODERATION_HANDLERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L863) |

---

### <a id='rdm_community_inclusion_request_cls'></a>`RDM_COMMUNITY_INCLUSION_REQUEST_CLS`
| **Description** | Request type for record inclusion requests. |
|--------------|-----------|
| **Default Value** | `CommunityInclusion` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L322) |

---

### <a id='rdm_community_required_to_publish'></a>`RDM_COMMUNITY_REQUIRED_TO_PUBLISH`
| **Description** | Enforces at least one community per record. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L320) |

---

### <a id='rdm_community_submission_request_cls'></a>`RDM_COMMUNITY_SUBMISSION_REQUEST_CLS`
| **Description** | Request type for community submission requests. |
|--------------|-----------|
| **Default Value** | `CommunitySubmission` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L155) |

---

### <a id='rdm_content_moderation_handlers'></a>`RDM_CONTENT_MODERATION_HANDLERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L858) |

---

### <a id='rdm_custom_fields'></a>`RDM_CUSTOM_FIELDS`
| **Description** | Records custom fields definition.  .. code-block:: python      [<custom-field-class-type>, <custom-f... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L775) |

---

### <a id='rdm_custom_fields_ui'></a>`RDM_CUSTOM_FIELDS_UI`
| **Description** | Upload form custom fields UI configuration.  Of the shape:  .. code-block:: python      [{         s... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L789) |

---

### <a id='rdm_datacite_dump_openaire_access_rights'></a>`RDM_DATACITE_DUMP_OPENAIRE_ACCESS_RIGHTS`
| **Description** | Flag to control dumping DataCite OpenAIRE access rights.  See https://guidelines.openaire.eu/en/late... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L896) |

---

### <a id='rdm_datacite_funder_identifiers_priority'></a>`RDM_DATACITE_FUNDER_IDENTIFIERS_PRIORITY`
| **Description** | Priority of funder identifiers types to be used for DataCite serialization. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L893) |

---

### <a id='rdm_default_files_enabled'></a>`RDM_DEFAULT_FILES_ENABLED`
| **Description** | Deposit page files enabled value on new records. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L167) |

---

### <a id='rdm_detail_side_bar_manage_attributes_extension_template'></a>`RDM_DETAIL_SIDE_BAR_MANAGE_ATTRIBUTES_EXTENSION_TEMPLATE`
| **Description** | Side bar manage attributes extension template. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1550) |

---

### <a id='rdm_facets'></a>`RDM_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L338) |

---

### <a id='rdm_files_default_max_additional_quota_size'></a>`RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE`
| **Description** | Default additional quota size for a bucket in bytes for files. |
|--------------|-----------|
| **Default Value** | `0` |
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L890) |

---

### <a id='rdm_files_default_max_file_size'></a>`RDM_FILES_DEFAULT_MAX_FILE_SIZE`
| **Description** | Default maximum file size for a bucket in bytes for files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L887) |

---

### <a id='rdm_files_default_quota_size'></a>`RDM_FILES_DEFAULT_QUOTA_SIZE`
| **Description** | Default size for a bucket in bytes for files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L884) |

---

### <a id='rdm_file_modification_period'></a>`RDM_FILE_MODIFICATION_PERIOD`
| **Description** | Time period after creation during which modified files can be published. 30 + 30 denotes grace perio... |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=45)` |
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L273) |

---

### <a id='rdm_file_modification_policy'></a>`RDM_FILE_MODIFICATION_POLICY`
| **Description** | Policy class which evaluates whether published files can be modified by a user. |
|--------------|-----------|
| **Default Value** | `FileModificationPolicyEvaluator` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L238) |

---

### <a id='rdm_iiif_manifest_formats'></a>`RDM_IIIF_MANIFEST_FORMATS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L904) |

---

### <a id='rdm_immediate_file_modification_enabled'></a>`RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED`
| **Description** | Allow editing of published files (by default by admins only). |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L241) |

---

### <a id='rdm_immediate_file_modification_policies'></a>`RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES`
| **Description** | List of policies for editing published files immediately.  To enable users to modify the files of th... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L244) |

---

### <a id='rdm_immediate_quota_increase_enabled'></a>`RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED`
| **Description** | Allow increasing of draft's quota from a user's additional quota.  RDM_FILES_DEFAULT_MAX_ADDITIONAL_... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L285) |

---

### <a id='rdm_immediate_quota_increase_policies'></a>`RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES`
| **Description** | List of policies for user's increasing their quota for a draft.  To enable users and admins to incre... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L291) |

---

### <a id='rdm_immediate_record_deletion_checklist'></a>`RDM_IMMEDIATE_RECORD_DELETION_CHECKLIST`
| **Description** | Checklist which appears on the modal to redirect user from immediate record deletion if possible.  T... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L198) |

---

### <a id='rdm_immediate_record_deletion_enabled'></a>`RDM_IMMEDIATE_RECORD_DELETION_ENABLED`
| **Description** | Allow users to immediately delete records. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L182) |

---

### <a id='rdm_immediate_record_deletion_policies'></a>`RDM_IMMEDIATE_RECORD_DELETION_POLICIES`
| **Description** | List of policies for immediate record deletion.  Policies are executed in order and the first one to... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L185) |

---

### <a id='rdm_lock_edit_published_files'></a>`RDM_LOCK_EDIT_PUBLISHED_FILES`
| **Description** | Lock editing already published files (enforce record versioning).     signature to implement:    def... |
|--------------|-----------|
| **Default Value** | `lock_edit_published_files` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L851) |

---

### <a id='rdm_media_files_default_max_file_size'></a>`RDM_MEDIA_FILES_DEFAULT_MAX_FILE_SIZE`
| **Description** | Default maximum file size for a bucket in bytes for media files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L881) |

---

### <a id='rdm_media_files_default_quota_size'></a>`RDM_MEDIA_FILES_DEFAULT_QUOTA_SIZE`
| **Description** | Default size for a bucket in bytes for media files. |
|--------------|-----------|
| **Default Value** | `10000000000` |
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L878) |

---

### <a id='rdm_namespaces'></a>`RDM_NAMESPACES`
| **Description** | Custom fields namespaces.  .. code-block:: python      {<namespace>: <uri>, ...}  For example:  .. c... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L757) |

---

### <a id='rdm_new_record_version_review_policy'></a>`RDM_NEW_RECORD_VERSION_REVIEW_POLICY`
| **Description** | Policy for when to require a community review for new record versions. |
|--------------|-----------|
| **Default Value** | `NewRecordVersionReviewPolicy` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L158) |

---

### <a id='rdm_oai_pmh_facets'></a>`RDM_OAI_PMH_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L530) |

---

### <a id='rdm_oai_pmh_search'></a>`RDM_OAI_PMH_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L552) |

---

### <a id='rdm_oai_pmh_sort_options'></a>`RDM_OAI_PMH_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L532) |

---

### <a id='rdm_optional_doi_validator'></a>`RDM_OPTIONAL_DOI_VALIDATOR`
| **Description** | Optional DOI transitions validate method.  Check the signature of validate_optional_doi for more inf... |
|--------------|-----------|
| **Default Value** | `validate_optional_doi` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L661) |

---

### <a id='rdm_parent_persistent_identifiers'></a>`RDM_PARENT_PERSISTENT_IDENTIFIERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L644) |

---

### <a id='rdm_parent_persistent_identifier_providers'></a>`RDM_PARENT_PERSISTENT_IDENTIFIER_PROVIDERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L633) |

---

### <a id='rdm_permission_policy'></a>`RDM_PERMISSION_POLICY`
| **Description** | Override the default record permission policy. |
|--------------|-----------|
| **Default Value** | `RDMRecordPermissionPolicy` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L144) |

---

### <a id='rdm_persistent_identifiers'></a>`RDM_PERSISTENT_IDENTIFIERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L604) |

---

### <a id='rdm_persistent_identifier_providers'></a>`RDM_PERSISTENT_IDENTIFIER_PROVIDERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L561) |

---

### <a id='rdm_quota_increase_policy'></a>`RDM_QUOTA_INCREASE_POLICY`
| **Description** | Policy class which evaluates whether the quota for drafts can be increased. |
|--------------|-----------|
| **Default Value** | `QuotaIncreasePolicyEvaluator` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L282) |

---

### <a id='rdm_records_allow_restriction_after_grace_period'></a>`RDM_RECORDS_ALLOW_RESTRICTION_AFTER_GRACE_PERIOD`
| **Description** | Whether record access restriction is allowed after the grace period or not. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L950) |

---

### <a id='rdm_records_container_extensions'></a>`RDM_RECORDS_CONTAINER_EXTENSIONS`
| **Description** | List of file extensions for container files. Experimental, this config can later be removed. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L956) |

---

### <a id='rdm_records_identifiers_schemes'></a>`RDM_RECORDS_IDENTIFIERS_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L86) |

---

### <a id='rdm_records_location_schemes'></a>`RDM_RECORDS_LOCATION_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L136) |

---

### <a id='rdm_records_max_files_count'></a>`RDM_RECORDS_MAX_FILES_COUNT`
| **Description** | Max amount of files allowed to upload in the deposit form. |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L872) |

---

### <a id='rdm_records_max_media_files_count'></a>`RDM_RECORDS_MAX_MEDIA_FILES_COUNT`
| **Description** | Max amount of media files allowed to upload in the deposit form. |
|--------------|-----------|
| **Default Value** | `100` |
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L875) |

---

### <a id='rdm_records_personorg_schemes'></a>`RDM_RECORDS_PERSONORG_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L79) |

---

### <a id='rdm_records_related_identifiers_schemes'></a>`RDM_RECORDS_RELATED_IDENTIFIERS_SCHEMES`
| **Description** | This variable is used to separate related identifiers. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L133) |

---

### <a id='rdm_records_require_secret_links_expiration'></a>`RDM_RECORDS_REQUIRE_SECRET_LINKS_EXPIRATION`
| **Description** | Whether share access links require an expiration date to be set or not. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L953) |

---

### <a id='rdm_records_restriction_grace_period'></a>`RDM_RECORDS_RESTRICTION_GRACE_PERIOD`
| **Description** | Grace period for changing record access to restricted. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(days=30)` |
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L947) |

---

### <a id='rdm_records_reviews'></a>`RDM_RECORDS_REVIEWS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L150) |

---

### <a id='rdm_records_ui_edit_url'></a>`RDM_RECORDS_UI_EDIT_URL`
| **Description** | Default UI URL for the edit page of a Bibliographic Record. |
|--------------|-----------|
| **Default Value** | `'/uploads/<pid_value>'` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L61) |

---

### <a id='rdm_records_user_fixture_passwords'></a>`RDM_RECORDS_USER_FIXTURE_PASSWORDS`
| **Description** | Overrides for the user fixtures' passwords.  The password set for a user fixture in this dictionary ... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L49) |

---

### <a id='rdm_record_deletion_policy'></a>`RDM_RECORD_DELETION_POLICY`
| **Description** | Policy class which evaluates whether a record can be deleted by a user. |
|--------------|-----------|
| **Default Value** | `RDMRecordDeletionPolicy` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L179) |

---

### <a id='rdm_record_file_extractors'></a>`RDM_RECORD_FILE_EXTRACTORS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L960) |

---

### <a id='rdm_requests_routes'></a>`RDM_REQUESTS_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1095) |

---

### <a id='rdm_request_record_deletion_checklist'></a>`RDM_REQUEST_RECORD_DELETION_CHECKLIST`
| **Description** | Checklist which appears on the modal to redirect user from record deletion request if possible. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L232) |

---

### <a id='rdm_request_record_deletion_enabled'></a>`RDM_REQUEST_RECORD_DELETION_ENABLED`
| **Description** | Allow users to request record deletion. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L226) |

---

### <a id='rdm_request_record_deletion_policies'></a>`RDM_REQUEST_RECORD_DELETION_POLICIES`
| **Description** | List of policies for record deletion requests. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L229) |

---

### <a id='rdm_resource_access_tokens_enabled'></a>`RDM_RESOURCE_ACCESS_TOKENS_ENABLED`
| **Description** | Flag to show whether RATs feature should be enabled. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L835) |

---

### <a id='rdm_resource_access_tokens_jwt_lifetime'></a>`RDM_RESOURCE_ACCESS_TOKENS_JWT_LIFETIME`
| **Description** | Maximum tokens lifetime. |
|--------------|-----------|
| **Default Value** | `datetime.timedelta(seconds=1800)` |
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L839) |

---

### <a id='rdm_resource_access_tokens_subject_schema'></a>`RDM_RESOURCE_ACCESS_TOKENS_SUBJECT_SCHEMA`
| **Description** | Resource access token Marshmallow schema for parsing JWT subject. |
|--------------|-----------|
| **Default Value** | `tokens.resource_access.SubjectSchema` |
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L848) |

---

### <a id='rdm_resource_access_tokens_whitelisted_jwt_algorithms'></a>`RDM_RESOURCE_ACCESS_TOKENS_WHITELISTED_JWT_ALGORITHMS`
| **Description** | Accepted JWT algorithms for decoding the RAT. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L842) |

---

### <a id='rdm_resource_access_token_request_arg'></a>`RDM_RESOURCE_ACCESS_TOKEN_REQUEST_ARG`
| **Description** | URL argument to provide resource access token. |
|--------------|-----------|
| **Default Value** | `'resource_access_token'` |
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L845) |

---

### <a id='rdm_search'></a>`RDM_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L466) |

---

### <a id='rdm_search_drafts'></a>`RDM_SEARCH_DRAFTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L507) |

---

### <a id='rdm_search_sort_by_verified'></a>`RDM_SEARCH_SORT_BY_VERIFIED`
| **Description** | Sort records by 'verified' first. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L411) |

---

### <a id='rdm_search_user_communities'></a>`RDM_SEARCH_USER_COMMUNITIES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1110) |

---

### <a id='rdm_search_user_requests'></a>`RDM_SEARCH_USER_REQUESTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1116) |

---

### <a id='rdm_search_versioning'></a>`RDM_SEARCH_VERSIONING`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L519) |

---

### <a id='rdm_sort_options'></a>`RDM_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L414) |

---

### <a id='rdm_stats_exclude_preview_file_download_events'></a>`RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS`
| **Description** | Exclude file-download stats events whose Referer is the file's own preview page. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L67) |

---

### <a id='rdm_user_moderation_enabled'></a>`RDM_USER_MODERATION_ENABLED`
| **Description** | Flag to enable creation of user moderation requests on specific user actions. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L869) |

---

### <a id='recaptcha_private_key'></a>`RECAPTCHA_PRIVATE_KEY`
| **Description** | reCAPTCHA private key. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L341) |

---

### <a id='recaptcha_public_key'></a>`RECAPTCHA_PUBLIC_KEY`
| **Description** | reCAPTCHA public key. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L338) |

---

### <a id='records_files_rest_endpoints'></a>`RECORDS_FILES_REST_ENDPOINTS`
| **Description** | REST endpoints configuration.  You can configure the REST API endpoint to access the record's files ... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-records-files](https://github.com/inveniosoftware/invenio-records-files/blob/master/invenio_records_files/config.py#L11) |

---

### <a id='records_permissions_record_policy'></a>`RECORDS_PERMISSIONS_RECORD_POLICY`
| **Default Value** | `'invenio_records_permissions.policies.RecordPermissionPolicy'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-permissions](https://github.com/inveniosoftware/invenio-records-permissions/blob/master/invenio_records_permissions/config.py#L12) |

---

### <a id='records_refresolver_cls'></a>`RECORDS_REFRESOLVER_CLS`
| **Description** | Custom JSONSchemas ref resolver class.  Note that when using a custom ref resolver class you should ... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L17); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L614) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='records_refresolver_store'></a>`RECORDS_REFRESOLVER_STORE`
| **Description** | JSONSchemas ref resolver store.  Used together with ``RECORDS_REFRESOLVER_CLS`` to provide a specifi... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L24); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L621) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='records_resources_allow_empty_files'></a>`RECORDS_RESOURCES_ALLOW_EMPTY_FILES`
| **Description** | Allow empty files to be uploaded. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L26) |

---

### <a id='records_resources_archive_download_max_size'></a>`RECORDS_RESOURCES_ARCHIVE_DOWNLOAD_MAX_SIZE`
| **Description** | Max total file size (bytes) for archive download. ``None`` disables the cap. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L64) |

---

### <a id='records_resources_default_transfer_type'></a>`RECORDS_RESOURCES_DEFAULT_TRANSFER_TYPE`
| **Description** | Default transfer class to use. One of 'L' (local), 'F' (fetch), 'R' (point to remote), 'M' (multipar... |
|--------------|-----------|
| **Default Value** | `'L'` |
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L38) |

---

### <a id='records_resources_extracted_stream_chunk_size'></a>`RECORDS_RESOURCES_EXTRACTED_STREAM_CHUNK_SIZE`
| **Description** | Chunk size of extracted stream used in ContainerItemResult.send_file(). |
|--------------|-----------|
| **Default Value** | `65536` |
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L43) |

---

### <a id='records_resources_files_allowed_domains'></a>`RECORDS_RESOURCES_FILES_ALLOWED_DOMAINS`
| **Description** | Explicitly allowed domains for external file fetching.  Only file URLs from these domains will be al... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L17) |

---

### <a id='records_resources_image_formats'></a>`RECORDS_RESOURCES_IMAGE_FORMATS`
| **Description** | Which image formats to extract metadata for. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Sources** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L23); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1216) |

---

### <a id='records_resources_transfers'></a>`RECORDS_RESOURCES_TRANSFERS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L29) |

---

### <a id='records_resources_zip_formats'></a>`RECORDS_RESOURCES_ZIP_FORMATS`
| **Description** | File extensions interpreted as ZIP files. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L46) |

---

### <a id='records_resources_zip_max_entries'></a>`RECORDS_RESOURCES_ZIP_MAX_ENTRIES`
| **Description** | Max allowed entries inside ZIP file. |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L61) |

---

### <a id='records_resources_zip_max_header_size'></a>`RECORDS_RESOURCES_ZIP_MAX_HEADER_SIZE`
| **Description** | Max header size of ZIP file that can be preloaded. |
|--------------|-----------|
| **Default Value** | `65536` |
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L52) |

---

### <a id='records_resources_zip_max_listing_entries'></a>`RECORDS_RESOURCES_ZIP_MAX_LISTING_ENTRIES`
| **Description** | Max entries returned by the container listing API. |
|--------------|-----------|
| **Default Value** | `1000` |
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L49) |

---

### <a id='records_resources_zip_max_ratio'></a>`RECORDS_RESOURCES_ZIP_MAX_RATIO`
| **Description** | Max allowed compression ratio of an entry inside ZIP file. |
|--------------|-----------|
| **Default Value** | `200.0` |
| **Type** | float |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L58) |

---

### <a id='records_resources_zip_max_total_uncompressed'></a>`RECORDS_RESOURCES_ZIP_MAX_TOTAL_UNCOMPRESSED`
| **Description** | Max allowed uncompressed size of ZIP. |
|--------------|-----------|
| **Default Value** | `524288000` |
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L55) |

---

### <a id='records_rest_default_create_permission_factory'></a>`RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY`
| **Description** | Default create permission factory: reject any request. |
|--------------|-----------|
| **Default Value** | `deny_all` |
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L357) |

---

### <a id='records_rest_default_delete_permission_factory'></a>`RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY`
| **Description** | Default delete permission factory: reject any request. |
|--------------|-----------|
| **Default Value** | `deny_all` |
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L369) |

---

### <a id='records_rest_default_list_permission_factory'></a>`RECORDS_REST_DEFAULT_LIST_PERMISSION_FACTORY`
| **Description** | Default list permission factory: allow all requests |
|--------------|-----------|
| **Default Value** | `allow_all` |
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L360) |

---

### <a id='records_rest_default_loaders'></a>`RECORDS_REST_DEFAULT_LOADERS`
| **Default Value** | `{'application/json': lambda: request.get_json(), 'application/json-patch+json': lambda: request.get_...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L237) |

---

### <a id='records_rest_default_read_permission_factory'></a>`RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY`
| **Description** | Default read permission factory: check if the record exists. |
|--------------|-----------|
| **Default Value** | `check_search` |
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L363) |

---

### <a id='records_rest_default_results_size'></a>`RECORDS_REST_DEFAULT_RESULTS_SIZE`
| **Description** | Default search results size. |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L381) |

---

### <a id='records_rest_default_sort'></a>`RECORDS_REST_DEFAULT_SORT`
| **Default Value** | `dict(records=dict(query='bestmatch', noquery='mostrecent'))` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L302) |

---

### <a id='records_rest_default_update_permission_factory'></a>`RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY`
| **Description** | Default update permission factory: reject any request. |
|--------------|-----------|
| **Default Value** | `deny_all` |
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L366) |

---

### <a id='records_rest_endpoints'></a>`RECORDS_REST_ENDPOINTS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L192); [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L19) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='records_rest_facets'></a>`RECORDS_REST_FACETS`
| **Default Value** | `dict(records=dict(aggs=dict(type=dict(terms=dict(field='type'))), post_filters=dict(type=terms_filte...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L322) |

---

### <a id='records_rest_facets_post_filters_propagate'></a>`RECORDS_REST_FACETS_POST_FILTERS_PROPAGATE`
| **Description** | Define if the post_filters facets in one category should be applied as filters to all the other cate... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L354) |

---

### <a id='records_rest_search_error_handlers'></a>`RECORDS_REST_SEARCH_ERROR_HANDLERS`
| **Default Value** | `{'query_parsing_exception': 'invenio_records_rest.views:search_query_parsing_exception_handler', 'qu...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L372) |

---

### <a id='records_rest_sort_options'></a>`RECORDS_REST_SORT_OPTIONS`
| **Default Value** | `dict(records=dict(bestmatch=dict(title=_('Best match'), fields=['_score'], default_order='desc', ord...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L259) |

---

### <a id='records_ui_base_template'></a>`RECORDS_UI_BASE_TEMPLATE`
| **Default Value** | `'invenio_records_ui/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='records_ui_default_permission_factory'></a>`RECORDS_UI_DEFAULT_PERMISSION_FACTORY`
| **Description** | Configure the default permission factory. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L16) |

---

### <a id='records_ui_endpoints'></a>`RECORDS_UI_ENDPOINTS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L22); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L193) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='records_ui_export_formats'></a>`RECORDS_UI_EXPORT_FORMATS`
| **Description** | Defaut record serialization views.  The structure of the dictionary is as follows:  .. code-block:: ... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L89) |

---

### <a id='records_ui_login_endpoint'></a>`RECORDS_UI_LOGIN_ENDPOINT`
| **Description** | Endpoint where redirect the user if login is required. |
|--------------|-----------|
| **Default Value** | `'security.login'` |
| **Type** | str |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L19) |

---

### <a id='records_ui_tombstone_template'></a>`RECORDS_UI_TOMBSTONE_TEMPLATE`
| **Description** | Configure the tombstone template. |
|--------------|-----------|
| **Default Value** | `'invenio_records_ui/tombstone.html'` |
| **Type** | str |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L13) |

---

### <a id='records_validation_types'></a>`RECORDS_VALIDATION_TYPES`
| **Description** | Pass additional types when validating a record against a schema. For more details, see: `<https://py... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L11) |

---

### <a id='record_routes'></a>`RECORD_ROUTES`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='remember_cookie_duration'></a>`REMEMBER_COOKIE_DURATION`
| **Description** | Remember me cookie life time changed to 90 days instead of 365 days. |
|--------------|-----------|
| **Default Value** | `timedelta(days=90)` |
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L265) |

---

### <a id='repository_description'></a>`REPOSITORY_DESCRIPTION`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='repository_keywords'></a>`REPOSITORY_KEYWORDS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='repository_name'></a>`REPOSITORY_NAME`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='repository_subtitle'></a>`REPOSITORY_SUBTITLE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='repository_support_contact'></a>`REPOSITORY_SUPPORT_CONTACT`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='requests_comments_allowed_extra_html_attrs'></a>`REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_ATTRS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L162) |

---

### <a id='requests_comments_allowed_extra_html_tags'></a>`REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_TAGS`
| **Description** | Extend allowed HTML tags list for requests comments content. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L159) |

---

### <a id='requests_comment_preview_limit'></a>`REQUESTS_COMMENT_PREVIEW_LIMIT`
| **Description** | Number of most recent child comments to inline in parent's search index.  This limits the size of in... |
|--------------|-----------|
| **Default Value** | `5` |
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L144) |

---

### <a id='requests_entity_resolvers'></a>`REQUESTS_ENTITY_RESOLVERS`
| **Description** | Registered resolvers for resolving/creating references in request metadata. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L37) |

---

### <a id='requests_error_handlers'></a>`REQUESTS_ERROR_HANDLERS`
| **Default Value** | `{**request_error_handlers, InvalidAccessRestrictions: create_error_handler(lambda e: HTTPJSONExcepti...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1518) |

---

### <a id='requests_events_service_components'></a>`REQUESTS_EVENTS_SERVICE_COMPONENTS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L154) |

---

### <a id='requests_facets'></a>`REQUESTS_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L75) |

---

### <a id='requests_files_default_max_file_size'></a>`REQUESTS_FILES_DEFAULT_MAX_FILE_SIZE`
| **Description** | 10MB |
|--------------|-----------|
| **Default Value** | `10000000` |
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L152) |

---

### <a id='requests_files_default_quota_size'></a>`REQUESTS_FILES_DEFAULT_QUOTA_SIZE`
| **Description** | 100MB |
|--------------|-----------|
| **Default Value** | `100000000` |
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L151) |

---

### <a id='requests_locking_enabled'></a>`REQUESTS_LOCKING_ENABLED`
| **Description** | Enable locking/unlocking for request conversations. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L141) |

---

### <a id='requests_moderation_role'></a>`REQUESTS_MODERATION_ROLE`
| **Description** | ID of the Role used for moderation. |
|--------------|-----------|
| **Default Value** | `'administration-moderation'` |
| **Type** | str |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L95) |

---

### <a id='requests_permission_policy'></a>`REQUESTS_PERMISSION_POLICY`
| **Description** | The requests permission policy, extended to work with guest access requests. |
|--------------|-----------|
| **Default Value** | `RDMRequestsPermissionPolicy` |
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1514); [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L24) |
| **Set by** | [`register_workflow`](api.html#oarepo_config.register_workflow) |

---

### <a id='requests_registered_event_types'></a>`REQUESTS_REGISTERED_EVENT_TYPES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L30) |

---

### <a id='requests_registered_types'></a>`REQUESTS_REGISTERED_TYPES`
| **Description** | Configuration for registered Request Types. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L27) |

---

### <a id='requests_reviewers_enabled'></a>`REQUESTS_REVIEWERS_ENABLED`
| **Description** | Enable reviewers for requests. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L135) |

---

### <a id='requests_reviewers_max_number'></a>`REQUESTS_REVIEWERS_MAX_NUMBER`
| **Description** | Maximum number of reviewers allowed for a request. |
|--------------|-----------|
| **Default Value** | `15` |
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L138) |

---

### <a id='requests_routes'></a>`REQUESTS_ROUTES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L40) |

---

### <a id='requests_search'></a>`REQUESTS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L45) |

---

### <a id='requests_sort_options'></a>`REQUESTS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L51) |

---

### <a id='requests_timeline_page_size'></a>`REQUESTS_TIMELINE_PAGE_SIZE`
| **Description** | Amount of items per page on the request details timeline |
|--------------|-----------|
| **Default Value** | `10` |
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L91) |

---

### <a id='requests_user_moderation_facets'></a>`REQUESTS_USER_MODERATION_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L124) |

---

### <a id='requests_user_moderation_search'></a>`REQUESTS_USER_MODERATION_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L102) |

---

### <a id='requests_user_moderation_sort_options'></a>`REQUESTS_USER_MODERATION_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L108) |

---

### <a id='rest_csrf_enabled'></a>`REST_CSRF_ENABLED`
| **Description** | Enable CSRF middleware. (Default: ``False``).  .. note::    The CSRF middleware accepts some configu... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L742); [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L79) |

---

### <a id='rest_enable_cors'></a>`REST_ENABLE_CORS`
| **Description** | Enable CORS configuration. (Default: ``False``). |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L54) |

---

### <a id='rest_mimetype_query_arg_name'></a>`REST_MIMETYPE_QUERY_ARG_NAME`
| **Description** | Name of the query argument to specify the mimetype wanted for the output.    Set it to None to disab... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L57) |

---

### <a id='ror_client_id'></a>`ROR_CLIENT_ID`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='s3_access_key_id'></a>`S3_ACCESS_KEY_ID`
| **Description** | The access key to use when creating the client.  This is entirely optional, and if not provided, the... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L32) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='s3_config_extra'></a>`S3_CONFIG_EXTRA`
| **Description** | Additional configuration to be passed to S3f3. In some cases, specially those not using AWS S3, some... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L78) |

---

### <a id='s3_default_block_size'></a>`S3_DEFAULT_BLOCK_SIZE`
| **Description** | Default block size value used to send multi-part uploads to S3. Typically 5Mb is minimum allowed by ... |
|--------------|-----------|
| **Default Value** | `5242880` |
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L74) |

---

### <a id='s3_endpoint_url'></a>`S3_ENDPOINT_URL`
| **Description** | S3 server URL endpoint.  If using Amazon AWS S3 service this config variable can be set to None as t... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L9) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='s3_maximum_number_of_parts'></a>`S3_MAXIMUM_NUMBER_OF_PARTS`
| **Description** | Maximum number of parts to be used. See `AWS Multipart Upload Overview <https://docs.aws.amazon.com/... |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L67) |

---

### <a id='s3_region_name'></a>`S3_REGION_NAME`
| **Description** | S3 region name  This is entirely optional, and if not provided, the region name will be automaticall... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L22) |

---

### <a id='s3_secret_access_key'></a>`S3_SECRET_ACCESS_KEY`
| **Description** | The secret key to use when creating the client.  This is entirely optional, and if not provided, the... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L42) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='s3_signature_version'></a>`S3_SIGNATURE_VERSION`
| **Description** | Version of the S3 signature algorithm. Can be 's3' (v2) or 's3v4' (v4). See `Amazon Boto3 documentat... |
|--------------|-----------|
| **Default Value** | `'s3v4'` |
| **Type** | str |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L60) |

---

### <a id='s3_upload_url_expiration'></a>`S3_UPLOAD_URL_EXPIRATION`
| **Description** | Number of seconds the file upload URL will be valid. The default here is 7 days to allow large file ... |
|--------------|-----------|
| **Default Value** | `604800` |
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L91) |

---

### <a id='s3_url_expiration'></a>`S3_URL_EXPIRATION`
| **Description** | Number of seconds the file serving URL will be valid.  See `Amazon Boto3 documentation on presigned ... |
|--------------|-----------|
| **Default Value** | `60` |
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L52) |

---

### <a id='search_client_config'></a>`SEARCH_CLIENT_CONFIG`
| **Description** | Dictionary of options for the Elasticsearch/OpenSearch client.  The value of this variable is passed... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L18) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='search_elastic_hosts'></a>`SEARCH_ELASTIC_HOSTS`
| **Description** | Deprecated alias for ``SEARCH_HOSTS``. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L55) |

---

### <a id='search_hosts'></a>`SEARCH_HOSTS`
| **Description** | Search hosts. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L736); [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L37) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='search_index_prefix'></a>`SEARCH_INDEX_PREFIX`
| **Description** | Any index, alias and templates will be prefixed with this string.  Useful to host multiple instances... |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L99) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='search_mappings'></a>`SEARCH_MAPPINGS`
| **Description** | List of aliases for which, their search mappings should be created.  - If `None` all aliases (and th... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L59) |

---

### <a id='search_results_min_score'></a>`SEARCH_RESULTS_MIN_SCORE`
| **Description** | If set, the `min_score` parameter is added to each search request body.  The `min_score` parameter e... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L84) |

---

### <a id='search_ui_base_template'></a>`SEARCH_UI_BASE_TEMPLATE`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='search_ui_header_template'></a>`SEARCH_UI_HEADER_TEMPLATE`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='search_ui_jstemplate_count'></a>`SEARCH_UI_JSTEMPLATE_COUNT`
| **Description** | Configure the count template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/count.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L29) |

---

### <a id='search_ui_jstemplate_error'></a>`SEARCH_UI_JSTEMPLATE_ERROR`
| **Description** | Configure the error page template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/error.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L32) |

---

### <a id='search_ui_jstemplate_facets'></a>`SEARCH_UI_JSTEMPLATE_FACETS`
| **Description** | Configure the facets template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/facets.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L35) |

---

### <a id='search_ui_jstemplate_loading'></a>`SEARCH_UI_JSTEMPLATE_LOADING`
| **Description** | Configure the loading template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/loading.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L49) |

---

### <a id='search_ui_jstemplate_pagination'></a>`SEARCH_UI_JSTEMPLATE_PAGINATION`
| **Description** | Configure the pagination template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/pagination.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L52) |

---

### <a id='search_ui_jstemplate_range'></a>`SEARCH_UI_JSTEMPLATE_RANGE`
| **Description** | Configure the range template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/range.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L38) |

---

### <a id='search_ui_jstemplate_range_options'></a>`SEARCH_UI_JSTEMPLATE_RANGE_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L41) |

---

### <a id='search_ui_jstemplate_results'></a>`SEARCH_UI_JSTEMPLATE_RESULTS`
| **Description** | Configure the results template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/results.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L55) |

---

### <a id='search_ui_jstemplate_select_box'></a>`SEARCH_UI_JSTEMPLATE_SELECT_BOX`
| **Description** | Configure the select box template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/selectbox.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L58) |

---

### <a id='search_ui_jstemplate_sort_order'></a>`SEARCH_UI_JSTEMPLATE_SORT_ORDER`
| **Description** | Configure the toggle button template. |
|--------------|-----------|
| **Default Value** | `'templates/invenio_search_ui/togglebutton.html'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L61) |

---

### <a id='search_ui_search_api'></a>`SEARCH_UI_SEARCH_API`
| **Description** | Configure the search engine endpoint. |
|--------------|-----------|
| **Default Value** | `'/api/records/'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L21) |

---

### <a id='search_ui_search_config_gen'></a>`SEARCH_UI_SEARCH_CONFIG_GEN`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L64) |

---

### <a id='search_ui_search_index'></a>`SEARCH_UI_SEARCH_INDEX`
| **Description** | Name of the search index used. |
|--------------|-----------|
| **Default Value** | `'records'` |
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L24) |

---

### <a id='search_ui_search_template'></a>`SEARCH_UI_SEARCH_TEMPLATE`
| **Description** | Configure the search page template. |
|--------------|-----------|
| **Default Value** | `'invenio_search_ui/search.html'` |
| **Type** | str |
| **Sources** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L16); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L786) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='search_ui_search_view'></a>`SEARCH_UI_SEARCH_VIEW`
| **Description** | Default funtion to do the `search` route. |
|--------------|-----------|
| **Default Value** | `search` |
| **Type** | unknown |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L13) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='secret_key'></a>`SECRET_KEY`
| **Description** | Flask secret key.  Each installation (dev, production, ...) needs a separate key.  SECURITY WARNING:... |
|--------------|-----------|
| **Default Value** | `'CHANGE_ME'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L217) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='secret_key_fallbacks'></a>`SECRET_KEY_FALLBACKS`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_auto_login_after_confirm'></a>`SECURITY_AUTO_LOGIN_AFTER_CONFIRM`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_blueprint_name'></a>`SECURITY_BLUEPRINT_NAME`
| **Default Value** | `'security'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_changeable'></a>`SECURITY_CHANGEABLE`
| **Description** | Allow password change by users. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L175) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='security_change_password_template'></a>`SECURITY_CHANGE_PASSWORD_TEMPLATE`
| **Description** | Default template for change password. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/change_password.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L223) |

---

### <a id='security_change_salt'></a>`SECURITY_CHANGE_SALT`
| **Default Value** | `'change-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_change_url'></a>`SECURITY_CHANGE_URL`
| **Description** | URL endpoint for password change. |
|--------------|-----------|
| **Default Value** | `'/account/settings/password/'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L244) |

---

### <a id='security_cli_roles_name'></a>`SECURITY_CLI_ROLES_NAME`
| **Default Value** | `'roles'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_cli_users_name'></a>`SECURITY_CLI_USERS_NAME`
| **Default Value** | `'users'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_confirmable'></a>`SECURITY_CONFIRMABLE`
| **Description** | Allow user to confirm their email address. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L178) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='security_confirm_email_within'></a>`SECURITY_CONFIRM_EMAIL_WITHIN`
| **Description** | Amount of time the email confirmation link is active.  Note, since the confirmation link will also l... |
|--------------|-----------|
| **Default Value** | `'30 minutes'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L187) |

---

### <a id='security_confirm_error_view'></a>`SECURITY_CONFIRM_ERROR_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_confirm_salt'></a>`SECURITY_CONFIRM_SALT`
| **Default Value** | `'confirm-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_confirm_url'></a>`SECURITY_CONFIRM_URL`
| **Default Value** | `'/confirm'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_default_http_auth_realm'></a>`SECURITY_DEFAULT_HTTP_AUTH_REALM`
| **Default Value** | `'Login Required'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_default_remember_me'></a>`SECURITY_DEFAULT_REMEMBER_ME`
| **Description** | "Remember me" default value in login form.  This is only the default value in the login form. A user... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L168) |

---

### <a id='security_deprecated_hashing_schemes'></a>`SECURITY_DEPRECATED_HASHING_SCHEMES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

---

### <a id='security_deprecated_password_schemes'></a>`SECURITY_DEPRECATED_PASSWORD_SCHEMES`
| **Description** | Deprecated password hashing algorithms.  Password hashes in a deprecated scheme are automatically mi... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L158) |

---

### <a id='security_email_html'></a>`SECURITY_EMAIL_HTML`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_email_plaintext'></a>`SECURITY_EMAIL_PLAINTEXT`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_email_subject_confirm'></a>`SECURITY_EMAIL_SUBJECT_CONFIRM`
| **Default Value** | `'Please confirm your email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_email_subject_password_change_notice'></a>`SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE`
| **Default Value** | `'Your password has been changed'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_email_subject_password_notice'></a>`SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE`
| **Default Value** | `'Your password has been reset'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_email_subject_password_reset'></a>`SECURITY_EMAIL_SUBJECT_PASSWORD_RESET`
| **Default Value** | `'Password reset instructions'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_email_subject_register'></a>`SECURITY_EMAIL_SUBJECT_REGISTER`
| **Description** | Email subject for account registration emails. |
|--------------|-----------|
| **Default Value** | `'Welcome'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L413) |

---

### <a id='security_flash_messages'></a>`SECURITY_FLASH_MESSAGES`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_forgot_password_template'></a>`SECURITY_FORGOT_PASSWORD_TEMPLATE`
| **Description** | Default template for password recovery (asking for email). |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/forgot_password.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L211) |

---

### <a id='security_hashing_schemes'></a>`SECURITY_HASHING_SCHEMES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

---

### <a id='security_i18n_dirname'></a>`SECURITY_I18N_DIRNAME`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-...` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_i18n_domain'></a>`SECURITY_I18N_DOMAIN`
| **Default Value** | `'flask_security'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_login_salt'></a>`SECURITY_LOGIN_SALT`
| **Default Value** | `'login-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_login_url'></a>`SECURITY_LOGIN_URL`
| **Description** | URL endpoint for login. |
|--------------|-----------|
| **Default Value** | `'/login/'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L238) |

---

### <a id='security_login_user_template'></a>`SECURITY_LOGIN_USER_TEMPLATE`
| **Description** | Default template for login. |
|--------------|-----------|
| **Default Value** | `'invenio_oauthclient/login_user.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L214) |

---

### <a id='security_login_within'></a>`SECURITY_LOGIN_WITHIN`
| **Default Value** | `'1 days'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_login_without_confirmation'></a>`SECURITY_LOGIN_WITHOUT_CONFIRMATION`
| **Description** | Allow users to login without first confirming their email address. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L204) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='security_logout_url'></a>`SECURITY_LOGOUT_URL`
| **Description** | URL endpoint for logout. |
|--------------|-----------|
| **Default Value** | `'/logout/'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L241) |

---

### <a id='security_msg_already_confirmed'></a>`SECURITY_MSG_ALREADY_CONFIRMED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_confirmation_expired'></a>`SECURITY_MSG_CONFIRMATION_EXPIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_confirmation_request'></a>`SECURITY_MSG_CONFIRMATION_REQUEST`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_confirmation_required'></a>`SECURITY_MSG_CONFIRMATION_REQUIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_confirm_registration'></a>`SECURITY_MSG_CONFIRM_REGISTRATION`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_disabled_account'></a>`SECURITY_MSG_DISABLED_ACCOUNT`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_email_already_associated'></a>`SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_email_confirmed'></a>`SECURITY_MSG_EMAIL_CONFIRMED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_email_not_provided'></a>`SECURITY_MSG_EMAIL_NOT_PROVIDED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_forgot_password'></a>`SECURITY_MSG_FORGOT_PASSWORD`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_invalid_confirmation_token'></a>`SECURITY_MSG_INVALID_CONFIRMATION_TOKEN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_invalid_email_address'></a>`SECURITY_MSG_INVALID_EMAIL_ADDRESS`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_invalid_login_token'></a>`SECURITY_MSG_INVALID_LOGIN_TOKEN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_invalid_password'></a>`SECURITY_MSG_INVALID_PASSWORD`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_invalid_redirect'></a>`SECURITY_MSG_INVALID_REDIRECT`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_invalid_reset_password_token'></a>`SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_local_login_disabled'></a>`SECURITY_MSG_LOCAL_LOGIN_DISABLED`
| **Description** | The error to be displayed in REST login when local login is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L247) |

---

### <a id='security_msg_login'></a>`SECURITY_MSG_LOGIN`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_login_email_sent'></a>`SECURITY_MSG_LOGIN_EMAIL_SENT`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_login_expired'></a>`SECURITY_MSG_LOGIN_EXPIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_breached'></a>`SECURITY_MSG_PASSWORD_BREACHED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_breached_site_error'></a>`SECURITY_MSG_PASSWORD_BREACHED_SITE_ERROR`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_change'></a>`SECURITY_MSG_PASSWORD_CHANGE`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_change_disabled'></a>`SECURITY_MSG_PASSWORD_CHANGE_DISABLED`
| **Description** | The error to be displayed in REST password change when it is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L253) |

---

### <a id='security_msg_password_invalid_length'></a>`SECURITY_MSG_PASSWORD_INVALID_LENGTH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_is_the_same'></a>`SECURITY_MSG_PASSWORD_IS_THE_SAME`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_mismatch'></a>`SECURITY_MSG_PASSWORD_MISMATCH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_not_provided'></a>`SECURITY_MSG_PASSWORD_NOT_PROVIDED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_not_set'></a>`SECURITY_MSG_PASSWORD_NOT_SET`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_recovery_disabled'></a>`SECURITY_MSG_PASSWORD_RECOVERY_DISABLED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L256) |

---

### <a id='security_msg_password_reset'></a>`SECURITY_MSG_PASSWORD_RESET`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_reset_disabled'></a>`SECURITY_MSG_PASSWORD_RESET_DISABLED`
| **Description** | The error to be displayed in REST password reset when it is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L262) |

---

### <a id='security_msg_password_reset_expired'></a>`SECURITY_MSG_PASSWORD_RESET_EXPIRED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_reset_request'></a>`SECURITY_MSG_PASSWORD_RESET_REQUEST`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_password_too_simple'></a>`SECURITY_MSG_PASSWORD_TOO_SIMPLE`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_refresh'></a>`SECURITY_MSG_REFRESH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_registration_disabled'></a>`SECURITY_MSG_REGISTRATION_DISABLED`
| **Description** | The error to be displayed in REST registration when it is disabled. |
|--------------|-----------|
| **Default Value** | `<tuple>` |
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L250) |

---

### <a id='security_msg_retype_password_mismatch'></a>`SECURITY_MSG_RETYPE_PASSWORD_MISMATCH`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_unauthorized'></a>`SECURITY_MSG_UNAUTHORIZED`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_msg_user_does_not_exist'></a>`SECURITY_MSG_USER_DOES_NOT_EXIST`
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

---

### <a id='security_password_breached_count'></a>`SECURITY_PASSWORD_BREACHED_COUNT`
| **Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='security_password_check_breached'></a>`SECURITY_PASSWORD_CHECK_BREACHED`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_password_complexity_checker'></a>`SECURITY_PASSWORD_COMPLEXITY_CHECKER`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_password_hash'></a>`SECURITY_PASSWORD_HASH`
| **Description** | Default password hashing algorithm for new passwords. |
|--------------|-----------|
| **Default Value** | `'pbkdf2_sha512'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L149) |

---

### <a id='security_password_length_min'></a>`SECURITY_PASSWORD_LENGTH_MIN`
| **Default Value** | `6` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='security_password_salt'></a>`SECURITY_PASSWORD_SALT`
| **Description** | Salt for storing passwords. |
|--------------|-----------|
| **Default Value** | `'CHANGE_ME'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L207) |

---

### <a id='security_password_schemes'></a>`SECURITY_PASSWORD_SCHEMES`
| **Description** | Supported password hashing algorithms (for passwords already stored).  You should include both the d... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L152) |

---

### <a id='security_password_single_hash'></a>`SECURITY_PASSWORD_SINGLE_HASH`
| **Description** | Password hashing algorithms requiring single hasing only. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L165) |

---

### <a id='security_post_change_view'></a>`SECURITY_POST_CHANGE_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_post_confirm_view'></a>`SECURITY_POST_CONFIRM_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_post_login_view'></a>`SECURITY_POST_LOGIN_VIEW`
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_post_logout_view'></a>`SECURITY_POST_LOGOUT_VIEW`
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_post_register_view'></a>`SECURITY_POST_REGISTER_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_post_reset_view'></a>`SECURITY_POST_RESET_VIEW`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_recoverable'></a>`SECURITY_RECOVERABLE`
| **Description** | Allow password recovery by users. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L181) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='security_registerable'></a>`SECURITY_REGISTERABLE`
| **Description** | Allow users to register. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L184) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='security_register_url'></a>`SECURITY_REGISTER_URL`
| **Description** | URL endpoint for user registation. |
|--------------|-----------|
| **Default Value** | `'/signup/'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L232) |

---

### <a id='security_register_user_template'></a>`SECURITY_REGISTER_USER_TEMPLATE`
| **Description** | Default template for user registration. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/register_user.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L217) |

---

### <a id='security_reset_password_template'></a>`SECURITY_RESET_PASSWORD_TEMPLATE`
| **Description** | Default template for password recovery (reset of the password). |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/reset_password.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L220) |

---

### <a id='security_reset_password_within'></a>`SECURITY_RESET_PASSWORD_WITHIN`
| **Description** | Amount of time the password reset link is active.  Note, since the confirmation link will also login... |
|--------------|-----------|
| **Default Value** | `'30 minutes'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L194) |

---

### <a id='security_reset_salt'></a>`SECURITY_RESET_SALT`
| **Default Value** | `'reset-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_reset_url'></a>`SECURITY_RESET_URL`
| **Description** | URL endpoint for password recovery. |
|--------------|-----------|
| **Default Value** | `'/lost-password/'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L235) |

---

### <a id='security_send_confirmation_template'></a>`SECURITY_SEND_CONFIRMATION_TEMPLATE`
| **Description** | Default template for email confirmation. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/send_confirmation.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L226) |

---

### <a id='security_send_login_template'></a>`SECURITY_SEND_LOGIN_TEMPLATE`
| **Description** | Default template for email confirmation. |
|--------------|-----------|
| **Default Value** | `'invenio_accounts/send_login.html'` |
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L229) |

---

### <a id='security_send_password_change_email'></a>`SECURITY_SEND_PASSWORD_CHANGE_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_send_password_reset_email'></a>`SECURITY_SEND_PASSWORD_RESET_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_send_password_reset_notice_email'></a>`SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_send_register_email'></a>`SECURITY_SEND_REGISTER_EMAIL`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='security_subdomain'></a>`SECURITY_SUBDOMAIN`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_token_authentication_header'></a>`SECURITY_TOKEN_AUTHENTICATION_HEADER`
| **Default Value** | `'Authentication-Token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_token_authentication_key'></a>`SECURITY_TOKEN_AUTHENTICATION_KEY`
| **Default Value** | `'auth_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='security_token_max_age'></a>`SECURITY_TOKEN_MAX_AGE`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_trackable'></a>`SECURITY_TRACKABLE`
| **Description** | Enable user tracking on login. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L201) |

---

### <a id='security_url_prefix'></a>`SECURITY_URL_PREFIX`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='security_user_identity_attributes'></a>`SECURITY_USER_IDENTITY_ATTRIBUTES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

---

### <a id='security_zxcvbn_minimum_score'></a>`SECURITY_ZXCVBN_MINIMUM_SCORE`
| **Default Value** | `3` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='send_file_max_age_default'></a>`SEND_FILE_MAX_AGE_DEFAULT`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='sentry_dsn'></a>`SENTRY_DSN`
| **Description** | Set SENTRY_DSN environment variable. |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L98) |

---

### <a id='server_name'></a>`SERVER_NAME`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='session_cookie_domain'></a>`SESSION_COOKIE_DOMAIN`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='session_cookie_httponly'></a>`SESSION_COOKIE_HTTPONLY`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='session_cookie_name'></a>`SESSION_COOKIE_NAME`
| **Default Value** | `'session'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='session_cookie_partitioned'></a>`SESSION_COOKIE_PARTITIONED`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='session_cookie_path'></a>`SESSION_COOKIE_PATH`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='session_cookie_samesite'></a>`SESSION_COOKIE_SAMESITE`
| **Description** | Restricts how cookies are sent with requests from external sites. |
|--------------|-----------|
| **Default Value** | `'Lax'` |
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L228) |

---

### <a id='session_cookie_secure'></a>`SESSION_COOKIE_SECURE`
| **Description** | Sets cookie with the secure flag by default. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L225) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='session_key_bits'></a>`SESSION_KEY_BITS`
| **Default Value** | `64` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

### <a id='session_random_source'></a>`SESSION_RANDOM_SOURCE`
| **Default Value** | `<random.SystemRandom object at 0xad738d820>` |
|--------------|-----------|
| **Type** | SystemRandom |
| **Source** | unknown |

---

### <a id='session_refresh_each_request'></a>`SESSION_REFRESH_EACH_REQUEST`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='settings_template'></a>`SETTINGS_TEMPLATE`
| **Description** | Settings page template used for e.g. display user settings views. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_settings.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L41); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L276) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='sitemap_max_entry_count'></a>`SITEMAP_MAX_ENTRY_COUNT`
| **Description** | Maximum number of entries (<url> or <sitemap>) per file.  The Sitemap protocol sets it at 50_000, bu... |
|--------------|-----------|
| **Default Value** | `10000` |
| **Type** | int |
| **Source** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L11) |

---

### <a id='sitemap_root_view_enabled'></a>`SITEMAP_ROOT_VIEW_ENABLED`
| **Description** | Enable the `/sitemap.xml` endpoint serving the first sitemap index. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L25) |

---

### <a id='sitemap_sections'></a>`SITEMAP_SECTIONS`
| **Description** | Instances of `sitemap.SitemapSection` that will populate the Sitemap files. |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Sources** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L22); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1556) |

---

### <a id='site_api_url'></a>`SITE_API_URL`
| **Default Value** | `'https://127.0.0.1:5000/api'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L15) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='site_ui_url'></a>`SITE_UI_URL`
| **Default Value** | `'https://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L13) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='sqlalchemy_binds'></a>`SQLALCHEMY_BINDS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

---

### <a id='sqlalchemy_database_uri'></a>`SQLALCHEMY_DATABASE_URI`
| **Default Value** | `'sqlite:////Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instan...` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L521) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='sqlalchemy_echo'></a>`SQLALCHEMY_ECHO`
| **Description** | Enable to see all SQL queries. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L529) |

---

### <a id='sqlalchemy_engine_options'></a>`SQLALCHEMY_ENGINE_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L532) |

---

### <a id='sqlalchemy_record_queries'></a>`SQLALCHEMY_RECORD_QUERIES`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='sqlalchemy_track_modifications'></a>`SQLALCHEMY_TRACK_MODIFICATIONS`
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='stats_aggregations'></a>`STATS_AGGREGATIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1284); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L47) |

---

### <a id='stats_events'></a>`STATS_EVENTS`
| **Description** | Enabled Events.  Each key is the name of an event. A queue will be created for each event.  If the d... |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1248); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L25) |

---

### <a id='stats_events_utc_datetime_enabled'></a>`STATS_EVENTS_UTC_DATETIME_ENABLED`
| **Description** | Enable timezone-aware UTC datetimes for event timestamps.  When set to ``False`` (default), naive UT... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L80) |

---

### <a id='stats_mq_exchange'></a>`STATS_MQ_EXCHANGE`
| **Default Value** | `Exchange('events', type='direct', delivery_mode='transient')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L67) |

---

### <a id='stats_permission_factory'></a>`STATS_PERMISSION_FACTORY`
| **Description** | Permission factory used by the statistics REST API.  This is a function which returns a permission g... |
|--------------|-----------|
| **Default Value** | `permissions_policy_lookup_factory` |
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1418); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L53) |

---

### <a id='stats_queries'></a>`STATS_QUERIES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1335); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L50) |

---

### <a id='stats_register_index_templates'></a>`STATS_REGISTER_INDEX_TEMPLATES`
| **Description** | Register templates as index templates.  Default behaviour will register the templates as search temp... |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L74) |

---

### <a id='stats_register_receivers'></a>`STATS_REGISTER_RECEIVERS`
| **Description** | Enable the registration of signal receivers.  Default is ``True``. The signal receivers are function... |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L16) |
| **Set by** | [`configure_stats`](api.html#oarepo_config.configure_stats) |

---

### <a id='templates_auto_reload'></a>`TEMPLATES_AUTO_RELOAD`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='testing'></a>`TESTING`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='theme_401_template'></a>`THEME_401_TEMPLATE`
| **Description** | The template used for 401 Unauthorized errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/401.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L144) |

---

### <a id='theme_403_template'></a>`THEME_403_TEMPLATE`
| **Description** | The template used for 403 Forbidden errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/403.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L147) |

---

### <a id='theme_404_template'></a>`THEME_404_TEMPLATE`
| **Description** | The template used for 404 Not Found errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/404.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L150) |

---

### <a id='theme_429_template'></a>`THEME_429_TEMPLATE`
| **Description** | The template used for 429 Too Many Requests errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/429.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L153) |

---

### <a id='theme_500_template'></a>`THEME_500_TEMPLATE`
| **Description** | The template used for 500 Internal Server Error errors. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/500.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L156) |

---

### <a id='theme_base_template'></a>`THEME_BASE_TEMPLATE`
| **Description** | Template which all templates in Invenio-Theme all extends from.  Defaults to value of :const:`BASE_T... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L67) |

---

### <a id='theme_cover_template'></a>`THEME_COVER_TEMPLATE`
| **Description** | Template which all cover templates in Invenio-Theme all extends from.  Defaults to value of :const:`... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_cover.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L73) |

---

### <a id='theme_css_template'></a>`THEME_CSS_TEMPLATE`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_error_template'></a>`THEME_ERROR_TEMPLATE`
| **Description** | Base template for error pages. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_error.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L85) |

---

### <a id='theme_footer_template'></a>`THEME_FOOTER_TEMPLATE`
| **Description** | Footer template which is normally included in :data:`BASE_TEMPLATE`. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/footer.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L50); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L279) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_frontpage'></a>`THEME_FRONTPAGE`
| **Description** | Enable or disable basic frontpage view. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L126); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L282) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_frontpage_logo'></a>`THEME_FRONTPAGE_LOGO`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_frontpage_template'></a>`THEME_FRONTPAGE_TEMPLATE`
| **Description** | Template for front page. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/frontpage.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L132); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L291) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_frontpage_title'></a>`THEME_FRONTPAGE_TITLE`
| **Description** | The title shown on the frontpage. |
|--------------|-----------|
| **Default Value** | `l'Invenio'` |
| **Type** | LazyString |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L129); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L285) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_generator'></a>`THEME_GENERATOR`
| **Description** | Generator meta tag to identify the software that generated the page.  Accepts a string or a func ret... |
|--------------|-----------|
| **Default Value** | `'Invenio'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L88); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L315) |

---

### <a id='theme_google_site_verification'></a>`THEME_GOOGLE_SITE_VERIFICATION`
| **Description** | List of Google Site Verification tokens to be used.  This adds the Google Site Verification into the... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L114) |

---

### <a id='theme_header_login_template'></a>`THEME_HEADER_LOGIN_TEMPLATE`
| **Description** | Header login template, included in :data:`THEME_HEADER_TEMPLATE`. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/header_login.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L47); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L294) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_header_template'></a>`THEME_HEADER_TEMPLATE`
| **Description** | Header template which is normally included in :data:`BASE_TEMPLATE`. |
|--------------|-----------|
| **Default Value** | `'invenio_theme/header.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L44); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L288) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_icons'></a>`THEME_ICONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L159) |

---

### <a id='theme_javascript_template'></a>`THEME_JAVASCRIPT_TEMPLATE`
| **Description** | Javascript assets template, normally included in :data:`BASE_TEMPLATE`.  The default template just i... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/javascript.html'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L53); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L333) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_logo'></a>`THEME_LOGO`
| **Description** | The logo to be used on the header and on the cover. |
|--------------|-----------|
| **Default Value** | `'images/invenio-white.svg'` |
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L120); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L321) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_logo_admin'></a>`THEME_LOGO_ADMIN`
| **Description** | The logo to be used on the admin views header. |
|--------------|-----------|
| **Default Value** | `'images/invenio-white.svg'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L123) |

---

### <a id='theme_mathjax_cdn'></a>`THEME_MATHJAX_CDN`
| **Description** | MathJax configuration for rendering mathematical formulas. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L186) |

---

### <a id='theme_meta_robot_tags'></a>`THEME_META_ROBOT_TAGS`
| **Description** | Robots meta tag to control indexing of the page.  Accepts a list of dicts that will be converted int... |
|--------------|-----------|
| **Default Value** | `<list>` |
| **Type** | list |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L94) |

---

### <a id='theme_searchbar'></a>`THEME_SEARCHBAR`
| **Description** | Enable or disable the header search bar. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L135) |

---

### <a id='theme_search_endpoint'></a>`THEME_SEARCH_ENDPOINT`
| **Description** | The endpoint for the search bar. |
|--------------|-----------|
| **Default Value** | `'/search'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L138) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_settings_template'></a>`THEME_SETTINGS_TEMPLATE`
| **Description** | Template which all settings templates in Invenio-Theme all extends from.  Defaults to value of :cons... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/page_settings.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L79) |

---

### <a id='theme_show_frontpage_intro_section'></a>`THEME_SHOW_FRONTPAGE_INTRO_SECTION`
| **Description** | Front page intro section visibility |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L330) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_sitename'></a>`THEME_SITENAME`
| **Description** | The name of the site to be used on the header and as a title. |
|--------------|-----------|
| **Default Value** | `l'Invenio'` |
| **Type** | LazyString |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L141); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L324) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_siteurl'></a>`THEME_SITEURL`
| **Default Value** | `'http://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L71) |

---

### <a id='theme_trackingcode_template'></a>`THEME_TRACKINGCODE_TEMPLATE`
| **Description** | Template for including a tracking code for web analytics.  The default template does not include any... |
|--------------|-----------|
| **Default Value** | `'invenio_theme/trackingcode.html'` |
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L61) |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='theme_twitterhandle'></a>`THEME_TWITTERHANDLE`
| **Description** | Twitter handle. |
|--------------|-----------|
| **Default Value** | `''` |
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L327) |

---

### <a id='trap_bad_request_errors'></a>`TRAP_BAD_REQUEST_ERRORS`
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

### <a id='trap_http_exceptions'></a>`TRAP_HTTP_EXCEPTIONS`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='trusted_hosts'></a>`TRUSTED_HOSTS`
| **Description** | A list of host/domain names that can be served.  This is a security measure to prevent HTTP Host hea... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L173); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L205) |

---

### <a id='type_checking'></a>`TYPE_CHECKING`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='userprofiles'></a>`USERPROFILES`
| **Description** | Enable or disable module extensions. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L11) |

---

### <a id='userprofiles_base_template'></a>`USERPROFILES_BASE_TEMPLATE`
| **Description** | Base templates for user profile module. |
|--------------|-----------|
| **Default Value** | `'invenio_userprofiles/base.html'` |
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L26) |

---

### <a id='userprofiles_email_enabled'></a>`USERPROFILES_EMAIL_ENABLED`
| **Description** | Include the user email in the profile form. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L14) |

---

### <a id='userprofiles_extend_security_forms'></a>`USERPROFILES_EXTEND_SECURITY_FORMS`
| **Description** | Extend the Invenio-Accounts user registration forms. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Sources** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L17); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L419) |

---

### <a id='userprofiles_profile_template'></a>`USERPROFILES_PROFILE_TEMPLATE`
| **Description** | Default profile template. |
|--------------|-----------|
| **Default Value** | `'invenio_userprofiles/settings/profile.html'` |
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L20) |

---

### <a id='userprofiles_profile_url'></a>`USERPROFILES_PROFILE_URL`
| **Description** | Default profile URL endpoint. |
|--------------|-----------|
| **Default Value** | `'/account/settings/profile/'` |
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L23) |

---

### <a id='userprofiles_read_only'></a>`USERPROFILES_READ_ONLY`
| **Description** | Make the user profiles read-only. |
|--------------|-----------|
| **Default Value** | `False` |
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L32) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters), [`configure_einfra_oidc`](api.html#oarepo_config.configure_einfra_oidc) |

---

### <a id='userprofiles_settings_template'></a>`USERPROFILES_SETTINGS_TEMPLATE`
| **Description** | Settings base templates for user profile module. |
|--------------|-----------|
| **Default Value** | `'invenio_userprofiles/settings/base.html'` |
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L29) |

---

### <a id='users_resources_avatar_colors'></a>`USERS_RESOURCES_AVATAR_COLORS`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L21) |

---

### <a id='users_resources_domains_org_schema'></a>`USERS_RESOURCES_DOMAINS_ORG_SCHEMA`
| **Description** | Domains organisation schema config. |
|--------------|-----------|
| **Default Value** | `OrgPropsSchema` |
| **Type** | unknown |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L311) |

---

### <a id='users_resources_domains_search'></a>`USERS_RESOURCES_DOMAINS_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L149) |

---

### <a id='users_resources_domains_search_facets'></a>`USERS_RESOURCES_DOMAINS_SEARCH_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L215) |

---

### <a id='users_resources_domains_sort_options'></a>`USERS_RESOURCES_DOMAINS_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L167) |

---

### <a id='users_resources_groups_admin_facets'></a>`USERS_RESOURCES_GROUPS_ADMIN_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L279) |

---

### <a id='users_resources_groups_admin_search'></a>`USERS_RESOURCES_GROUPS_ADMIN_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L273) |

---

### <a id='users_resources_groups_admin_sort_options'></a>`USERS_RESOURCES_GROUPS_ADMIN_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L249) |

---

### <a id='users_resources_groups_enabled'></a>`USERS_RESOURCES_GROUPS_ENABLED`
| **Description** | Config to enable features related to existence of groups. |
|--------------|-----------|
| **Default Value** | `True` |
| **Type** | bool |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L314) |

---

### <a id='users_resources_moderation_lock_default_timeout'></a>`USERS_RESOURCES_MODERATION_LOCK_DEFAULT_TIMEOUT`
| **Description** | Default timeout, in seconds, to lock a user when moderating. |
|--------------|-----------|
| **Default Value** | `30` |
| **Type** | int |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L142) |

---

### <a id='users_resources_moderation_lock_renewal_timeout'></a>`USERS_RESOURCES_MODERATION_LOCK_RENEWAL_TIMEOUT`
| **Description** | Renewal timeout, in seconds, to increase the lock time for a user when moderating. |
|--------------|-----------|
| **Default Value** | `120` |
| **Type** | int |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L145) |

---

### <a id='users_resources_protected_group_names'></a>`USERS_RESOURCES_PROTECTED_GROUP_NAMES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L289) |

---

### <a id='users_resources_search'></a>`USERS_RESOURCES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L54) |

---

### <a id='users_resources_search_facets'></a>`USERS_RESOURCES_SEARCH_FACETS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L99) |

---

### <a id='users_resources_service_schema'></a>`USERS_RESOURCES_SERVICE_SCHEMA`
| **Description** | Schema used by the users service. |
|--------------|-----------|
| **Default Value** | `NotificationsUserSchema` |
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1505); [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L51) |

---

### <a id='users_resources_sort_options'></a>`USERS_RESOURCES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L67) |

---

### <a id='user_dashboard_menu_overrides'></a>`USER_DASHBOARD_MENU_OVERRIDES`
| **Description** | Overrides for "dashboard" menu. |
|--------------|-----------|
| **Default Value** | `<dict>` |
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1532) |

---

### <a id='use_x_sendfile'></a>`USE_X_SENDFILE`
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

### <a id='vcs_template_index'></a>`VCS_TEMPLATE_INDEX`
| **Default Value** | `'invenio_vcs/rdm-index.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1610) |

---

### <a id='vcs_template_index_item'></a>`VCS_TEMPLATE_INDEX_ITEM`
| **Default Value** | `'invenio_vcs/rdm-index-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1611) |

---

### <a id='vcs_template_release_item'></a>`VCS_TEMPLATE_RELEASE_ITEM`
| **Default Value** | `'invenio_vcs/rdm-release-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1614) |

---

### <a id='vcs_template_repo_switch'></a>`VCS_TEMPLATE_REPO_SWITCH`
| **Default Value** | `'invenio_vcs/rdm-repo-switch.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1613) |

---

### <a id='vcs_template_view'></a>`VCS_TEMPLATE_VIEW`
| **Default Value** | `'invenio_vcs/rdm-view.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1612) |

---

### <a id='vocabularies_affiliations_edmo_country_mapping'></a>`VOCABULARIES_AFFILIATIONS_EDMO_COUNTRY_MAPPING`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L236) |

---

### <a id='vocabularies_affiliation_schemes'></a>`VOCABULARIES_AFFILIATION_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L66) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_awards_ec_ror_id'></a>`VOCABULARIES_AWARDS_EC_ROR_ID`
| **Description** | ROR ID for EC funder. |
|--------------|-----------|
| **Default Value** | `'00k4n6c32'` |
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L154) |

---

### <a id='vocabularies_awards_openaire_funders'></a>`VOCABULARIES_AWARDS_OPENAIRE_FUNDERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L88) |

---

### <a id='vocabularies_award_schemes'></a>`VOCABULARIES_AWARD_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L82) |

---

### <a id='vocabularies_custom_vocabulary_types'></a>`VOCABULARIES_CUSTOM_VOCABULARY_TYPES`
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L170) |

---

### <a id='vocabularies_datastream_readers'></a>`VOCABULARIES_DATASTREAM_READERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L179); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L747) |
| **Set by** | [`configure_datastreams`](api.html#oarepo_config.configure_datastreams), [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_datastream_transformers'></a>`VOCABULARIES_DATASTREAM_TRANSFORMERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L195); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L759) |
| **Set by** | [`configure_datastreams`](api.html#oarepo_config.configure_datastreams), [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_datastream_writers'></a>`VOCABULARIES_DATASTREAM_WRITERS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L200); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L771) |
| **Set by** | [`configure_datastreams`](api.html#oarepo_config.configure_datastreams), [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_funder_doi_prefix'></a>`VOCABULARIES_FUNDER_DOI_PREFIX`
| **Description** | DOI prefix for the identifier formed with the FundRef id. |
|--------------|-----------|
| **Default Value** | `'10.13039'` |
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L79) |

---

### <a id='vocabularies_funder_schemes'></a>`VOCABULARIES_FUNDER_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L73) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_identifier_schemes'></a>`VOCABULARIES_IDENTIFIER_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L43) |

---

### <a id='vocabularies_names_schemes'></a>`VOCABULARIES_NAMES_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L157) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_orcid_access_key'></a>`VOCABULARIES_ORCID_ACCESS_KEY`
| **Description** | ORCID access key to access the s3 bucket. |
|--------------|-----------|
| **Default Value** | `'CHANGEME'` |
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L241) |

---

### <a id='vocabularies_orcid_org_ids_mapping_path'></a>`VOCABULARIES_ORCID_ORG_IDS_MAPPING_PATH`
| **Description** | Path to the CSV file for mapping ORCiD organization IDs to affiliation IDs.  The path can be specifi... |
|--------------|-----------|
| **Default Value** | `None` |
| **Type** | NoneType |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L254) |

---

### <a id='vocabularies_orcid_secret_key'></a>`VOCABULARIES_ORCID_SECRET_KEY`
| **Description** | ORCID secret key to access the s3 bucket. |
|--------------|-----------|
| **Default Value** | `'CHANGEME'` |
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L243) |

---

### <a id='vocabularies_orcid_summaries_bucket'></a>`VOCABULARIES_ORCID_SUMMARIES_BUCKET`
| **Description** | ORCID summaries bucket name. |
|--------------|-----------|
| **Default Value** | `'v3.0-summaries'` |
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L245) |

---

### <a id='vocabularies_orcid_sync_max_workers'></a>`VOCABULARIES_ORCID_SYNC_MAX_WORKERS`
| **Description** | ORCID max number of simultaneous workers/connections. |
|--------------|-----------|
| **Default Value** | `32` |
| **Type** | int |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L247) |

---

### <a id='vocabularies_orcid_sync_since'></a>`VOCABULARIES_ORCID_SYNC_SINCE`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L249) |

---

### <a id='vocabularies_resource_config'></a>`VOCABULARIES_RESOURCE_CONFIG`
| **Description** | Configure the resource. |
|--------------|-----------|
| **Default Value** | `VocabulariesResourceConfig` |
| **Type** | unknown |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L37) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_service_config'></a>`VOCABULARIES_SERVICE_CONFIG`
| **Description** | Configure the service. |
|--------------|-----------|
| **Default Value** | `VocabulariesServiceConfig` |
| **Type** | unknown |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L40) |
| **Set by** | [`configure_generic_parameters`](api.html#oarepo_config.configure_generic_parameters) |

---

### <a id='vocabularies_subjects_euroscivoc_file_url'></a>`VOCABULARIES_SUBJECTS_EUROSCIVOC_FILE_URL`
| **Description** | Subject EuroSciVoc file download link. |
|--------------|-----------|
| **Default Value** | `'https://publications.europa.eu/resource/distribution/euroscivoc/rdf/skos_ap_eu/EuroSciVoc-skos-ap-e...` |
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L225) |

---

### <a id='vocabularies_subjects_gemet_file_url'></a>`VOCABULARIES_SUBJECTS_GEMET_FILE_URL`
| **Default Value** | `'https://www.eionet.europa.eu/gemet/latest/gemet.rdf.gz'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L228) |

---

### <a id='vocabularies_subjects_nvs_file_url'></a>`VOCABULARIES_SUBJECTS_NVS_FILE_URL`
| **Description** | Subject NVS-P02 file download link. |
|--------------|-----------|
| **Default Value** | `'http://vocab.nerc.ac.uk/collection/P02/current/?_profile=nvs&_mediatype=application/rdf+xml'` |
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L233) |

---

### <a id='vocabularies_subjects_schemes'></a>`VOCABULARIES_SUBJECTS_SCHEMES`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L164) |

---

### <a id='vocabularies_types_search'></a>`VOCABULARIES_TYPES_SEARCH`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L219) |

---

### <a id='vocabularies_types_sort_options'></a>`VOCABULARIES_TYPES_SORT_OPTIONS`
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L207) |

---

### <a id='webpackext_manifest_path'></a>`WEBPACKEXT_MANIFEST_PATH`
| **Default Value** | `'dist/manifest.json'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='webpackext_npm_pkg_cls'></a>`WEBPACKEXT_NPM_PKG_CLS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='webpackext_project'></a>`WEBPACKEXT_PROJECT`
| **Default Value** | `'invenio_assets.webpack:webpack_project'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |
| **Set by** | [`configure_ui`](api.html#oarepo_config.configure_ui) |

---

### <a id='webpackext_project_builddir'></a>`WEBPACKEXT_PROJECT_BUILDDIR`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/assets'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='webpackext_project_distdir'></a>`WEBPACKEXT_PROJECT_DISTDIR`
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static/...` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='webpackext_project_disturl'></a>`WEBPACKEXT_PROJECT_DISTURL`
| **Default Value** | `'/static/dist'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

### <a id='workflows'></a>`WORKFLOWS`
| **Type** | configured by function |
|--------------|-----------|
| **Source** | oarepo_config |
| **Set by** | [`register_workflow`](api.html#oarepo_config.register_workflow) |

---

