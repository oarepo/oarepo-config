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
| [`ACCESS_​ACTION_​CACHE_​PREFIX`](#access_action_cache_prefix) | str | - |
| [`ACCESS_​CACHE`](#access_cache) | NoneType | - |
| [`ACCESS_​LOAD_​SYSTEM_​ROLE_​NEEDS`](#access_load_system_role_needs) | bool | - |
| [`ACCOUNTS`](#accounts) | bool | - |
| [`ACCOUNTS_​BASE_​TEMPLATE`](#accounts_base_template) | str | - |
| [`ACCOUNTS_​CONFIRM_​EMAIL_​ENDPOINT`](#accounts_confirm_email_endpoint) | NoneType | - |
| [`ACCOUNTS_​COVER_​TEMPLATE`](#accounts_cover_template) | str | - |
| [`ACCOUNTS_​DEFAULT_​EMAIL_​VISIBILITY`](#accounts_default_email_visibility) | str | - |
| [`ACCOUNTS_​DEFAULT_​USERS_​VERIFIED`](#accounts_default_users_verified) | bool | - |
| [`ACCOUNTS_​DEFAULT_​USER_​VISIBILITY`](#accounts_default_user_visibility) | str | - |
| [`ACCOUNTS_​FORGOT_​PASSWORD_​EMAIL_​RATELIMIT`](#accounts_forgot_password_email_ratelimit) | NoneType | - |
| [`ACCOUNTS_​FORGOT_​PASSWORD_​EMAIL_​RATELIMIT_​KEY_​PREFIX`](#accounts_forgot_password_email_ratelimit_key_prefix) | str | - |
| [`ACCOUNTS_​FORGOT_​PASSWORD_​EMAIL_​RATELIMIT_​MSG`](#accounts_forgot_password_email_ratelimit_msg) | LazyString | - |
| [`ACCOUNTS_​JWT_​ALOGORITHM`](#accounts_jwt_alogorithm) | str | - |
| [`ACCOUNTS_​JWT_​CREATION_​FACTORY`](#accounts_jwt_creation_factory) | str | - |
| [`ACCOUNTS_​JWT_​DECODE_​FACTORY`](#accounts_jwt_decode_factory) | str | - |
| [`ACCOUNTS_​JWT_​DOM_​TOKEN`](#accounts_jwt_dom_token) | bool | - |
| [`ACCOUNTS_​JWT_​DOM_​TOKEN_​TEMPLATE`](#accounts_jwt_dom_token_template) | str | - |
| [`ACCOUNTS_​JWT_​ENABLE`](#accounts_jwt_enable) | bool | - |
| [`ACCOUNTS_​JWT_​EXPIRATION_​DELTA`](#accounts_jwt_expiration_delta) | timedelta | - |
| [`ACCOUNTS_​JWT_​SECRET_​KEY`](#accounts_jwt_secret_key) | str | - |
| [`ACCOUNTS_​LOCAL_​LOGIN_​ENABLED`](#accounts_local_login_enabled) | bool | `configure_generic_parameters` |
| [`ACCOUNTS_​LOGIN_​RATELIMIT`](#accounts_login_ratelimit) | NoneType | - |
| [`ACCOUNTS_​LOGIN_​RATELIMIT_​KEY_​PREFIX`](#accounts_login_ratelimit_key_prefix) | str | - |
| [`ACCOUNTS_​LOGIN_​RATELIMIT_​MSG`](#accounts_login_ratelimit_msg) | LazyString | - |
| [`ACCOUNTS_​LOGIN_​VIEW_​FUNCTION`](#accounts_login_view_function) | unknown | `configure_generic_parameters` |
| [`ACCOUNTS_​REGISTER_​BLUEPRINT`](#accounts_register_blueprint) | NoneType | - |
| [`ACCOUNTS_​RESET_​PASSWORD_​ENDPOINT`](#accounts_reset_password_endpoint) | NoneType | - |
| [`ACCOUNTS_​REST_​AUTH_​VIEWS`](#accounts_rest_auth_views) | dict | - |
| [`ACCOUNTS_​REST_​CONFIRM_​EMAIL_​ENDPOINT`](#accounts_rest_confirm_email_endpoint) | str | - |
| [`ACCOUNTS_​REST_​RESET_​PASSWORD_​ENDPOINT`](#accounts_rest_reset_password_endpoint) | str | - |
| [`ACCOUNTS_​RETENTION_​PERIOD`](#accounts_retention_period) | timedelta | - |
| [`ACCOUNTS_​SEND_​CONFIRMATION_​RATELIMIT`](#accounts_send_confirmation_ratelimit) | NoneType | - |
| [`ACCOUNTS_​SEND_​CONFIRMATION_​RATELIMIT_​KEY_​PREFIX`](#accounts_send_confirmation_ratelimit_key_prefix) | str | - |
| [`ACCOUNTS_​SEND_​CONFIRMATION_​RATELIMIT_​MSG`](#accounts_send_confirmation_ratelimit_msg) | LazyString | - |
| [`ACCOUNTS_​SESSION_​ACTIVITY_​ENABLED`](#accounts_session_activity_enabled) | bool | - |
| [`ACCOUNTS_​SESSION_​REDIS_​URL`](#accounts_session_redis_url) | NoneType | `configure_generic_parameters` |
| [`ACCOUNTS_​SESSION_​STORE_​FACTORY`](#accounts_session_store_factory) | str | - |
| [`ACCOUNTS_​SETTINGS_​SECURITY_​TEMPLATE`](#accounts_settings_security_template) | str | - |
| [`ACCOUNTS_​SETTINGS_​TEMPLATE`](#accounts_settings_template) | str | - |
| [`ACCOUNTS_​SITENAME`](#accounts_sitename) | LazyString | - |
| [`ACCOUNTS_​USERINFO_​HEADERS`](#accounts_userinfo_headers) | bool | - |
| [`ACCOUNTS_​USERNAME_​REGEX`](#accounts_username_regex) | str | - |
| [`ACCOUNTS_​USERNAME_​RULES_​TEXT`](#accounts_username_rules_text) | LazyString | - |
| [`ACCOUNTS_​USER_​PREFERENCES_​SCHEMA`](#accounts_user_preferences_schema) | UserPreferencesSchema | - |
| [`ACCOUNTS_​USER_​PROFILE_​SCHEMA`](#accounts_user_profile_schema) | UserProfileSchema | - |
| [`ACCOUNTS_​USE_​CELERY`](#accounts_use_celery) | bool | - |
| [`ADMINISTRATION_​APPNAME`](#administration_appname) | str | - |
| [`ADMINISTRATION_​BASE_​TEMPLATE`](#administration_base_template) | str | - |
| [`ADMINISTRATION_​DASHBOARD_​VIEW`](#administration_dashboard_view) | str | - |
| [`ADMINISTRATION_​DISPLAY_​VERSIONS`](#administration_display_versions) | list | - |
| [`ADMINISTRATION_​THEME_​BASE_​TEMPLATE`](#administration_theme_base_template) | str | `configure_ui` |
| [`ADMIN_​BASE_​TEMPLATE`](#admin_base_template) | str | - |
| [`ALEMBIC`](#alembic) | dict | - |
| [`ALEMBIC_​CONTEXT`](#alembic_context) | dict | - |
| [`ALLOWED_​HTML_​ATTRS`](#allowed_html_attrs) | dict | - |
| [`ALLOWED_​HTML_​TAGS`](#allowed_html_tags) | list | - |
| [`APPLICATION_​ROOT`](#application_root) | str | - |
| [`APP_​DEFAULT_​SECURE_​HEADERS`](#app_default_secure_headers) | dict | `configure_ui`, `configure_generic_parameters` |
| [`APP_​ENABLE_​SECURE_​HEADERS`](#app_enable_secure_headers) | bool | - |
| [`APP_​HEALTH_​BLUEPRINT_​ENABLED`](#app_health_blueprint_enabled) | bool | - |
| [`APP_​LOGS_​PERMISSION_​POLICY`](#app_logs_permission_policy) | unknown | `configure_jobs` |
| [`APP_​RDM_​ADMIN_​EMAIL_​RECIPIENT`](#app_rdm_admin_email_recipient) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​AUTOCOMPLETE_​NAMES`](#app_rdm_deposit_form_autocomplete_names) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​CUSTOM_​FIELD_​DEFAULTS`](#app_rdm_deposit_form_custom_field_defaults) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​DEFAULTS`](#app_rdm_deposit_form_defaults) | dict | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​PUBLISH_​MODAL_​EXTRA`](#app_rdm_deposit_form_publish_modal_extra) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​QUOTA`](#app_rdm_deposit_form_quota) | unknown | `configure_files` |
| [`APP_​RDM_​DEPOSIT_​FORM_​TEMPLATE`](#app_rdm_deposit_form_template) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​NG_​FILES_​UI_​ENABLED`](#app_rdm_deposit_ng_files_ui_enabled) | unknown | `configure_ui` |
| [`APP_​RDM_​DETAIL_​SIDE_​BAR_​TEMPLATES`](#app_rdm_detail_side_bar_templates) | unknown | `configure_ui` |
| [`APP_​RDM_​DISPLAY_​DECIMAL_​FILE_​SIZES`](#app_rdm_display_decimal_file_sizes) | unknown | - |
| [`APP_​RDM_​FILES_​INTEGRITY_​REPORT_​SUBJECT`](#app_rdm_files_integrity_report_subject) | unknown | - |
| [`APP_​RDM_​FILES_​INTEGRITY_​REPORT_​TEMPLATE`](#app_rdm_files_integrity_report_template) | unknown | - |
| [`APP_​RDM_​IDENTIFIER_​SCHEMES_​UI`](#app_rdm_identifier_schemes_ui) | unknown | `configure_generic_parameters` |
| [`APP_​RDM_​MODERATION_​REQUEST_​FACETS`](#app_rdm_moderation_request_facets) | dict | - |
| [`APP_​RDM_​MODERATION_​REQUEST_​SEARCH`](#app_rdm_moderation_request_search) | dict | - |
| [`APP_​RDM_​MODERATION_​REQUEST_​SORT_​OPTIONS`](#app_rdm_moderation_request_sort_options) | dict | - |
| [`APP_​RDM_​PAGES`](#app_rdm_pages) | dict | - |
| [`APP_​RDM_​RECORDS_​EXPORT_​URL`](#app_rdm_records_export_url) | unknown | - |
| [`APP_​RDM_​RECORD_​EXPORTERS`](#app_rdm_record_exporters) | unknown | - |
| [`APP_​RDM_​RECORD_​LANDING_​PAGE_​EXTERNAL_​LINKS`](#app_rdm_record_landing_page_external_links) | list | - |
| [`APP_​RDM_​RECORD_​LANDING_​PAGE_​FAIR_​SIGNPOSTING_​LEVEL_​1_​ENABLED`](#app_rdm_record_landing_page_fair_signposting_level_1_enabled) | unknown | - |
| [`APP_​RDM_​RECORD_​LANDING_​PAGE_​TEMPLATE`](#app_rdm_record_landing_page_template) | str | - |
| [`APP_​RDM_​RECORD_​THUMBNAIL_​SIZES`](#app_rdm_record_thumbnail_sizes) | unknown | - |
| [`APP_​RDM_​ROUTES`](#app_rdm_routes) | dict | - |
| [`APP_​RDM_​SUBCOMMUNITIES_​LABEL`](#app_rdm_subcommunities_label) | unknown | - |
| [`APP_​RDM_​USER_​DASHBOARD_​ROUTES`](#app_rdm_user_dashboard_routes) | dict | - |
| [`APP_​REQUESTID_​HEADER`](#app_requestid_header) | str | - |
| [`APP_​THEME`](#app_theme) | NoneType | `configure_ui` |
| [`ASSETS_​BUILDER`](#assets_builder) | configured by function | `configure_ui` |
| [`AUDIT_​LOGS_​DISABLED_​ACTIONS`](#audit_logs_disabled_actions) | set | - |
| [`AUDIT_​LOGS_​ENABLED`](#audit_logs_enabled) | bool | `configure_generic_parameters` |
| [`AUDIT_​LOGS_​FACETS`](#audit_logs_facets) | dict | - |
| [`AUDIT_​LOGS_​SEARCH`](#audit_logs_search) | dict | - |
| [`AUDIT_​LOGS_​SORT_​OPTIONS`](#audit_logs_sort_options) | dict | - |
| [`BABEL_​DEFAULT_​LOCALE`](#babel_default_locale) | str | `configure_generic_parameters` |
| [`BABEL_​DEFAULT_​TIMEZONE`](#babel_default_timezone) | unknown | `configure_generic_parameters` |
| [`BANNERS_​CATEGORIES`](#banners_categories) | list | - |
| [`BANNERS_​CATEGORIES_​TO_​STYLE`](#banners_categories_to_style) | unknown | - |
| [`BANNERS_​SEARCH`](#banners_search) | dict | - |
| [`BANNERS_​SORT_​OPTIONS`](#banners_sort_options) | dict | - |
| [`BASE_​TEMPLATE`](#base_template) | str | `configure_ui` |
| [`BROKER_​URL`](#broker_url) | str | `configure_generic_parameters` |
| [`CACHE_​IS_​AUTHENTICATED_​CALLBACK`](#cache_is_authenticated_callback) | NoneType | - |
| [`CACHE_​KEY_​PREFIX`](#cache_key_prefix) | str | - |
| [`CACHE_​REDIS_​URL`](#cache_redis_url) | str | `configure_generic_parameters` |
| [`CACHE_​TYPE`](#cache_type) | str | - |
| [`CELERY_​ACCEPT_​CONTENT`](#celery_accept_content) | list | - |
| [`CELERY_​BEAT_​SCHEDULE`](#celery_beat_schedule) | unknown | `configure_cron` |
| [`CELERY_​BROKER_​URL`](#celery_broker_url) | str | `configure_generic_parameters` |
| [`CELERY_​RESULT_​BACKEND`](#celery_result_backend) | str | `configure_generic_parameters` |
| [`CELERY_​RESULT_​SERIALIZER`](#celery_result_serializer) | str | - |
| [`CELERY_​TASK_​SERIALIZER`](#celery_task_serializer) | str | - |
| [`CHECKS_​COMMUNITIES_​SERVICE_​COMPONENTS`](#checks_communities_service_components) | unknown | - |
| [`CHECKS_​ENABLED`](#checks_enabled) | bool | `configure_llm` |
| [`CHECKS_​GENERIC_​COMMUNITY`](#checks_generic_community) | str | `configure_llm` |
| [`COLLECTIONS_​BASE_​TEMPLATE`](#collections_base_template) | str | - |
| [`COLLECTIONS_​MAX_​COLLECTIONS_​PER_​TREE`](#collections_max_collections_per_tree) | int | - |
| [`COLLECTIONS_​MAX_​DEPTH`](#collections_max_depth) | int | - |
| [`COLLECTIONS_​MAX_​TREES`](#collections_max_trees) | int | - |
| [`COLLECTIONS_​PERMISSION_​POLICY`](#collections_permission_policy) | unknown | - |
| [`COLLECT_​STATIC_​ROOT`](#collect_static_root) | str | - |
| [`COLLECT_​STORAGE`](#collect_storage) | str | `configure_generic_parameters` |
| [`COMMUNITIES_​ALLOW_​MEMBERSHIP_​REQUESTS`](#communities_allow_membership_requests) | bool | - |
| [`COMMUNITIES_​ALLOW_​RESTRICTED`](#communities_allow_restricted) | bool | - |
| [`COMMUNITIES_​ALWAYS_​SHOW_​CREATE_​LINK`](#communities_always_show_create_link) | bool | - |
| [`COMMUNITIES_​COLLECTIONS_​ENABLED`](#communities_collections_enabled) | bool | - |
| [`COMMUNITIES_​CUSTOM_​FIELDS`](#communities_custom_fields) | list | - |
| [`COMMUNITIES_​CUSTOM_​FIELDS_​UI`](#communities_custom_fields_ui) | list | - |
| [`COMMUNITIES_​DEFAULT_​RECORD_​SUBMISSION_​POLICY`](#communities_default_record_submission_policy) | RecordSubmissionPolicyEnum | - |
| [`COMMUNITIES_​ERROR_​HANDLERS`](#communities_error_handlers) | unknown | - |
| [`COMMUNITIES_​FACETS`](#communities_facets) | dict | - |
| [`COMMUNITIES_​IDENTITIES_​CACHE_​HANDLER`](#communities_identities_cache_handler) | str | - |
| [`COMMUNITIES_​IDENTITIES_​CACHE_​REDIS_​URL`](#communities_identities_cache_redis_url) | str | `configure_generic_parameters` |
| [`COMMUNITIES_​IDENTITIES_​CACHE_​TIME`](#communities_identities_cache_time) | int | - |
| [`COMMUNITIES_​INVITATIONS_​EXPIRES_​IN`](#communities_invitations_expires_in) | timedelta | - |
| [`COMMUNITIES_​INVITATIONS_​SEARCH`](#communities_invitations_search) | dict | - |
| [`COMMUNITIES_​INVITATIONS_​SORT_​OPTIONS`](#communities_invitations_sort_options) | dict | - |
| [`COMMUNITIES_​LOGO_​MAX_​FILE_​SIZE`](#communities_logo_max_file_size) | int | - |
| [`COMMUNITIES_​MEMBERSHIP_​REQUESTS_​DEFAULT_​ROLE`](#communities_membership_requests_default_role) | str | - |
| [`COMMUNITIES_​MEMBERSHIP_​REQUESTS_​EXPIRES_​IN`](#communities_membership_requests_expires_in) | timedelta | - |
| [`COMMUNITIES_​MEMBERSHIP_​REQUESTS_​FACETS`](#communities_membership_requests_facets) | dict | - |
| [`COMMUNITIES_​MEMBERSHIP_​REQUESTS_​SEARCH`](#communities_membership_requests_search) | dict | - |
| [`COMMUNITIES_​MEMBERS_​FACETS`](#communities_members_facets) | dict | - |
| [`COMMUNITIES_​MEMBERS_​SEARCH`](#communities_members_search) | dict | - |
| [`COMMUNITIES_​MEMBERS_​SORT_​OPTIONS`](#communities_members_sort_options) | dict | - |
| [`COMMUNITIES_​NAMESPACES`](#communities_namespaces) | dict | - |
| [`COMMUNITIES_​OAI_​SETS_​PREFIX`](#communities_oai_sets_prefix) | str | - |
| [`COMMUNITIES_​PERMISSION_​POLICY`](#communities_permission_policy) | configured by function | `configure_communities` |
| [`COMMUNITIES_​RECORDS_​SEARCH`](#communities_records_search) | unknown | - |
| [`COMMUNITIES_​RECORDS_​SEARCH_​ALL`](#communities_records_search_all) | bool | - |
| [`COMMUNITIES_​REGISTER_​UI_​BLUEPRINT`](#communities_register_ui_blueprint) | configured by function | `configure_communities` |
| [`COMMUNITIES_​REQUESTS_​SEARCH`](#communities_requests_search) | dict | - |
| [`COMMUNITIES_​ROLES`](#communities_roles) | list | `configure_communities` |
| [`COMMUNITIES_​ROUTES`](#communities_routes) | dict | - |
| [`COMMUNITIES_​SEARCH`](#communities_search) | dict | - |
| [`COMMUNITIES_​SEARCH_​SORT_​BY_​VERIFIED`](#communities_search_sort_by_verified) | bool | - |
| [`COMMUNITIES_​SERVICE_​COMPONENTS`](#communities_service_components) | list | - |
| [`COMMUNITIES_​SORT_​OPTIONS`](#communities_sort_options) | dict | - |
| [`COMMUNITIES_​SUBCOMMUNITIES_​FACETS`](#communities_subcommunities_facets) | dict | - |
| [`COMMUNITIES_​SUBCOMMUNITIES_​SEARCH`](#communities_subcommunities_search) | dict | - |
| [`COMMUNITIES_​SUB_​INVITATION_​REQUEST_​CLS`](#communities_sub_invitation_request_cls) | unknown | - |
| [`COMMUNITIES_​SUB_​REQUEST_​CLS`](#communities_sub_request_cls) | unknown | - |
| [`CORS_​EXPOSE_​HEADERS`](#cors_expose_headers) | unknown | - |
| [`CORS_​RESOURCES`](#cors_resources) | unknown | - |
| [`CORS_​SEND_​WILDCARD`](#cors_send_wildcard) | unknown | - |
| [`COVER_​TEMPLATE`](#cover_template) | str | `configure_ui` |
| [`CROSSREF_​ADDITIONAL_​PREFIXES`](#crossref_additional_prefixes) | list | - |
| [`CROSSREF_​DEPOSITOR`](#crossref_depositor) | str | - |
| [`CROSSREF_​EMAIL`](#crossref_email) | str | - |
| [`CROSSREF_​ENABLED`](#crossref_enabled) | bool | - |
| [`CROSSREF_​FORMAT`](#crossref_format) | str | - |
| [`CROSSREF_​PASSWORD`](#crossref_password) | str | - |
| [`CROSSREF_​PREFIX`](#crossref_prefix) | str | - |
| [`CROSSREF_​REGISTRANT`](#crossref_registrant) | str | - |
| [`CROSSREF_​TEST_​MODE`](#crossref_test_mode) | bool | - |
| [`CROSSREF_​URL`](#crossref_url) | str | - |
| [`CROSSREF_​USERNAME`](#crossref_username) | str | - |
| [`CSP`](#csp) | configured by function | `configure_ui` |
| [`CSRF_​ALLOWED_​CHARS`](#csrf_allowed_chars) | str | - |
| [`CSRF_​COOKIE_​NAME`](#csrf_cookie_name) | str | - |
| [`CSRF_​COOKIE_​SAMESITE`](#csrf_cookie_samesite) | str | - |
| [`CSRF_​FORCE_​SECURE_​REFERER`](#csrf_force_secure_referer) | bool | - |
| [`CSRF_​HEADER`](#csrf_header) | str | - |
| [`CSRF_​METHODS`](#csrf_methods) | list | - |
| [`CSRF_​SECRET_​SALT`](#csrf_secret_salt) | str | - |
| [`CSRF_​TOKEN_​EXPIRES_​IN`](#csrf_token_expires_in) | int | - |
| [`CSRF_​TOKEN_​GRACE_​PERIOD`](#csrf_token_grace_period) | int | - |
| [`CSRF_​TOKEN_​LENGTH`](#csrf_token_length) | int | - |
| [`DASHBOARD_​RECORD_​CREATE_​URL`](#dashboard_record_create_url) | configured by function | `configure_ui`, `configure_generic_parameters` |
| [`DATACITE_​ADDITIONAL_​PREFIXES`](#datacite_additional_prefixes) | list | - |
| [`DATACITE_​DATACENTER_​SYMBOL`](#datacite_datacenter_symbol) | str | - |
| [`DATACITE_​ENABLED`](#datacite_enabled) | bool | - |
| [`DATACITE_​FORMAT`](#datacite_format) | str | - |
| [`DATACITE_​PASSWORD`](#datacite_password) | str | - |
| [`DATACITE_​PREFIX`](#datacite_prefix) | str | - |
| [`DATACITE_​TEST_​MODE`](#datacite_test_mode) | bool | `configure_generic_parameters` |
| [`DATACITE_​URL`](#datacite_url) | str | - |
| [`DATACITE_​USERNAME`](#datacite_username) | str | - |
| [`DB_​VERSIONING`](#db_versioning) | bool | - |
| [`DB_​VERSIONING_​USER_​MODEL`](#db_versioning_user_model) | unknown | - |
| [`DEBUG`](#debug) | bool | - |
| [`DEBUG_​TB_​INTERCEPT_​REDIRECTS`](#debug_tb_intercept_redirects) | unknown | - |
| [`DEFAULT_​COMMUNITIES_​CUSTOM_​FIELDS`](#default_communities_custom_fields) | list | - |
| [`DEFAULT_​COMMUNITIES_​CUSTOM_​FIELDS_​UI`](#default_communities_custom_fields_ui) | list | - |
| [`DEFAULT_​WORKFLOW_​EVENTS`](#default_workflow_events) | dict | - |
| [`DEPLOYMENT_​VERSION`](#deployment_version) | configured by function | `configure_ui` |
| [`DISPLAY_​NEW_​COMMUNITIES`](#display_new_communities) | bool | - |
| [`DISPLAY_​USER_​COMMUNITIES`](#display_user_communities) | bool | - |
| [`DOI_​SETTINGS_​FACETS`](#doi_settings_facets) | dict | - |
| [`DOI_​SETTINGS_​SEARCH`](#doi_settings_search) | dict | - |
| [`DOI_​SETTINGS_​SORT_​OPTIONS`](#doi_settings_sort_options) | dict | - |
| [`EINFRA`](#einfra) | configured by function | `configure_einfra_oidc` |
| [`EINFRA_​CAPABILITIES_​ATTRIBUTE_​NAME`](#einfra_capabilities_attribute_name) | str | - |
| [`EINFRA_​ENTITLEMENTS_​PARSER`](#einfra_entitlements_parser) | NoneType | `configure_einfra_oidc` |
| [`EINFRA_​ENTITLEMENT_​NAMESPACES`](#einfra_entitlement_namespaces) | set | - |
| [`EINFRA_​ENTITLEMENT_​PREFIX`](#einfra_entitlement_prefix) | str | - |
| [`EINFRA_​LAST_​DUMP_​PATH`](#einfra_last_dump_path) | str | - |
| [`EINFRA_​LOGIN_​APP`](#einfra_login_app) | configured by function | `configure_einfra_oidc` |
| [`EINFRA_​RSA_​KEY`](#einfra_rsa_key) | bytes | - |
| [`EINFRA_​TOKEN_​EXCHANGE_​ISSUER`](#einfra_token_exchange_issuer) | str | - |
| [`EINFRA_​TOKEN_​EXCHANGE_​PUBLIC_​KEY`](#einfra_token_exchange_public_key) | bytes | - |
| [`EINFRA_​USER_​DISPLAY_​NAME_​ATTRIBUTE`](#einfra_user_display_name_attribute) | str | - |
| [`EINFRA_​USER_​DUMP_​S3_​ACCESS_​KEY`](#einfra_user_dump_s3_access_key) | str | - |
| [`EINFRA_​USER_​DUMP_​S3_​BUCKET`](#einfra_user_dump_s3_bucket) | str | - |
| [`EINFRA_​USER_​DUMP_​S3_​ENDPOINT`](#einfra_user_dump_s3_endpoint) | str | - |
| [`EINFRA_​USER_​DUMP_​S3_​SECRET_​KEY`](#einfra_user_dump_s3_secret_key) | str | - |
| [`EINFRA_​USER_​ID_​DUMP_​ATTRIBUTE`](#einfra_user_id_dump_attribute) | str | - |
| [`EINFRA_​USER_​ORGANIZATION_​ATTRIBUTE`](#einfra_user_organization_attribute) | str | - |
| [`EINFRA_​USER_​PREFERRED_​MAIL_​ATTRIBUTE`](#einfra_user_preferred_mail_attribute) | str | - |
| [`EXPLAIN_​TEMPLATE_​LOADING`](#explain_template_loading) | bool | - |
| [`FILES_​REST_​ALLOW_​RANGE_​REQUESTS`](#files_rest_allow_range_requests) | bool | - |
| [`FILES_​REST_​CHECKSUM_​VERIFICATION_​URI_​PREFIXES`](#files_rest_checksum_verification_uri_prefixes) | unknown | - |
| [`FILES_​REST_​DEFAULT_​MAX_​FILE_​SIZE`](#files_rest_default_max_file_size) | NoneType | `configure_files` |
| [`FILES_​REST_​DEFAULT_​QUOTA_​SIZE`](#files_rest_default_quota_size) | NoneType | `configure_files` |
| [`FILES_​REST_​DEFAULT_​STORAGE_​CLASS`](#files_rest_default_storage_class) | str | `configure_generic_parameters` |
| [`FILES_​REST_​FILE_​TAGS_​HEADER`](#files_rest_file_tags_header) | str | - |
| [`FILES_​REST_​FILE_​URI_​MAX_​LEN`](#files_rest_file_uri_max_len) | int | - |
| [`FILES_​REST_​MIN_​FILE_​SIZE`](#files_rest_min_file_size) | int | - |
| [`FILES_​REST_​MULTIPART_​CHUNKSIZE_​MAX`](#files_rest_multipart_chunksize_max) | int | - |
| [`FILES_​REST_​MULTIPART_​CHUNKSIZE_​MIN`](#files_rest_multipart_chunksize_min) | int | - |
| [`FILES_​REST_​MULTIPART_​EXPIRES`](#files_rest_multipart_expires) | timedelta | - |
| [`FILES_​REST_​MULTIPART_​MAX_​PARTS`](#files_rest_multipart_max_parts) | int | - |
| [`FILES_​REST_​MULTIPART_​PART_​FACTORIES`](#files_rest_multipart_part_factories) | list | - |
| [`FILES_​REST_​OBJECT_​KEY_​MAX_​LEN`](#files_rest_object_key_max_len) | int | - |
| [`FILES_​REST_​PERMISSION_​FACTORY`](#files_rest_permission_factory) | str | - |
| [`FILES_​REST_​SIZE_​LIMITERS`](#files_rest_size_limiters) | str | - |
| [`FILES_​REST_​STORAGE_​CLASS_​LIST`](#files_rest_storage_class_list) | dict | `configure_generic_parameters` |
| [`FILES_​REST_​STORAGE_​FACTORY`](#files_rest_storage_factory) | str | `configure_generic_parameters` |
| [`FILES_​REST_​STORAGE_​PATH_​DIMENSIONS`](#files_rest_storage_path_dimensions) | int | - |
| [`FILES_​REST_​STORAGE_​PATH_​SPLIT_​LENGTH`](#files_rest_storage_path_split_length) | int | - |
| [`FILES_​REST_​TASK_​WAIT_​INTERVAL`](#files_rest_task_wait_interval) | int | - |
| [`FILES_​REST_​TASK_​WAIT_​MAX_​SECONDS`](#files_rest_task_wait_max_seconds) | int | - |
| [`FILES_​REST_​UPLOAD_​FACTORIES`](#files_rest_upload_factories) | list | - |
| [`FILES_​REST_​XSENDFILE_​ENABLED`](#files_rest_xsendfile_enabled) | bool | - |
| [`FILES_​REST_​XSENDFILE_​RESPONSE_​FUNC`](#files_rest_xsendfile_response_func) | unknown | - |
| [`FORMATTER_​BADGES_​ALLOWED_​TITLES`](#formatter_badges_allowed_titles) | list | - |
| [`FORMATTER_​BADGES_​ENABLE`](#formatter_badges_enable) | bool | - |
| [`FORMATTER_​BADGES_​MAX_​CACHE_​AGE`](#formatter_badges_max_cache_age) | int | - |
| [`FORMATTER_​BADGES_​TITLE_​MAPPING`](#formatter_badges_title_mapping) | dict | - |
| [`HANDLE_​URL`](#handle_url) | str | - |
| [`HEADER_​TEMPLATE`](#header_template) | unknown | `configure_ui` |
| [`I18N_​DEFAULT_​REDIRECT_​ENDPOINT`](#i18n_default_redirect_endpoint) | NoneType | - |
| [`I18N_​JS_​DISTR_​EXCEPTIONAL_​PACKAGE_​MAP`](#i18n_js_distr_exceptional_package_map) | dict | - |
| [`I18N_​LANGUAGES`](#i18n_languages) | list | `configure_generic_parameters` |
| [`I18N_​SESSION_​KEY`](#i18n_session_key) | str | - |
| [`I18N_​SET_​LANGUAGE_​URL`](#i18n_set_language_url) | str | - |
| [`I18N_​TRANSIFEX_​JS_​RESOURCES_​MAP`](#i18n_transifex_js_resources_map) | dict | - |
| [`I18N_​TRANSLATIONS_​PATHS`](#i18n_translations_paths) | list | - |
| [`I18N_​USER_​LANG_​ATTR`](#i18n_user_lang_attr) | str | - |
| [`IIIF_​API_​DECORATOR_​HANDLER`](#iiif_api_decorator_handler) | unknown | - |
| [`IIIF_​API_​INFO_​RESPONSE_​SKELETON`](#iiif_api_info_response_skeleton) | dict | - |
| [`IIIF_​CACHE_​HANDLER`](#iiif_cache_handler) | str | - |
| [`IIIF_​CACHE_​IGNORE_​ERRORS`](#iiif_cache_ignore_errors) | bool | - |
| [`IIIF_​CACHE_​REDIS_​URL`](#iiif_cache_redis_url) | str | - |
| [`IIIF_​CACHE_​TIME`](#iiif_cache_time) | int | - |
| [`IIIF_​CONVERTERS`](#iiif_converters) | tuple | - |
| [`IIIF_​FORMATS`](#iiif_formats) | dict | - |
| [`IIIF_​FORMATS_​PIL_​MAP`](#iiif_formats_pil_map) | dict | - |
| [`IIIF_​GIF_​TEMP_​FOLDER_​PATH`](#iiif_gif_temp_folder_path) | str | - |
| [`IIIF_​MODE`](#iiif_mode) | dict | - |
| [`IIIF_​PREVIEW_​TEMPLATE`](#iiif_preview_template) | str | - |
| [`IIIF_​QUALITIES`](#iiif_qualities) | tuple | - |
| [`IIIF_​SIMPLE_​PREVIEWER_​NATIVE_​EXTENSIONS`](#iiif_simple_previewer_native_extensions) | list | - |
| [`IIIF_​SIMPLE_​PREVIEWER_​SIZE`](#iiif_simple_previewer_size) | str | - |
| [`IIIF_​TILES_​CONVERTER_​PARAMS`](#iiif_tiles_converter_params) | dict | - |
| [`IIIF_​TILES_​GENERATION_​ENABLED`](#iiif_tiles_generation_enabled) | bool | - |
| [`IIIF_​TILES_​STORAGE_​BASE_​PATH`](#iiif_tiles_storage_base_path) | str | - |
| [`IIIF_​TILES_​VALID_​EXTENSIONS`](#iiif_tiles_valid_extensions) | list | - |
| [`IIIF_​VALIDATIONS`](#iiif_validations) | dict | - |
| [`INDEXER_​BEFORE_​INDEX_​HOOKS`](#indexer_before_index_hooks) | list | - |
| [`INDEXER_​BULK_​REQUEST_​TIMEOUT`](#indexer_bulk_request_timeout) | int | - |
| [`INDEXER_​DEFAULT_​INDEX`](#indexer_default_index) | NoneType | - |
| [`INDEXER_​MAX_​BULK_​CONSUMERS`](#indexer_max_bulk_consumers) | int | - |
| [`INDEXER_​MQ_​EXCHANGE`](#indexer_mq_exchange) | unknown | - |
| [`INDEXER_​MQ_​PUBLISH_​KWARGS`](#indexer_mq_publish_kwargs) | dict | - |
| [`INDEXER_​MQ_​QUEUE`](#indexer_mq_queue) | unknown | - |
| [`INDEXER_​MQ_​ROUTING_​KEY`](#indexer_mq_routing_key) | str | - |
| [`INDEXER_​RECORD_​TO_​INDEX`](#indexer_record_to_index) | str | - |
| [`INDEXER_​REPLACE_​REFS`](#indexer_replace_refs) | bool | - |
| [`INFO_​ENDPOINT_​COMPONENTS`](#info_endpoint_components) | list | - |
| [`INSTANCE_​THEME_​FILE`](#instance_theme_file) | configured by function | `configure_ui` |
| [`INVENIO_​CACHE_​TYPE`](#invenio_cache_type) | configured by function | `configure_generic_parameters` |
| [`INVENIO_​COLLECTIONS_​COMMUNITY_​SLUG`](#invenio_collections_community_slug) | str | - |
| [`INVENIO_​COLLECTIONS_​UI_​URL_​PREFIX`](#invenio_collections_ui_url_prefix) | str | - |
| [`INVENIO_​RDM_​ENABLED`](#invenio_rdm_enabled) | bool | - |
| [`INVENIO_​VOCABULARY_​TYPE_​METADATA`](#invenio_vocabulary_type_metadata) | dict | `configure_vocabulary` |
| [`JAVASCRIPT_​PACKAGES_​MANAGER`](#javascript_packages_manager) | configured by function | `configure_ui` |
| [`JOBS_​DEFAULT_​QUEUE`](#jobs_default_queue) | NoneType | - |
| [`JOBS_​FACETS`](#jobs_facets) | dict | - |
| [`JOBS_​LOGGING`](#jobs_logging) | bool | - |
| [`JOBS_​LOGGING_​INDEX`](#jobs_logging_index) | str | - |
| [`JOBS_​LOGGING_​LEVEL`](#jobs_logging_level) | str | `configure_jobs` |
| [`JOBS_​LOGGING_​RETENTION_​DAYS`](#jobs_logging_retention_days) | int | - |
| [`JOBS_​LOGS_​BATCH_​SIZE`](#jobs_logs_batch_size) | int | - |
| [`JOBS_​LOGS_​MAX_​RESULTS`](#jobs_logs_max_results) | int | - |
| [`JOBS_​PERMISSION_​POLICY`](#jobs_permission_policy) | unknown | - |
| [`JOBS_​QUEUES`](#jobs_queues) | dict | - |
| [`JOBS_​RUNS_​PERMISSION_​POLICY`](#jobs_runs_permission_policy) | unknown | - |
| [`JOBS_​SEARCH`](#jobs_search) | dict | - |
| [`JOBS_​SORT_​OPTIONS`](#jobs_sort_options) | dict | - |
| [`JOBS_​TASKS_​PERMISSION_​POLICY`](#jobs_tasks_permission_policy) | unknown | - |
| [`JSONSCHEMAS_​ENDPOINT`](#jsonschemas_endpoint) | str | - |
| [`JSONSCHEMAS_​HOST`](#jsonschemas_host) | str | `configure_generic_parameters` |
| [`JSONSCHEMAS_​LOADER_​CLS`](#jsonschemas_loader_cls) | NoneType | - |
| [`JSONSCHEMAS_​LOCAL_​REFRESOLVER_​URI_​SCHEME`](#jsonschemas_local_refresolver_uri_scheme) | str | - |
| [`JSONSCHEMAS_​REGISTER_​ENDPOINTS_​API`](#jsonschemas_register_endpoints_api) | bool | - |
| [`JSONSCHEMAS_​REGISTER_​ENDPOINTS_​UI`](#jsonschemas_register_endpoints_ui) | bool | - |
| [`JSONSCHEMAS_​REPLACE_​REFS`](#jsonschemas_replace_refs) | bool | - |
| [`JSONSCHEMAS_​RESOLVER_​CLS`](#jsonschemas_resolver_cls) | str | - |
| [`JSONSCHEMAS_​RESOLVE_​SCHEMA`](#jsonschemas_resolve_schema) | bool | - |
| [`JSONSCHEMAS_​SCHEMAS`](#jsonschemas_schemas) | NoneType | - |
| [`JSONSCHEMAS_​URL_​SCHEME`](#jsonschemas_url_scheme) | str | - |
| [`LOGGING_​CONSOLE`](#logging_console) | bool | - |
| [`LOGGING_​CONSOLE_​LEVEL`](#logging_console_level) | NoneType | - |
| [`LOGGING_​CONSOLE_​PYWARNINGS`](#logging_console_pywarnings) | bool | - |
| [`LOGGING_​FS_​BACKUPCOUNT`](#logging_fs_backupcount) | int | - |
| [`LOGGING_​FS_​LEVEL`](#logging_fs_level) | str | - |
| [`LOGGING_​FS_​LOGFILE`](#logging_fs_logfile) | NoneType | - |
| [`LOGGING_​FS_​MAXBYTES`](#logging_fs_maxbytes) | int | - |
| [`LOGGING_​FS_​PYWARNINGS`](#logging_fs_pywarnings) | bool | - |
| [`LOGGING_​SENTRY_​CELERY`](#logging_sentry_celery) | bool | - |
| [`LOGGING_​SENTRY_​CLASS`](#logging_sentry_class) | NoneType | - |
| [`LOGGING_​SENTRY_​INIT_​KWARGS`](#logging_sentry_init_kwargs) | NoneType | - |
| [`LOGGING_​SENTRY_​LEVEL`](#logging_sentry_level) | str | - |
| [`LOGGING_​SENTRY_​PYWARNINGS`](#logging_sentry_pywarnings) | bool | - |
| [`LOGGING_​SENTRY_​REDIS`](#logging_sentry_redis) | bool | - |
| [`LOGGING_​SENTRY_​SQLALCHEMY`](#logging_sentry_sqlalchemy) | bool | - |
| [`MAIL_​DEBUG`](#mail_debug) | bool | - |
| [`MAIL_​DEFAULT_​REPLY_​TO`](#mail_default_reply_to) | NoneType | - |
| [`MAIL_​DEFAULT_​SENDER`](#mail_default_sender) | unknown | `configure_generic_parameters` |
| [`MAIL_​MAX_​ATTACHMENT_​SIZE`](#mail_max_attachment_size) | int | - |
| [`MAIL_​MAX_​RETRIES`](#mail_max_retries) | int | - |
| [`MAIL_​MIN_​LOGGING_​LEVEL`](#mail_min_logging_level) | int | - |
| [`MAIL_​SUPPRESS_​SEND`](#mail_suppress_send) | bool | `configure_generic_parameters` |
| [`MATOMO_​ANALYTICS_​SITE_​ID`](#matomo_analytics_site_id) | configured by function | `configure_ui` |
| [`MATOMO_​ANALYTICS_​TEMPLATE`](#matomo_analytics_template) | configured by function | `configure_ui` |
| [`MATOMO_​ANALYTICS_​URL`](#matomo_analytics_url) | configured by function | `configure_ui` |
| [`MAX_​CONTENT_​LENGTH`](#max_content_length) | NoneType | - |
| [`MAX_​COOKIE_​SIZE`](#max_cookie_size) | int | - |
| [`MAX_​FORM_​MEMORY_​SIZE`](#max_form_memory_size) | int | - |
| [`MAX_​FORM_​PARTS`](#max_form_parts) | int | - |
| [`MULTIPROFILER_​BASE_​TEMPLATE`](#multiprofiler_base_template) | unknown | - |
| [`MULTIPROFILER_​IGNORED_​ENDPOINTS`](#multiprofiler_ignored_endpoints) | unknown | - |
| [`MULTIPROFILER_​PERMISSION`](#multiprofiler_permission) | unknown | - |
| [`NOTIFICATIONS_​BACKENDS`](#notifications_backends) | dict | - |
| [`NOTIFICATIONS_​BUILDERS`](#notifications_builders) | dict | - |
| [`NOTIFICATIONS_​ENTITY_​RESOLVERS`](#notifications_entity_resolvers) | list | - |
| [`NOTIFICATIONS_​GROUP_​EMAIL_​DOMAIN`](#notifications_group_email_domain) | NoneType | - |
| [`NOTIFICATIONS_​MANAGER_​CLS`](#notifications_manager_cls) | str | - |
| [`NOTIFICATIONS_​SETTINGS_​VIEW_​FUNCTION`](#notifications_settings_view_function) | unknown | - |
| [`NOTIFICATION_​RECIPIENTS_​RESOLVERS`](#notification_recipients_resolvers) | dict | - |
| [`OAISERVER_​ADMIN_​EMAILS`](#oaiserver_admin_emails) | list | - |
| [`OAISERVER_​BASE_​TEMPLATE`](#oaiserver_base_template) | str | - |
| [`OAISERVER_​CACHE_​KEY`](#oaiserver_cache_key) | str | - |
| [`OAISERVER_​CELERY_​TASK_​CHUNK_​SIZE`](#oaiserver_celery_task_chunk_size) | int | - |
| [`OAISERVER_​COMPRESSIONS`](#oaiserver_compressions) | list | - |
| [`OAISERVER_​CONTROL_​NUMBER_​FETCHER`](#oaiserver_control_number_fetcher) | str | - |
| [`OAISERVER_​CREATED_​KEY`](#oaiserver_created_key) | str | - |
| [`OAISERVER_​DELETE_​PERCOLATOR_​FUNCTION`](#oaiserver_delete_percolator_function) | str | - |
| [`OAISERVER_​DESCRIPTIONS`](#oaiserver_descriptions) | list | - |
| [`OAISERVER_​GETRECORD_​FETCHER`](#oaiserver_getrecord_fetcher) | str | - |
| [`OAISERVER_​GRANULARITY`](#oaiserver_granularity) | str | - |
| [`OAISERVER_​ID_​FETCHER`](#oaiserver_id_fetcher) | str | - |
| [`OAISERVER_​ID_​PREFIX`](#oaiserver_id_prefix) | str | `configure_generic_parameters` |
| [`OAISERVER_​LAST_​UPDATE_​KEY`](#oaiserver_last_update_key) | str | - |
| [`OAISERVER_​METADATA_​FORMATS`](#oaiserver_metadata_formats) | OAIServerMetadataFormats | - |
| [`OAISERVER_​NEW_​PERCOLATOR_​FUNCTION`](#oaiserver_new_percolator_function) | str | - |
| [`OAISERVER_​PAGE_​SIZE`](#oaiserver_page_size) | int | - |
| [`OAISERVER_​PERCOLATOR_​DEDICATED_​INDEX`](#oaiserver_percolator_dedicated_index) | bool | - |
| [`OAISERVER_​PROTOCOL_​VERSION`](#oaiserver_protocol_version) | str | - |
| [`OAISERVER_​QUERY_​PARSER`](#oaiserver_query_parser) | unknown | - |
| [`OAISERVER_​QUERY_​PARSER_​FIELDS`](#oaiserver_query_parser_fields) | list | - |
| [`OAISERVER_​RECORD_​CLS`](#oaiserver_record_cls) | str | - |
| [`OAISERVER_​RECORD_​INDEX`](#oaiserver_record_index) | str | - |
| [`OAISERVER_​RECORD_​LIST_​SETS_​FETCHER`](#oaiserver_record_list_sets_fetcher) | str | - |
| [`OAISERVER_​RECORD_​SETS_​FETCHER`](#oaiserver_record_sets_fetcher) | str | - |
| [`OAISERVER_​REGISTER_​RECORD_​SIGNALS`](#oaiserver_register_record_signals) | bool | - |
| [`OAISERVER_​REGISTER_​SET_​SIGNALS`](#oaiserver_register_set_signals) | bool | - |
| [`OAISERVER_​REPOSITORY_​NAME`](#oaiserver_repository_name) | LazyString | `configure_oai` |
| [`OAISERVER_​RESUMPTION_​TOKEN_​EXPIRE_​TIME`](#oaiserver_resumption_token_expire_time) | int | - |
| [`OAISERVER_​SEARCH_​CLS`](#oaiserver_search_cls) | str | - |
| [`OAISERVER_​SET_​RECORDS_​QUERY_​FETCHER`](#oaiserver_set_records_query_fetcher) | str | - |
| [`OAISERVER_​XSL_​URL`](#oaiserver_xsl_url) | NoneType | - |
| [`OAREPO_​CHECKS_​DEFAULT_​CHAT_​EINFRA_​CLIENT`](#oarepo_checks_default_chat_einfra_client) | configured by function | `configure_llm` |
| [`OAREPO_​CHECKS_​DEFAULT_​LLM_​CLIENT`](#oarepo_checks_default_llm_client) | configured by function | `configure_llm` |
| [`OAREPO_​CHECKS_​LLM_​CLIENTS`](#oarepo_checks_llm_clients) | configured by function | `configure_llm` |
| [`OAREPO_​CHECKS_​MAX_​LLM_​INPUT_​CHARS`](#oarepo_checks_max_llm_input_chars) | int | - |
| [`OAREPO_​CHECKS_​MAX_​LLM_​OUTPUT_​CHARS`](#oarepo_checks_max_llm_output_chars) | int | - |
| [`OAREPO_​COMMUNITIES_​DEFAULT_​WORKFLOW`](#oarepo_communities_default_workflow) | str | - |
| [`OAREPO_​MODELS`](#oarepo_models) | dict | - |
| [`OAREPO_​PERMISSIONS_​PRESETS`](#oarepo_permissions_presets) | dict | - |
| [`OAREPO_​REQUESTS_​DEFAULT_​RECEIVER`](#oarepo_requests_default_receiver) | str | - |
| [`OAREPO_​UI_​JINJAX_​FILTERS`](#oarepo_ui_jinjax_filters) | dict | - |
| [`OAREPO_​UI_​JINJAX_​GLOBALS`](#oarepo_ui_jinjax_globals) | dict | - |
| [`OAREPO_​UI_​LESS_​COMPONENTS`](#oarepo_ui_less_components) | list | - |
| [`OAREPO_​UI_​MULTILINGUAL_​FIELD_​LANGUAGES`](#oarepo_ui_multilingual_field_languages) | list | - |
| [`OAREPO_​UI_​OVERRIDES`](#oarepo_ui_overrides) | set | - |
| [`OAREPO_​UI_​RECORD_​ACTIONS`](#oarepo_ui_record_actions) | set | - |
| [`OAREPO_​UI_​RESULT_​LIST_​ITEM_​REGISTRATION_​CALLBACKS`](#oarepo_ui_result_list_item_registration_callbacks) | list | - |
| [`OAREPO_​VOCABULARIES_​PERMISSIONS_​PRESETS`](#oarepo_vocabularies_permissions_presets) | dict | - |
| [`OAREPO_​VOCABULARIES_​SORT_​CF`](#oarepo_vocabularies_sort_cf) | list | - |
| [`OAREPO_​VOCABULARIES_​SUGGEST_​CF`](#oarepo_vocabularies_suggest_cf) | list | - |
| [`OAREPO_​VOCABULARIES_​UI_​RESOURCE`](#oarepo_vocabularies_ui_resource) | str | - |
| [`OAREPO_​VOCABULARIES_​UI_​RESOURCE_​CONFIG`](#oarepo_vocabularies_ui_resource_config) | str | - |
| [`OAREPO_​VOCABULARY_​NAMESPACE_​URI`](#oarepo_vocabulary_namespace_uri) | NoneType | - |
| [`OAREPO_​VOCABULARY_​TYPE_​RESOURCE`](#oarepo_vocabulary_type_resource) | unknown | - |
| [`OAREPO_​VOCABULARY_​TYPE_​RESOURCE_​CONFIG`](#oarepo_vocabulary_type_resource_config) | unknown | - |
| [`OAREPO_​VOCABULARY_​TYPE_​SERVICE`](#oarepo_vocabulary_type_service) | unknown | - |
| [`OAREPO_​VOCABULARY_​TYPE_​SERVICE_​CONFIG`](#oarepo_vocabulary_type_service_config) | unknown | - |
| [`OAUTH2SERVER_​ALLOWED_​GRANT_​TYPES`](#oauth2server_allowed_grant_types) | set | - |
| [`OAUTH2SERVER_​ALLOWED_​RESPONSE_​TYPES`](#oauth2server_allowed_response_types) | set | - |
| [`OAUTH2SERVER_​ALLOWED_​URLENCODE_​CHARACTERS`](#oauth2server_allowed_urlencode_characters) | str | - |
| [`OAUTH2SERVER_​AUTHORIZE_​TEMPLATE`](#oauth2server_authorize_template) | str | - |
| [`OAUTH2SERVER_​BASE_​TEMPLATE`](#oauth2server_base_template) | str | - |
| [`OAUTH2SERVER_​CLIENT_​ID_​SALT_​LEN`](#oauth2server_client_id_salt_len) | int | - |
| [`OAUTH2SERVER_​CLIENT_​SECRET_​SALT_​LEN`](#oauth2server_client_secret_salt_len) | int | - |
| [`OAUTH2SERVER_​COVER_​TEMPLATE`](#oauth2server_cover_template) | str | - |
| [`OAUTH2SERVER_​JWT_​AUTH_​HEADER`](#oauth2server_jwt_auth_header) | str | - |
| [`OAUTH2SERVER_​JWT_​AUTH_​HEADER_​TYPE`](#oauth2server_jwt_auth_header_type) | str | - |
| [`OAUTH2SERVER_​JWT_​VERIFICATION_​FACTORY`](#oauth2server_jwt_verification_factory) | str | - |
| [`OAUTH2SERVER_​SETTINGS_​TEMPLATE`](#oauth2server_settings_template) | str | - |
| [`OAUTH2SERVER_​TOKEN_​PERSONAL_​SALT_​LEN`](#oauth2server_token_personal_salt_len) | int | - |
| [`OAUTH2_​CACHE_​REDIS_​HOST`](#oauth2_cache_redis_host) | Redis | - |
| [`OAUTH2_​CACHE_​TYPE`](#oauth2_cache_type) | str | - |
| [`OAUTH2_​PROVIDER_​ERROR_​ENDPOINT`](#oauth2_provider_error_endpoint) | str | - |
| [`OAUTHCLIENT_​AUTO_​REDIRECT_​TO_​EXTERNAL_​LOGIN`](#oauthclient_auto_redirect_to_external_login) | bool | `configure_generic_parameters` |
| [`OAUTHCLIENT_​BASE_​TEMPLATE`](#oauthclient_base_template) | str | - |
| [`OAUTHCLIENT_​COVER_​TEMPLATE`](#oauthclient_cover_template) | str | - |
| [`OAUTHCLIENT_​LOGIN_​USER_​TEMPLATE_​PARENT`](#oauthclient_login_user_template_parent) | str | - |
| [`OAUTHCLIENT_​REMOTE_​APPS`](#oauthclient_remote_apps) | dict | `configure_generic_parameters`, `configure_einfra_oidc` |
| [`OAUTHCLIENT_​REST_​DEFAULT_​ERROR_​REDIRECT_​URL`](#oauthclient_rest_default_error_redirect_url) | str | - |
| [`OAUTHCLIENT_​REST_​DEFAULT_​RESPONSE_​HANDLER`](#oauthclient_rest_default_response_handler) | NoneType | - |
| [`OAUTHCLIENT_​REST_​REMOTE_​APPS`](#oauthclient_rest_remote_apps) | dict | - |
| [`OAUTHCLIENT_​SESSION_​KEY_​PREFIX`](#oauthclient_session_key_prefix) | str | - |
| [`OAUTHCLIENT_​SETTINGS_​TEMPLATE`](#oauthclient_settings_template) | str | - |
| [`OAUTHCLIENT_​SIGNUP_​FORM`](#oauthclient_signup_form) | unknown | - |
| [`OAUTHCLIENT_​SIGNUP_​TEMPLATE`](#oauthclient_signup_template) | str | - |
| [`OAUTHCLIENT_​SITENAME`](#oauthclient_sitename) | LazyString | - |
| [`OAUTHCLIENT_​STATE_​ENABLED`](#oauthclient_state_enabled) | bool | - |
| [`OAUTHCLIENT_​STATE_​EXPIRES`](#oauthclient_state_expires) | int | - |
| [`OAUTHCLIENT_​TOKEN_​EXPIRES_​LEEWAY`](#oauthclient_token_expires_leeway) | int | - |
| [`ORCID_​PUBLIC_​DUMP_​S3_​BUCKET_​NAME`](#orcid_public_dump_s3_bucket_name) | str | - |
| [`PAGES_​ALLOWED_​EXTRA_​HTML_​ATTRS`](#pages_allowed_extra_html_attrs) | dict | - |
| [`PAGES_​ALLOWED_​EXTRA_​HTML_​TAGS`](#pages_allowed_extra_html_tags) | list | - |
| [`PAGES_​BASE_​TEMPLATE`](#pages_base_template) | str | - |
| [`PAGES_​DEFAULT_​TEMPLATE`](#pages_default_template) | str | - |
| [`PAGES_​FACETS`](#pages_facets) | dict | - |
| [`PAGES_​SEARCH`](#pages_search) | dict | - |
| [`PAGES_​SORT_​OPTIONS`](#pages_sort_options) | dict | - |
| [`PAGES_​TEMPLATES`](#pages_templates) | list | - |
| [`PAGES_​WHITELIST_​CONFIG_​KEYS`](#pages_whitelist_config_keys) | list | - |
| [`PERMANENT_​SESSION_​LIFETIME`](#permanent_session_lifetime) | timedelta | - |
| [`PIDSTORE_​APP_​LOGGER_​HANDLERS`](#pidstore_app_logger_handlers) | bool | - |
| [`PIDSTORE_​DATACITE_​DOI_​PREFIX`](#pidstore_datacite_doi_prefix) | str | - |
| [`PIDSTORE_​OBJECT_​ENDPOINTS`](#pidstore_object_endpoints) | dict | - |
| [`PIDSTORE_​RECID_​FIELD`](#pidstore_recid_field) | str | - |
| [`PIDSTORE_​RECORDID_​OPTIONS`](#pidstore_recordid_options) | dict | - |
| [`PREFERRED_​URL_​SCHEME`](#preferred_url_scheme) | str | - |
| [`PREVIEWABLE_​ZIP_​PREVIEWER_​NATIVE_​EXTENSIONS`](#previewable_zip_previewer_native_extensions) | list | - |
| [`PREVIEWER_​ABSTRACT_​TEMPLATE`](#previewer_abstract_template) | str | - |
| [`PREVIEWER_​BASE_​CSS_​BUNDLES`](#previewer_base_css_bundles) | list | - |
| [`PREVIEWER_​BASE_​JS_​BUNDLES`](#previewer_base_js_bundles) | list | - |
| [`PREVIEWER_​BASE_​TEMPLATE`](#previewer_base_template) | str | - |
| [`PREVIEWER_​CHARDET_​BYTES`](#previewer_chardet_bytes) | int | - |
| [`PREVIEWER_​CHARDET_​CONFIDENCE`](#previewer_chardet_confidence) | float | - |
| [`PREVIEWER_​CONTAINER_​ITEM_​PREFERENCE`](#previewer_container_item_preference) | list | - |
| [`PREVIEWER_​CSV_​MAX_​BYTES`](#previewer_csv_max_bytes) | int | - |
| [`PREVIEWER_​CSV_​SNIFFER_​ALLOWED_​DELIMITERS`](#previewer_csv_sniffer_allowed_delimiters) | NoneType | - |
| [`PREVIEWER_​CSV_​VALIDATION_​BYTES`](#previewer_csv_validation_bytes) | int | - |
| [`PREVIEWER_​MAX_​FILE_​SIZE_​BYTES`](#previewer_max_file_size_bytes) | int | - |
| [`PREVIEWER_​MAX_​IMAGE_​SIZE_​BYTES`](#previewer_max_image_size_bytes) | float | - |
| [`PREVIEWER_​PDF_​JS_​DOCUMENT_​INIT_​PARAMS`](#previewer_pdf_js_document_init_params) | NoneType | - |
| [`PREVIEWER_​PDF_​JS_​ENABLE_​SCRIPTING`](#previewer_pdf_js_enable_scripting) | bool | - |
| [`PREVIEWER_​PREFERENCE`](#previewer_preference) | list | - |
| [`PREVIEWER_​RECORD_​FILE_​FACOTRY`](#previewer_record_file_facotry) | NoneType | - |
| [`PREVIEWER_​TXT_​MAX_​BYTES`](#previewer_txt_max_bytes) | int | - |
| [`PREVIEWER_​WEB_​ARCHIVE_​RANGE_​REQUESTS`](#previewer_web_archive_range_requests) | bool | - |
| [`PREVIEWER_​ZIP_​MAX_​FILES`](#previewer_zip_max_files) | int | - |
| [`PROPAGATE_​EXCEPTIONS`](#propagate_exceptions) | NoneType | - |
| [`PROVIDE_​AUTOMATIC_​OPTIONS`](#provide_automatic_options) | bool | - |
| [`PUBLISH_​REQUEST_​TYPES`](#publish_request_types) | list | - |
| [`QUEUES_​BROKER_​URL`](#queues_broker_url) | NoneType | - |
| [`QUEUES_​CONNECTION_​POOL`](#queues_connection_pool) | unknown | - |
| [`QUEUES_​DEFINITIONS`](#queues_definitions) | list | - |
| [`RATELIMIT_​APPLICATION`](#ratelimit_application) | unknown | - |
| [`RATELIMIT_​AUTHENTICATED_​USER`](#ratelimit_authenticated_user) | str | `configure_generic_parameters` |
| [`RATELIMIT_​ENABLED`](#ratelimit_enabled) | bool | - |
| [`RATELIMIT_​GUEST_​USER`](#ratelimit_guest_user) | str | `configure_generic_parameters` |
| [`RATELIMIT_​HEADERS_​ENABLED`](#ratelimit_headers_enabled) | bool | - |
| [`RATELIMIT_​KEY_​FUNC`](#ratelimit_key_func) | NoneType | - |
| [`RATELIMIT_​PER_​ENDPOINT`](#ratelimit_per_endpoint) | dict | - |
| [`RATELIMIT_​STORAGE_​URI`](#ratelimit_storage_uri) | str | - |
| [`RATELIMIT_​STRATEGY`](#ratelimit_strategy) | str | - |
| [`RDM_​ALLOW_​EXTERNAL_​DOI_​VERSIONING`](#rdm_allow_external_doi_versioning) | bool | - |
| [`RDM_​ALLOW_​METADATA_​ONLY_​RECORDS`](#rdm_allow_metadata_only_records) | bool | `configure_files` |
| [`RDM_​ALLOW_​OWNERS_​REMOVE_​COMMUNITY_​FROM_​RECORD`](#rdm_allow_owners_remove_community_from_record) | bool | - |
| [`RDM_​ALLOW_​RESTRICTED_​RECORDS`](#rdm_allow_restricted_records) | bool | - |
| [`RDM_​ARCHIVE_​DOWNLOAD_​ENABLED`](#rdm_archive_download_enabled) | bool | - |
| [`RDM_​CITATION_​STYLES`](#rdm_citation_styles) | list | - |
| [`RDM_​CITATION_​STYLES_​DEFAULT`](#rdm_citation_styles_default) | str | - |
| [`RDM_​COMMUNITIES_​ROUTES`](#rdm_communities_routes) | dict | - |
| [`RDM_​COMMUNITY_​COLLECTIONS_​RECORDS_​SERVICE_​CLASS`](#rdm_community_collections_records_service_class) | str | - |
| [`RDM_​COMMUNITY_​CONTENT_​MODERATION_​HANDLERS`](#rdm_community_content_moderation_handlers) | list | - |
| [`RDM_​COMMUNITY_​INCLUSION_​REQUEST_​CLS`](#rdm_community_inclusion_request_cls) | unknown | - |
| [`RDM_​COMMUNITY_​REQUIRED_​TO_​PUBLISH`](#rdm_community_required_to_publish) | bool | - |
| [`RDM_​COMMUNITY_​SUBMISSION_​REQUEST_​CLS`](#rdm_community_submission_request_cls) | unknown | - |
| [`RDM_​CONTENT_​MODERATION_​HANDLERS`](#rdm_content_moderation_handlers) | list | - |
| [`RDM_​CUSTOM_​FIELDS`](#rdm_custom_fields) | list | - |
| [`RDM_​CUSTOM_​FIELDS_​UI`](#rdm_custom_fields_ui) | list | - |
| [`RDM_​DATACITE_​DUMP_​OPENAIRE_​ACCESS_​RIGHTS`](#rdm_datacite_dump_openaire_access_rights) | bool | - |
| [`RDM_​DATACITE_​FUNDER_​IDENTIFIERS_​PRIORITY`](#rdm_datacite_funder_identifiers_priority) | tuple | - |
| [`RDM_​DEFAULT_​FILES_​ENABLED`](#rdm_default_files_enabled) | bool | - |
| [`RDM_​DETAIL_​SIDE_​BAR_​MANAGE_​ATTRIBUTES_​EXTENSION_​TEMPLATE`](#rdm_detail_side_bar_manage_attributes_extension_template) | unknown | - |
| [`RDM_​FACETS`](#rdm_facets) | unknown | - |
| [`RDM_​FILES_​DEFAULT_​MAX_​ADDITIONAL_​QUOTA_​SIZE`](#rdm_files_default_max_additional_quota_size) | int | `configure_files` |
| [`RDM_​FILES_​DEFAULT_​MAX_​FILE_​SIZE`](#rdm_files_default_max_file_size) | int | `configure_files` |
| [`RDM_​FILES_​DEFAULT_​QUOTA_​SIZE`](#rdm_files_default_quota_size) | int | `configure_files` |
| [`RDM_​FILE_​MODIFICATION_​PERIOD`](#rdm_file_modification_period) | timedelta | `configure_files` |
| [`RDM_​FILE_​MODIFICATION_​POLICY`](#rdm_file_modification_policy) | unknown | - |
| [`RDM_​IIIF_​MANIFEST_​FORMATS`](#rdm_iiif_manifest_formats) | list | - |
| [`RDM_​IMMEDIATE_​FILE_​MODIFICATION_​ENABLED`](#rdm_immediate_file_modification_enabled) | bool | `configure_files` |
| [`RDM_​IMMEDIATE_​FILE_​MODIFICATION_​POLICIES`](#rdm_immediate_file_modification_policies) | list | `configure_files` |
| [`RDM_​IMMEDIATE_​QUOTA_​INCREASE_​ENABLED`](#rdm_immediate_quota_increase_enabled) | bool | `configure_files` |
| [`RDM_​IMMEDIATE_​QUOTA_​INCREASE_​POLICIES`](#rdm_immediate_quota_increase_policies) | list | `configure_files` |
| [`RDM_​IMMEDIATE_​RECORD_​DELETION_​CHECKLIST`](#rdm_immediate_record_deletion_checklist) | list | - |
| [`RDM_​IMMEDIATE_​RECORD_​DELETION_​ENABLED`](#rdm_immediate_record_deletion_enabled) | bool | - |
| [`RDM_​IMMEDIATE_​RECORD_​DELETION_​POLICIES`](#rdm_immediate_record_deletion_policies) | list | - |
| [`RDM_​LOCK_​EDIT_​PUBLISHED_​FILES`](#rdm_lock_edit_published_files) | unknown | - |
| [`RDM_​MEDIA_​FILES_​DEFAULT_​MAX_​FILE_​SIZE`](#rdm_media_files_default_max_file_size) | int | - |
| [`RDM_​MEDIA_​FILES_​DEFAULT_​QUOTA_​SIZE`](#rdm_media_files_default_quota_size) | int | - |
| [`RDM_​NAMESPACES`](#rdm_namespaces) | dict | - |
| [`RDM_​NEW_​RECORD_​VERSION_​REVIEW_​POLICY`](#rdm_new_record_version_review_policy) | unknown | - |
| [`RDM_​NOTIFICATIONS_​BUILDERS`](#rdm_notifications_builders) | dict | - |
| [`RDM_​OAI_​PMH_​FACETS`](#rdm_oai_pmh_facets) | dict | - |
| [`RDM_​OAI_​PMH_​SEARCH`](#rdm_oai_pmh_search) | dict | - |
| [`RDM_​OAI_​PMH_​SORT_​OPTIONS`](#rdm_oai_pmh_sort_options) | dict | - |
| [`RDM_​OPTIONAL_​DOI_​VALIDATOR`](#rdm_optional_doi_validator) | unknown | - |
| [`RDM_​PARENT_​PERSISTENT_​IDENTIFIERS`](#rdm_parent_persistent_identifiers) | dict | - |
| [`RDM_​PARENT_​PERSISTENT_​IDENTIFIER_​PROVIDERS`](#rdm_parent_persistent_identifier_providers) | list | - |
| [`RDM_​PERMISSION_​POLICY`](#rdm_permission_policy) | unknown | - |
| [`RDM_​PERSISTENT_​IDENTIFIERS`](#rdm_persistent_identifiers) | dict | - |
| [`RDM_​PERSISTENT_​IDENTIFIER_​PROVIDERS`](#rdm_persistent_identifier_providers) | list | - |
| [`RDM_​QUOTA_​INCREASE_​POLICY`](#rdm_quota_increase_policy) | unknown | - |
| [`RDM_​RECORDS_​ACCESS_​SERVICE_​CLASS`](#rdm_records_access_service_class) | str | - |
| [`RDM_​RECORDS_​ALLOW_​RESTRICTION_​AFTER_​GRACE_​PERIOD`](#rdm_records_allow_restriction_after_grace_period) | bool | - |
| [`RDM_​RECORDS_​COMMUNITY_​RECORDS_​CONFIG_​CLASS`](#rdm_records_community_records_config_class) | str | - |
| [`RDM_​RECORDS_​COMMUNITY_​RECORDS_​SERVICE_​CLASS`](#rdm_records_community_records_service_class) | str | - |
| [`RDM_​RECORDS_​CONTAINER_​EXTENSIONS`](#rdm_records_container_extensions) | list | - |
| [`RDM_​RECORDS_​ERROR_​HANDLERS`](#rdm_records_error_handlers) | dict | `add_model` |
| [`RDM_​RECORDS_​IDENTIFIERS_​SCHEMES`](#rdm_records_identifiers_schemes) | dict | - |
| [`RDM_​RECORDS_​LOCATION_​SCHEMES`](#rdm_records_location_schemes) | dict | - |
| [`RDM_​RECORDS_​MAX_​FILES_​COUNT`](#rdm_records_max_files_count) | int | `configure_files` |
| [`RDM_​RECORDS_​MAX_​MEDIA_​FILES_​COUNT`](#rdm_records_max_media_files_count) | int | - |
| [`RDM_​RECORDS_​PERSONORG_​SCHEMES`](#rdm_records_personorg_schemes) | dict | - |
| [`RDM_​RECORDS_​PIDS_​SERVICE_​CLASS`](#rdm_records_pids_service_class) | str | - |
| [`RDM_​RECORDS_​RELATED_​IDENTIFIERS_​SCHEMES`](#rdm_records_related_identifiers_schemes) | dict | - |
| [`RDM_​RECORDS_​REQUIRE_​SECRET_​LINKS_​EXPIRATION`](#rdm_records_require_secret_links_expiration) | bool | - |
| [`RDM_​RECORDS_​RESOURCE_​CLASS`](#rdm_records_resource_class) | str | - |
| [`RDM_​RECORDS_​RESOURCE_​CONFIG_​CLASS`](#rdm_records_resource_config_class) | str | - |
| [`RDM_​RECORDS_​RESTRICTION_​GRACE_​PERIOD`](#rdm_records_restriction_grace_period) | timedelta | - |
| [`RDM_​RECORDS_​REVIEWS`](#rdm_records_reviews) | list | - |
| [`RDM_​RECORDS_​REVIEW_​SERVICE_​CLASS`](#rdm_records_review_service_class) | str | - |
| [`RDM_​RECORDS_​SERVICE_​CLASS`](#rdm_records_service_class) | str | - |
| [`RDM_​RECORDS_​SERVICE_​COMPONENTS`](#rdm_records_service_components) | list | - |
| [`RDM_​RECORDS_​SERVICE_​CONFIG_​CLASS`](#rdm_records_service_config_class) | str | - |
| [`RDM_​RECORDS_​UI_​EDIT_​URL`](#rdm_records_ui_edit_url) | str | - |
| [`RDM_​RECORDS_​USER_​FIXTURE_​PASSWORDS`](#rdm_records_user_fixture_passwords) | dict | - |
| [`RDM_​RECORD_​DELETION_​POLICY`](#rdm_record_deletion_policy) | unknown | - |
| [`RDM_​RECORD_​FILE_​EXTRACTORS`](#rdm_record_file_extractors) | list | - |
| [`RDM_​REQUESTS_​ROUTES`](#rdm_requests_routes) | dict | - |
| [`RDM_​REQUEST_​RECORD_​DELETION_​CHECKLIST`](#rdm_request_record_deletion_checklist) | list | - |
| [`RDM_​REQUEST_​RECORD_​DELETION_​ENABLED`](#rdm_request_record_deletion_enabled) | bool | - |
| [`RDM_​REQUEST_​RECORD_​DELETION_​POLICIES`](#rdm_request_record_deletion_policies) | list | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​ENABLED`](#rdm_resource_access_tokens_enabled) | bool | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​JWT_​LIFETIME`](#rdm_resource_access_tokens_jwt_lifetime) | timedelta | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​SUBJECT_​SCHEMA`](#rdm_resource_access_tokens_subject_schema) | unknown | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​WHITELISTED_​JWT_​ALGORITHMS`](#rdm_resource_access_tokens_whitelisted_jwt_algorithms) | list | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKEN_​REQUEST_​ARG`](#rdm_resource_access_token_request_arg) | str | - |
| [`RDM_​SEARCH`](#rdm_search) | unknown | - |
| [`RDM_​SEARCH_​DRAFTS`](#rdm_search_drafts) | unknown | - |
| [`RDM_​SEARCH_​SORT_​BY_​VERIFIED`](#rdm_search_sort_by_verified) | bool | - |
| [`RDM_​SEARCH_​USER_​COMMUNITIES`](#rdm_search_user_communities) | dict | - |
| [`RDM_​SEARCH_​USER_​REQUESTS`](#rdm_search_user_requests) | dict | - |
| [`RDM_​SEARCH_​VERSIONING`](#rdm_search_versioning) | dict | - |
| [`RDM_​SORT_​OPTIONS`](#rdm_sort_options) | dict | - |
| [`RDM_​STATS_​EXCLUDE_​PREVIEW_​FILE_​DOWNLOAD_​EVENTS`](#rdm_stats_exclude_preview_file_download_events) | bool | - |
| [`RDM_​USER_​MODERATION_​ENABLED`](#rdm_user_moderation_enabled) | bool | - |
| [`RECAPTCHA_​PRIVATE_​KEY`](#recaptcha_private_key) | unknown | - |
| [`RECAPTCHA_​PUBLIC_​KEY`](#recaptcha_public_key) | unknown | - |
| [`RECORDS_​FILES_​REST_​ENDPOINTS`](#records_files_rest_endpoints) | dict | - |
| [`RECORDS_​PERMISSIONS_​BASE_​TEMPLATE`](#records_permissions_base_template) | str | - |
| [`RECORDS_​PERMISSIONS_​RECORD_​POLICY`](#records_permissions_record_policy) | str | - |
| [`RECORDS_​REFRESOLVER_​CLS`](#records_refresolver_cls) | NoneType | `configure_generic_parameters` |
| [`RECORDS_​REFRESOLVER_​STORE`](#records_refresolver_store) | NoneType | `configure_generic_parameters` |
| [`RECORDS_​RESOURCES_​ALLOW_​EMPTY_​FILES`](#records_resources_allow_empty_files) | bool | `configure_files` |
| [`RECORDS_​RESOURCES_​ARCHIVE_​DOWNLOAD_​MAX_​SIZE`](#records_resources_archive_download_max_size) | NoneType | - |
| [`RECORDS_​RESOURCES_​DEFAULT_​TRANSFER_​TYPE`](#records_resources_default_transfer_type) | str | - |
| [`RECORDS_​RESOURCES_​EXTRACTED_​STREAM_​CHUNK_​SIZE`](#records_resources_extracted_stream_chunk_size) | int | - |
| [`RECORDS_​RESOURCES_​FILES_​ALLOWED_​DOMAINS`](#records_resources_files_allowed_domains) | list | - |
| [`RECORDS_​RESOURCES_​IMAGE_​FORMATS`](#records_resources_image_formats) | list | - |
| [`RECORDS_​RESOURCES_​TRANSFERS`](#records_resources_transfers) | list | - |
| [`RECORDS_​RESOURCES_​ZIP_​FORMATS`](#records_resources_zip_formats) | list | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​ENTRIES`](#records_resources_zip_max_entries) | int | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​HEADER_​SIZE`](#records_resources_zip_max_header_size) | int | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​LISTING_​ENTRIES`](#records_resources_zip_max_listing_entries) | int | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​RATIO`](#records_resources_zip_max_ratio) | float | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​TOTAL_​UNCOMPRESSED`](#records_resources_zip_max_total_uncompressed) | int | - |
| [`RECORDS_​REST_​DEFAULT_​CREATE_​PERMISSION_​FACTORY`](#records_rest_default_create_permission_factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​DELETE_​PERMISSION_​FACTORY`](#records_rest_default_delete_permission_factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​LIST_​PERMISSION_​FACTORY`](#records_rest_default_list_permission_factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​LOADERS`](#records_rest_default_loaders) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​READ_​PERMISSION_​FACTORY`](#records_rest_default_read_permission_factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​RESULTS_​SIZE`](#records_rest_default_results_size) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​SORT`](#records_rest_default_sort) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​UPDATE_​PERMISSION_​FACTORY`](#records_rest_default_update_permission_factory) | unknown | - |
| [`RECORDS_​REST_​ENDPOINTS`](#records_rest_endpoints) | list | `configure_generic_parameters` |
| [`RECORDS_​REST_​FACETS`](#records_rest_facets) | unknown | - |
| [`RECORDS_​REST_​FACETS_​POST_​FILTERS_​PROPAGATE`](#records_rest_facets_post_filters_propagate) | unknown | - |
| [`RECORDS_​REST_​SEARCH_​ERROR_​HANDLERS`](#records_rest_search_error_handlers) | unknown | - |
| [`RECORDS_​REST_​SORT_​OPTIONS`](#records_rest_sort_options) | unknown | - |
| [`RECORDS_​UI_​BASE_​TEMPLATE`](#records_ui_base_template) | str | - |
| [`RECORDS_​UI_​DEFAULT_​PERMISSION_​FACTORY`](#records_ui_default_permission_factory) | NoneType | - |
| [`RECORDS_​UI_​ENDPOINTS`](#records_ui_endpoints) | dict | `configure_ui` |
| [`RECORDS_​UI_​EXPORT_​FORMATS`](#records_ui_export_formats) | dict | - |
| [`RECORDS_​UI_​LOGIN_​ENDPOINT`](#records_ui_login_endpoint) | str | - |
| [`RECORDS_​UI_​TOMBSTONE_​TEMPLATE`](#records_ui_tombstone_template) | str | - |
| [`RECORDS_​VALIDATION_​TYPES`](#records_validation_types) | dict | - |
| [`RECORD_​ROUTES`](#record_routes) | configured by function | `configure_generic_parameters` |
| [`RELATED_​RESOURCES_​DEFAULT_​RESOURCE_​TYPE`](#related_resources_default_resource_type) | str | - |
| [`RELATED_​RESOURCES_​DEFAULT_​TIMEOUT`](#related_resources_default_timeout) | int | - |
| [`RELATED_​RESOURCES_​RECORD_​UI_​SCHEMA`](#related_resources_record_ui_schema) | str | - |
| [`RELATED_​RESOURCES_​RESOURCE_​CLASS`](#related_resources_resource_class) | str | - |
| [`RELATED_​RESOURCES_​RESOURCE_​CONFIG_​CLASS`](#related_resources_resource_config_class) | str | - |
| [`RELATED_​RESOURCES_​SERVICE_​CLASS`](#related_resources_service_class) | str | - |
| [`RELATED_​RESOURCES_​SERVICE_​CONFIG_​CLASS`](#related_resources_service_config_class) | str | - |
| [`REMEMBER_​COOKIE_​DURATION`](#remember_cookie_duration) | unknown | - |
| [`REPOSITORY_​DESCRIPTION`](#repository_description) | configured by function | `configure_ui` |
| [`REPOSITORY_​KEYWORDS`](#repository_keywords) | configured by function | `configure_ui` |
| [`REPOSITORY_​NAME`](#repository_name) | configured by function | `configure_ui` |
| [`REPOSITORY_​SUBTITLE`](#repository_subtitle) | configured by function | `configure_ui` |
| [`REPOSITORY_​SUPPORT_​CONTACT`](#repository_support_contact) | configured by function | `configure_ui` |
| [`REQUESTS_​ACTION_​COMPONENTS`](#requests_action_components) | list | - |
| [`REQUESTS_​ALLOWED_​RECEIVERS`](#requests_allowed_receivers) | list | - |
| [`REQUESTS_​COMMENTS_​ALLOWED_​EXTRA_​HTML_​ATTRS`](#requests_comments_allowed_extra_html_attrs) | dict | - |
| [`REQUESTS_​COMMENTS_​ALLOWED_​EXTRA_​HTML_​TAGS`](#requests_comments_allowed_extra_html_tags) | list | - |
| [`REQUESTS_​COMMENT_​PREVIEW_​LIMIT`](#requests_comment_preview_limit) | int | - |
| [`REQUESTS_​ENTITY_​RESOLVERS`](#requests_entity_resolvers) | list | - |
| [`REQUESTS_​ERROR_​HANDLERS`](#requests_error_handlers) | unknown | - |
| [`REQUESTS_​EVENTS_​SERVICE_​COMPONENTS`](#requests_events_service_components) | list | - |
| [`REQUESTS_​FACETS`](#requests_facets) | dict | - |
| [`REQUESTS_​FILES_​DEFAULT_​MAX_​FILE_​SIZE`](#requests_files_default_max_file_size) | int | - |
| [`REQUESTS_​FILES_​DEFAULT_​QUOTA_​SIZE`](#requests_files_default_quota_size) | int | - |
| [`REQUESTS_​LOCKING_​ENABLED`](#requests_locking_enabled) | bool | - |
| [`REQUESTS_​MODERATION_​ROLE`](#requests_moderation_role) | str | - |
| [`REQUESTS_​PERMISSION_​POLICY`](#requests_permission_policy) | unknown | - |
| [`REQUESTS_​REGISTERED_​EVENT_​TYPES`](#requests_registered_event_types) | list | - |
| [`REQUESTS_​REGISTERED_​TYPES`](#requests_registered_types) | list | - |
| [`REQUESTS_​RESOURCE_​CLASS`](#requests_resource_class) | unknown | - |
| [`REQUESTS_​RESOURCE_​CONFIG_​CLASS`](#requests_resource_config_class) | unknown | - |
| [`REQUESTS_​REVIEWERS_​ENABLED`](#requests_reviewers_enabled) | bool | - |
| [`REQUESTS_​REVIEWERS_​MAX_​NUMBER`](#requests_reviewers_max_number) | int | - |
| [`REQUESTS_​ROUTES`](#requests_routes) | dict | - |
| [`REQUESTS_​SEARCH`](#requests_search) | dict | - |
| [`REQUESTS_​SERVICE_​CLASS`](#requests_service_class) | unknown | - |
| [`REQUESTS_​SERVICE_​CONFIG_​CLASS`](#requests_service_config_class) | unknown | - |
| [`REQUESTS_​SORT_​OPTIONS`](#requests_sort_options) | dict | - |
| [`REQUESTS_​TIMELINE_​PAGE_​SIZE`](#requests_timeline_page_size) | int | - |
| [`REQUESTS_​USER_​MODERATION_​FACETS`](#requests_user_moderation_facets) | dict | - |
| [`REQUESTS_​USER_​MODERATION_​SEARCH`](#requests_user_moderation_search) | dict | - |
| [`REQUESTS_​USER_​MODERATION_​SORT_​OPTIONS`](#requests_user_moderation_sort_options) | dict | - |
| [`REST_​CSRF_​ENABLED`](#rest_csrf_enabled) | unknown | - |
| [`REST_​ENABLE_​CORS`](#rest_enable_cors) | unknown | - |
| [`REST_​MIMETYPE_​QUERY_​ARG_​NAME`](#rest_mimetype_query_arg_name) | unknown | - |
| [`ROR_​CLIENT_​ID`](#ror_client_id) | configured by function | `configure_generic_parameters` |
| [`S3_​ACCESS_​KEY_​ID`](#s3_access_key_id) | NoneType | `configure_generic_parameters` |
| [`S3_​CONFIG_​EXTRA`](#s3_config_extra) | dict | - |
| [`S3_​DEFAULT_​BLOCK_​SIZE`](#s3_default_block_size) | int | - |
| [`S3_​ENDPOINT_​URL`](#s3_endpoint_url) | NoneType | `configure_generic_parameters` |
| [`S3_​MAXIMUM_​NUMBER_​OF_​PARTS`](#s3_maximum_number_of_parts) | int | - |
| [`S3_​REGION_​NAME`](#s3_region_name) | NoneType | - |
| [`S3_​SECRET_​ACCESS_​KEY`](#s3_secret_access_key) | NoneType | `configure_generic_parameters` |
| [`S3_​SIGNATURE_​VERSION`](#s3_signature_version) | str | - |
| [`S3_​UPLOAD_​URL_​EXPIRATION`](#s3_upload_url_expiration) | int | - |
| [`S3_​URL_​EXPIRATION`](#s3_url_expiration) | int | - |
| [`SEARCH_​CLIENT_​CONFIG`](#search_client_config) | NoneType | `configure_generic_parameters` |
| [`SEARCH_​ELASTIC_​HOSTS`](#search_elastic_hosts) | NoneType | - |
| [`SEARCH_​HOSTS`](#search_hosts) | NoneType | `configure_generic_parameters` |
| [`SEARCH_​INDEX_​PREFIX`](#search_index_prefix) | str | `configure_generic_parameters` |
| [`SEARCH_​MAPPINGS`](#search_mappings) | NoneType | - |
| [`SEARCH_​RESULTS_​MIN_​SCORE`](#search_results_min_score) | NoneType | - |
| [`SEARCH_​UI_​BASE_​TEMPLATE`](#search_ui_base_template) | str | - |
| [`SEARCH_​UI_​HEADER_​TEMPLATE`](#search_ui_header_template) | NoneType | - |
| [`SEARCH_​UI_​JSTEMPLATE_​COUNT`](#search_ui_jstemplate_count) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​ERROR`](#search_ui_jstemplate_error) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​FACETS`](#search_ui_jstemplate_facets) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​LOADING`](#search_ui_jstemplate_loading) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​PAGINATION`](#search_ui_jstemplate_pagination) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​RANGE`](#search_ui_jstemplate_range) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​RANGE_​OPTIONS`](#search_ui_jstemplate_range_options) | dict | - |
| [`SEARCH_​UI_​JSTEMPLATE_​RESULTS`](#search_ui_jstemplate_results) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​SELECT_​BOX`](#search_ui_jstemplate_select_box) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​SORT_​ORDER`](#search_ui_jstemplate_sort_order) | str | - |
| [`SEARCH_​UI_​SEARCH_​API`](#search_ui_search_api) | str | - |
| [`SEARCH_​UI_​SEARCH_​CONFIG_​GEN`](#search_ui_search_config_gen) | dict | - |
| [`SEARCH_​UI_​SEARCH_​INDEX`](#search_ui_search_index) | str | - |
| [`SEARCH_​UI_​SEARCH_​TEMPLATE`](#search_ui_search_template) | str | `configure_ui` |
| [`SEARCH_​UI_​SEARCH_​VIEW`](#search_ui_search_view) | unknown | `configure_ui` |
| [`SECRET_​KEY`](#secret_key) | str | `configure_generic_parameters` |
| [`SECRET_​KEY_​FALLBACKS`](#secret_key_fallbacks) | NoneType | - |
| [`SECURITY_​AUTO_​LOGIN_​AFTER_​CONFIRM`](#security_auto_login_after_confirm) | bool | - |
| [`SECURITY_​BLUEPRINT_​NAME`](#security_blueprint_name) | str | - |
| [`SECURITY_​CHANGEABLE`](#security_changeable) | bool | `configure_generic_parameters` |
| [`SECURITY_​CHANGE_​PASSWORD_​TEMPLATE`](#security_change_password_template) | str | - |
| [`SECURITY_​CHANGE_​SALT`](#security_change_salt) | str | - |
| [`SECURITY_​CHANGE_​URL`](#security_change_url) | str | - |
| [`SECURITY_​CLI_​ROLES_​NAME`](#security_cli_roles_name) | str | - |
| [`SECURITY_​CLI_​USERS_​NAME`](#security_cli_users_name) | str | - |
| [`SECURITY_​CONFIRMABLE`](#security_confirmable) | bool | `configure_generic_parameters` |
| [`SECURITY_​CONFIRM_​EMAIL_​WITHIN`](#security_confirm_email_within) | str | - |
| [`SECURITY_​CONFIRM_​ERROR_​VIEW`](#security_confirm_error_view) | NoneType | - |
| [`SECURITY_​CONFIRM_​SALT`](#security_confirm_salt) | str | - |
| [`SECURITY_​CONFIRM_​URL`](#security_confirm_url) | str | - |
| [`SECURITY_​DEFAULT_​HTTP_​AUTH_​REALM`](#security_default_http_auth_realm) | str | - |
| [`SECURITY_​DEFAULT_​REMEMBER_​ME`](#security_default_remember_me) | bool | - |
| [`SECURITY_​DEPRECATED_​HASHING_​SCHEMES`](#security_deprecated_hashing_schemes) | list | - |
| [`SECURITY_​DEPRECATED_​PASSWORD_​SCHEMES`](#security_deprecated_password_schemes) | list | - |
| [`SECURITY_​EMAIL_​HTML`](#security_email_html) | bool | - |
| [`SECURITY_​EMAIL_​PLAINTEXT`](#security_email_plaintext) | bool | - |
| [`SECURITY_​EMAIL_​SUBJECT_​CONFIRM`](#security_email_subject_confirm) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​PASSWORD_​CHANGE_​NOTICE`](#security_email_subject_password_change_notice) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​PASSWORD_​NOTICE`](#security_email_subject_password_notice) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​PASSWORD_​RESET`](#security_email_subject_password_reset) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​REGISTER`](#security_email_subject_register) | str | - |
| [`SECURITY_​FLASH_​MESSAGES`](#security_flash_messages) | bool | - |
| [`SECURITY_​FORGOT_​PASSWORD_​TEMPLATE`](#security_forgot_password_template) | str | - |
| [`SECURITY_​HASHING_​SCHEMES`](#security_hashing_schemes) | list | - |
| [`SECURITY_​I18N_​DIRNAME`](#security_i18n_dirname) | str | - |
| [`SECURITY_​I18N_​DOMAIN`](#security_i18n_domain) | str | - |
| [`SECURITY_​LOGIN_​SALT`](#security_login_salt) | str | - |
| [`SECURITY_​LOGIN_​URL`](#security_login_url) | str | - |
| [`SECURITY_​LOGIN_​USER_​TEMPLATE`](#security_login_user_template) | str | - |
| [`SECURITY_​LOGIN_​WITHIN`](#security_login_within) | str | - |
| [`SECURITY_​LOGIN_​WITHOUT_​CONFIRMATION`](#security_login_without_confirmation) | bool | `configure_generic_parameters` |
| [`SECURITY_​LOGOUT_​URL`](#security_logout_url) | str | - |
| [`SECURITY_​MSG_​ALREADY_​CONFIRMED`](#security_msg_already_confirmed) | tuple | - |
| [`SECURITY_​MSG_​CONFIRMATION_​EXPIRED`](#security_msg_confirmation_expired) | tuple | - |
| [`SECURITY_​MSG_​CONFIRMATION_​REQUEST`](#security_msg_confirmation_request) | tuple | - |
| [`SECURITY_​MSG_​CONFIRMATION_​REQUIRED`](#security_msg_confirmation_required) | tuple | - |
| [`SECURITY_​MSG_​CONFIRM_​REGISTRATION`](#security_msg_confirm_registration) | tuple | - |
| [`SECURITY_​MSG_​DISABLED_​ACCOUNT`](#security_msg_disabled_account) | tuple | - |
| [`SECURITY_​MSG_​EMAIL_​ALREADY_​ASSOCIATED`](#security_msg_email_already_associated) | tuple | - |
| [`SECURITY_​MSG_​EMAIL_​CONFIRMED`](#security_msg_email_confirmed) | tuple | - |
| [`SECURITY_​MSG_​EMAIL_​NOT_​PROVIDED`](#security_msg_email_not_provided) | tuple | - |
| [`SECURITY_​MSG_​FORGOT_​PASSWORD`](#security_msg_forgot_password) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​CONFIRMATION_​TOKEN`](#security_msg_invalid_confirmation_token) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​EMAIL_​ADDRESS`](#security_msg_invalid_email_address) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​LOGIN_​TOKEN`](#security_msg_invalid_login_token) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​PASSWORD`](#security_msg_invalid_password) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​REDIRECT`](#security_msg_invalid_redirect) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​RESET_​PASSWORD_​TOKEN`](#security_msg_invalid_reset_password_token) | tuple | - |
| [`SECURITY_​MSG_​LOCAL_​LOGIN_​DISABLED`](#security_msg_local_login_disabled) | tuple | - |
| [`SECURITY_​MSG_​LOGIN`](#security_msg_login) | tuple | - |
| [`SECURITY_​MSG_​LOGIN_​EMAIL_​SENT`](#security_msg_login_email_sent) | tuple | - |
| [`SECURITY_​MSG_​LOGIN_​EXPIRED`](#security_msg_login_expired) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​BREACHED`](#security_msg_password_breached) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​BREACHED_​SITE_​ERROR`](#security_msg_password_breached_site_error) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​CHANGE`](#security_msg_password_change) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​CHANGE_​DISABLED`](#security_msg_password_change_disabled) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​INVALID_​LENGTH`](#security_msg_password_invalid_length) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​IS_​THE_​SAME`](#security_msg_password_is_the_same) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​MISMATCH`](#security_msg_password_mismatch) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​NOT_​PROVIDED`](#security_msg_password_not_provided) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​NOT_​SET`](#security_msg_password_not_set) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RECOVERY_​DISABLED`](#security_msg_password_recovery_disabled) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET`](#security_msg_password_reset) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET_​DISABLED`](#security_msg_password_reset_disabled) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET_​EXPIRED`](#security_msg_password_reset_expired) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET_​REQUEST`](#security_msg_password_reset_request) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​TOO_​SIMPLE`](#security_msg_password_too_simple) | tuple | - |
| [`SECURITY_​MSG_​REFRESH`](#security_msg_refresh) | tuple | - |
| [`SECURITY_​MSG_​REGISTRATION_​DISABLED`](#security_msg_registration_disabled) | tuple | - |
| [`SECURITY_​MSG_​RETYPE_​PASSWORD_​MISMATCH`](#security_msg_retype_password_mismatch) | tuple | - |
| [`SECURITY_​MSG_​UNAUTHORIZED`](#security_msg_unauthorized) | tuple | - |
| [`SECURITY_​MSG_​USER_​DOES_​NOT_​EXIST`](#security_msg_user_does_not_exist) | tuple | - |
| [`SECURITY_​PASSWORD_​BREACHED_​COUNT`](#security_password_breached_count) | int | - |
| [`SECURITY_​PASSWORD_​CHECK_​BREACHED`](#security_password_check_breached) | bool | - |
| [`SECURITY_​PASSWORD_​COMPLEXITY_​CHECKER`](#security_password_complexity_checker) | NoneType | - |
| [`SECURITY_​PASSWORD_​HASH`](#security_password_hash) | str | - |
| [`SECURITY_​PASSWORD_​LENGTH_​MIN`](#security_password_length_min) | int | - |
| [`SECURITY_​PASSWORD_​SALT`](#security_password_salt) | str | - |
| [`SECURITY_​PASSWORD_​SCHEMES`](#security_password_schemes) | list | - |
| [`SECURITY_​PASSWORD_​SINGLE_​HASH`](#security_password_single_hash) | list | - |
| [`SECURITY_​POST_​CHANGE_​VIEW`](#security_post_change_view) | NoneType | - |
| [`SECURITY_​POST_​CONFIRM_​VIEW`](#security_post_confirm_view) | NoneType | - |
| [`SECURITY_​POST_​LOGIN_​VIEW`](#security_post_login_view) | str | - |
| [`SECURITY_​POST_​LOGOUT_​VIEW`](#security_post_logout_view) | str | - |
| [`SECURITY_​POST_​REGISTER_​VIEW`](#security_post_register_view) | NoneType | - |
| [`SECURITY_​POST_​RESET_​VIEW`](#security_post_reset_view) | NoneType | - |
| [`SECURITY_​RECOVERABLE`](#security_recoverable) | bool | `configure_generic_parameters` |
| [`SECURITY_​REGISTERABLE`](#security_registerable) | bool | `configure_generic_parameters` |
| [`SECURITY_​REGISTER_​URL`](#security_register_url) | str | - |
| [`SECURITY_​REGISTER_​USER_​TEMPLATE`](#security_register_user_template) | str | - |
| [`SECURITY_​RESET_​PASSWORD_​TEMPLATE`](#security_reset_password_template) | str | - |
| [`SECURITY_​RESET_​PASSWORD_​WITHIN`](#security_reset_password_within) | str | - |
| [`SECURITY_​RESET_​SALT`](#security_reset_salt) | str | - |
| [`SECURITY_​RESET_​URL`](#security_reset_url) | str | - |
| [`SECURITY_​SEND_​CONFIRMATION_​TEMPLATE`](#security_send_confirmation_template) | str | - |
| [`SECURITY_​SEND_​LOGIN_​TEMPLATE`](#security_send_login_template) | str | - |
| [`SECURITY_​SEND_​PASSWORD_​CHANGE_​EMAIL`](#security_send_password_change_email) | bool | - |
| [`SECURITY_​SEND_​PASSWORD_​RESET_​EMAIL`](#security_send_password_reset_email) | bool | - |
| [`SECURITY_​SEND_​PASSWORD_​RESET_​NOTICE_​EMAIL`](#security_send_password_reset_notice_email) | bool | - |
| [`SECURITY_​SEND_​REGISTER_​EMAIL`](#security_send_register_email) | bool | - |
| [`SECURITY_​SUBDOMAIN`](#security_subdomain) | NoneType | - |
| [`SECURITY_​TOKEN_​AUTHENTICATION_​HEADER`](#security_token_authentication_header) | str | - |
| [`SECURITY_​TOKEN_​AUTHENTICATION_​KEY`](#security_token_authentication_key) | str | - |
| [`SECURITY_​TOKEN_​MAX_​AGE`](#security_token_max_age) | NoneType | - |
| [`SECURITY_​TRACKABLE`](#security_trackable) | bool | - |
| [`SECURITY_​URL_​PREFIX`](#security_url_prefix) | NoneType | - |
| [`SECURITY_​USER_​IDENTITY_​ATTRIBUTES`](#security_user_identity_attributes) | list | - |
| [`SECURITY_​ZXCVBN_​MINIMUM_​SCORE`](#security_zxcvbn_minimum_score) | int | - |
| [`SEND_​FILE_​MAX_​AGE_​DEFAULT`](#send_file_max_age_default) | NoneType | `configure_generic_parameters` |
| [`SENTRY_​DSN`](#sentry_dsn) | NoneType | - |
| [`SERVER_​NAME`](#server_name) | NoneType | - |
| [`SESSION_​COOKIE_​DOMAIN`](#session_cookie_domain) | NoneType | `configure_generic_parameters` |
| [`SESSION_​COOKIE_​HTTPONLY`](#session_cookie_httponly) | bool | - |
| [`SESSION_​COOKIE_​NAME`](#session_cookie_name) | str | - |
| [`SESSION_​COOKIE_​PARTITIONED`](#session_cookie_partitioned) | bool | - |
| [`SESSION_​COOKIE_​PATH`](#session_cookie_path) | NoneType | - |
| [`SESSION_​COOKIE_​SAMESITE`](#session_cookie_samesite) | str | - |
| [`SESSION_​COOKIE_​SECURE`](#session_cookie_secure) | bool | `configure_generic_parameters` |
| [`SESSION_​KEY_​BITS`](#session_key_bits) | int | - |
| [`SESSION_​RANDOM_​SOURCE`](#session_random_source) | SystemRandom | - |
| [`SESSION_​REFRESH_​EACH_​REQUEST`](#session_refresh_each_request) | bool | - |
| [`SETTINGS_​TEMPLATE`](#settings_template) | str | `configure_ui` |
| [`SITEMAP_​MAX_​ENTRY_​COUNT`](#sitemap_max_entry_count) | int | - |
| [`SITEMAP_​ROOT_​VIEW_​ENABLED`](#sitemap_root_view_enabled) | bool | - |
| [`SITEMAP_​SECTIONS`](#sitemap_sections) | list | - |
| [`SITE_​API_​URL`](#site_api_url) | str | `configure_generic_parameters` |
| [`SITE_​UI_​URL`](#site_ui_url) | str | `configure_generic_parameters` |
| [`SQLALCHEMY_​BINDS`](#sqlalchemy_binds) | dict | - |
| [`SQLALCHEMY_​DATABASE_​URI`](#sqlalchemy_database_uri) | str | `configure_generic_parameters` |
| [`SQLALCHEMY_​ECHO`](#sqlalchemy_echo) | bool | - |
| [`SQLALCHEMY_​ENGINE_​OPTIONS`](#sqlalchemy_engine_options) | dict | - |
| [`SQLALCHEMY_​RECORD_​QUERIES`](#sqlalchemy_record_queries) | bool | - |
| [`SQLALCHEMY_​TRACK_​MODIFICATIONS`](#sqlalchemy_track_modifications) | bool | - |
| [`STATS_​AGGREGATIONS`](#stats_aggregations) | dict | `configure_stats` |
| [`STATS_​EVENTS`](#stats_events) | dict | `configure_stats` |
| [`STATS_​EVENTS_​UTC_​DATETIME_​ENABLED`](#stats_events_utc_datetime_enabled) | bool | - |
| [`STATS_​MQ_​EXCHANGE`](#stats_mq_exchange) | unknown | - |
| [`STATS_​PERMISSION_​FACTORY`](#stats_permission_factory) | unknown | `configure_stats` |
| [`STATS_​QUERIES`](#stats_queries) | dict | `configure_stats` |
| [`STATS_​REGISTER_​INDEX_​TEMPLATES`](#stats_register_index_templates) | bool | - |
| [`STATS_​REGISTER_​RECEIVERS`](#stats_register_receivers) | bool | `configure_stats` |
| [`TEMPLATES_​AUTO_​RELOAD`](#templates_auto_reload) | NoneType | - |
| [`TESTING`](#testing) | bool | - |
| [`THEME_​401_​TEMPLATE`](#theme_401_template) | str | - |
| [`THEME_​403_​TEMPLATE`](#theme_403_template) | str | - |
| [`THEME_​404_​TEMPLATE`](#theme_404_template) | str | - |
| [`THEME_​429_​TEMPLATE`](#theme_429_template) | str | - |
| [`THEME_​500_​TEMPLATE`](#theme_500_template) | str | - |
| [`THEME_​BASE_​TEMPLATE`](#theme_base_template) | str | - |
| [`THEME_​COVER_​TEMPLATE`](#theme_cover_template) | str | - |
| [`THEME_​CSS_​TEMPLATE`](#theme_css_template) | configured by function | `configure_ui` |
| [`THEME_​ERROR_​TEMPLATE`](#theme_error_template) | str | - |
| [`THEME_​FOOTER_​TEMPLATE`](#theme_footer_template) | str | `configure_ui` |
| [`THEME_​FRONTPAGE`](#theme_frontpage) | bool | `configure_ui` |
| [`THEME_​FRONTPAGE_​LOGO`](#theme_frontpage_logo) | configured by function | `configure_ui` |
| [`THEME_​FRONTPAGE_​TEMPLATE`](#theme_frontpage_template) | str | `configure_ui` |
| [`THEME_​FRONTPAGE_​TITLE`](#theme_frontpage_title) | LazyString | `configure_ui` |
| [`THEME_​GENERATOR`](#theme_generator) | str | - |
| [`THEME_​GOOGLE_​SITE_​VERIFICATION`](#theme_google_site_verification) | list | - |
| [`THEME_​HEADER_​LOGIN_​TEMPLATE`](#theme_header_login_template) | str | `configure_ui` |
| [`THEME_​HEADER_​TEMPLATE`](#theme_header_template) | str | `configure_ui` |
| [`THEME_​ICONS`](#theme_icons) | dict | - |
| [`THEME_​JAVASCRIPT_​TEMPLATE`](#theme_javascript_template) | str | `configure_ui` |
| [`THEME_​LOGO`](#theme_logo) | str | `configure_ui` |
| [`THEME_​LOGO_​ADMIN`](#theme_logo_admin) | str | - |
| [`THEME_​MATHJAX_​CDN`](#theme_mathjax_cdn) | str | - |
| [`THEME_​META_​ROBOT_​TAGS`](#theme_meta_robot_tags) | list | - |
| [`THEME_​SEARCHBAR`](#theme_searchbar) | bool | - |
| [`THEME_​SEARCH_​ENDPOINT`](#theme_search_endpoint) | str | `configure_ui` |
| [`THEME_​SETTINGS_​TEMPLATE`](#theme_settings_template) | str | - |
| [`THEME_​SHOW_​FRONTPAGE_​INTRO_​SECTION`](#theme_show_frontpage_intro_section) | unknown | `configure_ui` |
| [`THEME_​SITENAME`](#theme_sitename) | LazyString | `configure_ui` |
| [`THEME_​SITEURL`](#theme_siteurl) | str | - |
| [`THEME_​TRACKINGCODE_​TEMPLATE`](#theme_trackingcode_template) | str | `configure_ui` |
| [`THEME_​TWITTERHANDLE`](#theme_twitterhandle) | unknown | - |
| [`TRAP_​BAD_​REQUEST_​ERRORS`](#trap_bad_request_errors) | NoneType | - |
| [`TRAP_​HTTP_​EXCEPTIONS`](#trap_http_exceptions) | bool | - |
| [`TRUSTED_​HOSTS`](#trusted_hosts) | NoneType | `configure_generic_parameters` |
| [`TYPE_​CHECKING`](#type_checking) | bool | - |
| [`USERPROFILES`](#userprofiles) | bool | - |
| [`USERPROFILES_​BASE_​TEMPLATE`](#userprofiles_base_template) | str | - |
| [`USERPROFILES_​EMAIL_​ENABLED`](#userprofiles_email_enabled) | bool | - |
| [`USERPROFILES_​EXTEND_​SECURITY_​FORMS`](#userprofiles_extend_security_forms) | bool | - |
| [`USERPROFILES_​PROFILE_​TEMPLATE`](#userprofiles_profile_template) | str | - |
| [`USERPROFILES_​PROFILE_​URL`](#userprofiles_profile_url) | str | - |
| [`USERPROFILES_​READ_​ONLY`](#userprofiles_read_only) | bool | `configure_generic_parameters`, `configure_einfra_oidc` |
| [`USERPROFILES_​SETTINGS_​TEMPLATE`](#userprofiles_settings_template) | str | - |
| [`USERS_​RESOURCES_​AVATAR_​COLORS`](#users_resources_avatar_colors) | list | - |
| [`USERS_​RESOURCES_​DOMAINS_​ORG_​SCHEMA`](#users_resources_domains_org_schema) | unknown | - |
| [`USERS_​RESOURCES_​DOMAINS_​SEARCH`](#users_resources_domains_search) | dict | - |
| [`USERS_​RESOURCES_​DOMAINS_​SEARCH_​FACETS`](#users_resources_domains_search_facets) | dict | - |
| [`USERS_​RESOURCES_​DOMAINS_​SORT_​OPTIONS`](#users_resources_domains_sort_options) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ADMIN_​FACETS`](#users_resources_groups_admin_facets) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ADMIN_​SEARCH`](#users_resources_groups_admin_search) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ADMIN_​SORT_​OPTIONS`](#users_resources_groups_admin_sort_options) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ENABLED`](#users_resources_groups_enabled) | bool | - |
| [`USERS_​RESOURCES_​MODERATION_​LOCK_​DEFAULT_​TIMEOUT`](#users_resources_moderation_lock_default_timeout) | int | - |
| [`USERS_​RESOURCES_​MODERATION_​LOCK_​RENEWAL_​TIMEOUT`](#users_resources_moderation_lock_renewal_timeout) | int | - |
| [`USERS_​RESOURCES_​PROTECTED_​GROUP_​NAMES`](#users_resources_protected_group_names) | list | - |
| [`USERS_​RESOURCES_​SEARCH`](#users_resources_search) | dict | - |
| [`USERS_​RESOURCES_​SEARCH_​FACETS`](#users_resources_search_facets) | dict | - |
| [`USERS_​RESOURCES_​SERVICE_​SCHEMA`](#users_resources_service_schema) | unknown | - |
| [`USERS_​RESOURCES_​SORT_​OPTIONS`](#users_resources_sort_options) | dict | - |
| [`USER_​DASHBOARD_​MENU_​OVERRIDES`](#user_dashboard_menu_overrides) | dict | - |
| [`USE_​X_​SENDFILE`](#use_x_sendfile) | bool | - |
| [`VCS_​TEMPLATE_​INDEX`](#vcs_template_index) | unknown | - |
| [`VCS_​TEMPLATE_​INDEX_​ITEM`](#vcs_template_index_item) | unknown | - |
| [`VCS_​TEMPLATE_​RELEASE_​ITEM`](#vcs_template_release_item) | unknown | - |
| [`VCS_​TEMPLATE_​REPO_​SWITCH`](#vcs_template_repo_switch) | unknown | - |
| [`VCS_​TEMPLATE_​VIEW`](#vcs_template_view) | unknown | - |
| [`VOCABULARIES_​AFFILIATIONS_​EDMO_​COUNTRY_​MAPPING`](#vocabularies_affiliations_edmo_country_mapping) | dict | - |
| [`VOCABULARIES_​AFFILIATION_​SCHEMES`](#vocabularies_affiliation_schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_​AWARDS_​EC_​ROR_​ID`](#vocabularies_awards_ec_ror_id) | str | - |
| [`VOCABULARIES_​AWARDS_​OPENAIRE_​FUNDERS`](#vocabularies_awards_openaire_funders) | dict | - |
| [`VOCABULARIES_​AWARD_​SCHEMES`](#vocabularies_award_schemes) | dict | - |
| [`VOCABULARIES_​CF`](#vocabularies_cf) | list | - |
| [`VOCABULARIES_​CUSTOM_​VOCABULARY_​TYPES`](#vocabularies_custom_vocabulary_types) | list | - |
| [`VOCABULARIES_​DATASTREAM_​READERS`](#vocabularies_datastream_readers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_​DATASTREAM_​TRANSFORMERS`](#vocabularies_datastream_transformers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_​DATASTREAM_​WRITERS`](#vocabularies_datastream_writers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_​FACET_​CACHE_​SIZE`](#vocabularies_facet_cache_size) | int | - |
| [`VOCABULARIES_​FACET_​CACHE_​TTL`](#vocabularies_facet_cache_ttl) | int | - |
| [`VOCABULARIES_​FUNDER_​DOI_​PREFIX`](#vocabularies_funder_doi_prefix) | str | - |
| [`VOCABULARIES_​FUNDER_​SCHEMES`](#vocabularies_funder_schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_​IDENTIFIER_​SCHEMES`](#vocabularies_identifier_schemes) | dict | - |
| [`VOCABULARIES_​NAMES_​SCHEMES`](#vocabularies_names_schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_​ORCID_​ACCESS_​KEY`](#vocabularies_orcid_access_key) | str | - |
| [`VOCABULARIES_​ORCID_​ORG_​IDS_​MAPPING_​PATH`](#vocabularies_orcid_org_ids_mapping_path) | NoneType | - |
| [`VOCABULARIES_​ORCID_​SECRET_​KEY`](#vocabularies_orcid_secret_key) | str | - |
| [`VOCABULARIES_​ORCID_​SUMMARIES_​BUCKET`](#vocabularies_orcid_summaries_bucket) | str | - |
| [`VOCABULARIES_​ORCID_​SYNC_​MAX_​WORKERS`](#vocabularies_orcid_sync_max_workers) | int | - |
| [`VOCABULARIES_​ORCID_​SYNC_​SINCE`](#vocabularies_orcid_sync_since) | dict | - |
| [`VOCABULARIES_​RESOURCE_​CONFIG`](#vocabularies_resource_config) | unknown | `configure_generic_parameters` |
| [`VOCABULARIES_​SERVICE_​CONFIG`](#vocabularies_service_config) | unknown | `configure_generic_parameters` |
| [`VOCABULARIES_​SUBJECTS_​EUROSCIVOC_​FILE_​URL`](#vocabularies_subjects_euroscivoc_file_url) | str | - |
| [`VOCABULARIES_​SUBJECTS_​GEMET_​FILE_​URL`](#vocabularies_subjects_gemet_file_url) | str | - |
| [`VOCABULARIES_​SUBJECTS_​NVS_​FILE_​URL`](#vocabularies_subjects_nvs_file_url) | str | - |
| [`VOCABULARIES_​SUBJECTS_​SCHEMES`](#vocabularies_subjects_schemes) | dict | - |
| [`VOCABULARIES_​TYPES_​SEARCH`](#vocabularies_types_search) | dict | - |
| [`VOCABULARIES_​TYPES_​SORT_​OPTIONS`](#vocabularies_types_sort_options) | dict | - |
| [`VOCABULARY_​TYPE_​UI_​RESOURCE`](#vocabulary_type_ui_resource) | str | - |
| [`VOCABULARY_​TYPE_​UI_​RESOURCE_​CONFIG`](#vocabulary_type_ui_resource_config) | str | - |
| [`WEBPACKEXT_​MANIFEST_​PATH`](#webpackext_manifest_path) | str | - |
| [`WEBPACKEXT_​NPM_​PKG_​CLS`](#webpackext_npm_pkg_cls) | configured by function | `configure_ui` |
| [`WEBPACKEXT_​PROJECT`](#webpackext_project) | str | `configure_ui` |
| [`WEBPACKEXT_​PROJECT_​BUILDDIR`](#webpackext_project_builddir) | str | - |
| [`WEBPACKEXT_​PROJECT_​DISTDIR`](#webpackext_project_distdir) | str | - |
| [`WEBPACKEXT_​PROJECT_​DISTURL`](#webpackext_project_disturl) | str | - |
| [`WORKFLOWS`](#workflows) | dict | - |
| [`WORKFLOWS_​DEFAULT_​WORKFLOW`](#workflows_default_workflow) | str | - |

## Detailed Variable Reference

### ACCESS_ACTION_CACHE_PREFIX

Prefix for actions cached when used in dynamic permissions.

| **Invenio RDM Default Value** | `'Permission::action::'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L16) |

---


### ACCESS_CACHE

A cache instance or an importable string pointing to the cache instance.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L13); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L725) |

---


### ACCESS_LOAD_SYSTEM_ROLE_NEEDS

Enables the loading of system role needs when users' identity change.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L19) |

---


### ACCOUNTS

Tells if the templates should use the accounts module.

If False, you won't be able to login via the web UI.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L16) |

---


### ACCOUNTS_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### ACCOUNTS_CONFIRM_EMAIL_ENDPOINT

Value to be used for the confirmation email link in the UI application.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L57) |

---


### ACCOUNTS_COVER_TEMPLATE
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### ACCOUNTS_DEFAULT_EMAIL_VISIBILITY

Default Email visibility value can be set to either 'restricted' or 'public'.

| **Invenio RDM Default Value** | `'restricted'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L60) |

---


### ACCOUNTS_DEFAULT_USERS_VERIFIED

Default verified status: if set to 'True', users are verified by default.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L379) |

---


### ACCOUNTS_DEFAULT_USER_VISIBILITY

Default User visibility value can be set to either 'restricted' or 'public'.

| **Invenio RDM Default Value** | `'restricted'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L359) |

---


### ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT

Flask-Limiter rate limit string for forgot-password requests per account.

Example: ``"3 per hour"``. Disabled when ``None``.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L86) |

---


### ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_KEY_PREFIX

Prefix used to namespace forgot-password per-account limiter keys.

| **Invenio RDM Default Value** | `'accounts.fp_email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L92) |

---


### ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_MSG
| **Invenio RDM Default Value** | `l'Too many password-reset requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L95) |

---


### ACCOUNTS_JWT_ALOGORITHM

Set JWT encryption alogirthm.

.. note::

   `Available aglorithms
   <https://pyjwt.readthedocs.io/en/latest/algorithms.html>`_

| **Invenio RDM Default Value** | `'HS256'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L318) |

---


### ACCOUNTS_JWT_CREATION_FACTORY

Import path of factory used to generate JWT.

| **Invenio RDM Default Value** | `'invenio_accounts.utils:jwt_create_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L330) |

---


### ACCOUNTS_JWT_DECODE_FACTORY

Import path of factory used to decode JWT.

| **Invenio RDM Default Value** | `'invenio_accounts.utils:jwt_decode_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L327) |

---


### ACCOUNTS_JWT_DOM_TOKEN

Register JWT context processor.

.. code-block:: html

    {% if current_user.is_authenticated %}
        {{ jwt() }}
    {% endif %}

This will generate a ``hidden`` field as follows:

.. code-block:: html

    <input type="hidden" name="authorized_token" value="xxx">

On your API call you can use it with simple javascript, an example using
``jQuery`` is the following:

.. code-block:: javascript

    $.ajax({
        url: '/example',
        method: 'POST',
        beforeSend: function(request) {
            request.setRequestHeader(
                'Authorization',
                'Bearer ' + $('[name=authorized_token]').val()
            );
        },
    });

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L272) |

---


### ACCOUNTS_JWT_DOM_TOKEN_TEMPLATE

Template for the context processor.

| **Invenio RDM Default Value** | `'invenio_accounts/jwt.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L304) |

---


### ACCOUNTS_JWT_ENABLE

Enable JWT support.

.. note::

    More details about `JWT <https://jwt.io>`_

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L264) |

---


### ACCOUNTS_JWT_EXPIRATION_DELTA

Token expiration period for JWT.

| **Invenio RDM Default Value** | `datetime.timedelta(days=1)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L315) |

---


### ACCOUNTS_JWT_SECRET_KEY

Secret key for JWT.

.. note::

    If is set to ``None`` it will use the ``SECRET_KEY``.

| **Invenio RDM Default Value** | `'CHANGE_ME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L307) |

---


### **\*ACCOUNTS_LOCAL_LOGIN_ENABLED**

Whether or not login with local account credentials should be enabled.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L350) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### ACCOUNTS_LOGIN_RATELIMIT

Flask-Limiter rate limit string for login requests per account.

Example: ``"5 per 15 minutes"``. Disabled when ``None``.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L100) |

---


### ACCOUNTS_LOGIN_RATELIMIT_KEY_PREFIX

Prefix used to namespace login per-account limiter keys.

| **Invenio RDM Default Value** | `'accounts.login'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L106) |

---


### ACCOUNTS_LOGIN_RATELIMIT_MSG
| **Invenio RDM Default Value** | `l'Too many login attempts for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L109) |

---


### **\*ACCOUNTS_LOGIN_VIEW_FUNCTION**

The view function to use for the login endpoint.

This can be either an import string, or the view function itself.
If set to None, the default login view function from Flask-Security will be
left as is.

| **Invenio RDM Default Value** | `login` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L342) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### ACCOUNTS_REGISTER_BLUEPRINT

Register the Security blueprint or not.

It can be used to override the ``register_blueprint`` option.

.. note:: If the value is ``None``, then the blueprint is not registered.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L37) |

---


### ACCOUNTS_RESET_PASSWORD_ENDPOINT

Value to be used for the confirmation email link in the UI application.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L73) |

---


### ACCOUNTS_REST_AUTH_VIEWS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L128) |

```
{'login': 'invenio_accounts.views.rest:LoginView',
 'logout': 'invenio_accounts.views.rest:LogoutView',
 'user_info': 'invenio_accounts.views.rest:UserInfoView',
 'register': 'invenio_accounts.views.rest:RegisterView',
 'forgot_password': 'invenio_accounts.views.rest:ForgotPasswordView',
 'reset_password': 'invenio_accounts.views.rest:ResetPasswordView',
 'change_password': 'invenio_accounts.views.rest:ChangePasswordView',
 'send_confirmation': 'invenio_accounts.views.rest:SendConfirmationEmailView',
 'confirm_email': 'invenio_accounts.views.rest:ConfirmEmailView',
 'sessions_list': 'invenio_accounts.views.rest:SessionsListView',
 'sessions_item': 'invenio_accounts.views.rest:SessionsItemView'}
```

---


### ACCOUNTS_REST_CONFIRM_EMAIL_ENDPOINT

Value to be used for the confirmation email link in the API application.

Can be a Flask endpoint (e.g. "invenio_accounts_rest_auth.confirm_email"), or
a URL part (e.g. "https://ui.example.com/confirm-email", "/confirm-email").

This will be used to build an absolute URL, thus if e.g. a hostname isn't
included, the one from the current request's context will be used.

| **Invenio RDM Default Value** | `'/confirm/{token}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L63) |

---


### ACCOUNTS_REST_RESET_PASSWORD_ENDPOINT

Value to be used for the reset password link in the API application.

Can be a Flask endpoint (e.g. "invenio_accounts_rest_auth.reset_password"), or
a URL part (e.g. "https://ui.example.com/reset-password", "/reset-password").

This will be used to build an absolute URL, thus if e.g. a hostname isn't
included, the one from the current request's context will be used.

| **Invenio RDM Default Value** | `'/lost-password/{token}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L76) |

---


### ACCOUNTS_RETENTION_PERIOD
| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L22) |

---


### ACCOUNTS_SEND_CONFIRMATION_RATELIMIT

Flask-Limiter rate limit string for send-confirmation requests per account.

Example: ``"3 per hour"``. Disabled when ``None``.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L114) |

---


### ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_KEY_PREFIX

Prefix used to namespace send-confirmation per-account limiter keys.

| **Invenio RDM Default Value** | `'accounts.cf_email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L120) |

---


### ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_MSG
| **Invenio RDM Default Value** | `l'Too many confirmation-email requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L123) |

---


### ACCOUNTS_SESSION_ACTIVITY_ENABLED

Enable session activity tracking.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L51) |

---


### **\*ACCOUNTS_SESSION_REDIS_URL**

Redis URL used by the module as a cache system for sessions.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L34); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L391) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### ACCOUNTS_SESSION_STORE_FACTORY
| **Invenio RDM Default Value** | `'invenio_accounts.sessions:default_session_store_factory'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L24) |

---


### ACCOUNTS_SETTINGS_SECURITY_TEMPLATE

Template for the account security page.

| **Invenio RDM Default Value** | `'invenio_accounts/settings/security.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L54) |

---


### ACCOUNTS_SETTINGS_TEMPLATE
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### ACCOUNTS_SITENAME
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | unknown |

---


### ACCOUNTS_USERINFO_HEADERS

If True, add X-Session-ID and X-User-ID to the HTTP response.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L339); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L394) |

---


### ACCOUNTS_USERNAME_REGEX

The regular expression used for validating usernames.

.. note:: When this configuration value is overridden, the value for
          ``ACCOUNTS_USERNAME_RULES_TEXT`` should be updated as well,
          to reflect the changes.

| **Invenio RDM Default Value** | `'^[a-zA-Z][a-zA-Z0-9-_]{2,255}$'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L362) |

---


### ACCOUNTS_USERNAME_RULES_TEXT
| **Invenio RDM Default Value** | `l'Username must start with a letter, be at least three characters long and only contain alphanumeric...` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L370) |

---


### ACCOUNTS_USER_PREFERENCES_SCHEMA

The schema to use for validation of the user preferences.

| **Invenio RDM Default Value** | `<UserPreferencesSchema(many=False)>` |
|--------------|-----------|
| **Type** | UserPreferencesSchema |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L353); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L403) |

---


### ACCOUNTS_USER_PROFILE_SCHEMA

The schema to use for validation of the user profile.

| **Invenio RDM Default Value** | `<UserProfileSchema(many=False)>` |
|--------------|-----------|
| **Type** | UserProfileSchema |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L356) |

---


### ACCOUNTS_USE_CELERY

Tells if the module should use Celery or not.

By default, it uses Celery if it can find it.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L45) |

---


### ADMINISTRATION_APPNAME

Name of the Flask-Admin app (also the page title of admin panel).

| **Invenio RDM Default Value** | `'Invenio-Administration'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L10) |

---


### ADMINISTRATION_BASE_TEMPLATE

Admin panel base template.
By default (``None``) uses the Flask-Admin template.

| **Invenio RDM Default Value** | `'invenio_administration/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L6) |

---


### ADMINISTRATION_DASHBOARD_VIEW
| **Invenio RDM Default Value** | `'invenio_administration.views.dashboard.AdminDashboardView'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L13) |

---


### ADMINISTRATION_DISPLAY_VERSIONS

Display packages versions in the admin panel side bar.

Accepts a list of tuples in the format (package name, version).
Example: [("my-app", "v1.3.2")]

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L21); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1536) |

```
[]
```

---


### **\*ADMINISTRATION_THEME_BASE_TEMPLATE**

Administration base template.

| **Invenio RDM Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L18); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1539) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### ADMIN_BASE_TEMPLATE

Base template for the administration interface.

The template changes the administration interface from using a standard
Bootstrap interface to using
`AdminLTE 2 <https://almsaeedstudio.com/themes/AdminLTE/index2.html>`_.

The variable is defined in Invenio-Admin which will use the value defined here
if Invenio-Theme is installed.

| **Invenio RDM Default Value** | `'invenio_theme/page_admin.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L22) |

---


### ALEMBIC
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'script_location': '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_db/alembic',
 'version_locations': [('invenio_pages',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pages/alembic'),
                       ('invenio_checks',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_checks/alembic'),
                       ('invenio_records_files',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_files/alembic'),
                       ('invenio_vocabularies',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/alembic'),
                       ('invenio_oauthclient',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/alembic'),
                       ('oarepo_doi',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/oarepo_doi/alembic'),
                       ('jobs',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/alembic'),
                       ('invenio_audit_logs',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_audit_logs/alembic'),
                       ('invenio_collections',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_collections/alembic'),
                       ('oarepo_vocabularies',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/oarepo_vocabularies/alembic'),
                       ('invenio_userprofiles',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/alembic'),
                       ('invenio_files_rest',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/alembic'),
                       ('invenio_records',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records/alembic'),
                       ('oarepo_requests',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/oarepo_requests/alembic'),
                       ('invenio_access',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_access/alembic'),
                       ('oarepo_oidc_einfra',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/oarepo_oidc_einfra/alembic'),
                       ('invenio_oauth2server',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/alembic'),
                       ('invenio_requests',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/alembic'),
                       ('invenio_rdm_records',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/alembic'),
                       ('invenio_banners',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_banners/alembic'),
                       ('invenio_oaiserver',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/alembic'),
                       ('invenio_pidstore',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pidstore/alembic'),
                       ('invenio_communities',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/alembic'),
                       ('invenio_accounts',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/alembic')]}
```

---


### ALEMBIC_CONTEXT
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'transaction_per_migration': True,
 'compare_type': True,
 'autogenerate_plugins': ['alembic.autogenerate.*',
                          '~alembic.autogenerate.checkconstraint_byname'],
 'compare_server_default': True}
```

---


### ALLOWED_HTML_ATTRS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'*': ['class'],
 'a': ['href', 'title', 'name', 'class', 'rel'],
 'abbr': ['title'],
 'acronym': ['title']}
```

---


### ALLOWED_HTML_TAGS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['a',
 'abbr',
 'acronym',
 'b',
 'blockquote',
 'br',
 'code',
 'div',
 'table',
 'tbody',
 'td',
 'th',
 'tr',
 'em',
 'h1',
 'h2',
 'h3',
 'h4',
 'h5',
 'i',
 'li',
 'ol',
 'p',
 'pre',
 'span',
 'strike',
 'strong',
 'sub',
 'sup',
 'u',
 'ul']
```

---


### APPLICATION_ROOT
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### **\*APP_DEFAULT_SECURE_HEADERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L120) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui), [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'force_https': True,
 'force_https_permanent': False,
 'force_file_save': False,
 'frame_options': 'sameorigin',
 'frame_options_allow_from': None,
 'strict_transport_security': True,
 'strict_transport_security_preload': False,
 'strict_transport_security_max_age': 31556926,
 'strict_transport_security_include_subdomains': True,
 'content_security_policy': {'default-src': ["'self'"], 'object-src': ["'none'"]},
 'content_security_policy_report_uri': None,
 'content_security_policy_report_only': False,
 'session_cookie_secure': True,
 'session_cookie_http_only': True}
```

---


### APP_ENABLE_SECURE_HEADERS

Enable Secure Headers. (Default: ``True``)

In case you want to disable completely `Talisman`, you can set to `False`.

Remember that, for development purpose, setting ```DEBUG = True``` is already
enough to disable any side effects such as force ``https``.

.. note::
    `W3C
    <https://www.w3.org/TR/CSP2/>`_

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L107) |

---


### APP_HEALTH_BLUEPRINT_ENABLED

Enable the ping (healthcheck) blueprint. (Default: ``False``)

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L183) |

---


### **\*APP_LOGS_PERMISSION_POLICY**

Permission policy for job logs.

| **Invenio RDM Default Value** | `JobLogsPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L25) |
| **Set by** | [`configure_jobs`](reference/index.md#oarepo_config.configure_jobs) |

---


### APP_RDM_ADMIN_EMAIL_RECIPIENT

Admin e-mail

| **Invenio RDM Default Value** | `'info@inveniosoftware.org'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1038) |

---


### APP_RDM_DEPOSIT_FORM_AUTOCOMPLETE_NAMES

Behavior for autocomplete names search field for creators/contributors.

Available options:

- ``search`` (default): Show search field and form always.
- ``search_only``: Only show search field. Form displayed after selection or
  explicit "manual" entry.
- ``off``: Only show person form (no search field).

| **Invenio RDM Default Value** | `'search'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L984) |

---


### APP_RDM_DEPOSIT_FORM_CUSTOM_FIELD_DEFAULTS

Default values for custom fields in new records in the deposit UI.

The keys denote the dot-separated path, where in the record's custom field
values should be set (see invenio-records.dictutils).
If the value is callable, its return value will be used for the field
(e.g. lambda/function for dynamic calculation of values).

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L975) |

```
{}
```

---


### APP_RDM_DEPOSIT_FORM_DEFAULTS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L62); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L950) |

```
{'publication_date': <function <lambda>>}
```

---


### APP_RDM_DEPOSIT_FORM_PUBLISH_MODAL_EXTRA

Additional text/html to be displayed in the publish and submit for review modal.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1004) |

---


### **\*APP_RDM_DEPOSIT_FORM_QUOTA**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L995) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

```
{
    'maxFiles': 100,
    'maxStorage': RDM_FILES_DEFAULT_QUOTA_SIZE,
}
```

---


### APP_RDM_DEPOSIT_FORM_TEMPLATE

Deposit page's form template.

| **Invenio RDM Default Value** | `'invenio_app_rdm/records/deposit.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L788) |

---


### **\*APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED**

Feature toggle to enable the next-generation (NG) file uploader UI in the deposit form.

When enabled, the deposit form will use the new Uppy.io-based file uploader, replacing the current file upload interface.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L943) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*APP_RDM_DETAIL_SIDE_BAR_TEMPLATES**
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1014) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

```
[
    'invenio_app_rdm/records/details/side_bar/manage_menu.html',
    'invenio_app_rdm/records/details/side_bar/metrics.html',
    'invenio_app_rdm/records/details/side_bar/versions.html',
    'invenio_app_rdm/records/details/side_bar/external_resources.html',
    'invenio_app_rdm/records/details/side_bar/communities.html',
    'invenio_app_rdm/records/details/side_bar/keywords_subjects.html',
    'invenio_app_rdm/records/details/side_bar/details.html',
    'invenio_app_rdm/records/details/side_bar/locations.html',
    'invenio_app_rdm/records/details/side_bar/licenses.html',
    'invenio_app_rdm/records/details/side_bar/citations.html',
    'invenio_app_rdm/records/details/side_bar/export.html',
    'invenio_app_rdm/records/details/side_bar/technical_metadata.html',
]
```

---


### APP_RDM_DISPLAY_DECIMAL_FILE_SIZES

Display the file sizes in powers of 1000 (KB, ...) or 1024 (KiB, ...).

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1001) |

---


### APP_RDM_FILES_INTEGRITY_REPORT_SUBJECT

Files integrity report subject

| **Invenio RDM Default Value** | `_('Files integrity report')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1035) |

---


### APP_RDM_FILES_INTEGRITY_REPORT_TEMPLATE
| **Invenio RDM Default Value** | `'invenio_app_rdm/files_integrity_report/email/files_integrity_report.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1030) |

---


### **\*APP_RDM_IDENTIFIER_SCHEMES_UI**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1041) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{
    'orcid': {
        'url_prefix': 'http://orcid.org/',
        'icon': 'images/orcid.svg',
        'label': 'ORCID',
    },
    'ror': {
        'url_prefix': 'https://ror.org/',
        'icon': 'images/ror-icon.svg',
        'label': 'ROR',
    },
    'gnd': {
        'url_prefix': 'http://d-nb.info/gnd/',
        'icon': 'images/gnd-icon.svg',
        'label': 'GND',
    },
}
```

---


### APP_RDM_MODERATION_REQUEST_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1591) |

```
{'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'status'}},
 'is_open': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
             'ui': {'field': 'is_open'}}}
```

---


### APP_RDM_MODERATION_REQUEST_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1560) |

```
{'facets': ['status', 'is_open'],
 'sort': ['bestmatch', 'newest', 'oldest', 'newestactivity', 'oldestactivity']}
```

---


### APP_RDM_MODERATION_REQUEST_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1566) |

```
{'bestmatch': {'title': 'Best match', 'fields': ['_score']},
 'newest': {'title': 'Newest', 'fields': ['-created']},
 'oldest': {'title': 'Oldest', 'fields': ['created']},
 'newestactivity': {'title': 'Newest activity', 'fields': ['-last_activity_at']},
 'oldestactivity': {'title': 'Oldest activity', 'fields': ['last_activity_at']}}
```

---


### APP_RDM_PAGES

Register static pages with predefined initial content from 'pages.yaml' file.

Example:
{
    "about": "/about",
    "terms": "/terms",
    "privacy-policy": "/privacy-policy",
}

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1228) |

```
{}
```

---


### APP_RDM_RECORDS_EXPORT_URL
| **Invenio RDM Default Value** | `'/records/<pid_value>/export/<export_format>'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L941) |

---


### APP_RDM_RECORD_EXPORTERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L819) |

```
{
    'json': {
        'name': _('JSON'),
        'serializer': 'flask_resources.serializers:JSONSerializer',
        'params': {
            'options': {
                'indent': 2,
                'sort_keys': True,
            },
        },
        'content-type': 'application/json',
        'filename': '{id}.json',
    },
    'json-ld': {
        'name': _('JSON-LD'),
        'serializer': 'invenio_rdm_records.resources.serializers:SchemaorgJSONLDSerializer',
        'content-type': 'application/ld+json',
        'filename': '{id}.json',
    },
    'csl': {
        'name': _('CSL'),
        'serializer': 'invenio_rdm_records.resources.serializers:CSLJSONSerializer',
        'params': {
            'options': {
                'indent': 2,
                'sort_keys': True,
            },
        },
        'content-type': 'application/vnd.citationstyles.csl+json',
        'filename': '{id}.json',
    },
    'datacite-json': {
        'name': _('DataCite JSON'),
        'serializer': 'invenio_rdm_records.resources.serializers:DataCite45JSONSerializer',
        'params': {
            'options': {
                'indent': 2,
                'sort_keys': True,
            },
        },
        'content-type': 'application/vnd.datacite.datacite+json',
        'filename': '{id}.json',
    },
    'datacite-xml': {
        'name': _('DataCite XML'),
        'serializer': 'invenio_rdm_records.resources.serializers:DataCite45XMLSerializer',
        'params': {},
        'content-type': 'application/vnd.datacite.datacite+xml',
        'filename': '{id}.xml',
    },
    'dublincore': {
        'name': _('Dublin Core XML'),
        'serializer': 'invenio_rdm_records.resources.serializers:DublinCoreXMLSerializer',
        'params': {},
        'content-type': 'application/x-dc+xml',
        'filename': '{id}.xml',
    },
    'marcxml': {
        'name': _('MARCXML'),
        'serializer': 'invenio_rdm_records.resources.serializers:MARCXMLSerializer',
        'params': {},
        'content-type': 'application/marcxml+xml',
        'filename': '{id}.xml',
    },
    'bibtex': {
        'name': _('BibTeX'),
        'serializer': 'invenio_rdm_records.resources.serializers:BibtexSerializer',
        'params': {},
        'content-type': 'application/x-bibtex',
        'filename': '{id}.bib',
    },
    'geojson': {
        'name': _('GeoJSON'),
        'serializer': 'invenio_rdm_records.resources.serializers:GeoJSONSerializer',
        'params': {
            'options': {
                'indent': 2,
                'sort_keys': True,
            },
        },
        'content-type': 'application/vnd.geo+json',
        'filename': '{id}.geojson',
    },
    'dcat-ap': {
        'name': _('DCAT'),
        'serializer': 'invenio_rdm_records.resources.serializers:DCATSerializer',
        'params': {},
        'content-type': 'application/dcat+xml',
        'filename': '{id}.xml',
    },
    'codemeta': {
        'name': _('Codemeta'),
        'serializer': 'invenio_rdm_records.resources.serializers:CodemetaSerializer',
        'params': {},
        'content-type': 'application/ld+json',
        'filename': '{id}.json',
    },
    'cff': {
        'name': _('Citation File Format'),
        'serializer': 'invenio_rdm_records.resources.serializers:CFFSerializer',
        'params': {},
        'content-type': 'application/x-yaml',
        'filename': '{id}.yaml',
    },
    'datapackage': {
        'name': _('Data Package JSON'),
        'serializer': 'invenio_rdm_records.resources.serializers:DataPackageSerializer',
        'params': {},
        'content-type': 'application/ld+json',
        'filename': '{id}.json',
    },
}
```

---


### APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS

Default format used for adding badges to a record.

Make sure the 'render' field points to a valid render function in invenio_app_rdm.records_ui.utils.
Example implementation can also be found in invenio_app_rdm.records_ui.utils.

APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS = [
    {
        "id": "github",
        "render": github_link_render,
    },
    {
        "id": "openaire",
        "render": openaire_link_render,
    },
}

def github_link_render(record):
    ...

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L920) |

```
[]
```

---


### APP_RDM_RECORD_LANDING_PAGE_FAIR_SIGNPOSTING_LEVEL_1_ENABLED
| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1009) |

---


### APP_RDM_RECORD_LANDING_PAGE_TEMPLATE
| **OARepo Default Value** | `'oarepo_rdm/record_detail_iframe.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L60); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1007) |

---


### APP_RDM_RECORD_THUMBNAIL_SIZES

Allowed record thumbnail sizes.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1011) |

```
[
    10,
    50,
    100,
    250,
    750,
    1200,
]
```

---


### APP_RDM_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L797) |

```
{'index': '/',
 'robots': '/robots.txt',
 'help_search': '/help/search',
 'help_statistics': '/help/statistics',
 'help_versioning': '/help/versioning',
 'record_search': '/search',
 'record_detail': '/records/<pid_value>',
 'record_export': '/records/<pid_value>/export/<export_format>',
 'record_file_preview': '/records/<pid_value>/preview/<path:filename>',
 'record_container_item_preview': '/records/<pid_value>/preview/<path:filename>/container/<path:path>',
 'record_file_download': '/records/<pid_value>/files/<path:filename>',
 'record_container_item_download': '/records/<pid_value>/files/<path:filename>/container/<path:path>',
 'record_thumbnail': '/records/<pid_value>/thumb<int:size>',
 'record_media_file_download': '/records/<pid_value>/media-files/<path:filename>',
 'record_from_pid': '/<any({schemes}):pid_scheme>/<path:pid_value>',
 'record_latest': '/records/<pid_value>/latest',
 'dashboard_home': '/me',
 'deposit_create': '/uploads/new',
 'deposit_edit': '/uploads/<pid_value>'}
```

---


### APP_RDM_SUBCOMMUNITIES_LABEL

Label for the subcommunities in the community browse page.

| **Invenio RDM Default Value** | `_('Subcommunities')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1543) |

---


### APP_RDM_USER_DASHBOARD_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L791) |

```
{'uploads': '/me/uploads', 'communities': '/me/communities', 'requests': '/me/requests'}
```

---


### APP_REQUESTID_HEADER

Name of header containing a request id (max length 200 characters).

If set, the request id will be extracted from the header and set on the global
Flask ``g`` request object. The extracted request id can be used by other
Invenio modules - e.g. Invenio-Logging could include it in log messages.

The request id can be used to trace requests between systems to make
troubleshooting easier.

You can configure Nginx 1.10+ to automatically generate a request id and
add it as a header to both the upstream WSGI server and downstream client::

    add_header X-Request-ID $request_id;

Set to ``None`` to not extract a request id.

| **Invenio RDM Default Value** | `'X-Request-Id'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L187) |

---


### **\*APP_THEME**

Application-wide themes list used for template and assets lookup.

The value is a list of theme strings applied in a fallback fashion in the order
they are specified:

.. code-block:: python

    APP_THEME = ['my-overlay', 'semantic-ui']

From the above example, templates and assets with the ``my-overlay`` prefix
will be looked up first, and if not found the ``semantic-ui`` prefix will be
used. If none of the lookups are successful, a non-prefixed lookup is done.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L92); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L263) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*ASSETS_BUILDER**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### AUDIT_LOGS_DISABLED_ACTIONS

Disabled actions to be excluded from the audit logs.
To find all the available actions, check the entry points in the `invenio_audit_logs.actions` group.
```python
>>> from invenio_base.utils import entry_points
>>> [ep.name for ep in entry_points(group="invenio_audit_logs.actions")]
```

| **Invenio RDM Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L48) |

```
set()
```

---


### **\*AUDIT_LOGS_ENABLED**

Feature flag. Disabled by default.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L45) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### AUDIT_LOGS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L20) |

```
{'resource': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
              'ui': {'field': 'resource.type'}},
 'action_name': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                 'ui': {'field': 'action'}}}
```

---


### AUDIT_LOGS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L10) |

```
{'facets': ['resource', 'action_name'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---


### AUDIT_LOGS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L38) |

```
{'bestmatch': {'title': 'Best match', 'fields': ['_score']},
 'newest': {'title': 'Newest', 'fields': ['-@timestamp']},
 'oldest': {'title': 'Oldest', 'fields': ['@timestamp']}}
```

---


### **\*BABEL_DEFAULT_LOCALE**

Default locale (language).

| **Invenio RDM Default Value** | `'en'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L243) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*BABEL_DEFAULT_TIMEZONE**

Default time zone.

| **Invenio RDM Default Value** | `'Europe/Zurich'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L246) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### BANNERS_CATEGORIES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L11) |

```
[('info', l'Info'), ('warning', l'Warning'), ('other', l'Other')]
```

---


### BANNERS_CATEGORIES_TO_STYLE

Function to transform the banner category to a specific Semantic-UI class.

| **Invenio RDM Default Value** | `style_category` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L18) |

---


### BANNERS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L21) |

```
{'facets': [], 'sort': ['url_path', 'start_datetime', 'end_datetime', 'active']}
```

---


### BANNERS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L32) |

```
{'url_path': {'title': l'URL path', 'fields': ['url_path']},
 'start_datetime': {'title': l'Start DateTime', 'fields': ['start_datetime']},
 'end_datetime': {'title': l'End DateTime', 'fields': ['end_datetime']},
 'active': {'title': l'Active', 'fields': ['active']}}
```

---


### **\*BASE_TEMPLATE**

Base template for user facing pages.

The template provides a basic skeleton which takes care of loading assets,
embedding header metadata and define basic template blocks. All other user
facing templates usually extends from this template and thus changing this
template allows to change design and layout of Invenio.

| **Invenio RDM Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L9); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L266) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*BROKER_URL**

URL of message broker for Celery 3 (default is RabbitMQ).

| **Invenio RDM Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L424); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L11) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### CACHE_IS_AUTHENTICATED_CALLBACK

Import path to callback.

Callback is executed to determine if request is authenticated.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L30) |

---


### CACHE_KEY_PREFIX

Cache key prefix.

| **Invenio RDM Default Value** | `'cache::'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L16) |

---


### **\*CACHE_REDIS_URL**

Redis location and database.

| **Invenio RDM Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L26); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L715) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### CACHE_TYPE

Cache type.

Please refer to Flask-Caching documentation for other cache types.

| **Invenio RDM Default Value** | `'flask_caching.backends.RedisCache'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L20); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L718) |

---


### CELERY_ACCEPT_CONTENT

A whitelist of content-types/serializers.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L18) |

```
['json', 'msgpack', 'yaml']
```

---


### **\*CELERY_BEAT_SCHEDULE**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L427) |
| **Set by** | [`configure_cron`](reference/index.md#oarepo_config.configure_cron) |

```
{
    'indexer': {
        'task': 'invenio_records_resources.tasks.manage_indexer_queues',
        'schedule': timedelta(seconds=10),
    },
    'accounts_sessions': {
        'task': 'invenio_accounts.tasks.clean_session_table',
        'schedule': timedelta(minutes=60),
    },
    'accounts_ips': {
        'task': 'invenio_accounts.tasks.delete_ips',
        'schedule': timedelta(hours=6),
    },
    'update_domain_status': {
        'task': 'invenio_accounts.tasks.update_domain_status',
        'schedule': timedelta(hours=4),
    },
    'draft_resources': {
        'task': 'invenio_drafts_resources.services.records.tasks.cleanup_drafts',
        'schedule': timedelta(minutes=60),
    },
    'rdm_records': {
        'task': 'invenio_rdm_records.services.tasks.update_expired_embargos',
        'schedule': crontab(minute=2, hour=0),
    },
    'expire_requests': {
        'task': 'invenio_requests.tasks.check_expired_requests',
        'schedule': crontab(minute=3, hour=0),
    },
    'file-checks': {
        'task': 'invenio_files_rest.tasks.schedule_checksum_verification',
        'schedule': timedelta(hours=1),
        'kwargs': {
            'batch_interval': {
                'hours': 1,
            },
            'frequency': {
                'days': 14,
            },
            'max_count': 0,
            'files_query': 'invenio_app_rdm.utils.files.checksum_verification_files_query',
        },
    },
    'file-integrity-report': {
        'task': 'invenio_app_rdm.tasks.file_integrity_report',
        'schedule': crontab(minute=0, hour=7),
    },
    'stats-process-events': {
        **StatsEventTask,
        'schedule': crontab(minute='25,55'),
    },
    'stats-aggregate-events': {
        **StatsAggregationTask,
        'schedule': crontab(minute=0),
    },
    'reindex-stats': StatsRDMReindexTask,
    'clear-cache': {
        'task': 'invenio_communities.tasks.clear_cache',
        'schedule': crontab(minute=0, hour=1),
    },
    'clean-access-request-tokens': {
        'task': 'invenio_rdm_records.requests.access.tasks.clean_expired_request_access_tokens',
        'schedule': crontab(minute=4, hour=0),
    },
    'delete-job-logs': {
        'task': 'invenio_jobs.logging.tasks.delete_logs',
        'schedule': crontab(minute=5, hour=0),
    },
    'update_sitemap': {
        'task': 'invenio_sitemap.tasks.update_sitemap_cache',
        'schedule': crontab(minute=0, hour=2),
    },
    'update-collections-size': {
        'task': 'invenio_rdm_records.collections.tasks.update_collections_size',
        'schedule': timedelta(hours=1),
    },
}
```

---


### **\*CELERY_BROKER_URL**

Same as BROKER_URL to support Celery 4.

| **Invenio RDM Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L507); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L12) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*CELERY_RESULT_BACKEND**

URL of backend for result storage (default is Redis).

| **Invenio RDM Default Value** | `'redis://localhost:6379/1'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L510); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L15) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### CELERY_RESULT_SERIALIZER

Result serialization format. Default is ``msgpack``.

| **Invenio RDM Default Value** | `'msgpack'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L21) |

---


### CELERY_TASK_SERIALIZER

The default serialization method to use. Default is ``msgpack``.

| **Invenio RDM Default Value** | `'msgpack'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L24) |

---


### CHECKS_COMMUNITIES_SERVICE_COMPONENTS

Extra components that are registered to COMMUNITIES_SERVICE_COMPONENTS.

The default (RegisterCheckComponent) will create a LLM configuration for a community
whenever it is added/modified.

| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-checks](https://github.com/oarepo/oarepo-checks/blob/master/oarepo_checks/config.py#L15) |

```
[
    RegisterCheckComponent,
]
```

---


### **\*CHECKS_ENABLED**

Enable checks.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-checks](https://github.com/inveniosoftware/invenio-checks/blob/master/invenio_checks/config.py#L6) |
| **Set by** | [`configure_llm`](reference/index.md#oarepo_config.configure_llm) |

---


### **\*CHECKS_GENERIC_COMMUNITY**

A slug of community that is used for LLM prompt when record does not belong to a community.

| **OARepo Default Value** | `'generic-community'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-checks](https://github.com/oarepo/oarepo-checks/blob/master/oarepo_checks/config.py#L12) |
| **Set by** | [`configure_llm`](reference/index.md#oarepo_config.configure_llm) |

---


### COLLECTIONS_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### COLLECTIONS_MAX_COLLECTIONS_PER_TREE

Maximum number of collections allowed per tree.

This counts all collections in a tree, regardless of depth.
Set to 0 for unlimited collections.
Default: 100

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L25) |

---


### COLLECTIONS_MAX_DEPTH

Maximum depth for collection hierarchies.

Depth 0 = root collections
Depth 1 = children of root
Depth 2 = grandchildren (not allowed by default)

Setting this to 1 allows 2 levels: root + children only.
Setting this to 2 would allow 3 levels: root + children + grandchildren.

| **Invenio RDM Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L7) |

---


### COLLECTIONS_MAX_TREES

Maximum number of collection trees allowed per namespace.

Set to 0 for unlimited trees.
Default: 10

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L18) |

---


### COLLECTIONS_PERMISSION_POLICY

Permission policy used by invenio-collections for managing collection trees.

| **Invenio RDM Default Value** | `CommunityPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L20) |

---


### COLLECT_STATIC_ROOT
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### **\*COLLECT_STORAGE**

Static files collection method (defaults to copying files).

| **Invenio RDM Default Value** | `'flask_collect.storage.link'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L382) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### COMMUNITIES_ALLOW_MEMBERSHIP_REQUESTS

Feature flag for membership request.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L372) |

---


### COMMUNITIES_ALLOW_RESTRICTED
| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L353) |

---


### COMMUNITIES_ALWAYS_SHOW_CREATE_LINK

Controls visibility of 'New Community' btn based on user's permission when set to True.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L369) |

---


### COMMUNITIES_COLLECTIONS_ENABLED

Feature flag to enable/disable collections feature.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L378) |

---


### COMMUNITIES_CUSTOM_FIELDS

Communities custom fields definition.

Of the shape:

.. code-block:: python

    [
        <custom-field-class-type(name='field')>,
        # ...
        <custom-field-class-type(name='fieldN')>'
    ]

For example:

.. code-block:: python

    [
        TextCF(name="experiment"),
        ...
    ]

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L285) |

```
[<oarepo_communities.services.custom_fields.workflow.WorkflowCF object>,
 <oarepo_communities.services.custom_fields.workflow.WorkflowCF object>]
```

---


### COMMUNITIES_CUSTOM_FIELDS_UI

Communities custom fields UI configuration.

Of the shape:

.. code-block:: python

    [{
        section: <section_name>,
        fields: [
            {
                field: "path-to-field",  # this should be validated against the defined fields in `RDM_CUSTOM_FIELDS`
                ui_widget: "<ui-widget-name>",  # predefined or user defined ui widget
                props: {
                    label:"<ui-label-to-display>",
                    placeholder:"<placeholder-passed-to-widget>",
                    icon:"<icon-passed-to-widget>",
                    description:"<description-passed-to-widget>",
                }
            },
        ],

        # ...
    }]

For example:

.. code-block:: python

    [{
        "section": "CERN Experiment"
        "fields" : [{
            field: "experiment",  # this should be validated against the defined fields in `RDM_CUSTOM_FIELDS`
            ui_widget: "CustomTextField",  # user defined widget in my-site
            props: {
                label: "Experiment",
                placeholder: "Type an experiment...",
                icon: "pencil",
                description: "You should fill this field with one of the experiments e.g LHC, ATLAS etc.",
            }
        },
        ...
    }]

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L308) |

```
[{'section': l'Workflows',
  'fields': [{'field': 'workflow',
              'ui_widget': 'Dropdown',
              'props': {'label': l'Default workflow',
                        'description': l'Default workflow for the community if workflow is not specified when depositing a record.',
                        'options': []}},
             {'field': 'allowed_workflows',
              'ui_widget': 'Dropdown',
              'props': {'label': l'Allowed workflows',
                        'multiple': True,
                        'description': l'Workflows allowed for the community.',
                        'options': []}}]}]
```

---


### COMMUNITIES_DEFAULT_RECORD_SUBMISSION_POLICY

Default value of record submission policy community access setting.

| **Invenio RDM Default Value** | `<RecordSubmissionPolicyEnum.OPEN: 'open'>` |
|--------------|-----------|
| **Type** | RecordSubmissionPolicyEnum |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L375) |

---


### COMMUNITIES_ERROR_HANDLERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1071) |

```
{
    **community_error_handlers,
    InvalidCommunityVisibility: create_error_handler(lambda e: HTTPJSONException(code=400, description=e.reason)),
}
```

---


### COMMUNITIES_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L47) |

```
{'type': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
          'ui': {'field': 'type'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                'ui': {'field': 'visibility'}}}
```

---


### COMMUNITIES_IDENTITIES_CACHE_HANDLER
| **Invenio RDM Default Value** | `'invenio_communities.cache.redis:IdentityRedisCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L363) |

---


### **\*COMMUNITIES_IDENTITIES_CACHE_REDIS_URL**
| **Invenio RDM Default Value** | `'redis://localhost:6379/4'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L360) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### COMMUNITIES_IDENTITIES_CACHE_TIME
| **Invenio RDM Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L357) |

---


### COMMUNITIES_INVITATIONS_EXPIRES_IN

Default amount of time before an invitation expires.

| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L231) |

---


### COMMUNITIES_INVITATIONS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L205) |

```
{'facets': ['type', 'status'], 'sort': ['bestmatch', 'name', 'newest', 'oldest']}
```

---


### COMMUNITIES_INVITATIONS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L211) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'name': {'title': l'Name', 'fields': ['user.profile.full_name.keyword']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']}}
```

---


### COMMUNITIES_LOGO_MAX_FILE_SIZE

Community logo size quota, in bytes.

| **Invenio RDM Default Value** | `1000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L266) |

---


### COMMUNITIES_MEMBERSHIP_REQUESTS_DEFAULT_ROLE

Role assigned to a member who joins via a membership request.

Must be the ``name`` of one of the roles defined in ``COMMUNITIES_ROLES``.
Deployments that customise ``COMMUNITIES_ROLES`` (and therefore may not define a
``reader`` role) can point this at their own lowest-privilege role.

| **Invenio RDM Default Value** | `'reader'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L259) |

---


### COMMUNITIES_MEMBERSHIP_REQUESTS_EXPIRES_IN

Default amount of time before a membership request expires.

| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L256) |

---


### COMMUNITIES_MEMBERSHIP_REQUESTS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L240) |

```
{'role': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
          'ui': {'field': 'role'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'role'}}}
```

---


### COMMUNITIES_MEMBERSHIP_REQUESTS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L234) |

```
{'facets': ['role', 'status'], 'sort': ['bestmatch', 'name', 'newest', 'oldest']}
```

---


### COMMUNITIES_MEMBERS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L189) |

```
{'role': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
          'ui': {'field': 'role'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                'ui': {'field': 'visible'}}}
```

---


### COMMUNITIES_MEMBERS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L163) |

```
{'facets': ['role', 'visibility'], 'sort': ['bestmatch', 'name', 'newest', 'oldest']}
```

---


### COMMUNITIES_MEMBERS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L169) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'name': {'title': l'Name', 'fields': ['user.profile.full_name.keyword']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']}}
```

---


### COMMUNITIES_NAMESPACES

Custom fields namespaces.

.. code-block:: python
    {<namespace>: <uri>, ...}

For example:

.. code-block:: python
    {
        "cern": "https://cern.ch/terms",
        "dwc": "http://rs.tdwg.org/dwc/terms/"
    }

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L269) |

```
{}
```

---


### COMMUNITIES_OAI_SETS_PREFIX
| **Invenio RDM Default Value** | `'community-'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L367) |

---


### **\*COMMUNITIES_PERMISSION_POLICY**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/communities.py#L68) |
| **Set by** | [`configure_communities`](reference/index.md#oarepo_config.configure_communities) |

---


### COMMUNITIES_RECORDS_SEARCH
| **OARepo Default Value** | `LocalProxy(lambda: current_oarepo_rdm.dynamic_rdm_search)` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L72); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1081) |

---


### COMMUNITIES_RECORDS_SEARCH_ALL
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### **\*COMMUNITIES_REGISTER_UI_BLUEPRINT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/communities.py#L68) |
| **Set by** | [`configure_communities`](reference/index.md#oarepo_config.configure_communities) |

---


### COMMUNITIES_REQUESTS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L157) |

```
{'facets': ['type', 'status'],
 'sort': ['bestmatch', 'newest', 'oldest', 'newestactivity', 'oldestactivity']}
```

---


### **\*COMMUNITIES_ROLES**
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L104) |
| **Set by** | [`configure_communities`](reference/index.md#oarepo_config.configure_communities) |

```
[{'name': 'reader',
  'title': l'Reader',
  'description': l'Can view restricted records.',
  'can_view': True},
 {'name': 'curator',
  'title': l'Curator',
  'description': l'Can curate records and view restricted records.',
  'can_curate': True,
  'can_view': True},
 {'name': 'manager',
  'title': l'Manager',
  'description': l'Can manage members, curate records and view restricted records.',
  'can_manage_roles': ['manager', 'curator', 'reader'],
  'can_manage': True,
  'can_curate': True,
  'can_view': True},
 {'name': 'owner',
  'title': l'Owner',
  'description': l'Full administrative access to the entire community.',
  'can_manage_roles': ['owner', 'manager', 'curator', 'reader'],
  'is_owner': True,
  'can_manage': True,
  'can_curate': True,
  'can_view': True}]
```

---


### COMMUNITIES_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L23) |

```
{'frontpage': '/communities',
 'search': '/communities-search',
 'deprecated_search': '/communities/search',
 'new': '/communities-new',
 'deprecated_new': '/communities/new',
 'upload': '/communities/<pid_value>/upload',
 'requests': '/communities/<pid_value>/requests',
 'subcommunities': '/communities/<pid_value>/browse/subcommunities',
 'new_subcommunity': '/communities/<pid_value>/subcommunities/new',
 'settings': '/communities/<pid_value>/settings',
 'settings_privileges': '/communities/<pid_value>/settings/privileges',
 'settings_submission_policy': '/communities/<pid_value>/settings/submission-policy',
 'settings_pages': '/communities/<pid_value>/settings/pages',
 'settings_collections': '/communities/<pid_value>/settings/collections',
 'members': '/communities/<pid_value>/members',
 'invitations': '/communities/<pid_value>/invitations',
 'membership_requests': '/communities/<pid_value>/membership-requests',
 'about': '/communities/<pid_value>/about',
 'curation_policy': '/communities/<pid_value>/curation-policy',
 'my_communities': '/me/communities'}
```

---


### COMMUNITIES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L142) |

```
{'facets': ['type', 'visibility'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---


### COMMUNITIES_SEARCH_SORT_BY_VERIFIED

Sort communities by 'verified' first.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L148) |

---


### COMMUNITIES_SERVICE_COMPONENTS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1063) |

```
[<class 'invenio_records_resources.services.records.components.metadata.MetadataComponent'>,
 <class 'invenio_communities.communities.services.components.CommunityThemeComponent'>,
 <class 'invenio_communities.communities.services.components.CustomFieldsComponent'>,
 <class 'invenio_communities.communities.services.components.PIDComponent'>,
 <class 'invenio_records_resources.services.records.components.relations.RelationsComponent'>,
 <class 'invenio_communities.communities.services.components.CommunityAccessComponent'>,
 <class 'invenio_communities.communities.services.components.OwnershipComponent'>,
 <class 'invenio_communities.communities.services.components.FeaturedCommunityComponent'>,
 <class 'invenio_communities.communities.services.components.OAISetComponent'>,
 <class 'invenio_communities.communities.services.components.CommunityDeletionComponent'>,
 <class 'invenio_communities.communities.services.components.ChildrenComponent'>,
 <class 'invenio_communities.communities.services.components.CommunityParentComponent'>,
 <class 'oarepo_checks.services.components.register_check_config.RegisterCheckComponent'>]
```

---


### COMMUNITIES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L67) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']},
 'version': {'title': l'Version', 'fields': ['-versions.index']},
 'updated-desc': {'title': l'Recently updated', 'fields': ['-updated']},
 'updated-asc': {'title': l'Least recently updated', 'fields': ['updated']},
 'newestactivity': {'title': l'Newest activity', 'fields': ['-last_activity_at']},
 'oldestactivity': {'title': l'Oldest activity', 'fields': ['last_activity_at']}}
```

---


### COMMUNITIES_SUBCOMMUNITIES_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L64) |

```
{'type': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
          'ui': {'field': 'type'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                'ui': {'field': 'visibility'}}}
```

---


### COMMUNITIES_SUBCOMMUNITIES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L151) |

```
{'facets': ['type'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---


### COMMUNITIES_SUB_INVITATION_REQUEST_CLS

RDM specific request type for subcommunity invitations.

| **Invenio RDM Default Value** | `RDMSubCommunityInvitationRequest` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1068) |

---


### COMMUNITIES_SUB_REQUEST_CLS

RDM specific request type for subcommunities.

| **OARepo Default Value** | `RDMSubCommunityRequest` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1065); [oarepo-communities](https://github.com/oarepo/oarepo-communities/blob/master/oarepo_communities/initial_config.py#L20) |

---


### CORS_EXPOSE_HEADERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L33) |

```
[
    'ETag',
    'Link',
    'X-RateLimit-Limit',
    'X-RateLimit-Remaining',
    'X-RateLimit-Reset',
    'Content-Type',
]
```

---


### CORS_RESOURCES

Dictionary for configuring CORS for endpoints.

   See Flask-CORS for further details.

.. note:: Overwrites
   `Flask-CORS
   <https://flask-cors.readthedocs.io/en/latest/api.html#flask_cors.CORS>`_
   configuration.

| **Invenio RDM Default Value** | `'*'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L13) |

---


### CORS_SEND_WILDCARD

Sending wildcard CORS header.

.. note:: Overwrites
   `Flask-CORS
   <https://flask-cors.readthedocs.io/en/latest/api.html#flask_cors.CORS>`_
   configuration.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L24) |

---


### **\*COVER_TEMPLATE**

Cover page template normally used e.g. for login and sign up pages.

| **Invenio RDM Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L33); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L269) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### CROSSREF_ADDITIONAL_PREFIXES

List of additional Crossref DOI prefixes supported for registration.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L724) |

```
[]
```

---


### CROSSREF_DEPOSITOR

Crossref depositor name.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L727) |

---


### CROSSREF_EMAIL

Crossref depositor email.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L730) |

---


### CROSSREF_ENABLED

Flag to enable/disable Crossref DOI registration.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L712) |

---


### CROSSREF_FORMAT

A string used for formatting the DOI or a callable.

If set to a string, you can used ``{prefix}`` and ``{id}`` inside the string.

You can also provide a callable instead:

.. code-block:: python

    def make_doi(prefix, record):
        return f"{prefix}/{record.pid.pid_value}"

    CROSSREF_FORMAT = make_doi

| **Invenio RDM Default Value** | `'{prefix}/{id}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L739) |

---


### CROSSREF_PASSWORD

Crossref password.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L718) |

---


### CROSSREF_PREFIX

Crossref DOI prefix.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L721) |

---


### CROSSREF_REGISTRANT

Crossref registrant.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L733) |

---


### CROSSREF_TEST_MODE

Crossref test mode enabled.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L736) |

---


### CROSSREF_URL
| **OARepo Default Value** | `'https://api.crossref.org/works/doi'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L12) |

---


### CROSSREF_USERNAME

Crossref username.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L715) |

---


### **\*CSP**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### CSRF_ALLOWED_CHARS
| **Default Value** | `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### CSRF_COOKIE_NAME
| **Default Value** | `'csrftoken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### CSRF_COOKIE_SAMESITE
| **Default Value** | `'Lax'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### CSRF_FORCE_SECURE_REFERER
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### CSRF_HEADER
| **Default Value** | `'X-CSRFToken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### CSRF_METHODS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['POST', 'PUT', 'PATCH', 'DELETE']
```

---


### CSRF_SECRET_SALT
| **Default Value** | `'invenio-csrf-token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### CSRF_TOKEN_EXPIRES_IN
| **Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### CSRF_TOKEN_GRACE_PERIOD
| **Default Value** | `604800` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### CSRF_TOKEN_LENGTH
| **Default Value** | `32` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### **\*DASHBOARD_RECORD_CREATE_URL**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui), [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### DATACITE_ADDITIONAL_PREFIXES

List of additional DataCite DOI prefixes supported for registration.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L682) |

```
[]
```

---


### DATACITE_DATACENTER_SYMBOL

DataCite data center symbol.

This is only required if you want your records to be harvestable (OAI-PMH)
in DataCite XML format.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L703) |

---


### DATACITE_ENABLED

Flag to enable/disable DataCite DOI registration.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L670) |

---


### DATACITE_FORMAT

A string used for formatting the DOI or a callable.

If set to a string, you can used ``{prefix}`` and ``{id}`` inside the string.

You can also provide a callable instead:

.. code-block:: python

    def make_doi(prefix, record):
        return f"{prefix}/{record.pid.pid_value}"

    DATACITE_FORMAT = make_doi

| **Invenio RDM Default Value** | `'{prefix}/{id}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L688) |

---


### DATACITE_PASSWORD

DataCite password.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L676) |

---


### DATACITE_PREFIX

DataCite DOI prefix.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L679) |

---


### **\*DATACITE_TEST_MODE**

DataCite test mode enabled.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L685) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### DATACITE_URL
| **OARepo Default Value** | `'https://api.datacite.org/dois'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L10) |

---


### DATACITE_USERNAME

DataCite username.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L673) |

---


### DB_VERSIONING
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### DB_VERSIONING_USER_MODEL
| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L593) |

---


### DEBUG
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### DEBUG_TB_INTERCEPT_REDIRECTS

Switches off incept of redirects by Flask-DebugToolbar.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L708) |

---


### DEFAULT_COMMUNITIES_CUSTOM_FIELDS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[<oarepo_communities.services.custom_fields.workflow.WorkflowCF object>,
 <oarepo_communities.services.custom_fields.workflow.WorkflowCF object>]
```

---


### DEFAULT_COMMUNITIES_CUSTOM_FIELDS_UI
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[{'section': l'Workflows',
  'fields': [{'field': 'workflow',
              'ui_widget': 'Dropdown',
              'props': {'label': l'Default workflow',
                        'description': l'Default workflow for the community if workflow is not specified when depositing a record.',
                        'options': []}},
             {'field': 'allowed_workflows',
              'ui_widget': 'Dropdown',
              'props': {'label': l'Allowed workflows',
                        'multiple': True,
                        'description': l'Workflows allowed for the community.',
                        'options': []}}]}]
```

---


### DEFAULT_WORKFLOW_EVENTS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'C': WorkflowEvent(submitters=[<invenio_records_permissions.generators.IfConfig object>]),
 'L': WorkflowEvent(submitters=[<invenio_records_permissions.generators.IfConfig object>])}
```

---


### **\*DEPLOYMENT_VERSION**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### DISPLAY_NEW_COMMUNITIES
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### DISPLAY_USER_COMMUNITIES
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### DOI_SETTINGS_FACETS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L68) |

```
{'community_slug': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                    'ui': {'field': 'community_slug'}},
 'prefix': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'prefix'}}}
```

---


### DOI_SETTINGS_SEARCH
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L61) |

```
{'facets': ['community_slug', 'prefix'],
 'sort': ['newest'],
 'sort_default': 'newest',
 'sort_default_no_query': 'newest'}
```

---


### DOI_SETTINGS_SORT_OPTIONS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L82) |

```
{'newest': {'title': l'Newest', 'fields': ['-created']}}
```

---


### **\*EINFRA**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/einfra.py#L28) |
| **Set by** | [`configure_einfra_oidc`](reference/index.md#oarepo_config.configure_einfra_oidc) |

---


### EINFRA_CAPABILITIES_ATTRIBUTE_NAME

Attribute name for resource capabilities in the PERUN dump.

| **OARepo Default Value** | `'urn:perun:resource:attribute-def:def:capabilities'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L55) |

---


### **\*EINFRA_ENTITLEMENTS_PARSER**
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |
| **Set by** | [`configure_einfra_oidc`](reference/index.md#oarepo_config.configure_einfra_oidc) |

---


### EINFRA_ENTITLEMENT_NAMESPACES

URN prefix for capabilities that can represent community roles.

| **OARepo Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L13) |

```
{'geant'}
```

---


### EINFRA_ENTITLEMENT_PREFIX

Parts of the entitlement URN name that represent communities.

| **OARepo Default Value** | `'cesnet.cz'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L16) |

---


### EINFRA_LAST_DUMP_PATH

Path to the last dump file in the S3 bucket.

| **OARepo Default Value** | `'nrp_invenio_export.json'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L58) |

---


### **\*EINFRA_LOGIN_APP**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/einfra.py#L28) |
| **Set by** | [`configure_einfra_oidc`](reference/index.md#oarepo_config.configure_einfra_oidc) |

---


### EINFRA_RSA_KEY
| **OARepo Default Value** | `b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmho5h/lz6USUUazQaVT3\nPHlo...` |
|--------------|-----------|
| **Type** | bytes |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L19) |

---


### EINFRA_TOKEN_EXCHANGE_ISSUER

Issuer of the token exchange token.

| **OARepo Default Value** | `'https://login.e-infra.cz/oidc/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L61) |

---


### EINFRA_TOKEN_EXCHANGE_PUBLIC_KEY

Public key of the token exchange token's issuer.

If not set, EINFRA_RSA_KEY is used instead.

| **OARepo Default Value** | `b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmho5h/lz6USUUazQaVT3\nPHlo...` |
|--------------|-----------|
| **Type** | bytes |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L64) |

---


### EINFRA_USER_DISPLAY_NAME_ATTRIBUTE

Attribute on user inside perun that represents the display name of the user.

| **OARepo Default Value** | `'urn:perun:user:attribute-def:core:displayName'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L46) |

---


### EINFRA_USER_DUMP_S3_ACCESS_KEY

Access key for the S3 bucket where the user dump from PERUN is stored.

| **OARepo Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L31) |

---


### EINFRA_USER_DUMP_S3_BUCKET

Bucket where the user dump from PERUN is stored.

| **OARepo Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L40) |

---


### EINFRA_USER_DUMP_S3_ENDPOINT

Endpoint for the S3 bucket where the user dump from PERUN is stored.

| **OARepo Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L37) |

---


### EINFRA_USER_DUMP_S3_SECRET_KEY

Secret key for the S3 bucket where the user dump from PERUN is stored.

| **OARepo Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L34) |

---


### EINFRA_USER_ID_DUMP_ATTRIBUTE

Attribute on user inside perun that represents the E-INFRA ID of the user.

| **OARepo Default Value** | `'urn:perun:user:attribute-def:virt:login-namespace:einfraid-persistent'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L43) |

---


### EINFRA_USER_ORGANIZATION_ATTRIBUTE

Attribute on user inside perun that represents the organization of the user.

| **OARepo Default Value** | `'urn:perun:user:attribute-def:def:organization'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L49) |

---


### EINFRA_USER_PREFERRED_MAIL_ATTRIBUTE

Attribute on user inside perun that represents the preferred mail of the user.

| **OARepo Default Value** | `'urn:perun:user:attribute-def:def:preferredMail'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L52) |

---


### EXPLAIN_TEMPLATE_LOADING
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### FILES_REST_ALLOW_RANGE_REQUESTS

Enable support for HTTP Range Requests.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L131) |

---


### FILES_REST_CHECKSUM_VERIFICATION_URI_PREFIXES

URI prefixes of files their checksums should be verified

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L344) |

```
[]
```

---


### **\*FILES_REST_DEFAULT_MAX_FILE_SIZE**

Default maximum file size for a bucket in bytes. `None` if unlimited.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L43) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### **\*FILES_REST_DEFAULT_QUOTA_SIZE**

Default quota size for a bucket in bytes. `None` if unlimited.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L40) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### **\*FILES_REST_DEFAULT_STORAGE_CLASS**

Default storage class. Must be one of `FILES_REST_STORAGE_CLASS_LIST`.

| **Invenio RDM Default Value** | `'S'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L37); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L354) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### FILES_REST_FILE_TAGS_HEADER

Header for updating file tags.

| **Invenio RDM Default Value** | `'X-Invenio-File-Tags'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L124) |

---


### FILES_REST_FILE_URI_MAX_LEN

Maximum length of the FileInstance.uri field.

.. warning::
   Setting this variable to anything higher than 255 is only supported
   with PostgreSQL database.

| **Invenio RDM Default Value** | `255` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L66) |

---


### FILES_REST_MIN_FILE_SIZE

Minimum file size when uploading, in bytes (do not allow empty files).

| **Invenio RDM Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L46) |

---


### FILES_REST_MULTIPART_CHUNKSIZE_MAX

Maximum chunk size in bytes of multipart objects.

| **Invenio RDM Default Value** | `5368709120` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L112) |

---


### FILES_REST_MULTIPART_CHUNKSIZE_MIN

Minimum chunk size in bytes of multipart objects.

| **Invenio RDM Default Value** | `5242880` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L109) |

---


### FILES_REST_MULTIPART_EXPIRES

Time delta after which a multipart upload is considered expired.

| **Invenio RDM Default Value** | `datetime.timedelta(days=4)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L115) |

---


### FILES_REST_MULTIPART_MAX_PARTS

Maximum number of parts when uploading files with multipart uploads.

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L106) |

---


### FILES_REST_MULTIPART_PART_FACTORIES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L88) |

```
['invenio_files_rest.views:default_partfactory',
 'invenio_files_rest.views:ngfileupload_partfactory']
```

---


### FILES_REST_OBJECT_KEY_MAX_LEN

Maximum length of the ObjectVersion.key field.

.. warning::
   Setting this variable to anything higher than 255 is only supported
   with PostgreSQL database.

| **Invenio RDM Default Value** | `255` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L58) |

---


### FILES_REST_PERMISSION_FACTORY

Permission factory to control the files access from the REST interface.

| **Invenio RDM Default Value** | `'invenio_files_rest.permissions.permission_factory'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L55); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L341) |

---


### FILES_REST_SIZE_LIMITERS

Import path of file size limiters factory to control bucket size limits.

| **Invenio RDM Default Value** | `'invenio_files_rest.limiters.file_size_limiters'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L49) |

---


### **\*FILES_REST_STORAGE_CLASS_LIST**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L26); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L348) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'S': 'Standard', 'A': 'Archive'}
```

---


### **\*FILES_REST_STORAGE_FACTORY**

Import path of factory used to create a storage instance.

| **Invenio RDM Default Value** | `'invenio_files_rest.storage.pyfs_storage_factory'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L52) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### FILES_REST_STORAGE_PATH_DIMENSIONS

Number of directory levels created when generating the path of a file.

   For example, if split length set to 2 and dimension to 3, the final
   path will be `a2/ad/4k/c9-8j39-34jn/`.

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L81) |

---


### FILES_REST_STORAGE_PATH_SPLIT_LENGTH

Number of chars to use as folder name when generating the path of a file.

   For example, if split length set to 4 and dimension to 4, the final
   path will be `a2ad/4kc9/8j39-34jn/`.

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L74) |

---


### FILES_REST_TASK_WAIT_INTERVAL

Interval in seconds between sending a whitespace to not close connection.

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L118) |

---


### FILES_REST_TASK_WAIT_MAX_SECONDS

Maximum number of seconds to wait for a task to finish.

| **Invenio RDM Default Value** | `600` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L121) |

---


### FILES_REST_UPLOAD_FACTORIES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L94) |

```
['invenio_files_rest.views:stream_uploadfactory',
 'invenio_files_rest.views:ngfileupload_uploadfactory']
```

---


### FILES_REST_XSENDFILE_ENABLED

Use the X-Accel-Redirect header to stream the file through a reverse proxy(
    e.g NGINX).

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L127) |

---


### FILES_REST_XSENDFILE_RESPONSE_FUNC

Function for the creation of a file streaming redirect response.

| **Invenio RDM Default Value** | `create_file_streaming_redirect_response` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L134) |

---


### FORMATTER_BADGES_ALLOWED_TITLES

List of allowed titles in badges.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L359); [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L6) |

```
['DOI']
```

---


### FORMATTER_BADGES_ENABLE
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### FORMATTER_BADGES_MAX_CACHE_AGE

The maximum amount of time a badge will be considered fresh.

| **Invenio RDM Default Value** | `0` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L12) |

---


### FORMATTER_BADGES_TITLE_MAPPING

Mapping of titles.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L362); [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L9) |

```
{}
```

---


### HANDLE_URL
| **OARepo Default Value** | `'https://hdl.handle.net'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L11) |

---


### **\*HEADER_TEMPLATE**

Base header template to be extended on custom headers.

| **Invenio RDM Default Value** | `'invenio_theme/header.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L18) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### I18N_DEFAULT_REDIRECT_ENDPOINT

Endpoint to redirect if no next parameter is provided.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L36) |

---


### I18N_JS_DISTR_EXCEPTIONAL_PACKAGE_MAP

Exceptional package name mapper for JS/React localization distribution.

Webpack entrypoints are used to determine the asset path for distributing JS/React localizations.
Entrypoint names usually match the corresponding package name, but some differ.
This mapping is used to associate exceptional entrypoint names with their package names.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L48) |

```
{}
```

---


### **\*I18N_LANGUAGES**

List of tuples of available languages.

Example configuration with english and danish with english as default language:

.. code-block:: python

    from flask_babel import lazy_gettext as _
    BABEL_DEFAULT_LOCALE = 'en'
    I18N_LANGUAGES = (('da', _('Danish')),)

.. note:: You should not include ``BABEL_DEFAULT_LOCALE`` in this list.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L16) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
[]
```

---


### I18N_SESSION_KEY

Key to retrieve language identifier from the current session object.

| **Invenio RDM Default Value** | `'language'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L39) |

---


### I18N_SET_LANGUAGE_URL

URL prefix for set language view.

Set to ``None`` to prevent view from being installed.

| **Invenio RDM Default Value** | `'/lang'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L30) |

---


### I18N_TRANSIFEX_JS_RESOURCES_MAP

Mapping of transifex resource names to invenioRDM package names.

All resources/packages that should be translated with Transifex should be added here.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L56) |

```
{}
```

---


### I18N_TRANSLATIONS_PATHS

List of paths to load message catalogs from.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L13) |

```
[]
```

---


### I18N_USER_LANG_ATTR

Attribute name which contains language identifier on the User object.

It is used only when the login manager is installed and a user is
authenticated. Set to ``None`` to prevent selector from being used.

| **Invenio RDM Default Value** | `'prefered_language'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L42) |

---


### IIIF_API_DECORATOR_HANDLER
| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1140) |

---


### IIIF_API_INFO_RESPONSE_SKELETON
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'v1': {'@context': 'http://library.stanford.edu/iiif/image-api/1.1/context.json',
        '@id': '',
        'width': '',
        'height': '',
        'profile': 'http://library.stanford.edu/iiif/image-api/compliance.html#level1',
        'tile_width': 256,
        'tile_height': 256,
        'scale_factors': [1, 2, 4, 8, 16, 32, 64]},
 'v2': {'@context': 'http://iiif.io/api/image/2/context.json',
        '@id': '',
        'protocol': 'http://iiif.io/api/image',
        'width': '',
        'height': '',
        'tiles': [{'width': 256, 'scaleFactors': [1, 2, 4, 8, 16, 32, 64]}],
        'profile': ['http://iiif.io/api/image/2/level2.json']}}
```

---


### IIIF_CACHE_HANDLER
| **Default Value** | `'flask_iiif.cache.simple:ImageSimpleCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### IIIF_CACHE_IGNORE_ERRORS
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### IIIF_CACHE_REDIS_URL
| **Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### IIIF_CACHE_TIME
| **Default Value** | `172800` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### IIIF_CONVERTERS
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('', 'L', 'L', '1', '', '')
```

---


### IIIF_FORMATS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1148) |

```
{'gif': 'image/gif',
 'jp2': 'image/jp2',
 'jpeg': 'image/jpeg',
 'jpg': 'image/jpeg',
 'pdf': 'application/pdf',
 'png': 'image/png',
 'tif': 'image/tiff',
 'tiff': 'image/tiff',
 'webp': 'image/webp'}
```

---


### IIIF_FORMATS_PIL_MAP
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1160) |

```
{'gif': 'gif',
 'jp2': 'jpeg2000',
 'jpeg': 'jpeg',
 'jpg': 'jpeg',
 'pdf': 'pdf',
 'png': 'png',
 'tif': 'tiff',
 'tiff': 'tiff',
 'webp': 'webp'}
```

---


### IIIF_GIF_TEMP_FOLDER_PATH
| **Default Value** | `'/tmp'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### IIIF_MODE
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'1': ['default', 'bitonal'],
 'L': ['default', 'gray', 'grey', 'bitonal'],
 'P': ['default', 'gray', 'grey', 'bitonal'],
 'RGB': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'RGBA': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'CMYK': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'YCbCr': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'I': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'F': ['default', 'color', 'gray', 'grey', 'bitonal']}
```

---


### IIIF_PREVIEW_TEMPLATE

Template for IIIF image preview.

| **Invenio RDM Default Value** | `'invenio_app_rdm/records/iiif_preview.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1137) |

---


### IIIF_QUALITIES
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('default', 'gray', 'grey', 'bitonal', 'color', 'native')
```

---


### IIIF_SIMPLE_PREVIEWER_NATIVE_EXTENSIONS

Images are converted to JPEG for preview, unless listed here.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1142) |

```
['gif', 'png']
```

---


### IIIF_SIMPLE_PREVIEWER_SIZE

Size of image in IIIF preview window. Must be a valid IIIF Image API size parameter.

| **Invenio RDM Default Value** | `'!800,800'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1145) |

---


### IIIF_TILES_CONVERTER_PARAMS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L939) |

```
{'compression': 'jpeg', 'Q': 90, 'tile_width': 256, 'tile_height': 256}
```

---


### IIIF_TILES_GENERATION_ENABLED

Enable generating pyramidal TIFF tiles for uploaded images.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L918) |

---


### IIIF_TILES_STORAGE_BASE_PATH

Base path for storing IIIF tiles.

Relative paths are resolved against the application instance path.

| **Invenio RDM Default Value** | `'images/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L933) |

---


### IIIF_TILES_VALID_EXTENSIONS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L921) |

```
['jp2', 'jpeg', 'jpg', 'pdf', 'png', 'png', 'tif', 'tiff']
```

---


### IIIF_VALIDATIONS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'v1': {'region': {'ignore': 'full',
                   'validate': '(^full|(pct:)?([\\d.]+,){3}([\\d.]+))'},
        'size': {'ignore': 'full',
                 'validate': '(^full|[\\d.]+,|,[\\d.]+|pct:[\\d.]+|[\\d.]+,[\\d.]+|![\\d.]+,[\\d.]+)'},
        'rotation': {'ignore': '0', 'validate': '^[\\d.]+$'},
        'quality': {'ignore': 'default', 'validate': '(native|color|gr[ae]y|bitonal)'},
        'image_format': {'ignore': '',
                         'validate': '(gif|jp2|jpe?g|pdf|png|tiff?|webp)'}},
 'v2': {'region': {'ignore': 'full',
                   'validate': '(^full|(pct:)?([\\d.]+,){3}([\\d.]+))'},
        'size': {'ignore': 'full',
                 'validate': '(^full|[\\d.]+,|,[\\d.]+|pct:[\\d.]+|[\\d.]+,[\\d.]+|![\\d.]+,[\\d.]+)'},
        'rotation': {'ignore': '0', 'validate': '^!?[\\d.]+$'},
        'quality': {'ignore': 'default', 'validate': '(default|color|gr[ae]y|bitonal)'},
        'image_format': {'ignore': '',
                         'validate': '(gif|jp2|jpe?g|pdf|png|tiff?|webp)'}}}
```

---


### INDEXER_BEFORE_INDEX_HOOKS

List of automatically connected hooks (function or importable string).

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L54) |

```
[]
```

---


### INDEXER_BULK_REQUEST_TIMEOUT

Request timeout to use in Bulk indexing.

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L41) |

---


### INDEXER_DEFAULT_INDEX

Default index to use if no schema is defined.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L8) |

---


### INDEXER_MAX_BULK_CONSUMERS

Maximum number of concurrent consumers for bulk indexing.

This threshold is applied per queue, so each indexing queue would
have a maximum of 5 consumers at the same time.

| **Invenio RDM Default Value** | `5` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L44) |

---


### INDEXER_MQ_EXCHANGE

Default exchange for message queue.

| **Invenio RDM Default Value** | `Exchange('indexer', type='direct')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L11) |

---


### INDEXER_MQ_PUBLISH_KWARGS

Default message queue producer publishing kwargs.

Passed to ``kombu.Producer:publish``.

.. code-block:: python

    INDEXER_MQ_PUBLISH_KWARGS = {
        "retry": True,
        "retry_policy": {         # Setting for maximum waiting time of ~10min:
            "interval_start": 0,  # First retry immediately,
            "interval_step": 2,   # then increase by 2s for every retry.
            "interval_max": 30,   # but don't exceed 30s between retries.
            "max_retries": 30,    # give up after 30 tries.
        },
    }

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L20) |

```
{}
```

---


### INDEXER_MQ_QUEUE

Default queue for message queue.

| **Invenio RDM Default Value** | `Queue('indexer', exchange=INDEXER_MQ_EXCHANGE, routing_key='indexer')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L14) |

---


### INDEXER_MQ_ROUTING_KEY

Default routing key for message queue.

| **Invenio RDM Default Value** | `'indexer'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L17) |

---


### INDEXER_RECORD_TO_INDEX

Provide an implementation of record_to_index function

| **Invenio RDM Default Value** | `'invenio_indexer.utils.default_record_to_index'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L51) |

---


### INDEXER_REPLACE_REFS

Whether to replace JSONRefs prior to indexing record.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L38) |

---


### INFO_ENDPOINT_COMPONENTS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['oarepo_rdm.info:RDMInfoComponent']
```

---


### **\*INSTANCE_THEME_FILE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*INVENIO_CACHE_TYPE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/generic_parameters.py#L42) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### INVENIO_COLLECTIONS_COMMUNITY_SLUG

Slug of the community that holds cross-repository ("global") collection trees.

Collections on this community search across every published record instead of
only records tagged with the holder community (the ``parent.communities.ids``
filter is skipped). The behavior is implemented by the collections records
service in oarepo-rdm. Set to ``None`` in deployment config to disable it.

| **OARepo Default Value** | `'global'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-communities](https://github.com/oarepo/oarepo-communities/blob/master/oarepo_communities/initial_config.py#L21) |

---


### INVENIO_COLLECTIONS_UI_URL_PREFIX

URL prefix mounted by the collections UI blueprint.

| **OARepo Default Value** | `'/collections'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-communities](https://github.com/oarepo/oarepo-communities/blob/master/oarepo_communities/initial_config.py#L30) |

---


### INVENIO_RDM_ENABLED
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### **\*INVENIO_VOCABULARY_TYPE_METADATA**
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |
| **Set by** | [`configure_vocabulary`](reference/index.md#oarepo_config.configure_vocabulary) |

```
{}
```

---


### **\*JAVASCRIPT_PACKAGES_MANAGER**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### JOBS_DEFAULT_QUEUE

Default Celery queue.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L49) |

---


### JOBS_FACETS

Facets/aggregations for Jobs results.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L28) |

```
{}
```

---


### JOBS_LOGGING

Enable logging for jobs.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L81) |

---


### JOBS_LOGGING_INDEX

"Index name for job logs.

| **Invenio RDM Default Value** | `'job-logs'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L84) |

---


### **\*JOBS_LOGGING_LEVEL**

Logging level for jobs.

| **Invenio RDM Default Value** | `'DEBUG'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L78) |
| **Set by** | [`configure_jobs`](reference/index.md#oarepo_config.configure_jobs) |

---


### JOBS_LOGGING_RETENTION_DAYS

Retention period for job logs in days.

| **Invenio RDM Default Value** | `90` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L87) |

---


### JOBS_LOGS_BATCH_SIZE

Number of log results to fetch per batch from the search backend.

| **Invenio RDM Default Value** | `500` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L93) |

---


### JOBS_LOGS_MAX_RESULTS

Maximum total number of log results to return in a single search request.

| **Invenio RDM Default Value** | `2000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L90) |

---


### JOBS_PERMISSION_POLICY

Permission policy for jobs.

| **Invenio RDM Default Value** | `JobPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L19) |

---


### JOBS_QUEUES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L31) |

```
{'celery': {'name': 'celery', 'title': l'Default', 'description': l'Default queue'},
 'low': {'name': 'low', 'title': l'Low', 'description': l'Low priority queue'}}
```

---


### JOBS_RUNS_PERMISSION_POLICY

Permission policy for job runs.

| **Invenio RDM Default Value** | `RunPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L22) |

---


### JOBS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L72) |

```
{'facets': [], 'sort': ['jobs', 'last_run_start_time', 'user', 'next_run']}
```

---


### JOBS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L52) |

```
{'jobs': {'title': l'Jobs', 'fields': ['jobs']},
 'last_run_start_time': {'title': l'Last run', 'fields': ['last_run_start_time']},
 'user': {'title': l'Started by', 'fields': ['user']},
 'next_run': {'title': l'Next run', 'fields': ['next_run']}}
```

---


### JOBS_TASKS_PERMISSION_POLICY

Permission policy for tasks.

| **Invenio RDM Default Value** | `TasksPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L16) |

---


### JSONSCHEMAS_ENDPOINT

Default schema endpoint.

| **Invenio RDM Default Value** | `'/schemas'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L9) |

---


### **\*JSONSCHEMAS_HOST**

Default json schema host.

| **Invenio RDM Default Value** | `'localhost'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L6); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L605) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### JSONSCHEMAS_LOADER_CLS

Loader class used in ``JSONRef`` when replacing ``$ref``.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L26) |

---


### JSONSCHEMAS_LOCAL_REFRESOLVER_URI_SCHEME

Non-standard URI scheme to reference local schemas.

| **Invenio RDM Default Value** | `'local://'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L65) |

---


### JSONSCHEMAS_REGISTER_ENDPOINTS_API

Register the endpoints on the API app.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L37); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L599) |

---


### JSONSCHEMAS_REGISTER_ENDPOINTS_UI

Register the endpoints on the UI app.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L40); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L602) |

---


### JSONSCHEMAS_REPLACE_REFS

Whether to resolve $ref before serving a schema.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L15) |

---


### JSONSCHEMAS_RESOLVER_CLS

Resolver used to resolve the schema.

if :py:const:`invenio_jsonschemas.config.JSONSCHEMAS_RESOLVE_SCHEMA` is
``True`` or there is ``?resolved=1`` parameter on the request the resolver
will run over the schema. This can be used for custom schemas resolver.

| **Invenio RDM Default Value** | `'invenio_jsonschemas.utils.resolve_schema'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L29) |

---


### JSONSCHEMAS_RESOLVE_SCHEMA

Whether to resolve schema using the Resolver Class.

If is ``True``, will replace $ref and run the
:py:const:`invenio_jsonschemas.config.JSONSCHEMAS_RESOLVER_CLS` class
before serving a schema.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L18) |

---


### JSONSCHEMAS_SCHEMAS

List of entrypoint names to register JSON Schemas for.

If `None`, all JSON Schemas defined through the ``invenio_jsonschemas.schemas``
entry point in setup.py will be registered.
If ``[]``, no JSON Schemas will be registered.

For example, if you only want to register `foo` and skip `bar` schemas:

.. code-block:: python

    # in your `setup.py` you would specify:
    entry_points={
        'invenio_jsonschemas.schemas': [
            'foo = invenio_foo.schemas',
            'bar = invenio_bar.schemas',
        ],
    }
    # and in your config.py
    JSONSCHEMAS_SCHEMAS = ['foo']

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L43) |

---


### JSONSCHEMAS_URL_SCHEME

Default url scheme for schemas.

| **Invenio RDM Default Value** | `'https'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L12) |

---


### LOGGING_CONSOLE

Enable logging to the console.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L27) |

---


### LOGGING_CONSOLE_LEVEL

Console logging level.

Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``,
``INFO``, ``DEBUG``, or ``NOTSET``.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L37) |

---


### LOGGING_CONSOLE_PYWARNINGS

Enable logging of Python warnings to the console.

By default, warnings are logged to the console if the application is in debug
mode, otherwise warnings are not logged.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L30) |

---


### LOGGING_FS_BACKUPCOUNT

Number of rotated log files to keep.

| **Invenio RDM Default Value** | `5` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L54) |

---


### LOGGING_FS_LEVEL

Filesystem logging level.

Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``,
``INFO``, ``DEBUG``, or ``NOTSET``.

| **Invenio RDM Default Value** | `'WARNING'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L60) |

---


### LOGGING_FS_LOGFILE

Enable logging to the filesystem.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L48) |

---


### LOGGING_FS_MAXBYTES

Maximum size of logging file. Default: 100MB.

| **Invenio RDM Default Value** | `104857600` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L57) |

---


### LOGGING_FS_PYWARNINGS

Enable logging of Python warnings to filesystem logging.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L51) |

---


### LOGGING_SENTRY_CELERY

Configure Celery to send logging to Sentry.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L81) |

---


### LOGGING_SENTRY_CLASS

Import path of sentry Flask extension class.

This allows you to customize the Sentry extension class.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L90) |

---


### LOGGING_SENTRY_INIT_KWARGS

Pass extra options when initializing Sentry instance.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L95) |

---


### LOGGING_SENTRY_LEVEL

Sentry logging level.

Defaults to only reporting errors and warnings.

| **Invenio RDM Default Value** | `'WARNING'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L72) |

---


### LOGGING_SENTRY_PYWARNINGS

Enable logging of Python warnings to Sentry.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L78) |

---


### LOGGING_SENTRY_REDIS

Configure REDIS to send logging to Sentry.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L87) |

---


### LOGGING_SENTRY_SQLALCHEMY

Configure SQL Alchemy to send logging to Sentry.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L84) |

---


### MAIL_DEBUG
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### MAIL_DEFAULT_REPLY_TO

Reply to mail address for e-mails.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L14) |

---


### **\*MAIL_DEFAULT_SENDER**

Email address used as sender of account registration emails.

`SECURITY_EMAIL_SENDER` will default to this value.

| **Invenio RDM Default Value** | `'info@inveniosoftware.org'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L372) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### MAIL_MAX_ATTACHMENT_SIZE

Max size of inline attachments, in bytes.

| **Invenio RDM Default Value** | `1000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L17) |

---


### MAIL_MAX_RETRIES

How often will we repeat if a problem occurred.

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L20) |

---


### MAIL_MIN_LOGGING_LEVEL

Minimum logging level for the mail logger.

| **Invenio RDM Default Value** | `40` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L23) |

---


### **\*MAIL_SUPPRESS_SEND**

Disable email sending by default.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L369) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*MATOMO_ANALYTICS_SITE_ID**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*MATOMO_ANALYTICS_TEMPLATE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*MATOMO_ANALYTICS_URL**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### MAX_CONTENT_LENGTH

Maximum allowed content length for form data.

This value limits the maximum file upload size via multipart-formdata and is
a Flask configuration variable that by default is unlimited.  The value must
be larger than the maximum part size you want to accept via
application/multipart-formdata (used by e.g. ng-file upload). This value only
limits file upload size via application/multipart-formdata and in particular
does not restrict the maximum file size possible when streaming a file in the
body of a PUT request.

Flask, by default, saves any file bigger than 500kb to a temporary file on
disk, thus do not set this value to large or you may run out of disk space on
your nodes.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L10); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L210) |

---


### MAX_COOKIE_SIZE
| **Default Value** | `4093` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### MAX_FORM_MEMORY_SIZE
| **Default Value** | `500000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### MAX_FORM_PARTS
| **Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### MULTIPROFILER_BASE_TEMPLATE

Base template for the profiler page.

| **Invenio RDM Default Value** | `'flask_multiprofiler/index.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1616) |

---


### MULTIPROFILER_IGNORED_ENDPOINTS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1619) |

```
[
    'static',
    '_debug_toolbar.static',
    'profiler\\..+',
    'invenio_formatter_badges.badge',
]
```

---


### MULTIPROFILER_PERMISSION

Function to check for permissions to access the profiler.

| **Invenio RDM Default Value** | `administration_permission.can` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1627) |

---


### NOTIFICATIONS_BACKENDS

Notification backends.

.. code-block::python

    NOTIFICATIONS_BACKENDS = {
        "email": EmailBackend,
        "cern": CERNNotificationsBackend,
        "slack": SlackBackend,
    }

| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L22); [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L79); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1422) |

```
{'email': <invenio_notifications.backends.email.EmailNotificationBackend object>}
```

---


### NOTIFICATIONS_BUILDERS

Notification builders.

The notification builders need to be registered by their type as lookup key for the
notification manager to be able to look up the right notification builder to process
scheduled notifications.
This is because if run as background task, the notification manager will be running
in a Python interpreter different from the one in which the notification was
originally built.

.. code-block::python

    NOTIFICATIONS_BUILDERS = {
        "community_submission_create": CommunitySubmissionCreate,
        "community_submission_accept": CommunitySubmissionAccept,
        "community_submission_reject": CommunitySubmissionReject,
        "member_invitation_create": CommunityMemberInvitationCreate,
        "member_invitation_accept": CommunityMemberInvitationAccept,
        "member_invitation_reject": CommunityMemberInvitationReject,
        "request_comment_create": RequestCommentCreate,
    }

| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L34); [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L59); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1428) |

```
{'guest-access-request-token.create': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestTokenCreateNotificationBuilder'>,
 'guest-access-request.accept': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestAcceptNotificationBuilder'>,
 'guest-access-request.submit': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestSubmitNotificationBuilder'>,
 'guest-access-request.submitted': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestSubmittedNotificationBuilder'>,
 'guest-access-request.cancel': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestCancelNotificationBuilder'>,
 'guest-access-request.decline': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestDeclineNotificationBuilder'>,
 'user-access-request.accept': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestAcceptNotificationBuilder'>,
 'user-access-request.submit': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestSubmitNotificationBuilder'>,
 'user-access-request.decline': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestDeclineNotificationBuilder'>,
 'user-access-request.cancel': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestCancelNotificationBuilder'>,
 'grant-user-access.create': <class 'invenio_rdm_records.notifications.builders.GrantUserAccessNotificationBuilder'>,
 'comment-request-event.create': <class 'oarepo_requests.notifications.builders.comment.CommentRequestEventCreateNotificationBuilder'>,
 'comment-request-event.reply': <class 'invenio_requests.notifications.builders.CommentRequestEventReplyNotificationBuilder'>,
 'comment-subcommunity-request.create': <class 'invenio_communities.notifications.builders.SubComReqCommentNotificationBuilder'>,
 'comment-subcommunity-invitation-request.create': <class 'invenio_communities.notifications.builders.SubComInvCommentNotificationBuilder'>,
 'community-submission.accept': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionAcceptNotificationBuilder'>,
 'community-submission.cancel': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionCancelNotificationBuilder'>,
 'community-submission.decline': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionDeclineNotificationBuilder'>,
 'community-submission.expire': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionExpireNotificationBuilder'>,
 'community-submission.submit': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionSubmittedNotificationBuilder'>,
 'community-invitation.accept': <class 'invenio_communities.notifications.builders.CommunityInvitationAcceptNotificationBuilder'>,
 'community-invitation.cancel': <class 'invenio_communities.notifications.builders.CommunityInvitationCancelNotificationBuilder'>,
 'community-invitation.decline': <class 'invenio_communities.notifications.builders.CommunityInvitationDeclineNotificationBuilder'>,
 'community-invitation.expire': <class 'invenio_communities.notifications.builders.CommunityInvitationExpireNotificationBuilder'>,
 'community-invitation.submit': <class 'invenio_communities.notifications.builders.CommunityInvitationSubmittedNotificationBuilder'>,
 'community-membership-request.accept': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestAcceptedNotificationBuilder'>,
 'community-membership-request.cancel': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestCancelledNotificationBuilder'>,
 'community-membership-request.decline': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestDeclinedNotificationBuilder'>,
 'community-membership-request.expire': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestExpiredNotificationBuilder'>,
 'community-membership-request.submit': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestSubmittedNotificationBuilder'>,
 'subcommunity-request.create': <class 'invenio_communities.notifications.builders.SubCommunityCreate'>,
 'subcommunity-request.accept': <class 'invenio_communities.notifications.builders.SubCommunityAccept'>,
 'subcommunity-request.decline': <class 'invenio_communities.notifications.builders.SubCommunityDecline'>,
 'subcommunity-invitation-request.create': <class 'invenio_communities.notifications.builders.SubComInvitationCreate'>,
 'subcommunity-invitation-request.accept': <class 'invenio_communities.notifications.builders.SubComInvitationAccept'>,
 'subcommunity-invitation-request.decline': <class 'invenio_communities.notifications.builders.SubComInvitationDecline'>,
 'subcommunity-invitation-request.expire': <class 'invenio_communities.notifications.builders.SubComInvitationExpire'>,
 'record-deletion.accept': <class 'invenio_rdm_records.notifications.builders.RecordDeletionAcceptNotificationBuilder'>,
 'record-deletion.decline': <class 'invenio_rdm_records.notifications.builders.RecordDeletionDeclineNotificationBuilder'>,
 'delete-published-record-request-event.submit': <class 'oarepo_requests.notifications.builders.delete_published_record.DeletePublishedRecordRequestSubmitNotificationBuilder'>,
 'delete-published-record-request-event.accept': <class 'oarepo_requests.notifications.builders.delete_published_record.DeletePublishedRecordRequestAcceptNotificationBuilder'>,
 'delete-published-record-request-event.decline': <class 'oarepo_requests.notifications.builders.delete_published_record.DeletePublishedRecordRequestDeclineNotificationBuilder'>,
 'publish-draft-request-event.submit': <class 'oarepo_requests.notifications.builders.publish.PublishDraftRequestSubmitNotificationBuilder'>,
 'publish-draft-request-event.accept': <class 'oarepo_requests.notifications.builders.publish.PublishDraftRequestAcceptNotificationBuilder'>,
 'publish-draft-request-event.decline': <class 'oarepo_requests.notifications.builders.publish.PublishDraftRequestDeclineNotificationBuilder'>,
 'publish-changed-metadata-request-event.submit': <class 'oarepo_requests.notifications.builders.publish.PublishChangedMetadataRequestSubmitNotificationBuilder'>,
 'publish-changed-metadata-request-event.accept': <class 'oarepo_requests.notifications.builders.publish.PublishChangedMetadataRequestAcceptNotificationBuilder'>,
 'publish-changed-metadata-request-event.decline': <class 'oarepo_requests.notifications.builders.publish.PublishChangedMetadataRequestDeclineNotificationBuilder'>,
 'publish-new-version-request-event.submit': <class 'oarepo_requests.notifications.builders.publish.PublishNewVersionRequestSubmitNotificationBuilder'>,
 'publish-new-version-request-event.accept': <class 'oarepo_requests.notifications.builders.publish.PublishNewVersionRequestAcceptNotificationBuilder'>,
 'publish-new-version-request-event.decline': <class 'oarepo_requests.notifications.builders.publish.PublishNewVersionRequestDeclineNotificationBuilder'>,
 'group-membership-request-event.submit': <class 'oarepo_requests.notifications.builders.group_membership.GroupMembershipRequestSubmitNotificationBuilder'>,
 'group-membership-request-event.accept': <class 'oarepo_requests.notifications.builders.group_membership.GroupMembershipRequestAcceptNotificationBuilder'>,
 'group-membership-request-event.decline': <class 'oarepo_requests.notifications.builders.group_membership.GroupMembershipRequestDeclineNotificationBuilder'>}
```

---


### NOTIFICATIONS_ENTITY_RESOLVERS

List of entity resolvers used by notification builders.

.. code-block::python

    NOTIFICATIONS_ENTITY_RESOLVERS = [
        UserResultItemResolver(),
        RDMRecordResultItemResolver(),
        CommunityResultItemResolver(),
        RequestResultItemResolver(),
        RequestEventResultItemResolver(),
    ]

| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L57); [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L83); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1481) |

```
[<invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object>,
 <invenio_rdm_records.requests.entity_resolvers.RDMRecordServiceResultResolver object>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object>,
 <invenio_rdm_records.requests.entity_resolvers.EmailResolver object>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object>,
 <oarepo_requests.notifications.resolvers.MultipleEntitiesNotificationResolver object>]
```

---


### NOTIFICATIONS_GROUP_EMAIL_DOMAIN

Domain suffix to append to group names when email is not provided.

When a recipient is a group and has no email or email_hidden field, the group's
name will be used as the email address with this domain appended.

Example:
    NOTIFICATIONS_GROUP_EMAIL_DOMAIN = "cern.ch"
    # Group "physics-team" becomes "physics-team@cern.ch"

Set to None to disable domain formatting (groups must have email field set).

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L78) |

---


### NOTIFICATIONS_MANAGER_CLS
| **Default Value** | `'oarepo_requests.notifications.manager.NotificationManager'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### NOTIFICATIONS_SETTINGS_VIEW_FUNCTION

View function for notification settings.

This should be set higher up in the module hierarchy (e.g. invenio-app-rdm), as
this module does not have knowledge of the settings view.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L71); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1492) |

---


### NOTIFICATION_RECIPIENTS_RESOLVERS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'community_role': <function <lambda>>,
 'community': <function <lambda>>,
 'user': <function <lambda>>,
 'group': <function <lambda>>,
 'multiple': <function <lambda>>,
 'action_need': <function <lambda>>}
```

---


### OAISERVER_ADMIN_EMAILS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L32) |

```
['info@inveniosoftware.org']
```

---


### OAISERVER_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAISERVER_CACHE_KEY

Key prefix added before all keys in cache server.

| **Invenio RDM Default Value** | `'DynamicOAISets::'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L157) |

---


### OAISERVER_CELERY_TASK_CHUNK_SIZE

Specify the maximum number of records each task will update.

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L160) |

---


### OAISERVER_COMPRESSIONS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L41) |

```
['identity']
```

---


### OAISERVER_CONTROL_NUMBER_FETCHER

PIDStore fetcher for the OAI ID control number.

| **Invenio RDM Default Value** | `'recid'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L163) |

---


### OAISERVER_CREATED_KEY

Record created key.

| **Invenio RDM Default Value** | `'created'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L684); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L127) |

---


### OAISERVER_DELETE_PERCOLATOR_FUNCTION
| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:_delete_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L108) |

---


### OAISERVER_DESCRIPTIONS

Specify the optional description containers that can be used to express
properties of the repository that are not covered by the standard response
to the Identify verb.
For further information see:
http://www.openarchives.org/OAI/2.0/guidelines.htm

The `eprints`, `oai_identifier` and `friends` description can be added using
the helper functions in utils.py as follows:

.. code-block:: python

    from invenio_oaiserver.utils import eprints_description
    from invenio_oaiserver.utils import friends_description
    from invenio_oaiserver.utils import oai_identifier_description

    OAISERVER_DESCRIPTIONS = [
        eprints_description(metadataPolicy, dataPolicy,
                            submissionPolicy, content),
        oai_identifier_description(scheme, repositoryIdentifier,
                                   delimiter, sampleIdentifier),
        friends_description(baseUrls)
    ]

The parameters of each description element are strings if their type is unique
or dictionaries, with the type being the key, if it can differ.
E.g. the dataPolicy of the eprints element can consist of a
text and or URL so it will have the form:

.. code-block:: python

    metadataPolicy = {'text': 'Metadata can be used by commercial'
                      'and non-commercial service providers',
                      'URL': 'http://arXiv.org/arXiv_metadata_use.htm'}

Whereas for the scheme of the oai_identifier it will just be:

.. code-block:: python

    scheme = 'oai'

If the parameter can take an arbitrary amount of elements it can be a list:

.. code-block:: python

    baseUrls = [http://oai.east.org/foo/,
                http://oai.hq.org/bar/,
                http://oai.south.org/repo.cgi]

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L166) |

```
[]
```

---


### OAISERVER_GETRECORD_FETCHER

Record data fetcher for serialization.

| **Invenio RDM Default Value** | `'invenio_rdm_records.oai:getrecord_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L699); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L148) |

---


### OAISERVER_GRANULARITY

The finest harvesting granularity supported by the repository.

The legitimate values are ``YYYY-MM-DD`` and ``YYYY-MM-DDThh:mm:ssZ``
with meanings as defined in ISO8601.

| **Invenio RDM Default Value** | `'YYYY-MM-DDThh:mm:ssZ'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L45) |

---


### OAISERVER_ID_FETCHER

OAI ID fetcher function.

| **Invenio RDM Default Value** | `'invenio_rdm_records.oai:oaiid_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L635); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L121) |

---


### **\*OAISERVER_ID_PREFIX**

The prefix that will be applied to the generated OAI-PMH ids.

| **Invenio RDM Default Value** | `'oai:eduroam-tlh22.cesnet.cz:'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L629); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L19) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### OAISERVER_LAST_UPDATE_KEY

Record update key.

| **Invenio RDM Default Value** | `'updated'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L681); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L124) |

---


### OAISERVER_METADATA_FORMATS
| **OARepo Default Value** | `<oarepo_rdm.oai.config.OAIServerMetadataFormats object>` |
|--------------|-----------|
| **Type** | OAIServerMetadataFormats |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L56); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L638); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L65) |

---


### OAISERVER_NEW_PERCOLATOR_FUNCTION
| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:_new_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L106) |

---


### OAISERVER_PAGE_SIZE

Define maximum length of list responses.

Request with verbs ``ListRecords``, ``ListIdentifiers``, and ``ListSets``
are affected by this option.

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L12) |

---


### OAISERVER_PERCOLATOR_DEDICATED_INDEX

Create a dedicated index for the percolators, instead of storing them in
the same index as the records.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L136) |

---


### OAISERVER_PROTOCOL_VERSION
| **Invenio RDM Default Value** | `'2.0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L30) |

---


### OAISERVER_QUERY_PARSER

Define query parser for OIASet definition.

| **Invenio RDM Default Value** | `invenio_search.engine.dsl.Q` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L151) |

---


### OAISERVER_QUERY_PARSER_FIELDS

Define query parser search fields list for OIASet definition.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L154) |

```
[]
```

---


### OAISERVER_RECORD_CLS

Record retrieval class.

| **Invenio RDM Default Value** | `'invenio_rdm_records.records.api:RDMRecord'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L687); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L145) |

---


### OAISERVER_RECORD_INDEX

Specify a search index with records that should be exposed via OAI-PMH.

| **Invenio RDM Default Value** | `'oaisource'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L693); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L26) |

---


### OAISERVER_RECORD_LIST_SETS_FETCHER

Record's list OAI sets function.

| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:sets_search_all'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L133) |

---


### OAISERVER_RECORD_SETS_FETCHER

Record's OAI sets function.

| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:find_sets_for_record'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L690); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L130) |

---


### OAISERVER_REGISTER_RECORD_SIGNALS

Catch record/set insert/update/delete signals and update the `_oai`
field.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L110) |

---


### OAISERVER_REGISTER_SET_SIGNALS

Catch set insert/update/delete signals and update the `_oai` record
field.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L114) |

---


### **\*OAISERVER_REPOSITORY_NAME**
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | unknown |
| **Set by** | [`configure_oai`](reference/index.md#oarepo_config.configure_oai) |

---


### OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME

The expiration time of a resumption token in seconds.

**Default: 60 seconds = 1 minute**.

.. note::

    Setting longer expiration time may have a negative impact on your
    search cluster as it might need to keep open cursors.

    https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L52) |

---


### OAISERVER_SEARCH_CLS

Class for record search.

| **Invenio RDM Default Value** | `'invenio_rdm_records.oai:OAIRecordSearch'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L632); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L118) |

---


### OAISERVER_SET_RECORDS_QUERY_FETCHER
| **Invenio RDM Default Value** | `'invenio_oaiserver.fetchers:set_records_query_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L141) |

---


### OAISERVER_XSL_URL

Specify the url (relative or absolute) to the XML Stylesheet file to
transform XML OAI 2.0 responses into XHTML.

The url can be a relative path to a local static file:

.. code-block:: python

    OAISERVER_XSL_URL = '/static/xsl/oai2.xsl'

or an absolute url to a remote file (be aware of CORS restrictions):

.. code-block:: python

    OAISERVER_XSL_URL = 'https//www.otherdomain.org/oai2.xsl'

You can obtain an already defined XSL Stylesheet for OAIS 2.0 on `EPrints
repository
<https://raw.githubusercontent.com/eprints/eprints/3.3/lib/static/oai2.xsl>`_
(GPLv3 licensed).

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L217) |

---


### **\*OAREPO_CHECKS_DEFAULT_CHAT_EINFRA_CLIENT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/llm.py#L13) |
| **Set by** | [`configure_llm`](reference/index.md#oarepo_config.configure_llm) |

---


### **\*OAREPO_CHECKS_DEFAULT_LLM_CLIENT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/llm.py#L13) |
| **Set by** | [`configure_llm`](reference/index.md#oarepo_config.configure_llm) |

---


### **\*OAREPO_CHECKS_LLM_CLIENTS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/llm.py#L13) |
| **Set by** | [`configure_llm`](reference/index.md#oarepo_config.configure_llm) |

---


### OAREPO_CHECKS_MAX_LLM_INPUT_CHARS
| **Default Value** | `2000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### OAREPO_CHECKS_MAX_LLM_OUTPUT_CHARS
| **Default Value** | `5000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### OAREPO_COMMUNITIES_DEFAULT_WORKFLOW
| **Default Value** | `'default'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAREPO_MODELS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'vocabularies': <oarepo_runtime.api.Model object>,
 'affiliations': <oarepo_runtime.api.Model object>,
 'funders': <oarepo_runtime.api.Model object>,
 'awards': <oarepo_runtime.api.Model object>,
 'names': <oarepo_runtime.api.Model object>,
 'subjects': <oarepo_runtime.api.Model object>}
```

---


### OAREPO_PERMISSIONS_PRESETS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'vocabularies': <class 'invenio_vocabularies.services.permissions.PermissionPolicy'>}
```

---


### OAREPO_REQUESTS_DEFAULT_RECEIVER
| **Default Value** | `'oarepo_requests.receiver.default_workflow_receiver_function'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAREPO_UI_JINJAX_FILTERS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-ui](https://github.com/oarepo/oarepo-ui/blob/master/oarepo_ui/config.py#L34) |

```
{'compact_number': 'invenio_app_rdm.records_ui.views.filters:compact_number',
 'localize_number': 'invenio_app_rdm.records_ui.views.filters:localize_number',
 'truncate_number': 'invenio_app_rdm.records_ui.views.filters:truncate_number',
 'as_dict': 'oarepo_ui.templating.filters:as_dict',
 'ui_value': 'oarepo_ui.templating.filters:ui_value',
 'localized': 'oarepo_ui.templating.filters:localized',
 'append_query_params': 'oarepo_ui.utils:append_query_params'}
```

---


### OAREPO_UI_JINJAX_GLOBALS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-ui](https://github.com/oarepo/oarepo-ui/blob/master/oarepo_ui/config.py#L44) |

```
{'ui_value': 'oarepo_ui.templating.filters:ui_value',
 'as_array': 'oarepo_ui.templating.filters:as_array',
 'value': 'oarepo_ui.templating.filters:value',
 'as_dict': 'oarepo_ui.templating.filters:as_dict',
 'localized': 'oarepo_ui.templating.filters:localized',
 'append_query_params': 'oarepo_ui.utils:append_query_params',
 'can_view_deposit_page': 'oarepo_ui.utils:can_view_deposit_page'}
```

---


### OAREPO_UI_LESS_COMPONENTS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['dl_table']
```

---


### OAREPO_UI_MULTILINGUAL_FIELD_LANGUAGES
| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [oarepo-ui](https://github.com/oarepo/oarepo-ui/blob/master/oarepo_ui/config.py#L90) |

```
[{'text': 'English', 'value': 'en'}, {'text': 'Czech', 'value': 'cs'}]
```

---


### OAREPO_UI_OVERRIDES
| **Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | unknown |

```
{UIComponentOverride(endpoint='invenio_app_rdm.index',
                     overridable_id='InvenioAppRDM.RecordsList.layout',
                     component=UIComponent(RecordsList <@js/oarepo_ui/search/RecordsList>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_communities.communities_detail',
                     overridable_id='InvenioCommunities.DetailsSearch.ResultsList.item',
                     component=UIComponent(DynamicResultsListItem <@js/oarepo_ui/search/DynamicResultsListItem>, UIComponentImportMode.DEFAULT import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_communities.communities_detail',
                     overridable_id='InvenioCommunities.DetailsSearch.SearchBar.element',
                     component=UIComponent(ClearableSearchbarElement <@js/oarepo_ui/search/ClearableSearchbarElement>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.uploads',
                     overridable_id='InvenioAppRdm.DashboardUploads.ResultsList.item',
                     component=UIComponent(DynamicResultsListItem <@js/oarepo_ui/search/DynamicResultsListItem>, UIComponentImportMode.DEFAULT import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_settings',
                     overridable_id='InvenioCommunities.CommunityProfileForm.GridRow.DangerZone',
                     component=UIComponent(Disabled <@js/oarepo_ui/components/Disabled>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_search_ui.search',
                     overridable_id='InvenioAppRdm.Search.ResultsList.item',
                     component=UIComponent(DynamicResultsListItem <@js/oarepo_ui/search/DynamicResultsListItem>, UIComponentImportMode.DEFAULT import)>)),
 UIComponentOverride(endpoint='invenio_search_ui.search',
                     overridable_id='InvenioAppRdm.Search.SearchBar.element',
                     component=UIComponent(ClearableSearchbarElement <@js/oarepo_ui/search/ClearableSearchbarElement>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='oarepo_communities_collections.collection_detail',
                     overridable_id='InvenioAppRdm.Search.ResultsList.item',
                     component=UIComponent(DynamicResultsListItem <@js/oarepo_ui/search/DynamicResultsListItem>, UIComponentImportMode.DEFAULT import)>)),
 UIComponentOverride(endpoint='oarepo_communities_collections.collection_detail',
                     overridable_id='InvenioAppRdm.Search.SearchBar.element',
                     component=UIComponent(ClearableSearchbarElement <@js/oarepo_ui/search/ClearableSearchbarElement>, UIComponentImportMode.NAMED import)>))}
```

---


### OAREPO_UI_RECORD_ACTIONS
| **OARepo Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [oarepo-ui](https://github.com/oarepo/oarepo-ui/blob/master/oarepo_ui/config.py#L55) |

```
{'create',
 'delete',
 'delete_draft',
 'draft_read_deleted_files',
 'draft_read_files',
 'draft_update_files',
 'edit',
 'manage',
 'manage_files',
 'manage_record_access',
 'media_read_files',
 'moderate',
 'new_version',
 'publish',
 'read',
 'read_deleted_files',
 'read_draft',
 'read_files',
 'review',
 'search',
 'update',
 'update_draft',
 'update_files',
 'view'}
```

---


### OAREPO_UI_RESULT_LIST_ITEM_REGISTRATION_CALLBACKS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[<function _register_main_search_result_item>,
 <function _register_home_page_search_result_item>,
 <function _register_collection_search_result_item>,
 <function _register_community_uploads_result_item>,
 <function _register_dashboard_uploads_result_item>]
```

---


### OAREPO_VOCABULARIES_PERMISSIONS_PRESETS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L22) |

```
{'vocabularies': <class 'invenio_vocabularies.services.permissions.PermissionPolicy'>}
```

---


### OAREPO_VOCABULARIES_SORT_CF
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[]
```

---


### OAREPO_VOCABULARIES_SUGGEST_CF
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[]
```

---


### OAREPO_VOCABULARIES_UI_RESOURCE
| **Default Value** | `'oarepo_vocabularies.ui.resources.resource:InvenioVocabulariesUIResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAREPO_VOCABULARIES_UI_RESOURCE_CONFIG
| **Default Value** | `'oarepo_vocabularies.ui.resources.config:InvenioVocabulariesUIResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAREPO_VOCABULARY_NAMESPACE_URI
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### OAREPO_VOCABULARY_TYPE_RESOURCE
| **OARepo Default Value** | `VocabularyTypeResource` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L35) |

---


### OAREPO_VOCABULARY_TYPE_RESOURCE_CONFIG
| **OARepo Default Value** | `VocabularyTypeResourceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L36) |

---


### OAREPO_VOCABULARY_TYPE_SERVICE
| **OARepo Default Value** | `VocabularyTypeService` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L32) |

---


### OAREPO_VOCABULARY_TYPE_SERVICE_CONFIG
| **OARepo Default Value** | `VocabularyTypeServiceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L33) |

---


### OAUTH2SERVER_ALLOWED_GRANT_TYPES
| **Invenio RDM Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L26) |

```
{'authorization_code', 'client_credentials', 'refresh_token'}
```

---


### OAUTH2SERVER_ALLOWED_RESPONSE_TYPES
| **Invenio RDM Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L39) |

```
{'code', 'token'}
```

---


### OAUTH2SERVER_ALLOWED_URLENCODE_CHARACTERS

A string of special characters that should be valid inside a query string.

.. seealso::

    See :py:func:`monkeypatch_oauthlib_urlencode_chars
    <invenio_oauth2server.ext.InvenioOAuth2ServerREST.monkeypatch_oauthlib_urlencode_chars>`
    for a full explanation.

| **Invenio RDM Default Value** | `'=&;:%+~,*@!()/?'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L51) |

---


### OAUTH2SERVER_AUTHORIZE_TEMPLATE

Template used for rendering the authorization request.

| **Invenio RDM Default Value** | `'invenio_oauth2server/authorize.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L14) |

---


### OAUTH2SERVER_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAUTH2SERVER_CLIENT_ID_SALT_LEN

Length of client id.

| **Invenio RDM Default Value** | `40` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L17) |

---


### OAUTH2SERVER_CLIENT_SECRET_SALT_LEN

Length of the client secret.

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L20) |

---


### OAUTH2SERVER_COVER_TEMPLATE
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAUTH2SERVER_JWT_AUTH_HEADER

Header for the JWT.

.. note::

    Authorization: Bearer xxx

| **Invenio RDM Default Value** | `'Authorization'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L61) |

---


### OAUTH2SERVER_JWT_AUTH_HEADER_TYPE

Header Authorization type.

.. note::

    By default the authorization type is ``Bearer`` as recommented by
    `JWT  <https://jwt.io>`_

| **Invenio RDM Default Value** | `'Bearer'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L69) |

---


### OAUTH2SERVER_JWT_VERIFICATION_FACTORY

Import path of factory used to verify JWT.

The ``request.headers`` should be passed as parameter.

| **Invenio RDM Default Value** | `'invenio_oauth2server.utils:jwt_verify_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L78) |

---


### OAUTH2SERVER_SETTINGS_TEMPLATE
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAUTH2SERVER_TOKEN_PERSONAL_SALT_LEN

Length of the personal access token.

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L23) |

---


### OAUTH2_CACHE_REDIS_HOST
| **Default Value** | `<redis.client.Redis(<redis.connection.ConnectionPool(<redis.connection.Connection(host=localhost,por...` |
|--------------|-----------|
| **Type** | Redis |
| **Source** | unknown |

---


### OAUTH2_CACHE_TYPE

Type of cache to use for storing the temporary grant token.

| **Invenio RDM Default Value** | `'redis'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L8) |

---


### OAUTH2_PROVIDER_ERROR_ENDPOINT

Error view endpoint.

| **Invenio RDM Default Value** | `'invenio_oauth2server.errors'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L11) |

---


### **\*OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN**

Redirect to the only external login service under specific conditions.

If this option is enabled and there is exactly one external authentication
service enabled (i.e. one OAuthClient remote app is configured, and local
login is disabled), the login view function will automatically redirect to
that external authentication service.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L347) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### OAUTHCLIENT_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAUTHCLIENT_COVER_TEMPLATE
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAUTHCLIENT_LOGIN_USER_TEMPLATE_PARENT
| **Default Value** | `'invenio_accounts/login_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### **\*OAUTHCLIENT_REMOTE_APPS**

Configuration of remote applications.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L320) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters), [`configure_einfra_oidc`](reference/index.md#oarepo_config.configure_einfra_oidc) |

```
{}
```

---


### OAUTHCLIENT_REST_DEFAULT_ERROR_REDIRECT_URL

Configuration of default error redirect URL.

| **Invenio RDM Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L341) |

---


### OAUTHCLIENT_REST_DEFAULT_RESPONSE_HANDLER

Default REST response handler.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L344) |

---


### OAUTHCLIENT_REST_REMOTE_APPS

Configuration of remote rest applications.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L338) |

```
{}
```

---


### OAUTHCLIENT_SESSION_KEY_PREFIX

Session key prefix used when storing the access token for a remote app.

| **Invenio RDM Default Value** | `'oauth_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L323) |

---


### OAUTHCLIENT_SETTINGS_TEMPLATE
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### OAUTHCLIENT_SIGNUP_FORM

Function called to render the sign up form after authorization succeeded.

| **Invenio RDM Default Value** | `_create_registrationform` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L332) |

---


### OAUTHCLIENT_SIGNUP_TEMPLATE

Template for the signup page.

| **Invenio RDM Default Value** | `'invenio_oauthclient/signup.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L335) |

---


### OAUTHCLIENT_SITENAME
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | unknown |

---


### OAUTHCLIENT_STATE_ENABLED

Internal variable used to disable state validation during tests.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L329) |

---


### OAUTHCLIENT_STATE_EXPIRES

Number of seconds after which the state token expires.

| **Invenio RDM Default Value** | `300` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L326) |

---


### OAUTHCLIENT_TOKEN_EXPIRES_LEEWAY

The number of seconds before the actual expiration of an access token from which it is considered expired.

This ensures that it won't cause issues if some time passes between the check for whether the token is expired and any requests that the token is then used in.

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L356) |

---


### ORCID_PUBLIC_DUMP_S3_BUCKET_NAME
| **OARepo Default Value** | `'v3.0-summaries'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L14) |

---


### PAGES_ALLOWED_EXTRA_HTML_ATTRS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L56) |

```
{'img': ['src', 'alt', 'title', 'width', 'height', 'loading'],
 'button': ['type', 'name', 'value', 'disabled', 'onclick']}
```

---


### PAGES_ALLOWED_EXTRA_HTML_TAGS

Extend allowed HTML tags list for static pages content.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L53) |

```
['img', 'button']
```

---


### PAGES_BASE_TEMPLATE
| **Default Value** | `'invenio_pages/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### PAGES_DEFAULT_TEMPLATE

Default template to render.

| **Invenio RDM Default Value** | `'invenio_pages/default.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1219); [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L9) |

---


### PAGES_FACETS

Available facets defined for this module.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L49) |

```
{}
```

---


### PAGES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L23) |

```
{'facets': [], 'sort': ['url', 'title', 'created', 'updated']}
```

---


### PAGES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L29) |

```
{'url': {'title': l'URL', 'fields': ['url']},
 'title': {'title': l'Title', 'fields': ['title']},
 'created': {'title': l'Created', 'fields': ['created']},
 'updated': {'title': l'Updated', 'fields': ['updated']}}
```

---


### PAGES_TEMPLATES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1222); [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L12) |

```
[('invenio_pages/default.html', 'Default'),
 ('invenio_pages/dynamic.html', 'Default dynamic')]
```

---


### PAGES_WHITELIST_CONFIG_KEYS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L18) |

```
['THEME_SITENAME']
```

---


### PERMANENT_SESSION_LIFETIME
| **Default Value** | `datetime.timedelta(days=31)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | unknown |

---


### PIDSTORE_APP_LOGGER_HANDLERS
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### PIDSTORE_DATACITE_DOI_PREFIX

Provide a DOI prefix here.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L14) |

---


### PIDSTORE_OBJECT_ENDPOINTS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'rec': 'recordmetadata.details_view'}
```

---


### PIDSTORE_RECID_FIELD

Default record id field inside the json data.

This name will be used by the fetcher, to retrieve the record ID value from the
JSON, and by the minter, to store it inside the JSON.

| **Invenio RDM Default Value** | `'control_number'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L6) |

---


### PIDSTORE_RECORDID_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L17) |

```
{'length': 10, 'split_every': 5, 'checksum': True}
```

---


### PREFERRED_URL_SCHEME
| **Default Value** | `'http'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### PREVIEWABLE_ZIP_PREVIEWER_NATIVE_EXTENSIONS

Extensions for previewable zip.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1172) |

```
['zip']
```

---


### PREVIEWER_ABSTRACT_TEMPLATE

Parent template used by the available previewers.

| **Invenio RDM Default Value** | `'invenio_previewer/abstract_previewer.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L67); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1195) |

---


### PREVIEWER_BASE_CSS_BUNDLES

Basic bundle which includes Font-Awesome/Bootstrap.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L70) |

```
['previewer_theme.css']
```

---


### PREVIEWER_BASE_JS_BUNDLES

Basic bundle which includes Bootstrap/jQuery.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L73) |

```
['previewer_theme.js']
```

---


### PREVIEWER_BASE_TEMPLATE
| **Default Value** | `'invenio_previewer/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### PREVIEWER_CHARDET_BYTES

Number of bytes to read for character encoding detection by `cchardet`.

| **Invenio RDM Default Value** | `1024` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L12) |

---


### PREVIEWER_CHARDET_CONFIDENCE

Confidence threshold for character encoding detection by `cchardet`.

| **Invenio RDM Default Value** | `0.9` |
|--------------|-----------|
| **Type** | float |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L15) |

---


### PREVIEWER_CONTAINER_ITEM_PREFERENCE
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1198) |

```
['csv_papaparsejs',
 'pdfjs',
 'simple_image',
 'json_prismjs',
 'xml_prismjs',
 'mistune',
 'video_videojs',
 'audio_videojs',
 'ipynb',
 'zip',
 'txt']
```

---


### PREVIEWER_CSV_MAX_BYTES

Maximum file size in bytes for CSV files.

| **Invenio RDM Default Value** | `104857600` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L27) |

---


### PREVIEWER_CSV_SNIFFER_ALLOWED_DELIMITERS

Allowed delimiter characters passed to the ``csv.Sniffer.sniff`` method.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L9) |

---


### PREVIEWER_CSV_VALIDATION_BYTES

Number of bytes read by CSV previewer to validate the file.

| **Invenio RDM Default Value** | `1024` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L6) |

---


### PREVIEWER_MAX_FILE_SIZE_BYTES

Maximum file size in bytes for JSON/XML files.

| **Invenio RDM Default Value** | `1048576` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L18) |

---


### PREVIEWER_MAX_IMAGE_SIZE_BYTES

Maximum file size in bytes for image files.

| **Invenio RDM Default Value** | `524288.0` |
|--------------|-----------|
| **Type** | float |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L21) |

---


### PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS

Additional DocumentInitParameters passed to pdfjsLib.getDocument().

See https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib.html for the full
list of available options.

Example (disable range requests, streaming, and auto-fetching)::

    PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS = {
        "disableStream": True,
        "disableRange": True,
        "disableAutoFetch": True,
    }

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L36) |

---


### PREVIEWER_PDF_JS_ENABLE_SCRIPTING

Enable JavaScript execution in PDF files (disabled by default for security).

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L33) |

---


### PREVIEWER_PREFERENCE
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L51); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1179) |

```
['csv_papaparsejs',
 'pdfjs',
 'iiif_simple',
 'simple_image',
 'json_prismjs',
 'xml_prismjs',
 'mistune',
 'video_videojs',
 'audio_videojs',
 'ipynb',
 'previewable_zip',
 'txt']
```

---


### PREVIEWER_RECORD_FILE_FACOTRY

Factory for extracting files from records.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L76) |

---


### PREVIEWER_TXT_MAX_BYTES

Maximum number of .txt file bytes to preview before truncated.

| **Invenio RDM Default Value** | `1048576` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L24) |

---


### PREVIEWER_WEB_ARCHIVE_RANGE_REQUESTS

Whether the file server supports range requests or not.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L79) |

---


### PREVIEWER_ZIP_MAX_FILES

Max number of files showed in the ZIP previewer.

| **Invenio RDM Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L30) |

---


### PROPAGATE_EXCEPTIONS
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### PROVIDE_AUTOMATIC_OPTIONS
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### PUBLISH_REQUEST_TYPES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['publish_draft', 'publish_new_version']
```

---


### QUEUES_BROKER_URL

Broker URL for queues.

If the variable is not configured it falls back to the default ``BROKER_URL``
of our application. For more information about how to define your broker here:
https://kombu.readthedocs.io/en/latest/reference/kombu.connection.html#connection

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L8) |

---


### QUEUES_CONNECTION_POOL

Default queues connection pool.

| **Invenio RDM Default Value** | `get_connection_pool` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L16) |

---


### QUEUES_DEFINITIONS

Static queue definitions.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L19) |

```
[]
```

---


### RATELIMIT_APPLICATION

Global rate limit.

| **Invenio RDM Default Value** | `set_rate_limit` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L19) |

---


### **\*RATELIMIT_AUTHENTICATED_USER**

Rate limit for logged in users.

| **Invenio RDM Default Value** | `'5000 per hour;100 per minute'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L86); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L235) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### RATELIMIT_ENABLED
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### **\*RATELIMIT_GUEST_USER**

Rate limit for non logged in users.

| **Invenio RDM Default Value** | `'1000 per hour;60 per minute'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L89); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L237) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### RATELIMIT_HEADERS_ENABLED

Enable rate limit headers. (Default: ``True``)

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L32) |

---


### RATELIMIT_KEY_FUNC

Define custom key function.

This config is not part of Flask-Limiter.

This function is used to generate a unique key for each visitor to track
the number of performed requests. If not defined, the default ``key_func``
will be used, which will create the key by concatenating the user agent and
the IP address of the user.

For more information you can also see `here
<https://flask-limiter.readthedocs.io/en/stable/#rate-limit-domain>`_

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L49) |

---


### RATELIMIT_PER_ENDPOINT
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L63) |

```
{'security.login': '10 per minute',
 'security.register': '10 per minute',
 'security.forgot_password': '10 per minute',
 'security.reset_password': '10 per minute'}
```

---


### RATELIMIT_STORAGE_URI

Storage backend to store rate-limiting information.

    Memory is used by default if no value is provided.
    For more information regarding the mentioned above configuration values and
    their available options you can see the `Flask-Limiter configuration
    <https://flask-limiter.readthedocs.io/en/stable/#configuration>`_.

.. note::

   Provide your Redis URL if you are rate limiting a multithreaded application.

| **Invenio RDM Default Value** | `'memory://'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L35); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L231) |

---


### RATELIMIT_STRATEGY

The rate limiting strategy to use.

The strategy used here is the most consistant but also expensive one.
If you are experiencing performance issues due to the increased Redis
traffic, you can replace it with another one from the following
`Flask-Limiter strategies
<https://flask-limiter.readthedocs.io/en/stable/#ratelimit-strategy>`_.

| **Invenio RDM Default Value** | `'moving-window'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L22) |

---


### RDM_ALLOW_EXTERNAL_DOI_VERSIONING

Allow records with external DOIs to be versioned.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L657) |

---


### **\*RDM_ALLOW_METADATA_ONLY_RECORDS**

Allow users to publish metadata-only records.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L164) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### RDM_ALLOW_OWNERS_REMOVE_COMMUNITY_FROM_RECORD

Allow record owners to remove communities from records.

When set to False, only community curators, managers, and owners can remove
communities from records. This applies to published records.
Record owners will still be able to add communities, but removal is restricted
to community curators, managers, and owners.

Default: True (backwards compatible - owners can remove communities)

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L324) |

---


### RDM_ALLOW_RESTRICTED_RECORDS

Allow users to set restricted/private records.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L173) |

---


### RDM_ARCHIVE_DOWNLOAD_ENABLED

Flag to enable/disable the all-in-one download endpoint.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L64) |

---


### RDM_CITATION_STYLES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1120) |

```
[('apa', 'APA'),
 ('harvard-cite-them-right', 'Harvard'),
 ('modern-language-association', 'MLA'),
 ('nlm-citation-sequence', 'Vancouver'),
 ('chicago-notes-bibliography', 'Chicago'),
 ('ieee', 'IEEE'),
 ('iso690-author-date-cs', l'ČSN ISO 690')]
```

---


### RDM_CITATION_STYLES_DEFAULT

Default citation style

| **Invenio RDM Default Value** | `'iso690-author-date-cs'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1130) |

---


### RDM_COMMUNITIES_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1098) |

```
{'community-detail': '/communities/<pid_value>/records',
 'community-home': '/communities/<pid_value>/',
 'community-browse': '/communities/<pid_value>/browse',
 'community-static-page': '/communities/<pid_value>/pages/<path:page_slug>',
 'community-collection': '/communities/<pid_value>/collections/<tree_slug>/<collection_slug>'}
```

---


### RDM_COMMUNITY_COLLECTIONS_RECORDS_SERVICE_CLASS

Records service backing collections; searches all records for the global-collections community.

| **OARepo Default Value** | `'oarepo_rdm.services.collections:OARepoCollectionsRecordsService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L46) |

---


### RDM_COMMUNITY_CONTENT_MODERATION_HANDLERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L863) |

```
[<invenio_rdm_records.services.communities.moderation.UserModerationHandler object>]
```

---


### RDM_COMMUNITY_INCLUSION_REQUEST_CLS

Request type for record inclusion requests.

| **Invenio RDM Default Value** | `CommunityInclusion` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L322) |

---


### RDM_COMMUNITY_REQUIRED_TO_PUBLISH

Enforces at least one community per record.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L320) |

---


### RDM_COMMUNITY_SUBMISSION_REQUEST_CLS

Request type for community submission requests.

| **OARepo Default Value** | `CommunitySubmission` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L155); [oarepo-communities](https://github.com/oarepo/oarepo-communities/blob/master/oarepo_communities/initial_config.py#L16) |

---


### RDM_CONTENT_MODERATION_HANDLERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L858) |

```
[<invenio_rdm_records.services.components.verified.UserModerationHandler object>]
```

---


### RDM_CUSTOM_FIELDS

Records custom fields definition.

.. code-block:: python

    [<custom-field-class-type>, <custom-field-class-type>, ...]

For example:

.. code-block:: python

    [TextCF(name="experiment"), ...]

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L775) |

```
[]
```

---


### RDM_CUSTOM_FIELDS_UI

Upload form custom fields UI configuration.

Of the shape:

.. code-block:: python

    [{
        section: <section_name>,
        fields: [
            {
                field: "path-to-field",  # this should be validated against the defined fields in `RDM_CUSTOM_FIELDS`
                ui_widget: "<ui-widget-name>",  # predefined or user defined ui widget
                props: {
                    label:"<ui-label-to-display>",
                    placeholder:"<placeholder-passed-to-widget>",
                    icon:"<icon-passed-to-widget>",
                    description:"<description-passed-to-widget>",
                }
            },
        ],

        # ...
    }]

For example:

.. code-block:: python

    [{
        "section": "CERN Experiment"
        "fields" : [{
            field: "experiment",  # this should be validated against the defined fields in `RDM_CUSTOM_FIELDS`
            ui_widget: "CustomTextField",  # user defined widget in my-site
            props: {
                label: "Experiment",
                placeholder: "Type an experiment...",
                icon: "pencil",
                description: "You should fill this field with one of the experiments e.g LHC, ATLAS etc.",
            }
        },
        ...
    }]

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L789) |

```
[]
```

---


### RDM_DATACITE_DUMP_OPENAIRE_ACCESS_RIGHTS

Flag to control dumping DataCite OpenAIRE access rights.

See https://guidelines.openaire.eu/en/latest/data/field_rights.html for further
information on how the OpenAIRE Guidelines expect access rights to be exposed
via the DataCite schema.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L896) |

---


### RDM_DATACITE_FUNDER_IDENTIFIERS_PRIORITY

Priority of funder identifiers types to be used for DataCite serialization.

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L893) |

```
('ror', 'doi', 'grid', 'isni', 'gnd')
```

---


### RDM_DEFAULT_FILES_ENABLED

Deposit page files enabled value on new records.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L167) |

---


### RDM_DETAIL_SIDE_BAR_MANAGE_ATTRIBUTES_EXTENSION_TEMPLATE

Side bar manage attributes extension template.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1546) |

---


### RDM_FACETS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L338); [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L69) |

```
{
    'access_status': {
        'facet': facets.access_status,
        'ui': {
            'field': 'access.status',
        },
    },
    'is_published': {
        'facet': facets.is_published,
        'ui': {
            'field': 'is_published',
        },
    },
    'file_type': {
        'facet': facets.filetype,
        'ui': {
            'field': 'files.types',
        },
    },
    'language': {
        'facet': facets.language,
        'ui': {
            'field': 'languages',
        },
    },
    'resource_type': {
        'facet': facets.resource_type,
        'ui': {
            'field': 'resource_type.type',
            'childAgg': {
                'field': 'resource_type.subtype',
            },
        },
    },
    'subject': {
        'facet': facets.subject,
        'ui': {
            'field': 'subjects.subject',
        },
    },
    'subject_nested': {
        'facet': facets.subject_nested,
        'ui': {
            'field': 'subjects.scheme',
            'childAgg': {
                'field': 'subjects.subject',
            },
        },
    },
    'subject_combined': {
        'facet': facets.subject_combined,
        'ui': {
            'field': 'subjects.scheme',
            'childAgg': {
                'field': 'subjects.subject',
            },
        },
    },
    'publication_date': {
        'facet': facets.publication_date,
        'ui': {
            'field': 'publication_date',
            'type': 'date',
            'separator': '..',
        },
    },
}
```

---


### **\*RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE**

Default additional quota size for a bucket in bytes for files.

| **Invenio RDM Default Value** | `0` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L890) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### **\*RDM_FILES_DEFAULT_MAX_FILE_SIZE**

Default maximum file size for a bucket in bytes for files.

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L887) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### **\*RDM_FILES_DEFAULT_QUOTA_SIZE**

Default size for a bucket in bytes for files.

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L884) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### **\*RDM_FILE_MODIFICATION_PERIOD**

Time period after creation during which modified files can be published.
30 + 30 denotes grace period + extra days for file modification. This is checked
during publish to block people from publishing after this period given the bucket stays open.

| **Invenio RDM Default Value** | `datetime.timedelta(days=45)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L273) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### RDM_FILE_MODIFICATION_POLICY

Policy class which evaluates whether published files can be modified by a user.

| **Invenio RDM Default Value** | `FileModificationPolicyEvaluator` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L238) |

---


### RDM_IIIF_MANIFEST_FORMATS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L904) |

```
['gif', 'jp2', 'jpeg', 'jpg', 'png', 'tif', 'tiff']
```

---


### **\*RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED**

Allow editing of published files (by default by admins only).

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L241) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### **\*RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES**

List of policies for editing published files immediately.

To enable users to modify the files of their records, configure as:

.. code-block:: python

    from invenio_rdm_records.services.request_policies import (
        FileModificationGracePeriodPolicy,
        FileModificationAdminPolicy,
    )
    RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES = [
        FileModificationGracePeriodPolicy(),
        FileModificationAdminPolicy(),
    ]

Also check whether you also want to pass a custom grace period or change
``RDM_FILE_MODIFICATION_PERIOD``.

Policies are executed in order and the first one to return True is used
as the policy for the record. As such, policies should be specified from most
to least specific.

To update a policy, create a duplicate of it and add a check on creation date to
both. When your policy comes into effect on a date in the future it will be used,
and this is the date which you will use to check whether the new or old policy
will apply.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L244) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

```
[<invenio_rdm_records.services.request_policies.FileModificationAdminPolicy object>]
```

---


### **\*RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED**

Allow increasing of draft's quota from a user's additional quota.

RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE controls how much each user has
available across their records

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L285) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### **\*RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES**

List of policies for user's increasing their quota for a draft.

To enable users and admins to increase the quota for drafts, configure as:

.. code-block:: python

    from invenio_rdm_records.services.request_policies import (
        QuotaIncreaseAdminPolicy,
        QuotaIncreasePolicy,
    )
    RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES = [
        QuotaIncreasePolicy(),
        QuotaIncreaseAdminPolicy(),
    ]

Policies are executed in order and the first one to return True is used
as the policy for the record. As such, policies should be specified from most
to least specific.

To update a policy, create a duplicate of it and add a check on creation date to
both. When your policy comes into effect on a date in the future it will be used,
and this is the date which you will use to check whether the new or old policy
will apply.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L291) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

```
[]
```

---


### RDM_IMMEDIATE_RECORD_DELETION_CHECKLIST

Checklist which appears on the modal to redirect user from immediate record deletion if possible.

The config accepts a list of dictionaries with "label" and "message" key-value pairs.
The "label" is used as the checklist question item, and the "message" is displayed in
case the user selects "Yes" on the checklist item.

Example config value:

.. code-block:: python

    RDM_IMMEDIATE_RECORD_DELETION_CHECKLIST = [
        {
            "label": _("I want to change the metadata (title, description, etc.)"),
            "message": _(
                "You can edit the metadata of a published record at any time."
            ),
        },
        {
            "label": _("I forgot to submit to a community"),
            "message": _(
                "You can submit a published record to a community by going to the "
                "record landing page and selecting the cog in the communities sidebar."
            ),
        },
    ]

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L198) |

```
[]
```

---


### RDM_IMMEDIATE_RECORD_DELETION_ENABLED

Allow users to immediately delete records.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L182) |

---


### RDM_IMMEDIATE_RECORD_DELETION_POLICIES

List of policies for immediate record deletion.

Policies are executed in order and the first one to return True is used
as the policy for the record. As such, policies should be specified from most
to least specific.

To update a policy, create a duplicate of it and add a check on creation date to
both. When your policy comes into effect on a date in the future it will be used,
and this is the date which you will use to check whether the new or old policy
will apply.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L185) |

```
[<invenio_rdm_records.services.request_policies.GracePeriodPolicy object>]
```

---


### RDM_LOCK_EDIT_PUBLISHED_FILES

Lock editing already published files (enforce record versioning).

   signature to implement:
   def lock_edit_published_files(service, identity, record=None, draft=None):

| **Invenio RDM Default Value** | `lock_edit_published_files` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L851) |

---


### RDM_MEDIA_FILES_DEFAULT_MAX_FILE_SIZE

Default maximum file size for a bucket in bytes for media files.

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L881) |

---


### RDM_MEDIA_FILES_DEFAULT_QUOTA_SIZE

Default size for a bucket in bytes for media files.

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L878) |

---


### RDM_NAMESPACES

Custom fields namespaces.

.. code-block:: python

    {<namespace>: <uri>, ...}

For example:

.. code-block:: python

    {
        "cern": "https://cern.ch/terms",
        "dwc": "http://rs.tdwg.org/dwc/terms/"
    }

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L757) |

```
{}
```

---


### RDM_NEW_RECORD_VERSION_REVIEW_POLICY

Policy for when to require a community review for new record versions.

| **Invenio RDM Default Value** | `NewRecordVersionReviewPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L158) |

---


### RDM_NOTIFICATIONS_BUILDERS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'guest-access-request-token.create': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestTokenCreateNotificationBuilder'>,
 'guest-access-request.accept': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestAcceptNotificationBuilder'>,
 'guest-access-request.submit': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestSubmitNotificationBuilder'>,
 'guest-access-request.submitted': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestSubmittedNotificationBuilder'>,
 'guest-access-request.cancel': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestCancelNotificationBuilder'>,
 'guest-access-request.decline': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestDeclineNotificationBuilder'>,
 'user-access-request.accept': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestAcceptNotificationBuilder'>,
 'user-access-request.submit': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestSubmitNotificationBuilder'>,
 'user-access-request.decline': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestDeclineNotificationBuilder'>,
 'user-access-request.cancel': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestCancelNotificationBuilder'>,
 'grant-user-access.create': <class 'invenio_rdm_records.notifications.builders.GrantUserAccessNotificationBuilder'>,
 'comment-request-event.create': <class 'invenio_requests.notifications.builders.CommentRequestEventCreateNotificationBuilder'>,
 'comment-request-event.reply': <class 'invenio_requests.notifications.builders.CommentRequestEventReplyNotificationBuilder'>,
 'comment-subcommunity-request.create': <class 'invenio_communities.notifications.builders.SubComReqCommentNotificationBuilder'>,
 'comment-subcommunity-invitation-request.create': <class 'invenio_communities.notifications.builders.SubComInvCommentNotificationBuilder'>,
 'community-submission.accept': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionAcceptNotificationBuilder'>,
 'community-submission.cancel': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionCancelNotificationBuilder'>,
 'community-submission.decline': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionDeclineNotificationBuilder'>,
 'community-submission.expire': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionExpireNotificationBuilder'>,
 'community-submission.submit': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionSubmittedNotificationBuilder'>,
 'community-invitation.accept': <class 'invenio_communities.notifications.builders.CommunityInvitationAcceptNotificationBuilder'>,
 'community-invitation.cancel': <class 'invenio_communities.notifications.builders.CommunityInvitationCancelNotificationBuilder'>,
 'community-invitation.decline': <class 'invenio_communities.notifications.builders.CommunityInvitationDeclineNotificationBuilder'>,
 'community-invitation.expire': <class 'invenio_communities.notifications.builders.CommunityInvitationExpireNotificationBuilder'>,
 'community-invitation.submit': <class 'invenio_communities.notifications.builders.CommunityInvitationSubmittedNotificationBuilder'>,
 'community-membership-request.accept': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestAcceptedNotificationBuilder'>,
 'community-membership-request.cancel': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestCancelledNotificationBuilder'>,
 'community-membership-request.decline': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestDeclinedNotificationBuilder'>,
 'community-membership-request.expire': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestExpiredNotificationBuilder'>,
 'community-membership-request.submit': <class 'invenio_communities.notifications.builders.CommunityMembershipRequestSubmittedNotificationBuilder'>,
 'subcommunity-request.create': <class 'invenio_communities.notifications.builders.SubCommunityCreate'>,
 'subcommunity-request.accept': <class 'invenio_communities.notifications.builders.SubCommunityAccept'>,
 'subcommunity-request.decline': <class 'invenio_communities.notifications.builders.SubCommunityDecline'>,
 'subcommunity-invitation-request.create': <class 'invenio_communities.notifications.builders.SubComInvitationCreate'>,
 'subcommunity-invitation-request.accept': <class 'invenio_communities.notifications.builders.SubComInvitationAccept'>,
 'subcommunity-invitation-request.decline': <class 'invenio_communities.notifications.builders.SubComInvitationDecline'>,
 'subcommunity-invitation-request.expire': <class 'invenio_communities.notifications.builders.SubComInvitationExpire'>,
 'record-deletion.accept': <class 'invenio_rdm_records.notifications.builders.RecordDeletionAcceptNotificationBuilder'>,
 'record-deletion.decline': <class 'invenio_rdm_records.notifications.builders.RecordDeletionDeclineNotificationBuilder'>}
```

---


### RDM_OAI_PMH_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L530) |

```
{}
```

---


### RDM_OAI_PMH_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L552) |

```
{'facets': [], 'sort': ['name', 'spec', 'created', 'updated']}
```

---


### RDM_OAI_PMH_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L532) |

```
{'name': {'title': l'Set name', 'fields': ['name']},
 'spec': {'title': l'Set spec', 'fields': ['spec']},
 'created': {'title': l'Created', 'fields': ['created']},
 'updated': {'title': l'Updated', 'fields': ['updated']}}
```

---


### RDM_OPTIONAL_DOI_VALIDATOR

Optional DOI transitions validate method.

Check the signature of validate_optional_doi for more information.

| **Invenio RDM Default Value** | `validate_optional_doi` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L661) |

---


### RDM_PARENT_PERSISTENT_IDENTIFIERS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L644); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L49) |

```
{'doi': {'providers': ['datacite'],
         'required': True,
         'condition': <function <lambda>>,
         'label': l'Concept DOI',
         'validator': <function is_doi>,
         'normalizer': <function normalize_doi>,
         'is_enabled': <bound method DataCitePIDProvider.is_enabled of <class 'oarepo_doi.services.providers.provider.DataCiteRecordAwareProvider'>>}}
```

---


### RDM_PARENT_PERSISTENT_IDENTIFIER_PROVIDERS
| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L633); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L39) |

```
[<oarepo_doi.services.providers.provider.DataCiteRecordAwareProvider object>]
```

---


### RDM_PERMISSION_POLICY

Override the default record permission policy.

| **Invenio RDM Default Value** | `RDMRecordPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L144) |

---


### RDM_PERSISTENT_IDENTIFIERS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L604); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L27) |

```
{'doi': {'providers': ['datacite'],
         'required': True,
         'label': l'DOI',
         'validator': <function is_doi>,
         'normalizer': <function normalize_doi>,
         'is_enabled': <bound method DataCitePIDProvider.is_enabled of <class 'oarepo_doi.services.providers.provider.DataCiteRecordAwareProvider'>>,
         'ui': {'default_selected': 'no'}},
 'oai': {'providers': ['oai'],
         'required': True,
         'label': l'OAI',
         'is_enabled': <bound method OAIPIDProvider.is_enabled of <class 'invenio_rdm_records.services.pids.providers.oai.OAIPIDProvider'>>}}
```

---


### RDM_PERSISTENT_IDENTIFIER_PROVIDERS
| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L561); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L18) |

```
[<oarepo_doi.services.providers.provider.DataCiteRecordAwareProvider object>,
 <invenio_rdm_records.services.pids.providers.oai.OAIPIDProvider object>]
```

---


### RDM_QUOTA_INCREASE_POLICY

Policy class which evaluates whether the quota for drafts can be increased.

| **Invenio RDM Default Value** | `QuotaIncreasePolicyEvaluator` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L282) |

---


### RDM_RECORDS_ACCESS_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_rdm.services.delegating.DelegatingRecordAccessService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L34) |

---


### RDM_RECORDS_ALLOW_RESTRICTION_AFTER_GRACE_PERIOD

Whether record access restriction is allowed after the grace period or not.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L950) |

---


### RDM_RECORDS_COMMUNITY_RECORDS_CONFIG_CLASS

Community records service config that uses the multiplexed search options.

| **OARepo Default Value** | `'oarepo_rdm.services.config:OARepoCommunityRecordsConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L38) |

---


### RDM_RECORDS_COMMUNITY_RECORDS_SERVICE_CLASS

Community records service that multiplexes search across per-model services.

| **OARepo Default Value** | `'oarepo_rdm.services.service:OARepoCommunityRecordsService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L41) |

---


### RDM_RECORDS_CONTAINER_EXTENSIONS

List of file extensions for container files.
Experimental, this config can later be removed.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L956) |

```
['.zip']
```

---


### **\*RDM_RECORDS_ERROR_HANDLERS**
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L59) |
| **Set by** | [`add_model`](reference/index.md#oarepo_config.add_model) |

```
{<class 'marshmallow.exceptions.ValidationError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.ValidationErrorGroup'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.RevisionIdMismatchError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.QuerystringValidationError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.PermissionDeniedError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.RecordPermissionDeniedError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_pidstore.errors.PIDDeletedError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_pidstore.errors.PIDAlreadyExists'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_pidstore.errors.PIDDoesNotExistError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_pidstore.errors.PIDUnregistered'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_pidstore.errors.PIDRedirectedError'>: <function create_pid_redirected_error_handler.<locals>.pid_redirected_error_handler>,
 <class 'sqlalchemy.exc.NoResultFound'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.FacetNotFoundError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.FileKeyNotFoundError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.ArchiveDownloadTooLargeException'>: <function create_error_handler.<locals>.error_handler>,
 <class 'json.decoder.JSONDecodeError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records.systemfields.relations.errors.InvalidRelationValue'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records.systemfields.relations.errors.InvalidCheckValue'>: <function create_error_handler.<locals>.error_handler>,
 <class 'opensearchpy.exceptions.RequestError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.FailedFileUploadException'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_records_resources.services.errors.FilesCountExceededException'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.resources.deserializers.errors.DeserializerError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'citeproc_styles.errors.StyleNotFoundError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.ReviewNotFoundError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.ReviewStateError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.ReviewExistsError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.InvalidAccessRestrictions'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.ValidationErrorWithMessageAsList'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.AccessRequestExistsError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.RecordDeletedException'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.DeletionStatusException'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.RecordSubmissionClosedCommunityError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'invenio_rdm_records.services.errors.CommunityRequiredError'>: <function create_error_handler.<locals>.error_handler>,
 <class 'oarepo_rdm.errors.UndefinedModelError'>: <function create_error_handler.<locals>.error_handler>}
```

---


### RDM_RECORDS_IDENTIFIERS_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L86) |

```
{'ark': {'label': l'ARK',
         'validator': <function is_ark>,
         'datacite': 'ARK'},
 'arxiv': {'label': l'arXiv',
           'validator': <function is_arxiv>,
           'datacite': 'arXiv'},
 'ads': {'label': l'Bibcode',
         'validator': <function is_ads>,
         'datacite': 'bibcode'},
 'crossreffunderid': {'label': l'Crossref Funder ID',
                      'validator': <function always_valid>,
                      'datacite': 'Crossref Funder ID'},
 'cstr': {'label': l'CSTR',
          'validator': <function is_cstr>,
          'datacite': 'CSTR'},
 'doi': {'label': l'DOI',
         'validator': <function is_doi>,
         'datacite': 'DOI'},
 'ean13': {'label': l'EAN13',
           'validator': <function is_ean13>,
           'datacite': 'EAN13'},
 'eissn': {'label': l'EISSN',
           'validator': <function is_issn>,
           'datacite': 'EISSN'},
 'grid': {'label': l'GRID',
          'validator': <function always_valid>,
          'datacite': 'GRID'},
 'handle': {'label': l'Handle',
            'validator': <function is_handle>,
            'datacite': 'Handle'},
 'igsn': {'label': l'IGSN',
          'validator': <function always_valid>,
          'datacite': 'IGSN'},
 'isbn': {'label': l'ISBN',
          'validator': <function is_isbn>,
          'datacite': 'ISBN'},
 'isni': {'label': l'ISNI',
          'validator': <function is_isni>,
          'datacite': 'ISNI'},
 'issn': {'label': l'ISSN',
          'validator': <function is_issn>,
          'datacite': 'ISSN'},
 'istc': {'label': l'ISTC',
          'validator': <function is_istc>,
          'datacite': 'ISTC'},
 'lissn': {'label': l'LISSN',
           'validator': <function is_issn>,
           'datacite': 'LISSN'},
 'lsid': {'label': l'LSID',
          'validator': <function is_lsid>,
          'datacite': 'LSID'},
 'pmid': {'label': l'PMID',
          'validator': <function is_pmid>,
          'datacite': 'PMID'},
 'purl': {'label': l'PURL',
          'validator': <function is_purl>,
          'datacite': 'PURL'},
 'rrid': {'label': l'RRID',
          'validator': <function is_rrid>,
          'datacite': 'RRID'},
 'upc': {'label': l'UPC',
         'validator': <function always_valid>,
         'datacite': 'UPC'},
 'url': {'label': l'URL',
         'validator': <function is_url>,
         'datacite': 'URL'},
 'urn': {'label': l'URN',
         'validator': <function is_urn>,
         'datacite': 'URN'},
 'wikidata': {'label': l'Wikidata',
              'validator': <function is_wikidata>,
              'datacite': 'Other'},
 'w3id': {'label': l'W3ID',
          'validator': <function always_valid>,
          'datacite': 'w3id'},
 'other': {'label': l'Other',
           'validator': <function always_valid>,
           'datacite': 'Other'}}
```

---


### RDM_RECORDS_LOCATION_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L136) |

```
{'wikidata': {'label': l'Wikidata', 'validator': <function is_wikidata>},
 'geonames': {'label': l'GeoNames',
              'validator': <function always_valid>}}
```

---


### **\*RDM_RECORDS_MAX_FILES_COUNT**

Max amount of files allowed to upload in the deposit form.

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L872) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### RDM_RECORDS_MAX_MEDIA_FILES_COUNT

Max amount of media files allowed to upload in the deposit form.

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L875) |

---


### RDM_RECORDS_PERSONORG_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L79) |

```
{'orcid': {'label': l'ORCID',
           'validator': <function is_orcid>,
           'datacite': 'ORCID'},
 'isni': {'label': l'ISNI',
          'validator': <function is_isni>,
          'datacite': 'ISNI'},
 'gnd': {'label': l'GND',
         'validator': <function is_gnd>,
         'datacite': 'GND'},
 'ror': {'label': l'ROR',
         'validator': <function is_ror>,
         'datacite': 'ROR'},
 'scopusid': {'label': l'Scopus Author ID',
              'validator': <function is_scopus_id>,
              'datacite': 'Scopus Author ID'},
 'researcherid': {'label': l'Researcher ID',
                  'validator': <function is_researcher_id>,
                  'datacite': 'ResearcherID'},
 'czenasautid': {'label': l'CzenasAutID',
                 'validator': <function <lambda>>},
 'vedidk': {'label': l'vedIDK', 'validator': <function is_vedidk>},
 'institutionalid': {'label': l'InstitutionalID',
                     'validator': <function <lambda>>},
 'ico': {'label': l'ICO', 'validator': <function <lambda>>},
 'doi': {'label': l'DOI',
         'validator': <function is_doi>,
         'datacite': 'DOI'},
 'url': {'label': l'URL', 'validator': <function <lambda>>},
 'grid': {'label': l'GRID', 'validator': <function <lambda>>}}
```

---


### RDM_RECORDS_PIDS_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_rdm.services.delegating.DelegatingPIDsService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L35) |

---


### RDM_RECORDS_RELATED_IDENTIFIERS_SCHEMES

This variable is used to separate related identifiers.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L133) |

```
{'ark': {'label': l'ARK',
         'validator': <function is_ark>,
         'datacite': 'ARK'},
 'arxiv': {'label': l'arXiv',
           'validator': <function is_arxiv>,
           'datacite': 'arXiv'},
 'ads': {'label': l'Bibcode',
         'validator': <function is_ads>,
         'datacite': 'bibcode'},
 'crossreffunderid': {'label': l'Crossref Funder ID',
                      'validator': <function always_valid>,
                      'datacite': 'Crossref Funder ID'},
 'cstr': {'label': l'CSTR',
          'validator': <function is_cstr>,
          'datacite': 'CSTR'},
 'doi': {'label': l'DOI',
         'validator': <function is_doi>,
         'datacite': 'DOI'},
 'ean13': {'label': l'EAN13',
           'validator': <function is_ean13>,
           'datacite': 'EAN13'},
 'eissn': {'label': l'EISSN',
           'validator': <function is_issn>,
           'datacite': 'EISSN'},
 'grid': {'label': l'GRID',
          'validator': <function always_valid>,
          'datacite': 'GRID'},
 'handle': {'label': l'Handle',
            'validator': <function is_handle>,
            'datacite': 'Handle'},
 'igsn': {'label': l'IGSN',
          'validator': <function always_valid>,
          'datacite': 'IGSN'},
 'isbn': {'label': l'ISBN',
          'validator': <function is_isbn>,
          'datacite': 'ISBN'},
 'isni': {'label': l'ISNI',
          'validator': <function is_isni>,
          'datacite': 'ISNI'},
 'issn': {'label': l'ISSN',
          'validator': <function is_issn>,
          'datacite': 'ISSN'},
 'istc': {'label': l'ISTC',
          'validator': <function is_istc>,
          'datacite': 'ISTC'},
 'lissn': {'label': l'LISSN',
           'validator': <function is_issn>,
           'datacite': 'LISSN'},
 'lsid': {'label': l'LSID',
          'validator': <function is_lsid>,
          'datacite': 'LSID'},
 'pmid': {'label': l'PMID',
          'validator': <function is_pmid>,
          'datacite': 'PMID'},
 'purl': {'label': l'PURL',
          'validator': <function is_purl>,
          'datacite': 'PURL'},
 'rrid': {'label': l'RRID',
          'validator': <function is_rrid>,
          'datacite': 'RRID'},
 'upc': {'label': l'UPC',
         'validator': <function always_valid>,
         'datacite': 'UPC'},
 'url': {'label': l'URL',
         'validator': <function is_url>,
         'datacite': 'URL'},
 'urn': {'label': l'URN',
         'validator': <function is_urn>,
         'datacite': 'URN'},
 'wikidata': {'label': l'Wikidata',
              'validator': <function is_wikidata>,
              'datacite': 'Other'},
 'w3id': {'label': l'W3ID',
          'validator': <function always_valid>,
          'datacite': 'w3id'},
 'other': {'label': l'Other',
           'validator': <function always_valid>,
           'datacite': 'Other'}}
```

---


### RDM_RECORDS_REQUIRE_SECRET_LINKS_EXPIRATION

Whether share access links require an expiration date to be set or not.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L953) |

---


### RDM_RECORDS_RESOURCE_CLASS

Replacement for the plain RDM resource class.

| **OARepo Default Value** | `'oarepo_rdm.resources.records.resource:OARepoRDMRecordResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L30) |

---


### RDM_RECORDS_RESOURCE_CONFIG_CLASS

Resource config class.

| **OARepo Default Value** | `'oarepo_rdm.resources.records.config:OARepoRDMRecordResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L27) |

---


### RDM_RECORDS_RESTRICTION_GRACE_PERIOD

Grace period for changing record access to restricted.

| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L947) |

---


### RDM_RECORDS_REVIEWS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L150) |

```
['community-submission']
```

---


### RDM_RECORDS_REVIEW_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_rdm.services.delegating.DelegatingReviewService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L33) |

---


### RDM_RECORDS_SERVICE_CLASS

Replacement for the plain RDM service class.

| **OARepo Default Value** | `'oarepo_rdm.services.service:OARepoRDMService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L24) |

---


### RDM_RECORDS_SERVICE_COMPONENTS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[<class 'invenio_rdm_records.services.components.metadata.MetadataComponent'>,
 <class 'invenio_rdm_records.services.components.custom_fields.CustomFieldsComponent'>,
 <class 'invenio_rdm_records.services.components.access.AccessComponent'>,
 <class 'invenio_rdm_records.services.components.files.RDMDraftFilesComponent'>,
 <class 'invenio_records_resources.services.base.config.Custom_DraftMediaFilesComponent'>,
 <class 'invenio_rdm_records.services.components.record_files.RecordFilesProcessorComponent'>,
 <class 'invenio_rdm_records.services.components.record_deletion.RecordDeletionComponent'>,
 <class 'invenio_drafts_resources.services.records.components.pid.PIDComponent'>,
 <class 'invenio_rdm_records.services.components.pids.PIDsComponent'>,
 <class 'invenio_rdm_records.services.components.pids.ParentPIDsComponent'>,
 <class 'invenio_drafts_resources.services.records.components.relations.RelationsComponent'>,
 <class 'invenio_rdm_records.services.components.review.ReviewComponent'>,
 <class 'invenio_rdm_records.services.components.verified.ContentModerationComponent'>,
 <class 'invenio_rdm_records.services.components.internal_notes.InternalNotesComponent'>,
 <class 'oarepo_checks.services.components.checks.OARepoCheckComponent'>]
```

---


### RDM_RECORDS_SERVICE_CONFIG_CLASS

Service config class.

| **OARepo Default Value** | `'oarepo_rdm.services.config:OARepoRDMServiceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L21) |

---


### RDM_RECORDS_UI_EDIT_URL

Default UI URL for the edit page of a Bibliographic Record.

| **Invenio RDM Default Value** | `'/uploads/<pid_value>'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L61) |

---


### RDM_RECORDS_USER_FIXTURE_PASSWORDS

Overrides for the user fixtures' passwords.

The password set for a user fixture in this dictionary overrides the
password set in the ``users.yaml`` file. This can be used to set custom
passwords for the fixture users (of course, this has to be configured
before the fixtures are installed, e.g. by setting up the services).
If ``None`` or an empty string is configured in this dictionary, then the
password from ``users.yaml`` will be used. If that is also absent, a password
will be generated randomly.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L49) |

```
{'admin@inveniosoftware.org': None}
```

---


### RDM_RECORD_DELETION_POLICY

Policy class which evaluates whether a record can be deleted by a user.

| **Invenio RDM Default Value** | `RDMRecordDeletionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L179) |

---


### RDM_RECORD_FILE_EXTRACTORS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L960) |

```
[<invenio_records_resources.services.files.extractors.zip.ZipExtractor object>]
```

---


### RDM_REQUESTS_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1091) |

```
{'user-dashboard-request-details': '/me/requests/<uuid:request_pid_value>',
 'community-dashboard-request-details': '/communities/<pid_value>/requests/<uuid:request_pid_value>',
 'community-dashboard-invitation-details': '/communities/<pid_value>/invitations/<uuid:request_pid_value>',
 'community-dashboard-membership-request-details': '/communities/<pid_value>/membership-requests/<uuid:request_pid_value>'}
```

---


### RDM_REQUEST_RECORD_DELETION_CHECKLIST

Checklist which appears on the modal to redirect user from record deletion request if possible.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L232) |

```
[]
```

---


### RDM_REQUEST_RECORD_DELETION_ENABLED

Allow users to request record deletion.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L226) |

---


### RDM_REQUEST_RECORD_DELETION_POLICIES

List of policies for record deletion requests.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L229) |

```
[<invenio_rdm_records.services.request_policies.RequestDeletionPolicy object>]
```

---


### RDM_RESOURCE_ACCESS_TOKENS_ENABLED

Flag to show whether RATs feature should be enabled.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L835) |

---


### RDM_RESOURCE_ACCESS_TOKENS_JWT_LIFETIME

Maximum tokens lifetime.

| **Invenio RDM Default Value** | `datetime.timedelta(seconds=1800)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L839) |

---


### RDM_RESOURCE_ACCESS_TOKENS_SUBJECT_SCHEMA

Resource access token Marshmallow schema for parsing JWT subject.

| **Invenio RDM Default Value** | `tokens.resource_access.SubjectSchema` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L848) |

---


### RDM_RESOURCE_ACCESS_TOKENS_WHITELISTED_JWT_ALGORITHMS

Accepted JWT algorithms for decoding the RAT.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L842) |

```
['HS256', 'HS384', 'HS512']
```

---


### RDM_RESOURCE_ACCESS_TOKEN_REQUEST_ARG

URL argument to provide resource access token.

| **Invenio RDM Default Value** | `'resource_access_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L845) |

---


### RDM_SEARCH
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L466); [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L70) |

```
{
    'facets': [
        'publication_date',
        'access_status',
        'file_type',
        'resource_type',
    ],
    'sort': [
        'bestmatch',
        'newest',
        'oldest',
        'version',
        'mostviewed',
        'mostdownloaded',
    ],
    'query_parser_cls': QueryParser.factory(mapping={'internal_notes.note': RestrictedTerm(system_permission), 'internal_notes.id': RestrictedTerm(system_permission), 'internal_notes.added_by': RestrictedTerm(system_permission), 'internal_notes.timestamp': RestrictedTerm(system_permission), '_exists_': RestrictedTermValue(system_permission, word=word_internal_notes)}, tree_transformer_cls=SearchFieldTransformer),
}
```

---


### RDM_SEARCH_DRAFTS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L507); [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L71) |

```
{
    'facets': [
        'publication_date',
        'access_status',
        'is_published',
        'resource_type',
        'file_type',
    ],
    'sort': [
        'bestmatch',
        'updated-desc',
        'updated-asc',
        'newest',
        'oldest',
        'version',
    ],
}
```

---


### RDM_SEARCH_SORT_BY_VERIFIED

Sort records by 'verified' first.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L411) |

---


### RDM_SEARCH_USER_COMMUNITIES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1106) |

```
{'facets': ['visibility', 'type'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---


### RDM_SEARCH_USER_REQUESTS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1112) |

```
{'facets': ['type', 'status'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---


### RDM_SEARCH_VERSIONING
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L519) |

```
{'facets': [],
 'sort': ['version'],
 'sort_default': 'version',
 'sort_default_no_query': 'version'}
```

---


### RDM_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L414) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']},
 'version': {'title': l'Version', 'fields': ['-versions.index']},
 'updated-desc': {'title': l'Recently updated', 'fields': ['-updated']},
 'updated-asc': {'title': l'Least recently updated', 'fields': ['updated']},
 'mostviewed': {'title': l'Most viewed',
                'fields': ['-stats.all_versions.unique_views']},
 'mostdownloaded': {'title': l'Most downloaded',
                    'fields': ['-stats.all_versions.unique_downloads']},
 'newestactivity': {'title': l'Newest activity', 'fields': ['-last_activity_at']},
 'oldestactivity': {'title': l'Oldest activity', 'fields': ['last_activity_at']}}
```

---


### RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS

Exclude file-download stats events whose Referer is the file's own preview page.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L67) |

---


### RDM_USER_MODERATION_ENABLED

Flag to enable creation of user moderation requests on specific user actions.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L869) |

---


### RECAPTCHA_PRIVATE_KEY

reCAPTCHA private key.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L336) |

---


### RECAPTCHA_PUBLIC_KEY

reCAPTCHA public key.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L333) |

---


### RECORDS_FILES_REST_ENDPOINTS

REST endpoints configuration.

You can configure the REST API endpoint to access the record's
files as follows:

.. code-block:: python

    RECORDS_FILES_REST_ENDPOINTS = {
        '<*_REST_ENDPOINTS>': {
            '<endpoint-prefix>': '<endpoint-suffix>',
        }
    }

* ``<*_REST_ENDPOINTS>`` corresponds to `Invenio-Records-REST endpoint
  configurations names
  <https://invenio-records-rest.readthedocs.io/en/latest/configuration.html
  #invenio_records_rest.config.RECORDS_REST_ENDPOINTS>`_
  that you have defined in your application.

* ``<endpoint-prefix>`` is the unique name of the endpoint configuration as it
  is defined in `Invenio-Records-REST
  <https://invenio-records-rest.readthedocs.io/en/latest/configuration.html
  #invenio_records_rest.config.RECORDS_REST_ENDPOINTS>`_ like configuration.
  This needs to match an already existing endpoint name in the
  `<*_REST_ENDPOINTS>` configuration.

* ``<endpoint-suffix>`` is the endpoint path name to access the record's files.

.. code-block:: console

    {'recid': '/myawesomefiles'} -> /records/1/myawesomefiles

An example of this configuration is provided in the
`Integration with Invenio REST API
<usage.html#integration-with-invenio-rest-api>`_ section of the documentation.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-records-files](https://github.com/inveniosoftware/invenio-records-files/blob/master/invenio_records_files/config.py#L6) |

```
{}
```

---


### RECORDS_PERMISSIONS_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### RECORDS_PERMISSIONS_RECORD_POLICY
| **Invenio RDM Default Value** | `'invenio_records_permissions.policies.RecordPermissionPolicy'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-permissions](https://github.com/inveniosoftware/invenio-records-permissions/blob/master/invenio_records_permissions/config.py#L7) |

---


### **\*RECORDS_REFRESOLVER_CLS**

Custom JSONSchemas ref resolver class.

Note that when using a custom ref resolver class you should also set
``RECORDS_REFRESOLVER_STORE`` to point to a JSONSchema ref resolver store.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L12); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L610) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*RECORDS_REFRESOLVER_STORE**

JSONSchemas ref resolver store.

Used together with ``RECORDS_REFRESOLVER_CLS`` to provide a specific
ref resolver store.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L19); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L617) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*RECORDS_RESOURCES_ALLOW_EMPTY_FILES**

Allow empty files to be uploaded.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L21) |
| **Set by** | [`configure_files`](reference/index.md#oarepo_config.configure_files) |

---


### RECORDS_RESOURCES_ARCHIVE_DOWNLOAD_MAX_SIZE

Max total file size (bytes) for archive download. ``None`` disables the cap.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L59) |

---


### RECORDS_RESOURCES_DEFAULT_TRANSFER_TYPE

Default transfer class to use.
One of 'L' (local), 'F' (fetch), 'R' (point to remote), 'M' (multipart).

| **Invenio RDM Default Value** | `'L'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L33) |

---


### RECORDS_RESOURCES_EXTRACTED_STREAM_CHUNK_SIZE

Chunk size of extracted stream used in ContainerItemResult.send_file().

| **Invenio RDM Default Value** | `65536` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L38) |

---


### RECORDS_RESOURCES_FILES_ALLOWED_DOMAINS

Explicitly allowed domains for external file fetching.

Only file URLs from these domains will be allowed to be fetched.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L12) |

```
[]
```

---


### RECORDS_RESOURCES_IMAGE_FORMATS

Which image formats to extract metadata for.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L18); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1212) |

```
['.jpg', '.jpeg', '.jp2', '.png', '.tif', '.tiff']
```

---


### RECORDS_RESOURCES_TRANSFERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L24) |

```
['invenio_records_resources.services.files.transfer.LocalTransfer',
 'invenio_records_resources.services.files.transfer.FetchTransfer',
 'invenio_records_resources.services.files.transfer.RemoteTransfer',
 'invenio_records_resources.services.files.transfer.MultipartTransfer']
```

---


### RECORDS_RESOURCES_ZIP_FORMATS

File extensions interpreted as ZIP files.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L41) |

```
['.zip']
```

---


### RECORDS_RESOURCES_ZIP_MAX_ENTRIES

Max allowed entries inside ZIP file.

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L56) |

---


### RECORDS_RESOURCES_ZIP_MAX_HEADER_SIZE

Max header size of ZIP file that can be preloaded.

| **Invenio RDM Default Value** | `65536` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L47) |

---


### RECORDS_RESOURCES_ZIP_MAX_LISTING_ENTRIES

Max entries returned by the container listing API.

| **Invenio RDM Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L44) |

---


### RECORDS_RESOURCES_ZIP_MAX_RATIO

Max allowed compression ratio of an entry inside ZIP file.

| **Invenio RDM Default Value** | `200.0` |
|--------------|-----------|
| **Type** | float |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L53) |

---


### RECORDS_RESOURCES_ZIP_MAX_TOTAL_UNCOMPRESSED

Max allowed uncompressed size of ZIP.

| **Invenio RDM Default Value** | `524288000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L50) |

---


### RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY

Default create permission factory: reject any request.

| **Invenio RDM Default Value** | `deny_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L352) |

---


### RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY

Default delete permission factory: reject any request.

| **Invenio RDM Default Value** | `deny_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L364) |

---


### RECORDS_REST_DEFAULT_LIST_PERMISSION_FACTORY

Default list permission factory: allow all requests

| **Invenio RDM Default Value** | `allow_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L355) |

---


### RECORDS_REST_DEFAULT_LOADERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L232) |

```
{
    'application/json': lambda: request.get_json(),
    'application/json-patch+json': lambda: request.get_json(force=True),
}
```

---


### RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY

Default read permission factory: check if the record exists.

| **Invenio RDM Default Value** | `check_search` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L358) |

---


### RECORDS_REST_DEFAULT_RESULTS_SIZE

Default search results size.

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L376) |

---


### RECORDS_REST_DEFAULT_SORT
| **Invenio RDM Default Value** | `dict(records=dict(query='bestmatch', noquery='mostrecent'))` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L297) |

---


### RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY

Default update permission factory: reject any request.

| **Invenio RDM Default Value** | `deny_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L361) |

---


### **\*RECORDS_REST_ENDPOINTS**
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L188); [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L14) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
[]
```

---


### RECORDS_REST_FACETS
| **Invenio RDM Default Value** | `dict(records=dict(aggs=dict(type=dict(terms=dict(field='type'))), post_filters=dict(type=terms_filte...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L317) |

---


### RECORDS_REST_FACETS_POST_FILTERS_PROPAGATE

Define if the post_filters facets in one category should be applied as filters to all the other categories

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L349) |

---


### RECORDS_REST_SEARCH_ERROR_HANDLERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L367) |

```
{
    'query_parsing_exception': 'invenio_records_rest.views:search_query_parsing_exception_handler',
    'query_shard_exception': 'invenio_records_rest.views:search_query_parsing_exception_handler',
}
```

---


### RECORDS_REST_SORT_OPTIONS
| **Invenio RDM Default Value** | `dict(records=dict(bestmatch=dict(title=_('Best match'), fields=['_score'], default_order='desc', ord...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L254) |

---


### RECORDS_UI_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### RECORDS_UI_DEFAULT_PERMISSION_FACTORY

Configure the default permission factory.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L11) |

---


### **\*RECORDS_UI_ENDPOINTS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L17); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L189) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

```
{'recid': {'pid_type': 'recid',
           'route': '/records/<pid_value>',
           'template': 'invenio_records_ui/detail.html'},
 'recid_export': {'pid_type': 'recid',
                  'route': '/records/<pid_value>/export/<format>',
                  'view_imp': 'invenio_records_ui.views.export',
                  'template': 'invenio_records_ui/export.html'}}
```

---


### RECORDS_UI_EXPORT_FORMATS

Defaut record serialization views.

The structure of the dictionary is as follows:

.. code-block:: python

    RECORDS_UI_EXPORT_FORMATS = {
        {"<pid-type>": {
            "<format-slug>": {
                "title": "<export format title>",
                "serializer": "<object or import path to record serializer>",
                "order": 1,
            },
            ...
        },
        ...
    }

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L84) |

```
{}
```

---


### RECORDS_UI_LOGIN_ENDPOINT

Endpoint where redirect the user if login is required.

| **Invenio RDM Default Value** | `'security.login'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L14) |

---


### RECORDS_UI_TOMBSTONE_TEMPLATE

Configure the tombstone template.

| **Invenio RDM Default Value** | `'invenio_records_ui/tombstone.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L8) |

---


### RECORDS_VALIDATION_TYPES

Pass additional types when validating a record against a schema.
For more details, see:
`<https://python-jsonschema.readthedocs.io/en/latest/validate/#validating-types>`_.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L6) |

```
{}
```

---


### **\*RECORD_ROUTES**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/generic_parameters.py#L42) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### RELATED_RESOURCES_DEFAULT_RESOURCE_TYPE
| **OARepo Default Value** | `'dataset'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L26) |

---


### RELATED_RESOURCES_DEFAULT_TIMEOUT
| **OARepo Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L28) |

---


### RELATED_RESOURCES_RECORD_UI_SCHEMA
| **OARepo Default Value** | `'invenio_rdm_records.resources.serializers.ui.UIRecordSchema'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L27) |

---


### RELATED_RESOURCES_RESOURCE_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.resources.RelatedResourcesResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L18) |

---


### RELATED_RESOURCES_RESOURCE_CONFIG_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.resources.RelatedResourcesResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L19) |

---


### RELATED_RESOURCES_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.services.RelatedResourcesService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L16) |

---


### RELATED_RESOURCES_SERVICE_CONFIG_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.services.RelatedResourcesServiceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L17) |

---


### REMEMBER_COOKIE_DURATION

Remember me cookie life time changed to 90 days instead of 365 days.

| **Invenio RDM Default Value** | `timedelta(days=90)` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L260) |

---


### **\*REPOSITORY_DESCRIPTION**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*REPOSITORY_KEYWORDS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*REPOSITORY_NAME**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*REPOSITORY_SUBTITLE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*REPOSITORY_SUPPORT_CONTACT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### REQUESTS_ACTION_COMPONENTS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[<class 'oarepo_requests.actions.components.WorkflowTransitionComponent'>,
 <class 'oarepo_requests.actions.components.AutoAcceptComponent'>]
```

---


### REQUESTS_ALLOWED_RECEIVERS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['community_role', 'user', 'group', 'auto_approve', 'multiple', 'action_need']
```

---


### REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_ATTRS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L158) |

```
{'img': ['src', 'alt', 'width', 'height']}
```

---


### REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_TAGS

Extend allowed HTML tags list for requests comments content.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L155) |

```
['img']
```

---


### REQUESTS_COMMENT_PREVIEW_LIMIT

Number of most recent child comments to inline in parent's search index.

This limits the size of indexed documents when comments have many replies.
Additional replies can be loaded via pagination.

| **Invenio RDM Default Value** | `5` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L140) |

---


### REQUESTS_ENTITY_RESOLVERS

Registered resolvers for resolving/creating references in request metadata.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L33) |

```
[<invenio_users_resources.entity_resolvers.UserResolver object>,
 <invenio_users_resources.entity_resolvers.GroupResolver object>]
```

---


### REQUESTS_ERROR_HANDLERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1514) |

```
{
    **request_error_handlers,
    InvalidAccessRestrictions: create_error_handler(lambda e: HTTPJSONException(code=400, description=e.description)),
}
```

---


### REQUESTS_EVENTS_SERVICE_COMPONENTS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L150) |

```
[<class 'invenio_requests.services.requests.components.RequestCommentFileValidationComponent'>,
 <class 'invenio_requests.services.requests.components.RequestCommentFileCleanupComponent'>]
```

---


### REQUESTS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L71) |

```
{'type': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
          'ui': {'field': 'type'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'status'}}}
```

---


### REQUESTS_FILES_DEFAULT_MAX_FILE_SIZE

10MB

| **Invenio RDM Default Value** | `10000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L148) |

---


### REQUESTS_FILES_DEFAULT_QUOTA_SIZE

100MB

| **Invenio RDM Default Value** | `100000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L147) |

---


### REQUESTS_LOCKING_ENABLED

Enable locking/unlocking for request conversations.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L137) |

---


### REQUESTS_MODERATION_ROLE

ID of the Role used for moderation.

| **Invenio RDM Default Value** | `'administration-moderation'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L91) |

---


### REQUESTS_PERMISSION_POLICY

The requests permission policy, extended to work with guest access requests.

| **OARepo Default Value** | `RDMRequestsPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1510); [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L20); [oarepo-workflows](https://github.com/oarepo/oarepo-workflows/blob/master/oarepo_workflows/initial_config.py#L16) |

---


### REQUESTS_REGISTERED_EVENT_TYPES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L26) |

```
[<RequestEventType 'L'>, <RequestEventType 'C'>, <RequestEventType 'R'>]
```

---


### REQUESTS_REGISTERED_TYPES

Configuration for registered Request Types.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L23) |

```
[]
```

---


### REQUESTS_RESOURCE_CLASS
| **OARepo Default Value** | `OARepoRequestsResource` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L55) |

---


### REQUESTS_RESOURCE_CONFIG_CLASS
| **OARepo Default Value** | `OARepoRequestsResourceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L56) |

---


### REQUESTS_REVIEWERS_ENABLED

Enable reviewers for requests.

| **OARepo Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L57); [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L131) |

---


### REQUESTS_REVIEWERS_MAX_NUMBER

Maximum number of reviewers allowed for a request.

| **Invenio RDM Default Value** | `15` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L134) |

---


### REQUESTS_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L36) |

```
{'download_file_html': '/requests/<uuid:pid_value>/files/<path:file_key>'}
```

---


### REQUESTS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L41) |

```
{'facets': ['type', 'status'],
 'sort': ['bestmatch', 'newest', 'oldest', 'newestactivity', 'oldestactivity']}
```

---


### REQUESTS_SERVICE_CLASS
| **OARepo Default Value** | `OARepoRequestsService` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L53) |

---


### REQUESTS_SERVICE_CONFIG_CLASS
| **OARepo Default Value** | `OARepoRequestsServiceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L54) |

---


### REQUESTS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L47) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']},
 'newestactivity': {'title': l'Newest activity', 'fields': ['-last_activity_at']},
 'oldestactivity': {'title': l'Oldest activity', 'fields': ['last_activity_at']}}
```

---


### REQUESTS_TIMELINE_PAGE_SIZE

Amount of items per page on the request details timeline

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L87) |

---


### REQUESTS_USER_MODERATION_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L120) |

```
{'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'status'}},
 'is_open': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
             'ui': {'field': 'is_open'}}}
```

---


### REQUESTS_USER_MODERATION_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L98) |

```
{'facets': ['status', 'is_open'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---


### REQUESTS_USER_MODERATION_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L104) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']}}
```

---


### REST_CSRF_ENABLED

Enable CSRF middleware. (Default: ``False``).

.. note::
   The CSRF middleware accepts some configuration parameters that are used to
   adjust the workflow of the CSRF validation. The available options are:

   \\`CSRF_SAFE_METHODS\\`: HTTP methods against which the csrf check should
   NOT run.
   Defaults to \\`['POST', 'PUT', 'PATCH', 'DELETE']\\`.

   \\`CSRF_HEADER\\`: The name of the request header used for CSRF
   authentication. Defaults to \\`X-CSRF-Token\\`.

   \\`CSRF_COOKIE_NAME\\`: The name of the request cookie used for CSRF
   authentication. Defaults to \\`_csrftoken\\`.

   \\`CSRF_COOKIE_MAX_AGE\\`: The maximum time until the cookie expires. After
   the expiration the cookie will be removed. Defaults to \\`60*60*24*7*52\\`
   (1 year).

   \\`CSRF_COOKIE_DOMAIN\\`: The domain for which the CSRF cookie should be
   valid. Defaults to \\`flask.sessions.SessionInterface.get_cookie_domain\\`.

   \\`CSRF_COOKIE_PATH\\`: The url path for which the cookie is set. This is
   useful if you have multiple Flask instances running under the same hostname.
   They can use different cookie paths, and each instance will only see its own
   CSRF cookie.
   Defaults to \\`flask.sessions.SessionInterface.get_cookie_path\\`.

   \\`CSRF_COOKIE_SAMESITE\\`: Restrict if CSRF cookie should be sent along
   requests coming from external sites. Defaults to
   \\`SESSION_COOKIE_SAMESITE\\` configuation variable, if this is set to
   a not \\`None\\` value, or \\`Lax\\`. Lax prevents sending cookies with
   CSRF-prone requests from external sites, such as submitting a form.

   \\`CSRF_SECRET\\`: Secret key to encode/decode csrf token. Defaults to
   application \\`SECRET_KEY\\`.

   \\`CSRF_SECRET_SALT\\`: The salt value used to encode/decode csrf token.
   Defaults to \\`invenio-csrf-token\\`.

   \\`CSRF_TOKEN_LENGTH\\`: The length of the generated csrf token. Defaults to
   \\`12\\`.

   \\`CSRF_ALLOWED_CHARS\\`: The allowed characters that can be included in the
   generation of the csrf token. Defaults to \\`string.ascii_letters\\` +
   \\`string.digits\\`.

   \\`CSRF_FORCE_SECURE_REFERER\\`: Flag to disable secure referrer check. This
   should used only in development if you run your UI application over HTTP.
   Defaults to \\`True\\`.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L738); [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L74) |

---


### REST_ENABLE_CORS

Enable CORS configuration. (Default: ``False``).

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L49) |

---


### REST_MIMETYPE_QUERY_ARG_NAME

Name of the query argument to specify the mimetype wanted for the output.
   Set it to None to disable.

.. note::
   You can customize the query argument name by specifying it as a string::

        REST_MIMETYPE_QUERY_ARG_NAME = 'format'

   With this value, the url will be::

        /api/record/<id>?format=<value>

   You can set the accepted values passing a dictionary to the key
   `record_serializers_aliases`::

       record_serializers_aliases={
          'json': 'application/json',
          'marc21': 'application/marcxml+xml'
       }

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L52) |

---


### **\*ROR_CLIENT_ID**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/generic_parameters.py#L42) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*S3_ACCESS_KEY_ID**

The access key to use when creating the client.

This is entirely optional, and if not provided, the credentials configured for
the session will automatically be used.
See `Configuring Credentials
<https://boto3.readthedocs.io/en/latest/guide/configuration.html#credentials>`_.
for more information.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L28) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### S3_CONFIG_EXTRA

Additional configuration to be passed to S3f3.
In some cases, specially those not using AWS S3, some extra configuration might be needed.

 .. code-block:: python

    {
        "request_checksum_calculation": "WHEN_REQUIRED",
        "response_checksum_validation": "WHEN_REQUIRED",
    }

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L74) |

```
{}
```

---


### S3_DEFAULT_BLOCK_SIZE

Default block size value used to send multi-part uploads to S3.
Typically 5Mb is minimum allowed by the API.

| **Invenio RDM Default Value** | `5242880` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L70) |

---


### **\*S3_ENDPOINT_URL**

S3 server URL endpoint.

If using Amazon AWS S3 service this config variable can be set to None as the
underlining library, `boto3 <https://boto3.readthedocs.io/en/latest/>`_,
will automatically construct the appropriate URL to use when communicating with
a service.

If set to a value (including the "http/https" scheme) it will be passed as
``endpoint_url`` to boto3 `client
<https://boto3.readthedocs.io/en/latest/reference/core/session.html#boto3.session.Session.client>`_.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L5) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### S3_MAXIMUM_NUMBER_OF_PARTS

Maximum number of parts to be used.
See `AWS Multipart Upload Overview
<https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_ for more
information.

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L63) |

---


### S3_REGION_NAME

S3 region name

This is entirely optional, and if not provided, the region name will be
automatically set to 'us-east-1'.

If set to a value it will be passed as ``region_name`` to boto3 `client
<https://boto3.readthedocs.io/en/latest/reference/core/session.html#boto3.session.Session.client>`_.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L18) |

---


### **\*S3_SECRET_ACCESS_KEY**

The secret key to use when creating the client.

This is entirely optional, and if not provided, the credentials configured for
the session will automatically be used.
See `Configuring Credentials
<https://boto3.readthedocs.io/en/latest/guide/configuration.html#credentials>`_.
for more information.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L38) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### S3_SIGNATURE_VERSION

Version of the S3 signature algorithm. Can be 's3' (v2) or 's3v4' (v4).
See `Amazon Boto3 documentation on configuration variables
<https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuration-file>`_
for more information.

| **Invenio RDM Default Value** | `'s3v4'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L56) |

---


### S3_UPLOAD_URL_EXPIRATION

Number of seconds the file upload URL will be valid. The default here is 7 days
to allow large file uploads with large number of chunks to be completed. This is
currently the maximum allowed by the AWS.
See `Amazon Boto3 documentation on presigned URLs
<https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.generate_presigned_url>`_
for more information.

| **Invenio RDM Default Value** | `604800` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L87) |

---


### S3_URL_EXPIRATION

Number of seconds the file serving URL will be valid.

See `Amazon Boto3 documentation on presigned URLs
<https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.generate_presigned_url>`_
for more information.

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L48) |

---


### **\*SEARCH_CLIENT_CONFIG**

Dictionary of options for the Elasticsearch/OpenSearch client.

The value of this variable is passed to :py:class:`elasticsearch.Elasticsearch`
(or :py:class:`opensearchpy.OpenSearch`) as keyword arguments and is used to configure
the client. See the available keyword arguments in the two following classes:

- :py:class:`elasticsearch.Elasticsearch`
- :py:class:`elasticsearch.Transport`

Or:

- :py:class:`opensearchpy.OpenSearch`
- :py:class:`opensearchpy.Transport`

If you specify the key ``hosts`` in this dictionary, the configuration variable
:py:class:`~invenio_search.config.SEARCH_HOSTS` will have no effect.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L13) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SEARCH_ELASTIC_HOSTS

Deprecated alias for ``SEARCH_HOSTS``.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L50) |

---


### **\*SEARCH_HOSTS**

Search hosts.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L732); [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L32) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*SEARCH_INDEX_PREFIX**

Any index, alias and templates will be prefixed with this string.

Useful to host multiple instances of the app on the same Elasticsearch cluster,
for example on one app you can set it to `dev-` and on the other to `prod-`,
and each will create non-colliding indices prefixed with the corresponding
string.

Usage example:

.. code-block:: python

    # in your config.py
    SEARCH_INDEX_PREFIX = 'prod-'

For templates, ensure that the prefix `__SEARCH_INDEX_PREFIX__` is added to
your index names. This pattern will be replaced by the prefix config value.

Usage example in your template.json:

.. code-block:: json

    {
        "index_patterns": ["__SEARCH_INDEX_PREFIX__myindex-name-*"]
    }

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L94) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SEARCH_MAPPINGS

List of aliases for which, their search mappings should be created.

- If `None` all aliases (and their search mappings) defined through the
  ``invenio_search.mappings`` entry point in setup.py will be created.
- Provide an empty list ``[]`` if no aliases (or their search mappings)
  should be created.

For example if you don't want to create aliases
and their mappings for `authors`:

.. code-block:: python

    # in your `setup.py` you would specify:
    entry_points={
        'invenio_search.mappings': [
            'records = invenio_foo_bar.mappings',
            'authors = invenio_foo_bar.mappings',
        ],
    }

    # and in your config.py
    SEARCH_MAPPINGS = ['records']

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L54) |

---


### SEARCH_RESULTS_MIN_SCORE

If set, the `min_score` parameter is added to each search request body.

The `min_score` parameter excludes results which have a `_score` less than
the minimum specified in `min_score`.

Note that the `max_score` varies depending on the number of results for a given
search query and it is not absolute value. Therefore, setting `min_score` too
high can lead to 0 results because it can be higher than any result's `_score`.

Please refer to `Elasticsearch min_score documentation
<https://www.elastic.co/guide/en/elasticsearch/reference/current/
search-request-min-score.html>`_ for more information.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L79) |

---


### SEARCH_UI_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SEARCH_UI_HEADER_TEMPLATE
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SEARCH_UI_JSTEMPLATE_COUNT

Configure the count template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/count.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L24) |

---


### SEARCH_UI_JSTEMPLATE_ERROR

Configure the error page template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/error.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L27) |

---


### SEARCH_UI_JSTEMPLATE_FACETS

Configure the facets template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/facets.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L30) |

---


### SEARCH_UI_JSTEMPLATE_LOADING

Configure the loading template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/loading.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L44) |

---


### SEARCH_UI_JSTEMPLATE_PAGINATION

Configure the pagination template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/pagination.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L47) |

---


### SEARCH_UI_JSTEMPLATE_RANGE

Configure the range template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/range.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L33) |

---


### SEARCH_UI_JSTEMPLATE_RANGE_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L36) |

```
{'histogramId': '#year_hist',
 'selectionId': '#year_select',
 'name': 'years',
 'width': 180}
```

---


### SEARCH_UI_JSTEMPLATE_RESULTS

Configure the results template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/results.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L50) |

---


### SEARCH_UI_JSTEMPLATE_SELECT_BOX

Configure the select box template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/selectbox.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L53) |

---


### SEARCH_UI_JSTEMPLATE_SORT_ORDER

Configure the toggle button template.

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/togglebutton.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L56) |

---


### SEARCH_UI_SEARCH_API

Configure the search engine endpoint.

| **Invenio RDM Default Value** | `'/api/records/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L16) |

---


### SEARCH_UI_SEARCH_CONFIG_GEN
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L59) |

```
{'invenio_records_rest': <class 'invenio_search_ui.views.SearchAppInvenioRestConfigHelper'>}
```

---


### SEARCH_UI_SEARCH_INDEX

Name of the search index used.

| **Invenio RDM Default Value** | `'records'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L19) |

---


### **\*SEARCH_UI_SEARCH_TEMPLATE**

Configure the search page template.

| **Invenio RDM Default Value** | `'invenio_search_ui/search.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L11); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L782) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*SEARCH_UI_SEARCH_VIEW**

Default funtion to do the `search` route.

| **Invenio RDM Default Value** | `search` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L8) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*SECRET_KEY**

Flask secret key.

Each installation (dev, production, ...) needs a separate key.

SECURITY WARNING: keep the secret key used in production secret!

| **Invenio RDM Default Value** | `'CHANGE_ME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L213) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SECRET_KEY_FALLBACKS
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_AUTO_LOGIN_AFTER_CONFIRM
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_BLUEPRINT_NAME
| **Default Value** | `'security'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### **\*SECURITY_CHANGEABLE**

Allow password change by users.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L170) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SECURITY_CHANGE_PASSWORD_TEMPLATE

Default template for change password.

| **Invenio RDM Default Value** | `'invenio_accounts/change_password.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L218) |

---


### SECURITY_CHANGE_SALT
| **Default Value** | `'change-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_CHANGE_URL

URL endpoint for password change.

| **Invenio RDM Default Value** | `'/account/settings/password/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L239) |

---


### SECURITY_CLI_ROLES_NAME
| **Default Value** | `'roles'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_CLI_USERS_NAME
| **Default Value** | `'users'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### **\*SECURITY_CONFIRMABLE**

Allow user to confirm their email address.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L173) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SECURITY_CONFIRM_EMAIL_WITHIN

Amount of time the email confirmation link is active.

Note, since the confirmation link will also login the associated user we expire
the link fast.

| **Invenio RDM Default Value** | `'30 minutes'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L182) |

---


### SECURITY_CONFIRM_ERROR_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_CONFIRM_SALT
| **Default Value** | `'confirm-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_CONFIRM_URL
| **Default Value** | `'/confirm'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_DEFAULT_HTTP_AUTH_REALM
| **Default Value** | `'Login Required'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_DEFAULT_REMEMBER_ME

"Remember me" default value in login form.

This is only the default value in the login form. A user can always choose to
change it when they login.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L163) |

---


### SECURITY_DEPRECATED_HASHING_SCHEMES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['hex_md5']
```

---


### SECURITY_DEPRECATED_PASSWORD_SCHEMES

Deprecated password hashing algorithms.

Password hashes in a deprecated scheme are automatically migrated to the
new default algorithm the next time the user login.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L153) |

```
['invenio_aes_encrypted_email']
```

---


### SECURITY_EMAIL_HTML
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_EMAIL_PLAINTEXT
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_EMAIL_SUBJECT_CONFIRM
| **Default Value** | `'Please confirm your email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE
| **Default Value** | `'Your password has been changed'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE
| **Default Value** | `'Your password has been reset'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_EMAIL_SUBJECT_PASSWORD_RESET
| **Default Value** | `'Password reset instructions'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_EMAIL_SUBJECT_REGISTER

Email subject for account registration emails.

| **Invenio RDM Default Value** | `'Welcome'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L409) |

---


### SECURITY_FLASH_MESSAGES
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_FORGOT_PASSWORD_TEMPLATE

Default template for password recovery (asking for email).

| **Invenio RDM Default Value** | `'invenio_accounts/forgot_password.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L206) |

---


### SECURITY_HASHING_SCHEMES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['sha256_crypt', 'hex_md5']
```

---


### SECURITY_I18N_DIRNAME
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-...` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_I18N_DOMAIN
| **Default Value** | `'messages'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_LOGIN_SALT
| **Default Value** | `'login-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_LOGIN_URL

URL endpoint for login.

| **Invenio RDM Default Value** | `'/login/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L233) |

---


### SECURITY_LOGIN_USER_TEMPLATE

Default template for login.

| **Invenio RDM Default Value** | `'invenio_oauthclient/login_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L209) |

---


### SECURITY_LOGIN_WITHIN
| **Default Value** | `'1 days'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### **\*SECURITY_LOGIN_WITHOUT_CONFIRMATION**

Allow users to login without first confirming their email address.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L199) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SECURITY_LOGOUT_URL

URL endpoint for logout.

| **Invenio RDM Default Value** | `'/logout/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L236) |

---


### SECURITY_MSG_ALREADY_CONFIRMED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Your email has already been confirmed.', 'info')
```

---


### SECURITY_MSG_CONFIRMATION_EXPIRED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You did not confirm your email within %(within)s. New instructions to confirm your '
 'email have been sent to %(email)s.',
 'error')
```

---


### SECURITY_MSG_CONFIRMATION_REQUEST
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Confirmation instructions have been sent to %(email)s.', 'info')
```

---


### SECURITY_MSG_CONFIRMATION_REQUIRED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Email requires confirmation.', 'error')
```

---


### SECURITY_MSG_CONFIRM_REGISTRATION
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Thank you. Confirmation instructions have been sent to %(email)s.', 'success')
```

---


### SECURITY_MSG_DISABLED_ACCOUNT
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Account is disabled.', 'error')
```

---


### SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('%(email)s is already associated with an account.', 'error')
```

---


### SECURITY_MSG_EMAIL_CONFIRMED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Thank you. Your email has been confirmed.', 'success')
```

---


### SECURITY_MSG_EMAIL_NOT_PROVIDED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Email not provided', 'error')
```

---


### SECURITY_MSG_FORGOT_PASSWORD
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Forgot password?', 'info')
```

---


### SECURITY_MSG_INVALID_CONFIRMATION_TOKEN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid confirmation token.', 'error')
```

---


### SECURITY_MSG_INVALID_EMAIL_ADDRESS
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid email address', 'error')
```

---


### SECURITY_MSG_INVALID_LOGIN_TOKEN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid login token.', 'error')
```

---


### SECURITY_MSG_INVALID_PASSWORD
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid password', 'error')
```

---


### SECURITY_MSG_INVALID_REDIRECT
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Redirections outside the domain are forbidden', 'error')
```

---


### SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid reset password token.', 'error')
```

---


### SECURITY_MSG_LOCAL_LOGIN_DISABLED

The error to be displayed in REST login when local login is disabled.

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L242) |

```
('Local login is disabled.', 'error')
```

---


### SECURITY_MSG_LOGIN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Please log in to access this page.', 'info')
```

---


### SECURITY_MSG_LOGIN_EMAIL_SENT
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Instructions to login have been sent to %(email)s.', 'success')
```

---


### SECURITY_MSG_LOGIN_EXPIRED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You did not login within %(within)s. New instructions to login have been sent to '
 '%(email)s.',
 'error')
```

---


### SECURITY_MSG_PASSWORD_BREACHED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password on breached list', 'error')
```

---


### SECURITY_MSG_PASSWORD_BREACHED_SITE_ERROR
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Failed to contact breached passwords site', 'error')
```

---


### SECURITY_MSG_PASSWORD_CHANGE
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You successfully changed your password.', 'success')
```

---


### SECURITY_MSG_PASSWORD_CHANGE_DISABLED

The error to be displayed in REST password change when it is disabled.

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L248) |

```
('Password change is disabled.', 'error')
```

---


### SECURITY_MSG_PASSWORD_INVALID_LENGTH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password must be at least %(length)s characters', 'error')
```

---


### SECURITY_MSG_PASSWORD_IS_THE_SAME
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Your new password must be different than your previous password.', 'error')
```

---


### SECURITY_MSG_PASSWORD_MISMATCH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password does not match', 'error')
```

---


### SECURITY_MSG_PASSWORD_NOT_PROVIDED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password not provided', 'error')
```

---


### SECURITY_MSG_PASSWORD_NOT_SET
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('No password is set for this user', 'error')
```

---


### SECURITY_MSG_PASSWORD_RECOVERY_DISABLED
| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L251) |

```
('Password recovery is disabled.', 'error')
```

---


### SECURITY_MSG_PASSWORD_RESET
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You successfully reset your password and you have been logged in automatically.',
 'success')
```

---


### SECURITY_MSG_PASSWORD_RESET_DISABLED

The error to be displayed in REST password reset when it is disabled.

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L257) |

```
('Password reset is disabled.', 'error')
```

---


### SECURITY_MSG_PASSWORD_RESET_EXPIRED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You did not reset your password within %(within)s. New instructions have been sent '
 'to %(email)s.',
 'error')
```

---


### SECURITY_MSG_PASSWORD_RESET_REQUEST
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Instructions to reset your password have been sent to %(email)s.', 'info')
```

---


### SECURITY_MSG_PASSWORD_TOO_SIMPLE
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password not complex enough', 'error')
```

---


### SECURITY_MSG_REFRESH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Please reauthenticate to access this page.', 'info')
```

---


### SECURITY_MSG_REGISTRATION_DISABLED

The error to be displayed in REST registration when it is disabled.

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L245) |

```
('Registration is disabled.', 'error')
```

---


### SECURITY_MSG_RETYPE_PASSWORD_MISMATCH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Passwords do not match', 'error')
```

---


### SECURITY_MSG_UNAUTHORIZED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You do not have permission to view this resource.', 'error')
```

---


### SECURITY_MSG_USER_DOES_NOT_EXIST
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Specified user does not exist', 'error')
```

---


### SECURITY_PASSWORD_BREACHED_COUNT
| **Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### SECURITY_PASSWORD_CHECK_BREACHED
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_PASSWORD_COMPLEXITY_CHECKER
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_PASSWORD_HASH

Default password hashing algorithm for new passwords.

| **Invenio RDM Default Value** | `'pbkdf2_sha512'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L144) |

---


### SECURITY_PASSWORD_LENGTH_MIN
| **Default Value** | `6` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### SECURITY_PASSWORD_SALT

Salt for storing passwords.

| **Invenio RDM Default Value** | `'CHANGE_ME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L202) |

---


### SECURITY_PASSWORD_SCHEMES

Supported password hashing algorithms (for passwords already stored).

You should include both the default, supported and any deprecated schemes.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L147) |

```
['pbkdf2_sha512', 'invenio_aes_encrypted_email']
```

---


### SECURITY_PASSWORD_SINGLE_HASH

Password hashing algorithms requiring single hasing only.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L160) |

```
['invenio_aes_encrypted_email']
```

---


### SECURITY_POST_CHANGE_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_POST_CONFIRM_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_POST_LOGIN_VIEW
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_POST_LOGOUT_VIEW
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_POST_REGISTER_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_POST_RESET_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### **\*SECURITY_RECOVERABLE**

Allow password recovery by users.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L176) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*SECURITY_REGISTERABLE**

Allow users to register.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L179) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SECURITY_REGISTER_URL

URL endpoint for user registation.

| **Invenio RDM Default Value** | `'/signup/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L227) |

---


### SECURITY_REGISTER_USER_TEMPLATE

Default template for user registration.

| **Invenio RDM Default Value** | `'invenio_accounts/register_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L212) |

---


### SECURITY_RESET_PASSWORD_TEMPLATE

Default template for password recovery (reset of the password).

| **Invenio RDM Default Value** | `'invenio_accounts/reset_password.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L215) |

---


### SECURITY_RESET_PASSWORD_WITHIN

Amount of time the password reset link is active.

Note, since the confirmation link will also login the associated user we expire
the link fast.

| **Invenio RDM Default Value** | `'30 minutes'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L189) |

---


### SECURITY_RESET_SALT
| **Default Value** | `'reset-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_RESET_URL

URL endpoint for password recovery.

| **Invenio RDM Default Value** | `'/lost-password/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L230) |

---


### SECURITY_SEND_CONFIRMATION_TEMPLATE

Default template for email confirmation.

| **Invenio RDM Default Value** | `'invenio_accounts/send_confirmation.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L221) |

---


### SECURITY_SEND_LOGIN_TEMPLATE

Default template for email confirmation.

| **Invenio RDM Default Value** | `'invenio_accounts/send_login.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L224) |

---


### SECURITY_SEND_PASSWORD_CHANGE_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_SEND_PASSWORD_RESET_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_SEND_REGISTER_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SECURITY_SUBDOMAIN
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_TOKEN_AUTHENTICATION_HEADER
| **Default Value** | `'Authentication-Token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_TOKEN_AUTHENTICATION_KEY
| **Default Value** | `'auth_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SECURITY_TOKEN_MAX_AGE
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_TRACKABLE

Enable user tracking on login.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L196) |

---


### SECURITY_URL_PREFIX
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SECURITY_USER_IDENTITY_ATTRIBUTES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['email']
```

---


### SECURITY_ZXCVBN_MINIMUM_SCORE
| **Default Value** | `3` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### **\*SEND_FILE_MAX_AGE_DEFAULT**
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SENTRY_DSN

Set SENTRY_DSN environment variable.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L98) |

---


### SERVER_NAME
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### **\*SESSION_COOKIE_DOMAIN**
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SESSION_COOKIE_HTTPONLY
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SESSION_COOKIE_NAME
| **Default Value** | `'session'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### SESSION_COOKIE_PARTITIONED
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SESSION_COOKIE_PATH
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### SESSION_COOKIE_SAMESITE

Restricts how cookies are sent with requests from external sites.

| **Invenio RDM Default Value** | `'Lax'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L224) |

---


### **\*SESSION_COOKIE_SECURE**

Sets cookie with the secure flag by default.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L221) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SESSION_KEY_BITS
| **Default Value** | `64` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---


### SESSION_RANDOM_SOURCE
| **Default Value** | `<random.SystemRandom object>` |
|--------------|-----------|
| **Type** | SystemRandom |
| **Source** | unknown |

---


### SESSION_REFRESH_EACH_REQUEST
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### **\*SETTINGS_TEMPLATE**

Settings page template used for e.g. display user settings views.

| **Invenio RDM Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L36); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L272) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### SITEMAP_MAX_ENTRY_COUNT

Maximum number of entries (<url> or <sitemap>) per file.

The Sitemap protocol sets it at 50_000, but it also sets the max size of the
resulting file at 50 MiB. Following the initial Zenodo implementation, we
set it much lower than 50_000 so as to not have to check for generated size.

Following the initial Zenodo implementation, we use the same config for the
number of entries in the Sitemap Index and Sitemap files.

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L7) |

---


### SITEMAP_ROOT_VIEW_ENABLED

Enable the `/sitemap.xml` endpoint serving the first sitemap index.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L21) |

---


### SITEMAP_SECTIONS

Instances of `sitemap.SitemapSection` that will populate the Sitemap files.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L18); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1552) |

```
[]
```

---


### **\*SITE_API_URL**
| **Invenio RDM Default Value** | `'https://127.0.0.1:5000/api'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L10) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*SITE_UI_URL**
| **Invenio RDM Default Value** | `'https://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L8) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SQLALCHEMY_BINDS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{}
```

---


### **\*SQLALCHEMY_DATABASE_URI**
| **Invenio RDM Default Value** | `'sqlite:////Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instan...` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L517) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### SQLALCHEMY_ECHO

Enable to see all SQL queries.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L525) |

---


### SQLALCHEMY_ENGINE_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L528) |

```
{}
```

---


### SQLALCHEMY_RECORD_QUERIES
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### SQLALCHEMY_TRACK_MODIFICATIONS
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### **\*STATS_AGGREGATIONS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1280); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L42) |
| **Set by** | [`configure_stats`](reference/index.md#oarepo_config.configure_stats) |

```
{}
```

---


### **\*STATS_EVENTS**

Enabled Events.

Each key is the name of an event. A queue will be created for each event.

If the dict of an event contains the ``signal`` key, and the config variable
``STATS_REGISTER_RECEIVERS`` is ``True``, a signal receiver will be registered.
Receiver function which will be connected on a signal and emit events. The key
is the name of the emitted event.

``signal``: Signal to which the receiver will be connected to.

``event_builders``: list of functions which will create and enhance the event.
    Each function will receive the event created by the previous function and
    can update it. Keep in mind that these functions will run synchronously
    during the creation of the event, meaning that if the signal is sent during
    a request they will increase the response time.

You can find a sampe of STATS_EVENT configuration in the `registrations.py`

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1244); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L20) |
| **Set by** | [`configure_stats`](reference/index.md#oarepo_config.configure_stats) |

```
{}
```

---


### STATS_EVENTS_UTC_DATETIME_ENABLED

Enable timezone-aware UTC datetimes for event timestamps.

When set to ``False`` (default), naive UTC datetimes are used (tzinfo is
stripped via ``datetime.replace(tzinfo=None)``). Set to ``True`` to use
timezone-aware UTC datetimes with explicit UTC timezone information.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L75) |

---


### STATS_MQ_EXCHANGE
| **Invenio RDM Default Value** | `Exchange('events', type='direct', delivery_mode='transient')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L62) |

---


### **\*STATS_PERMISSION_FACTORY**

Permission factory used by the statistics REST API.

This is a function which returns a permission granting or forbidding access
to a request. It is of the form ``permission_factory(query_name, params)``
where ``query_name`` is the name of the statistic requested by the user and
``params`` is a dict of parameters for this statistic. The result of the
function is a Permission.

See Invenio-access and Flask-principal for a better understanding of the
access control mechanisms.

| **Invenio RDM Default Value** | `permissions_policy_lookup_factory` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1414); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L48) |
| **Set by** | [`configure_stats`](reference/index.md#oarepo_config.configure_stats) |

---


### **\*STATS_QUERIES**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1331); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L45) |
| **Set by** | [`configure_stats`](reference/index.md#oarepo_config.configure_stats) |

```
{}
```

---


### STATS_REGISTER_INDEX_TEMPLATES

Register templates as index templates.

Default behaviour will register the templates as search templates.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L69) |

---


### **\*STATS_REGISTER_RECEIVERS**

Enable the registration of signal receivers.

Default is ``True``.
The signal receivers are functions which will listen to the signals listed in
by the ``STATS_EVENTS`` config variable. An event will be generated for each
signal sent.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L11) |
| **Set by** | [`configure_stats`](reference/index.md#oarepo_config.configure_stats) |

---


### TEMPLATES_AUTO_RELOAD
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### TESTING
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### THEME_401_TEMPLATE

The template used for 401 Unauthorized errors.

| **Invenio RDM Default Value** | `'invenio_theme/401.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L139) |

---


### THEME_403_TEMPLATE

The template used for 403 Forbidden errors.

| **Invenio RDM Default Value** | `'invenio_theme/403.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L142) |

---


### THEME_404_TEMPLATE

The template used for 404 Not Found errors.

| **Invenio RDM Default Value** | `'invenio_theme/404.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L145) |

---


### THEME_429_TEMPLATE

The template used for 429 Too Many Requests errors.

| **Invenio RDM Default Value** | `'invenio_theme/429.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L148) |

---


### THEME_500_TEMPLATE

The template used for 500 Internal Server Error errors.

| **Invenio RDM Default Value** | `'invenio_theme/500.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L151) |

---


### THEME_BASE_TEMPLATE

Template which all templates in Invenio-Theme all extends from.

Defaults to value of :const:`BASE_TEMPLATE`.

| **Invenio RDM Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L62) |

---


### THEME_COVER_TEMPLATE

Template which all cover templates in Invenio-Theme all extends from.

Defaults to value of :const:`COVER_TEMPLATE`.

| **Invenio RDM Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L68) |

---


### **\*THEME_CSS_TEMPLATE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### THEME_ERROR_TEMPLATE

Base template for error pages.

| **Invenio RDM Default Value** | `'invenio_theme/page_error.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L80) |

---


### **\*THEME_FOOTER_TEMPLATE**

Footer template which is normally included in :data:`BASE_TEMPLATE`.

| **Invenio RDM Default Value** | `'invenio_theme/footer.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L45); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L275) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*THEME_FRONTPAGE**

Enable or disable basic frontpage view.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L121); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L278) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*THEME_FRONTPAGE_LOGO**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*THEME_FRONTPAGE_TEMPLATE**

Template for front page.

| **Invenio RDM Default Value** | `'invenio_theme/frontpage.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L127); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L287) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*THEME_FRONTPAGE_TITLE**

The title shown on the frontpage.

| **Invenio RDM Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L124); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L281) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### THEME_GENERATOR

Generator meta tag to identify the software that generated the page.

Accepts a string or a func returning a string. Set it to `None` to disable it.

| **Invenio RDM Default Value** | `'Invenio'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L83); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L311) |

---


### THEME_GOOGLE_SITE_VERIFICATION

List of Google Site Verification tokens to be used.

This adds the Google Site Verification into the meta tags of all pages.

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L109) |

```
[]
```

---


### **\*THEME_HEADER_LOGIN_TEMPLATE**

Header login template, included in :data:`THEME_HEADER_TEMPLATE`.

| **Invenio RDM Default Value** | `'invenio_theme/header_login.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L42); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L290) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*THEME_HEADER_TEMPLATE**

Header template which is normally included in :data:`BASE_TEMPLATE`.

| **Invenio RDM Default Value** | `'invenio_theme/header.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L39); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L284) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### THEME_ICONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L154) |

```
{'semantic-ui': {'key': 'key icon',
                 'link': 'linkify icon',
                 'shield': 'shield alternate icon',
                 'user': 'user icon',
                 'codepen': 'codepen icon',
                 'cogs': 'cogs icon',
                 'home': 'home icon',
                 'exchange': 'exchange icon',
                 'star_outline': 'star outline icon',
                 'users': 'users icon',
                 '*': '{} icon'},
 'bootstrap3': {'key': 'fa fa-key fa-fw',
                'link': 'fa fa-link fa-fw',
                'shield': 'fa fa-shield fa-fw',
                'user': 'fa fa-user fa-fw',
                'codepen': 'fa fa-codepen fa-fw',
                'cogs': 'fa fa-cogs fa-fw',
                '*': 'fa fa-{} fa-fw'}}
```

---


### **\*THEME_JAVASCRIPT_TEMPLATE**

Javascript assets template, normally included in :data:`BASE_TEMPLATE`.

The default template just includes the Invenio-Theme JavaScript bundle.
Set a new template if you would like to customize which JavaScript assets are
included on all pages.

| **Invenio RDM Default Value** | `'invenio_theme/javascript.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L48); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L329) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*THEME_LOGO**

The logo to be used on the header and on the cover.

| **Invenio RDM Default Value** | `'images/invenio-white.svg'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L115); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L317) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### THEME_LOGO_ADMIN

The logo to be used on the admin views header.

| **Invenio RDM Default Value** | `'images/invenio-white.svg'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L118) |

---


### THEME_MATHJAX_CDN

MathJax configuration for rendering mathematical formulas.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L181) |

---


### THEME_META_ROBOT_TAGS

Robots meta tag to control indexing of the page.

Accepts a list of dicts that will be converted into meta tag attributes, e.g.:

.. code-block:: python

    THEME_META_ROBOT_TAGS = [
        {"name": "robots", "content": "noindex, nofollow"},
        {"name": "googlebot", "content": "noimageindex"},
    ]

will generate:

.. code-block:: html

    <meta name="robots" content="noindex, nofollow">
    <meta name="googlebot" content="noimageindex">

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L89) |

```
[]
```

---


### THEME_SEARCHBAR

Enable or disable the header search bar.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L130) |

---


### **\*THEME_SEARCH_ENDPOINT**

The endpoint for the search bar.

| **Invenio RDM Default Value** | `'/search'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L133) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### THEME_SETTINGS_TEMPLATE

Template which all settings templates in Invenio-Theme all extends from.

Defaults to value of :const:`SETTINGS_TEMPLATE`.

| **Invenio RDM Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L74) |

---


### **\*THEME_SHOW_FRONTPAGE_INTRO_SECTION**

Front page intro section visibility

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L326) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*THEME_SITENAME**

The name of the site to be used on the header and as a title.

| **Invenio RDM Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L136); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L320) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### THEME_SITEURL
| **Invenio RDM Default Value** | `'http://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L71) |

---


### **\*THEME_TRACKINGCODE_TEMPLATE**

Template for including a tracking code for web analytics.

The default template does not include any tracking code.

| **Invenio RDM Default Value** | `'invenio_theme/trackingcode.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L56) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### THEME_TWITTERHANDLE

Twitter handle.

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L323) |

---


### TRAP_BAD_REQUEST_ERRORS
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---


### TRAP_HTTP_EXCEPTIONS
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### **\*TRUSTED_HOSTS**

A list of host/domain names that can be served.

This is a security measure to prevent HTTP Host header attacks, which are
possible even under many seemingly-safe web server configurations.

By default all hosts are allowed. Values in this list can be fully qualified
names (e.g. 'www.example.com'). The validation only applies to
``request.host``.

In addition to this configuration variable, you should make sure that your
web server does not route requests to the application with an invalid Host
header.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L168); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L201) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### TYPE_CHECKING
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### USERPROFILES

Enable or disable module extensions.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L6) |

---


### USERPROFILES_BASE_TEMPLATE

Base templates for user profile module.

| **Invenio RDM Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L21) |

---


### USERPROFILES_EMAIL_ENABLED

Include the user email in the profile form.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L9) |

---


### USERPROFILES_EXTEND_SECURITY_FORMS

Extend the Invenio-Accounts user registration forms.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L12); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L415) |

---


### USERPROFILES_PROFILE_TEMPLATE

Default profile template.

| **Invenio RDM Default Value** | `'invenio_userprofiles/settings/profile.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L15) |

---


### USERPROFILES_PROFILE_URL

Default profile URL endpoint.

| **Invenio RDM Default Value** | `'/account/settings/profile/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L18) |

---


### **\*USERPROFILES_READ_ONLY**

Make the user profiles read-only.

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L27) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters), [`configure_einfra_oidc`](reference/index.md#oarepo_config.configure_einfra_oidc) |

---


### USERPROFILES_SETTINGS_TEMPLATE

Settings base templates for user profile module.

| **Invenio RDM Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L24) |

---


### USERS_RESOURCES_AVATAR_COLORS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L16) |

```
['#e06055',
 '#ff8a65',
 '#e91e63',
 '#f06292',
 '#673ab7',
 '#ba68c8',
 '#7986cb',
 '#3f51b5',
 '#5e97f6',
 '#00a4e4',
 '#4dd0e1',
 '#0097a7',
 '#d4e157',
 '#aed581',
 '#57bb8a',
 '#4db6ac',
 '#607d8b',
 '#795548',
 '#a1887f',
 '#fdd835',
 '#a3a3a3',
 '#556c60',
 '#605264',
 '#923035',
 '#915a30',
 '#55526f',
 '#67635a']
```

---


### USERS_RESOURCES_DOMAINS_ORG_SCHEMA

Domains organisation schema config.

| **Invenio RDM Default Value** | `OrgPropsSchema` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L306) |

---


### USERS_RESOURCES_DOMAINS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L144) |

```
{'sort': ['bestmatch',
          'domain',
          'newest',
          'oldest',
          'updated',
          'num-users',
          'num-active',
          'num-inactive',
          'num-confirmed',
          'num-verified',
          'num-blocked'],
 'facets': ['status', 'flagged', 'category', 'organisation', 'tld']}
```

---


### USERS_RESOURCES_DOMAINS_SEARCH_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L210) |

```
{'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'status'}},
 'flagged': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
             'ui': {'field': 'flagged'}},
 'category': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
              'ui': {'field': 'category'}},
 'organisation': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                  'ui': {'field': 'organisation'}},
 'tld': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
         'ui': {'field': 'tld'}}}
```

---


### USERS_RESOURCES_DOMAINS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L162) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'domain': {'title': l'Domain', 'fields': ['domain', '-created']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']},
 'updated': {'title': l'Recently updated', 'fields': ['-updated']},
 'num-users': {'title': l'# Users', 'fields': ['-num_users']},
 'num-active': {'title': l'# Active', 'fields': ['-num_active']},
 'num-inactive': {'title': l'# Inactive', 'fields': ['-num_inactive']},
 'num-confirmed': {'title': l'# Confirmed', 'fields': ['-num_confirmed']},
 'num-verified': {'title': l'# Verified', 'fields': ['-num_verified']},
 'num-blocked': {'title': l'# Blocked', 'fields': ['-num_blocked']}}
```

---


### USERS_RESOURCES_GROUPS_ADMIN_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L274) |

```
{'is_managed': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                'ui': {'field': 'is_managed'}}}
```

---


### USERS_RESOURCES_GROUPS_ADMIN_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L268) |

```
{'sort': ['bestmatch', 'name', 'name_desc', 'managed', 'unmanaged'],
 'facets': ['is_managed']}
```

---


### USERS_RESOURCES_GROUPS_ADMIN_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L244) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'name': {'title': l'Name (A-Z)', 'fields': ['name.keyword']},
 'name_desc': {'title': l'Name (Z-A)', 'fields': ['-name.keyword']},
 'managed': {'title': l'Managed first', 'fields': ['-is_managed', 'name.keyword']},
 'unmanaged': {'title': l'Unmanaged first', 'fields': ['is_managed', 'name.keyword']}}
```

---


### USERS_RESOURCES_GROUPS_ENABLED

Config to enable features related to existence of groups.

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L309) |

---


### USERS_RESOURCES_MODERATION_LOCK_DEFAULT_TIMEOUT

Default timeout, in seconds, to lock a user when moderating.

| **Invenio RDM Default Value** | `30` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L137) |

---


### USERS_RESOURCES_MODERATION_LOCK_RENEWAL_TIMEOUT

Renewal timeout, in seconds, to increase the lock time for a user when moderating.

| **Invenio RDM Default Value** | `120` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L140) |

---


### USERS_RESOURCES_PROTECTED_GROUP_NAMES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L284) |

```
['admin', 'administration', 'superuser-access', 'administration-moderation']
```

---


### USERS_RESOURCES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L49) |

```
{'sort': ['bestmatch', 'username', 'email', 'domain', 'newest', 'oldest', 'updated'],
 'facets': ['status', 'visibility', 'domain_status', 'domain', 'affiliations', 'roles']}
```

---


### USERS_RESOURCES_SEARCH_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L94) |

```
{'domain': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'domain'}},
 'domain_status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                   'ui': {'field': 'domain_status'}},
 'affiliations': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                  'ui': {'field': 'profile.affiliations.keyword'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
            'ui': {'field': 'status'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
                'ui': {'field': 'visibility'}},
 'roles': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object>,
           'facet_options': {'size': 100},
           'ui': {'field': 'roles'}}}
```

---


### USERS_RESOURCES_SERVICE_SCHEMA

Schema used by the users service.

| **Invenio RDM Default Value** | `NotificationsUserSchema` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1501); [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L46) |

---


### USERS_RESOURCES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L62) |

```
{'bestmatch': {'title': l'Best match', 'fields': ['_score']},
 'username': {'title': l'Username', 'fields': ['username.keyword', '-created']},
 'email': {'title': l'Email', 'fields': ['email_hidden', '-created']},
 'domain': {'title': l'Domain', 'fields': ['domain', '-created']},
 'newest': {'title': l'Newest', 'fields': ['-created']},
 'oldest': {'title': l'Oldest', 'fields': ['created']},
 'updated': {'title': l'Recently updated', 'fields': ['-updated']}}
```

---


### USER_DASHBOARD_MENU_OVERRIDES

Overrides for "dashboard" menu.

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1528) |

```
{}
```

---


### USE_X_SENDFILE
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---


### VCS_TEMPLATE_INDEX
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-index.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1606) |

---


### VCS_TEMPLATE_INDEX_ITEM
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-index-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1607) |

---


### VCS_TEMPLATE_RELEASE_ITEM
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-release-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1610) |

---


### VCS_TEMPLATE_REPO_SWITCH
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-repo-switch.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1609) |

---


### VCS_TEMPLATE_VIEW
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-view.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1608) |

---


### VOCABULARIES_AFFILIATIONS_EDMO_COUNTRY_MAPPING
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L231) |

```
{'Cape Verde': 'Cabo Verde'}
```

---


### **\*VOCABULARIES_AFFILIATION_SCHEMES**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L61) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'grid': {'label': l'GRID', 'validator': <function <lambda>>},
 'gnd': {'label': l'GND', 'validator': <function is_gnd>},
 'isni': {'label': l'ISNI', 'validator': <function is_isni>},
 'ror': {'label': l'ROR', 'validator': <function is_ror>},
 'pic': {'label': l'PIC', 'validator': <function is_pic>},
 'edmo': {'label': l'EDMO', 'validator': <function is_edmo>}}
```

---


### VOCABULARIES_AWARDS_EC_ROR_ID

ROR ID for EC funder.

| **Invenio RDM Default Value** | `'00k4n6c32'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L149) |

---


### VOCABULARIES_AWARDS_OPENAIRE_FUNDERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L83) |

```
{'aka_________': '05k73zm37',
 'anr_________': '00rbzpz17',
 'arc_________': '05mmh0f86',
 'asap________': '03zj4c476',
 'cihr________': '01gavpb45',
 'corda_______': '00k4n6c32',
 'corda_____he': '00k4n6c32',
 'corda__h2020': '00k4n6c32',
 'euenvagency_': '02k4b9v70',
 'fct_________': '00snfqn58',
 'fwf_________': '013tf3c58',
 'inca________': '03m8vkq32',
 'irb_hr______': '03n51vw80',
 'lcs_________': '02ar66p97',
 'mestd_______': '01znas443',
 'nhmrc_______': '011kf5r70',
 'nih_________': '01cwqze88',
 'nserc_______': '01h531d29',
 'nsf_________': '021nxhr62',
 'nwo_________': '04jsz6e67',
 'rcuk________': '00dq2kk65',
 'sfi_________': '0271asj38',
 'snsf________': '00yjd3n13',
 'sshrc_______': '006cvnv84',
 'tubitakf____': '04w9kkr77',
 'twcf________': '00x0z1472',
 'ukri________': '001aqnf71',
 'wt__________': '029chgv08',
 'cf__________': '01kpjmx04',
 'fcf_________': '027xav248',
 'ibf_________': '04jsz6e67',
 '501100011626': '04q0a4f84',
 'erasmusplus_': '00k4n6c32',
 'dfgf________': '018mejw64',
 'drf_________': '004j3q729',
 'fmf_________': '0593mby10',
 'hsf_________': '05tdna171',
 'irfd________': '05svhj534',
 'kaute_______': '00zwv5854',
 'kf__________': '05jwty529',
 'lf__________': '03hz8wd80',
 'mtnf________': '047egay20',
 'nnf_________': '04txyc737',
 'pf__________': '048e7gn38',
 'pnf_________': '009vp0837',
 'rcn_________': '00epmv149',
 'rif_________': '00en9ce74',
 'sslf________': '04a31ep84',
 've__________': '05nqkay65',
 'vf__________': '013w1n936',
 '501100001581': '02dd61a62',
 '501100001635': '00a0n9e72',
 'mvt_________': '019pxzh98',
 '100012733___': '03xkf7525',
 '100015319___': '04bnxk453',
 '100022943___': '02g8v2v69',
 '501100001638': '04a1a1e81',
 'jaef________': '03vxy9y38',
 '100019637___': '003mr9q86',
 '501100001630': '051sx6d27',
 '100013433___': '054tsxk98',
 '501100001587': '04q0a4f84'}
```

---


### VOCABULARIES_AWARD_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L77) |

```
{'url': {'label': l'URL', 'validator': <function is_url>},
 'doi': {'label': l'DOI', 'validator': <function is_doi>}}
```

---


### VOCABULARIES_CF
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[]
```

---


### VOCABULARIES_CUSTOM_VOCABULARY_TYPES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L165) |

```
['names', 'affiliations', 'awards', 'funders', 'subjects']
```

---


### **\*VOCABULARIES_DATASTREAM_READERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L174); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L743) |
| **Set by** | [`configure_datastreams`](reference/index.md#oarepo_config.configure_datastreams), [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'csv': <class 'invenio_vocabularies.datastreams.readers.CSVReader'>,
 'json': <class 'invenio_vocabularies.datastreams.readers.JsonReader'>,
 'jsonl': <class 'invenio_vocabularies.datastreams.readers.JsonLinesReader'>,
 'gzip': <class 'invenio_vocabularies.datastreams.readers.GzipReader'>,
 'tar': <class 'invenio_vocabularies.datastreams.readers.TarReader'>,
 'http': <class 'invenio_vocabularies.datastreams.readers.SimpleHTTPReader'>,
 'rdf': <class 'invenio_vocabularies.datastreams.readers.RDFReader'>,
 'sparql': <class 'invenio_vocabularies.datastreams.readers.SPARQLReader'>,
 'yaml': <class 'invenio_vocabularies.datastreams.readers.YamlReader'>,
 'zip': <class 'invenio_vocabularies.datastreams.readers.ZipReader'>,
 'xml': <class 'invenio_vocabularies.datastreams.readers.XMLReader'>,
 'oai-pmh': <class 'invenio_vocabularies.datastreams.readers.OAIPMHReader'>}
```

---


### **\*VOCABULARIES_DATASTREAM_TRANSFORMERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L190); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L755) |
| **Set by** | [`configure_datastreams`](reference/index.md#oarepo_config.configure_datastreams), [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'xml': <class 'invenio_vocabularies.datastreams.transformers.XMLTransformer'>}
```

---


### **\*VOCABULARIES_DATASTREAM_WRITERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L195); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L767) |
| **Set by** | [`configure_datastreams`](reference/index.md#oarepo_config.configure_datastreams), [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'service': <class 'invenio_vocabularies.datastreams.writers.ServiceWriter'>,
 'yaml': <class 'invenio_vocabularies.datastreams.writers.YamlWriter'>,
 'async': <class 'invenio_vocabularies.datastreams.writers.AsyncWriter'>}
```

---


### VOCABULARIES_FACET_CACHE_SIZE
| **OARepo Default Value** | `2048` |
|--------------|-----------|
| **Type** | int |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L41) |

---


### VOCABULARIES_FACET_CACHE_TTL
| **OARepo Default Value** | `34560` |
|--------------|-----------|
| **Type** | int |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L42) |

---


### VOCABULARIES_FUNDER_DOI_PREFIX

DOI prefix for the identifier formed with the FundRef id.

| **Invenio RDM Default Value** | `'10.13039'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L74) |

---


### **\*VOCABULARIES_FUNDER_SCHEMES**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L68) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'grid': {'label': l'GRID', 'validator': <function <lambda>>},
 'gnd': {'label': l'GND', 'validator': <function is_gnd>},
 'isni': {'label': l'ISNI', 'validator': <function is_isni>},
 'ror': {'label': l'ROR', 'validator': <function is_ror>},
 'doi': {'label': l'DOI', 'validator': <function is_doi>}}
```

---


### VOCABULARIES_IDENTIFIER_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L38) |

```
{'grid': {'label': l'GRID', 'validator': <function <lambda>>},
 'gnd': {'label': l'GND', 'validator': <function is_gnd>},
 'isni': {'label': l'ISNI', 'validator': <function is_isni>},
 'ror': {'label': l'ROR', 'validator': <function is_ror>}}
```

---


### **\*VOCABULARIES_NAMES_SCHEMES**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L152) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

```
{'orcid': {'label': l'ORCID',
           'validator': <function is_orcid>,
           'datacite': 'ORCID'},
 'isni': {'label': l'ISNI',
          'validator': <function is_isni>,
          'datacite': 'ISNI'},
 'gnd': {'label': l'GND',
         'validator': <function is_gnd>,
         'datacite': 'GND'}}
```

---


### VOCABULARIES_ORCID_ACCESS_KEY

ORCID access key to access the s3 bucket.

| **Invenio RDM Default Value** | `'CHANGEME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L236) |

---


### VOCABULARIES_ORCID_ORG_IDS_MAPPING_PATH

Path to the CSV file for mapping ORCiD organization IDs to affiliation IDs.

The path can be specified as either an absolute path or a relative path within the
Flask app instance folder (i.e. ``current_app.instance_path``).

The CSV file should have the following columns:

- `org_scheme`: The ORCiD organization ID.
- `org_id`: The ORCiD organization ID.
- `aff_id`: The affiliation ID to map to.

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L249) |

---


### VOCABULARIES_ORCID_SECRET_KEY

ORCID secret key to access the s3 bucket.

| **Invenio RDM Default Value** | `'CHANGEME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L238) |

---


### VOCABULARIES_ORCID_SUMMARIES_BUCKET

ORCID summaries bucket name.

| **Invenio RDM Default Value** | `'v3.0-summaries'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L240) |

---


### VOCABULARIES_ORCID_SYNC_MAX_WORKERS

ORCID max number of simultaneous workers/connections.

| **Invenio RDM Default Value** | `32` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L242) |

---


### VOCABULARIES_ORCID_SYNC_SINCE
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L244) |

```
{'days': 1}
```

---


### **\*VOCABULARIES_RESOURCE_CONFIG**

Configure the resource.

| **Invenio RDM Default Value** | `VocabulariesResourceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L32) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### **\*VOCABULARIES_SERVICE_CONFIG**

Configure the service.

| **Invenio RDM Default Value** | `VocabulariesServiceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L35) |
| **Set by** | [`configure_generic_parameters`](reference/index.md#oarepo_config.configure_generic_parameters) |

---


### VOCABULARIES_SUBJECTS_EUROSCIVOC_FILE_URL

Subject EuroSciVoc file download link.

| **Invenio RDM Default Value** | `'https://publications.europa.eu/resource/distribution/euroscivoc/rdf/skos_ap_eu/EuroSciVoc-skos-ap-e...` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L220) |

---


### VOCABULARIES_SUBJECTS_GEMET_FILE_URL
| **Invenio RDM Default Value** | `'https://www.eionet.europa.eu/gemet/latest/gemet.rdf.gz'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L223) |

---


### VOCABULARIES_SUBJECTS_NVS_FILE_URL

Subject NVS-P02 file download link.

| **Invenio RDM Default Value** | `'http://vocab.nerc.ac.uk/collection/P02/current/?_profile=nvs&_mediatype=application/rdf+xml'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L228) |

---


### VOCABULARIES_SUBJECTS_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L159) |

```
{'gnd': {'label': l'GND',
         'validator': <function is_gnd>,
         'datacite': 'GND'},
 'url': {'label': l'URL', 'validator': <function is_url>}}
```

---


### VOCABULARIES_TYPES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L214) |

```
{'facets': [], 'sort': ['name', 'count']}
```

---


### VOCABULARIES_TYPES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L202) |

```
{'name': {'title': l'Name', 'fields': ['id']},
 'count': {'title': l'Number of entries', 'fields': ['count']}}
```

---


### VOCABULARY_TYPE_UI_RESOURCE
| **Default Value** | `'oarepo_vocabularies.ui.resources.vocabulary_type.resource:VocabularyTypeUIResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### VOCABULARY_TYPE_UI_RESOURCE_CONFIG
| **Default Value** | `'oarepo_vocabularies.ui.resources.vocabulary_type.config:VocabularyTypeUIResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### WEBPACKEXT_MANIFEST_PATH
| **Default Value** | `'dist/manifest.json'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### **\*WEBPACKEXT_NPM_PKG_CLS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L202) |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### **\*WEBPACKEXT_PROJECT**
| **Default Value** | `'oarepo_ui.webpack:project'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |
| **Set by** | [`configure_ui`](reference/index.md#oarepo_config.configure_ui) |

---


### WEBPACKEXT_PROJECT_BUILDDIR
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/assets'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### WEBPACKEXT_PROJECT_DISTDIR
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static/...` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### WEBPACKEXT_PROJECT_DISTURL
| **Default Value** | `'/static/dist'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---


### WORKFLOWS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{}
```

---


### WORKFLOWS_DEFAULT_WORKFLOW
| **Default Value** | `'individual'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

