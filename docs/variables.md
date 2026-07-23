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
| [`ACCESS_​ACTION_​CACHE_​PREFIX`](#access-action-cache-prefix) | str | - |
| [`ACCESS_​CACHE`](#access-cache) | NoneType | - |
| [`ACCESS_​LOAD_​SYSTEM_​ROLE_​NEEDS`](#access-load-system-role-needs) | bool | - |
| [`ACCOUNTS`](#accounts) | bool | - |
| [`ACCOUNTS_​BASE_​TEMPLATE`](#accounts-base-template) | str | - |
| [`ACCOUNTS_​CONFIRM_​EMAIL_​ENDPOINT`](#accounts-confirm-email-endpoint) | NoneType | - |
| [`ACCOUNTS_​COVER_​TEMPLATE`](#accounts-cover-template) | str | - |
| [`ACCOUNTS_​DEFAULT_​EMAIL_​VISIBILITY`](#accounts-default-email-visibility) | str | - |
| [`ACCOUNTS_​DEFAULT_​USERS_​VERIFIED`](#accounts-default-users-verified) | bool | - |
| [`ACCOUNTS_​DEFAULT_​USER_​VISIBILITY`](#accounts-default-user-visibility) | str | - |
| [`ACCOUNTS_​FORGOT_​PASSWORD_​EMAIL_​RATELIMIT`](#accounts-forgot-password-email-ratelimit) | NoneType | - |
| [`ACCOUNTS_​FORGOT_​PASSWORD_​EMAIL_​RATELIMIT_​KEY_​PREFIX`](#accounts-forgot-password-email-ratelimit-key-prefix) | str | - |
| [`ACCOUNTS_​FORGOT_​PASSWORD_​EMAIL_​RATELIMIT_​MSG`](#accounts-forgot-password-email-ratelimit-msg) | LazyString | - |
| [`ACCOUNTS_​JWT_​ALOGORITHM`](#accounts-jwt-alogorithm) | str | - |
| [`ACCOUNTS_​JWT_​CREATION_​FACTORY`](#accounts-jwt-creation-factory) | str | - |
| [`ACCOUNTS_​JWT_​DECODE_​FACTORY`](#accounts-jwt-decode-factory) | str | - |
| [`ACCOUNTS_​JWT_​DOM_​TOKEN`](#accounts-jwt-dom-token) | bool | - |
| [`ACCOUNTS_​JWT_​DOM_​TOKEN_​TEMPLATE`](#accounts-jwt-dom-token-template) | str | - |
| [`ACCOUNTS_​JWT_​ENABLE`](#accounts-jwt-enable) | bool | - |
| [`ACCOUNTS_​JWT_​EXPIRATION_​DELTA`](#accounts-jwt-expiration-delta) | timedelta | - |
| [`ACCOUNTS_​JWT_​SECRET_​KEY`](#accounts-jwt-secret-key) | str | - |
| [`ACCOUNTS_​LOCAL_​LOGIN_​ENABLED`](#accounts-local-login-enabled) | bool | `configure_generic_parameters` |
| [`ACCOUNTS_​LOGIN_​RATELIMIT`](#accounts-login-ratelimit) | NoneType | - |
| [`ACCOUNTS_​LOGIN_​RATELIMIT_​KEY_​PREFIX`](#accounts-login-ratelimit-key-prefix) | str | - |
| [`ACCOUNTS_​LOGIN_​RATELIMIT_​MSG`](#accounts-login-ratelimit-msg) | LazyString | - |
| [`ACCOUNTS_​LOGIN_​VIEW_​FUNCTION`](#accounts-login-view-function) | unknown | `configure_generic_parameters` |
| [`ACCOUNTS_​REGISTER_​BLUEPRINT`](#accounts-register-blueprint) | NoneType | - |
| [`ACCOUNTS_​RESET_​PASSWORD_​ENDPOINT`](#accounts-reset-password-endpoint) | NoneType | - |
| [`ACCOUNTS_​REST_​AUTH_​VIEWS`](#accounts-rest-auth-views) | dict | - |
| [`ACCOUNTS_​REST_​CONFIRM_​EMAIL_​ENDPOINT`](#accounts-rest-confirm-email-endpoint) | str | - |
| [`ACCOUNTS_​REST_​RESET_​PASSWORD_​ENDPOINT`](#accounts-rest-reset-password-endpoint) | str | - |
| [`ACCOUNTS_​RETENTION_​PERIOD`](#accounts-retention-period) | timedelta | - |
| [`ACCOUNTS_​SEND_​CONFIRMATION_​RATELIMIT`](#accounts-send-confirmation-ratelimit) | NoneType | - |
| [`ACCOUNTS_​SEND_​CONFIRMATION_​RATELIMIT_​KEY_​PREFIX`](#accounts-send-confirmation-ratelimit-key-prefix) | str | - |
| [`ACCOUNTS_​SEND_​CONFIRMATION_​RATELIMIT_​MSG`](#accounts-send-confirmation-ratelimit-msg) | LazyString | - |
| [`ACCOUNTS_​SESSION_​ACTIVITY_​ENABLED`](#accounts-session-activity-enabled) | bool | - |
| [`ACCOUNTS_​SESSION_​REDIS_​URL`](#accounts-session-redis-url) | NoneType | `configure_generic_parameters` |
| [`ACCOUNTS_​SESSION_​STORE_​FACTORY`](#accounts-session-store-factory) | str | - |
| [`ACCOUNTS_​SETTINGS_​SECURITY_​TEMPLATE`](#accounts-settings-security-template) | str | - |
| [`ACCOUNTS_​SETTINGS_​TEMPLATE`](#accounts-settings-template) | str | - |
| [`ACCOUNTS_​SITENAME`](#accounts-sitename) | LazyString | - |
| [`ACCOUNTS_​USERINFO_​HEADERS`](#accounts-userinfo-headers) | bool | - |
| [`ACCOUNTS_​USERNAME_​REGEX`](#accounts-username-regex) | str | - |
| [`ACCOUNTS_​USERNAME_​RULES_​TEXT`](#accounts-username-rules-text) | LazyString | - |
| [`ACCOUNTS_​USER_​PREFERENCES_​SCHEMA`](#accounts-user-preferences-schema) | UserPreferencesSchema | - |
| [`ACCOUNTS_​USER_​PROFILE_​SCHEMA`](#accounts-user-profile-schema) | UserProfileSchema | - |
| [`ACCOUNTS_​USE_​CELERY`](#accounts-use-celery) | bool | - |
| [`ADMINISTRATION_​APPNAME`](#administration-appname) | str | - |
| [`ADMINISTRATION_​BASE_​TEMPLATE`](#administration-base-template) | str | - |
| [`ADMINISTRATION_​DASHBOARD_​VIEW`](#administration-dashboard-view) | str | - |
| [`ADMINISTRATION_​DISPLAY_​VERSIONS`](#administration-display-versions) | list | - |
| [`ADMINISTRATION_​THEME_​BASE_​TEMPLATE`](#administration-theme-base-template) | str | `configure_ui` |
| [`ADMIN_​BASE_​TEMPLATE`](#admin-base-template) | str | - |
| [`ALEMBIC`](#alembic) | dict | - |
| [`ALEMBIC_​CONTEXT`](#alembic-context) | dict | - |
| [`ALLOWED_​HTML_​ATTRS`](#allowed-html-attrs) | dict | - |
| [`ALLOWED_​HTML_​TAGS`](#allowed-html-tags) | list | - |
| [`APPLICATION_​ROOT`](#application-root) | str | - |
| [`APP_​ALLOWED_​HOSTS`](#app-allowed-hosts) | configured by function | `configure_generic_parameters` |
| [`APP_​DEFAULT_​SECURE_​HEADERS`](#app-default-secure-headers) | dict | `configure_ui`, `configure_generic_parameters` |
| [`APP_​ENABLE_​SECURE_​HEADERS`](#app-enable-secure-headers) | bool | - |
| [`APP_​HEALTH_​BLUEPRINT_​ENABLED`](#app-health-blueprint-enabled) | bool | - |
| [`APP_​LOGS_​PERMISSION_​POLICY`](#app-logs-permission-policy) | unknown | `configure_jobs` |
| [`APP_​RDM_​ADMIN_​EMAIL_​RECIPIENT`](#app-rdm-admin-email-recipient) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​AUTOCOMPLETE_​NAMES`](#app-rdm-deposit-form-autocomplete-names) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​CUSTOM_​FIELD_​DEFAULTS`](#app-rdm-deposit-form-custom-field-defaults) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​DEFAULTS`](#app-rdm-deposit-form-defaults) | dict | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​PUBLISH_​MODAL_​EXTRA`](#app-rdm-deposit-form-publish-modal-extra) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​FORM_​QUOTA`](#app-rdm-deposit-form-quota) | unknown | `configure_generic_parameters` |
| [`APP_​RDM_​DEPOSIT_​FORM_​TEMPLATE`](#app-rdm-deposit-form-template) | unknown | - |
| [`APP_​RDM_​DEPOSIT_​NG_​FILES_​UI_​ENABLED`](#app-rdm-deposit-ng-files-ui-enabled) | unknown | `configure_ui` |
| [`APP_​RDM_​DETAIL_​SIDE_​BAR_​TEMPLATES`](#app-rdm-detail-side-bar-templates) | unknown | `configure_ui` |
| [`APP_​RDM_​DISPLAY_​DECIMAL_​FILE_​SIZES`](#app-rdm-display-decimal-file-sizes) | unknown | - |
| [`APP_​RDM_​FILES_​INTEGRITY_​REPORT_​SUBJECT`](#app-rdm-files-integrity-report-subject) | unknown | - |
| [`APP_​RDM_​FILES_​INTEGRITY_​REPORT_​TEMPLATE`](#app-rdm-files-integrity-report-template) | unknown | - |
| [`APP_​RDM_​IDENTIFIER_​SCHEMES_​UI`](#app-rdm-identifier-schemes-ui) | unknown | `configure_generic_parameters` |
| [`APP_​RDM_​MODERATION_​REQUEST_​FACETS`](#app-rdm-moderation-request-facets) | dict | - |
| [`APP_​RDM_​MODERATION_​REQUEST_​SEARCH`](#app-rdm-moderation-request-search) | dict | - |
| [`APP_​RDM_​MODERATION_​REQUEST_​SORT_​OPTIONS`](#app-rdm-moderation-request-sort-options) | dict | - |
| [`APP_​RDM_​PAGES`](#app-rdm-pages) | unknown | - |
| [`APP_​RDM_​RECORDS_​EXPORT_​URL`](#app-rdm-records-export-url) | unknown | - |
| [`APP_​RDM_​RECORD_​EXPORTERS`](#app-rdm-record-exporters) | unknown | - |
| [`APP_​RDM_​RECORD_​LANDING_​PAGE_​EXTERNAL_​LINKS`](#app-rdm-record-landing-page-external-links) | list | - |
| [`APP_​RDM_​RECORD_​LANDING_​PAGE_​FAIR_​SIGNPOSTING_​LEVEL_​1_​ENABLED`](#app-rdm-record-landing-page-fair-signposting-level-1-enabled) | unknown | - |
| [`APP_​RDM_​RECORD_​LANDING_​PAGE_​TEMPLATE`](#app-rdm-record-landing-page-template) | str | - |
| [`APP_​RDM_​RECORD_​THUMBNAIL_​SIZES`](#app-rdm-record-thumbnail-sizes) | unknown | - |
| [`APP_​RDM_​ROUTES`](#app-rdm-routes) | dict | - |
| [`APP_​RDM_​SUBCOMMUNITIES_​LABEL`](#app-rdm-subcommunities-label) | unknown | - |
| [`APP_​RDM_​USER_​DASHBOARD_​ROUTES`](#app-rdm-user-dashboard-routes) | dict | - |
| [`APP_​REQUESTID_​HEADER`](#app-requestid-header) | str | - |
| [`APP_​THEME`](#app-theme) | NoneType | `configure_ui` |
| [`ASSETS_​BUILDER`](#assets-builder) | configured by function | `configure_ui` |
| [`AUDIT_​LOGS_​DISABLED_​ACTIONS`](#audit-logs-disabled-actions) | set | - |
| [`AUDIT_​LOGS_​ENABLED`](#audit-logs-enabled) | bool | - |
| [`AUDIT_​LOGS_​FACETS`](#audit-logs-facets) | dict | - |
| [`AUDIT_​LOGS_​SEARCH`](#audit-logs-search) | dict | - |
| [`AUDIT_​LOGS_​SORT_​OPTIONS`](#audit-logs-sort-options) | dict | - |
| [`BABEL_​DEFAULT_​LOCALE`](#babel-default-locale) | str | `configure_generic_parameters` |
| [`BABEL_​DEFAULT_​TIMEZONE`](#babel-default-timezone) | unknown | `configure_generic_parameters` |
| [`BANNERS_​CATEGORIES`](#banners-categories) | list | - |
| [`BANNERS_​CATEGORIES_​TO_​STYLE`](#banners-categories-to-style) | unknown | - |
| [`BANNERS_​SEARCH`](#banners-search) | dict | - |
| [`BANNERS_​SORT_​OPTIONS`](#banners-sort-options) | dict | - |
| [`BASE_​TEMPLATE`](#base-template) | str | `configure_ui` |
| [`BROKER_​URL`](#broker-url) | str | `configure_generic_parameters` |
| [`CACHE_​IS_​AUTHENTICATED_​CALLBACK`](#cache-is-authenticated-callback) | NoneType | - |
| [`CACHE_​KEY_​PREFIX`](#cache-key-prefix) | str | - |
| [`CACHE_​REDIS_​URL`](#cache-redis-url) | str | `configure_generic_parameters` |
| [`CACHE_​TYPE`](#cache-type) | str | - |
| [`CELERY_​ACCEPT_​CONTENT`](#celery-accept-content) | list | - |
| [`CELERY_​BEAT_​SCHEDULE`](#celery-beat-schedule) | unknown | `configure_cron` |
| [`CELERY_​BROKER_​URL`](#celery-broker-url) | str | `configure_generic_parameters` |
| [`CELERY_​RESULT_​BACKEND`](#celery-result-backend) | str | `configure_generic_parameters` |
| [`CELERY_​RESULT_​SERIALIZER`](#celery-result-serializer) | str | - |
| [`CELERY_​TASK_​SERIALIZER`](#celery-task-serializer) | str | - |
| [`CHECKS_​COMMUNITIES_​SERVICE_​COMPONENTS`](#checks-communities-service-components) | unknown | - |
| [`CHECKS_​ENABLED`](#checks-enabled) | bool | `configure_llm` |
| [`CHECKS_​GENERIC_​COMMUNITY`](#checks-generic-community) | str | `configure_llm` |
| [`COLLECTIONS_​MAX_​COLLECTIONS_​PER_​TREE`](#collections-max-collections-per-tree) | int | - |
| [`COLLECTIONS_​MAX_​DEPTH`](#collections-max-depth) | int | - |
| [`COLLECTIONS_​MAX_​TREES`](#collections-max-trees) | int | - |
| [`COLLECTIONS_​PERMISSION_​POLICY`](#collections-permission-policy) | unknown | - |
| [`COLLECT_​STATIC_​ROOT`](#collect-static-root) | str | - |
| [`COLLECT_​STORAGE`](#collect-storage) | str | `configure_generic_parameters` |
| [`COMMUNITIES_​ALLOW_​MEMBERSHIP_​REQUESTS`](#communities-allow-membership-requests) | bool | - |
| [`COMMUNITIES_​ALLOW_​RESTRICTED`](#communities-allow-restricted) | bool | - |
| [`COMMUNITIES_​ALWAYS_​SHOW_​CREATE_​LINK`](#communities-always-show-create-link) | bool | - |
| [`COMMUNITIES_​COLLECTIONS_​ENABLED`](#communities-collections-enabled) | bool | - |
| [`COMMUNITIES_​CUSTOM_​FIELDS`](#communities-custom-fields) | list | - |
| [`COMMUNITIES_​CUSTOM_​FIELDS_​UI`](#communities-custom-fields-ui) | list | - |
| [`COMMUNITIES_​DEFAULT_​RECORD_​SUBMISSION_​POLICY`](#communities-default-record-submission-policy) | RecordSubmissionPolicyEnum | - |
| [`COMMUNITIES_​ERROR_​HANDLERS`](#communities-error-handlers) | unknown | - |
| [`COMMUNITIES_​FACETS`](#communities-facets) | dict | - |
| [`COMMUNITIES_​IDENTITIES_​CACHE_​HANDLER`](#communities-identities-cache-handler) | str | - |
| [`COMMUNITIES_​IDENTITIES_​CACHE_​REDIS_​URL`](#communities-identities-cache-redis-url) | str | `configure_generic_parameters` |
| [`COMMUNITIES_​IDENTITIES_​CACHE_​TIME`](#communities-identities-cache-time) | int | - |
| [`COMMUNITIES_​INVITATIONS_​EXPIRES_​IN`](#communities-invitations-expires-in) | timedelta | - |
| [`COMMUNITIES_​INVITATIONS_​SEARCH`](#communities-invitations-search) | dict | - |
| [`COMMUNITIES_​INVITATIONS_​SORT_​OPTIONS`](#communities-invitations-sort-options) | dict | - |
| [`COMMUNITIES_​LOGO_​MAX_​FILE_​SIZE`](#communities-logo-max-file-size) | int | - |
| [`COMMUNITIES_​MEMBERSHIP_​REQUESTS_​EXPIRES_​IN`](#communities-membership-requests-expires-in) | timedelta | - |
| [`COMMUNITIES_​MEMBERSHIP_​REQUESTS_​FACETS`](#communities-membership-requests-facets) | dict | - |
| [`COMMUNITIES_​MEMBERSHIP_​REQUESTS_​SEARCH`](#communities-membership-requests-search) | dict | - |
| [`COMMUNITIES_​MEMBERS_​FACETS`](#communities-members-facets) | dict | - |
| [`COMMUNITIES_​MEMBERS_​SEARCH`](#communities-members-search) | dict | - |
| [`COMMUNITIES_​MEMBERS_​SERVICE_​COMPONENTS`](#communities-members-service-components) | list | - |
| [`COMMUNITIES_​MEMBERS_​SORT_​OPTIONS`](#communities-members-sort-options) | dict | - |
| [`COMMUNITIES_​NAMESPACES`](#communities-namespaces) | dict | - |
| [`COMMUNITIES_​OAI_​SETS_​PREFIX`](#communities-oai-sets-prefix) | str | - |
| [`COMMUNITIES_​PERMISSION_​POLICY`](#communities-permission-policy) | configured by function | `configure_communities` |
| [`COMMUNITIES_​RECORDS_​SEARCH`](#communities-records-search) | unknown | - |
| [`COMMUNITIES_​RECORDS_​SEARCH_​ALL`](#communities-records-search-all) | bool | - |
| [`COMMUNITIES_​REGISTER_​UI_​BLUEPRINT`](#communities-register-ui-blueprint) | configured by function | `configure_communities` |
| [`COMMUNITIES_​REQUESTS_​SEARCH`](#communities-requests-search) | dict | - |
| [`COMMUNITIES_​ROLES`](#communities-roles) | list | `configure_communities` |
| [`COMMUNITIES_​ROUTES`](#communities-routes) | dict | - |
| [`COMMUNITIES_​SEARCH`](#communities-search) | dict | - |
| [`COMMUNITIES_​SEARCH_​SORT_​BY_​VERIFIED`](#communities-search-sort-by-verified) | bool | - |
| [`COMMUNITIES_​SERVICE_​COMPONENTS`](#communities-service-components) | list | - |
| [`COMMUNITIES_​SORT_​OPTIONS`](#communities-sort-options) | dict | - |
| [`COMMUNITIES_​SUBCOMMUNITIES_​FACETS`](#communities-subcommunities-facets) | dict | - |
| [`COMMUNITIES_​SUBCOMMUNITIES_​SEARCH`](#communities-subcommunities-search) | dict | - |
| [`COMMUNITIES_​SUB_​INVITATION_​REQUEST_​CLS`](#communities-sub-invitation-request-cls) | unknown | - |
| [`COMMUNITIES_​SUB_​REQUEST_​CLS`](#communities-sub-request-cls) | unknown | - |
| [`CORS_​EXPOSE_​HEADERS`](#cors-expose-headers) | unknown | - |
| [`CORS_​RESOURCES`](#cors-resources) | unknown | - |
| [`CORS_​SEND_​WILDCARD`](#cors-send-wildcard) | unknown | - |
| [`COVER_​TEMPLATE`](#cover-template) | str | `configure_ui` |
| [`CROSSREF_​ADDITIONAL_​PREFIXES`](#crossref-additional-prefixes) | list | - |
| [`CROSSREF_​DEPOSITOR`](#crossref-depositor) | str | - |
| [`CROSSREF_​EMAIL`](#crossref-email) | str | - |
| [`CROSSREF_​ENABLED`](#crossref-enabled) | bool | - |
| [`CROSSREF_​FORMAT`](#crossref-format) | str | - |
| [`CROSSREF_​PASSWORD`](#crossref-password) | str | - |
| [`CROSSREF_​PREFIX`](#crossref-prefix) | str | - |
| [`CROSSREF_​REGISTRANT`](#crossref-registrant) | str | - |
| [`CROSSREF_​TEST_​MODE`](#crossref-test-mode) | bool | - |
| [`CROSSREF_​URL`](#crossref-url) | str | - |
| [`CROSSREF_​USERNAME`](#crossref-username) | str | - |
| [`CSRF_​ALLOWED_​CHARS`](#csrf-allowed-chars) | str | - |
| [`CSRF_​COOKIE_​NAME`](#csrf-cookie-name) | str | - |
| [`CSRF_​COOKIE_​SAMESITE`](#csrf-cookie-samesite) | str | - |
| [`CSRF_​FORCE_​SECURE_​REFERER`](#csrf-force-secure-referer) | bool | - |
| [`CSRF_​HEADER`](#csrf-header) | str | - |
| [`CSRF_​METHODS`](#csrf-methods) | list | - |
| [`CSRF_​SECRET_​SALT`](#csrf-secret-salt) | str | - |
| [`CSRF_​TOKEN_​EXPIRES_​IN`](#csrf-token-expires-in) | int | - |
| [`CSRF_​TOKEN_​GRACE_​PERIOD`](#csrf-token-grace-period) | int | - |
| [`CSRF_​TOKEN_​LENGTH`](#csrf-token-length) | int | - |
| [`DASHBOARD_​RECORD_​CREATE_​URL`](#dashboard-record-create-url) | configured by function | `configure_ui`, `configure_generic_parameters` |
| [`DATACITE_​ADDITIONAL_​PREFIXES`](#datacite-additional-prefixes) | list | - |
| [`DATACITE_​DATACENTER_​SYMBOL`](#datacite-datacenter-symbol) | str | - |
| [`DATACITE_​ENABLED`](#datacite-enabled) | bool | - |
| [`DATACITE_​FORMAT`](#datacite-format) | str | - |
| [`DATACITE_​PASSWORD`](#datacite-password) | str | - |
| [`DATACITE_​PREFIX`](#datacite-prefix) | str | - |
| [`DATACITE_​TEST_​MODE`](#datacite-test-mode) | bool | `configure_generic_parameters` |
| [`DATACITE_​URL`](#datacite-url) | str | - |
| [`DATACITE_​USERNAME`](#datacite-username) | str | - |
| [`DB_​VERSIONING`](#db-versioning) | bool | - |
| [`DB_​VERSIONING_​USER_​MODEL`](#db-versioning-user-model) | unknown | - |
| [`DEBUG`](#debug) | bool | - |
| [`DEBUG_​TB_​INTERCEPT_​REDIRECTS`](#debug-tb-intercept-redirects) | unknown | - |
| [`DEFAULT_​COMMUNITIES_​CUSTOM_​FIELDS`](#default-communities-custom-fields) | list | - |
| [`DEFAULT_​COMMUNITIES_​CUSTOM_​FIELDS_​UI`](#default-communities-custom-fields-ui) | list | - |
| [`DEFAULT_​WORKFLOW_​EVENTS`](#default-workflow-events) | dict | - |
| [`DEPLOYMENT_​VERSION`](#deployment-version) | configured by function | `configure_ui` |
| [`DISPLAY_​NEW_​COMMUNITIES`](#display-new-communities) | bool | - |
| [`DISPLAY_​USER_​COMMUNITIES`](#display-user-communities) | bool | - |
| [`DOI_​SETTINGS_​FACETS`](#doi-settings-facets) | dict | - |
| [`DOI_​SETTINGS_​SEARCH`](#doi-settings-search) | dict | - |
| [`DOI_​SETTINGS_​SORT_​OPTIONS`](#doi-settings-sort-options) | dict | - |
| [`EINFRA`](#einfra) | configured by function | `configure_einfra_oidc` |
| [`EINFRA_​API_​URL`](#einfra-api-url) | str | - |
| [`EINFRA_​CAPABILITIES_​ATTRIBUTE_​NAME`](#einfra-capabilities-attribute-name) | str | - |
| [`EINFRA_​COMMUNITY_​INVITATION_​SYNCHRONIZATION`](#einfra-community-invitation-synchronization) | bool | - |
| [`EINFRA_​COMMUNITY_​MEMBER_​SYNCHRONIZATION`](#einfra-community-member-synchronization) | bool | - |
| [`EINFRA_​COMMUNITY_​SYNCHRONIZATION`](#einfra-community-synchronization) | bool | - |
| [`EINFRA_​DEFAULT_​INVITATION_​LANGUAGE`](#einfra-default-invitation-language) | str | - |
| [`EINFRA_​ENTITLEMENT_​NAMESPACES`](#einfra-entitlement-namespaces) | set | - |
| [`EINFRA_​ENTITLEMENT_​PREFIX`](#einfra-entitlement-prefix) | str | - |
| [`EINFRA_​LAST_​DUMP_​PATH`](#einfra-last-dump-path) | str | - |
| [`EINFRA_​LOGIN_​APP`](#einfra-login-app) | configured by function | `configure_einfra_oidc` |
| [`EINFRA_​RSA_​KEY`](#einfra-rsa-key) | bytes | - |
| [`EINFRA_​USER_​DISPLAY_​NAME_​ATTRIBUTE`](#einfra-user-display-name-attribute) | str | - |
| [`EINFRA_​USER_​ID_​DUMP_​ATTRIBUTE`](#einfra-user-id-dump-attribute) | str | - |
| [`EINFRA_​USER_​ID_​SEARCH_​ATTRIBUTE`](#einfra-user-id-search-attribute) | str | - |
| [`EINFRA_​USER_​ORGANIZATION_​ATTRIBUTE`](#einfra-user-organization-attribute) | str | - |
| [`EINFRA_​USER_​PREFERRED_​MAIL_​ATTRIBUTE`](#einfra-user-preferred-mail-attribute) | str | - |
| [`EXPLAIN_​TEMPLATE_​LOADING`](#explain-template-loading) | bool | - |
| [`FILES_​REST_​ALLOW_​RANGE_​REQUESTS`](#files-rest-allow-range-requests) | bool | - |
| [`FILES_​REST_​CHECKSUM_​VERIFICATION_​URI_​PREFIXES`](#files-rest-checksum-verification-uri-prefixes) | unknown | - |
| [`FILES_​REST_​DEFAULT_​MAX_​FILE_​SIZE`](#files-rest-default-max-file-size) | NoneType | - |
| [`FILES_​REST_​DEFAULT_​QUOTA_​SIZE`](#files-rest-default-quota-size) | NoneType | `configure_generic_parameters` |
| [`FILES_​REST_​DEFAULT_​STORAGE_​CLASS`](#files-rest-default-storage-class) | str | `configure_generic_parameters` |
| [`FILES_​REST_​FILE_​TAGS_​HEADER`](#files-rest-file-tags-header) | str | - |
| [`FILES_​REST_​FILE_​URI_​MAX_​LEN`](#files-rest-file-uri-max-len) | int | - |
| [`FILES_​REST_​MIN_​FILE_​SIZE`](#files-rest-min-file-size) | int | - |
| [`FILES_​REST_​MULTIPART_​CHUNKSIZE_​MAX`](#files-rest-multipart-chunksize-max) | int | - |
| [`FILES_​REST_​MULTIPART_​CHUNKSIZE_​MIN`](#files-rest-multipart-chunksize-min) | int | - |
| [`FILES_​REST_​MULTIPART_​EXPIRES`](#files-rest-multipart-expires) | timedelta | - |
| [`FILES_​REST_​MULTIPART_​MAX_​PARTS`](#files-rest-multipart-max-parts) | int | - |
| [`FILES_​REST_​MULTIPART_​PART_​FACTORIES`](#files-rest-multipart-part-factories) | list | - |
| [`FILES_​REST_​OBJECT_​KEY_​MAX_​LEN`](#files-rest-object-key-max-len) | int | - |
| [`FILES_​REST_​PERMISSION_​FACTORY`](#files-rest-permission-factory) | str | - |
| [`FILES_​REST_​SIZE_​LIMITERS`](#files-rest-size-limiters) | str | - |
| [`FILES_​REST_​STORAGE_​CLASS_​LIST`](#files-rest-storage-class-list) | dict | `configure_generic_parameters` |
| [`FILES_​REST_​STORAGE_​FACTORY`](#files-rest-storage-factory) | str | `configure_generic_parameters` |
| [`FILES_​REST_​STORAGE_​PATH_​DIMENSIONS`](#files-rest-storage-path-dimensions) | int | - |
| [`FILES_​REST_​STORAGE_​PATH_​SPLIT_​LENGTH`](#files-rest-storage-path-split-length) | int | - |
| [`FILES_​REST_​TASK_​WAIT_​INTERVAL`](#files-rest-task-wait-interval) | int | - |
| [`FILES_​REST_​TASK_​WAIT_​MAX_​SECONDS`](#files-rest-task-wait-max-seconds) | int | - |
| [`FILES_​REST_​UPLOAD_​FACTORIES`](#files-rest-upload-factories) | list | - |
| [`FILES_​REST_​XSENDFILE_​ENABLED`](#files-rest-xsendfile-enabled) | bool | - |
| [`FILES_​REST_​XSENDFILE_​RESPONSE_​FUNC`](#files-rest-xsendfile-response-func) | unknown | - |
| [`FORMATTER_​BADGES_​ALLOWED_​TITLES`](#formatter-badges-allowed-titles) | list | - |
| [`FORMATTER_​BADGES_​ENABLE`](#formatter-badges-enable) | bool | - |
| [`FORMATTER_​BADGES_​MAX_​CACHE_​AGE`](#formatter-badges-max-cache-age) | int | - |
| [`FORMATTER_​BADGES_​TITLE_​MAPPING`](#formatter-badges-title-mapping) | dict | - |
| [`GLOBAL_​SEARCH_​MODELS`](#global-search-models) | configured by function | `add_model` |
| [`HANDLE_​URL`](#handle-url) | str | - |
| [`HEADER_​TEMPLATE`](#header-template) | unknown | `configure_ui` |
| [`I18N_​DEFAULT_​REDIRECT_​ENDPOINT`](#i18n-default-redirect-endpoint) | NoneType | - |
| [`I18N_​JS_​DISTR_​EXCEPTIONAL_​PACKAGE_​MAP`](#i18n-js-distr-exceptional-package-map) | dict | - |
| [`I18N_​LANGUAGES`](#i18n-languages) | list | `configure_generic_parameters` |
| [`I18N_​SESSION_​KEY`](#i18n-session-key) | str | - |
| [`I18N_​SET_​LANGUAGE_​URL`](#i18n-set-language-url) | str | - |
| [`I18N_​TRANSIFEX_​JS_​RESOURCES_​MAP`](#i18n-transifex-js-resources-map) | dict | - |
| [`I18N_​TRANSLATIONS_​PATHS`](#i18n-translations-paths) | list | - |
| [`I18N_​USER_​LANG_​ATTR`](#i18n-user-lang-attr) | str | - |
| [`IIIF_​API_​DECORATOR_​HANDLER`](#iiif-api-decorator-handler) | unknown | - |
| [`IIIF_​API_​INFO_​RESPONSE_​SKELETON`](#iiif-api-info-response-skeleton) | dict | - |
| [`IIIF_​CACHE_​HANDLER`](#iiif-cache-handler) | str | - |
| [`IIIF_​CACHE_​IGNORE_​ERRORS`](#iiif-cache-ignore-errors) | bool | - |
| [`IIIF_​CACHE_​REDIS_​URL`](#iiif-cache-redis-url) | str | - |
| [`IIIF_​CACHE_​TIME`](#iiif-cache-time) | int | - |
| [`IIIF_​CONVERTERS`](#iiif-converters) | tuple | - |
| [`IIIF_​FORMATS`](#iiif-formats) | dict | - |
| [`IIIF_​FORMATS_​PIL_​MAP`](#iiif-formats-pil-map) | dict | - |
| [`IIIF_​GIF_​TEMP_​FOLDER_​PATH`](#iiif-gif-temp-folder-path) | str | - |
| [`IIIF_​MODE`](#iiif-mode) | dict | - |
| [`IIIF_​PREVIEW_​TEMPLATE`](#iiif-preview-template) | str | - |
| [`IIIF_​QUALITIES`](#iiif-qualities) | tuple | - |
| [`IIIF_​SIMPLE_​PREVIEWER_​NATIVE_​EXTENSIONS`](#iiif-simple-previewer-native-extensions) | list | - |
| [`IIIF_​SIMPLE_​PREVIEWER_​SIZE`](#iiif-simple-previewer-size) | str | - |
| [`IIIF_​TILES_​CONVERTER_​PARAMS`](#iiif-tiles-converter-params) | dict | - |
| [`IIIF_​TILES_​GENERATION_​ENABLED`](#iiif-tiles-generation-enabled) | bool | - |
| [`IIIF_​TILES_​STORAGE_​BASE_​PATH`](#iiif-tiles-storage-base-path) | str | - |
| [`IIIF_​TILES_​VALID_​EXTENSIONS`](#iiif-tiles-valid-extensions) | list | - |
| [`IIIF_​VALIDATIONS`](#iiif-validations) | dict | - |
| [`INDEXER_​BEFORE_​INDEX_​HOOKS`](#indexer-before-index-hooks) | list | - |
| [`INDEXER_​BULK_​REQUEST_​TIMEOUT`](#indexer-bulk-request-timeout) | int | - |
| [`INDEXER_​DEFAULT_​INDEX`](#indexer-default-index) | NoneType | - |
| [`INDEXER_​MAX_​BULK_​CONSUMERS`](#indexer-max-bulk-consumers) | int | - |
| [`INDEXER_​MQ_​EXCHANGE`](#indexer-mq-exchange) | unknown | - |
| [`INDEXER_​MQ_​PUBLISH_​KWARGS`](#indexer-mq-publish-kwargs) | dict | - |
| [`INDEXER_​MQ_​QUEUE`](#indexer-mq-queue) | unknown | - |
| [`INDEXER_​MQ_​ROUTING_​KEY`](#indexer-mq-routing-key) | str | - |
| [`INDEXER_​RECORD_​TO_​INDEX`](#indexer-record-to-index) | str | - |
| [`INDEXER_​REPLACE_​REFS`](#indexer-replace-refs) | bool | - |
| [`INFO_​ENDPOINT_​COMPONENTS`](#info-endpoint-components) | list | - |
| [`INSTANCE_​THEME_​FILE`](#instance-theme-file) | configured by function | `configure_ui` |
| [`INVENIO_​CACHE_​TYPE`](#invenio-cache-type) | configured by function | `configure_generic_parameters` |
| [`INVENIO_​RDM_​ENABLED`](#invenio-rdm-enabled) | bool | - |
| [`INVENIO_​VOCABULARY_​TYPE_​METADATA`](#invenio-vocabulary-type-metadata) | dict | `configure_vocabulary` |
| [`JAVASCRIPT_​PACKAGES_​MANAGER`](#javascript-packages-manager) | configured by function | `configure_ui` |
| [`JOBS_​DEFAULT_​QUEUE`](#jobs-default-queue) | NoneType | - |
| [`JOBS_​FACETS`](#jobs-facets) | dict | - |
| [`JOBS_​LOGGING`](#jobs-logging) | bool | - |
| [`JOBS_​LOGGING_​INDEX`](#jobs-logging-index) | str | - |
| [`JOBS_​LOGGING_​LEVEL`](#jobs-logging-level) | str | `configure_jobs` |
| [`JOBS_​LOGGING_​RETENTION_​DAYS`](#jobs-logging-retention-days) | int | - |
| [`JOBS_​LOGS_​BATCH_​SIZE`](#jobs-logs-batch-size) | int | - |
| [`JOBS_​LOGS_​MAX_​RESULTS`](#jobs-logs-max-results) | int | - |
| [`JOBS_​PERMISSION_​POLICY`](#jobs-permission-policy) | unknown | - |
| [`JOBS_​QUEUES`](#jobs-queues) | dict | - |
| [`JOBS_​RUNS_​PERMISSION_​POLICY`](#jobs-runs-permission-policy) | unknown | - |
| [`JOBS_​SEARCH`](#jobs-search) | dict | - |
| [`JOBS_​SORT_​OPTIONS`](#jobs-sort-options) | dict | - |
| [`JOBS_​TASKS_​PERMISSION_​POLICY`](#jobs-tasks-permission-policy) | unknown | - |
| [`JSONSCHEMAS_​ENDPOINT`](#jsonschemas-endpoint) | str | - |
| [`JSONSCHEMAS_​HOST`](#jsonschemas-host) | str | `configure_generic_parameters` |
| [`JSONSCHEMAS_​LOADER_​CLS`](#jsonschemas-loader-cls) | NoneType | - |
| [`JSONSCHEMAS_​LOCAL_​REFRESOLVER_​URI_​SCHEME`](#jsonschemas-local-refresolver-uri-scheme) | str | - |
| [`JSONSCHEMAS_​REGISTER_​ENDPOINTS_​API`](#jsonschemas-register-endpoints-api) | bool | - |
| [`JSONSCHEMAS_​REGISTER_​ENDPOINTS_​UI`](#jsonschemas-register-endpoints-ui) | bool | - |
| [`JSONSCHEMAS_​REPLACE_​REFS`](#jsonschemas-replace-refs) | bool | - |
| [`JSONSCHEMAS_​RESOLVER_​CLS`](#jsonschemas-resolver-cls) | str | - |
| [`JSONSCHEMAS_​RESOLVE_​SCHEMA`](#jsonschemas-resolve-schema) | bool | - |
| [`JSONSCHEMAS_​SCHEMAS`](#jsonschemas-schemas) | NoneType | - |
| [`JSONSCHEMAS_​URL_​SCHEME`](#jsonschemas-url-scheme) | str | - |
| [`LOGGING_​CONSOLE`](#logging-console) | bool | - |
| [`LOGGING_​CONSOLE_​LEVEL`](#logging-console-level) | NoneType | - |
| [`LOGGING_​CONSOLE_​PYWARNINGS`](#logging-console-pywarnings) | bool | - |
| [`LOGGING_​FS_​BACKUPCOUNT`](#logging-fs-backupcount) | int | - |
| [`LOGGING_​FS_​LEVEL`](#logging-fs-level) | str | - |
| [`LOGGING_​FS_​LOGFILE`](#logging-fs-logfile) | NoneType | - |
| [`LOGGING_​FS_​MAXBYTES`](#logging-fs-maxbytes) | int | - |
| [`LOGGING_​FS_​PYWARNINGS`](#logging-fs-pywarnings) | bool | - |
| [`LOGGING_​SENTRY_​CELERY`](#logging-sentry-celery) | bool | - |
| [`LOGGING_​SENTRY_​CLASS`](#logging-sentry-class) | NoneType | - |
| [`LOGGING_​SENTRY_​INIT_​KWARGS`](#logging-sentry-init-kwargs) | NoneType | - |
| [`LOGGING_​SENTRY_​LEVEL`](#logging-sentry-level) | str | - |
| [`LOGGING_​SENTRY_​PYWARNINGS`](#logging-sentry-pywarnings) | bool | - |
| [`LOGGING_​SENTRY_​REDIS`](#logging-sentry-redis) | bool | - |
| [`LOGGING_​SENTRY_​SQLALCHEMY`](#logging-sentry-sqlalchemy) | bool | - |
| [`MAIL_​DEBUG`](#mail-debug) | bool | - |
| [`MAIL_​DEFAULT_​REPLY_​TO`](#mail-default-reply-to) | NoneType | - |
| [`MAIL_​DEFAULT_​SENDER`](#mail-default-sender) | unknown | `configure_generic_parameters` |
| [`MAIL_​MAX_​ATTACHMENT_​SIZE`](#mail-max-attachment-size) | int | - |
| [`MAIL_​MAX_​RETRIES`](#mail-max-retries) | int | - |
| [`MAIL_​MIN_​LOGGING_​LEVEL`](#mail-min-logging-level) | int | - |
| [`MAIL_​SUPPRESS_​SEND`](#mail-suppress-send) | bool | `configure_generic_parameters` |
| [`MATOMO_​ANALYTICS_​SITE_​ID`](#matomo-analytics-site-id) | configured by function | `configure_ui` |
| [`MATOMO_​ANALYTICS_​TEMPLATE`](#matomo-analytics-template) | configured by function | `configure_ui` |
| [`MATOMO_​ANALYTICS_​URL`](#matomo-analytics-url) | configured by function | `configure_ui` |
| [`MAX_​CONTENT_​LENGTH`](#max-content-length) | NoneType | - |
| [`MAX_​COOKIE_​SIZE`](#max-cookie-size) | int | - |
| [`MAX_​FORM_​MEMORY_​SIZE`](#max-form-memory-size) | int | - |
| [`MAX_​FORM_​PARTS`](#max-form-parts) | int | - |
| [`MULTIPROFILER_​BASE_​TEMPLATE`](#multiprofiler-base-template) | unknown | - |
| [`MULTIPROFILER_​IGNORED_​ENDPOINTS`](#multiprofiler-ignored-endpoints) | unknown | - |
| [`MULTIPROFILER_​PERMISSION`](#multiprofiler-permission) | unknown | - |
| [`NOTIFICATIONS_​BACKENDS`](#notifications-backends) | dict | - |
| [`NOTIFICATIONS_​BUILDERS`](#notifications-builders) | dict | - |
| [`NOTIFICATIONS_​ENTITY_​RESOLVERS`](#notifications-entity-resolvers) | list | - |
| [`NOTIFICATIONS_​GROUP_​EMAIL_​DOMAIN`](#notifications-group-email-domain) | NoneType | - |
| [`NOTIFICATIONS_​SETTINGS_​VIEW_​FUNCTION`](#notifications-settings-view-function) | NoneType | - |
| [`NOTIFICATION_​RECIPIENTS_​RESOLVERS`](#notification-recipients-resolvers) | dict | - |
| [`OAISERVER_​ADMIN_​EMAILS`](#oaiserver-admin-emails) | list | - |
| [`OAISERVER_​BASE_​TEMPLATE`](#oaiserver-base-template) | str | - |
| [`OAISERVER_​CACHE_​KEY`](#oaiserver-cache-key) | str | - |
| [`OAISERVER_​CELERY_​TASK_​CHUNK_​SIZE`](#oaiserver-celery-task-chunk-size) | int | - |
| [`OAISERVER_​COMPRESSIONS`](#oaiserver-compressions) | list | - |
| [`OAISERVER_​CONTROL_​NUMBER_​FETCHER`](#oaiserver-control-number-fetcher) | str | - |
| [`OAISERVER_​CREATED_​KEY`](#oaiserver-created-key) | str | - |
| [`OAISERVER_​DELETE_​PERCOLATOR_​FUNCTION`](#oaiserver-delete-percolator-function) | str | - |
| [`OAISERVER_​DESCRIPTIONS`](#oaiserver-descriptions) | list | - |
| [`OAISERVER_​GETRECORD_​FETCHER`](#oaiserver-getrecord-fetcher) | str | - |
| [`OAISERVER_​GRANULARITY`](#oaiserver-granularity) | str | - |
| [`OAISERVER_​ID_​FETCHER`](#oaiserver-id-fetcher) | str | - |
| [`OAISERVER_​ID_​PREFIX`](#oaiserver-id-prefix) | str | `configure_generic_parameters` |
| [`OAISERVER_​LAST_​UPDATE_​KEY`](#oaiserver-last-update-key) | str | - |
| [`OAISERVER_​METADATA_​FORMATS`](#oaiserver-metadata-formats) | OAIServerMetadataFormats | - |
| [`OAISERVER_​NEW_​PERCOLATOR_​FUNCTION`](#oaiserver-new-percolator-function) | str | - |
| [`OAISERVER_​PAGE_​SIZE`](#oaiserver-page-size) | int | - |
| [`OAISERVER_​PERCOLATOR_​DEDICATED_​INDEX`](#oaiserver-percolator-dedicated-index) | bool | - |
| [`OAISERVER_​PROTOCOL_​VERSION`](#oaiserver-protocol-version) | str | - |
| [`OAISERVER_​QUERY_​PARSER`](#oaiserver-query-parser) | unknown | - |
| [`OAISERVER_​QUERY_​PARSER_​FIELDS`](#oaiserver-query-parser-fields) | list | - |
| [`OAISERVER_​RECORD_​CLS`](#oaiserver-record-cls) | str | - |
| [`OAISERVER_​RECORD_​INDEX`](#oaiserver-record-index) | str | - |
| [`OAISERVER_​RECORD_​LIST_​SETS_​FETCHER`](#oaiserver-record-list-sets-fetcher) | str | - |
| [`OAISERVER_​RECORD_​SETS_​FETCHER`](#oaiserver-record-sets-fetcher) | str | - |
| [`OAISERVER_​REGISTER_​RECORD_​SIGNALS`](#oaiserver-register-record-signals) | bool | - |
| [`OAISERVER_​REGISTER_​SET_​SIGNALS`](#oaiserver-register-set-signals) | bool | - |
| [`OAISERVER_​REPOSITORY_​NAME`](#oaiserver-repository-name) | str | `configure_oai` |
| [`OAISERVER_​RESUMPTION_​TOKEN_​EXPIRE_​TIME`](#oaiserver-resumption-token-expire-time) | int | - |
| [`OAISERVER_​SEARCH_​CLS`](#oaiserver-search-cls) | str | - |
| [`OAISERVER_​SET_​RECORDS_​QUERY_​FETCHER`](#oaiserver-set-records-query-fetcher) | str | - |
| [`OAISERVER_​XSL_​URL`](#oaiserver-xsl-url) | NoneType | - |
| [`OAREPO_​CHECKS_​DEFAULT_​CHAT_​EINFRA_​CLIENT`](#oarepo-checks-default-chat-einfra-client) | configured by function | `configure_llm` |
| [`OAREPO_​CHECKS_​DEFAULT_​LLM_​CLIENT`](#oarepo-checks-default-llm-client) | configured by function | `configure_llm` |
| [`OAREPO_​CHECKS_​LLM_​CLIENTS`](#oarepo-checks-llm-clients) | configured by function | `configure_llm` |
| [`OAREPO_​COMMUNITIES_​DEFAULT_​WORKFLOW`](#oarepo-communities-default-workflow) | str | - |
| [`OAREPO_​MODELS`](#oarepo-models) | dict | - |
| [`OAREPO_​PERMISSIONS_​PRESETS`](#oarepo-permissions-presets) | dict | - |
| [`OAREPO_​REQUESTS_​DEFAULT_​RECEIVER`](#oarepo-requests-default-receiver) | str | - |
| [`OAREPO_​UI_​JINJAX_​FILTERS`](#oarepo-ui-jinjax-filters) | dict | - |
| [`OAREPO_​UI_​JINJAX_​GLOBALS`](#oarepo-ui-jinjax-globals) | dict | - |
| [`OAREPO_​UI_​LESS_​COMPONENTS`](#oarepo-ui-less-components) | list | - |
| [`OAREPO_​UI_​MULTILINGUAL_​FIELD_​LANGUAGES`](#oarepo-ui-multilingual-field-languages) | list | - |
| [`OAREPO_​UI_​OVERRIDES`](#oarepo-ui-overrides) | set | - |
| [`OAREPO_​UI_​RECORD_​ACTIONS`](#oarepo-ui-record-actions) | set | - |
| [`OAREPO_​UI_​RESULT_​LIST_​ITEM_​REGISTRATION_​CALLBACKS`](#oarepo-ui-result-list-item-registration-callbacks) | list | - |
| [`OAREPO_​VOCABULARIES_​PERMISSIONS_​PRESETS`](#oarepo-vocabularies-permissions-presets) | dict | - |
| [`OAREPO_​VOCABULARIES_​SORT_​CF`](#oarepo-vocabularies-sort-cf) | list | - |
| [`OAREPO_​VOCABULARIES_​SUGGEST_​CF`](#oarepo-vocabularies-suggest-cf) | list | - |
| [`OAREPO_​VOCABULARIES_​UI_​RESOURCE`](#oarepo-vocabularies-ui-resource) | str | - |
| [`OAREPO_​VOCABULARIES_​UI_​RESOURCE_​CONFIG`](#oarepo-vocabularies-ui-resource-config) | str | - |
| [`OAREPO_​VOCABULARY_​TYPE_​RESOURCE`](#oarepo-vocabulary-type-resource) | unknown | - |
| [`OAREPO_​VOCABULARY_​TYPE_​RESOURCE_​CONFIG`](#oarepo-vocabulary-type-resource-config) | unknown | - |
| [`OAREPO_​VOCABULARY_​TYPE_​SERVICE`](#oarepo-vocabulary-type-service) | unknown | - |
| [`OAREPO_​VOCABULARY_​TYPE_​SERVICE_​CONFIG`](#oarepo-vocabulary-type-service-config) | unknown | - |
| [`OAUTH2SERVER_​ALLOWED_​GRANT_​TYPES`](#oauth2server-allowed-grant-types) | set | - |
| [`OAUTH2SERVER_​ALLOWED_​RESPONSE_​TYPES`](#oauth2server-allowed-response-types) | set | - |
| [`OAUTH2SERVER_​ALLOWED_​URLENCODE_​CHARACTERS`](#oauth2server-allowed-urlencode-characters) | str | - |
| [`OAUTH2SERVER_​BASE_​TEMPLATE`](#oauth2server-base-template) | str | - |
| [`OAUTH2SERVER_​CLIENT_​ID_​SALT_​LEN`](#oauth2server-client-id-salt-len) | int | - |
| [`OAUTH2SERVER_​CLIENT_​SECRET_​SALT_​LEN`](#oauth2server-client-secret-salt-len) | int | - |
| [`OAUTH2SERVER_​COVER_​TEMPLATE`](#oauth2server-cover-template) | str | - |
| [`OAUTH2SERVER_​JWT_​AUTH_​HEADER`](#oauth2server-jwt-auth-header) | str | - |
| [`OAUTH2SERVER_​JWT_​AUTH_​HEADER_​TYPE`](#oauth2server-jwt-auth-header-type) | str | - |
| [`OAUTH2SERVER_​JWT_​VERIFICATION_​FACTORY`](#oauth2server-jwt-verification-factory) | str | - |
| [`OAUTH2SERVER_​SETTINGS_​TEMPLATE`](#oauth2server-settings-template) | str | - |
| [`OAUTH2SERVER_​TOKEN_​PERSONAL_​SALT_​LEN`](#oauth2server-token-personal-salt-len) | int | - |
| [`OAUTH2_​CACHE_​TYPE`](#oauth2-cache-type) | str | - |
| [`OAUTH2_​PROVIDER_​ERROR_​ENDPOINT`](#oauth2-provider-error-endpoint) | str | - |
| [`OAUTHCLIENT_​AUTO_​REDIRECT_​TO_​EXTERNAL_​LOGIN`](#oauthclient-auto-redirect-to-external-login) | bool | `configure_generic_parameters` |
| [`OAUTHCLIENT_​BASE_​TEMPLATE`](#oauthclient-base-template) | str | - |
| [`OAUTHCLIENT_​COVER_​TEMPLATE`](#oauthclient-cover-template) | str | - |
| [`OAUTHCLIENT_​LOGIN_​USER_​TEMPLATE_​PARENT`](#oauthclient-login-user-template-parent) | str | - |
| [`OAUTHCLIENT_​REMOTE_​APPS`](#oauthclient-remote-apps) | dict | `configure_generic_parameters`, `configure_einfra_oidc` |
| [`OAUTHCLIENT_​REST_​DEFAULT_​ERROR_​REDIRECT_​URL`](#oauthclient-rest-default-error-redirect-url) | str | - |
| [`OAUTHCLIENT_​REST_​DEFAULT_​RESPONSE_​HANDLER`](#oauthclient-rest-default-response-handler) | NoneType | - |
| [`OAUTHCLIENT_​REST_​REMOTE_​APPS`](#oauthclient-rest-remote-apps) | dict | - |
| [`OAUTHCLIENT_​SESSION_​KEY_​PREFIX`](#oauthclient-session-key-prefix) | str | - |
| [`OAUTHCLIENT_​SETTINGS_​TEMPLATE`](#oauthclient-settings-template) | str | - |
| [`OAUTHCLIENT_​SIGNUP_​FORM`](#oauthclient-signup-form) | unknown | - |
| [`OAUTHCLIENT_​SIGNUP_​TEMPLATE`](#oauthclient-signup-template) | str | - |
| [`OAUTHCLIENT_​SITENAME`](#oauthclient-sitename) | LazyString | - |
| [`OAUTHCLIENT_​STATE_​ENABLED`](#oauthclient-state-enabled) | bool | - |
| [`OAUTHCLIENT_​STATE_​EXPIRES`](#oauthclient-state-expires) | int | - |
| [`OAUTHCLIENT_​TOKEN_​EXPIRES_​LEEWAY`](#oauthclient-token-expires-leeway) | int | - |
| [`ORCID_​PUBLIC_​DUMP_​S3_​BUCKET_​NAME`](#orcid-public-dump-s3-bucket-name) | str | - |
| [`PAGES_​ALLOWED_​EXTRA_​HTML_​ATTRS`](#pages-allowed-extra-html-attrs) | dict | - |
| [`PAGES_​ALLOWED_​EXTRA_​HTML_​TAGS`](#pages-allowed-extra-html-tags) | list | - |
| [`PAGES_​BASE_​TEMPLATE`](#pages-base-template) | str | - |
| [`PAGES_​DEFAULT_​TEMPLATE`](#pages-default-template) | str | - |
| [`PAGES_​FACETS`](#pages-facets) | dict | - |
| [`PAGES_​SEARCH`](#pages-search) | dict | - |
| [`PAGES_​SORT_​OPTIONS`](#pages-sort-options) | dict | - |
| [`PAGES_​TEMPLATES`](#pages-templates) | list | - |
| [`PAGES_​WHITELIST_​CONFIG_​KEYS`](#pages-whitelist-config-keys) | list | - |
| [`PERMANENT_​SESSION_​LIFETIME`](#permanent-session-lifetime) | timedelta | - |
| [`PIDSTORE_​APP_​LOGGER_​HANDLERS`](#pidstore-app-logger-handlers) | bool | - |
| [`PIDSTORE_​DATACITE_​DOI_​PREFIX`](#pidstore-datacite-doi-prefix) | str | - |
| [`PIDSTORE_​OBJECT_​ENDPOINTS`](#pidstore-object-endpoints) | dict | - |
| [`PIDSTORE_​RECID_​FIELD`](#pidstore-recid-field) | str | - |
| [`PIDSTORE_​RECORDID_​OPTIONS`](#pidstore-recordid-options) | dict | - |
| [`PREFERRED_​URL_​SCHEME`](#preferred-url-scheme) | str | - |
| [`PREVIEWABLE_​ZIP_​PREVIEWER_​NATIVE_​EXTENSIONS`](#previewable-zip-previewer-native-extensions) | list | - |
| [`PREVIEWER_​ABSTRACT_​TEMPLATE`](#previewer-abstract-template) | str | - |
| [`PREVIEWER_​BASE_​CSS_​BUNDLES`](#previewer-base-css-bundles) | list | - |
| [`PREVIEWER_​BASE_​JS_​BUNDLES`](#previewer-base-js-bundles) | list | - |
| [`PREVIEWER_​BASE_​TEMPLATE`](#previewer-base-template) | str | - |
| [`PREVIEWER_​CHARDET_​BYTES`](#previewer-chardet-bytes) | int | - |
| [`PREVIEWER_​CHARDET_​CONFIDENCE`](#previewer-chardet-confidence) | float | - |
| [`PREVIEWER_​CONTAINER_​ITEM_​PREFERENCE`](#previewer-container-item-preference) | list | - |
| [`PREVIEWER_​CSV_​MAX_​BYTES`](#previewer-csv-max-bytes) | int | - |
| [`PREVIEWER_​CSV_​SNIFFER_​ALLOWED_​DELIMITERS`](#previewer-csv-sniffer-allowed-delimiters) | NoneType | - |
| [`PREVIEWER_​CSV_​VALIDATION_​BYTES`](#previewer-csv-validation-bytes) | int | - |
| [`PREVIEWER_​MAX_​FILE_​SIZE_​BYTES`](#previewer-max-file-size-bytes) | int | - |
| [`PREVIEWER_​MAX_​IMAGE_​SIZE_​BYTES`](#previewer-max-image-size-bytes) | float | - |
| [`PREVIEWER_​PDF_​JS_​DOCUMENT_​INIT_​PARAMS`](#previewer-pdf-js-document-init-params) | NoneType | - |
| [`PREVIEWER_​PDF_​JS_​ENABLE_​SCRIPTING`](#previewer-pdf-js-enable-scripting) | bool | - |
| [`PREVIEWER_​PREFERENCE`](#previewer-preference) | list | - |
| [`PREVIEWER_​RECORD_​FILE_​FACOTRY`](#previewer-record-file-facotry) | NoneType | - |
| [`PREVIEWER_​TXT_​MAX_​BYTES`](#previewer-txt-max-bytes) | int | - |
| [`PREVIEWER_​WEB_​ARCHIVE_​RANGE_​REQUESTS`](#previewer-web-archive-range-requests) | bool | - |
| [`PREVIEWER_​ZIP_​MAX_​FILES`](#previewer-zip-max-files) | int | - |
| [`PROPAGATE_​EXCEPTIONS`](#propagate-exceptions) | NoneType | - |
| [`PROVIDE_​AUTOMATIC_​OPTIONS`](#provide-automatic-options) | bool | - |
| [`PUBLISH_​REQUEST_​TYPES`](#publish-request-types) | list | - |
| [`QUEUES_​BROKER_​URL`](#queues-broker-url) | NoneType | - |
| [`QUEUES_​CONNECTION_​POOL`](#queues-connection-pool) | unknown | - |
| [`QUEUES_​DEFINITIONS`](#queues-definitions) | list | - |
| [`RATELIMIT_​APPLICATION`](#ratelimit-application) | unknown | - |
| [`RATELIMIT_​AUTHENTICATED_​USER`](#ratelimit-authenticated-user) | str | `configure_generic_parameters` |
| [`RATELIMIT_​ENABLED`](#ratelimit-enabled) | bool | - |
| [`RATELIMIT_​GUEST_​USER`](#ratelimit-guest-user) | str | `configure_generic_parameters` |
| [`RATELIMIT_​HEADERS_​ENABLED`](#ratelimit-headers-enabled) | bool | - |
| [`RATELIMIT_​KEY_​FUNC`](#ratelimit-key-func) | NoneType | - |
| [`RATELIMIT_​PER_​ENDPOINT`](#ratelimit-per-endpoint) | dict | - |
| [`RATELIMIT_​STORAGE_​URI`](#ratelimit-storage-uri) | str | - |
| [`RATELIMIT_​STRATEGY`](#ratelimit-strategy) | str | - |
| [`RDM_​ALLOW_​EXTERNAL_​DOI_​VERSIONING`](#rdm-allow-external-doi-versioning) | bool | - |
| [`RDM_​ALLOW_​METADATA_​ONLY_​RECORDS`](#rdm-allow-metadata-only-records) | bool | - |
| [`RDM_​ALLOW_​OWNERS_​REMOVE_​COMMUNITY_​FROM_​RECORD`](#rdm-allow-owners-remove-community-from-record) | bool | - |
| [`RDM_​ALLOW_​RESTRICTED_​RECORDS`](#rdm-allow-restricted-records) | bool | - |
| [`RDM_​ARCHIVE_​DOWNLOAD_​ENABLED`](#rdm-archive-download-enabled) | bool | - |
| [`RDM_​CITATION_​STYLES`](#rdm-citation-styles) | list | - |
| [`RDM_​CITATION_​STYLES_​DEFAULT`](#rdm-citation-styles-default) | str | - |
| [`RDM_​COMMUNITIES_​ROUTES`](#rdm-communities-routes) | dict | - |
| [`RDM_​COMMUNITY_​CONTENT_​MODERATION_​HANDLERS`](#rdm-community-content-moderation-handlers) | list | - |
| [`RDM_​COMMUNITY_​INCLUSION_​REQUEST_​CLS`](#rdm-community-inclusion-request-cls) | unknown | - |
| [`RDM_​COMMUNITY_​REQUIRED_​TO_​PUBLISH`](#rdm-community-required-to-publish) | bool | - |
| [`RDM_​COMMUNITY_​SUBMISSION_​REQUEST_​CLS`](#rdm-community-submission-request-cls) | unknown | - |
| [`RDM_​CONTENT_​MODERATION_​HANDLERS`](#rdm-content-moderation-handlers) | list | - |
| [`RDM_​CUSTOM_​FIELDS`](#rdm-custom-fields) | list | - |
| [`RDM_​CUSTOM_​FIELDS_​UI`](#rdm-custom-fields-ui) | list | - |
| [`RDM_​DATACITE_​DUMP_​OPENAIRE_​ACCESS_​RIGHTS`](#rdm-datacite-dump-openaire-access-rights) | bool | - |
| [`RDM_​DATACITE_​FUNDER_​IDENTIFIERS_​PRIORITY`](#rdm-datacite-funder-identifiers-priority) | tuple | - |
| [`RDM_​DEFAULT_​FILES_​ENABLED`](#rdm-default-files-enabled) | bool | - |
| [`RDM_​DETAIL_​SIDE_​BAR_​MANAGE_​ATTRIBUTES_​EXTENSION_​TEMPLATE`](#rdm-detail-side-bar-manage-attributes-extension-template) | unknown | - |
| [`RDM_​FACETS`](#rdm-facets) | unknown | - |
| [`RDM_​FILES_​DEFAULT_​MAX_​ADDITIONAL_​QUOTA_​SIZE`](#rdm-files-default-max-additional-quota-size) | int | - |
| [`RDM_​FILES_​DEFAULT_​MAX_​FILE_​SIZE`](#rdm-files-default-max-file-size) | int | - |
| [`RDM_​FILES_​DEFAULT_​QUOTA_​SIZE`](#rdm-files-default-quota-size) | int | - |
| [`RDM_​FILE_​MODIFICATION_​PERIOD`](#rdm-file-modification-period) | timedelta | - |
| [`RDM_​FILE_​MODIFICATION_​POLICY`](#rdm-file-modification-policy) | unknown | - |
| [`RDM_​IIIF_​MANIFEST_​FORMATS`](#rdm-iiif-manifest-formats) | list | - |
| [`RDM_​IMMEDIATE_​FILE_​MODIFICATION_​ENABLED`](#rdm-immediate-file-modification-enabled) | bool | - |
| [`RDM_​IMMEDIATE_​FILE_​MODIFICATION_​POLICIES`](#rdm-immediate-file-modification-policies) | list | - |
| [`RDM_​IMMEDIATE_​QUOTA_​INCREASE_​ENABLED`](#rdm-immediate-quota-increase-enabled) | bool | - |
| [`RDM_​IMMEDIATE_​QUOTA_​INCREASE_​POLICIES`](#rdm-immediate-quota-increase-policies) | list | - |
| [`RDM_​IMMEDIATE_​RECORD_​DELETION_​CHECKLIST`](#rdm-immediate-record-deletion-checklist) | list | - |
| [`RDM_​IMMEDIATE_​RECORD_​DELETION_​ENABLED`](#rdm-immediate-record-deletion-enabled) | bool | - |
| [`RDM_​IMMEDIATE_​RECORD_​DELETION_​POLICIES`](#rdm-immediate-record-deletion-policies) | list | - |
| [`RDM_​LOCK_​EDIT_​PUBLISHED_​FILES`](#rdm-lock-edit-published-files) | unknown | - |
| [`RDM_​MEDIA_​FILES_​DEFAULT_​MAX_​FILE_​SIZE`](#rdm-media-files-default-max-file-size) | int | - |
| [`RDM_​MEDIA_​FILES_​DEFAULT_​QUOTA_​SIZE`](#rdm-media-files-default-quota-size) | int | - |
| [`RDM_​NAMESPACES`](#rdm-namespaces) | dict | - |
| [`RDM_​NEW_​RECORD_​VERSION_​REVIEW_​POLICY`](#rdm-new-record-version-review-policy) | unknown | - |
| [`RDM_​OAI_​PMH_​FACETS`](#rdm-oai-pmh-facets) | dict | - |
| [`RDM_​OAI_​PMH_​SEARCH`](#rdm-oai-pmh-search) | dict | - |
| [`RDM_​OAI_​PMH_​SORT_​OPTIONS`](#rdm-oai-pmh-sort-options) | dict | - |
| [`RDM_​OPTIONAL_​DOI_​VALIDATOR`](#rdm-optional-doi-validator) | unknown | - |
| [`RDM_​PARENT_​PERSISTENT_​IDENTIFIERS`](#rdm-parent-persistent-identifiers) | dict | - |
| [`RDM_​PARENT_​PERSISTENT_​IDENTIFIER_​PROVIDERS`](#rdm-parent-persistent-identifier-providers) | list | - |
| [`RDM_​PERMISSION_​POLICY`](#rdm-permission-policy) | unknown | - |
| [`RDM_​PERSISTENT_​IDENTIFIERS`](#rdm-persistent-identifiers) | dict | - |
| [`RDM_​PERSISTENT_​IDENTIFIER_​PROVIDERS`](#rdm-persistent-identifier-providers) | list | - |
| [`RDM_​QUOTA_​INCREASE_​POLICY`](#rdm-quota-increase-policy) | unknown | - |
| [`RDM_​RECORDS_​ACCESS_​SERVICE_​CLASS`](#rdm-records-access-service-class) | str | - |
| [`RDM_​RECORDS_​ALLOW_​RESTRICTION_​AFTER_​GRACE_​PERIOD`](#rdm-records-allow-restriction-after-grace-period) | bool | - |
| [`RDM_​RECORDS_​COMMUNITY_​RECORDS_​CONFIG_​CLASS`](#rdm-records-community-records-config-class) | str | - |
| [`RDM_​RECORDS_​COMMUNITY_​RECORDS_​SERVICE_​CLASS`](#rdm-records-community-records-service-class) | str | - |
| [`RDM_​RECORDS_​CONTAINER_​EXTENSIONS`](#rdm-records-container-extensions) | list | - |
| [`RDM_​RECORDS_​ERROR_​HANDLERS`](#rdm-records-error-handlers) | dict | - |
| [`RDM_​RECORDS_​IDENTIFIERS_​SCHEMES`](#rdm-records-identifiers-schemes) | dict | - |
| [`RDM_​RECORDS_​LOCATION_​SCHEMES`](#rdm-records-location-schemes) | dict | - |
| [`RDM_​RECORDS_​MAX_​FILES_​COUNT`](#rdm-records-max-files-count) | int | - |
| [`RDM_​RECORDS_​MAX_​MEDIA_​FILES_​COUNT`](#rdm-records-max-media-files-count) | int | - |
| [`RDM_​RECORDS_​PERSONORG_​SCHEMES`](#rdm-records-personorg-schemes) | dict | - |
| [`RDM_​RECORDS_​PIDS_​SERVICE_​CLASS`](#rdm-records-pids-service-class) | str | - |
| [`RDM_​RECORDS_​RELATED_​IDENTIFIERS_​SCHEMES`](#rdm-records-related-identifiers-schemes) | dict | - |
| [`RDM_​RECORDS_​REQUIRE_​SECRET_​LINKS_​EXPIRATION`](#rdm-records-require-secret-links-expiration) | bool | - |
| [`RDM_​RECORDS_​RESOURCE_​CLASS`](#rdm-records-resource-class) | str | - |
| [`RDM_​RECORDS_​RESOURCE_​CONFIG_​CLASS`](#rdm-records-resource-config-class) | str | - |
| [`RDM_​RECORDS_​RESTRICTION_​GRACE_​PERIOD`](#rdm-records-restriction-grace-period) | timedelta | - |
| [`RDM_​RECORDS_​REVIEWS`](#rdm-records-reviews) | list | - |
| [`RDM_​RECORDS_​REVIEW_​SERVICE_​CLASS`](#rdm-records-review-service-class) | str | - |
| [`RDM_​RECORDS_​SERVICE_​CLASS`](#rdm-records-service-class) | str | - |
| [`RDM_​RECORDS_​SERVICE_​COMPONENTS`](#rdm-records-service-components) | list | - |
| [`RDM_​RECORDS_​SERVICE_​CONFIG_​CLASS`](#rdm-records-service-config-class) | str | - |
| [`RDM_​RECORDS_​UI_​EDIT_​URL`](#rdm-records-ui-edit-url) | str | - |
| [`RDM_​RECORDS_​USER_​FIXTURE_​PASSWORDS`](#rdm-records-user-fixture-passwords) | dict | - |
| [`RDM_​RECORD_​DELETION_​POLICY`](#rdm-record-deletion-policy) | unknown | - |
| [`RDM_​RECORD_​FILE_​EXTRACTORS`](#rdm-record-file-extractors) | list | - |
| [`RDM_​REQUESTS_​ROUTES`](#rdm-requests-routes) | dict | - |
| [`RDM_​REQUEST_​RECORD_​DELETION_​CHECKLIST`](#rdm-request-record-deletion-checklist) | list | - |
| [`RDM_​REQUEST_​RECORD_​DELETION_​ENABLED`](#rdm-request-record-deletion-enabled) | bool | - |
| [`RDM_​REQUEST_​RECORD_​DELETION_​POLICIES`](#rdm-request-record-deletion-policies) | list | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​ENABLED`](#rdm-resource-access-tokens-enabled) | bool | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​JWT_​LIFETIME`](#rdm-resource-access-tokens-jwt-lifetime) | timedelta | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​SUBJECT_​SCHEMA`](#rdm-resource-access-tokens-subject-schema) | unknown | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKENS_​WHITELISTED_​JWT_​ALGORITHMS`](#rdm-resource-access-tokens-whitelisted-jwt-algorithms) | list | - |
| [`RDM_​RESOURCE_​ACCESS_​TOKEN_​REQUEST_​ARG`](#rdm-resource-access-token-request-arg) | str | - |
| [`RDM_​SEARCH`](#rdm-search) | unknown | - |
| [`RDM_​SEARCH_​DRAFTS`](#rdm-search-drafts) | unknown | - |
| [`RDM_​SEARCH_​SORT_​BY_​VERIFIED`](#rdm-search-sort-by-verified) | bool | - |
| [`RDM_​SEARCH_​USER_​COMMUNITIES`](#rdm-search-user-communities) | dict | - |
| [`RDM_​SEARCH_​USER_​REQUESTS`](#rdm-search-user-requests) | dict | - |
| [`RDM_​SEARCH_​VERSIONING`](#rdm-search-versioning) | dict | - |
| [`RDM_​SORT_​OPTIONS`](#rdm-sort-options) | dict | - |
| [`RDM_​STATS_​EXCLUDE_​PREVIEW_​FILE_​DOWNLOAD_​EVENTS`](#rdm-stats-exclude-preview-file-download-events) | bool | - |
| [`RDM_​USER_​MODERATION_​ENABLED`](#rdm-user-moderation-enabled) | bool | - |
| [`RECAPTCHA_​PRIVATE_​KEY`](#recaptcha-private-key) | unknown | - |
| [`RECAPTCHA_​PUBLIC_​KEY`](#recaptcha-public-key) | unknown | - |
| [`RECORDS_​FILES_​REST_​ENDPOINTS`](#records-files-rest-endpoints) | dict | - |
| [`RECORDS_​PERMISSIONS_​RECORD_​POLICY`](#records-permissions-record-policy) | str | - |
| [`RECORDS_​REFRESOLVER_​CLS`](#records-refresolver-cls) | NoneType | `configure_generic_parameters` |
| [`RECORDS_​REFRESOLVER_​STORE`](#records-refresolver-store) | NoneType | `configure_generic_parameters` |
| [`RECORDS_​RESOURCES_​ALLOW_​EMPTY_​FILES`](#records-resources-allow-empty-files) | bool | - |
| [`RECORDS_​RESOURCES_​ARCHIVE_​DOWNLOAD_​MAX_​SIZE`](#records-resources-archive-download-max-size) | NoneType | - |
| [`RECORDS_​RESOURCES_​DEFAULT_​TRANSFER_​TYPE`](#records-resources-default-transfer-type) | str | - |
| [`RECORDS_​RESOURCES_​EXTRACTED_​STREAM_​CHUNK_​SIZE`](#records-resources-extracted-stream-chunk-size) | int | - |
| [`RECORDS_​RESOURCES_​FILES_​ALLOWED_​DOMAINS`](#records-resources-files-allowed-domains) | list | - |
| [`RECORDS_​RESOURCES_​IMAGE_​FORMATS`](#records-resources-image-formats) | list | - |
| [`RECORDS_​RESOURCES_​TRANSFERS`](#records-resources-transfers) | list | - |
| [`RECORDS_​RESOURCES_​ZIP_​FORMATS`](#records-resources-zip-formats) | list | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​ENTRIES`](#records-resources-zip-max-entries) | int | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​HEADER_​SIZE`](#records-resources-zip-max-header-size) | int | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​LISTING_​ENTRIES`](#records-resources-zip-max-listing-entries) | int | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​RATIO`](#records-resources-zip-max-ratio) | float | - |
| [`RECORDS_​RESOURCES_​ZIP_​MAX_​TOTAL_​UNCOMPRESSED`](#records-resources-zip-max-total-uncompressed) | int | - |
| [`RECORDS_​REST_​DEFAULT_​CREATE_​PERMISSION_​FACTORY`](#records-rest-default-create-permission-factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​DELETE_​PERMISSION_​FACTORY`](#records-rest-default-delete-permission-factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​LIST_​PERMISSION_​FACTORY`](#records-rest-default-list-permission-factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​LOADERS`](#records-rest-default-loaders) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​READ_​PERMISSION_​FACTORY`](#records-rest-default-read-permission-factory) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​RESULTS_​SIZE`](#records-rest-default-results-size) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​SORT`](#records-rest-default-sort) | unknown | - |
| [`RECORDS_​REST_​DEFAULT_​UPDATE_​PERMISSION_​FACTORY`](#records-rest-default-update-permission-factory) | unknown | - |
| [`RECORDS_​REST_​ENDPOINTS`](#records-rest-endpoints) | list | `configure_generic_parameters` |
| [`RECORDS_​REST_​FACETS`](#records-rest-facets) | unknown | - |
| [`RECORDS_​REST_​FACETS_​POST_​FILTERS_​PROPAGATE`](#records-rest-facets-post-filters-propagate) | unknown | - |
| [`RECORDS_​REST_​SEARCH_​ERROR_​HANDLERS`](#records-rest-search-error-handlers) | unknown | - |
| [`RECORDS_​REST_​SORT_​OPTIONS`](#records-rest-sort-options) | unknown | - |
| [`RECORDS_​UI_​BASE_​TEMPLATE`](#records-ui-base-template) | str | - |
| [`RECORDS_​UI_​DEFAULT_​PERMISSION_​FACTORY`](#records-ui-default-permission-factory) | NoneType | - |
| [`RECORDS_​UI_​ENDPOINTS`](#records-ui-endpoints) | dict | `configure_ui` |
| [`RECORDS_​UI_​EXPORT_​FORMATS`](#records-ui-export-formats) | dict | - |
| [`RECORDS_​UI_​LOGIN_​ENDPOINT`](#records-ui-login-endpoint) | str | - |
| [`RECORDS_​UI_​TOMBSTONE_​TEMPLATE`](#records-ui-tombstone-template) | str | - |
| [`RECORDS_​VALIDATION_​TYPES`](#records-validation-types) | dict | - |
| [`RECORD_​ROUTES`](#record-routes) | configured by function | `configure_generic_parameters` |
| [`RELATED_​RESOURCES_​DEFAULT_​RESOURCE_​TYPE`](#related-resources-default-resource-type) | str | - |
| [`RELATED_​RESOURCES_​DEFAULT_​TIMEOUT`](#related-resources-default-timeout) | int | - |
| [`RELATED_​RESOURCES_​RECORD_​UI_​SCHEMA`](#related-resources-record-ui-schema) | str | - |
| [`RELATED_​RESOURCES_​RESOURCE_​CLASS`](#related-resources-resource-class) | str | - |
| [`RELATED_​RESOURCES_​RESOURCE_​CONFIG_​CLASS`](#related-resources-resource-config-class) | str | - |
| [`RELATED_​RESOURCES_​SERVICE_​CLASS`](#related-resources-service-class) | str | - |
| [`RELATED_​RESOURCES_​SERVICE_​CONFIG_​CLASS`](#related-resources-service-config-class) | str | - |
| [`REMEMBER_​COOKIE_​DURATION`](#remember-cookie-duration) | unknown | - |
| [`REPOSITORY_​DESCRIPTION`](#repository-description) | configured by function | `configure_ui` |
| [`REPOSITORY_​KEYWORDS`](#repository-keywords) | configured by function | `configure_ui` |
| [`REPOSITORY_​NAME`](#repository-name) | configured by function | `configure_ui` |
| [`REPOSITORY_​SUBTITLE`](#repository-subtitle) | configured by function | `configure_ui` |
| [`REPOSITORY_​SUPPORT_​CONTACT`](#repository-support-contact) | configured by function | `configure_ui` |
| [`REQUESTS_​ACTION_​COMPONENTS`](#requests-action-components) | list | - |
| [`REQUESTS_​ALLOWED_​RECEIVERS`](#requests-allowed-receivers) | list | - |
| [`REQUESTS_​COMMENTS_​ALLOWED_​EXTRA_​HTML_​ATTRS`](#requests-comments-allowed-extra-html-attrs) | dict | - |
| [`REQUESTS_​COMMENTS_​ALLOWED_​EXTRA_​HTML_​TAGS`](#requests-comments-allowed-extra-html-tags) | list | - |
| [`REQUESTS_​COMMENT_​PREVIEW_​LIMIT`](#requests-comment-preview-limit) | int | - |
| [`REQUESTS_​ENTITY_​RESOLVERS`](#requests-entity-resolvers) | list | - |
| [`REQUESTS_​ERROR_​HANDLERS`](#requests-error-handlers) | unknown | - |
| [`REQUESTS_​EVENTS_​SERVICE_​COMPONENTS`](#requests-events-service-components) | list | - |
| [`REQUESTS_​FACETS`](#requests-facets) | dict | - |
| [`REQUESTS_​FILES_​DEFAULT_​MAX_​FILE_​SIZE`](#requests-files-default-max-file-size) | int | - |
| [`REQUESTS_​FILES_​DEFAULT_​QUOTA_​SIZE`](#requests-files-default-quota-size) | int | - |
| [`REQUESTS_​LOCKING_​ENABLED`](#requests-locking-enabled) | bool | - |
| [`REQUESTS_​MODERATION_​ROLE`](#requests-moderation-role) | str | - |
| [`REQUESTS_​PERMISSION_​POLICY`](#requests-permission-policy) | unknown | - |
| [`REQUESTS_​REGISTERED_​EVENT_​TYPES`](#requests-registered-event-types) | list | - |
| [`REQUESTS_​REGISTERED_​TYPES`](#requests-registered-types) | list | - |
| [`REQUESTS_​RESOURCE_​CLASS`](#requests-resource-class) | unknown | - |
| [`REQUESTS_​RESOURCE_​CONFIG_​CLASS`](#requests-resource-config-class) | unknown | - |
| [`REQUESTS_​REVIEWERS_​ENABLED`](#requests-reviewers-enabled) | bool | - |
| [`REQUESTS_​REVIEWERS_​MAX_​NUMBER`](#requests-reviewers-max-number) | int | - |
| [`REQUESTS_​ROUTES`](#requests-routes) | dict | - |
| [`REQUESTS_​SEARCH`](#requests-search) | dict | - |
| [`REQUESTS_​SERVICE_​CLASS`](#requests-service-class) | unknown | - |
| [`REQUESTS_​SERVICE_​CONFIG_​CLASS`](#requests-service-config-class) | unknown | - |
| [`REQUESTS_​SORT_​OPTIONS`](#requests-sort-options) | dict | - |
| [`REQUESTS_​TIMELINE_​PAGE_​SIZE`](#requests-timeline-page-size) | int | - |
| [`REQUESTS_​USER_​MODERATION_​FACETS`](#requests-user-moderation-facets) | dict | - |
| [`REQUESTS_​USER_​MODERATION_​SEARCH`](#requests-user-moderation-search) | dict | - |
| [`REQUESTS_​USER_​MODERATION_​SORT_​OPTIONS`](#requests-user-moderation-sort-options) | dict | - |
| [`REST_​CSRF_​ENABLED`](#rest-csrf-enabled) | unknown | - |
| [`REST_​ENABLE_​CORS`](#rest-enable-cors) | unknown | - |
| [`REST_​MIMETYPE_​QUERY_​ARG_​NAME`](#rest-mimetype-query-arg-name) | unknown | - |
| [`ROR_​CLIENT_​ID`](#ror-client-id) | configured by function | `configure_generic_parameters` |
| [`S3_​ACCESS_​KEY_​ID`](#s3-access-key-id) | NoneType | `configure_generic_parameters` |
| [`S3_​CONFIG_​EXTRA`](#s3-config-extra) | dict | - |
| [`S3_​DEFAULT_​BLOCK_​SIZE`](#s3-default-block-size) | int | - |
| [`S3_​ENDPOINT_​URL`](#s3-endpoint-url) | NoneType | `configure_generic_parameters` |
| [`S3_​MAXIMUM_​NUMBER_​OF_​PARTS`](#s3-maximum-number-of-parts) | int | - |
| [`S3_​REGION_​NAME`](#s3-region-name) | NoneType | - |
| [`S3_​SECRET_​ACCESS_​KEY`](#s3-secret-access-key) | NoneType | `configure_generic_parameters` |
| [`S3_​SIGNATURE_​VERSION`](#s3-signature-version) | str | - |
| [`S3_​UPLOAD_​URL_​EXPIRATION`](#s3-upload-url-expiration) | int | - |
| [`S3_​URL_​EXPIRATION`](#s3-url-expiration) | int | - |
| [`SEARCH_​CLIENT_​CONFIG`](#search-client-config) | NoneType | `configure_generic_parameters` |
| [`SEARCH_​ELASTIC_​HOSTS`](#search-elastic-hosts) | NoneType | - |
| [`SEARCH_​HOSTS`](#search-hosts) | NoneType | `configure_generic_parameters` |
| [`SEARCH_​INDEX_​PREFIX`](#search-index-prefix) | str | `configure_generic_parameters` |
| [`SEARCH_​MAPPINGS`](#search-mappings) | NoneType | - |
| [`SEARCH_​RESULTS_​MIN_​SCORE`](#search-results-min-score) | NoneType | - |
| [`SEARCH_​UI_​BASE_​TEMPLATE`](#search-ui-base-template) | NoneType | - |
| [`SEARCH_​UI_​HEADER_​TEMPLATE`](#search-ui-header-template) | NoneType | - |
| [`SEARCH_​UI_​JSTEMPLATE_​COUNT`](#search-ui-jstemplate-count) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​ERROR`](#search-ui-jstemplate-error) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​FACETS`](#search-ui-jstemplate-facets) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​LOADING`](#search-ui-jstemplate-loading) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​PAGINATION`](#search-ui-jstemplate-pagination) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​RANGE`](#search-ui-jstemplate-range) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​RANGE_​OPTIONS`](#search-ui-jstemplate-range-options) | dict | - |
| [`SEARCH_​UI_​JSTEMPLATE_​RESULTS`](#search-ui-jstemplate-results) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​SELECT_​BOX`](#search-ui-jstemplate-select-box) | str | - |
| [`SEARCH_​UI_​JSTEMPLATE_​SORT_​ORDER`](#search-ui-jstemplate-sort-order) | str | - |
| [`SEARCH_​UI_​SEARCH_​API`](#search-ui-search-api) | str | - |
| [`SEARCH_​UI_​SEARCH_​CONFIG_​GEN`](#search-ui-search-config-gen) | dict | - |
| [`SEARCH_​UI_​SEARCH_​INDEX`](#search-ui-search-index) | str | - |
| [`SEARCH_​UI_​SEARCH_​TEMPLATE`](#search-ui-search-template) | str | `configure_ui` |
| [`SEARCH_​UI_​SEARCH_​VIEW`](#search-ui-search-view) | unknown | `configure_ui` |
| [`SECRET_​KEY`](#secret-key) | str | `configure_generic_parameters` |
| [`SECRET_​KEY_​FALLBACKS`](#secret-key-fallbacks) | NoneType | - |
| [`SECURITY_​AUTO_​LOGIN_​AFTER_​CONFIRM`](#security-auto-login-after-confirm) | bool | - |
| [`SECURITY_​BLUEPRINT_​NAME`](#security-blueprint-name) | str | - |
| [`SECURITY_​CHANGEABLE`](#security-changeable) | bool | `configure_generic_parameters` |
| [`SECURITY_​CHANGE_​PASSWORD_​TEMPLATE`](#security-change-password-template) | str | - |
| [`SECURITY_​CHANGE_​SALT`](#security-change-salt) | str | - |
| [`SECURITY_​CHANGE_​URL`](#security-change-url) | str | - |
| [`SECURITY_​CLI_​ROLES_​NAME`](#security-cli-roles-name) | str | - |
| [`SECURITY_​CLI_​USERS_​NAME`](#security-cli-users-name) | str | - |
| [`SECURITY_​CONFIRMABLE`](#security-confirmable) | bool | `configure_generic_parameters` |
| [`SECURITY_​CONFIRM_​EMAIL_​WITHIN`](#security-confirm-email-within) | str | - |
| [`SECURITY_​CONFIRM_​ERROR_​VIEW`](#security-confirm-error-view) | NoneType | - |
| [`SECURITY_​CONFIRM_​SALT`](#security-confirm-salt) | str | - |
| [`SECURITY_​CONFIRM_​URL`](#security-confirm-url) | str | - |
| [`SECURITY_​DEFAULT_​HTTP_​AUTH_​REALM`](#security-default-http-auth-realm) | str | - |
| [`SECURITY_​DEFAULT_​REMEMBER_​ME`](#security-default-remember-me) | bool | - |
| [`SECURITY_​DEPRECATED_​HASHING_​SCHEMES`](#security-deprecated-hashing-schemes) | list | - |
| [`SECURITY_​DEPRECATED_​PASSWORD_​SCHEMES`](#security-deprecated-password-schemes) | list | - |
| [`SECURITY_​EMAIL_​HTML`](#security-email-html) | bool | - |
| [`SECURITY_​EMAIL_​PLAINTEXT`](#security-email-plaintext) | bool | - |
| [`SECURITY_​EMAIL_​SUBJECT_​CONFIRM`](#security-email-subject-confirm) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​PASSWORD_​CHANGE_​NOTICE`](#security-email-subject-password-change-notice) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​PASSWORD_​NOTICE`](#security-email-subject-password-notice) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​PASSWORD_​RESET`](#security-email-subject-password-reset) | str | - |
| [`SECURITY_​EMAIL_​SUBJECT_​REGISTER`](#security-email-subject-register) | str | - |
| [`SECURITY_​FLASH_​MESSAGES`](#security-flash-messages) | bool | - |
| [`SECURITY_​FORGOT_​PASSWORD_​TEMPLATE`](#security-forgot-password-template) | str | - |
| [`SECURITY_​HASHING_​SCHEMES`](#security-hashing-schemes) | list | - |
| [`SECURITY_​I18N_​DIRNAME`](#security-i18n-dirname) | str | - |
| [`SECURITY_​I18N_​DOMAIN`](#security-i18n-domain) | str | - |
| [`SECURITY_​LOGIN_​SALT`](#security-login-salt) | str | - |
| [`SECURITY_​LOGIN_​URL`](#security-login-url) | str | - |
| [`SECURITY_​LOGIN_​USER_​TEMPLATE`](#security-login-user-template) | str | - |
| [`SECURITY_​LOGIN_​WITHIN`](#security-login-within) | str | - |
| [`SECURITY_​LOGIN_​WITHOUT_​CONFIRMATION`](#security-login-without-confirmation) | bool | `configure_generic_parameters` |
| [`SECURITY_​LOGOUT_​URL`](#security-logout-url) | str | - |
| [`SECURITY_​MSG_​ALREADY_​CONFIRMED`](#security-msg-already-confirmed) | tuple | - |
| [`SECURITY_​MSG_​CONFIRMATION_​EXPIRED`](#security-msg-confirmation-expired) | tuple | - |
| [`SECURITY_​MSG_​CONFIRMATION_​REQUEST`](#security-msg-confirmation-request) | tuple | - |
| [`SECURITY_​MSG_​CONFIRMATION_​REQUIRED`](#security-msg-confirmation-required) | tuple | - |
| [`SECURITY_​MSG_​CONFIRM_​REGISTRATION`](#security-msg-confirm-registration) | tuple | - |
| [`SECURITY_​MSG_​DISABLED_​ACCOUNT`](#security-msg-disabled-account) | tuple | - |
| [`SECURITY_​MSG_​EMAIL_​ALREADY_​ASSOCIATED`](#security-msg-email-already-associated) | tuple | - |
| [`SECURITY_​MSG_​EMAIL_​CONFIRMED`](#security-msg-email-confirmed) | tuple | - |
| [`SECURITY_​MSG_​EMAIL_​NOT_​PROVIDED`](#security-msg-email-not-provided) | tuple | - |
| [`SECURITY_​MSG_​FORGOT_​PASSWORD`](#security-msg-forgot-password) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​CONFIRMATION_​TOKEN`](#security-msg-invalid-confirmation-token) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​EMAIL_​ADDRESS`](#security-msg-invalid-email-address) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​LOGIN_​TOKEN`](#security-msg-invalid-login-token) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​PASSWORD`](#security-msg-invalid-password) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​REDIRECT`](#security-msg-invalid-redirect) | tuple | - |
| [`SECURITY_​MSG_​INVALID_​RESET_​PASSWORD_​TOKEN`](#security-msg-invalid-reset-password-token) | tuple | - |
| [`SECURITY_​MSG_​LOCAL_​LOGIN_​DISABLED`](#security-msg-local-login-disabled) | tuple | - |
| [`SECURITY_​MSG_​LOGIN`](#security-msg-login) | tuple | - |
| [`SECURITY_​MSG_​LOGIN_​EMAIL_​SENT`](#security-msg-login-email-sent) | tuple | - |
| [`SECURITY_​MSG_​LOGIN_​EXPIRED`](#security-msg-login-expired) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​BREACHED`](#security-msg-password-breached) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​BREACHED_​SITE_​ERROR`](#security-msg-password-breached-site-error) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​CHANGE`](#security-msg-password-change) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​CHANGE_​DISABLED`](#security-msg-password-change-disabled) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​INVALID_​LENGTH`](#security-msg-password-invalid-length) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​IS_​THE_​SAME`](#security-msg-password-is-the-same) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​MISMATCH`](#security-msg-password-mismatch) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​NOT_​PROVIDED`](#security-msg-password-not-provided) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​NOT_​SET`](#security-msg-password-not-set) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RECOVERY_​DISABLED`](#security-msg-password-recovery-disabled) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET`](#security-msg-password-reset) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET_​DISABLED`](#security-msg-password-reset-disabled) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET_​EXPIRED`](#security-msg-password-reset-expired) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​RESET_​REQUEST`](#security-msg-password-reset-request) | tuple | - |
| [`SECURITY_​MSG_​PASSWORD_​TOO_​SIMPLE`](#security-msg-password-too-simple) | tuple | - |
| [`SECURITY_​MSG_​REFRESH`](#security-msg-refresh) | tuple | - |
| [`SECURITY_​MSG_​REGISTRATION_​DISABLED`](#security-msg-registration-disabled) | tuple | - |
| [`SECURITY_​MSG_​RETYPE_​PASSWORD_​MISMATCH`](#security-msg-retype-password-mismatch) | tuple | - |
| [`SECURITY_​MSG_​UNAUTHORIZED`](#security-msg-unauthorized) | tuple | - |
| [`SECURITY_​MSG_​USER_​DOES_​NOT_​EXIST`](#security-msg-user-does-not-exist) | tuple | - |
| [`SECURITY_​PASSWORD_​BREACHED_​COUNT`](#security-password-breached-count) | int | - |
| [`SECURITY_​PASSWORD_​CHECK_​BREACHED`](#security-password-check-breached) | bool | - |
| [`SECURITY_​PASSWORD_​COMPLEXITY_​CHECKER`](#security-password-complexity-checker) | NoneType | - |
| [`SECURITY_​PASSWORD_​HASH`](#security-password-hash) | str | - |
| [`SECURITY_​PASSWORD_​LENGTH_​MIN`](#security-password-length-min) | int | - |
| [`SECURITY_​PASSWORD_​SALT`](#security-password-salt) | str | - |
| [`SECURITY_​PASSWORD_​SCHEMES`](#security-password-schemes) | list | - |
| [`SECURITY_​PASSWORD_​SINGLE_​HASH`](#security-password-single-hash) | list | - |
| [`SECURITY_​POST_​CHANGE_​VIEW`](#security-post-change-view) | NoneType | - |
| [`SECURITY_​POST_​CONFIRM_​VIEW`](#security-post-confirm-view) | NoneType | - |
| [`SECURITY_​POST_​LOGIN_​VIEW`](#security-post-login-view) | str | - |
| [`SECURITY_​POST_​LOGOUT_​VIEW`](#security-post-logout-view) | str | - |
| [`SECURITY_​POST_​REGISTER_​VIEW`](#security-post-register-view) | NoneType | - |
| [`SECURITY_​POST_​RESET_​VIEW`](#security-post-reset-view) | NoneType | - |
| [`SECURITY_​RECOVERABLE`](#security-recoverable) | bool | `configure_generic_parameters` |
| [`SECURITY_​REGISTERABLE`](#security-registerable) | bool | `configure_generic_parameters` |
| [`SECURITY_​REGISTER_​URL`](#security-register-url) | str | - |
| [`SECURITY_​REGISTER_​USER_​TEMPLATE`](#security-register-user-template) | str | - |
| [`SECURITY_​RESET_​PASSWORD_​TEMPLATE`](#security-reset-password-template) | str | - |
| [`SECURITY_​RESET_​PASSWORD_​WITHIN`](#security-reset-password-within) | str | - |
| [`SECURITY_​RESET_​SALT`](#security-reset-salt) | str | - |
| [`SECURITY_​RESET_​URL`](#security-reset-url) | str | - |
| [`SECURITY_​SEND_​CONFIRMATION_​TEMPLATE`](#security-send-confirmation-template) | str | - |
| [`SECURITY_​SEND_​LOGIN_​TEMPLATE`](#security-send-login-template) | str | - |
| [`SECURITY_​SEND_​PASSWORD_​CHANGE_​EMAIL`](#security-send-password-change-email) | bool | - |
| [`SECURITY_​SEND_​PASSWORD_​RESET_​EMAIL`](#security-send-password-reset-email) | bool | - |
| [`SECURITY_​SEND_​PASSWORD_​RESET_​NOTICE_​EMAIL`](#security-send-password-reset-notice-email) | bool | - |
| [`SECURITY_​SEND_​REGISTER_​EMAIL`](#security-send-register-email) | bool | - |
| [`SECURITY_​SUBDOMAIN`](#security-subdomain) | NoneType | - |
| [`SECURITY_​TOKEN_​AUTHENTICATION_​HEADER`](#security-token-authentication-header) | str | - |
| [`SECURITY_​TOKEN_​AUTHENTICATION_​KEY`](#security-token-authentication-key) | str | - |
| [`SECURITY_​TOKEN_​MAX_​AGE`](#security-token-max-age) | NoneType | - |
| [`SECURITY_​TRACKABLE`](#security-trackable) | bool | - |
| [`SECURITY_​URL_​PREFIX`](#security-url-prefix) | NoneType | - |
| [`SECURITY_​USER_​IDENTITY_​ATTRIBUTES`](#security-user-identity-attributes) | list | - |
| [`SECURITY_​ZXCVBN_​MINIMUM_​SCORE`](#security-zxcvbn-minimum-score) | int | - |
| [`SEND_​FILE_​MAX_​AGE_​DEFAULT`](#send-file-max-age-default) | NoneType | `configure_generic_parameters` |
| [`SENTRY_​DSN`](#sentry-dsn) | NoneType | - |
| [`SERVER_​NAME`](#server-name) | NoneType | - |
| [`SESSION_​COOKIE_​DOMAIN`](#session-cookie-domain) | NoneType | `configure_generic_parameters` |
| [`SESSION_​COOKIE_​HTTPONLY`](#session-cookie-httponly) | bool | - |
| [`SESSION_​COOKIE_​NAME`](#session-cookie-name) | str | - |
| [`SESSION_​COOKIE_​PARTITIONED`](#session-cookie-partitioned) | bool | - |
| [`SESSION_​COOKIE_​PATH`](#session-cookie-path) | NoneType | - |
| [`SESSION_​COOKIE_​SAMESITE`](#session-cookie-samesite) | str | - |
| [`SESSION_​COOKIE_​SECURE`](#session-cookie-secure) | bool | `configure_generic_parameters` |
| [`SESSION_​KEY_​BITS`](#session-key-bits) | int | - |
| [`SESSION_​RANDOM_​SOURCE`](#session-random-source) | SystemRandom | - |
| [`SESSION_​REFRESH_​EACH_​REQUEST`](#session-refresh-each-request) | bool | - |
| [`SETTINGS_​TEMPLATE`](#settings-template) | str | `configure_ui` |
| [`SITEMAP_​MAX_​ENTRY_​COUNT`](#sitemap-max-entry-count) | int | - |
| [`SITEMAP_​ROOT_​VIEW_​ENABLED`](#sitemap-root-view-enabled) | bool | - |
| [`SITEMAP_​SECTIONS`](#sitemap-sections) | list | - |
| [`SITE_​API_​URL`](#site-api-url) | str | `configure_generic_parameters` |
| [`SITE_​UI_​URL`](#site-ui-url) | str | `configure_generic_parameters` |
| [`SQLALCHEMY_​BINDS`](#sqlalchemy-binds) | dict | - |
| [`SQLALCHEMY_​DATABASE_​URI`](#sqlalchemy-database-uri) | str | `configure_generic_parameters` |
| [`SQLALCHEMY_​ECHO`](#sqlalchemy-echo) | bool | - |
| [`SQLALCHEMY_​ENGINE_​OPTIONS`](#sqlalchemy-engine-options) | dict | - |
| [`SQLALCHEMY_​RECORD_​QUERIES`](#sqlalchemy-record-queries) | bool | - |
| [`SQLALCHEMY_​TRACK_​MODIFICATIONS`](#sqlalchemy-track-modifications) | bool | - |
| [`STATS_​AGGREGATIONS`](#stats-aggregations) | dict | - |
| [`STATS_​EVENTS`](#stats-events) | dict | - |
| [`STATS_​EVENTS_​UTC_​DATETIME_​ENABLED`](#stats-events-utc-datetime-enabled) | bool | - |
| [`STATS_​MQ_​EXCHANGE`](#stats-mq-exchange) | unknown | - |
| [`STATS_​PERMISSION_​FACTORY`](#stats-permission-factory) | unknown | - |
| [`STATS_​QUERIES`](#stats-queries) | dict | - |
| [`STATS_​REGISTER_​INDEX_​TEMPLATES`](#stats-register-index-templates) | bool | - |
| [`STATS_​REGISTER_​RECEIVERS`](#stats-register-receivers) | bool | `configure_stats` |
| [`TEMPLATES_​AUTO_​RELOAD`](#templates-auto-reload) | NoneType | - |
| [`TESTING`](#testing) | bool | - |
| [`THEME_​401_​TEMPLATE`](#theme-401-template) | str | - |
| [`THEME_​403_​TEMPLATE`](#theme-403-template) | str | - |
| [`THEME_​404_​TEMPLATE`](#theme-404-template) | str | - |
| [`THEME_​429_​TEMPLATE`](#theme-429-template) | str | - |
| [`THEME_​500_​TEMPLATE`](#theme-500-template) | str | - |
| [`THEME_​BASE_​TEMPLATE`](#theme-base-template) | str | - |
| [`THEME_​COVER_​TEMPLATE`](#theme-cover-template) | str | - |
| [`THEME_​CSS_​TEMPLATE`](#theme-css-template) | configured by function | `configure_ui` |
| [`THEME_​ERROR_​TEMPLATE`](#theme-error-template) | str | - |
| [`THEME_​FOOTER_​TEMPLATE`](#theme-footer-template) | str | `configure_ui` |
| [`THEME_​FRONTPAGE`](#theme-frontpage) | bool | `configure_ui` |
| [`THEME_​FRONTPAGE_​LOGO`](#theme-frontpage-logo) | configured by function | `configure_ui` |
| [`THEME_​FRONTPAGE_​TEMPLATE`](#theme-frontpage-template) | str | `configure_ui` |
| [`THEME_​FRONTPAGE_​TITLE`](#theme-frontpage-title) | LazyString | `configure_ui` |
| [`THEME_​GENERATOR`](#theme-generator) | str | - |
| [`THEME_​GOOGLE_​SITE_​VERIFICATION`](#theme-google-site-verification) | list | - |
| [`THEME_​HEADER_​LOGIN_​TEMPLATE`](#theme-header-login-template) | str | `configure_ui` |
| [`THEME_​HEADER_​TEMPLATE`](#theme-header-template) | str | `configure_ui` |
| [`THEME_​ICONS`](#theme-icons) | dict | - |
| [`THEME_​JAVASCRIPT_​TEMPLATE`](#theme-javascript-template) | str | `configure_ui` |
| [`THEME_​LOGO`](#theme-logo) | str | `configure_ui` |
| [`THEME_​LOGO_​ADMIN`](#theme-logo-admin) | str | - |
| [`THEME_​MATHJAX_​CDN`](#theme-mathjax-cdn) | str | - |
| [`THEME_​META_​ROBOT_​TAGS`](#theme-meta-robot-tags) | list | - |
| [`THEME_​SEARCHBAR`](#theme-searchbar) | bool | - |
| [`THEME_​SEARCH_​ENDPOINT`](#theme-search-endpoint) | str | `configure_ui` |
| [`THEME_​SETTINGS_​TEMPLATE`](#theme-settings-template) | str | - |
| [`THEME_​SHOW_​FRONTPAGE_​INTRO_​SECTION`](#theme-show-frontpage-intro-section) | unknown | `configure_ui` |
| [`THEME_​SITENAME`](#theme-sitename) | LazyString | `configure_ui` |
| [`THEME_​SITEURL`](#theme-siteurl) | str | - |
| [`THEME_​TRACKINGCODE_​TEMPLATE`](#theme-trackingcode-template) | str | `configure_ui` |
| [`THEME_​TWITTERHANDLE`](#theme-twitterhandle) | unknown | - |
| [`TRAP_​BAD_​REQUEST_​ERRORS`](#trap-bad-request-errors) | NoneType | - |
| [`TRAP_​HTTP_​EXCEPTIONS`](#trap-http-exceptions) | bool | - |
| [`TRUSTED_​HOSTS`](#trusted-hosts) | NoneType | - |
| [`TYPE_​CHECKING`](#type-checking) | bool | - |
| [`USERPROFILES`](#userprofiles) | bool | - |
| [`USERPROFILES_​BASE_​TEMPLATE`](#userprofiles-base-template) | str | - |
| [`USERPROFILES_​EMAIL_​ENABLED`](#userprofiles-email-enabled) | bool | - |
| [`USERPROFILES_​EXTEND_​SECURITY_​FORMS`](#userprofiles-extend-security-forms) | bool | - |
| [`USERPROFILES_​PROFILE_​TEMPLATE`](#userprofiles-profile-template) | str | - |
| [`USERPROFILES_​PROFILE_​URL`](#userprofiles-profile-url) | str | - |
| [`USERPROFILES_​READ_​ONLY`](#userprofiles-read-only) | bool | `configure_generic_parameters`, `configure_einfra_oidc` |
| [`USERPROFILES_​SETTINGS_​TEMPLATE`](#userprofiles-settings-template) | str | - |
| [`USERS_​RESOURCES_​AVATAR_​COLORS`](#users-resources-avatar-colors) | list | - |
| [`USERS_​RESOURCES_​DOMAINS_​ORG_​SCHEMA`](#users-resources-domains-org-schema) | unknown | - |
| [`USERS_​RESOURCES_​DOMAINS_​SEARCH`](#users-resources-domains-search) | dict | - |
| [`USERS_​RESOURCES_​DOMAINS_​SEARCH_​FACETS`](#users-resources-domains-search-facets) | dict | - |
| [`USERS_​RESOURCES_​DOMAINS_​SORT_​OPTIONS`](#users-resources-domains-sort-options) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ADMIN_​FACETS`](#users-resources-groups-admin-facets) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ADMIN_​SEARCH`](#users-resources-groups-admin-search) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ADMIN_​SORT_​OPTIONS`](#users-resources-groups-admin-sort-options) | dict | - |
| [`USERS_​RESOURCES_​GROUPS_​ENABLED`](#users-resources-groups-enabled) | bool | - |
| [`USERS_​RESOURCES_​MODERATION_​LOCK_​DEFAULT_​TIMEOUT`](#users-resources-moderation-lock-default-timeout) | int | - |
| [`USERS_​RESOURCES_​MODERATION_​LOCK_​RENEWAL_​TIMEOUT`](#users-resources-moderation-lock-renewal-timeout) | int | - |
| [`USERS_​RESOURCES_​PROTECTED_​GROUP_​NAMES`](#users-resources-protected-group-names) | list | - |
| [`USERS_​RESOURCES_​SEARCH`](#users-resources-search) | dict | - |
| [`USERS_​RESOURCES_​SEARCH_​FACETS`](#users-resources-search-facets) | dict | - |
| [`USERS_​RESOURCES_​SERVICE_​SCHEMA`](#users-resources-service-schema) | unknown | - |
| [`USERS_​RESOURCES_​SORT_​OPTIONS`](#users-resources-sort-options) | dict | - |
| [`USER_​DASHBOARD_​MENU_​OVERRIDES`](#user-dashboard-menu-overrides) | dict | - |
| [`USE_​X_​SENDFILE`](#use-x-sendfile) | bool | - |
| [`VCS_​TEMPLATE_​INDEX`](#vcs-template-index) | unknown | - |
| [`VCS_​TEMPLATE_​INDEX_​ITEM`](#vcs-template-index-item) | unknown | - |
| [`VCS_​TEMPLATE_​RELEASE_​ITEM`](#vcs-template-release-item) | unknown | - |
| [`VCS_​TEMPLATE_​REPO_​SWITCH`](#vcs-template-repo-switch) | unknown | - |
| [`VCS_​TEMPLATE_​VIEW`](#vcs-template-view) | unknown | - |
| [`VOCABULARIES_​AFFILIATIONS_​EDMO_​COUNTRY_​MAPPING`](#vocabularies-affiliations-edmo-country-mapping) | dict | - |
| [`VOCABULARIES_​AFFILIATION_​SCHEMES`](#vocabularies-affiliation-schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_​AWARDS_​EC_​ROR_​ID`](#vocabularies-awards-ec-ror-id) | str | - |
| [`VOCABULARIES_​AWARDS_​OPENAIRE_​FUNDERS`](#vocabularies-awards-openaire-funders) | dict | - |
| [`VOCABULARIES_​AWARD_​SCHEMES`](#vocabularies-award-schemes) | dict | - |
| [`VOCABULARIES_​CF`](#vocabularies-cf) | list | - |
| [`VOCABULARIES_​CUSTOM_​VOCABULARY_​TYPES`](#vocabularies-custom-vocabulary-types) | list | - |
| [`VOCABULARIES_​DATASTREAM_​READERS`](#vocabularies-datastream-readers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_​DATASTREAM_​TRANSFORMERS`](#vocabularies-datastream-transformers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_​DATASTREAM_​WRITERS`](#vocabularies-datastream-writers) | dict | `configure_datastreams`, `configure_generic_parameters` |
| [`VOCABULARIES_​FACET_​CACHE_​SIZE`](#vocabularies-facet-cache-size) | int | - |
| [`VOCABULARIES_​FACET_​CACHE_​TTL`](#vocabularies-facet-cache-ttl) | int | - |
| [`VOCABULARIES_​FUNDER_​DOI_​PREFIX`](#vocabularies-funder-doi-prefix) | str | - |
| [`VOCABULARIES_​FUNDER_​SCHEMES`](#vocabularies-funder-schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_​IDENTIFIER_​SCHEMES`](#vocabularies-identifier-schemes) | dict | - |
| [`VOCABULARIES_​NAMES_​SCHEMES`](#vocabularies-names-schemes) | dict | `configure_generic_parameters` |
| [`VOCABULARIES_​ORCID_​ACCESS_​KEY`](#vocabularies-orcid-access-key) | str | - |
| [`VOCABULARIES_​ORCID_​ORG_​IDS_​MAPPING_​PATH`](#vocabularies-orcid-org-ids-mapping-path) | NoneType | - |
| [`VOCABULARIES_​ORCID_​SECRET_​KEY`](#vocabularies-orcid-secret-key) | str | - |
| [`VOCABULARIES_​ORCID_​SUMMARIES_​BUCKET`](#vocabularies-orcid-summaries-bucket) | str | - |
| [`VOCABULARIES_​ORCID_​SYNC_​MAX_​WORKERS`](#vocabularies-orcid-sync-max-workers) | int | - |
| [`VOCABULARIES_​ORCID_​SYNC_​SINCE`](#vocabularies-orcid-sync-since) | dict | - |
| [`VOCABULARIES_​RESOURCE_​CONFIG`](#vocabularies-resource-config) | unknown | `configure_generic_parameters` |
| [`VOCABULARIES_​SERVICE_​CONFIG`](#vocabularies-service-config) | unknown | `configure_generic_parameters` |
| [`VOCABULARIES_​SUBJECTS_​EUROSCIVOC_​FILE_​URL`](#vocabularies-subjects-euroscivoc-file-url) | str | - |
| [`VOCABULARIES_​SUBJECTS_​GEMET_​FILE_​URL`](#vocabularies-subjects-gemet-file-url) | str | - |
| [`VOCABULARIES_​SUBJECTS_​NVS_​FILE_​URL`](#vocabularies-subjects-nvs-file-url) | str | - |
| [`VOCABULARIES_​SUBJECTS_​SCHEMES`](#vocabularies-subjects-schemes) | dict | - |
| [`VOCABULARIES_​TYPES_​SEARCH`](#vocabularies-types-search) | dict | - |
| [`VOCABULARIES_​TYPES_​SORT_​OPTIONS`](#vocabularies-types-sort-options) | dict | - |
| [`VOCABULARY_​TYPE_​UI_​RESOURCE`](#vocabulary-type-ui-resource) | str | - |
| [`VOCABULARY_​TYPE_​UI_​RESOURCE_​CONFIG`](#vocabulary-type-ui-resource-config) | str | - |
| [`WEBPACKEXT_​MANIFEST_​PATH`](#webpackext-manifest-path) | str | - |
| [`WEBPACKEXT_​NPM_​PKG_​CLS`](#webpackext-npm-pkg-cls) | configured by function | `configure_ui` |
| [`WEBPACKEXT_​PROJECT`](#webpackext-project) | str | `configure_ui` |
| [`WEBPACKEXT_​PROJECT_​BUILDDIR`](#webpackext-project-builddir) | str | - |
| [`WEBPACKEXT_​PROJECT_​DISTDIR`](#webpackext-project-distdir) | str | - |
| [`WEBPACKEXT_​PROJECT_​DISTURL`](#webpackext-project-disturl) | str | - |
| [`WORKFLOWS`](#workflows) | dict | - |
| [`WORKFLOWS_​DEFAULT_​WORKFLOW`](#workflows-default-workflow) | str | - |

## Detailed Variable Reference
(access-action-cache-prefix)=
### ACCESS_ACTION_CACHE_PREFIX

```{eval-rst}
Prefix for actions cached when used in dynamic permissions.
```

| **Invenio RDM Default Value** | `'Permission::action::'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L21) |

---

(access-cache)=
### ACCESS_CACHE

```{eval-rst}
A cache instance or an importable string pointing to the cache instance.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L18); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L729) |

---

(access-load-system-role-needs)=
### ACCESS_LOAD_SYSTEM_ROLE_NEEDS

```{eval-rst}
Enables the loading of system role needs when users' identity change.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-access](https://github.com/inveniosoftware/invenio-access/blob/master/invenio_access/config.py#L24) |

---

(accounts)=
### ACCOUNTS

```{eval-rst}
Tells if the templates should use the accounts module.

If False, you won't be able to login via the web UI.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L21) |

---

(accounts-base-template)=
### ACCOUNTS_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(accounts-confirm-email-endpoint)=
### ACCOUNTS_CONFIRM_EMAIL_ENDPOINT

```{eval-rst}
Value to be used for the confirmation email link in the UI application.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L62) |

---

(accounts-cover-template)=
### ACCOUNTS_COVER_TEMPLATE
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(accounts-default-email-visibility)=
### ACCOUNTS_DEFAULT_EMAIL_VISIBILITY

```{eval-rst}
Default Email visibility value can be set to either 'restricted' or 'public'.
```

| **Invenio RDM Default Value** | `'restricted'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L65) |

---

(accounts-default-users-verified)=
### ACCOUNTS_DEFAULT_USERS_VERIFIED

```{eval-rst}
Default verified status: if set to 'True', users are verified by default.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L384) |

---

(accounts-default-user-visibility)=
### ACCOUNTS_DEFAULT_USER_VISIBILITY

```{eval-rst}
Default User visibility value can be set to either 'restricted' or 'public'.
```

| **Invenio RDM Default Value** | `'restricted'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L364) |

---

(accounts-forgot-password-email-ratelimit)=
### ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT

```{eval-rst}
Flask-Limiter rate limit string for forgot-password requests per account.

Example: ``"3 per hour"``. Disabled when ``None``.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L91) |

---

(accounts-forgot-password-email-ratelimit-key-prefix)=
### ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_KEY_PREFIX

```{eval-rst}
Prefix used to namespace forgot-password per-account limiter keys.
```

| **Invenio RDM Default Value** | `'accounts.fp_email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L97) |

---

(accounts-forgot-password-email-ratelimit-msg)=
### ACCOUNTS_FORGOT_PASSWORD_EMAIL_RATELIMIT_MSG
| **Invenio RDM Default Value** | `l'Too many password-reset requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L100) |

---

(accounts-jwt-alogorithm)=
### ACCOUNTS_JWT_ALOGORITHM

```{eval-rst}
Set JWT encryption alogirthm.

.. note::

   `Available aglorithms
   <https://pyjwt.readthedocs.io/en/latest/algorithms.html>`_
```

| **Invenio RDM Default Value** | `'HS256'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L323) |

---

(accounts-jwt-creation-factory)=
### ACCOUNTS_JWT_CREATION_FACTORY

```{eval-rst}
Import path of factory used to generate JWT.
```

| **Invenio RDM Default Value** | `'invenio_accounts.utils:jwt_create_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L335) |

---

(accounts-jwt-decode-factory)=
### ACCOUNTS_JWT_DECODE_FACTORY

```{eval-rst}
Import path of factory used to decode JWT.
```

| **Invenio RDM Default Value** | `'invenio_accounts.utils:jwt_decode_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L332) |

---

(accounts-jwt-dom-token)=
### ACCOUNTS_JWT_DOM_TOKEN

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L277) |

---

(accounts-jwt-dom-token-template)=
### ACCOUNTS_JWT_DOM_TOKEN_TEMPLATE

```{eval-rst}
Template for the context processor.
```

| **Invenio RDM Default Value** | `'invenio_accounts/jwt.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L309) |

---

(accounts-jwt-enable)=
### ACCOUNTS_JWT_ENABLE

```{eval-rst}
Enable JWT support.

.. note::

    More details about `JWT <https://jwt.io>`_
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L269) |

---

(accounts-jwt-expiration-delta)=
### ACCOUNTS_JWT_EXPIRATION_DELTA

```{eval-rst}
Token expiration period for JWT.
```

| **Invenio RDM Default Value** | `datetime.timedelta(days=1)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L320) |

---

(accounts-jwt-secret-key)=
### ACCOUNTS_JWT_SECRET_KEY

```{eval-rst}
Secret key for JWT.

.. note::

    If is set to ``None`` it will use the ``SECRET_KEY``.
```

| **Invenio RDM Default Value** | `'CHANGE_ME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L312) |

---

(accounts-local-login-enabled)=
### ***ACCOUNTS_LOCAL_LOGIN_ENABLED**

```{eval-rst}
Whether or not login with local account credentials should be enabled.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L355) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(accounts-login-ratelimit)=
### ACCOUNTS_LOGIN_RATELIMIT

```{eval-rst}
Flask-Limiter rate limit string for login requests per account.

Example: ``"5 per 15 minutes"``. Disabled when ``None``.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L105) |

---

(accounts-login-ratelimit-key-prefix)=
### ACCOUNTS_LOGIN_RATELIMIT_KEY_PREFIX

```{eval-rst}
Prefix used to namespace login per-account limiter keys.
```

| **Invenio RDM Default Value** | `'accounts.login'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L111) |

---

(accounts-login-ratelimit-msg)=
### ACCOUNTS_LOGIN_RATELIMIT_MSG
| **Invenio RDM Default Value** | `l'Too many login attempts for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L114) |

---

(accounts-login-view-function)=
### ***ACCOUNTS_LOGIN_VIEW_FUNCTION**

```{eval-rst}
The view function to use for the login endpoint.

This can be either an import string, or the view function itself.
If set to None, the default login view function from Flask-Security will be
left as is.
```

| **Invenio RDM Default Value** | `login` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L347) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(accounts-register-blueprint)=
### ACCOUNTS_REGISTER_BLUEPRINT

```{eval-rst}
Register the Security blueprint or not.

It can be used to override the ``register_blueprint`` option.

.. note:: If the value is ``None``, then the blueprint is not registered.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L42) |

---

(accounts-reset-password-endpoint)=
### ACCOUNTS_RESET_PASSWORD_ENDPOINT

```{eval-rst}
Value to be used for the confirmation email link in the UI application.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L78) |

---

(accounts-rest-auth-views)=
### ACCOUNTS_REST_AUTH_VIEWS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L133) |

```
{'change_password': 'invenio_accounts.views.rest:ChangePasswordView',
 'confirm_email': 'invenio_accounts.views.rest:ConfirmEmailView',
 'forgot_password': 'invenio_accounts.views.rest:ForgotPasswordView',
 'login': 'invenio_accounts.views.rest:LoginView',
 'logout': 'invenio_accounts.views.rest:LogoutView',
 'register': 'invenio_accounts.views.rest:RegisterView',
 'reset_password': 'invenio_accounts.views.rest:ResetPasswordView',
 'send_confirmation': 'invenio_accounts.views.rest:SendConfirmationEmailView',
 'sessions_item': 'invenio_accounts.views.rest:SessionsItemView',
 'sessions_list': 'invenio_accounts.views.rest:SessionsListView',
 'user_info': 'invenio_accounts.views.rest:UserInfoView'}
```

---

(accounts-rest-confirm-email-endpoint)=
### ACCOUNTS_REST_CONFIRM_EMAIL_ENDPOINT

```{eval-rst}
Value to be used for the confirmation email link in the API application.

Can be a Flask endpoint (e.g. "invenio_accounts_rest_auth.confirm_email"), or
a URL part (e.g. "https://ui.example.com/confirm-email", "/confirm-email").

This will be used to build an absolute URL, thus if e.g. a hostname isn't
included, the one from the current request's context will be used.
```

| **Invenio RDM Default Value** | `'/confirm/{token}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L68) |

---

(accounts-rest-reset-password-endpoint)=
### ACCOUNTS_REST_RESET_PASSWORD_ENDPOINT

```{eval-rst}
Value to be used for the reset password link in the API application.

Can be a Flask endpoint (e.g. "invenio_accounts_rest_auth.reset_password"), or
a URL part (e.g. "https://ui.example.com/reset-password", "/reset-password").

This will be used to build an absolute URL, thus if e.g. a hostname isn't
included, the one from the current request's context will be used.
```

| **Invenio RDM Default Value** | `'/lost-password/{token}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L81) |

---

(accounts-retention-period)=
### ACCOUNTS_RETENTION_PERIOD
| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L27) |

---

(accounts-send-confirmation-ratelimit)=
### ACCOUNTS_SEND_CONFIRMATION_RATELIMIT

```{eval-rst}
Flask-Limiter rate limit string for send-confirmation requests per account.

Example: ``"3 per hour"``. Disabled when ``None``.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L119) |

---

(accounts-send-confirmation-ratelimit-key-prefix)=
### ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_KEY_PREFIX

```{eval-rst}
Prefix used to namespace send-confirmation per-account limiter keys.
```

| **Invenio RDM Default Value** | `'accounts.cf_email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L125) |

---

(accounts-send-confirmation-ratelimit-msg)=
### ACCOUNTS_SEND_CONFIRMATION_RATELIMIT_MSG
| **Invenio RDM Default Value** | `l'Too many confirmation-email requests for this account. Please try again later.'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L128) |

---

(accounts-session-activity-enabled)=
### ACCOUNTS_SESSION_ACTIVITY_ENABLED

```{eval-rst}
Enable session activity tracking.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L56) |

---

(accounts-session-redis-url)=
### ***ACCOUNTS_SESSION_REDIS_URL**

```{eval-rst}
Redis URL used by the module as a cache system for sessions.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L39); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L395) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(accounts-session-store-factory)=
### ACCOUNTS_SESSION_STORE_FACTORY
| **Invenio RDM Default Value** | `'invenio_accounts.sessions:default_session_store_factory'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L29) |

---

(accounts-settings-security-template)=
### ACCOUNTS_SETTINGS_SECURITY_TEMPLATE

```{eval-rst}
Template for the account security page.
```

| **Invenio RDM Default Value** | `'invenio_accounts/settings/security.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L59) |

---

(accounts-settings-template)=
### ACCOUNTS_SETTINGS_TEMPLATE
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(accounts-sitename)=
### ACCOUNTS_SITENAME
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | unknown |

---

(accounts-userinfo-headers)=
### ACCOUNTS_USERINFO_HEADERS

```{eval-rst}
If True, add X-Session-ID and X-User-ID to the HTTP response.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L344); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L398) |

---

(accounts-username-regex)=
### ACCOUNTS_USERNAME_REGEX

```{eval-rst}
The regular expression used for validating usernames.

.. note:: When this configuration value is overridden, the value for
          ``ACCOUNTS_USERNAME_RULES_TEXT`` should be updated as well,
          to reflect the changes.
```

| **Invenio RDM Default Value** | `'^[a-zA-Z][a-zA-Z0-9-_]{2,255}$'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L367) |

---

(accounts-username-rules-text)=
### ACCOUNTS_USERNAME_RULES_TEXT
| **Invenio RDM Default Value** | `l'Username must start with a letter, be at least three characters long and only contain alphanumeric...` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L375) |

---

(accounts-user-preferences-schema)=
### ACCOUNTS_USER_PREFERENCES_SCHEMA

```{eval-rst}
The schema to use for validation of the user preferences.
```

| **Invenio RDM Default Value** | `<UserPreferencesSchema(many=False)>` |
|--------------|-----------|
| **Type** | UserPreferencesSchema |
| **Sources** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L358); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L407) |

---

(accounts-user-profile-schema)=
### ACCOUNTS_USER_PROFILE_SCHEMA

```{eval-rst}
The schema to use for validation of the user profile.
```

| **Invenio RDM Default Value** | `<UserProfileSchema(many=False)>` |
|--------------|-----------|
| **Type** | UserProfileSchema |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L361) |

---

(accounts-use-celery)=
### ACCOUNTS_USE_CELERY

```{eval-rst}
Tells if the module should use Celery or not.

By default, it uses Celery if it can find it.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L50) |

---

(administration-appname)=
### ADMINISTRATION_APPNAME

```{eval-rst}
Name of the Flask-Admin app (also the page title of admin panel).
```

| **Invenio RDM Default Value** | `'Invenio-Administration'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L15) |

---

(administration-base-template)=
### ADMINISTRATION_BASE_TEMPLATE

```{eval-rst}
Admin panel base template.
By default (``None``) uses the Flask-Admin template.
```

| **Invenio RDM Default Value** | `'invenio_administration/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L11) |

---

(administration-dashboard-view)=
### ADMINISTRATION_DASHBOARD_VIEW
| **Invenio RDM Default Value** | `'invenio_administration.views.dashboard.AdminDashboardView'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L18) |

---

(administration-display-versions)=
### ADMINISTRATION_DISPLAY_VERSIONS

```{eval-rst}
Display packages versions in the admin panel side bar.

Accepts a list of tuples in the format (package name, version).
Example: [("my-app", "v1.3.2")]
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L26); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1540) |

```
[]
```

---

(administration-theme-base-template)=
### ***ADMINISTRATION_THEME_BASE_TEMPLATE**

```{eval-rst}
Administration base template.
```

| **Invenio RDM Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-administration](https://github.com/inveniosoftware/invenio-administration/blob/master/invenio_administration/config.py#L23); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1543) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(admin-base-template)=
### ADMIN_BASE_TEMPLATE

```{eval-rst}
Base template for the administration interface.

The template changes the administration interface from using a standard
Bootstrap interface to using
`AdminLTE 2 <https://almsaeedstudio.com/themes/AdminLTE/index2.html>`_.

The variable is defined in Invenio-Admin which will use the value defined here
if Invenio-Theme is installed.
```

| **Invenio RDM Default Value** | `'invenio_theme/page_admin.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L27) |

---

(alembic)=
### ALEMBIC
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'script_location': '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_db/alembic',
 'version_locations': [('jobs',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_jobs/alembic'),
                       ('invenio_collections',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_collections/alembic'),
                       ('oarepo_requests',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/oarepo_requests/alembic'),
                       ('invenio_rdm_records',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_rdm_records/alembic'),
                       ('invenio_checks',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_checks/alembic'),
                       ('invenio_banners',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_banners/alembic'),
                       ('invenio_oauth2server',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauth2server/alembic'),
                       ('oarepo_doi',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/oarepo_doi/alembic'),
                       ('invenio_records_files',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records_files/alembic'),
                       ('invenio_oaiserver',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oaiserver/alembic'),
                       ('invenio_pidstore',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pidstore/alembic'),
                       ('invenio_communities',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_communities/alembic'),
                       ('invenio_accounts',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_accounts/alembic'),
                       ('invenio_requests',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_requests/alembic'),
                       ('oarepo_vocabularies',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/oarepo_vocabularies/alembic'),
                       ('invenio_userprofiles',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_userprofiles/alembic'),
                       ('invenio_files_rest',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_files_rest/alembic'),
                       ('invenio_audit_logs',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_audit_logs/alembic'),
                       ('invenio_vocabularies',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_vocabularies/alembic'),
                       ('invenio_access',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_access/alembic'),
                       ('invenio_oauthclient',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_oauthclient/alembic'),
                       ('invenio_records',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_records/alembic'),
                       ('invenio_pages',
                        '/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-packages/invenio_pages/alembic')]}
```

---

(alembic-context)=
### ALEMBIC_CONTEXT
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'compare_server_default': True,
 'compare_type': True,
 'transaction_per_migration': True}
```

---

(allowed-html-attrs)=
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

(allowed-html-tags)=
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

(application-root)=
### APPLICATION_ROOT
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(app-allowed-hosts)=
### ***APP_ALLOWED_HOSTS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/generic_parameters.py#L46) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(app-default-secure-headers)=
### ***APP_DEFAULT_SECURE_HEADERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L125) |
| **Set by** | {py:func}`~oarepo_config.configure_ui`, {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'content_security_policy': {'default-src': ["'self'"], 'object-src': ["'none'"]},
 'content_security_policy_report_only': False,
 'content_security_policy_report_uri': None,
 'force_file_save': False,
 'force_https': True,
 'force_https_permanent': False,
 'frame_options': 'sameorigin',
 'frame_options_allow_from': None,
 'session_cookie_http_only': True,
 'session_cookie_secure': True,
 'strict_transport_security': True,
 'strict_transport_security_include_subdomains': True,
 'strict_transport_security_max_age': 31556926,
 'strict_transport_security_preload': False}
```

---

(app-enable-secure-headers)=
### APP_ENABLE_SECURE_HEADERS

```{eval-rst}
Enable Secure Headers. (Default: ``True``)

In case you want to disable completely `Talisman`, you can set to `False`.

Remember that, for development purpose, setting ```DEBUG = True``` is already
enough to disable any side effects such as force ``https``.

.. note::
    `W3C
    <https://www.w3.org/TR/CSP2/>`_
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L112) |

---

(app-health-blueprint-enabled)=
### APP_HEALTH_BLUEPRINT_ENABLED

```{eval-rst}
Enable the ping (healthcheck) blueprint. (Default: ``False``)
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L188) |

---

(app-logs-permission-policy)=
### ***APP_LOGS_PERMISSION_POLICY**

```{eval-rst}
Permission policy for job logs.
```

| **Invenio RDM Default Value** | `JobLogsPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L29) |
| **Set by** | {py:func}`~oarepo_config.configure_jobs` |

---

(app-rdm-admin-email-recipient)=
### APP_RDM_ADMIN_EMAIL_RECIPIENT

```{eval-rst}
Admin e-mail
```

| **Invenio RDM Default Value** | `'info@inveniosoftware.org'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1042) |

---

(app-rdm-deposit-form-autocomplete-names)=
### APP_RDM_DEPOSIT_FORM_AUTOCOMPLETE_NAMES

```{eval-rst}
Behavior for autocomplete names search field for creators/contributors.

Available options:

- ``search`` (default): Show search field and form always.
- ``search_only``: Only show search field. Form displayed after selection or
  explicit "manual" entry.
- ``off``: Only show person form (no search field).
```

| **Invenio RDM Default Value** | `'search'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L988) |

---

(app-rdm-deposit-form-custom-field-defaults)=
### APP_RDM_DEPOSIT_FORM_CUSTOM_FIELD_DEFAULTS

```{eval-rst}
Default values for custom fields in new records in the deposit UI.

The keys denote the dot-separated path, where in the record's custom field
values should be set (see invenio-records.dictutils).
If the value is callable, its return value will be used for the field
(e.g. lambda/function for dynamic calculation of values).
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L979) |

```
{}
```

---

(app-rdm-deposit-form-defaults)=
### APP_RDM_DEPOSIT_FORM_DEFAULTS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L67); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L954) |

```
{'publication_date': <function <lambda> at 0x111faeb90>}
```

---

(app-rdm-deposit-form-publish-modal-extra)=
### APP_RDM_DEPOSIT_FORM_PUBLISH_MODAL_EXTRA

```{eval-rst}
Additional text/html to be displayed in the publish and submit for review modal.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1008) |

---

(app-rdm-deposit-form-quota)=
### ***APP_RDM_DEPOSIT_FORM_QUOTA**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L999) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

```
{
    'maxFiles': 100,
    'maxStorage': RDM_FILES_DEFAULT_QUOTA_SIZE,
}
```

---

(app-rdm-deposit-form-template)=
### APP_RDM_DEPOSIT_FORM_TEMPLATE

```{eval-rst}
Deposit page's form template.
```

| **Invenio RDM Default Value** | `'invenio_app_rdm/records/deposit.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L792) |

---

(app-rdm-deposit-ng-files-ui-enabled)=
### ***APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED**

```{eval-rst}
Feature toggle to enable the next-generation (NG) file uploader UI in the deposit form.

When enabled, the deposit form will use the new Uppy.io-based file uploader, replacing the current file upload interface.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L947) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(app-rdm-detail-side-bar-templates)=
### ***APP_RDM_DETAIL_SIDE_BAR_TEMPLATES**
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1018) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

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

(app-rdm-display-decimal-file-sizes)=
### APP_RDM_DISPLAY_DECIMAL_FILE_SIZES

```{eval-rst}
Display the file sizes in powers of 1000 (KB, ...) or 1024 (KiB, ...).
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1005) |

---

(app-rdm-files-integrity-report-subject)=
### APP_RDM_FILES_INTEGRITY_REPORT_SUBJECT

```{eval-rst}
Files integrity report subject
```

| **Invenio RDM Default Value** | `_('Files integrity report')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1039) |

---

(app-rdm-files-integrity-report-template)=
### APP_RDM_FILES_INTEGRITY_REPORT_TEMPLATE
| **Invenio RDM Default Value** | `'invenio_app_rdm/files_integrity_report/email/files_integrity_report.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1034) |

---

(app-rdm-identifier-schemes-ui)=
### ***APP_RDM_IDENTIFIER_SCHEMES_UI**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1045) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

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

(app-rdm-moderation-request-facets)=
### APP_RDM_MODERATION_REQUEST_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1595) |

```
{'is_open': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10deb0510>,
             'ui': {'field': 'is_open'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10de5f750>,
            'ui': {'field': 'status'}}}
```

---

(app-rdm-moderation-request-search)=
### APP_RDM_MODERATION_REQUEST_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1564) |

```
{'facets': ['status', 'is_open'],
 'sort': ['bestmatch', 'newest', 'oldest', 'newestactivity', 'oldestactivity']}
```

---

(app-rdm-moderation-request-sort-options)=
### APP_RDM_MODERATION_REQUEST_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1570) |

```
{'bestmatch': {'fields': ['_score'], 'title': 'Best match'},
 'newest': {'fields': ['-created'], 'title': 'Newest'},
 'newestactivity': {'fields': ['-last_activity_at'], 'title': 'Newest activity'},
 'oldest': {'fields': ['created'], 'title': 'Oldest'},
 'oldestactivity': {'fields': ['last_activity_at'], 'title': 'Oldest activity'}}
```

---

(app-rdm-pages)=
### APP_RDM_PAGES

```{eval-rst}
Register static pages with predefined initial content from 'pages.yaml' file.

Example:
{
    "about": "/about",
    "terms": "/terms",
    "privacy-policy": "/privacy-policy",
}
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1232) |

```
{}
```

---

(app-rdm-records-export-url)=
### APP_RDM_RECORDS_EXPORT_URL
| **Invenio RDM Default Value** | `'/records/<pid_value>/export/<export_format>'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L945) |

---

(app-rdm-record-exporters)=
### APP_RDM_RECORD_EXPORTERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L823) |

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

(app-rdm-record-landing-page-external-links)=
### APP_RDM_RECORD_LANDING_PAGE_EXTERNAL_LINKS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L924) |

```
[]
```

---

(app-rdm-record-landing-page-fair-signposting-level-1-enabled)=
### APP_RDM_RECORD_LANDING_PAGE_FAIR_SIGNPOSTING_LEVEL_1_ENABLED
| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1013) |

---

(app-rdm-record-landing-page-template)=
### APP_RDM_RECORD_LANDING_PAGE_TEMPLATE
| **OARepo Default Value** | `'oarepo_rdm/record_detail_iframe.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L65); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1011) |

---

(app-rdm-record-thumbnail-sizes)=
### APP_RDM_RECORD_THUMBNAIL_SIZES

```{eval-rst}
Allowed record thumbnail sizes.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1015) |

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

(app-rdm-routes)=
### APP_RDM_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L801) |

```
{'dashboard_home': '/me',
 'deposit_create': '/uploads/new',
 'deposit_edit': '/uploads/<pid_value>',
 'help_search': '/help/search',
 'help_statistics': '/help/statistics',
 'help_versioning': '/help/versioning',
 'index': '/',
 'record_container_item_download': '/records/<pid_value>/files/<path:filename>/container/<path:path>',
 'record_container_item_preview': '/records/<pid_value>/preview/<path:filename>/container/<path:path>',
 'record_detail': '/records/<pid_value>',
 'record_export': '/records/<pid_value>/export/<export_format>',
 'record_file_download': '/records/<pid_value>/files/<path:filename>',
 'record_file_preview': '/records/<pid_value>/preview/<path:filename>',
 'record_from_pid': '/<any({schemes}):pid_scheme>/<path:pid_value>',
 'record_latest': '/records/<pid_value>/latest',
 'record_media_file_download': '/records/<pid_value>/media-files/<path:filename>',
 'record_search': '/search',
 'record_thumbnail': '/records/<pid_value>/thumb<int:size>',
 'robots': '/robots.txt'}
```

---

(app-rdm-subcommunities-label)=
### APP_RDM_SUBCOMMUNITIES_LABEL

```{eval-rst}
Label for the subcommunities in the community browse page.
```

| **Invenio RDM Default Value** | `_('Subcommunities')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1547) |

---

(app-rdm-user-dashboard-routes)=
### APP_RDM_USER_DASHBOARD_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L795) |

```
{'communities': '/me/communities', 'requests': '/me/requests', 'uploads': '/me/uploads'}
```

---

(app-requestid-header)=
### APP_REQUESTID_HEADER

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `'X-Request-Id'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L192) |

---

(app-theme)=
### ***APP_THEME**

```{eval-rst}
Application-wide themes list used for template and assets lookup.

The value is a list of theme strings applied in a fallback fashion in the order
they are specified:

.. code-block:: python

    APP_THEME = ['my-overlay', 'semantic-ui']

From the above example, templates and assets with the ``my-overlay`` prefix
will be looked up first, and if not found the ``semantic-ui`` prefix will be
used. If none of the lookups are successful, a non-prefixed lookup is done.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L97); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L267) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(assets-builder)=
### ***ASSETS_BUILDER**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(audit-logs-disabled-actions)=
### AUDIT_LOGS_DISABLED_ACTIONS

```{eval-rst}
Disabled actions to be excluded from the audit logs.
To find all the available actions, check the entry points in the `invenio_audit_logs.actions` group.
```python
>>> from invenio_base.utils import entry_points
>>> [ep.name for ep in entry_points(group="invenio_audit_logs.actions")]
```
```

| **Invenio RDM Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L52) |

```
set()
```

---

(audit-logs-enabled)=
### AUDIT_LOGS_ENABLED

```{eval-rst}
Feature flag. Disabled by default.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L49) |

---

(audit-logs-facets)=
### AUDIT_LOGS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L24) |

```
{'action_name': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e77fc70>,
                 'ui': {'field': 'action'}},
 'resource': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e802a50>,
              'ui': {'field': 'resource.type'}}}
```

---

(audit-logs-search)=
### AUDIT_LOGS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L14) |

```
{'facets': ['resource', 'action_name'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---

(audit-logs-sort-options)=
### AUDIT_LOGS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-audit-logs](https://github.com/inveniosoftware/invenio-audit-logs/blob/master/invenio_audit_logs/config.py#L42) |

```
{'bestmatch': {'fields': ['_score'], 'title': 'Best match'},
 'newest': {'fields': ['-@timestamp'], 'title': 'Newest'},
 'oldest': {'fields': ['@timestamp'], 'title': 'Oldest'}}
```

---

(babel-default-locale)=
### ***BABEL_DEFAULT_LOCALE**

```{eval-rst}
Default locale (language).
```

| **Invenio RDM Default Value** | `'en'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L247) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(babel-default-timezone)=
### ***BABEL_DEFAULT_TIMEZONE**

```{eval-rst}
Default time zone.
```

| **Invenio RDM Default Value** | `'Europe/Zurich'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L250) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(banners-categories)=
### BANNERS_CATEGORIES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L15) |

```
[('info', l'Info'), ('warning', l'Warning'), ('other', l'Other')]
```

---

(banners-categories-to-style)=
### BANNERS_CATEGORIES_TO_STYLE

```{eval-rst}
Function to transform the banner category to a specific Semantic-UI class.
```

| **Invenio RDM Default Value** | `style_category` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L22) |

---

(banners-search)=
### BANNERS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L25) |

```
{'facets': [], 'sort': ['url_path', 'start_datetime', 'end_datetime', 'active']}
```

---

(banners-sort-options)=
### BANNERS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-banners](https://github.com/inveniosoftware/invenio-banners/blob/master/invenio_banners/config.py#L36) |

```
{'active': {'fields': ['active'], 'title': l'Active'},
 'end_datetime': {'fields': ['end_datetime'], 'title': l'End DateTime'},
 'start_datetime': {'fields': ['start_datetime'], 'title': l'Start DateTime'},
 'url_path': {'fields': ['url_path'], 'title': l'URL path'}}
```

---

(base-template)=
### ***BASE_TEMPLATE**

```{eval-rst}
Base template for user facing pages.

The template provides a basic skeleton which takes care of loading assets,
embedding header metadata and define basic template blocks. All other user
facing templates usually extends from this template and thus changing this
template allows to change design and layout of Invenio.
```

| **Invenio RDM Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L14); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L270) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(broker-url)=
### ***BROKER_URL**

```{eval-rst}
URL of message broker for Celery 3 (default is RabbitMQ).
```

| **Invenio RDM Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L428); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L16) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(cache-is-authenticated-callback)=
### CACHE_IS_AUTHENTICATED_CALLBACK

```{eval-rst}
Import path to callback.

Callback is executed to determine if request is authenticated.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L34) |

---

(cache-key-prefix)=
### CACHE_KEY_PREFIX

```{eval-rst}
Cache key prefix.
```

| **Invenio RDM Default Value** | `'cache::'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L20) |

---

(cache-redis-url)=
### ***CACHE_REDIS_URL**

```{eval-rst}
Redis location and database.
```

| **Invenio RDM Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L30); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L719) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(cache-type)=
### CACHE_TYPE

```{eval-rst}
Cache type.

Please refer to Flask-Caching documentation for other cache types.
```

| **Invenio RDM Default Value** | `'flask_caching.backends.redis'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-cache](https://github.com/inveniosoftware/invenio-cache/blob/master/invenio_cache/config.py#L24); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L722) |

---

(celery-accept-content)=
### CELERY_ACCEPT_CONTENT

```{eval-rst}
A whitelist of content-types/serializers.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L23) |

```
['json', 'msgpack', 'yaml']
```

---

(celery-beat-schedule)=
### ***CELERY_BEAT_SCHEDULE**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L431) |
| **Set by** | {py:func}`~oarepo_config.configure_cron` |

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

(celery-broker-url)=
### ***CELERY_BROKER_URL**

```{eval-rst}
Same as BROKER_URL to support Celery 4.
```

| **Invenio RDM Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L511); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L17) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(celery-result-backend)=
### ***CELERY_RESULT_BACKEND**

```{eval-rst}
URL of backend for result storage (default is Redis).
```

| **Invenio RDM Default Value** | `'redis://localhost:6379/1'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L514); [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L20) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(celery-result-serializer)=
### CELERY_RESULT_SERIALIZER

```{eval-rst}
Result serialization format. Default is ``msgpack``.
```

| **Invenio RDM Default Value** | `'msgpack'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L26) |

---

(celery-task-serializer)=
### CELERY_TASK_SERIALIZER

```{eval-rst}
The default serialization method to use. Default is ``msgpack``.
```

| **Invenio RDM Default Value** | `'msgpack'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-celery](https://github.com/inveniosoftware/invenio-celery/blob/master/invenio_celery/config.py#L29) |

---

(checks-communities-service-components)=
### CHECKS_COMMUNITIES_SERVICE_COMPONENTS

```{eval-rst}
Extra components that are registered to COMMUNITIES_SERVICE_COMPONENTS.

The default (RegisterCheckComponent) will create a LLM configuration for a community
whenever it is added/modified.
```

| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-checks](https://github.com/oarepo/oarepo-checks/blob/master/oarepo_checks/config.py#L20) |

```
[
    RegisterCheckComponent,
]
```

---

(checks-enabled)=
### ***CHECKS_ENABLED**

```{eval-rst}
Enable checks.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-checks](https://github.com/inveniosoftware/invenio-checks/blob/master/invenio_checks/config.py#L6) |
| **Set by** | {py:func}`~oarepo_config.configure_llm` |

---

(checks-generic-community)=
### ***CHECKS_GENERIC_COMMUNITY**

```{eval-rst}
A slug of community that is used for LLM prompt when record does not belong to a community.
```

| **OARepo Default Value** | `'generic-community'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-checks](https://github.com/oarepo/oarepo-checks/blob/master/oarepo_checks/config.py#L17) |
| **Set by** | {py:func}`~oarepo_config.configure_llm` |

---

(collections-max-collections-per-tree)=
### COLLECTIONS_MAX_COLLECTIONS_PER_TREE

```{eval-rst}
Maximum number of collections allowed per tree.

This counts all collections in a tree, regardless of depth.
Set to 0 for unlimited collections.
Default: 100
```

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L25) |

---

(collections-max-depth)=
### COLLECTIONS_MAX_DEPTH

```{eval-rst}
Maximum depth for collection hierarchies.

Depth 0 = root collections
Depth 1 = children of root
Depth 2 = grandchildren (not allowed by default)

Setting this to 1 allows 2 levels: root + children only.
Setting this to 2 would allow 3 levels: root + children + grandchildren.
```

| **Invenio RDM Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L7) |

---

(collections-max-trees)=
### COLLECTIONS_MAX_TREES

```{eval-rst}
Maximum number of collection trees allowed per namespace.

Set to 0 for unlimited trees.
Default: 10
```

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-collections](https://github.com/inveniosoftware/invenio-collections/blob/master/invenio_collections/config.py#L18) |

---

(collections-permission-policy)=
### COLLECTIONS_PERMISSION_POLICY

```{eval-rst}
Permission policy used by invenio-collections for managing collection trees.
```

| **Invenio RDM Default Value** | `CommunityPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L25) |

---

(collect-static-root)=
### COLLECT_STATIC_ROOT
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(collect-storage)=
### ***COLLECT_STORAGE**

```{eval-rst}
Static files collection method (defaults to copying files).
```

| **Invenio RDM Default Value** | `'flask_collect.storage.link'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L386) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(communities-allow-membership-requests)=
### COMMUNITIES_ALLOW_MEMBERSHIP_REQUESTS

```{eval-rst}
Feature flag for membership request.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L370) |

---

(communities-allow-restricted)=
### COMMUNITIES_ALLOW_RESTRICTED
| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L351) |

---

(communities-always-show-create-link)=
### COMMUNITIES_ALWAYS_SHOW_CREATE_LINK

```{eval-rst}
Controls visibility of 'New Community' btn based on user's permission when set to True.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L367) |

---

(communities-collections-enabled)=
### COMMUNITIES_COLLECTIONS_ENABLED

```{eval-rst}
Feature flag to enable/disable collections feature.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L376) |

---

(communities-custom-fields)=
### COMMUNITIES_CUSTOM_FIELDS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L283) |

```
[<oarepo_communities.services.custom_fields.workflow.WorkflowCF object at 0x112ef6ba0>,
 <oarepo_communities.services.custom_fields.workflow.WorkflowCF object at 0x112f40e10>]
```

---

(communities-custom-fields-ui)=
### COMMUNITIES_CUSTOM_FIELDS_UI

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L306) |

```
[{'fields': [{'field': 'workflow',
              'props': {'description': l'Default workflow for the community if workflow is not specified when depositing a record.',
                        'label': l'Default workflow',
                        'options': []},
              'ui_widget': 'Dropdown'},
             {'field': 'allowed_workflows',
              'props': {'description': l'Workflows allowed for the community.',
                        'label': l'Allowed workflows',
                        'multiple': True,
                        'options': []},
              'ui_widget': 'Dropdown'}],
  'section': l'Workflows'}]
```

---

(communities-default-record-submission-policy)=
### COMMUNITIES_DEFAULT_RECORD_SUBMISSION_POLICY

```{eval-rst}
Default value of record submission policy community access setting.
```

| **Invenio RDM Default Value** | `<RecordSubmissionPolicyEnum.OPEN: 'open'>` |
|--------------|-----------|
| **Type** | RecordSubmissionPolicyEnum |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L373) |

---

(communities-error-handlers)=
### COMMUNITIES_ERROR_HANDLERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1075) |

```
{
    **community_error_handlers,
    InvalidCommunityVisibility: create_error_handler(lambda e: HTTPJSONException(code=400, description=e.reason)),
}
```

---

(communities-facets)=
### COMMUNITIES_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L52) |

```
{'type': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e4df2f0>,
          'ui': {'field': 'type'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e518e20>,
                'ui': {'field': 'visibility'}}}
```

---

(communities-identities-cache-handler)=
### COMMUNITIES_IDENTITIES_CACHE_HANDLER
| **Invenio RDM Default Value** | `'invenio_communities.cache.redis:IdentityRedisCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L361) |

---

(communities-identities-cache-redis-url)=
### ***COMMUNITIES_IDENTITIES_CACHE_REDIS_URL**
| **Invenio RDM Default Value** | `'redis://localhost:6379/4'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L358) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(communities-identities-cache-time)=
### COMMUNITIES_IDENTITIES_CACHE_TIME
| **Invenio RDM Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L355) |

---

(communities-invitations-expires-in)=
### COMMUNITIES_INVITATIONS_EXPIRES_IN

```{eval-rst}
Default amount of time before an invitation expires.
```

| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L236) |

---

(communities-invitations-search)=
### COMMUNITIES_INVITATIONS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L210) |

```
{'facets': ['type', 'status'], 'sort': ['bestmatch', 'name', 'newest', 'oldest']}
```

---

(communities-invitations-sort-options)=
### COMMUNITIES_INVITATIONS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L216) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'name': {'fields': ['user.profile.full_name.keyword'], 'title': l'Name'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'}}
```

---

(communities-logo-max-file-size)=
### COMMUNITIES_LOGO_MAX_FILE_SIZE

```{eval-rst}
Community logo size quota, in bytes.
```

| **Invenio RDM Default Value** | `1000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L264) |

---

(communities-membership-requests-expires-in)=
### COMMUNITIES_MEMBERSHIP_REQUESTS_EXPIRES_IN

```{eval-rst}
Default amount of time before a membership request expires.
```

| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L261) |

---

(communities-membership-requests-facets)=
### COMMUNITIES_MEMBERSHIP_REQUESTS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L245) |

```
{'role': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e51a7a0>,
          'ui': {'field': 'role'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10de5f750>,
            'ui': {'field': 'role'}}}
```

---

(communities-membership-requests-search)=
### COMMUNITIES_MEMBERSHIP_REQUESTS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L239) |

```
{'facets': ['role', 'status'], 'sort': ['bestmatch', 'name', 'newest', 'oldest']}
```

---

(communities-members-facets)=
### COMMUNITIES_MEMBERS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L194) |

```
{'role': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e51a7a0>,
          'ui': {'field': 'role'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e59e950>,
                'ui': {'field': 'visible'}}}
```

---

(communities-members-search)=
### COMMUNITIES_MEMBERS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L168) |

```
{'facets': ['role', 'visibility'], 'sort': ['bestmatch', 'name', 'newest', 'oldest']}
```

---

(communities-members-service-components)=
### COMMUNITIES_MEMBERS_SERVICE_COMPONENTS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[<class 'oarepo_oidc_einfra.services.components.aai_invitations.AAIInvitationComponent'>,
 <class 'invenio_records_resources.services.records.components.metadata.MetadataComponent'>,
 <class 'invenio_communities.members.services.components.CommunityMemberCachingComponent'>]
```

---

(communities-members-sort-options)=
### COMMUNITIES_MEMBERS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L174) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'name': {'fields': ['user.profile.full_name.keyword'], 'title': l'Name'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'}}
```

---

(communities-namespaces)=
### COMMUNITIES_NAMESPACES

```{eval-rst}
Custom fields namespaces.

.. code-block:: python
    {<namespace>: <uri>, ...}

For example:

.. code-block:: python
    {
        "cern": "https://cern.ch/terms",
        "dwc": "http://rs.tdwg.org/dwc/terms/"
    }
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L267) |

```
{}
```

---

(communities-oai-sets-prefix)=
### COMMUNITIES_OAI_SETS_PREFIX
| **Invenio RDM Default Value** | `'community-'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L365) |

---

(communities-permission-policy)=
### ***COMMUNITIES_PERMISSION_POLICY**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/communities.py#L63) |
| **Set by** | {py:func}`~oarepo_config.configure_communities` |

---

(communities-records-search)=
### COMMUNITIES_RECORDS_SEARCH
| **OARepo Default Value** | `LocalProxy(lambda: current_oarepo_rdm.dynamic_rdm_search)` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L77); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1085) |

---

(communities-records-search-all)=
### COMMUNITIES_RECORDS_SEARCH_ALL
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(communities-register-ui-blueprint)=
### ***COMMUNITIES_REGISTER_UI_BLUEPRINT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/communities.py#L63) |
| **Set by** | {py:func}`~oarepo_config.configure_communities` |

---

(communities-requests-search)=
### COMMUNITIES_REQUESTS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L162) |

```
{'facets': ['type', 'status'],
 'sort': ['bestmatch', 'newest', 'oldest', 'newestactivity', 'oldestactivity']}
```

---

(communities-roles)=
### ***COMMUNITIES_ROLES**
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L109) |
| **Set by** | {py:func}`~oarepo_config.configure_communities` |

```
[{'can_view': True,
  'description': l'Can view restricted records.',
  'name': 'reader',
  'title': l'Reader'},
 {'can_curate': True,
  'can_view': True,
  'description': l'Can curate records and view restricted records.',
  'name': 'curator',
  'title': l'Curator'},
 {'can_curate': True,
  'can_manage': True,
  'can_manage_roles': ['manager', 'curator', 'reader'],
  'can_view': True,
  'description': l'Can manage members, curate records and view restricted records.',
  'name': 'manager',
  'title': l'Manager'},
 {'can_curate': True,
  'can_manage': True,
  'can_manage_roles': ['owner', 'manager', 'curator', 'reader'],
  'can_view': True,
  'description': l'Full administrative access to the entire community.',
  'is_owner': True,
  'name': 'owner',
  'title': l'Owner'}]
```

---

(communities-routes)=
### COMMUNITIES_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L28) |

```
{'about': '/communities/<pid_value>/about',
 'curation_policy': '/communities/<pid_value>/curation-policy',
 'deprecated_new': '/communities/new',
 'deprecated_search': '/communities/search',
 'frontpage': '/communities',
 'invitations': '/communities/<pid_value>/invitations',
 'members': '/communities/<pid_value>/members',
 'membership_requests': '/communities/<pid_value>/membership-requests',
 'my_communities': '/me/communities',
 'new': '/communities-new',
 'new_subcommunity': '/communities/<pid_value>/subcommunities/new',
 'requests': '/communities/<pid_value>/requests',
 'search': '/communities-search',
 'settings': '/communities/<pid_value>/settings',
 'settings_collections': '/communities/<pid_value>/settings/collections',
 'settings_pages': '/communities/<pid_value>/settings/pages',
 'settings_privileges': '/communities/<pid_value>/settings/privileges',
 'settings_submission_policy': '/communities/<pid_value>/settings/submission-policy',
 'subcommunities': '/communities/<pid_value>/browse/subcommunities',
 'upload': '/communities/<pid_value>/upload'}
```

---

(communities-search)=
### COMMUNITIES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L147) |

```
{'facets': ['type', 'visibility'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---

(communities-search-sort-by-verified)=
### COMMUNITIES_SEARCH_SORT_BY_VERIFIED

```{eval-rst}
Sort communities by 'verified' first.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L153) |

---

(communities-service-components)=
### COMMUNITIES_SERVICE_COMPONENTS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1067) |

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
 <class 'oarepo_checks.services.components.register_check_config.RegisterCheckComponent'>,
 <class 'oarepo_oidc_einfra.services.components.aai_communities.CommunityAAIComponent'>]
```

---

(communities-sort-options)=
### COMMUNITIES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L72) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'newestactivity': {'fields': ['-last_activity_at'], 'title': l'Newest activity'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'},
 'oldestactivity': {'fields': ['last_activity_at'], 'title': l'Oldest activity'},
 'updated-asc': {'fields': ['updated'], 'title': l'Least recently updated'},
 'updated-desc': {'fields': ['-updated'], 'title': l'Recently updated'},
 'version': {'fields': ['-versions.index'], 'title': l'Version'}}
```

---

(communities-subcommunities-facets)=
### COMMUNITIES_SUBCOMMUNITIES_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L69) |

```
{'type': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e4df2f0>,
          'ui': {'field': 'type'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10e518e20>,
                'ui': {'field': 'visibility'}}}
```

---

(communities-subcommunities-search)=
### COMMUNITIES_SUBCOMMUNITIES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-communities](https://github.com/inveniosoftware/invenio-communities/blob/master/invenio_communities/config.py#L156) |

```
{'facets': ['type'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---

(communities-sub-invitation-request-cls)=
### COMMUNITIES_SUB_INVITATION_REQUEST_CLS

```{eval-rst}
RDM specific request type for subcommunity invitations.
```

| **Invenio RDM Default Value** | `RDMSubCommunityInvitationRequest` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1072) |

---

(communities-sub-request-cls)=
### COMMUNITIES_SUB_REQUEST_CLS

```{eval-rst}
RDM specific request type for subcommunities.
```

| **Invenio RDM Default Value** | `RDMSubCommunityRequest` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1069) |

---

(cors-expose-headers)=
### CORS_EXPOSE_HEADERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L38) |

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

(cors-resources)=
### CORS_RESOURCES

```{eval-rst}
Dictionary for configuring CORS for endpoints.

   See Flask-CORS for further details.

.. note:: Overwrites
   `Flask-CORS
   <https://flask-cors.readthedocs.io/en/latest/api.html#flask_cors.CORS>`_
   configuration.
```

| **Invenio RDM Default Value** | `'*'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L18) |

---

(cors-send-wildcard)=
### CORS_SEND_WILDCARD

```{eval-rst}
Sending wildcard CORS header.

.. note:: Overwrites
   `Flask-CORS
   <https://flask-cors.readthedocs.io/en/latest/api.html#flask_cors.CORS>`_
   configuration.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L29) |

---

(cover-template)=
### ***COVER_TEMPLATE**

```{eval-rst}
Cover page template normally used e.g. for login and sign up pages.
```

| **Invenio RDM Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L38); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L273) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(crossref-additional-prefixes)=
### CROSSREF_ADDITIONAL_PREFIXES

```{eval-rst}
List of additional Crossref DOI prefixes supported for registration.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L724) |

```
[]
```

---

(crossref-depositor)=
### CROSSREF_DEPOSITOR

```{eval-rst}
Crossref depositor name.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L727) |

---

(crossref-email)=
### CROSSREF_EMAIL

```{eval-rst}
Crossref depositor email.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L730) |

---

(crossref-enabled)=
### CROSSREF_ENABLED

```{eval-rst}
Flag to enable/disable Crossref DOI registration.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L712) |

---

(crossref-format)=
### CROSSREF_FORMAT

```{eval-rst}
A string used for formatting the DOI or a callable.

If set to a string, you can used ``{prefix}`` and ``{id}`` inside the string.

You can also provide a callable instead:

.. code-block:: python

    def make_doi(prefix, record):
        return f"{prefix}/{record.pid.pid_value}"

    CROSSREF_FORMAT = make_doi
```

| **Invenio RDM Default Value** | `'{prefix}/{id}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L739) |

---

(crossref-password)=
### CROSSREF_PASSWORD

```{eval-rst}
Crossref password.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L718) |

---

(crossref-prefix)=
### CROSSREF_PREFIX

```{eval-rst}
Crossref DOI prefix.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L721) |

---

(crossref-registrant)=
### CROSSREF_REGISTRANT

```{eval-rst}
Crossref registrant.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L733) |

---

(crossref-test-mode)=
### CROSSREF_TEST_MODE

```{eval-rst}
Crossref test mode enabled.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L736) |

---

(crossref-url)=
### CROSSREF_URL
| **OARepo Default Value** | `'https://api.crossref.org/works/doi'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L17) |

---

(crossref-username)=
### CROSSREF_USERNAME

```{eval-rst}
Crossref username.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L715) |

---

(csrf-allowed-chars)=
### CSRF_ALLOWED_CHARS
| **Default Value** | `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(csrf-cookie-name)=
### CSRF_COOKIE_NAME
| **Default Value** | `'csrftoken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(csrf-cookie-samesite)=
### CSRF_COOKIE_SAMESITE
| **Default Value** | `'Lax'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(csrf-force-secure-referer)=
### CSRF_FORCE_SECURE_REFERER
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(csrf-header)=
### CSRF_HEADER
| **Default Value** | `'X-CSRFToken'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(csrf-methods)=
### CSRF_METHODS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['POST', 'PUT', 'PATCH', 'DELETE']
```

---

(csrf-secret-salt)=
### CSRF_SECRET_SALT
| **Default Value** | `'invenio-csrf-token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(csrf-token-expires-in)=
### CSRF_TOKEN_EXPIRES_IN
| **Default Value** | `86400` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(csrf-token-grace-period)=
### CSRF_TOKEN_GRACE_PERIOD
| **Default Value** | `604800` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(csrf-token-length)=
### CSRF_TOKEN_LENGTH
| **Default Value** | `32` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(dashboard-record-create-url)=
### ***DASHBOARD_RECORD_CREATE_URL**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui`, {py:func}`~oarepo_config.configure_generic_parameters` |

---

(datacite-additional-prefixes)=
### DATACITE_ADDITIONAL_PREFIXES

```{eval-rst}
List of additional DataCite DOI prefixes supported for registration.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L682) |

```
[]
```

---

(datacite-datacenter-symbol)=
### DATACITE_DATACENTER_SYMBOL

```{eval-rst}
DataCite data center symbol.

This is only required if you want your records to be harvestable (OAI-PMH)
in DataCite XML format.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L703) |

---

(datacite-enabled)=
### DATACITE_ENABLED

```{eval-rst}
Flag to enable/disable DataCite DOI registration.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L670) |

---

(datacite-format)=
### DATACITE_FORMAT

```{eval-rst}
A string used for formatting the DOI or a callable.

If set to a string, you can used ``{prefix}`` and ``{id}`` inside the string.

You can also provide a callable instead:

.. code-block:: python

    def make_doi(prefix, record):
        return f"{prefix}/{record.pid.pid_value}"

    DATACITE_FORMAT = make_doi
```

| **Invenio RDM Default Value** | `'{prefix}/{id}'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L688) |

---

(datacite-password)=
### DATACITE_PASSWORD

```{eval-rst}
DataCite password.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L676) |

---

(datacite-prefix)=
### DATACITE_PREFIX

```{eval-rst}
DataCite DOI prefix.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L679) |

---

(datacite-test-mode)=
### ***DATACITE_TEST_MODE**

```{eval-rst}
DataCite test mode enabled.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L685) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(datacite-url)=
### DATACITE_URL
| **OARepo Default Value** | `'https://api.datacite.org/dois'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L15) |

---

(datacite-username)=
### DATACITE_USERNAME

```{eval-rst}
DataCite username.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L673) |

---

(db-versioning)=
### DB_VERSIONING
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(db-versioning-user-model)=
### DB_VERSIONING_USER_MODEL
| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L597) |

---

(debug)=
### DEBUG
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(debug-tb-intercept-redirects)=
### DEBUG_TB_INTERCEPT_REDIRECTS

```{eval-rst}
Switches off incept of redirects by Flask-DebugToolbar.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L712) |

---

(default-communities-custom-fields)=
### DEFAULT_COMMUNITIES_CUSTOM_FIELDS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[<oarepo_communities.services.custom_fields.workflow.WorkflowCF object at 0x112ef6ba0>,
 <oarepo_communities.services.custom_fields.workflow.WorkflowCF object at 0x112f40e10>]
```

---

(default-communities-custom-fields-ui)=
### DEFAULT_COMMUNITIES_CUSTOM_FIELDS_UI
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[{'fields': [{'field': 'workflow',
              'props': {'description': l'Default workflow for the community if workflow is not specified when depositing a record.',
                        'label': l'Default workflow',
                        'options': []},
              'ui_widget': 'Dropdown'},
             {'field': 'allowed_workflows',
              'props': {'description': l'Workflows allowed for the community.',
                        'label': l'Allowed workflows',
                        'multiple': True,
                        'options': []},
              'ui_widget': 'Dropdown'}],
  'section': l'Workflows'}]
```

---

(default-workflow-events)=
### DEFAULT_WORKFLOW_EVENTS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'C': WorkflowEvent(submitters=[<invenio_records_permissions.generators.IfConfig object at 0x10de5e5d0>]),
 'L': WorkflowEvent(submitters=[<invenio_records_permissions.generators.IfConfig object at 0x10de5e5d0>])}
```

---

(deployment-version)=
### ***DEPLOYMENT_VERSION**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(display-new-communities)=
### DISPLAY_NEW_COMMUNITIES
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(display-user-communities)=
### DISPLAY_USER_COMMUNITIES
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(doi-settings-facets)=
### DOI_SETTINGS_FACETS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L73) |

```
{'community_slug': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x1127fa7b0>,
                    'ui': {'field': 'community_slug'}},
 'prefix': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x1127fa890>,
            'ui': {'field': 'prefix'}}}
```

---

(doi-settings-search)=
### DOI_SETTINGS_SEARCH
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L66) |

```
{'facets': ['community_slug', 'prefix'],
 'sort': ['newest'],
 'sort_default': 'newest',
 'sort_default_no_query': 'newest'}
```

---

(doi-settings-sort-options)=
### DOI_SETTINGS_SORT_OPTIONS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L87) |

```
{'newest': {'fields': ['-created'], 'title': l'Newest'}}
```

---

(einfra)=
### ***EINFRA**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/einfra.py#L24) |
| **Set by** | {py:func}`~oarepo_config.configure_einfra_oidc` |

---

(einfra-api-url)=
### EINFRA_API_URL

```{eval-rst}
URL of the E-INFRA Perun API.
```

| **OARepo Default Value** | `'https://perun-api.e-infra.cz/krb'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L28) |

---

(einfra-capabilities-attribute-name)=
### EINFRA_CAPABILITIES_ATTRIBUTE_NAME

```{eval-rst}
urn of the attribute in the E-INFRA Perun that represents the capabilities.
```

| **OARepo Default Value** | `'urn:perun:resource:attribute-def:def:capabilities'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L43) |

---

(einfra-community-invitation-synchronization)=
### EINFRA_COMMUNITY_INVITATION_SYNCHRONIZATION

```{eval-rst}
Synchronize community membership invitation to E-Infra Perun
    (create perun invitation) when user is invited in repository UI.
```

| **OARepo Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L15) |

---

(einfra-community-member-synchronization)=
### EINFRA_COMMUNITY_MEMBER_SYNCHRONIZATION

```{eval-rst}
Synchronize community membership to E-Infra Perun when user changes role within a community.
```

| **OARepo Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L19) |

---

(einfra-community-synchronization)=
### EINFRA_COMMUNITY_SYNCHRONIZATION

```{eval-rst}
Synchronize community to E-Infra Perun when community is created.
```

| **OARepo Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L12) |

---

(einfra-default-invitation-language)=
### EINFRA_DEFAULT_INVITATION_LANGUAGE

```{eval-rst}
Language of the invitation emails that are sent to the users.
```

| **OARepo Default Value** | `'en'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L98) |

---

(einfra-entitlement-namespaces)=
### EINFRA_ENTITLEMENT_NAMESPACES

```{eval-rst}
URN prefix for capabilities that can represent community roles.
```

| **OARepo Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L22) |

```
{'geant'}
```

---

(einfra-entitlement-prefix)=
### EINFRA_ENTITLEMENT_PREFIX

```{eval-rst}
Parts of the entitlement URN name that represent communities.
```

| **OARepo Default Value** | `'cesnet.cz'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L25) |

---

(einfra-last-dump-path)=
### EINFRA_LAST_DUMP_PATH

```{eval-rst}
Path to the last dump file in the S3 bucket.
```

| **OARepo Default Value** | `'nrp_invenio_export.json'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L101) |

---

(einfra-login-app)=
### ***EINFRA_LOGIN_APP**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/einfra.py#L24) |
| **Set by** | {py:func}`~oarepo_config.configure_einfra_oidc` |

---

(einfra-rsa-key)=
### EINFRA_RSA_KEY
| **OARepo Default Value** | `b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmho5h/lz6USUUazQaVT3\nPHlo...` |
|--------------|-----------|
| **Type** | bytes |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L31) |

---

(einfra-user-display-name-attribute)=
### EINFRA_USER_DISPLAY_NAME_ATTRIBUTE

```{eval-rst}
Attribute on user inside perun that represents the display name of the user.
```

| **OARepo Default Value** | `'urn:perun:user:attribute-def:core:displayName'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L89) |

---

(einfra-user-id-dump-attribute)=
### EINFRA_USER_ID_DUMP_ATTRIBUTE

```{eval-rst}
Attribute on user inside perun that represents the E-INFRA ID of the user.
```

| **OARepo Default Value** | `'urn:perun:user:attribute-def:virt:login-namespace:einfraid-persistent'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L86) |

---

(einfra-user-id-search-attribute)=
### EINFRA_USER_ID_SEARCH_ATTRIBUTE

```{eval-rst}
Attribute on user inside perun that represents the E-INFRA ID of the user.
```

| **OARepo Default Value** | `'urn:perun:user:attribute-def:def:login-namespace:einfraid-persistent-shadow'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L83) |

---

(einfra-user-organization-attribute)=
### EINFRA_USER_ORGANIZATION_ATTRIBUTE

```{eval-rst}
Attribute on user inside perun that represents the organization of the user.
```

| **OARepo Default Value** | `'urn:perun:user:attribute-def:def:organization'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L92) |

---

(einfra-user-preferred-mail-attribute)=
### EINFRA_USER_PREFERRED_MAIL_ATTRIBUTE

```{eval-rst}
Attribute on user inside perun that represents the preferred mail of the user.
```

| **OARepo Default Value** | `'urn:perun:user:attribute-def:def:preferredMail'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-oidc-einfra](https://github.com/oarepo/oarepo-oidc-einfra/blob/master/oarepo_oidc_einfra/config.py#L95) |

---

(explain-template-loading)=
### EXPLAIN_TEMPLATE_LOADING
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(files-rest-allow-range-requests)=
### FILES_REST_ALLOW_RANGE_REQUESTS

```{eval-rst}
Enable support for HTTP Range Requests.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L136) |

---

(files-rest-checksum-verification-uri-prefixes)=
### FILES_REST_CHECKSUM_VERIFICATION_URI_PREFIXES

```{eval-rst}
URI prefixes of files their checksums should be verified
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L348) |

```
[]
```

---

(files-rest-default-max-file-size)=
### FILES_REST_DEFAULT_MAX_FILE_SIZE

```{eval-rst}
Default maximum file size for a bucket in bytes. `None` if unlimited.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L48) |

---

(files-rest-default-quota-size)=
### ***FILES_REST_DEFAULT_QUOTA_SIZE**

```{eval-rst}
Default quota size for a bucket in bytes. `None` if unlimited.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L45) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(files-rest-default-storage-class)=
### ***FILES_REST_DEFAULT_STORAGE_CLASS**

```{eval-rst}
Default storage class. Must be one of `FILES_REST_STORAGE_CLASS_LIST`.
```

| **Invenio RDM Default Value** | `'S'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L42); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L358) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(files-rest-file-tags-header)=
### FILES_REST_FILE_TAGS_HEADER

```{eval-rst}
Header for updating file tags.
```

| **Invenio RDM Default Value** | `'X-Invenio-File-Tags'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L129) |

---

(files-rest-file-uri-max-len)=
### FILES_REST_FILE_URI_MAX_LEN

```{eval-rst}
Maximum length of the FileInstance.uri field.

.. warning::
   Setting this variable to anything higher than 255 is only supported
   with PostgreSQL database.
```

| **Invenio RDM Default Value** | `255` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L71) |

---

(files-rest-min-file-size)=
### FILES_REST_MIN_FILE_SIZE

```{eval-rst}
Minimum file size when uploading, in bytes (do not allow empty files).
```

| **Invenio RDM Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L51) |

---

(files-rest-multipart-chunksize-max)=
### FILES_REST_MULTIPART_CHUNKSIZE_MAX

```{eval-rst}
Maximum chunk size in bytes of multipart objects.
```

| **Invenio RDM Default Value** | `5368709120` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L117) |

---

(files-rest-multipart-chunksize-min)=
### FILES_REST_MULTIPART_CHUNKSIZE_MIN

```{eval-rst}
Minimum chunk size in bytes of multipart objects.
```

| **Invenio RDM Default Value** | `5242880` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L114) |

---

(files-rest-multipart-expires)=
### FILES_REST_MULTIPART_EXPIRES

```{eval-rst}
Time delta after which a multipart upload is considered expired.
```

| **Invenio RDM Default Value** | `datetime.timedelta(days=4)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L120) |

---

(files-rest-multipart-max-parts)=
### FILES_REST_MULTIPART_MAX_PARTS

```{eval-rst}
Maximum number of parts when uploading files with multipart uploads.
```

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L111) |

---

(files-rest-multipart-part-factories)=
### FILES_REST_MULTIPART_PART_FACTORIES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L93) |

```
['invenio_files_rest.views:default_partfactory',
 'invenio_files_rest.views:ngfileupload_partfactory']
```

---

(files-rest-object-key-max-len)=
### FILES_REST_OBJECT_KEY_MAX_LEN

```{eval-rst}
Maximum length of the ObjectVersion.key field.

.. warning::
   Setting this variable to anything higher than 255 is only supported
   with PostgreSQL database.
```

| **Invenio RDM Default Value** | `255` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L63) |

---

(files-rest-permission-factory)=
### FILES_REST_PERMISSION_FACTORY

```{eval-rst}
Permission factory to control the files access from the REST interface.
```

| **Invenio RDM Default Value** | `'invenio_files_rest.permissions.permission_factory'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L60); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L345) |

---

(files-rest-size-limiters)=
### FILES_REST_SIZE_LIMITERS

```{eval-rst}
Import path of file size limiters factory to control bucket size limits.
```

| **Invenio RDM Default Value** | `'invenio_files_rest.limiters.file_size_limiters'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L54) |

---

(files-rest-storage-class-list)=
### ***FILES_REST_STORAGE_CLASS_LIST**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L31); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L352) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'A': 'Archive', 'S': 'Standard'}
```

---

(files-rest-storage-factory)=
### ***FILES_REST_STORAGE_FACTORY**

```{eval-rst}
Import path of factory used to create a storage instance.
```

| **Invenio RDM Default Value** | `'invenio_files_rest.storage.pyfs_storage_factory'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L57) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(files-rest-storage-path-dimensions)=
### FILES_REST_STORAGE_PATH_DIMENSIONS

```{eval-rst}
Number of directory levels created when generating the path of a file.

   For example, if split length set to 2 and dimension to 3, the final
   path will be `a2/ad/4k/c9-8j39-34jn/`.
```

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L86) |

---

(files-rest-storage-path-split-length)=
### FILES_REST_STORAGE_PATH_SPLIT_LENGTH

```{eval-rst}
Number of chars to use as folder name when generating the path of a file.

   For example, if split length set to 4 and dimension to 4, the final
   path will be `a2ad/4kc9/8j39-34jn/`.
```

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L79) |

---

(files-rest-task-wait-interval)=
### FILES_REST_TASK_WAIT_INTERVAL

```{eval-rst}
Interval in seconds between sending a whitespace to not close connection.
```

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L123) |

---

(files-rest-task-wait-max-seconds)=
### FILES_REST_TASK_WAIT_MAX_SECONDS

```{eval-rst}
Maximum number of seconds to wait for a task to finish.
```

| **Invenio RDM Default Value** | `600` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L126) |

---

(files-rest-upload-factories)=
### FILES_REST_UPLOAD_FACTORIES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L99) |

```
['invenio_files_rest.views:stream_uploadfactory',
 'invenio_files_rest.views:ngfileupload_uploadfactory']
```

---

(files-rest-xsendfile-enabled)=
### FILES_REST_XSENDFILE_ENABLED

```{eval-rst}
Use the X-Accel-Redirect header to stream the file through a reverse proxy(
    e.g NGINX).
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L132) |

---

(files-rest-xsendfile-response-func)=
### FILES_REST_XSENDFILE_RESPONSE_FUNC

```{eval-rst}
Function for the creation of a file streaming redirect response.
```

| **Invenio RDM Default Value** | `create_file_streaming_redirect_response` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L139) |

---

(formatter-badges-allowed-titles)=
### FORMATTER_BADGES_ALLOWED_TITLES

```{eval-rst}
List of allowed titles in badges.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L363); [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L11) |

```
['DOI']
```

---

(formatter-badges-enable)=
### FORMATTER_BADGES_ENABLE
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(formatter-badges-max-cache-age)=
### FORMATTER_BADGES_MAX_CACHE_AGE

```{eval-rst}
The maximum amount of time a badge will be considered fresh.
```

| **Invenio RDM Default Value** | `0` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L17) |

---

(formatter-badges-title-mapping)=
### FORMATTER_BADGES_TITLE_MAPPING

```{eval-rst}
Mapping of titles.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L366); [invenio-formatter](https://github.com/inveniosoftware/invenio-formatter/blob/master/invenio_formatter/config.py#L14) |

```
{}
```

---

(global-search-models)=
### ***GLOBAL_SEARCH_MODELS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/models.py#L22) |
| **Set by** | {py:func}`~oarepo_config.add_model` |

---

(handle-url)=
### HANDLE_URL
| **OARepo Default Value** | `'https://hdl.handle.net'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L16) |

---

(header-template)=
### ***HEADER_TEMPLATE**

```{eval-rst}
Base header template to be extended on custom headers.
```

| **Invenio RDM Default Value** | `'invenio_theme/header.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L23) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(i18n-default-redirect-endpoint)=
### I18N_DEFAULT_REDIRECT_ENDPOINT

```{eval-rst}
Endpoint to redirect if no next parameter is provided.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L41) |

---

(i18n-js-distr-exceptional-package-map)=
### I18N_JS_DISTR_EXCEPTIONAL_PACKAGE_MAP

```{eval-rst}
Exceptional package name mapper for JS/React localization distribution.

Webpack entrypoints are used to determine the asset path for distributing JS/React localizations.
Entrypoint names usually match the corresponding package name, but some differ.
This mapping is used to associate exceptional entrypoint names with their package names.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L53) |

```
{}
```

---

(i18n-languages)=
### ***I18N_LANGUAGES**

```{eval-rst}
List of tuples of available languages.

Example configuration with english and danish with english as default language:

.. code-block:: python

    from flask_babel import lazy_gettext as _
    BABEL_DEFAULT_LOCALE = 'en'
    I18N_LANGUAGES = (('da', _('Danish')),)

.. note:: You should not include ``BABEL_DEFAULT_LOCALE`` in this list.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L21) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

```
[]
```

---

(i18n-session-key)=
### I18N_SESSION_KEY

```{eval-rst}
Key to retrieve language identifier from the current session object.
```

| **Invenio RDM Default Value** | `'language'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L44) |

---

(i18n-set-language-url)=
### I18N_SET_LANGUAGE_URL

```{eval-rst}
URL prefix for set language view.

Set to ``None`` to prevent view from being installed.
```

| **Invenio RDM Default Value** | `'/lang'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L35) |

---

(i18n-transifex-js-resources-map)=
### I18N_TRANSIFEX_JS_RESOURCES_MAP

```{eval-rst}
Mapping of transifex resource names to invenioRDM package names.

All resources/packages that should be translated with Transifex should be added here.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L61) |

```
{}
```

---

(i18n-translations-paths)=
### I18N_TRANSLATIONS_PATHS

```{eval-rst}
List of paths to load message catalogs from.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L18) |

```
[]
```

---

(i18n-user-lang-attr)=
### I18N_USER_LANG_ATTR

```{eval-rst}
Attribute name which contains language identifier on the User object.

It is used only when the login manager is installed and a user is
authenticated. Set to ``None`` to prevent selector from being used.
```

| **Invenio RDM Default Value** | `'prefered_language'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-i18n](https://github.com/inveniosoftware/invenio-i18n/blob/master/invenio_i18n/config.py#L47) |

---

(iiif-api-decorator-handler)=
### IIIF_API_DECORATOR_HANDLER
| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1144) |

---

(iiif-api-info-response-skeleton)=
### IIIF_API_INFO_RESPONSE_SKELETON
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'v1': {'@context': 'http://library.stanford.edu/iiif/image-api/1.1/context.json',
        '@id': '',
        'height': '',
        'profile': 'http://library.stanford.edu/iiif/image-api/compliance.html#level1',
        'scale_factors': [1, 2, 4, 8, 16, 32, 64],
        'tile_height': 256,
        'tile_width': 256,
        'width': ''},
 'v2': {'@context': 'http://iiif.io/api/image/2/context.json',
        '@id': '',
        'height': '',
        'profile': ['http://iiif.io/api/image/2/level2.json'],
        'protocol': 'http://iiif.io/api/image',
        'tiles': [{'scaleFactors': [1, 2, 4, 8, 16, 32, 64], 'width': 256}],
        'width': ''}}
```

---

(iiif-cache-handler)=
### IIIF_CACHE_HANDLER
| **Default Value** | `'flask_iiif.cache.simple:ImageSimpleCache'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(iiif-cache-ignore-errors)=
### IIIF_CACHE_IGNORE_ERRORS
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(iiif-cache-redis-url)=
### IIIF_CACHE_REDIS_URL
| **Default Value** | `'redis://localhost:6379/0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(iiif-cache-time)=
### IIIF_CACHE_TIME
| **Default Value** | `172800` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(iiif-converters)=
### IIIF_CONVERTERS
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('', 'L', 'L', '1', '', '')
```

---

(iiif-formats)=
### IIIF_FORMATS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1152) |

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

(iiif-formats-pil-map)=
### IIIF_FORMATS_PIL_MAP
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1164) |

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

(iiif-gif-temp-folder-path)=
### IIIF_GIF_TEMP_FOLDER_PATH
| **Default Value** | `'/tmp'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(iiif-mode)=
### IIIF_MODE
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'1': ['default', 'bitonal'],
 'CMYK': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'F': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'I': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'L': ['default', 'gray', 'grey', 'bitonal'],
 'P': ['default', 'gray', 'grey', 'bitonal'],
 'RGB': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'RGBA': ['default', 'color', 'gray', 'grey', 'bitonal'],
 'YCbCr': ['default', 'color', 'gray', 'grey', 'bitonal']}
```

---

(iiif-preview-template)=
### IIIF_PREVIEW_TEMPLATE

```{eval-rst}
Template for IIIF image preview.
```

| **Invenio RDM Default Value** | `'invenio_app_rdm/records/iiif_preview.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1141) |

---

(iiif-qualities)=
### IIIF_QUALITIES
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('default', 'gray', 'grey', 'bitonal', 'color', 'native')
```

---

(iiif-simple-previewer-native-extensions)=
### IIIF_SIMPLE_PREVIEWER_NATIVE_EXTENSIONS

```{eval-rst}
Images are converted to JPEG for preview, unless listed here.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1146) |

```
['gif', 'png']
```

---

(iiif-simple-previewer-size)=
### IIIF_SIMPLE_PREVIEWER_SIZE

```{eval-rst}
Size of image in IIIF preview window. Must be a valid IIIF Image API size parameter.
```

| **Invenio RDM Default Value** | `'!800,800'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1149) |

---

(iiif-tiles-converter-params)=
### IIIF_TILES_CONVERTER_PARAMS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L939) |

```
{'Q': 90, 'compression': 'jpeg', 'tile_height': 256, 'tile_width': 256}
```

---

(iiif-tiles-generation-enabled)=
### IIIF_TILES_GENERATION_ENABLED

```{eval-rst}
Enable generating pyramidal TIFF tiles for uploaded images.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L918) |

---

(iiif-tiles-storage-base-path)=
### IIIF_TILES_STORAGE_BASE_PATH

```{eval-rst}
Base path for storing IIIF tiles.

Relative paths are resolved against the application instance path.
```

| **Invenio RDM Default Value** | `'images/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L933) |

---

(iiif-tiles-valid-extensions)=
### IIIF_TILES_VALID_EXTENSIONS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L921) |

```
['jp2', 'jpeg', 'jpg', 'pdf', 'png', 'png', 'tif', 'tiff']
```

---

(iiif-validations)=
### IIIF_VALIDATIONS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'v1': {'image_format': {'ignore': '',
                         'validate': '(gif|jp2|jpe?g|pdf|png|tiff?|webp)'},
        'quality': {'ignore': 'default', 'validate': '(native|color|gr[ae]y|bitonal)'},
        'region': {'ignore': 'full',
                   'validate': '(^full|(pct:)?([\\d.]+,){3}([\\d.]+))'},
        'rotation': {'ignore': '0', 'validate': '^[\\d.]+$'},
        'size': {'ignore': 'full',
                 'validate': '(^full|[\\d.]+,|,[\\d.]+|pct:[\\d.]+|[\\d.]+,[\\d.]+|![\\d.]+,[\\d.]+)'}},
 'v2': {'image_format': {'ignore': '',
                         'validate': '(gif|jp2|jpe?g|pdf|png|tiff?|webp)'},
        'quality': {'ignore': 'default', 'validate': '(default|color|gr[ae]y|bitonal)'},
        'region': {'ignore': 'full',
                   'validate': '(^full|(pct:)?([\\d.]+,){3}([\\d.]+))'},
        'rotation': {'ignore': '0', 'validate': '^!?[\\d.]+$'},
        'size': {'ignore': 'full',
                 'validate': '(^full|[\\d.]+,|,[\\d.]+|pct:[\\d.]+|[\\d.]+,[\\d.]+|![\\d.]+,[\\d.]+)'}}}
```

---

(indexer-before-index-hooks)=
### INDEXER_BEFORE_INDEX_HOOKS

```{eval-rst}
List of automatically connected hooks (function or importable string).
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L59) |

```
[]
```

---

(indexer-bulk-request-timeout)=
### INDEXER_BULK_REQUEST_TIMEOUT

```{eval-rst}
Request timeout to use in Bulk indexing.
```

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L46) |

---

(indexer-default-index)=
### INDEXER_DEFAULT_INDEX

```{eval-rst}
Default index to use if no schema is defined.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L13) |

---

(indexer-max-bulk-consumers)=
### INDEXER_MAX_BULK_CONSUMERS

```{eval-rst}
Maximum number of concurrent consumers for bulk indexing.

This threshold is applied per queue, so each indexing queue would
have a maximum of 5 consumers at the same time.
```

| **Invenio RDM Default Value** | `5` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L49) |

---

(indexer-mq-exchange)=
### INDEXER_MQ_EXCHANGE

```{eval-rst}
Default exchange for message queue.
```

| **Invenio RDM Default Value** | `Exchange('indexer', type='direct')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L16) |

---

(indexer-mq-publish-kwargs)=
### INDEXER_MQ_PUBLISH_KWARGS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L25) |

```
{}
```

---

(indexer-mq-queue)=
### INDEXER_MQ_QUEUE

```{eval-rst}
Default queue for message queue.
```

| **Invenio RDM Default Value** | `Queue('indexer', exchange=INDEXER_MQ_EXCHANGE, routing_key='indexer')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L19) |

---

(indexer-mq-routing-key)=
### INDEXER_MQ_ROUTING_KEY

```{eval-rst}
Default routing key for message queue.
```

| **Invenio RDM Default Value** | `'indexer'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L22) |

---

(indexer-record-to-index)=
### INDEXER_RECORD_TO_INDEX

```{eval-rst}
Provide an implementation of record_to_index function
```

| **Invenio RDM Default Value** | `'invenio_indexer.utils.default_record_to_index'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L56) |

---

(indexer-replace-refs)=
### INDEXER_REPLACE_REFS

```{eval-rst}
Whether to replace JSONRefs prior to indexing record.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-indexer](https://github.com/inveniosoftware/invenio-indexer/blob/master/invenio_indexer/config.py#L43) |

---

(info-endpoint-components)=
### INFO_ENDPOINT_COMPONENTS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['oarepo_rdm.info:RDMInfoComponent']
```

---

(instance-theme-file)=
### ***INSTANCE_THEME_FILE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(invenio-cache-type)=
### ***INVENIO_CACHE_TYPE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/generic_parameters.py#L46) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(invenio-rdm-enabled)=
### INVENIO_RDM_ENABLED
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(invenio-vocabulary-type-metadata)=
### ***INVENIO_VOCABULARY_TYPE_METADATA**
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |
| **Set by** | {py:func}`~oarepo_config.configure_vocabulary` |

```
{}
```

---

(javascript-packages-manager)=
### ***JAVASCRIPT_PACKAGES_MANAGER**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(jobs-default-queue)=
### JOBS_DEFAULT_QUEUE

```{eval-rst}
Default Celery queue.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L53) |

---

(jobs-facets)=
### JOBS_FACETS

```{eval-rst}
Facets/aggregations for Jobs results.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L32) |

```
{}
```

---

(jobs-logging)=
### JOBS_LOGGING

```{eval-rst}
Enable logging for jobs.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L85) |

---

(jobs-logging-index)=
### JOBS_LOGGING_INDEX

```{eval-rst}
"Index name for job logs.
```

| **Invenio RDM Default Value** | `'job-logs'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L88) |

---

(jobs-logging-level)=
### ***JOBS_LOGGING_LEVEL**

```{eval-rst}
Logging level for jobs.
```

| **Invenio RDM Default Value** | `'DEBUG'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L82) |
| **Set by** | {py:func}`~oarepo_config.configure_jobs` |

---

(jobs-logging-retention-days)=
### JOBS_LOGGING_RETENTION_DAYS

```{eval-rst}
Retention period for job logs in days.
```

| **Invenio RDM Default Value** | `90` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L91) |

---

(jobs-logs-batch-size)=
### JOBS_LOGS_BATCH_SIZE

```{eval-rst}
Number of log results to fetch per batch from the search backend.
```

| **Invenio RDM Default Value** | `500` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L97) |

---

(jobs-logs-max-results)=
### JOBS_LOGS_MAX_RESULTS

```{eval-rst}
Maximum total number of log results to return in a single search request.
```

| **Invenio RDM Default Value** | `2000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L94) |

---

(jobs-permission-policy)=
### JOBS_PERMISSION_POLICY

```{eval-rst}
Permission policy for jobs.
```

| **Invenio RDM Default Value** | `JobPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L23) |

---

(jobs-queues)=
### JOBS_QUEUES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L35) |

```
{'celery': {'description': l'Default queue', 'name': 'celery', 'title': l'Default'},
 'low': {'description': l'Low priority queue', 'name': 'low', 'title': l'Low'}}
```

---

(jobs-runs-permission-policy)=
### JOBS_RUNS_PERMISSION_POLICY

```{eval-rst}
Permission policy for job runs.
```

| **Invenio RDM Default Value** | `RunPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L26) |

---

(jobs-search)=
### JOBS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L76) |

```
{'facets': [], 'sort': ['jobs', 'last_run_start_time', 'user', 'next_run']}
```

---

(jobs-sort-options)=
### JOBS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L56) |

```
{'jobs': {'fields': ['jobs'], 'title': l'Jobs'},
 'last_run_start_time': {'fields': ['last_run_start_time'], 'title': l'Last run'},
 'next_run': {'fields': ['next_run'], 'title': l'Next run'},
 'user': {'fields': ['user'], 'title': l'Started by'}}
```

---

(jobs-tasks-permission-policy)=
### JOBS_TASKS_PERMISSION_POLICY

```{eval-rst}
Permission policy for tasks.
```

| **Invenio RDM Default Value** | `TasksPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-jobs](https://github.com/inveniosoftware/invenio-jobs/blob/master/invenio_jobs/config.py#L20) |

---

(jsonschemas-endpoint)=
### JSONSCHEMAS_ENDPOINT

```{eval-rst}
Default schema endpoint.
```

| **Invenio RDM Default Value** | `'/schemas'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L14) |

---

(jsonschemas-host)=
### ***JSONSCHEMAS_HOST**

```{eval-rst}
Default json schema host.
```

| **Invenio RDM Default Value** | `'localhost'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L11); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L609) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(jsonschemas-loader-cls)=
### JSONSCHEMAS_LOADER_CLS

```{eval-rst}
Loader class used in ``JSONRef`` when replacing ``$ref``.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L31) |

---

(jsonschemas-local-refresolver-uri-scheme)=
### JSONSCHEMAS_LOCAL_REFRESOLVER_URI_SCHEME

```{eval-rst}
Non-standard URI scheme to reference local schemas.
```

| **Invenio RDM Default Value** | `'local://'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L70) |

---

(jsonschemas-register-endpoints-api)=
### JSONSCHEMAS_REGISTER_ENDPOINTS_API

```{eval-rst}
Register the endpoints on the API app.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L42); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L603) |

---

(jsonschemas-register-endpoints-ui)=
### JSONSCHEMAS_REGISTER_ENDPOINTS_UI

```{eval-rst}
Register the endpoints on the UI app.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L45); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L606) |

---

(jsonschemas-replace-refs)=
### JSONSCHEMAS_REPLACE_REFS

```{eval-rst}
Whether to resolve $ref before serving a schema.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L20) |

---

(jsonschemas-resolver-cls)=
### JSONSCHEMAS_RESOLVER_CLS

```{eval-rst}
Resolver used to resolve the schema.

if :py:const:`invenio_jsonschemas.config.JSONSCHEMAS_RESOLVE_SCHEMA` is
``True`` or there is ``?resolved=1`` parameter on the request the resolver
will run over the schema. This can be used for custom schemas resolver.
```

| **Invenio RDM Default Value** | `'invenio_jsonschemas.utils.resolve_schema'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L34) |

---

(jsonschemas-resolve-schema)=
### JSONSCHEMAS_RESOLVE_SCHEMA

```{eval-rst}
Whether to resolve schema using the Resolver Class.

If is ``True``, will replace $ref and run the
:py:const:`invenio_jsonschemas.config.JSONSCHEMAS_RESOLVER_CLS` class
before serving a schema.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L23) |

---

(jsonschemas-schemas)=
### JSONSCHEMAS_SCHEMAS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L48) |

---

(jsonschemas-url-scheme)=
### JSONSCHEMAS_URL_SCHEME

```{eval-rst}
Default url scheme for schemas.
```

| **Invenio RDM Default Value** | `'https'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-jsonschemas](https://github.com/inveniosoftware/invenio-jsonschemas/blob/master/invenio_jsonschemas/config.py#L17) |

---

(logging-console)=
### LOGGING_CONSOLE

```{eval-rst}
Enable logging to the console.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L27) |

---

(logging-console-level)=
### LOGGING_CONSOLE_LEVEL

```{eval-rst}
Console logging level.

Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``,
``INFO``, ``DEBUG``, or ``NOTSET``.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L37) |

---

(logging-console-pywarnings)=
### LOGGING_CONSOLE_PYWARNINGS

```{eval-rst}
Enable logging of Python warnings to the console.

By default, warnings are logged to the console if the application is in debug
mode, otherwise warnings are not logged.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L30) |

---

(logging-fs-backupcount)=
### LOGGING_FS_BACKUPCOUNT

```{eval-rst}
Number of rotated log files to keep.
```

| **Invenio RDM Default Value** | `5` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L54) |

---

(logging-fs-level)=
### LOGGING_FS_LEVEL

```{eval-rst}
Filesystem logging level.

Set to a valid Python logging level: ``CRITICAL``, ``ERROR``, ``WARNING``,
``INFO``, ``DEBUG``, or ``NOTSET``.
```

| **Invenio RDM Default Value** | `'WARNING'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L60) |

---

(logging-fs-logfile)=
### LOGGING_FS_LOGFILE

```{eval-rst}
Enable logging to the filesystem.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L48) |

---

(logging-fs-maxbytes)=
### LOGGING_FS_MAXBYTES

```{eval-rst}
Maximum size of logging file. Default: 100MB.
```

| **Invenio RDM Default Value** | `104857600` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L57) |

---

(logging-fs-pywarnings)=
### LOGGING_FS_PYWARNINGS

```{eval-rst}
Enable logging of Python warnings to filesystem logging.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L51) |

---

(logging-sentry-celery)=
### LOGGING_SENTRY_CELERY

```{eval-rst}
Configure Celery to send logging to Sentry.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L81) |

---

(logging-sentry-class)=
### LOGGING_SENTRY_CLASS

```{eval-rst}
Import path of sentry Flask extension class.

This allows you to customize the Sentry extension class.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L90) |

---

(logging-sentry-init-kwargs)=
### LOGGING_SENTRY_INIT_KWARGS

```{eval-rst}
Pass extra options when initializing Sentry instance.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L95) |

---

(logging-sentry-level)=
### LOGGING_SENTRY_LEVEL

```{eval-rst}
Sentry logging level.

Defaults to only reporting errors and warnings.
```

| **Invenio RDM Default Value** | `'WARNING'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L72) |

---

(logging-sentry-pywarnings)=
### LOGGING_SENTRY_PYWARNINGS

```{eval-rst}
Enable logging of Python warnings to Sentry.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L78) |

---

(logging-sentry-redis)=
### LOGGING_SENTRY_REDIS

```{eval-rst}
Configure REDIS to send logging to Sentry.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L87) |

---

(logging-sentry-sqlalchemy)=
### LOGGING_SENTRY_SQLALCHEMY

```{eval-rst}
Configure SQL Alchemy to send logging to Sentry.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L84) |

---

(mail-debug)=
### MAIL_DEBUG
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(mail-default-reply-to)=
### MAIL_DEFAULT_REPLY_TO

```{eval-rst}
Reply to mail address for e-mails.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L19) |

---

(mail-default-sender)=
### ***MAIL_DEFAULT_SENDER**

```{eval-rst}
Email address used as sender of account registration emails.

`SECURITY_EMAIL_SENDER` will default to this value.
```

| **Invenio RDM Default Value** | `'info@inveniosoftware.org'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L376) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(mail-max-attachment-size)=
### MAIL_MAX_ATTACHMENT_SIZE

```{eval-rst}
Max size of inline attachments, in bytes.
```

| **Invenio RDM Default Value** | `1000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L22) |

---

(mail-max-retries)=
### MAIL_MAX_RETRIES

```{eval-rst}
How often will we repeat if a problem occurred.
```

| **Invenio RDM Default Value** | `2` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L25) |

---

(mail-min-logging-level)=
### MAIL_MIN_LOGGING_LEVEL

```{eval-rst}
Minimum logging level for the mail logger.
```

| **Invenio RDM Default Value** | `40` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-mail](https://github.com/inveniosoftware/invenio-mail/blob/master/invenio_mail/config.py#L28) |

---

(mail-suppress-send)=
### ***MAIL_SUPPRESS_SEND**

```{eval-rst}
Disable email sending by default.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L373) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(matomo-analytics-site-id)=
### ***MATOMO_ANALYTICS_SITE_ID**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(matomo-analytics-template)=
### ***MATOMO_ANALYTICS_TEMPLATE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(matomo-analytics-url)=
### ***MATOMO_ANALYTICS_URL**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(max-content-length)=
### MAX_CONTENT_LENGTH

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-files-rest](https://github.com/inveniosoftware/invenio-files-rest/blob/master/invenio_files_rest/config.py#L15); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L214) |

---

(max-cookie-size)=
### MAX_COOKIE_SIZE
| **Default Value** | `4093` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(max-form-memory-size)=
### MAX_FORM_MEMORY_SIZE
| **Default Value** | `500000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(max-form-parts)=
### MAX_FORM_PARTS
| **Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(multiprofiler-base-template)=
### MULTIPROFILER_BASE_TEMPLATE

```{eval-rst}
Base template for the profiler page.
```

| **Invenio RDM Default Value** | `'flask_multiprofiler/index.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1620) |

---

(multiprofiler-ignored-endpoints)=
### MULTIPROFILER_IGNORED_ENDPOINTS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1623) |

```
[
    'static',
    '_debug_toolbar.static',
    'profiler\\..+',
    'invenio_formatter_badges.badge',
]
```

---

(multiprofiler-permission)=
### MULTIPROFILER_PERMISSION

```{eval-rst}
Function to check for permissions to access the profiler.
```

| **Invenio RDM Default Value** | `administration_permission.can` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1631) |

---

(notifications-backends)=
### NOTIFICATIONS_BACKENDS

```{eval-rst}
Notification backends.

.. code-block::python

    NOTIFICATIONS_BACKENDS = {
        "email": EmailBackend,
        "cern": CERNNotificationsBackend,
        "slack": SlackBackend,
    }
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L12); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1426) |

```
{'email': <invenio_notifications.backends.email.EmailNotificationBackend object at 0x111655010>}
```

---

(notifications-builders)=
### NOTIFICATIONS_BUILDERS

```{eval-rst}
Notification builders.

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
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L24); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1432) |

```
{'comment-request-event.create': <class 'invenio_requests.notifications.builders.CommentRequestEventCreateNotificationBuilder'>,
 'comment-request-event.reply': <class 'invenio_requests.notifications.builders.CommentRequestEventReplyNotificationBuilder'>,
 'comment-subcommunity-invitation-request.create': <class 'invenio_communities.notifications.builders.SubComInvCommentNotificationBuilder'>,
 'comment-subcommunity-request.create': <class 'invenio_communities.notifications.builders.SubComReqCommentNotificationBuilder'>,
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
 'community-submission.accept': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionAcceptNotificationBuilder'>,
 'community-submission.cancel': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionCancelNotificationBuilder'>,
 'community-submission.decline': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionDeclineNotificationBuilder'>,
 'community-submission.expire': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionExpireNotificationBuilder'>,
 'community-submission.submit': <class 'invenio_rdm_records.notifications.builders.CommunityInclusionSubmittedNotificationBuilder'>,
 'delete-published-record-request-event.accept': <class 'oarepo_requests.notifications.builders.delete_published_record.DeletePublishedRecordRequestAcceptNotificationBuilder'>,
 'delete-published-record-request-event.decline': <class 'oarepo_requests.notifications.builders.delete_published_record.DeletePublishedRecordRequestDeclineNotificationBuilder'>,
 'delete-published-record-request-event.submit': <class 'oarepo_requests.notifications.builders.delete_published_record.DeletePublishedRecordRequestSubmitNotificationBuilder'>,
 'grant-user-access.create': <class 'invenio_rdm_records.notifications.builders.GrantUserAccessNotificationBuilder'>,
 'guest-access-request-token.create': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestTokenCreateNotificationBuilder'>,
 'guest-access-request.accept': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestAcceptNotificationBuilder'>,
 'guest-access-request.cancel': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestCancelNotificationBuilder'>,
 'guest-access-request.decline': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestDeclineNotificationBuilder'>,
 'guest-access-request.submit': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestSubmitNotificationBuilder'>,
 'guest-access-request.submitted': <class 'invenio_rdm_records.notifications.builders.GuestAccessRequestSubmittedNotificationBuilder'>,
 'publish-draft-request-event.accept': <class 'oarepo_requests.notifications.builders.publish.PublishDraftRequestAcceptNotificationBuilder'>,
 'publish-draft-request-event.decline': <class 'oarepo_requests.notifications.builders.publish.PublishDraftRequestDeclineNotificationBuilder'>,
 'publish-draft-request-event.submit': <class 'oarepo_requests.notifications.builders.publish.PublishDraftRequestSubmitNotificationBuilder'>,
 'record-deletion.accept': <class 'invenio_rdm_records.notifications.builders.RecordDeletionAcceptNotificationBuilder'>,
 'record-deletion.decline': <class 'invenio_rdm_records.notifications.builders.RecordDeletionDeclineNotificationBuilder'>,
 'subcommunity-invitation-request.accept': <class 'invenio_communities.notifications.builders.SubComInvitationAccept'>,
 'subcommunity-invitation-request.create': <class 'invenio_communities.notifications.builders.SubComInvitationCreate'>,
 'subcommunity-invitation-request.decline': <class 'invenio_communities.notifications.builders.SubComInvitationDecline'>,
 'subcommunity-invitation-request.expire': <class 'invenio_communities.notifications.builders.SubComInvitationExpire'>,
 'subcommunity-request.accept': <class 'invenio_communities.notifications.builders.SubCommunityAccept'>,
 'subcommunity-request.create': <class 'invenio_communities.notifications.builders.SubCommunityCreate'>,
 'subcommunity-request.decline': <class 'invenio_communities.notifications.builders.SubCommunityDecline'>,
 'user-access-request.accept': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestAcceptNotificationBuilder'>,
 'user-access-request.cancel': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestCancelNotificationBuilder'>,
 'user-access-request.decline': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestDeclineNotificationBuilder'>,
 'user-access-request.submit': <class 'invenio_rdm_records.notifications.builders.UserAccessRequestSubmitNotificationBuilder'>}
```

---

(notifications-entity-resolvers)=
### NOTIFICATIONS_ENTITY_RESOLVERS

```{eval-rst}
List of entity resolvers used by notification builders.

.. code-block::python

    NOTIFICATIONS_ENTITY_RESOLVERS = [
        UserResultItemResolver(),
        RDMRecordResultItemResolver(),
        CommunityResultItemResolver(),
        RequestResultItemResolver(),
        RequestEventResultItemResolver(),
    ]
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L40); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1485) |

```
[<invenio_rdm_records.requests.entity_resolvers.EmailResolver object at 0x111655160>,
 <invenio_rdm_records.requests.entity_resolvers.RDMRecordServiceResultResolver object at 0x111655400>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object at 0x111655550>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object at 0x1116ac550>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object at 0x1116ac690>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object at 0x1116dc180>,
 <invenio_records_resources.references.entity_resolvers.results.ServiceResultResolver object at 0x1116dc2b0>]
```

---

(notifications-group-email-domain)=
### NOTIFICATIONS_GROUP_EMAIL_DOMAIN

```{eval-rst}
Domain suffix to append to group names when email is not provided.

When a recipient is a group and has no email or email_hidden field, the group's
name will be used as the email address with this domain appended.

Example:
    NOTIFICATIONS_GROUP_EMAIL_DOMAIN = "cern.ch"
    # Group "physics-team" becomes "physics-team@cern.ch"

Set to None to disable domain formatting (groups must have email field set).
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L61) |

---

(notifications-settings-view-function)=
### NOTIFICATIONS_SETTINGS_VIEW_FUNCTION

```{eval-rst}
View function for notification settings.

This should be set higher up in the module hierarchy (e.g. invenio-app-rdm), as
this module does not have knowledge of the settings view.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-notifications](https://github.com/inveniosoftware/invenio-notifications/blob/master/invenio_notifications/config.py#L54); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1496) |

---

(notification-recipients-resolvers)=
### NOTIFICATION_RECIPIENTS_RESOLVERS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'action_need': <function <lambda> at 0x112b099b0>,
 'group': <function <lambda> at 0x1121c05c0>,
 'multiple': <function <lambda> at 0x1121c0460>,
 'user': <function <lambda> at 0x1121c0300>}
```

---

(oaiserver-admin-emails)=
### OAISERVER_ADMIN_EMAILS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L37) |

```
['info@inveniosoftware.org']
```

---

(oaiserver-base-template)=
### OAISERVER_BASE_TEMPLATE
| **Default Value** | `'invenio_oaiserver/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oaiserver-cache-key)=
### OAISERVER_CACHE_KEY

```{eval-rst}
Key prefix added before all keys in cache server.
```

| **Invenio RDM Default Value** | `'DynamicOAISets::'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L162) |

---

(oaiserver-celery-task-chunk-size)=
### OAISERVER_CELERY_TASK_CHUNK_SIZE

```{eval-rst}
Specify the maximum number of records each task will update.
```

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L165) |

---

(oaiserver-compressions)=
### OAISERVER_COMPRESSIONS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L46) |

```
['identity']
```

---

(oaiserver-control-number-fetcher)=
### OAISERVER_CONTROL_NUMBER_FETCHER

```{eval-rst}
PIDStore fetcher for the OAI ID control number.
```

| **Invenio RDM Default Value** | `'recid'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L168) |

---

(oaiserver-created-key)=
### OAISERVER_CREATED_KEY

```{eval-rst}
Record created key.
```

| **Invenio RDM Default Value** | `'created'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L688); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L132) |

---

(oaiserver-delete-percolator-function)=
### OAISERVER_DELETE_PERCOLATOR_FUNCTION
| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:_delete_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L113) |

---

(oaiserver-descriptions)=
### OAISERVER_DESCRIPTIONS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L171) |

```
[]
```

---

(oaiserver-getrecord-fetcher)=
### OAISERVER_GETRECORD_FETCHER

```{eval-rst}
Record data fetcher for serialization.
```

| **Invenio RDM Default Value** | `'invenio_rdm_records.oai:getrecord_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L703); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L153) |

---

(oaiserver-granularity)=
### OAISERVER_GRANULARITY

```{eval-rst}
The finest harvesting granularity supported by the repository.

The legitimate values are ``YYYY-MM-DD`` and ``YYYY-MM-DDThh:mm:ssZ``
with meanings as defined in ISO8601.
```

| **Invenio RDM Default Value** | `'YYYY-MM-DDThh:mm:ssZ'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L50) |

---

(oaiserver-id-fetcher)=
### OAISERVER_ID_FETCHER

```{eval-rst}
OAI ID fetcher function.
```

| **Invenio RDM Default Value** | `'invenio_rdm_records.oai:oaiid_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L639); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L126) |

---

(oaiserver-id-prefix)=
### ***OAISERVER_ID_PREFIX**

```{eval-rst}
The prefix that will be applied to the generated OAI-PMH ids.
```

| **Invenio RDM Default Value** | `'oai:tlha144.cesnet.cz:'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L633); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L24) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(oaiserver-last-update-key)=
### OAISERVER_LAST_UPDATE_KEY

```{eval-rst}
Record update key.
```

| **Invenio RDM Default Value** | `'updated'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L685); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L129) |

---

(oaiserver-metadata-formats)=
### OAISERVER_METADATA_FORMATS
| **OARepo Default Value** | `<oarepo_rdm.oai.config.OAIServerMetadataFormats object at 0x111f1a3c0>` |
|--------------|-----------|
| **Type** | OAIServerMetadataFormats |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L53); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L642); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L70) |

---

(oaiserver-new-percolator-function)=
### OAISERVER_NEW_PERCOLATOR_FUNCTION
| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:_new_percolator'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L111) |

---

(oaiserver-page-size)=
### OAISERVER_PAGE_SIZE

```{eval-rst}
Define maximum length of list responses.

Request with verbs ``ListRecords``, ``ListIdentifiers``, and ``ListSets``
are affected by this option.
```

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L17) |

---

(oaiserver-percolator-dedicated-index)=
### OAISERVER_PERCOLATOR_DEDICATED_INDEX

```{eval-rst}
Create a dedicated index for the percolators, instead of storing them in
the same index as the records.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L141) |

---

(oaiserver-protocol-version)=
### OAISERVER_PROTOCOL_VERSION
| **Invenio RDM Default Value** | `'2.0'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L35) |

---

(oaiserver-query-parser)=
### OAISERVER_QUERY_PARSER

```{eval-rst}
Define query parser for OIASet definition.
```

| **Invenio RDM Default Value** | `invenio_search.engine.dsl.Q` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L156) |

---

(oaiserver-query-parser-fields)=
### OAISERVER_QUERY_PARSER_FIELDS

```{eval-rst}
Define query parser search fields list for OIASet definition.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L159) |

```
[]
```

---

(oaiserver-record-cls)=
### OAISERVER_RECORD_CLS

```{eval-rst}
Record retrieval class.
```

| **Invenio RDM Default Value** | `'invenio_rdm_records.records.api:RDMRecord'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L691); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L150) |

---

(oaiserver-record-index)=
### OAISERVER_RECORD_INDEX

```{eval-rst}
Specify a search index with records that should be exposed via OAI-PMH.
```

| **Invenio RDM Default Value** | `'oaisource'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L697); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L31) |

---

(oaiserver-record-list-sets-fetcher)=
### OAISERVER_RECORD_LIST_SETS_FETCHER

```{eval-rst}
Record's list OAI sets function.
```

| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:sets_search_all'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L138) |

---

(oaiserver-record-sets-fetcher)=
### OAISERVER_RECORD_SETS_FETCHER

```{eval-rst}
Record's OAI sets function.
```

| **Invenio RDM Default Value** | `'invenio_oaiserver.percolator:find_sets_for_record'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L694); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L135) |

---

(oaiserver-register-record-signals)=
### OAISERVER_REGISTER_RECORD_SIGNALS

```{eval-rst}
Catch record/set insert/update/delete signals and update the `_oai`
field.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L115) |

---

(oaiserver-register-set-signals)=
### OAISERVER_REGISTER_SET_SIGNALS

```{eval-rst}
Catch set insert/update/delete signals and update the `_oai` record
field.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L119) |

---

(oaiserver-repository-name)=
### ***OAISERVER_REPOSITORY_NAME**
| **Default Value** | `'Invenio-OAIServer'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |
| **Set by** | {py:func}`~oarepo_config.configure_oai` |

---

(oaiserver-resumption-token-expire-time)=
### OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME

```{eval-rst}
The expiration time of a resumption token in seconds.

**Default: 60 seconds = 1 minute**.

.. note::

    Setting longer expiration time may have a negative impact on your
    search cluster as it might need to keep open cursors.

    https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html
```

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L57) |

---

(oaiserver-search-cls)=
### OAISERVER_SEARCH_CLS

```{eval-rst}
Class for record search.
```

| **Invenio RDM Default Value** | `'invenio_rdm_records.oai:OAIRecordSearch'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L636); [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L123) |

---

(oaiserver-set-records-query-fetcher)=
### OAISERVER_SET_RECORDS_QUERY_FETCHER
| **Invenio RDM Default Value** | `'invenio_oaiserver.fetchers:set_records_query_fetcher'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L146) |

---

(oaiserver-xsl-url)=
### OAISERVER_XSL_URL

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-oaiserver](https://github.com/inveniosoftware/invenio-oaiserver/blob/master/invenio_oaiserver/config.py#L222) |

---

(oarepo-checks-default-chat-einfra-client)=
### ***OAREPO_CHECKS_DEFAULT_CHAT_EINFRA_CLIENT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/llm.py#L18) |
| **Set by** | {py:func}`~oarepo_config.configure_llm` |

---

(oarepo-checks-default-llm-client)=
### ***OAREPO_CHECKS_DEFAULT_LLM_CLIENT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/llm.py#L18) |
| **Set by** | {py:func}`~oarepo_config.configure_llm` |

---

(oarepo-checks-llm-clients)=
### ***OAREPO_CHECKS_LLM_CLIENTS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/llm.py#L18) |
| **Set by** | {py:func}`~oarepo_config.configure_llm` |

---

(oarepo-communities-default-workflow)=
### OAREPO_COMMUNITIES_DEFAULT_WORKFLOW
| **Default Value** | `'default'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oarepo-models)=
### OAREPO_MODELS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'affiliations': <oarepo_runtime.api.Model object at 0x1116afd90>,
 'awards': <oarepo_runtime.api.Model object at 0x11179e2c0>,
 'funders': <oarepo_runtime.api.Model object at 0x1116ace10>,
 'names': <oarepo_runtime.api.Model object at 0x11179e3f0>,
 'subjects': <oarepo_runtime.api.Model object at 0x1117b68d0>,
 'vocabularies': <oarepo_runtime.api.Model object at 0x11177f620>}
```

---

(oarepo-permissions-presets)=
### OAREPO_PERMISSIONS_PRESETS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'vocabularies': <class 'invenio_vocabularies.services.permissions.PermissionPolicy'>}
```

---

(oarepo-requests-default-receiver)=
### OAREPO_REQUESTS_DEFAULT_RECEIVER
| **Default Value** | `'oarepo_requests.receiver.default_workflow_receiver_function'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oarepo-ui-jinjax-filters)=
### OAREPO_UI_JINJAX_FILTERS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-ui](https://github.com/oarepo/oarepo-ui/blob/master/oarepo_ui/config.py#L34) |

```
{'append_query_params': 'oarepo_ui.utils:append_query_params',
 'as_dict': 'oarepo_ui.templating.filters:as_dict',
 'compact_number': 'invenio_app_rdm.records_ui.views.filters:compact_number',
 'localize_number': 'invenio_app_rdm.records_ui.views.filters:localize_number',
 'localized': 'oarepo_ui.templating.filters:localized',
 'truncate_number': 'invenio_app_rdm.records_ui.views.filters:truncate_number',
 'ui_value': 'oarepo_ui.templating.filters:ui_value'}
```

---

(oarepo-ui-jinjax-globals)=
### OAREPO_UI_JINJAX_GLOBALS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-ui](https://github.com/oarepo/oarepo-ui/blob/master/oarepo_ui/config.py#L44) |

```
{'append_query_params': 'oarepo_ui.utils:append_query_params',
 'as_array': 'oarepo_ui.templating.filters:as_array',
 'as_dict': 'oarepo_ui.templating.filters:as_dict',
 'can_view_deposit_page': 'oarepo_ui.utils:can_view_deposit_page',
 'localized': 'oarepo_ui.templating.filters:localized',
 'ui_value': 'oarepo_ui.templating.filters:ui_value',
 'value': 'oarepo_ui.templating.filters:value'}
```

---

(oarepo-ui-less-components)=
### OAREPO_UI_LESS_COMPONENTS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['dl_table', 'dl_table', 'dl_table', 'dl_table']
```

---

(oarepo-ui-multilingual-field-languages)=
### OAREPO_UI_MULTILINGUAL_FIELD_LANGUAGES
| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [oarepo-ui](https://github.com/oarepo/oarepo-ui/blob/master/oarepo_ui/config.py#L90) |

```
[{'text': 'English', 'value': 'en'}, {'text': 'Czech', 'value': 'cs'}]
```

---

(oarepo-ui-overrides)=
### OAREPO_UI_OVERRIDES
| **Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | unknown |

```
{UIComponentOverride(endpoint='invenio_search_ui.search',
                     overridable_id='InvenioAppRdm.Search.ResultsList.item',
                     component=UIComponent(DynamicResultsListItem <@js/oarepo_ui/search/DynamicResultsListItem>, UIComponentImportMode.DEFAULT import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_communities.communities_detail',
                     overridable_id='InvenioCommunities.DetailsSearch.ResultsList.item',
                     component=UIComponent(DynamicResultsListItem <@js/oarepo_ui/search/DynamicResultsListItem>, UIComponentImportMode.DEFAULT import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_communities.communities_detail',
                     overridable_id='InvenioCommunities.DetailsSearch.SearchBar.element',
                     component=UIComponent(ClearableSearchbarElement <@js/oarepo_ui/search/ClearableSearchbarElement>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_settings',
                     overridable_id='InvenioCommunities.CommunityProfileForm.GridRow.DangerZone',
                     component=UIComponent(Disabled <@js/oarepo_ui/components/Disabled>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.invitations',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.InvitationsSearchLayout.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.members',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.ManagerEmptyResults.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.invitations',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.ManagerSearchLayout.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.invitations',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.ManagerEmptyResults.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.members',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.ManagerMembersResultsContainer.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.members',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.InvitationsResultsContainer.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.invitations',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.InvitationsResultsContainer.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.members',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.InvitationsSearchLayout.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.members',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.ManagerSearchLayout.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.invitations',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.ManagerMembersResultsContainer.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.members',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.InvitationsEmptyResults.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.invitations',
                     overridable_id='InvenioCommunities.CommunityMembersSearch.InvitationsEmptyResults.InvitationsModal.container',
                     component=UIComponent(CommunityInvitationsModal <@js/oarepo_communities/components/CommunityInvitationsModal>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_invitation_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_changed_metadata',
                     component=UIComponent(LabelTypePublishChangedMetadata <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.delete_published_record',
                     component=UIComponent(LabelTypeDeletePublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_communities.communities_requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_draft',
                     component=UIComponent(LabelTypePublishDraft <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.new_version',
                     component=UIComponent(LabelTypeNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.user_dashboard_request_view',
                     overridable_id='RequestTypeLabel.layout.publish_new_version',
                     component=UIComponent(LabelTypePublishNewVersion <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='RequestTypeLabel.layout.edit_published_record',
                     component=UIComponent(LabelTypeEditPublishedRecord <@js/oarepo_requests/components/labels>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_draft',
                     component=UIComponent(IconTypePublishDraft <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.new_version',
                     component=UIComponent(IconTypeNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_changed_metadata',
                     component=UIComponent(IconTypePublishChangedMetadata <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.delete_published_record',
                     component=UIComponent(IconTypeDeletePublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_requests.community_dashboard_membership_request_view',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.edit_published_record',
                     component=UIComponent(IconTypeEditPublishedRecord <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm.index',
                     overridable_id='InvenioAppRDM.RecordsList.layout',
                     component=UIComponent(RecordsList <@js/oarepo_ui/search/RecordsList>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_search_ui.search',
                     overridable_id='InvenioAppRdm.Search.SearchBar.element',
                     component=UIComponent(ClearableSearchbarElement <@js/oarepo_ui/search/ClearableSearchbarElement>, UIComponentImportMode.NAMED import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.uploads',
                     overridable_id='InvenioAppRdm.DashboardUploads.ResultsList.item',
                     component=UIComponent(DynamicResultsListItem <@js/oarepo_ui/search/DynamicResultsListItem>, UIComponentImportMode.DEFAULT import)>)),
 UIComponentOverride(endpoint='invenio_app_rdm_users.requests',
                     overridable_id='InvenioRequests.RequestTypeIcon.layout.publish_new_version',
                     component=UIComponent(IconTypePublishNewVersion <@js/oarepo_requests/components/icons>, UIComponentImportMode.NAMED import)>))}
```

---

(oarepo-ui-record-actions)=
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

(oarepo-ui-result-list-item-registration-callbacks)=
### OAREPO_UI_RESULT_LIST_ITEM_REGISTRATION_CALLBACKS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[<function _register_main_search_result_item at 0x112e989e0>,
 <function _register_home_page_search_result_item at 0x112e994e0>,
 <function _register_community_uploads_result_item at 0x114018eb0>,
 <function _register_dashboard_uploads_result_item at 0x114019dd0>]
```

---

(oarepo-vocabularies-permissions-presets)=
### OAREPO_VOCABULARIES_PERMISSIONS_PRESETS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L27) |

```
{'vocabularies': <class 'invenio_vocabularies.services.permissions.PermissionPolicy'>}
```

---

(oarepo-vocabularies-sort-cf)=
### OAREPO_VOCABULARIES_SORT_CF
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[]
```

---

(oarepo-vocabularies-suggest-cf)=
### OAREPO_VOCABULARIES_SUGGEST_CF
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[]
```

---

(oarepo-vocabularies-ui-resource)=
### OAREPO_VOCABULARIES_UI_RESOURCE
| **Default Value** | `'oarepo_vocabularies.ui.resources.resource:InvenioVocabulariesUIResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oarepo-vocabularies-ui-resource-config)=
### OAREPO_VOCABULARIES_UI_RESOURCE_CONFIG
| **Default Value** | `'oarepo_vocabularies.ui.resources.config:InvenioVocabulariesUIResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oarepo-vocabulary-type-resource)=
### OAREPO_VOCABULARY_TYPE_RESOURCE
| **OARepo Default Value** | `VocabularyTypeResource` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L40) |

---

(oarepo-vocabulary-type-resource-config)=
### OAREPO_VOCABULARY_TYPE_RESOURCE_CONFIG
| **OARepo Default Value** | `VocabularyTypeResourceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L41) |

---

(oarepo-vocabulary-type-service)=
### OAREPO_VOCABULARY_TYPE_SERVICE
| **OARepo Default Value** | `VocabularyTypeService` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L37) |

---

(oarepo-vocabulary-type-service-config)=
### OAREPO_VOCABULARY_TYPE_SERVICE_CONFIG
| **OARepo Default Value** | `VocabularyTypeServiceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L38) |

---

(oauth2server-allowed-grant-types)=
### OAUTH2SERVER_ALLOWED_GRANT_TYPES
| **Invenio RDM Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L27) |

```
{'refresh_token', 'authorization_code', 'client_credentials'}
```

---

(oauth2server-allowed-response-types)=
### OAUTH2SERVER_ALLOWED_RESPONSE_TYPES
| **Invenio RDM Default Value** | `<set>` |
|--------------|-----------|
| **Type** | set |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L40) |

```
{'token', 'code'}
```

---

(oauth2server-allowed-urlencode-characters)=
### OAUTH2SERVER_ALLOWED_URLENCODE_CHARACTERS

```{eval-rst}
A string of special characters that should be valid inside a query string.

.. seealso::

    See :py:func:`monkeypatch_oauthlib_urlencode_chars
    <invenio_oauth2server.ext.InvenioOAuth2ServerREST.monkeypatch_oauthlib_urlencode_chars>`
    for a full explanation.
```

| **Invenio RDM Default Value** | `'=&;:%+~,*@!()/?'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L52) |

---

(oauth2server-base-template)=
### OAUTH2SERVER_BASE_TEMPLATE
| **Default Value** | `'invenio_oauth2server/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oauth2server-client-id-salt-len)=
### OAUTH2SERVER_CLIENT_ID_SALT_LEN

```{eval-rst}
Length of client id.
```

| **Invenio RDM Default Value** | `40` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L18) |

---

(oauth2server-client-secret-salt-len)=
### OAUTH2SERVER_CLIENT_SECRET_SALT_LEN

```{eval-rst}
Length of the client secret.
```

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L21) |

---

(oauth2server-cover-template)=
### OAUTH2SERVER_COVER_TEMPLATE
| **Default Value** | `'invenio_oauth2server/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oauth2server-jwt-auth-header)=
### OAUTH2SERVER_JWT_AUTH_HEADER

```{eval-rst}
Header for the JWT.

.. note::

    Authorization: Bearer xxx
```

| **Invenio RDM Default Value** | `'Authorization'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L62) |

---

(oauth2server-jwt-auth-header-type)=
### OAUTH2SERVER_JWT_AUTH_HEADER_TYPE

```{eval-rst}
Header Authorization type.

.. note::

    By default the authorization type is ``Bearer`` as recommented by
    `JWT  <https://jwt.io>`_
```

| **Invenio RDM Default Value** | `'Bearer'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L70) |

---

(oauth2server-jwt-verification-factory)=
### OAUTH2SERVER_JWT_VERIFICATION_FACTORY

```{eval-rst}
Import path of factory used to verify JWT.

The ``request.headers`` should be passed as parameter.
```

| **Invenio RDM Default Value** | `'invenio_oauth2server.utils:jwt_verify_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L79) |

---

(oauth2server-settings-template)=
### OAUTH2SERVER_SETTINGS_TEMPLATE
| **Default Value** | `'invenio_oauth2server/settings/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oauth2server-token-personal-salt-len)=
### OAUTH2SERVER_TOKEN_PERSONAL_SALT_LEN

```{eval-rst}
Length of the personal access token.
```

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L24) |

---

(oauth2-cache-type)=
### OAUTH2_CACHE_TYPE

```{eval-rst}
Type of cache to use for storing the temporary grant token.
```

| **Invenio RDM Default Value** | `'redis'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L12) |

---

(oauth2-provider-error-endpoint)=
### OAUTH2_PROVIDER_ERROR_ENDPOINT

```{eval-rst}
Error view endpoint.
```

| **Invenio RDM Default Value** | `'invenio_oauth2server.errors'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauth2server](https://github.com/inveniosoftware/invenio-oauth2server/blob/master/invenio_oauth2server/config.py#L15) |

---

(oauthclient-auto-redirect-to-external-login)=
### ***OAUTHCLIENT_AUTO_REDIRECT_TO_EXTERNAL_LOGIN**

```{eval-rst}
Redirect to the only external login service under specific conditions.

If this option is enabled and there is exactly one external authentication
service enabled (i.e. one OAuthClient remote app is configured, and local
login is disabled), the login view function will automatically redirect to
that external authentication service.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L352) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(oauthclient-base-template)=
### OAUTHCLIENT_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oauthclient-cover-template)=
### OAUTHCLIENT_COVER_TEMPLATE
| **Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oauthclient-login-user-template-parent)=
### OAUTHCLIENT_LOGIN_USER_TEMPLATE_PARENT
| **Default Value** | `'invenio_accounts/login_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oauthclient-remote-apps)=
### ***OAUTHCLIENT_REMOTE_APPS**

```{eval-rst}
Configuration of remote applications.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L325) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters`, {py:func}`~oarepo_config.configure_einfra_oidc` |

```
{}
```

---

(oauthclient-rest-default-error-redirect-url)=
### OAUTHCLIENT_REST_DEFAULT_ERROR_REDIRECT_URL

```{eval-rst}
Configuration of default error redirect URL.
```

| **Invenio RDM Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L346) |

---

(oauthclient-rest-default-response-handler)=
### OAUTHCLIENT_REST_DEFAULT_RESPONSE_HANDLER

```{eval-rst}
Default REST response handler.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L349) |

---

(oauthclient-rest-remote-apps)=
### OAUTHCLIENT_REST_REMOTE_APPS

```{eval-rst}
Configuration of remote rest applications.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L343) |

```
{}
```

---

(oauthclient-session-key-prefix)=
### OAUTHCLIENT_SESSION_KEY_PREFIX

```{eval-rst}
Session key prefix used when storing the access token for a remote app.
```

| **Invenio RDM Default Value** | `'oauth_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L328) |

---

(oauthclient-settings-template)=
### OAUTHCLIENT_SETTINGS_TEMPLATE
| **Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(oauthclient-signup-form)=
### OAUTHCLIENT_SIGNUP_FORM

```{eval-rst}
Function called to render the sign up form after authorization succeeded.
```

| **Invenio RDM Default Value** | `_create_registrationform` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L337) |

---

(oauthclient-signup-template)=
### OAUTHCLIENT_SIGNUP_TEMPLATE

```{eval-rst}
Template for the signup page.
```

| **Invenio RDM Default Value** | `'invenio_oauthclient/signup.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L340) |

---

(oauthclient-sitename)=
### OAUTHCLIENT_SITENAME
| **Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Source** | unknown |

---

(oauthclient-state-enabled)=
### OAUTHCLIENT_STATE_ENABLED

```{eval-rst}
Internal variable used to disable state validation during tests.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L334) |

---

(oauthclient-state-expires)=
### OAUTHCLIENT_STATE_EXPIRES

```{eval-rst}
Number of seconds after which the state token expires.
```

| **Invenio RDM Default Value** | `300` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L331) |

---

(oauthclient-token-expires-leeway)=
### OAUTHCLIENT_TOKEN_EXPIRES_LEEWAY

```{eval-rst}
The number of seconds before the actual expiration of an access token from which it is considered expired.

This ensures that it won't cause issues if some time passes between the check for whether the token is expired and any requests that the token is then used in.
```

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-oauthclient](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/config.py#L361) |

---

(orcid-public-dump-s3-bucket-name)=
### ORCID_PUBLIC_DUMP_S3_BUCKET_NAME
| **OARepo Default Value** | `'v3.0-summaries'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L19) |

---

(pages-allowed-extra-html-attrs)=
### PAGES_ALLOWED_EXTRA_HTML_ATTRS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L61) |

```
{'button': ['type', 'name', 'value', 'disabled', 'onclick'],
 'img': ['src', 'alt', 'title', 'width', 'height', 'loading']}
```

---

(pages-allowed-extra-html-tags)=
### PAGES_ALLOWED_EXTRA_HTML_TAGS

```{eval-rst}
Extend allowed HTML tags list for static pages content.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L58) |

```
['img', 'button']
```

---

(pages-base-template)=
### PAGES_BASE_TEMPLATE
| **Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(pages-default-template)=
### PAGES_DEFAULT_TEMPLATE

```{eval-rst}
Default template to render.
```

| **Invenio RDM Default Value** | `'invenio_pages/default.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1223); [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L14) |

---

(pages-facets)=
### PAGES_FACETS

```{eval-rst}
Available facets defined for this module.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L54) |

```
{}
```

---

(pages-search)=
### PAGES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L28) |

```
{'facets': [], 'sort': ['url', 'title', 'created', 'updated']}
```

---

(pages-sort-options)=
### PAGES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L34) |

```
{'created': {'fields': ['created'], 'title': l'Created'},
 'title': {'fields': ['title'], 'title': l'Title'},
 'updated': {'fields': ['updated'], 'title': l'Updated'},
 'url': {'fields': ['url'], 'title': l'URL'}}
```

---

(pages-templates)=
### PAGES_TEMPLATES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1226); [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L17) |

```
[('invenio_pages/default.html', 'Default'),
 ('invenio_pages/dynamic.html', 'Default dynamic')]
```

---

(pages-whitelist-config-keys)=
### PAGES_WHITELIST_CONFIG_KEYS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-pages](https://github.com/inveniosoftware/invenio-pages/blob/master/invenio_pages/config.py#L23) |

```
['THEME_SITENAME']
```

---

(permanent-session-lifetime)=
### PERMANENT_SESSION_LIFETIME
| **Default Value** | `datetime.timedelta(days=31)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | unknown |

---

(pidstore-app-logger-handlers)=
### PIDSTORE_APP_LOGGER_HANDLERS
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(pidstore-datacite-doi-prefix)=
### PIDSTORE_DATACITE_DOI_PREFIX

```{eval-rst}
Provide a DOI prefix here.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L19) |

---

(pidstore-object-endpoints)=
### PIDSTORE_OBJECT_ENDPOINTS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{'rec': 'recordmetadata.details_view'}
```

---

(pidstore-recid-field)=
### PIDSTORE_RECID_FIELD

```{eval-rst}
Default record id field inside the json data.

This name will be used by the fetcher, to retrieve the record ID value from the
JSON, and by the minter, to store it inside the JSON.
```

| **Invenio RDM Default Value** | `'control_number'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L11) |

---

(pidstore-recordid-options)=
### PIDSTORE_RECORDID_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-pidstore](https://github.com/inveniosoftware/invenio-pidstore/blob/master/invenio_pidstore/config.py#L22) |

```
{'checksum': True, 'length': 10, 'split_every': 5}
```

---

(preferred-url-scheme)=
### PREFERRED_URL_SCHEME
| **Default Value** | `'http'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(previewable-zip-previewer-native-extensions)=
### PREVIEWABLE_ZIP_PREVIEWER_NATIVE_EXTENSIONS

```{eval-rst}
Extensions for previewable zip.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1176) |

```
['zip']
```

---

(previewer-abstract-template)=
### PREVIEWER_ABSTRACT_TEMPLATE

```{eval-rst}
Parent template used by the available previewers.
```

| **Invenio RDM Default Value** | `'invenio_previewer/abstract_previewer.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L72); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1199) |

---

(previewer-base-css-bundles)=
### PREVIEWER_BASE_CSS_BUNDLES

```{eval-rst}
Basic bundle which includes Font-Awesome/Bootstrap.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L75) |

```
['previewer_theme.css']
```

---

(previewer-base-js-bundles)=
### PREVIEWER_BASE_JS_BUNDLES

```{eval-rst}
Basic bundle which includes Bootstrap/jQuery.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L78) |

```
['previewer_theme.js']
```

---

(previewer-base-template)=
### PREVIEWER_BASE_TEMPLATE
| **Default Value** | `'invenio_previewer/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(previewer-chardet-bytes)=
### PREVIEWER_CHARDET_BYTES

```{eval-rst}
Number of bytes to read for character encoding detection by `cchardet`.
```

| **Invenio RDM Default Value** | `1024` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L17) |

---

(previewer-chardet-confidence)=
### PREVIEWER_CHARDET_CONFIDENCE

```{eval-rst}
Confidence threshold for character encoding detection by `cchardet`.
```

| **Invenio RDM Default Value** | `0.9` |
|--------------|-----------|
| **Type** | float |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L20) |

---

(previewer-container-item-preference)=
### PREVIEWER_CONTAINER_ITEM_PREFERENCE
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1202) |

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

(previewer-csv-max-bytes)=
### PREVIEWER_CSV_MAX_BYTES

```{eval-rst}
Maximum file size in bytes for CSV files.
```

| **Invenio RDM Default Value** | `104857600` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L32) |

---

(previewer-csv-sniffer-allowed-delimiters)=
### PREVIEWER_CSV_SNIFFER_ALLOWED_DELIMITERS

```{eval-rst}
Allowed delimiter characters passed to the ``csv.Sniffer.sniff`` method.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L14) |

---

(previewer-csv-validation-bytes)=
### PREVIEWER_CSV_VALIDATION_BYTES

```{eval-rst}
Number of bytes read by CSV previewer to validate the file.
```

| **Invenio RDM Default Value** | `1024` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L11) |

---

(previewer-max-file-size-bytes)=
### PREVIEWER_MAX_FILE_SIZE_BYTES

```{eval-rst}
Maximum file size in bytes for JSON/XML files.
```

| **Invenio RDM Default Value** | `1048576` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L23) |

---

(previewer-max-image-size-bytes)=
### PREVIEWER_MAX_IMAGE_SIZE_BYTES

```{eval-rst}
Maximum file size in bytes for image files.
```

| **Invenio RDM Default Value** | `524288.0` |
|--------------|-----------|
| **Type** | float |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L26) |

---

(previewer-pdf-js-document-init-params)=
### PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS

```{eval-rst}
Additional DocumentInitParameters passed to pdfjsLib.getDocument().

See https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib.html for the full
list of available options.

Example (disable range requests, streaming, and auto-fetching)::

    PREVIEWER_PDF_JS_DOCUMENT_INIT_PARAMS = {
        "disableStream": True,
        "disableRange": True,
        "disableAutoFetch": True,
    }
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L41) |

---

(previewer-pdf-js-enable-scripting)=
### PREVIEWER_PDF_JS_ENABLE_SCRIPTING

```{eval-rst}
Enable JavaScript execution in PDF files (disabled by default for security).
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L38) |

---

(previewer-preference)=
### PREVIEWER_PREFERENCE
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L56); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1183) |

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

(previewer-record-file-facotry)=
### PREVIEWER_RECORD_FILE_FACOTRY

```{eval-rst}
Factory for extracting files from records.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L81) |

---

(previewer-txt-max-bytes)=
### PREVIEWER_TXT_MAX_BYTES

```{eval-rst}
Maximum number of .txt file bytes to preview before truncated.
```

| **Invenio RDM Default Value** | `1048576` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L29) |

---

(previewer-web-archive-range-requests)=
### PREVIEWER_WEB_ARCHIVE_RANGE_REQUESTS

```{eval-rst}
Whether the file server supports range requests or not.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L84) |

---

(previewer-zip-max-files)=
### PREVIEWER_ZIP_MAX_FILES

```{eval-rst}
Max number of files showed in the ZIP previewer.
```

| **Invenio RDM Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-previewer](https://github.com/inveniosoftware/invenio-previewer/blob/master/invenio_previewer/config.py#L35) |

---

(propagate-exceptions)=
### PROPAGATE_EXCEPTIONS
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(provide-automatic-options)=
### PROVIDE_AUTOMATIC_OPTIONS
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(publish-request-types)=
### PUBLISH_REQUEST_TYPES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['publish_draft', 'publish_new_version']
```

---

(queues-broker-url)=
### QUEUES_BROKER_URL

```{eval-rst}
Broker URL for queues.

If the variable is not configured it falls back to the default ``BROKER_URL``
of our application. For more information about how to define your broker here:
https://kombu.readthedocs.io/en/latest/reference/kombu.connection.html#connection
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L13) |

---

(queues-connection-pool)=
### QUEUES_CONNECTION_POOL

```{eval-rst}
Default queues connection pool.
```

| **Invenio RDM Default Value** | `get_connection_pool` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L21) |

---

(queues-definitions)=
### QUEUES_DEFINITIONS

```{eval-rst}
Static queue definitions.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-queues](https://github.com/inveniosoftware/invenio-queues/blob/master/invenio_queues/config.py#L24) |

```
[]
```

---

(ratelimit-application)=
### RATELIMIT_APPLICATION

```{eval-rst}
Global rate limit.
```

| **Invenio RDM Default Value** | `set_rate_limit` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L24) |

---

(ratelimit-authenticated-user)=
### ***RATELIMIT_AUTHENTICATED_USER**

```{eval-rst}
Rate limit for logged in users.
```

| **Invenio RDM Default Value** | `'5000 per hour;100 per minute'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L91); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L239) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(ratelimit-enabled)=
### RATELIMIT_ENABLED
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(ratelimit-guest-user)=
### ***RATELIMIT_GUEST_USER**

```{eval-rst}
Rate limit for non logged in users.
```

| **Invenio RDM Default Value** | `'1000 per hour;60 per minute'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L94); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L241) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(ratelimit-headers-enabled)=
### RATELIMIT_HEADERS_ENABLED

```{eval-rst}
Enable rate limit headers. (Default: ``True``)
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L37) |

---

(ratelimit-key-func)=
### RATELIMIT_KEY_FUNC

```{eval-rst}
Define custom key function.

This config is not part of Flask-Limiter.

This function is used to generate a unique key for each visitor to track
the number of performed requests. If not defined, the default ``key_func``
will be used, which will create the key by concatenating the user agent and
the IP address of the user.

For more information you can also see `here
<https://flask-limiter.readthedocs.io/en/stable/#rate-limit-domain>`_
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L54) |

---

(ratelimit-per-endpoint)=
### RATELIMIT_PER_ENDPOINT
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L68) |

```
{'security.forgot_password': '10 per minute',
 'security.login': '10 per minute',
 'security.register': '10 per minute',
 'security.reset_password': '10 per minute'}
```

---

(ratelimit-storage-uri)=
### RATELIMIT_STORAGE_URI

```{eval-rst}
Storage backend to store rate-limiting information.

    Memory is used by default if no value is provided.
    For more information regarding the mentioned above configuration values and
    their available options you can see the `Flask-Limiter configuration
    <https://flask-limiter.readthedocs.io/en/stable/#configuration>`_.

.. note::

   Provide your Redis URL if you are rate limiting a multithreaded application.
```

| **Invenio RDM Default Value** | `'memory://'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L40); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L235) |

---

(ratelimit-strategy)=
### RATELIMIT_STRATEGY

```{eval-rst}
The rate limiting strategy to use.

The strategy used here is the most consistant but also expensive one.
If you are experiencing performance issues due to the increased Redis
traffic, you can replace it with another one from the following
`Flask-Limiter strategies
<https://flask-limiter.readthedocs.io/en/stable/#ratelimit-strategy>`_.
```

| **Invenio RDM Default Value** | `'moving-window'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L27) |

---

(rdm-allow-external-doi-versioning)=
### RDM_ALLOW_EXTERNAL_DOI_VERSIONING

```{eval-rst}
Allow records with external DOIs to be versioned.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L657) |

---

(rdm-allow-metadata-only-records)=
### RDM_ALLOW_METADATA_ONLY_RECORDS

```{eval-rst}
Allow users to publish metadata-only records.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L164) |

---

(rdm-allow-owners-remove-community-from-record)=
### RDM_ALLOW_OWNERS_REMOVE_COMMUNITY_FROM_RECORD

```{eval-rst}
Allow record owners to remove communities from records.

When set to False, only community curators, managers, and owners can remove
communities from records. This applies to published records.
Record owners will still be able to add communities, but removal is restricted
to community curators, managers, and owners.

Default: True (backwards compatible - owners can remove communities)
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L324) |

---

(rdm-allow-restricted-records)=
### RDM_ALLOW_RESTRICTED_RECORDS

```{eval-rst}
Allow users to set restricted/private records.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L173) |

---

(rdm-archive-download-enabled)=
### RDM_ARCHIVE_DOWNLOAD_ENABLED

```{eval-rst}
Flag to enable/disable the all-in-one download endpoint.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L64) |

---

(rdm-citation-styles)=
### RDM_CITATION_STYLES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1124) |

```
[('apa', 'APA'),
 ('harvard-cite-them-right', 'Harvard'),
 ('modern-language-association', 'MLA'),
 ('vancouver', 'Vancouver'),
 ('chicago-fullnote-bibliography', 'Chicago'),
 ('ieee', 'IEEE'),
 ('iso690-author-date-cs', l'ČSN ISO 690')]
```

---

(rdm-citation-styles-default)=
### RDM_CITATION_STYLES_DEFAULT

```{eval-rst}
Default citation style
```

| **Invenio RDM Default Value** | `'iso690-author-date-cs'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1134) |

---

(rdm-communities-routes)=
### RDM_COMMUNITIES_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1102) |

```
{'community-browse': '/communities/<pid_value>/browse',
 'community-collection': '/communities/<pid_value>/collections/<tree_slug>/<collection_slug>',
 'community-detail': '/communities/<pid_value>/records',
 'community-home': '/communities/<pid_value>/',
 'community-static-page': '/communities/<pid_value>/pages/<path:page_slug>'}
```

---

(rdm-community-content-moderation-handlers)=
### RDM_COMMUNITY_CONTENT_MODERATION_HANDLERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L863) |

```
[<invenio_rdm_records.services.communities.moderation.UserModerationHandler object at 0x1111bbb60>]
```

---

(rdm-community-inclusion-request-cls)=
### RDM_COMMUNITY_INCLUSION_REQUEST_CLS

```{eval-rst}
Request type for record inclusion requests.
```

| **Invenio RDM Default Value** | `CommunityInclusion` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L322) |

---

(rdm-community-required-to-publish)=
### RDM_COMMUNITY_REQUIRED_TO_PUBLISH

```{eval-rst}
Enforces at least one community per record.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L320) |

---

(rdm-community-submission-request-cls)=
### RDM_COMMUNITY_SUBMISSION_REQUEST_CLS

```{eval-rst}
Request type for community submission requests.
```

| **OARepo Default Value** | `CommunitySubmission` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L155); [oarepo-communities](https://github.com/oarepo/oarepo-communities/blob/master/oarepo_communities/initial_config.py#L18) |

---

(rdm-content-moderation-handlers)=
### RDM_CONTENT_MODERATION_HANDLERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L858) |

```
[<invenio_rdm_records.services.components.verified.UserModerationHandler object at 0x1111bba10>]
```

---

(rdm-custom-fields)=
### RDM_CUSTOM_FIELDS

```{eval-rst}
Records custom fields definition.

.. code-block:: python

    [<custom-field-class-type>, <custom-field-class-type>, ...]

For example:

.. code-block:: python

    [TextCF(name="experiment"), ...]
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L775) |

```
[]
```

---

(rdm-custom-fields-ui)=
### RDM_CUSTOM_FIELDS_UI

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L789) |

```
[]
```

---

(rdm-datacite-dump-openaire-access-rights)=
### RDM_DATACITE_DUMP_OPENAIRE_ACCESS_RIGHTS

```{eval-rst}
Flag to control dumping DataCite OpenAIRE access rights.

See https://guidelines.openaire.eu/en/latest/data/field_rights.html for further
information on how the OpenAIRE Guidelines expect access rights to be exposed
via the DataCite schema.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L896) |

---

(rdm-datacite-funder-identifiers-priority)=
### RDM_DATACITE_FUNDER_IDENTIFIERS_PRIORITY

```{eval-rst}
Priority of funder identifiers types to be used for DataCite serialization.
```

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L893) |

```
('ror', 'doi', 'grid', 'isni', 'gnd')
```

---

(rdm-default-files-enabled)=
### RDM_DEFAULT_FILES_ENABLED

```{eval-rst}
Deposit page files enabled value on new records.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L167) |

---

(rdm-detail-side-bar-manage-attributes-extension-template)=
### RDM_DETAIL_SIDE_BAR_MANAGE_ATTRIBUTES_EXTENSION_TEMPLATE

```{eval-rst}
Side bar manage attributes extension template.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1550) |

---

(rdm-facets)=
### RDM_FACETS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L338); [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L74) |

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

(rdm-files-default-max-additional-quota-size)=
### RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE

```{eval-rst}
Default additional quota size for a bucket in bytes for files.
```

| **Invenio RDM Default Value** | `0` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L890) |

---

(rdm-files-default-max-file-size)=
### RDM_FILES_DEFAULT_MAX_FILE_SIZE

```{eval-rst}
Default maximum file size for a bucket in bytes for files.
```

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L887) |

---

(rdm-files-default-quota-size)=
### RDM_FILES_DEFAULT_QUOTA_SIZE

```{eval-rst}
Default size for a bucket in bytes for files.
```

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L884) |

---

(rdm-file-modification-period)=
### RDM_FILE_MODIFICATION_PERIOD

```{eval-rst}
Time period after creation during which modified files can be published.
30 + 30 denotes grace period + extra days for file modification. This is checked
during publish to block people from publishing after this period given the bucket stays open.
```

| **Invenio RDM Default Value** | `datetime.timedelta(days=45)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L273) |

---

(rdm-file-modification-policy)=
### RDM_FILE_MODIFICATION_POLICY

```{eval-rst}
Policy class which evaluates whether published files can be modified by a user.
```

| **Invenio RDM Default Value** | `FileModificationPolicyEvaluator` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L238) |

---

(rdm-iiif-manifest-formats)=
### RDM_IIIF_MANIFEST_FORMATS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L904) |

```
['gif', 'jp2', 'jpeg', 'jpg', 'png', 'tif', 'tiff']
```

---

(rdm-immediate-file-modification-enabled)=
### RDM_IMMEDIATE_FILE_MODIFICATION_ENABLED

```{eval-rst}
Allow editing of published files (by default by admins only).
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L241) |

---

(rdm-immediate-file-modification-policies)=
### RDM_IMMEDIATE_FILE_MODIFICATION_POLICIES

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L244) |

```
[<invenio_rdm_records.services.request_policies.FileModificationAdminPolicy object at 0x1111baa50>]
```

---

(rdm-immediate-quota-increase-enabled)=
### RDM_IMMEDIATE_QUOTA_INCREASE_ENABLED

```{eval-rst}
Allow increasing of draft's quota from a user's additional quota.

RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE controls how much each user has
available across their records
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L285) |

---

(rdm-immediate-quota-increase-policies)=
### RDM_IMMEDIATE_QUOTA_INCREASE_POLICIES

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L291) |

```
[]
```

---

(rdm-immediate-record-deletion-checklist)=
### RDM_IMMEDIATE_RECORD_DELETION_CHECKLIST

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L198) |

```
[]
```

---

(rdm-immediate-record-deletion-enabled)=
### RDM_IMMEDIATE_RECORD_DELETION_ENABLED

```{eval-rst}
Allow users to immediately delete records.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L182) |

---

(rdm-immediate-record-deletion-policies)=
### RDM_IMMEDIATE_RECORD_DELETION_POLICIES

```{eval-rst}
List of policies for immediate record deletion.

Policies are executed in order and the first one to return True is used
as the policy for the record. As such, policies should be specified from most
to least specific.

To update a policy, create a duplicate of it and add a check on creation date to
both. When your policy comes into effect on a date in the future it will be used,
and this is the date which you will use to check whether the new or old policy
will apply.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L185) |

```
[<invenio_rdm_records.services.request_policies.GracePeriodPolicy object at 0x1111ba7b0>]
```

---

(rdm-lock-edit-published-files)=
### RDM_LOCK_EDIT_PUBLISHED_FILES

```{eval-rst}
Lock editing already published files (enforce record versioning).

   signature to implement:
   def lock_edit_published_files(service, identity, record=None, draft=None):
```

| **Invenio RDM Default Value** | `lock_edit_published_files` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L851) |

---

(rdm-media-files-default-max-file-size)=
### RDM_MEDIA_FILES_DEFAULT_MAX_FILE_SIZE

```{eval-rst}
Default maximum file size for a bucket in bytes for media files.
```

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L881) |

---

(rdm-media-files-default-quota-size)=
### RDM_MEDIA_FILES_DEFAULT_QUOTA_SIZE

```{eval-rst}
Default size for a bucket in bytes for media files.
```

| **Invenio RDM Default Value** | `10000000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L878) |

---

(rdm-namespaces)=
### RDM_NAMESPACES

```{eval-rst}
Custom fields namespaces.

.. code-block:: python

    {<namespace>: <uri>, ...}

For example:

.. code-block:: python

    {
        "cern": "https://cern.ch/terms",
        "dwc": "http://rs.tdwg.org/dwc/terms/"
    }
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L757) |

```
{}
```

---

(rdm-new-record-version-review-policy)=
### RDM_NEW_RECORD_VERSION_REVIEW_POLICY

```{eval-rst}
Policy for when to require a community review for new record versions.
```

| **Invenio RDM Default Value** | `NewRecordVersionReviewPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L158) |

---

(rdm-oai-pmh-facets)=
### RDM_OAI_PMH_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L530) |

```
{}
```

---

(rdm-oai-pmh-search)=
### RDM_OAI_PMH_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L552) |

```
{'facets': [], 'sort': ['name', 'spec', 'created', 'updated']}
```

---

(rdm-oai-pmh-sort-options)=
### RDM_OAI_PMH_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L532) |

```
{'created': {'fields': ['created'], 'title': l'Created'},
 'name': {'fields': ['name'], 'title': l'Set name'},
 'spec': {'fields': ['spec'], 'title': l'Set spec'},
 'updated': {'fields': ['updated'], 'title': l'Updated'}}
```

---

(rdm-optional-doi-validator)=
### RDM_OPTIONAL_DOI_VALIDATOR

```{eval-rst}
Optional DOI transitions validate method.

Check the signature of validate_optional_doi for more information.
```

| **Invenio RDM Default Value** | `validate_optional_doi` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L661) |

---

(rdm-parent-persistent-identifiers)=
### RDM_PARENT_PERSISTENT_IDENTIFIERS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L644); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L54) |

```
{}
```

---

(rdm-parent-persistent-identifier-providers)=
### RDM_PARENT_PERSISTENT_IDENTIFIER_PROVIDERS
| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L633); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L44) |

```
[<invenio_rdm_records.services.pids.providers.datacite.DataCitePIDProvider object at 0x1111e8cd0>]
```

---

(rdm-permission-policy)=
### RDM_PERMISSION_POLICY

```{eval-rst}
Override the default record permission policy.
```

| **Invenio RDM Default Value** | `RDMRecordPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L144) |

---

(rdm-persistent-identifiers)=
### RDM_PERSISTENT_IDENTIFIERS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L604); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L32) |

```
{'oai': {'is_enabled': <bound method OAIPIDProvider.is_enabled of <class 'invenio_rdm_records.services.pids.providers.oai.OAIPIDProvider'>>,
         'label': l'OAI',
         'providers': ['oai'],
         'required': True}}
```

---

(rdm-persistent-identifier-providers)=
### RDM_PERSISTENT_IDENTIFIER_PROVIDERS
| **OARepo Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L561); [oarepo-doi](https://github.com/oarepo/oarepo-doi/blob/master/oarepo_doi/config.py#L23) |

```
[<invenio_rdm_records.services.pids.providers.datacite.DataCitePIDProvider object at 0x1111baf90>,
 <invenio_rdm_records.services.pids.providers.crossref.CrossrefPIDProvider object at 0x1111bb230>,
 <invenio_rdm_records.services.pids.providers.external.ExternalPIDProvider object at 0x1111bb770>,
 <invenio_rdm_records.services.pids.providers.oai.OAIPIDProvider object at 0x1111bb8c0>,
 <invenio_rdm_records.services.pids.providers.oai.OAIPIDProvider object at 0x112be6fd0>,
 <invenio_rdm_records.services.pids.providers.oai.OAIPIDProvider object at 0x112be6fd0>]
```

---

(rdm-quota-increase-policy)=
### RDM_QUOTA_INCREASE_POLICY

```{eval-rst}
Policy class which evaluates whether the quota for drafts can be increased.
```

| **Invenio RDM Default Value** | `QuotaIncreasePolicyEvaluator` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L282) |

---

(rdm-records-access-service-class)=
### RDM_RECORDS_ACCESS_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_rdm.services.delegating.DelegatingRecordAccessService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L36) |

---

(rdm-records-allow-restriction-after-grace-period)=
### RDM_RECORDS_ALLOW_RESTRICTION_AFTER_GRACE_PERIOD

```{eval-rst}
Whether record access restriction is allowed after the grace period or not.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L950) |

---

(rdm-records-community-records-config-class)=
### RDM_RECORDS_COMMUNITY_RECORDS_CONFIG_CLASS

```{eval-rst}
Community records service config that uses the multiplexed search options.
```

| **OARepo Default Value** | `'oarepo_rdm.services.config:OARepoCommunityRecordsConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L40) |

---

(rdm-records-community-records-service-class)=
### RDM_RECORDS_COMMUNITY_RECORDS_SERVICE_CLASS

```{eval-rst}
Community records service that multiplexes search across per-model services.
```

| **OARepo Default Value** | `'oarepo_rdm.services.service:OARepoCommunityRecordsService'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L43); [oarepo-communities](https://github.com/oarepo/oarepo-communities/blob/master/oarepo_communities/initial_config.py#L17) |

---

(rdm-records-container-extensions)=
### RDM_RECORDS_CONTAINER_EXTENSIONS

```{eval-rst}
List of file extensions for container files.
Experimental, this config can later be removed.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L956) |

```
['.zip']
```

---

(rdm-records-error-handlers)=
### RDM_RECORDS_ERROR_HANDLERS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L56) |

```
{<class 'oarepo_rdm.errors.UndefinedModelError'>: <function create_error_handler.<locals>.error_handler at 0x111fae8d0>,
 <class 'invenio_rdm_records.services.errors.RecordDeletedException'>: <function create_error_handler.<locals>.error_handler at 0x110a266c0>,
 <class 'invenio_rdm_records.services.errors.DeletionStatusException'>: <function create_error_handler.<locals>.error_handler at 0x110a26770>,
 <class 'invenio_rdm_records.services.errors.ReviewNotFoundError'>: <function create_error_handler.<locals>.error_handler at 0x110a273d0>,
 <class 'invenio_rdm_records.services.errors.ReviewStateError'>: <function create_error_handler.<locals>.error_handler at 0x110a27060>,
 <class 'invenio_rdm_records.services.errors.ReviewExistsError'>: <function create_error_handler.<locals>.error_handler at 0x110a27110>,
 <class 'invenio_rdm_records.services.errors.InvalidAccessRestrictions'>: <function create_error_handler.<locals>.error_handler at 0x110a26e50>,
 <class 'invenio_rdm_records.services.errors.ValidationErrorWithMessageAsList'>: <function create_error_handler.<locals>.error_handler at 0x110a26ae0>,
 <class 'invenio_rdm_records.services.errors.AccessRequestExistsError'>: <function create_error_handler.<locals>.error_handler at 0x110a26b90>,
 <class 'invenio_rdm_records.services.errors.RecordSubmissionClosedCommunityError'>: <function create_error_handler.<locals>.error_handler at 0x110a26400>,
 <class 'invenio_rdm_records.services.errors.CommunityRequiredError'>: <function create_error_handler.<locals>.error_handler at 0x110a26820>,
 <class 'citeproc_styles.errors.StyleNotFoundError'>: <function create_error_handler.<locals>.error_handler at 0x110a278a0>,
 <class 'invenio_rdm_records.resources.deserializers.errors.DeserializerError'>: <function create_error_handler.<locals>.error_handler at 0x110a3cb40>,
 <class 'invenio_records.systemfields.relations.errors.InvalidRelationValue'>: <function create_error_handler.<locals>.error_handler at 0x110a26da0>,
 <class 'invenio_records.systemfields.relations.errors.InvalidCheckValue'>: <function create_error_handler.<locals>.error_handler at 0x10dae5f30>,
 <class 'invenio_records_resources.services.errors.RecordPermissionDeniedError'>: <function create_error_handler.<locals>.error_handler at 0x10dae54e0>,
 <class 'invenio_records_resources.services.errors.PermissionDeniedError'>: <function create_error_handler.<locals>.error_handler at 0x10dae5430>,
 <class 'invenio_records_resources.services.errors.RevisionIdMismatchError'>: <function create_error_handler.<locals>.error_handler at 0x10dae5220>,
 <class 'invenio_records_resources.services.errors.QuerystringValidationError'>: <function create_error_handler.<locals>.error_handler at 0x10dae5380>,
 <class 'invenio_records_resources.services.errors.ValidationErrorGroup'>: <function create_error_handler.<locals>.error_handler at 0x10dae50c0>,
 <class 'invenio_records_resources.services.errors.ArchiveDownloadTooLargeException'>: <function create_error_handler.<locals>.error_handler at 0x10dae5d20>,
 <class 'invenio_records_resources.services.errors.FacetNotFoundError'>: <function create_error_handler.<locals>.error_handler at 0x10dae5a60>,
 <class 'invenio_records_resources.services.errors.FileKeyNotFoundError'>: <function create_error_handler.<locals>.error_handler at 0x10dae5bc0>,
 <class 'invenio_records_resources.services.errors.FailedFileUploadException'>: <function create_error_handler.<locals>.error_handler at 0x10dae6140>,
 <class 'invenio_records_resources.services.errors.FilesCountExceededException'>: <function create_error_handler.<locals>.error_handler at 0x10dae61f0>,
 <class 'invenio_pidstore.errors.PIDAlreadyExists'>: <function create_error_handler.<locals>.error_handler at 0x10dae5640>,
 <class 'invenio_pidstore.errors.PIDDoesNotExistError'>: <function create_error_handler.<locals>.error_handler at 0x10dae56f0>,
 <class 'invenio_pidstore.errors.PIDDeletedError'>: <function create_error_handler.<locals>.error_handler at 0x10dae5590>,
 <class 'invenio_pidstore.errors.PIDUnregistered'>: <function create_error_handler.<locals>.error_handler at 0x10dae57a0>,
 <class 'invenio_pidstore.errors.PIDRedirectedError'>: <function create_pid_redirected_error_handler.<locals>.pid_redirected_error_handler at 0x10dae5850>,
 <class 'marshmallow.exceptions.ValidationError'>: <function create_error_handler.<locals>.error_handler at 0x10dae4f60>,
 <class 'opensearchpy.exceptions.RequestError'>: <function create_error_handler.<locals>.error_handler at 0x10dae6090>,
 <class 'sqlalchemy.exc.NoResultFound'>: <function create_error_handler.<locals>.error_handler at 0x10dae5900>,
 <class 'json.decoder.JSONDecodeError'>: <function create_error_handler.<locals>.error_handler at 0x10dae5dd0>}
```

---

(rdm-records-identifiers-schemes)=
### RDM_RECORDS_IDENTIFIERS_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L86) |

```
{'ads': {'datacite': 'bibcode',
         'label': l'Bibcode',
         'validator': <function is_ads at 0x10b453e20>},
 'ark': {'datacite': 'ARK',
         'label': l'ARK',
         'validator': <function is_ark at 0x10b453ab0>},
 'arxiv': {'datacite': 'arXiv',
           'label': l'arXiv',
           'validator': <function is_arxiv at 0x10b4ac0f0>},
 'crossreffunderid': {'datacite': 'Crossref Funder ID',
                      'label': l'Crossref Funder ID',
                      'validator': <function always_valid at 0x10e7df7f0>},
 'cstr': {'datacite': 'CSTR',
          'label': l'CSTR',
          'validator': <function is_cstr at 0x10b4ad220>},
 'doi': {'datacite': 'DOI',
         'label': l'DOI',
         'validator': <function is_doi at 0x10ae30b40>},
 'ean13': {'datacite': 'EAN13',
           'label': l'EAN13',
           'validator': <function is_ean13 at 0x10b4537f0>},
 'eissn': {'datacite': 'EISSN',
           'label': l'EISSN',
           'validator': <function is_issn at 0x10ae307d0>},
 'grid': {'datacite': 'GRID',
          'label': l'GRID',
          'validator': <function always_valid at 0x10e7df7f0>},
 'handle': {'datacite': 'Handle',
            'label': l'Handle',
            'validator': <function is_handle at 0x10b452fb0>},
 'igsn': {'datacite': 'IGSN',
          'label': l'IGSN',
          'validator': <function always_valid at 0x10e7df7f0>},
 'isbn': {'datacite': 'ISBN',
          'label': l'ISBN',
          'validator': <function is_isbn at 0x10ae305c0>},
 'isni': {'datacite': 'ISNI',
          'label': l'ISNI',
          'validator': <function is_isni at 0x10b453950>},
 'issn': {'datacite': 'ISSN',
          'label': l'ISSN',
          'validator': <function is_issn at 0x10ae307d0>},
 'istc': {'datacite': 'ISTC',
          'label': l'ISTC',
          'validator': <function is_istc at 0x10ae30a90>},
 'lissn': {'datacite': 'LISSN',
           'label': l'LISSN',
           'validator': <function is_issn at 0x10ae307d0>},
 'lsid': {'datacite': 'LSID',
          'label': l'LSID',
          'validator': <function is_lsid at 0x10b453cc0>},
 'other': {'datacite': 'Other',
           'label': l'Other',
           'validator': <function always_valid at 0x10e7df7f0>},
 'pmid': {'datacite': 'PMID',
          'label': l'PMID',
          'validator': <function is_pmid at 0x10b4ac250>},
 'purl': {'datacite': 'PURL',
          'label': l'PURL',
          'validator': <function is_purl at 0x10b453b60>},
 'rrid': {'datacite': 'RRID',
          'label': l'RRID',
          'validator': <function is_rrid at 0x10b4ad2d0>},
 'upc': {'datacite': 'UPC',
         'label': l'UPC',
         'validator': <function always_valid at 0x10e7df7f0>},
 'url': {'datacite': 'URL',
         'label': l'URL',
         'validator': <function is_url at 0x10b453c10>},
 'urn': {'datacite': 'URN',
         'label': l'URN',
         'validator': <function is_urn at 0x10b453d70>},
 'w3id': {'datacite': 'w3id',
          'label': l'W3ID',
          'validator': <function always_valid at 0x10e7df7f0>},
 'wikidata': {'datacite': 'Other',
              'label': l'Wikidata',
              'validator': <function is_wikidata at 0x10b4ad0c0>}}
```

---

(rdm-records-location-schemes)=
### RDM_RECORDS_LOCATION_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L136) |

```
{'geonames': {'label': l'GeoNames',
              'validator': <function always_valid at 0x10e7df7f0>},
 'wikidata': {'label': l'Wikidata', 'validator': <function is_wikidata at 0x10b4ad0c0>}}
```

---

(rdm-records-max-files-count)=
### RDM_RECORDS_MAX_FILES_COUNT

```{eval-rst}
Max amount of files allowed to upload in the deposit form.
```

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L872) |

---

(rdm-records-max-media-files-count)=
### RDM_RECORDS_MAX_MEDIA_FILES_COUNT

```{eval-rst}
Max amount of media files allowed to upload in the deposit form.
```

| **Invenio RDM Default Value** | `100` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L875) |

---

(rdm-records-personorg-schemes)=
### RDM_RECORDS_PERSONORG_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L79) |

```
{'czenasautid': {'label': l'CzenasAutID',
                 'validator': <function <lambda> at 0x1116f0670>},
 'doi': {'datacite': 'DOI',
         'label': l'DOI',
         'validator': <function is_doi at 0x10ae30b40>},
 'gnd': {'datacite': 'GND',
         'label': l'GND',
         'validator': <function is_gnd at 0x10b4ac3b0>},
 'grid': {'label': l'GRID', 'validator': <function <lambda> at 0x1116f0930>},
 'ico': {'label': l'ICO', 'validator': <function <lambda> at 0x1116f07d0>},
 'institutionalid': {'label': l'InstitutionalID',
                     'validator': <function <lambda> at 0x1116f0720>},
 'isni': {'datacite': 'ISNI',
          'label': l'ISNI',
          'validator': <function is_isni at 0x10b453950>},
 'orcid': {'datacite': 'ORCID',
           'label': l'ORCID',
           'validator': <function is_orcid at 0x10b453a00>},
 'researcherid': {'datacite': 'ResearcherID',
                  'label': l'Researcher ID',
                  'validator': <function is_researcher_id at 0x1116f0300>},
 'ror': {'datacite': 'ROR',
         'label': l'ROR',
         'validator': <function is_ror at 0x10b4ace00>},
 'scopusid': {'datacite': 'Scopus Author ID',
              'label': l'Scopus Author ID',
              'validator': <function is_scopus_id at 0x1116f05c0>},
 'url': {'label': l'URL', 'validator': <function <lambda> at 0x1116f0880>},
 'vedidk': {'label': l'vedIDK', 'validator': <function is_vedidk at 0x1116f0460>}}
```

---

(rdm-records-pids-service-class)=
### RDM_RECORDS_PIDS_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_rdm.services.delegating.DelegatingPIDsService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L37) |

---

(rdm-records-related-identifiers-schemes)=
### RDM_RECORDS_RELATED_IDENTIFIERS_SCHEMES

```{eval-rst}
This variable is used to separate related identifiers.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L133) |

```
{'ads': {'datacite': 'bibcode',
         'label': l'Bibcode',
         'validator': <function is_ads at 0x10b453e20>},
 'ark': {'datacite': 'ARK',
         'label': l'ARK',
         'validator': <function is_ark at 0x10b453ab0>},
 'arxiv': {'datacite': 'arXiv',
           'label': l'arXiv',
           'validator': <function is_arxiv at 0x10b4ac0f0>},
 'crossreffunderid': {'datacite': 'Crossref Funder ID',
                      'label': l'Crossref Funder ID',
                      'validator': <function always_valid at 0x10e7df7f0>},
 'cstr': {'datacite': 'CSTR',
          'label': l'CSTR',
          'validator': <function is_cstr at 0x10b4ad220>},
 'doi': {'datacite': 'DOI',
         'label': l'DOI',
         'validator': <function is_doi at 0x10ae30b40>},
 'ean13': {'datacite': 'EAN13',
           'label': l'EAN13',
           'validator': <function is_ean13 at 0x10b4537f0>},
 'eissn': {'datacite': 'EISSN',
           'label': l'EISSN',
           'validator': <function is_issn at 0x10ae307d0>},
 'grid': {'datacite': 'GRID',
          'label': l'GRID',
          'validator': <function always_valid at 0x10e7df7f0>},
 'handle': {'datacite': 'Handle',
            'label': l'Handle',
            'validator': <function is_handle at 0x10b452fb0>},
 'igsn': {'datacite': 'IGSN',
          'label': l'IGSN',
          'validator': <function always_valid at 0x10e7df7f0>},
 'isbn': {'datacite': 'ISBN',
          'label': l'ISBN',
          'validator': <function is_isbn at 0x10ae305c0>},
 'isni': {'datacite': 'ISNI',
          'label': l'ISNI',
          'validator': <function is_isni at 0x10b453950>},
 'issn': {'datacite': 'ISSN',
          'label': l'ISSN',
          'validator': <function is_issn at 0x10ae307d0>},
 'istc': {'datacite': 'ISTC',
          'label': l'ISTC',
          'validator': <function is_istc at 0x10ae30a90>},
 'lissn': {'datacite': 'LISSN',
           'label': l'LISSN',
           'validator': <function is_issn at 0x10ae307d0>},
 'lsid': {'datacite': 'LSID',
          'label': l'LSID',
          'validator': <function is_lsid at 0x10b453cc0>},
 'other': {'datacite': 'Other',
           'label': l'Other',
           'validator': <function always_valid at 0x10e7df7f0>},
 'pmid': {'datacite': 'PMID',
          'label': l'PMID',
          'validator': <function is_pmid at 0x10b4ac250>},
 'purl': {'datacite': 'PURL',
          'label': l'PURL',
          'validator': <function is_purl at 0x10b453b60>},
 'rrid': {'datacite': 'RRID',
          'label': l'RRID',
          'validator': <function is_rrid at 0x10b4ad2d0>},
 'upc': {'datacite': 'UPC',
         'label': l'UPC',
         'validator': <function always_valid at 0x10e7df7f0>},
 'url': {'datacite': 'URL',
         'label': l'URL',
         'validator': <function is_url at 0x10b453c10>},
 'urn': {'datacite': 'URN',
         'label': l'URN',
         'validator': <function is_urn at 0x10b453d70>},
 'w3id': {'datacite': 'w3id',
          'label': l'W3ID',
          'validator': <function always_valid at 0x10e7df7f0>},
 'wikidata': {'datacite': 'Other',
              'label': l'Wikidata',
              'validator': <function is_wikidata at 0x10b4ad0c0>}}
```

---

(rdm-records-require-secret-links-expiration)=
### RDM_RECORDS_REQUIRE_SECRET_LINKS_EXPIRATION

```{eval-rst}
Whether share access links require an expiration date to be set or not.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L953) |

---

(rdm-records-resource-class)=
### RDM_RECORDS_RESOURCE_CLASS

```{eval-rst}
Replacement for the plain RDM resource class.
```

| **OARepo Default Value** | `'oarepo_rdm.resources.records.resource:OARepoRDMRecordResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L32) |

---

(rdm-records-resource-config-class)=
### RDM_RECORDS_RESOURCE_CONFIG_CLASS

```{eval-rst}
Resource config class.
```

| **OARepo Default Value** | `'oarepo_rdm.resources.records.config:OARepoRDMRecordResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L29) |

---

(rdm-records-restriction-grace-period)=
### RDM_RECORDS_RESTRICTION_GRACE_PERIOD

```{eval-rst}
Grace period for changing record access to restricted.
```

| **Invenio RDM Default Value** | `datetime.timedelta(days=30)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L947) |

---

(rdm-records-reviews)=
### RDM_RECORDS_REVIEWS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L150) |

```
['community-submission']
```

---

(rdm-records-review-service-class)=
### RDM_RECORDS_REVIEW_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_rdm.services.delegating.DelegatingReviewService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L35) |

---

(rdm-records-service-class)=
### RDM_RECORDS_SERVICE_CLASS

```{eval-rst}
Replacement for the plain RDM service class.
```

| **OARepo Default Value** | `'oarepo_rdm.services.service:OARepoRDMService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L26) |

---

(rdm-records-service-components)=
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

(rdm-records-service-config-class)=
### RDM_RECORDS_SERVICE_CONFIG_CLASS

```{eval-rst}
Service config class.
```

| **OARepo Default Value** | `'oarepo_rdm.services.config:OARepoRDMServiceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L23) |

---

(rdm-records-ui-edit-url)=
### RDM_RECORDS_UI_EDIT_URL

```{eval-rst}
Default UI URL for the edit page of a Bibliographic Record.
```

| **Invenio RDM Default Value** | `'/uploads/<pid_value>'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L61) |

---

(rdm-records-user-fixture-passwords)=
### RDM_RECORDS_USER_FIXTURE_PASSWORDS

```{eval-rst}
Overrides for the user fixtures' passwords.

The password set for a user fixture in this dictionary overrides the
password set in the ``users.yaml`` file. This can be used to set custom
passwords for the fixture users (of course, this has to be configured
before the fixtures are installed, e.g. by setting up the services).
If ``None`` or an empty string is configured in this dictionary, then the
password from ``users.yaml`` will be used. If that is also absent, a password
will be generated randomly.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L49) |

```
{'admin@inveniosoftware.org': None}
```

---

(rdm-record-deletion-policy)=
### RDM_RECORD_DELETION_POLICY

```{eval-rst}
Policy class which evaluates whether a record can be deleted by a user.
```

| **Invenio RDM Default Value** | `RDMRecordDeletionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L179) |

---

(rdm-record-file-extractors)=
### RDM_RECORD_FILE_EXTRACTORS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L960) |

```
[<invenio_records_resources.services.files.extractors.zip.ZipExtractor object at 0x1111e8e10>]
```

---

(rdm-requests-routes)=
### RDM_REQUESTS_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1095) |

```
{'community-dashboard-invitation-details': '/communities/<pid_value>/invitations/<uuid:request_pid_value>',
 'community-dashboard-membership-request-details': '/communities/<pid_value>/membership-requests/<uuid:request_pid_value>',
 'community-dashboard-request-details': '/communities/<pid_value>/requests/<uuid:request_pid_value>',
 'user-dashboard-request-details': '/me/requests/<uuid:request_pid_value>'}
```

---

(rdm-request-record-deletion-checklist)=
### RDM_REQUEST_RECORD_DELETION_CHECKLIST

```{eval-rst}
Checklist which appears on the modal to redirect user from record deletion request if possible.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L232) |

```
[]
```

---

(rdm-request-record-deletion-enabled)=
### RDM_REQUEST_RECORD_DELETION_ENABLED

```{eval-rst}
Allow users to request record deletion.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L226) |

---

(rdm-request-record-deletion-policies)=
### RDM_REQUEST_RECORD_DELETION_POLICIES

```{eval-rst}
List of policies for record deletion requests.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L229) |

```
[<invenio_rdm_records.services.request_policies.RequestDeletionPolicy object at 0x1111ba900>]
```

---

(rdm-resource-access-tokens-enabled)=
### RDM_RESOURCE_ACCESS_TOKENS_ENABLED

```{eval-rst}
Flag to show whether RATs feature should be enabled.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L835) |

---

(rdm-resource-access-tokens-jwt-lifetime)=
### RDM_RESOURCE_ACCESS_TOKENS_JWT_LIFETIME

```{eval-rst}
Maximum tokens lifetime.
```

| **Invenio RDM Default Value** | `datetime.timedelta(seconds=1800)` |
|--------------|-----------|
| **Type** | timedelta |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L839) |

---

(rdm-resource-access-tokens-subject-schema)=
### RDM_RESOURCE_ACCESS_TOKENS_SUBJECT_SCHEMA

```{eval-rst}
Resource access token Marshmallow schema for parsing JWT subject.
```

| **Invenio RDM Default Value** | `tokens.resource_access.SubjectSchema` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L848) |

---

(rdm-resource-access-tokens-whitelisted-jwt-algorithms)=
### RDM_RESOURCE_ACCESS_TOKENS_WHITELISTED_JWT_ALGORITHMS

```{eval-rst}
Accepted JWT algorithms for decoding the RAT.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L842) |

```
['HS256', 'HS384', 'HS512']
```

---

(rdm-resource-access-token-request-arg)=
### RDM_RESOURCE_ACCESS_TOKEN_REQUEST_ARG

```{eval-rst}
URL argument to provide resource access token.
```

| **Invenio RDM Default Value** | `'resource_access_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L845) |

---

(rdm-search)=
### RDM_SEARCH
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L466); [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L75) |

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

(rdm-search-drafts)=
### RDM_SEARCH_DRAFTS
| **OARepo Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L507); [oarepo-rdm](https://github.com/oarepo/oarepo-rdm/blob/master/oarepo_rdm/initial_config.py#L76) |

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

(rdm-search-sort-by-verified)=
### RDM_SEARCH_SORT_BY_VERIFIED

```{eval-rst}
Sort records by 'verified' first.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L411) |

---

(rdm-search-user-communities)=
### RDM_SEARCH_USER_COMMUNITIES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1110) |

```
{'facets': ['visibility', 'type'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---

(rdm-search-user-requests)=
### RDM_SEARCH_USER_REQUESTS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1116) |

```
{'facets': ['type', 'status'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---

(rdm-search-versioning)=
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

(rdm-sort-options)=
### RDM_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L414) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'mostdownloaded': {'fields': ['-stats.all_versions.unique_downloads'],
                    'title': l'Most downloaded'},
 'mostviewed': {'fields': ['-stats.all_versions.unique_views'],
                'title': l'Most viewed'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'newestactivity': {'fields': ['-last_activity_at'], 'title': l'Newest activity'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'},
 'oldestactivity': {'fields': ['last_activity_at'], 'title': l'Oldest activity'},
 'updated-asc': {'fields': ['updated'], 'title': l'Least recently updated'},
 'updated-desc': {'fields': ['-updated'], 'title': l'Recently updated'},
 'version': {'fields': ['-versions.index'], 'title': l'Version'}}
```

---

(rdm-stats-exclude-preview-file-download-events)=
### RDM_STATS_EXCLUDE_PREVIEW_FILE_DOWNLOAD_EVENTS

```{eval-rst}
Exclude file-download stats events whose Referer is the file's own preview page.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L67) |

---

(rdm-user-moderation-enabled)=
### RDM_USER_MODERATION_ENABLED

```{eval-rst}
Flag to enable creation of user moderation requests on specific user actions.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L869) |

---

(recaptcha-private-key)=
### RECAPTCHA_PRIVATE_KEY

```{eval-rst}
reCAPTCHA private key.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L341) |

---

(recaptcha-public-key)=
### RECAPTCHA_PUBLIC_KEY

```{eval-rst}
reCAPTCHA public key.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L338) |

---

(records-files-rest-endpoints)=
### RECORDS_FILES_REST_ENDPOINTS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-records-files](https://github.com/inveniosoftware/invenio-records-files/blob/master/invenio_records_files/config.py#L11) |

```
{}
```

---

(records-permissions-record-policy)=
### RECORDS_PERMISSIONS_RECORD_POLICY
| **Invenio RDM Default Value** | `'invenio_records_permissions.policies.RecordPermissionPolicy'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-permissions](https://github.com/inveniosoftware/invenio-records-permissions/blob/master/invenio_records_permissions/config.py#L12) |

---

(records-refresolver-cls)=
### ***RECORDS_REFRESOLVER_CLS**

```{eval-rst}
Custom JSONSchemas ref resolver class.

Note that when using a custom ref resolver class you should also set
``RECORDS_REFRESOLVER_STORE`` to point to a JSONSchema ref resolver store.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L17); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L614) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(records-refresolver-store)=
### ***RECORDS_REFRESOLVER_STORE**

```{eval-rst}
JSONSchemas ref resolver store.

Used together with ``RECORDS_REFRESOLVER_CLS`` to provide a specific
ref resolver store.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L24); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L621) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(records-resources-allow-empty-files)=
### RECORDS_RESOURCES_ALLOW_EMPTY_FILES

```{eval-rst}
Allow empty files to be uploaded.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L26) |
| **Set by** | {py:func}`~oarepo_config.configure_files` |

---

(records-resources-archive-download-max-size)=
### RECORDS_RESOURCES_ARCHIVE_DOWNLOAD_MAX_SIZE

```{eval-rst}
Max total file size (bytes) for archive download. ``None`` disables the cap.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L64) |

---

(records-resources-default-transfer-type)=
### RECORDS_RESOURCES_DEFAULT_TRANSFER_TYPE

```{eval-rst}
Default transfer class to use.
One of 'L' (local), 'F' (fetch), 'R' (point to remote), 'M' (multipart).
```

| **Invenio RDM Default Value** | `'L'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L38) |

---

(records-resources-extracted-stream-chunk-size)=
### RECORDS_RESOURCES_EXTRACTED_STREAM_CHUNK_SIZE

```{eval-rst}
Chunk size of extracted stream used in ContainerItemResult.send_file().
```

| **Invenio RDM Default Value** | `65536` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L43) |

---

(records-resources-files-allowed-domains)=
### RECORDS_RESOURCES_FILES_ALLOWED_DOMAINS

```{eval-rst}
Explicitly allowed domains for external file fetching.

Only file URLs from these domains will be allowed to be fetched.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L17) |

```
[]
```

---

(records-resources-image-formats)=
### RECORDS_RESOURCES_IMAGE_FORMATS

```{eval-rst}
Which image formats to extract metadata for.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L23); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1216) |

```
['.jpg', '.jpeg', '.jp2', '.png', '.tif', '.tiff']
```

---

(records-resources-transfers)=
### RECORDS_RESOURCES_TRANSFERS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L29) |

```
['invenio_records_resources.services.files.transfer.LocalTransfer',
 'invenio_records_resources.services.files.transfer.FetchTransfer',
 'invenio_records_resources.services.files.transfer.RemoteTransfer',
 'invenio_records_resources.services.files.transfer.MultipartTransfer']
```

---

(records-resources-zip-formats)=
### RECORDS_RESOURCES_ZIP_FORMATS

```{eval-rst}
File extensions interpreted as ZIP files.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L46) |

```
['.zip']
```

---

(records-resources-zip-max-entries)=
### RECORDS_RESOURCES_ZIP_MAX_ENTRIES

```{eval-rst}
Max allowed entries inside ZIP file.
```

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L61) |

---

(records-resources-zip-max-header-size)=
### RECORDS_RESOURCES_ZIP_MAX_HEADER_SIZE

```{eval-rst}
Max header size of ZIP file that can be preloaded.
```

| **Invenio RDM Default Value** | `65536` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L52) |

---

(records-resources-zip-max-listing-entries)=
### RECORDS_RESOURCES_ZIP_MAX_LISTING_ENTRIES

```{eval-rst}
Max entries returned by the container listing API.
```

| **Invenio RDM Default Value** | `1000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L49) |

---

(records-resources-zip-max-ratio)=
### RECORDS_RESOURCES_ZIP_MAX_RATIO

```{eval-rst}
Max allowed compression ratio of an entry inside ZIP file.
```

| **Invenio RDM Default Value** | `200.0` |
|--------------|-----------|
| **Type** | float |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L58) |

---

(records-resources-zip-max-total-uncompressed)=
### RECORDS_RESOURCES_ZIP_MAX_TOTAL_UNCOMPRESSED

```{eval-rst}
Max allowed uncompressed size of ZIP.
```

| **Invenio RDM Default Value** | `524288000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L55) |

---

(records-rest-default-create-permission-factory)=
### RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY

```{eval-rst}
Default create permission factory: reject any request.
```

| **Invenio RDM Default Value** | `deny_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L357) |

---

(records-rest-default-delete-permission-factory)=
### RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY

```{eval-rst}
Default delete permission factory: reject any request.
```

| **Invenio RDM Default Value** | `deny_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L369) |

---

(records-rest-default-list-permission-factory)=
### RECORDS_REST_DEFAULT_LIST_PERMISSION_FACTORY

```{eval-rst}
Default list permission factory: allow all requests
```

| **Invenio RDM Default Value** | `allow_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L360) |

---

(records-rest-default-loaders)=
### RECORDS_REST_DEFAULT_LOADERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L237) |

```
{
    'application/json': lambda: request.get_json(),
    'application/json-patch+json': lambda: request.get_json(force=True),
}
```

---

(records-rest-default-read-permission-factory)=
### RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY

```{eval-rst}
Default read permission factory: check if the record exists.
```

| **Invenio RDM Default Value** | `check_search` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L363) |

---

(records-rest-default-results-size)=
### RECORDS_REST_DEFAULT_RESULTS_SIZE

```{eval-rst}
Default search results size.
```

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L381) |

---

(records-rest-default-sort)=
### RECORDS_REST_DEFAULT_SORT
| **Invenio RDM Default Value** | `dict(records=dict(query='bestmatch', noquery='mostrecent'))` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L302) |

---

(records-rest-default-update-permission-factory)=
### RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY

```{eval-rst}
Default update permission factory: reject any request.
```

| **Invenio RDM Default Value** | `deny_all` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L366) |

---

(records-rest-endpoints)=
### ***RECORDS_REST_ENDPOINTS**
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L192); [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L19) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

```
[]
```

---

(records-rest-facets)=
### RECORDS_REST_FACETS
| **Invenio RDM Default Value** | `dict(records=dict(aggs=dict(type=dict(terms=dict(field='type'))), post_filters=dict(type=terms_filte...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L322) |

---

(records-rest-facets-post-filters-propagate)=
### RECORDS_REST_FACETS_POST_FILTERS_PROPAGATE

```{eval-rst}
Define if the post_filters facets in one category should be applied as filters to all the other categories
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L354) |

---

(records-rest-search-error-handlers)=
### RECORDS_REST_SEARCH_ERROR_HANDLERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L372) |

```
{
    'query_parsing_exception': 'invenio_records_rest.views:search_query_parsing_exception_handler',
    'query_shard_exception': 'invenio_records_rest.views:search_query_parsing_exception_handler',
}
```

---

(records-rest-sort-options)=
### RECORDS_REST_SORT_OPTIONS
| **Invenio RDM Default Value** | `dict(records=dict(bestmatch=dict(title=_('Best match'), fields=['_score'], default_order='desc', ord...` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-records-rest](https://github.com/inveniosoftware/invenio-records-rest/blob/master/invenio_records_rest/config.py#L259) |

---

(records-ui-base-template)=
### RECORDS_UI_BASE_TEMPLATE
| **Default Value** | `'invenio_records_ui/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(records-ui-default-permission-factory)=
### RECORDS_UI_DEFAULT_PERMISSION_FACTORY

```{eval-rst}
Configure the default permission factory.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L16) |

---

(records-ui-endpoints)=
### ***RECORDS_UI_ENDPOINTS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L22); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L193) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

```
{'recid': {'pid_type': 'recid',
           'route': '/records/<pid_value>',
           'template': 'invenio_records_ui/detail.html'},
 'recid_export': {'pid_type': 'recid',
                  'route': '/records/<pid_value>/export/<format>',
                  'template': 'invenio_records_ui/export.html',
                  'view_imp': 'invenio_records_ui.views.export'}}
```

---

(records-ui-export-formats)=
### RECORDS_UI_EXPORT_FORMATS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L89) |

```
{}
```

---

(records-ui-login-endpoint)=
### RECORDS_UI_LOGIN_ENDPOINT

```{eval-rst}
Endpoint where redirect the user if login is required.
```

| **Invenio RDM Default Value** | `'security.login'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L19) |

---

(records-ui-tombstone-template)=
### RECORDS_UI_TOMBSTONE_TEMPLATE

```{eval-rst}
Configure the tombstone template.
```

| **Invenio RDM Default Value** | `'invenio_records_ui/tombstone.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-ui](https://github.com/inveniosoftware/invenio-records-ui/blob/master/invenio_records_ui/config.py#L13) |

---

(records-validation-types)=
### RECORDS_VALIDATION_TYPES

```{eval-rst}
Pass additional types when validating a record against a schema.
For more details, see:
`<https://python-jsonschema.readthedocs.io/en/latest/validate/#validating-types>`_.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-records](https://github.com/inveniosoftware/invenio-records/blob/master/invenio_records/config.py#L11) |

```
{}
```

---

(record-routes)=
### ***RECORD_ROUTES**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/generic_parameters.py#L46) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(related-resources-default-resource-type)=
### RELATED_RESOURCES_DEFAULT_RESOURCE_TYPE
| **OARepo Default Value** | `'dataset'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L31) |

---

(related-resources-default-timeout)=
### RELATED_RESOURCES_DEFAULT_TIMEOUT
| **OARepo Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L33) |

---

(related-resources-record-ui-schema)=
### RELATED_RESOURCES_RECORD_UI_SCHEMA
| **OARepo Default Value** | `'invenio_rdm_records.resources.serializers.ui.UIRecordSchema'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L32) |

---

(related-resources-resource-class)=
### RELATED_RESOURCES_RESOURCE_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.resources.RelatedResourcesResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L23) |

---

(related-resources-resource-config-class)=
### RELATED_RESOURCES_RESOURCE_CONFIG_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.resources.RelatedResourcesResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L24) |

---

(related-resources-service-class)=
### RELATED_RESOURCES_SERVICE_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.services.RelatedResourcesService'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L21) |

---

(related-resources-service-config-class)=
### RELATED_RESOURCES_SERVICE_CONFIG_CLASS
| **OARepo Default Value** | `'oarepo_related_resources.services.RelatedResourcesServiceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [oarepo-related-resources](https://github.com/oarepo/oarepo-related-resources/blob/master/oarepo_related_resources/config.py#L22) |

---

(remember-cookie-duration)=
### REMEMBER_COOKIE_DURATION

```{eval-rst}
Remember me cookie life time changed to 90 days instead of 365 days.
```

| **Invenio RDM Default Value** | `timedelta(days=90)` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L265) |

---

(repository-description)=
### ***REPOSITORY_DESCRIPTION**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(repository-keywords)=
### ***REPOSITORY_KEYWORDS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(repository-name)=
### ***REPOSITORY_NAME**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(repository-subtitle)=
### ***REPOSITORY_SUBTITLE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(repository-support-contact)=
### ***REPOSITORY_SUPPORT_CONTACT**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(requests-action-components)=
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

(requests-allowed-receivers)=
### REQUESTS_ALLOWED_RECEIVERS
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['user', 'group', 'auto_approve', 'multiple', 'action_need', 'community_role']
```

---

(requests-comments-allowed-extra-html-attrs)=
### REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_ATTRS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L162) |

```
{'img': ['src', 'alt', 'width', 'height']}
```

---

(requests-comments-allowed-extra-html-tags)=
### REQUESTS_COMMENTS_ALLOWED_EXTRA_HTML_TAGS

```{eval-rst}
Extend allowed HTML tags list for requests comments content.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L159) |

```
['img']
```

---

(requests-comment-preview-limit)=
### REQUESTS_COMMENT_PREVIEW_LIMIT

```{eval-rst}
Number of most recent child comments to inline in parent's search index.

This limits the size of indexed documents when comments have many replies.
Additional replies can be loaded via pagination.
```

| **Invenio RDM Default Value** | `5` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L144) |

---

(requests-entity-resolvers)=
### REQUESTS_ENTITY_RESOLVERS

```{eval-rst}
Registered resolvers for resolving/creating references in request metadata.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L37) |

```
[<invenio_users_resources.entity_resolvers.UserResolver object at 0x10de73620>,
 <invenio_users_resources.entity_resolvers.GroupResolver object at 0x10de73770>]
```

---

(requests-error-handlers)=
### REQUESTS_ERROR_HANDLERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1518) |

```
{
    **request_error_handlers,
    InvalidAccessRestrictions: create_error_handler(lambda e: HTTPJSONException(code=400, description=e.description)),
}
```

---

(requests-events-service-components)=
### REQUESTS_EVENTS_SERVICE_COMPONENTS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L154) |

```
[<class 'invenio_requests.services.requests.components.RequestCommentFileValidationComponent'>,
 <class 'invenio_requests.services.requests.components.RequestCommentFileCleanupComponent'>]
```

---

(requests-facets)=
### REQUESTS_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L75) |

```
{'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10de5f750>,
            'ui': {'field': 'status'}},
 'type': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10de5f610>,
          'ui': {'field': 'type'}}}
```

---

(requests-files-default-max-file-size)=
### REQUESTS_FILES_DEFAULT_MAX_FILE_SIZE

```{eval-rst}
10MB
```

| **Invenio RDM Default Value** | `10000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L152) |

---

(requests-files-default-quota-size)=
### REQUESTS_FILES_DEFAULT_QUOTA_SIZE

```{eval-rst}
100MB
```

| **Invenio RDM Default Value** | `100000000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L151) |

---

(requests-locking-enabled)=
### REQUESTS_LOCKING_ENABLED

```{eval-rst}
Enable locking/unlocking for request conversations.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L141) |

---

(requests-moderation-role)=
### REQUESTS_MODERATION_ROLE

```{eval-rst}
ID of the Role used for moderation.
```

| **Invenio RDM Default Value** | `'administration-moderation'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L95) |

---

(requests-permission-policy)=
### REQUESTS_PERMISSION_POLICY

```{eval-rst}
The requests permission policy, extended to work with guest access requests.
```

| **OARepo Default Value** | `RDMRequestsPermissionPolicy` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1514); [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L24); [oarepo-workflows](https://github.com/oarepo/oarepo-workflows/blob/master/oarepo_workflows/initial_config.py#L16) |

---

(requests-registered-event-types)=
### REQUESTS_REGISTERED_EVENT_TYPES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L30) |

```
[<RequestEventType 'L'>, <RequestEventType 'C'>, <RequestEventType 'R'>]
```

---

(requests-registered-types)=
### REQUESTS_REGISTERED_TYPES

```{eval-rst}
Configuration for registered Request Types.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L27) |

```
[]
```

---

(requests-resource-class)=
### REQUESTS_RESOURCE_CLASS
| **OARepo Default Value** | `OARepoRequestsResource` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L19) |

---

(requests-resource-config-class)=
### REQUESTS_RESOURCE_CONFIG_CLASS
| **OARepo Default Value** | `OARepoRequestsResourceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L20) |

---

(requests-reviewers-enabled)=
### REQUESTS_REVIEWERS_ENABLED

```{eval-rst}
Enable reviewers for requests.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L135) |

---

(requests-reviewers-max-number)=
### REQUESTS_REVIEWERS_MAX_NUMBER

```{eval-rst}
Maximum number of reviewers allowed for a request.
```

| **Invenio RDM Default Value** | `15` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L138) |

---

(requests-routes)=
### REQUESTS_ROUTES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L40) |

```
{'download_file_html': '/requests/<uuid:pid_value>/files/<path:file_key>'}
```

---

(requests-search)=
### REQUESTS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L45) |

```
{'facets': ['type', 'status'],
 'sort': ['bestmatch', 'newest', 'oldest', 'newestactivity', 'oldestactivity']}
```

---

(requests-service-class)=
### REQUESTS_SERVICE_CLASS
| **OARepo Default Value** | `OARepoRequestsService` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L17) |

---

(requests-service-config-class)=
### REQUESTS_SERVICE_CONFIG_CLASS
| **OARepo Default Value** | `OARepoRequestsServiceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [oarepo-requests](https://github.com/oarepo/oarepo-requests/blob/master/oarepo_requests/initial_config.py#L18) |

---

(requests-sort-options)=
### REQUESTS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L51) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'newestactivity': {'fields': ['-last_activity_at'], 'title': l'Newest activity'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'},
 'oldestactivity': {'fields': ['last_activity_at'], 'title': l'Oldest activity'}}
```

---

(requests-timeline-page-size)=
### REQUESTS_TIMELINE_PAGE_SIZE

```{eval-rst}
Amount of items per page on the request details timeline
```

| **Invenio RDM Default Value** | `10` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L91) |

---

(requests-user-moderation-facets)=
### REQUESTS_USER_MODERATION_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L124) |

```
{'is_open': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10deb0510>,
             'ui': {'field': 'is_open'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10de5f750>,
            'ui': {'field': 'status'}}}
```

---

(requests-user-moderation-search)=
### REQUESTS_USER_MODERATION_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L102) |

```
{'facets': ['status', 'is_open'], 'sort': ['bestmatch', 'newest', 'oldest']}
```

---

(requests-user-moderation-sort-options)=
### REQUESTS_USER_MODERATION_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-requests](https://github.com/inveniosoftware/invenio-requests/blob/master/invenio_requests/config.py#L108) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'}}
```

---

(rest-csrf-enabled)=
### REST_CSRF_ENABLED

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L742); [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L79) |

---

(rest-enable-cors)=
### REST_ENABLE_CORS

```{eval-rst}
Enable CORS configuration. (Default: ``False``).
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L54) |

---

(rest-mimetype-query-arg-name)=
### REST_MIMETYPE_QUERY_ARG_NAME

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-rest](https://github.com/inveniosoftware/invenio-rest/blob/master/invenio_rest/config.py#L57) |

---

(ror-client-id)=
### ***ROR_CLIENT_ID**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/generic_parameters.py#L46) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(s3-access-key-id)=
### ***S3_ACCESS_KEY_ID**

```{eval-rst}
The access key to use when creating the client.

This is entirely optional, and if not provided, the credentials configured for
the session will automatically be used.
See `Configuring Credentials
<https://boto3.readthedocs.io/en/latest/guide/configuration.html#credentials>`_.
for more information.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L32) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(s3-config-extra)=
### S3_CONFIG_EXTRA

```{eval-rst}
Additional configuration to be passed to S3f3.
In some cases, specially those not using AWS S3, some extra configuration might be needed.

 .. code-block:: python

    {
        "request_checksum_calculation": "WHEN_REQUIRED",
        "response_checksum_validation": "WHEN_REQUIRED",
    }
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L78) |

```
{}
```

---

(s3-default-block-size)=
### S3_DEFAULT_BLOCK_SIZE

```{eval-rst}
Default block size value used to send multi-part uploads to S3.
Typically 5Mb is minimum allowed by the API.
```

| **Invenio RDM Default Value** | `5242880` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L74) |

---

(s3-endpoint-url)=
### ***S3_ENDPOINT_URL**

```{eval-rst}
S3 server URL endpoint.

If using Amazon AWS S3 service this config variable can be set to None as the
underlining library, `boto3 <https://boto3.readthedocs.io/en/latest/>`_,
will automatically construct the appropriate URL to use when communicating with
a service.

If set to a value (including the "http/https" scheme) it will be passed as
``endpoint_url`` to boto3 `client
<https://boto3.readthedocs.io/en/latest/reference/core/session.html#boto3.session.Session.client>`_.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L9) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(s3-maximum-number-of-parts)=
### S3_MAXIMUM_NUMBER_OF_PARTS

```{eval-rst}
Maximum number of parts to be used.
See `AWS Multipart Upload Overview
<https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_ for more
information.
```

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L67) |

---

(s3-region-name)=
### S3_REGION_NAME

```{eval-rst}
S3 region name

This is entirely optional, and if not provided, the region name will be
automatically set to 'us-east-1'.

If set to a value it will be passed as ``region_name`` to boto3 `client
<https://boto3.readthedocs.io/en/latest/reference/core/session.html#boto3.session.Session.client>`_.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L22) |

---

(s3-secret-access-key)=
### ***S3_SECRET_ACCESS_KEY**

```{eval-rst}
The secret key to use when creating the client.

This is entirely optional, and if not provided, the credentials configured for
the session will automatically be used.
See `Configuring Credentials
<https://boto3.readthedocs.io/en/latest/guide/configuration.html#credentials>`_.
for more information.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L42) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(s3-signature-version)=
### S3_SIGNATURE_VERSION

```{eval-rst}
Version of the S3 signature algorithm. Can be 's3' (v2) or 's3v4' (v4).
See `Amazon Boto3 documentation on configuration variables
<https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuration-file>`_
for more information.
```

| **Invenio RDM Default Value** | `'s3v4'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L60) |

---

(s3-upload-url-expiration)=
### S3_UPLOAD_URL_EXPIRATION

```{eval-rst}
Number of seconds the file upload URL will be valid. The default here is 7 days
to allow large file uploads with large number of chunks to be completed. This is
currently the maximum allowed by the AWS.
See `Amazon Boto3 documentation on presigned URLs
<https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.generate_presigned_url>`_
for more information.
```

| **Invenio RDM Default Value** | `604800` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L91) |

---

(s3-url-expiration)=
### S3_URL_EXPIRATION

```{eval-rst}
Number of seconds the file serving URL will be valid.

See `Amazon Boto3 documentation on presigned URLs
<https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.generate_presigned_url>`_
for more information.
```

| **Invenio RDM Default Value** | `60` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-s3](https://github.com/inveniosoftware/invenio-s3/blob/master/invenio_s3/config.py#L52) |

---

(search-client-config)=
### ***SEARCH_CLIENT_CONFIG**

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L18) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(search-elastic-hosts)=
### SEARCH_ELASTIC_HOSTS

```{eval-rst}
Deprecated alias for ``SEARCH_HOSTS``.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L55) |

---

(search-hosts)=
### ***SEARCH_HOSTS**

```{eval-rst}
Search hosts.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L736); [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L37) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(search-index-prefix)=
### ***SEARCH_INDEX_PREFIX**

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L99) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(search-mappings)=
### SEARCH_MAPPINGS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L59) |

---

(search-results-min-score)=
### SEARCH_RESULTS_MIN_SCORE

```{eval-rst}
If set, the `min_score` parameter is added to each search request body.

The `min_score` parameter excludes results which have a `_score` less than
the minimum specified in `min_score`.

Note that the `max_score` varies depending on the number of results for a given
search query and it is not absolute value. Therefore, setting `min_score` too
high can lead to 0 results because it can be higher than any result's `_score`.

Please refer to `Elasticsearch min_score documentation
<https://www.elastic.co/guide/en/elasticsearch/reference/current/
search-request-min-score.html>`_ for more information.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-search](https://github.com/inveniosoftware/invenio-search/blob/master/invenio_search/config.py#L84) |

---

(search-ui-base-template)=
### SEARCH_UI_BASE_TEMPLATE
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(search-ui-header-template)=
### SEARCH_UI_HEADER_TEMPLATE
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(search-ui-jstemplate-count)=
### SEARCH_UI_JSTEMPLATE_COUNT

```{eval-rst}
Configure the count template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/count.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L29) |

---

(search-ui-jstemplate-error)=
### SEARCH_UI_JSTEMPLATE_ERROR

```{eval-rst}
Configure the error page template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/error.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L32) |

---

(search-ui-jstemplate-facets)=
### SEARCH_UI_JSTEMPLATE_FACETS

```{eval-rst}
Configure the facets template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/facets.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L35) |

---

(search-ui-jstemplate-loading)=
### SEARCH_UI_JSTEMPLATE_LOADING

```{eval-rst}
Configure the loading template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/loading.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L49) |

---

(search-ui-jstemplate-pagination)=
### SEARCH_UI_JSTEMPLATE_PAGINATION

```{eval-rst}
Configure the pagination template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/pagination.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L52) |

---

(search-ui-jstemplate-range)=
### SEARCH_UI_JSTEMPLATE_RANGE

```{eval-rst}
Configure the range template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/range.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L38) |

---

(search-ui-jstemplate-range-options)=
### SEARCH_UI_JSTEMPLATE_RANGE_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L41) |

```
{'histogramId': '#year_hist',
 'name': 'years',
 'selectionId': '#year_select',
 'width': 180}
```

---

(search-ui-jstemplate-results)=
### SEARCH_UI_JSTEMPLATE_RESULTS

```{eval-rst}
Configure the results template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/results.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L55) |

---

(search-ui-jstemplate-select-box)=
### SEARCH_UI_JSTEMPLATE_SELECT_BOX

```{eval-rst}
Configure the select box template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/selectbox.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L58) |

---

(search-ui-jstemplate-sort-order)=
### SEARCH_UI_JSTEMPLATE_SORT_ORDER

```{eval-rst}
Configure the toggle button template.
```

| **Invenio RDM Default Value** | `'templates/invenio_search_ui/togglebutton.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L61) |

---

(search-ui-search-api)=
### SEARCH_UI_SEARCH_API

```{eval-rst}
Configure the search engine endpoint.
```

| **Invenio RDM Default Value** | `'/api/records/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L21) |

---

(search-ui-search-config-gen)=
### SEARCH_UI_SEARCH_CONFIG_GEN
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L64) |

```
{'invenio_records_rest': <class 'invenio_search_ui.views.SearchAppInvenioRestConfigHelper'>}
```

---

(search-ui-search-index)=
### SEARCH_UI_SEARCH_INDEX

```{eval-rst}
Name of the search index used.
```

| **Invenio RDM Default Value** | `'records'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L24) |

---

(search-ui-search-template)=
### ***SEARCH_UI_SEARCH_TEMPLATE**

```{eval-rst}
Configure the search page template.
```

| **Invenio RDM Default Value** | `'invenio_search_ui/search.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L16); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L786) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(search-ui-search-view)=
### ***SEARCH_UI_SEARCH_VIEW**

```{eval-rst}
Default funtion to do the `search` route.
```

| **Invenio RDM Default Value** | `search` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-search-ui](https://github.com/inveniosoftware/invenio-search-ui/blob/master/invenio_search_ui/config.py#L13) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(secret-key)=
### ***SECRET_KEY**

```{eval-rst}
Flask secret key.

Each installation (dev, production, ...) needs a separate key.

SECURITY WARNING: keep the secret key used in production secret!
```

| **Invenio RDM Default Value** | `'CHANGE_ME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L217) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(secret-key-fallbacks)=
### SECRET_KEY_FALLBACKS
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-auto-login-after-confirm)=
### SECURITY_AUTO_LOGIN_AFTER_CONFIRM
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-blueprint-name)=
### SECURITY_BLUEPRINT_NAME
| **Default Value** | `'security'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-changeable)=
### ***SECURITY_CHANGEABLE**

```{eval-rst}
Allow password change by users.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L175) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(security-change-password-template)=
### SECURITY_CHANGE_PASSWORD_TEMPLATE

```{eval-rst}
Default template for change password.
```

| **Invenio RDM Default Value** | `'invenio_accounts/change_password.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L223) |

---

(security-change-salt)=
### SECURITY_CHANGE_SALT
| **Default Value** | `'change-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-change-url)=
### SECURITY_CHANGE_URL

```{eval-rst}
URL endpoint for password change.
```

| **Invenio RDM Default Value** | `'/account/settings/password/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L244) |

---

(security-cli-roles-name)=
### SECURITY_CLI_ROLES_NAME
| **Default Value** | `'roles'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-cli-users-name)=
### SECURITY_CLI_USERS_NAME
| **Default Value** | `'users'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-confirmable)=
### ***SECURITY_CONFIRMABLE**

```{eval-rst}
Allow user to confirm their email address.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L178) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(security-confirm-email-within)=
### SECURITY_CONFIRM_EMAIL_WITHIN

```{eval-rst}
Amount of time the email confirmation link is active.

Note, since the confirmation link will also login the associated user we expire
the link fast.
```

| **Invenio RDM Default Value** | `'30 minutes'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L187) |

---

(security-confirm-error-view)=
### SECURITY_CONFIRM_ERROR_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-confirm-salt)=
### SECURITY_CONFIRM_SALT
| **Default Value** | `'confirm-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-confirm-url)=
### SECURITY_CONFIRM_URL
| **Default Value** | `'/confirm'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-default-http-auth-realm)=
### SECURITY_DEFAULT_HTTP_AUTH_REALM
| **Default Value** | `'Login Required'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-default-remember-me)=
### SECURITY_DEFAULT_REMEMBER_ME

```{eval-rst}
"Remember me" default value in login form.

This is only the default value in the login form. A user can always choose to
change it when they login.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L168) |

---

(security-deprecated-hashing-schemes)=
### SECURITY_DEPRECATED_HASHING_SCHEMES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['hex_md5']
```

---

(security-deprecated-password-schemes)=
### SECURITY_DEPRECATED_PASSWORD_SCHEMES

```{eval-rst}
Deprecated password hashing algorithms.

Password hashes in a deprecated scheme are automatically migrated to the
new default algorithm the next time the user login.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L158) |

```
['invenio_aes_encrypted_email']
```

---

(security-email-html)=
### SECURITY_EMAIL_HTML
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-email-plaintext)=
### SECURITY_EMAIL_PLAINTEXT
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-email-subject-confirm)=
### SECURITY_EMAIL_SUBJECT_CONFIRM
| **Default Value** | `'Please confirm your email'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-email-subject-password-change-notice)=
### SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE
| **Default Value** | `'Your password has been changed'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-email-subject-password-notice)=
### SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE
| **Default Value** | `'Your password has been reset'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-email-subject-password-reset)=
### SECURITY_EMAIL_SUBJECT_PASSWORD_RESET
| **Default Value** | `'Password reset instructions'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-email-subject-register)=
### SECURITY_EMAIL_SUBJECT_REGISTER

```{eval-rst}
Email subject for account registration emails.
```

| **Invenio RDM Default Value** | `'Welcome'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L413) |

---

(security-flash-messages)=
### SECURITY_FLASH_MESSAGES
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-forgot-password-template)=
### SECURITY_FORGOT_PASSWORD_TEMPLATE

```{eval-rst}
Default template for password recovery (asking for email).
```

| **Invenio RDM Default Value** | `'invenio_accounts/forgot_password.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L211) |

---

(security-hashing-schemes)=
### SECURITY_HASHING_SCHEMES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['sha256_crypt', 'hex_md5']
```

---

(security-i18n-dirname)=
### SECURITY_I18N_DIRNAME
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/lib/python3.14/site-...` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-i18n-domain)=
### SECURITY_I18N_DOMAIN
| **Default Value** | `'messages'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-login-salt)=
### SECURITY_LOGIN_SALT
| **Default Value** | `'login-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-login-url)=
### SECURITY_LOGIN_URL

```{eval-rst}
URL endpoint for login.
```

| **Invenio RDM Default Value** | `'/login/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L238) |

---

(security-login-user-template)=
### SECURITY_LOGIN_USER_TEMPLATE

```{eval-rst}
Default template for login.
```

| **Invenio RDM Default Value** | `'invenio_oauthclient/login_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L214) |

---

(security-login-within)=
### SECURITY_LOGIN_WITHIN
| **Default Value** | `'1 days'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-login-without-confirmation)=
### ***SECURITY_LOGIN_WITHOUT_CONFIRMATION**

```{eval-rst}
Allow users to login without first confirming their email address.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L204) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(security-logout-url)=
### SECURITY_LOGOUT_URL

```{eval-rst}
URL endpoint for logout.
```

| **Invenio RDM Default Value** | `'/logout/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L241) |

---

(security-msg-already-confirmed)=
### SECURITY_MSG_ALREADY_CONFIRMED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Your email has already been confirmed.', 'info')
```

---

(security-msg-confirmation-expired)=
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

(security-msg-confirmation-request)=
### SECURITY_MSG_CONFIRMATION_REQUEST
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Confirmation instructions have been sent to %(email)s.', 'info')
```

---

(security-msg-confirmation-required)=
### SECURITY_MSG_CONFIRMATION_REQUIRED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Email requires confirmation.', 'error')
```

---

(security-msg-confirm-registration)=
### SECURITY_MSG_CONFIRM_REGISTRATION
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Thank you. Confirmation instructions have been sent to %(email)s.', 'success')
```

---

(security-msg-disabled-account)=
### SECURITY_MSG_DISABLED_ACCOUNT
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Account is disabled.', 'error')
```

---

(security-msg-email-already-associated)=
### SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('%(email)s is already associated with an account.', 'error')
```

---

(security-msg-email-confirmed)=
### SECURITY_MSG_EMAIL_CONFIRMED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Thank you. Your email has been confirmed.', 'success')
```

---

(security-msg-email-not-provided)=
### SECURITY_MSG_EMAIL_NOT_PROVIDED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Email not provided', 'error')
```

---

(security-msg-forgot-password)=
### SECURITY_MSG_FORGOT_PASSWORD
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Forgot password?', 'info')
```

---

(security-msg-invalid-confirmation-token)=
### SECURITY_MSG_INVALID_CONFIRMATION_TOKEN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid confirmation token.', 'error')
```

---

(security-msg-invalid-email-address)=
### SECURITY_MSG_INVALID_EMAIL_ADDRESS
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid email address', 'error')
```

---

(security-msg-invalid-login-token)=
### SECURITY_MSG_INVALID_LOGIN_TOKEN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid login token.', 'error')
```

---

(security-msg-invalid-password)=
### SECURITY_MSG_INVALID_PASSWORD
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid password', 'error')
```

---

(security-msg-invalid-redirect)=
### SECURITY_MSG_INVALID_REDIRECT
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Redirections outside the domain are forbidden', 'error')
```

---

(security-msg-invalid-reset-password-token)=
### SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Invalid reset password token.', 'error')
```

---

(security-msg-local-login-disabled)=
### SECURITY_MSG_LOCAL_LOGIN_DISABLED

```{eval-rst}
The error to be displayed in REST login when local login is disabled.
```

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L247) |

```
('Local login is disabled.', 'error')
```

---

(security-msg-login)=
### SECURITY_MSG_LOGIN
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Please log in to access this page.', 'info')
```

---

(security-msg-login-email-sent)=
### SECURITY_MSG_LOGIN_EMAIL_SENT
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Instructions to login have been sent to %(email)s.', 'success')
```

---

(security-msg-login-expired)=
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

(security-msg-password-breached)=
### SECURITY_MSG_PASSWORD_BREACHED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password on breached list', 'error')
```

---

(security-msg-password-breached-site-error)=
### SECURITY_MSG_PASSWORD_BREACHED_SITE_ERROR
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Failed to contact breached passwords site', 'error')
```

---

(security-msg-password-change)=
### SECURITY_MSG_PASSWORD_CHANGE
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You successfully changed your password.', 'success')
```

---

(security-msg-password-change-disabled)=
### SECURITY_MSG_PASSWORD_CHANGE_DISABLED

```{eval-rst}
The error to be displayed in REST password change when it is disabled.
```

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L253) |

```
('Password change is disabled.', 'error')
```

---

(security-msg-password-invalid-length)=
### SECURITY_MSG_PASSWORD_INVALID_LENGTH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password must be at least %(length)s characters', 'error')
```

---

(security-msg-password-is-the-same)=
### SECURITY_MSG_PASSWORD_IS_THE_SAME
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Your new password must be different than your previous password.', 'error')
```

---

(security-msg-password-mismatch)=
### SECURITY_MSG_PASSWORD_MISMATCH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password does not match', 'error')
```

---

(security-msg-password-not-provided)=
### SECURITY_MSG_PASSWORD_NOT_PROVIDED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password not provided', 'error')
```

---

(security-msg-password-not-set)=
### SECURITY_MSG_PASSWORD_NOT_SET
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('No password is set for this user', 'error')
```

---

(security-msg-password-recovery-disabled)=
### SECURITY_MSG_PASSWORD_RECOVERY_DISABLED
| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L256) |

```
('Password recovery is disabled.', 'error')
```

---

(security-msg-password-reset)=
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

(security-msg-password-reset-disabled)=
### SECURITY_MSG_PASSWORD_RESET_DISABLED

```{eval-rst}
The error to be displayed in REST password reset when it is disabled.
```

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L262) |

```
('Password reset is disabled.', 'error')
```

---

(security-msg-password-reset-expired)=
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

(security-msg-password-reset-request)=
### SECURITY_MSG_PASSWORD_RESET_REQUEST
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Instructions to reset your password have been sent to %(email)s.', 'info')
```

---

(security-msg-password-too-simple)=
### SECURITY_MSG_PASSWORD_TOO_SIMPLE
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Password not complex enough', 'error')
```

---

(security-msg-refresh)=
### SECURITY_MSG_REFRESH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Please reauthenticate to access this page.', 'info')
```

---

(security-msg-registration-disabled)=
### SECURITY_MSG_REGISTRATION_DISABLED

```{eval-rst}
The error to be displayed in REST registration when it is disabled.
```

| **Invenio RDM Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L250) |

```
('Registration is disabled.', 'error')
```

---

(security-msg-retype-password-mismatch)=
### SECURITY_MSG_RETYPE_PASSWORD_MISMATCH
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Passwords do not match', 'error')
```

---

(security-msg-unauthorized)=
### SECURITY_MSG_UNAUTHORIZED
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('You do not have permission to view this resource.', 'error')
```

---

(security-msg-user-does-not-exist)=
### SECURITY_MSG_USER_DOES_NOT_EXIST
| **Default Value** | `<tuple>` |
|--------------|-----------|
| **Type** | tuple |
| **Source** | unknown |

```
('Specified user does not exist', 'error')
```

---

(security-password-breached-count)=
### SECURITY_PASSWORD_BREACHED_COUNT
| **Default Value** | `1` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(security-password-check-breached)=
### SECURITY_PASSWORD_CHECK_BREACHED
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-password-complexity-checker)=
### SECURITY_PASSWORD_COMPLEXITY_CHECKER
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-password-hash)=
### SECURITY_PASSWORD_HASH

```{eval-rst}
Default password hashing algorithm for new passwords.
```

| **Invenio RDM Default Value** | `'pbkdf2_sha512'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L149) |

---

(security-password-length-min)=
### SECURITY_PASSWORD_LENGTH_MIN
| **Default Value** | `6` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(security-password-salt)=
### SECURITY_PASSWORD_SALT

```{eval-rst}
Salt for storing passwords.
```

| **Invenio RDM Default Value** | `'CHANGE_ME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L207) |

---

(security-password-schemes)=
### SECURITY_PASSWORD_SCHEMES

```{eval-rst}
Supported password hashing algorithms (for passwords already stored).

You should include both the default, supported and any deprecated schemes.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L152) |

```
['pbkdf2_sha512', 'invenio_aes_encrypted_email']
```

---

(security-password-single-hash)=
### SECURITY_PASSWORD_SINGLE_HASH

```{eval-rst}
Password hashing algorithms requiring single hasing only.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L165) |

```
['invenio_aes_encrypted_email']
```

---

(security-post-change-view)=
### SECURITY_POST_CHANGE_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-post-confirm-view)=
### SECURITY_POST_CONFIRM_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-post-login-view)=
### SECURITY_POST_LOGIN_VIEW
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-post-logout-view)=
### SECURITY_POST_LOGOUT_VIEW
| **Default Value** | `'/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-post-register-view)=
### SECURITY_POST_REGISTER_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-post-reset-view)=
### SECURITY_POST_RESET_VIEW
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-recoverable)=
### ***SECURITY_RECOVERABLE**

```{eval-rst}
Allow password recovery by users.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L181) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(security-registerable)=
### ***SECURITY_REGISTERABLE**

```{eval-rst}
Allow users to register.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L184) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(security-register-url)=
### SECURITY_REGISTER_URL

```{eval-rst}
URL endpoint for user registation.
```

| **Invenio RDM Default Value** | `'/signup/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L232) |

---

(security-register-user-template)=
### SECURITY_REGISTER_USER_TEMPLATE

```{eval-rst}
Default template for user registration.
```

| **Invenio RDM Default Value** | `'invenio_accounts/register_user.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L217) |

---

(security-reset-password-template)=
### SECURITY_RESET_PASSWORD_TEMPLATE

```{eval-rst}
Default template for password recovery (reset of the password).
```

| **Invenio RDM Default Value** | `'invenio_accounts/reset_password.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L220) |

---

(security-reset-password-within)=
### SECURITY_RESET_PASSWORD_WITHIN

```{eval-rst}
Amount of time the password reset link is active.

Note, since the confirmation link will also login the associated user we expire
the link fast.
```

| **Invenio RDM Default Value** | `'30 minutes'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L194) |

---

(security-reset-salt)=
### SECURITY_RESET_SALT
| **Default Value** | `'reset-salt'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-reset-url)=
### SECURITY_RESET_URL

```{eval-rst}
URL endpoint for password recovery.
```

| **Invenio RDM Default Value** | `'/lost-password/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L235) |

---

(security-send-confirmation-template)=
### SECURITY_SEND_CONFIRMATION_TEMPLATE

```{eval-rst}
Default template for email confirmation.
```

| **Invenio RDM Default Value** | `'invenio_accounts/send_confirmation.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L226) |

---

(security-send-login-template)=
### SECURITY_SEND_LOGIN_TEMPLATE

```{eval-rst}
Default template for email confirmation.
```

| **Invenio RDM Default Value** | `'invenio_accounts/send_login.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L229) |

---

(security-send-password-change-email)=
### SECURITY_SEND_PASSWORD_CHANGE_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-send-password-reset-email)=
### SECURITY_SEND_PASSWORD_RESET_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-send-password-reset-notice-email)=
### SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-send-register-email)=
### SECURITY_SEND_REGISTER_EMAIL
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(security-subdomain)=
### SECURITY_SUBDOMAIN
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-token-authentication-header)=
### SECURITY_TOKEN_AUTHENTICATION_HEADER
| **Default Value** | `'Authentication-Token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-token-authentication-key)=
### SECURITY_TOKEN_AUTHENTICATION_KEY
| **Default Value** | `'auth_token'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(security-token-max-age)=
### SECURITY_TOKEN_MAX_AGE
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-trackable)=
### SECURITY_TRACKABLE

```{eval-rst}
Enable user tracking on login.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-accounts](https://github.com/inveniosoftware/invenio-accounts/blob/master/invenio_accounts/config.py#L201) |

---

(security-url-prefix)=
### SECURITY_URL_PREFIX
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(security-user-identity-attributes)=
### SECURITY_USER_IDENTITY_ATTRIBUTES
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
['email']
```

---

(security-zxcvbn-minimum-score)=
### SECURITY_ZXCVBN_MINIMUM_SCORE
| **Default Value** | `3` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(send-file-max-age-default)=
### ***SEND_FILE_MAX_AGE_DEFAULT**
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(sentry-dsn)=
### SENTRY_DSN

```{eval-rst}
Set SENTRY_DSN environment variable.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-logging](https://github.com/inveniosoftware/invenio-logging/blob/master/invenio_logging/config.py#L98) |

---

(server-name)=
### SERVER_NAME
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(session-cookie-domain)=
### ***SESSION_COOKIE_DOMAIN**
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(session-cookie-httponly)=
### SESSION_COOKIE_HTTPONLY
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(session-cookie-name)=
### SESSION_COOKIE_NAME
| **Default Value** | `'session'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(session-cookie-partitioned)=
### SESSION_COOKIE_PARTITIONED
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(session-cookie-path)=
### SESSION_COOKIE_PATH
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(session-cookie-samesite)=
### SESSION_COOKIE_SAMESITE

```{eval-rst}
Restricts how cookies are sent with requests from external sites.
```

| **Invenio RDM Default Value** | `'Lax'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L228) |

---

(session-cookie-secure)=
### ***SESSION_COOKIE_SECURE**

```{eval-rst}
Sets cookie with the secure flag by default.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L225) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(session-key-bits)=
### SESSION_KEY_BITS
| **Default Value** | `64` |
|--------------|-----------|
| **Type** | int |
| **Source** | unknown |

---

(session-random-source)=
### SESSION_RANDOM_SOURCE
| **Default Value** | `<random.SystemRandom object at 0x83dc07020>` |
|--------------|-----------|
| **Type** | SystemRandom |
| **Source** | unknown |

---

(session-refresh-each-request)=
### SESSION_REFRESH_EACH_REQUEST
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(settings-template)=
### ***SETTINGS_TEMPLATE**

```{eval-rst}
Settings page template used for e.g. display user settings views.
```

| **Invenio RDM Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L41); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L276) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(sitemap-max-entry-count)=
### SITEMAP_MAX_ENTRY_COUNT

```{eval-rst}
Maximum number of entries (<url> or <sitemap>) per file.

The Sitemap protocol sets it at 50_000, but it also sets the max size of the
resulting file at 50 MiB. Following the initial Zenodo implementation, we
set it much lower than 50_000 so as to not have to check for generated size.

Following the initial Zenodo implementation, we use the same config for the
number of entries in the Sitemap Index and Sitemap files.
```

| **Invenio RDM Default Value** | `10000` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L11) |

---

(sitemap-root-view-enabled)=
### SITEMAP_ROOT_VIEW_ENABLED

```{eval-rst}
Enable the `/sitemap.xml` endpoint serving the first sitemap index.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L25) |

---

(sitemap-sections)=
### SITEMAP_SECTIONS

```{eval-rst}
Instances of `sitemap.SitemapSection` that will populate the Sitemap files.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Sources** | [invenio-sitemap](https://github.com/inveniosoftware/invenio-sitemap/blob/master/invenio_sitemap/config.py#L22); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1556) |

```
[]
```

---

(site-api-url)=
### ***SITE_API_URL**
| **Invenio RDM Default Value** | `'https://127.0.0.1:5000/api'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L15) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(site-ui-url)=
### ***SITE_UI_URL**
| **Invenio RDM Default Value** | `'https://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-records-resources](https://github.com/inveniosoftware/invenio-records-resources/blob/master/invenio_records_resources/config.py#L13) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(sqlalchemy-binds)=
### SQLALCHEMY_BINDS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{}
```

---

(sqlalchemy-database-uri)=
### ***SQLALCHEMY_DATABASE_URI**
| **Invenio RDM Default Value** | `'sqlite:////Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instan...` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L521) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(sqlalchemy-echo)=
### SQLALCHEMY_ECHO

```{eval-rst}
Enable to see all SQL queries.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L529) |

---

(sqlalchemy-engine-options)=
### SQLALCHEMY_ENGINE_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L532) |

```
{}
```

---

(sqlalchemy-record-queries)=
### SQLALCHEMY_RECORD_QUERIES
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(sqlalchemy-track-modifications)=
### SQLALCHEMY_TRACK_MODIFICATIONS
| **Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(stats-aggregations)=
### STATS_AGGREGATIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1284); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L47) |

```
{}
```

---

(stats-events)=
### STATS_EVENTS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1248); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L25) |

```
{}
```

---

(stats-events-utc-datetime-enabled)=
### STATS_EVENTS_UTC_DATETIME_ENABLED

```{eval-rst}
Enable timezone-aware UTC datetimes for event timestamps.

When set to ``False`` (default), naive UTC datetimes are used (tzinfo is
stripped via ``datetime.replace(tzinfo=None)``). Set to ``True`` to use
timezone-aware UTC datetimes with explicit UTC timezone information.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L80) |

---

(stats-mq-exchange)=
### STATS_MQ_EXCHANGE
| **Invenio RDM Default Value** | `Exchange('events', type='direct', delivery_mode='transient')` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L67) |

---

(stats-permission-factory)=
### STATS_PERMISSION_FACTORY

```{eval-rst}
Permission factory used by the statistics REST API.

This is a function which returns a permission granting or forbidding access
to a request. It is of the form ``permission_factory(query_name, params)``
where ``query_name`` is the name of the statistic requested by the user and
``params`` is a dict of parameters for this statistic. The result of the
function is a Permission.

See Invenio-access and Flask-principal for a better understanding of the
access control mechanisms.
```

| **Invenio RDM Default Value** | `permissions_policy_lookup_factory` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1418); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L53) |

---

(stats-queries)=
### STATS_QUERIES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1335); [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L50) |

```
{}
```

---

(stats-register-index-templates)=
### STATS_REGISTER_INDEX_TEMPLATES

```{eval-rst}
Register templates as index templates.

Default behaviour will register the templates as search templates.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L74) |

---

(stats-register-receivers)=
### ***STATS_REGISTER_RECEIVERS**

```{eval-rst}
Enable the registration of signal receivers.

Default is ``True``.
The signal receivers are functions which will listen to the signals listed in
by the ``STATS_EVENTS`` config variable. An event will be generated for each
signal sent.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-stats](https://github.com/inveniosoftware/invenio-stats/blob/master/invenio_stats/config.py#L16) |
| **Set by** | {py:func}`~oarepo_config.configure_stats` |

---

(templates-auto-reload)=
### TEMPLATES_AUTO_RELOAD
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(testing)=
### TESTING
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(theme-401-template)=
### THEME_401_TEMPLATE

```{eval-rst}
The template used for 401 Unauthorized errors.
```

| **Invenio RDM Default Value** | `'invenio_theme/401.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L144) |

---

(theme-403-template)=
### THEME_403_TEMPLATE

```{eval-rst}
The template used for 403 Forbidden errors.
```

| **Invenio RDM Default Value** | `'invenio_theme/403.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L147) |

---

(theme-404-template)=
### THEME_404_TEMPLATE

```{eval-rst}
The template used for 404 Not Found errors.
```

| **Invenio RDM Default Value** | `'invenio_theme/404.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L150) |

---

(theme-429-template)=
### THEME_429_TEMPLATE

```{eval-rst}
The template used for 429 Too Many Requests errors.
```

| **Invenio RDM Default Value** | `'invenio_theme/429.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L153) |

---

(theme-500-template)=
### THEME_500_TEMPLATE

```{eval-rst}
The template used for 500 Internal Server Error errors.
```

| **Invenio RDM Default Value** | `'invenio_theme/500.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L156) |

---

(theme-base-template)=
### THEME_BASE_TEMPLATE

```{eval-rst}
Template which all templates in Invenio-Theme all extends from.

Defaults to value of :const:`BASE_TEMPLATE`.
```

| **Invenio RDM Default Value** | `'invenio_theme/page.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L67) |

---

(theme-cover-template)=
### THEME_COVER_TEMPLATE

```{eval-rst}
Template which all cover templates in Invenio-Theme all extends from.

Defaults to value of :const:`COVER_TEMPLATE`.
```

| **Invenio RDM Default Value** | `'invenio_theme/page_cover.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L73) |

---

(theme-css-template)=
### ***THEME_CSS_TEMPLATE**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-error-template)=
### THEME_ERROR_TEMPLATE

```{eval-rst}
Base template for error pages.
```

| **Invenio RDM Default Value** | `'invenio_theme/page_error.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L85) |

---

(theme-footer-template)=
### ***THEME_FOOTER_TEMPLATE**

```{eval-rst}
Footer template which is normally included in :data:`BASE_TEMPLATE`.
```

| **Invenio RDM Default Value** | `'invenio_theme/footer.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L50); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L279) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-frontpage)=
### ***THEME_FRONTPAGE**

```{eval-rst}
Enable or disable basic frontpage view.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L126); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L282) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-frontpage-logo)=
### ***THEME_FRONTPAGE_LOGO**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-frontpage-template)=
### ***THEME_FRONTPAGE_TEMPLATE**

```{eval-rst}
Template for front page.
```

| **Invenio RDM Default Value** | `'invenio_theme/frontpage.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L132); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L291) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-frontpage-title)=
### ***THEME_FRONTPAGE_TITLE**

```{eval-rst}
The title shown on the frontpage.
```

| **Invenio RDM Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L129); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L285) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-generator)=
### THEME_GENERATOR

```{eval-rst}
Generator meta tag to identify the software that generated the page.

Accepts a string or a func returning a string. Set it to `None` to disable it.
```

| **Invenio RDM Default Value** | `'Invenio'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L88); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L315) |

---

(theme-google-site-verification)=
### THEME_GOOGLE_SITE_VERIFICATION

```{eval-rst}
List of Google Site Verification tokens to be used.

This adds the Google Site Verification into the meta tags of all pages.
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L114) |

```
[]
```

---

(theme-header-login-template)=
### ***THEME_HEADER_LOGIN_TEMPLATE**

```{eval-rst}
Header login template, included in :data:`THEME_HEADER_TEMPLATE`.
```

| **Invenio RDM Default Value** | `'invenio_theme/header_login.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L47); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L294) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-header-template)=
### ***THEME_HEADER_TEMPLATE**

```{eval-rst}
Header template which is normally included in :data:`BASE_TEMPLATE`.
```

| **Invenio RDM Default Value** | `'invenio_theme/header.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L44); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L288) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-icons)=
### THEME_ICONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L159) |

```
{'bootstrap3': {'*': 'fa fa-{} fa-fw',
                'codepen': 'fa fa-codepen fa-fw',
                'cogs': 'fa fa-cogs fa-fw',
                'key': 'fa fa-key fa-fw',
                'link': 'fa fa-link fa-fw',
                'shield': 'fa fa-shield fa-fw',
                'user': 'fa fa-user fa-fw'},
 'semantic-ui': {'*': '{} icon',
                 'codepen': 'codepen icon',
                 'cogs': 'cogs icon',
                 'exchange': 'exchange icon',
                 'home': 'home icon',
                 'key': 'key icon',
                 'link': 'linkify icon',
                 'shield': 'shield alternate icon',
                 'star_outline': 'star outline icon',
                 'user': 'user icon',
                 'users': 'users icon'}}
```

---

(theme-javascript-template)=
### ***THEME_JAVASCRIPT_TEMPLATE**

```{eval-rst}
Javascript assets template, normally included in :data:`BASE_TEMPLATE`.

The default template just includes the Invenio-Theme JavaScript bundle.
Set a new template if you would like to customize which JavaScript assets are
included on all pages.
```

| **Invenio RDM Default Value** | `'invenio_theme/javascript.html'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L53); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L333) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-logo)=
### ***THEME_LOGO**

```{eval-rst}
The logo to be used on the header and on the cover.
```

| **Invenio RDM Default Value** | `'images/invenio-white.svg'` |
|--------------|-----------|
| **Type** | str |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L120); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L321) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-logo-admin)=
### THEME_LOGO_ADMIN

```{eval-rst}
The logo to be used on the admin views header.
```

| **Invenio RDM Default Value** | `'images/invenio-white.svg'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L123) |

---

(theme-mathjax-cdn)=
### THEME_MATHJAX_CDN

```{eval-rst}
MathJax configuration for rendering mathematical formulas.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L186) |

---

(theme-meta-robot-tags)=
### THEME_META_ROBOT_TAGS

```{eval-rst}
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
```

| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L94) |

```
[]
```

---

(theme-searchbar)=
### THEME_SEARCHBAR

```{eval-rst}
Enable or disable the header search bar.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L135) |

---

(theme-search-endpoint)=
### ***THEME_SEARCH_ENDPOINT**

```{eval-rst}
The endpoint for the search bar.
```

| **Invenio RDM Default Value** | `'/search'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L138) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-settings-template)=
### THEME_SETTINGS_TEMPLATE

```{eval-rst}
Template which all settings templates in Invenio-Theme all extends from.

Defaults to value of :const:`SETTINGS_TEMPLATE`.
```

| **Invenio RDM Default Value** | `'invenio_theme/page_settings.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L79) |

---

(theme-show-frontpage-intro-section)=
### ***THEME_SHOW_FRONTPAGE_INTRO_SECTION**

```{eval-rst}
Front page intro section visibility
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L330) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-sitename)=
### ***THEME_SITENAME**

```{eval-rst}
The name of the site to be used on the header and as a title.
```

| **Invenio RDM Default Value** | `l'Invenio'` |
|--------------|-----------|
| **Type** | LazyString |
| **Sources** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L141); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L324) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-siteurl)=
### THEME_SITEURL
| **Invenio RDM Default Value** | `'http://127.0.0.1:5000'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-rdm-records](https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py#L71) |

---

(theme-trackingcode-template)=
### ***THEME_TRACKINGCODE_TEMPLATE**

```{eval-rst}
Template for including a tracking code for web analytics.

The default template does not include any tracking code.
```

| **Invenio RDM Default Value** | `'invenio_theme/trackingcode.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-theme](https://github.com/inveniosoftware/invenio-theme/blob/master/invenio_theme/config.py#L61) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(theme-twitterhandle)=
### THEME_TWITTERHANDLE

```{eval-rst}
Twitter handle.
```

| **Invenio RDM Default Value** | `''` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L327) |

---

(trap-bad-request-errors)=
### TRAP_BAD_REQUEST_ERRORS
| **Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | unknown |

---

(trap-http-exceptions)=
### TRAP_HTTP_EXCEPTIONS
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(trusted-hosts)=
### TRUSTED_HOSTS

```{eval-rst}
A list of host/domain names that can be served.

This is a security measure to prevent HTTP Host header attacks, which are
possible even under many seemingly-safe web server configurations.

By default all hosts are allowed. Values in this list can be fully qualified
names (e.g. 'www.example.com'). The validation only applies to
``request.host``.

In addition to this configuration variable, you should make sure that your
web server does not route requests to the application with an invalid Host
header.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Sources** | [invenio-app](https://github.com/inveniosoftware/invenio-app/blob/master/invenio_app/config.py#L173); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L205) |

---

(type-checking)=
### TYPE_CHECKING
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(userprofiles)=
### USERPROFILES

```{eval-rst}
Enable or disable module extensions.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L11) |

---

(userprofiles-base-template)=
### USERPROFILES_BASE_TEMPLATE

```{eval-rst}
Base templates for user profile module.
```

| **Invenio RDM Default Value** | `'invenio_userprofiles/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L26) |

---

(userprofiles-email-enabled)=
### USERPROFILES_EMAIL_ENABLED

```{eval-rst}
Include the user email in the profile form.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L14) |

---

(userprofiles-extend-security-forms)=
### USERPROFILES_EXTEND_SECURITY_FORMS

```{eval-rst}
Extend the Invenio-Accounts user registration forms.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Sources** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L17); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L419) |

---

(userprofiles-profile-template)=
### USERPROFILES_PROFILE_TEMPLATE

```{eval-rst}
Default profile template.
```

| **Invenio RDM Default Value** | `'invenio_userprofiles/settings/profile.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L20) |

---

(userprofiles-profile-url)=
### USERPROFILES_PROFILE_URL

```{eval-rst}
Default profile URL endpoint.
```

| **Invenio RDM Default Value** | `'/account/settings/profile/'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L23) |

---

(userprofiles-read-only)=
### ***USERPROFILES_READ_ONLY**

```{eval-rst}
Make the user profiles read-only.
```

| **Invenio RDM Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L32) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters`, {py:func}`~oarepo_config.configure_einfra_oidc` |

---

(userprofiles-settings-template)=
### USERPROFILES_SETTINGS_TEMPLATE

```{eval-rst}
Settings base templates for user profile module.
```

| **Invenio RDM Default Value** | `'invenio_userprofiles/settings/base.html'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-userprofiles](https://github.com/inveniosoftware/invenio-userprofiles/blob/master/invenio_userprofiles/config.py#L29) |

---

(users-resources-avatar-colors)=
### USERS_RESOURCES_AVATAR_COLORS
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L21) |

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

(users-resources-domains-org-schema)=
### USERS_RESOURCES_DOMAINS_ORG_SCHEMA

```{eval-rst}
Domains organisation schema config.
```

| **Invenio RDM Default Value** | `OrgPropsSchema` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L311) |

---

(users-resources-domains-search)=
### USERS_RESOURCES_DOMAINS_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L149) |

```
{'facets': ['status', 'flagged', 'category', 'organisation', 'tld'],
 'sort': ['bestmatch',
          'domain',
          'newest',
          'oldest',
          'updated',
          'num-users',
          'num-active',
          'num-inactive',
          'num-confirmed',
          'num-verified',
          'num-blocked']}
```

---

(users-resources-domains-search-facets)=
### USERS_RESOURCES_DOMAINS_SEARCH_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L215) |

```
{'category': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x1121271c0>,
              'ui': {'field': 'category'}},
 'flagged': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x11217d7d0>,
             'ui': {'field': 'flagged'}},
 'organisation': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x1121263c0>,
                  'ui': {'field': 'organisation'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x11217e3d0>,
            'ui': {'field': 'status'}},
 'tld': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x1121265f0>,
         'ui': {'field': 'tld'}}}
```

---

(users-resources-domains-sort-options)=
### USERS_RESOURCES_DOMAINS_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L167) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'domain': {'fields': ['domain', '-created'], 'title': l'Domain'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'num-active': {'fields': ['-num_active'], 'title': l'# Active'},
 'num-blocked': {'fields': ['-num_blocked'], 'title': l'# Blocked'},
 'num-confirmed': {'fields': ['-num_confirmed'], 'title': l'# Confirmed'},
 'num-inactive': {'fields': ['-num_inactive'], 'title': l'# Inactive'},
 'num-users': {'fields': ['-num_users'], 'title': l'# Users'},
 'num-verified': {'fields': ['-num_verified'], 'title': l'# Verified'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'},
 'updated': {'fields': ['-updated'], 'title': l'Recently updated'}}
```

---

(users-resources-groups-admin-facets)=
### USERS_RESOURCES_GROUPS_ADMIN_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L279) |

```
{'is_managed': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x10dd95e80>,
                'ui': {'field': 'is_managed'}}}
```

---

(users-resources-groups-admin-search)=
### USERS_RESOURCES_GROUPS_ADMIN_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L273) |

```
{'facets': ['is_managed'],
 'sort': ['bestmatch', 'name', 'name_desc', 'managed', 'unmanaged']}
```

---

(users-resources-groups-admin-sort-options)=
### USERS_RESOURCES_GROUPS_ADMIN_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L249) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'managed': {'fields': ['-is_managed', 'name.keyword'], 'title': l'Managed first'},
 'name': {'fields': ['name.keyword'], 'title': l'Name (A-Z)'},
 'name_desc': {'fields': ['-name.keyword'], 'title': l'Name (Z-A)'},
 'unmanaged': {'fields': ['is_managed', 'name.keyword'], 'title': l'Unmanaged first'}}
```

---

(users-resources-groups-enabled)=
### USERS_RESOURCES_GROUPS_ENABLED

```{eval-rst}
Config to enable features related to existence of groups.
```

| **Invenio RDM Default Value** | `True` |
|--------------|-----------|
| **Type** | bool |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L314) |

---

(users-resources-moderation-lock-default-timeout)=
### USERS_RESOURCES_MODERATION_LOCK_DEFAULT_TIMEOUT

```{eval-rst}
Default timeout, in seconds, to lock a user when moderating.
```

| **Invenio RDM Default Value** | `30` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L142) |

---

(users-resources-moderation-lock-renewal-timeout)=
### USERS_RESOURCES_MODERATION_LOCK_RENEWAL_TIMEOUT

```{eval-rst}
Renewal timeout, in seconds, to increase the lock time for a user when moderating.
```

| **Invenio RDM Default Value** | `120` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L145) |

---

(users-resources-protected-group-names)=
### USERS_RESOURCES_PROTECTED_GROUP_NAMES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L289) |

```
['admin', 'administration', 'superuser-access', 'administration-moderation']
```

---

(users-resources-search)=
### USERS_RESOURCES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L54) |

```
{'facets': ['status', 'visibility', 'domain_status', 'domain', 'affiliations', 'roles'],
 'sort': ['bestmatch', 'username', 'email', 'domain', 'newest', 'oldest', 'updated']}
```

---

(users-resources-search-facets)=
### USERS_RESOURCES_SEARCH_FACETS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L99) |

```
{'affiliations': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x112126740>,
                  'ui': {'field': 'profile.affiliations.keyword'}},
 'domain': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x112126660>,
            'ui': {'field': 'domain'}},
 'domain_status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x1121266d0>,
                   'ui': {'field': 'domain_status'}},
 'roles': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x112126580>,
           'facet_options': {'size': 100},
           'ui': {'field': 'roles'}},
 'status': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x1121272a0>,
            'ui': {'field': 'status'}},
 'visibility': {'facet': <invenio_records_resources.services.records.facets.facets.TermsFacet object at 0x112127380>,
                'ui': {'field': 'visibility'}}}
```

---

(users-resources-service-schema)=
### USERS_RESOURCES_SERVICE_SCHEMA

```{eval-rst}
Schema used by the users service.
```

| **Invenio RDM Default Value** | `NotificationsUserSchema` |
|--------------|-----------|
| **Type** | unknown |
| **Sources** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1505); [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L51) |

---

(users-resources-sort-options)=
### USERS_RESOURCES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-users-resources](https://github.com/inveniosoftware/invenio-users-resources/blob/master/invenio_users_resources/config.py#L67) |

```
{'bestmatch': {'fields': ['_score'], 'title': l'Best match'},
 'domain': {'fields': ['domain', '-created'], 'title': l'Domain'},
 'email': {'fields': ['email_hidden', '-created'], 'title': l'Email'},
 'newest': {'fields': ['-created'], 'title': l'Newest'},
 'oldest': {'fields': ['created'], 'title': l'Oldest'},
 'updated': {'fields': ['-updated'], 'title': l'Recently updated'},
 'username': {'fields': ['username.keyword', '-created'], 'title': l'Username'}}
```

---

(user-dashboard-menu-overrides)=
### USER_DASHBOARD_MENU_OVERRIDES

```{eval-rst}
Overrides for "dashboard" menu.
```

| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1532) |

```
{}
```

---

(use-x-sendfile)=
### USE_X_SENDFILE
| **Default Value** | `False` |
|--------------|-----------|
| **Type** | bool |
| **Source** | unknown |

---

(vcs-template-index)=
### VCS_TEMPLATE_INDEX
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-index.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1610) |

---

(vcs-template-index-item)=
### VCS_TEMPLATE_INDEX_ITEM
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-index-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1611) |

---

(vcs-template-release-item)=
### VCS_TEMPLATE_RELEASE_ITEM
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-release-item.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1614) |

---

(vcs-template-repo-switch)=
### VCS_TEMPLATE_REPO_SWITCH
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-repo-switch.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1613) |

---

(vcs-template-view)=
### VCS_TEMPLATE_VIEW
| **Invenio RDM Default Value** | `'invenio_vcs/rdm-view.html'` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L1612) |

---

(vocabularies-affiliations-edmo-country-mapping)=
### VOCABULARIES_AFFILIATIONS_EDMO_COUNTRY_MAPPING
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L236) |

```
{'Cape Verde': 'Cabo Verde'}
```

---

(vocabularies-affiliation-schemes)=
### ***VOCABULARIES_AFFILIATION_SCHEMES**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L66) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'edmo': {'label': l'EDMO', 'validator': <function is_edmo at 0x10e4217a0>},
 'gnd': {'label': l'GND', 'validator': <function is_gnd at 0x10b4ac3b0>},
 'grid': {'label': l'GRID', 'validator': <function <lambda> at 0x10df5e350>},
 'isni': {'label': l'ISNI', 'validator': <function is_isni at 0x10b453950>},
 'pic': {'label': l'PIC', 'validator': <function is_pic at 0x10e4212d0>},
 'ror': {'label': l'ROR', 'validator': <function is_ror at 0x10b4ace00>}}
```

---

(vocabularies-awards-ec-ror-id)=
### VOCABULARIES_AWARDS_EC_ROR_ID

```{eval-rst}
ROR ID for EC funder.
```

| **Invenio RDM Default Value** | `'00k4n6c32'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L154) |

---

(vocabularies-awards-openaire-funders)=
### VOCABULARIES_AWARDS_OPENAIRE_FUNDERS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L88) |

```
{'100012733___': '03xkf7525',
 '100013433___': '054tsxk98',
 '100015319___': '04bnxk453',
 '100019637___': '003mr9q86',
 '100022943___': '02g8v2v69',
 '501100001581': '02dd61a62',
 '501100001587': '04q0a4f84',
 '501100001630': '051sx6d27',
 '501100001635': '00a0n9e72',
 '501100001638': '04a1a1e81',
 '501100011626': '04q0a4f84',
 'aka_________': '05k73zm37',
 'anr_________': '00rbzpz17',
 'arc_________': '05mmh0f86',
 'asap________': '03zj4c476',
 'cf__________': '01kpjmx04',
 'cihr________': '01gavpb45',
 'corda_______': '00k4n6c32',
 'corda_____he': '00k4n6c32',
 'corda__h2020': '00k4n6c32',
 'dfgf________': '018mejw64',
 'drf_________': '004j3q729',
 'erasmusplus_': '00k4n6c32',
 'euenvagency_': '02k4b9v70',
 'fcf_________': '027xav248',
 'fct_________': '00snfqn58',
 'fmf_________': '0593mby10',
 'fwf_________': '013tf3c58',
 'hsf_________': '05tdna171',
 'ibf_________': '04jsz6e67',
 'inca________': '03m8vkq32',
 'irb_hr______': '03n51vw80',
 'irfd________': '05svhj534',
 'jaef________': '03vxy9y38',
 'kaute_______': '00zwv5854',
 'kf__________': '05jwty529',
 'lcs_________': '02ar66p97',
 'lf__________': '03hz8wd80',
 'mestd_______': '01znas443',
 'mtnf________': '047egay20',
 'mvt_________': '019pxzh98',
 'nhmrc_______': '011kf5r70',
 'nih_________': '01cwqze88',
 'nnf_________': '04txyc737',
 'nserc_______': '01h531d29',
 'nsf_________': '021nxhr62',
 'nwo_________': '04jsz6e67',
 'pf__________': '048e7gn38',
 'pnf_________': '009vp0837',
 'rcn_________': '00epmv149',
 'rcuk________': '00dq2kk65',
 'rif_________': '00en9ce74',
 'sfi_________': '0271asj38',
 'snsf________': '00yjd3n13',
 'sshrc_______': '006cvnv84',
 'sslf________': '04a31ep84',
 'tubitakf____': '04w9kkr77',
 'twcf________': '00x0z1472',
 'ukri________': '001aqnf71',
 've__________': '05nqkay65',
 'vf__________': '013w1n936',
 'wt__________': '029chgv08'}
```

---

(vocabularies-award-schemes)=
### VOCABULARIES_AWARD_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L82) |

```
{'doi': {'label': l'DOI', 'validator': <function is_doi at 0x10ae30b40>},
 'url': {'label': l'URL', 'validator': <function is_url at 0x10b453c10>}}
```

---

(vocabularies-cf)=
### VOCABULARIES_CF
| **Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | unknown |

```
[]
```

---

(vocabularies-custom-vocabulary-types)=
### VOCABULARIES_CUSTOM_VOCABULARY_TYPES
| **Invenio RDM Default Value** | `<list>` |
|--------------|-----------|
| **Type** | list |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L170) |

```
['names', 'affiliations', 'awards', 'funders', 'subjects']
```

---

(vocabularies-datastream-readers)=
### ***VOCABULARIES_DATASTREAM_READERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L179); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L747) |
| **Set by** | {py:func}`~oarepo_config.configure_datastreams`, {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'csv': <class 'invenio_vocabularies.datastreams.readers.CSVReader'>,
 'gzip': <class 'invenio_vocabularies.datastreams.readers.GzipReader'>,
 'http': <class 'invenio_vocabularies.datastreams.readers.SimpleHTTPReader'>,
 'json': <class 'invenio_vocabularies.datastreams.readers.JsonReader'>,
 'jsonl': <class 'invenio_vocabularies.datastreams.readers.JsonLinesReader'>,
 'oai-pmh': <class 'invenio_vocabularies.datastreams.readers.OAIPMHReader'>,
 'rdf': <class 'invenio_vocabularies.datastreams.readers.RDFReader'>,
 'sparql': <class 'invenio_vocabularies.datastreams.readers.SPARQLReader'>,
 'tar': <class 'invenio_vocabularies.datastreams.readers.TarReader'>,
 'xml': <class 'invenio_vocabularies.datastreams.readers.XMLReader'>,
 'yaml': <class 'invenio_vocabularies.datastreams.readers.YamlReader'>,
 'zip': <class 'invenio_vocabularies.datastreams.readers.ZipReader'>}
```

---

(vocabularies-datastream-transformers)=
### ***VOCABULARIES_DATASTREAM_TRANSFORMERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L195); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L759) |
| **Set by** | {py:func}`~oarepo_config.configure_datastreams`, {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'xml': <class 'invenio_vocabularies.datastreams.transformers.XMLTransformer'>}
```

---

(vocabularies-datastream-writers)=
### ***VOCABULARIES_DATASTREAM_WRITERS**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Sources** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L200); [invenio-app-rdm](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py#L771) |
| **Set by** | {py:func}`~oarepo_config.configure_datastreams`, {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'async': <class 'invenio_vocabularies.datastreams.writers.AsyncWriter'>,
 'service': <class 'invenio_vocabularies.datastreams.writers.ServiceWriter'>,
 'yaml': <class 'invenio_vocabularies.datastreams.writers.YamlWriter'>}
```

---

(vocabularies-facet-cache-size)=
### VOCABULARIES_FACET_CACHE_SIZE
| **OARepo Default Value** | `2048` |
|--------------|-----------|
| **Type** | int |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L44) |

---

(vocabularies-facet-cache-ttl)=
### VOCABULARIES_FACET_CACHE_TTL
| **OARepo Default Value** | `34560` |
|--------------|-----------|
| **Type** | int |
| **Source** | [oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies/blob/master/oarepo_vocabularies/config.py#L45) |

---

(vocabularies-funder-doi-prefix)=
### VOCABULARIES_FUNDER_DOI_PREFIX

```{eval-rst}
DOI prefix for the identifier formed with the FundRef id.
```

| **Invenio RDM Default Value** | `'10.13039'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L79) |

---

(vocabularies-funder-schemes)=
### ***VOCABULARIES_FUNDER_SCHEMES**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L73) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'doi': {'label': l'DOI', 'validator': <function is_doi at 0x10ae30b40>},
 'gnd': {'label': l'GND', 'validator': <function is_gnd at 0x10b4ac3b0>},
 'grid': {'label': l'GRID', 'validator': <function <lambda> at 0x10df5e350>},
 'isni': {'label': l'ISNI', 'validator': <function is_isni at 0x10b453950>},
 'ror': {'label': l'ROR', 'validator': <function is_ror at 0x10b4ace00>}}
```

---

(vocabularies-identifier-schemes)=
### VOCABULARIES_IDENTIFIER_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L43) |

```
{'gnd': {'label': l'GND', 'validator': <function is_gnd at 0x10b4ac3b0>},
 'grid': {'label': l'GRID', 'validator': <function <lambda> at 0x10df5e350>},
 'isni': {'label': l'ISNI', 'validator': <function is_isni at 0x10b453950>},
 'ror': {'label': l'ROR', 'validator': <function is_ror at 0x10b4ace00>}}
```

---

(vocabularies-names-schemes)=
### ***VOCABULARIES_NAMES_SCHEMES**
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L157) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

```
{'gnd': {'datacite': 'GND',
         'label': l'GND',
         'validator': <function is_gnd at 0x10b4ac3b0>},
 'isni': {'datacite': 'ISNI',
          'label': l'ISNI',
          'validator': <function is_isni at 0x10b453950>},
 'orcid': {'datacite': 'ORCID',
           'label': l'ORCID',
           'validator': <function is_orcid at 0x10b453a00>}}
```

---

(vocabularies-orcid-access-key)=
### VOCABULARIES_ORCID_ACCESS_KEY

```{eval-rst}
ORCID access key to access the s3 bucket.
```

| **Invenio RDM Default Value** | `'CHANGEME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L241) |

---

(vocabularies-orcid-org-ids-mapping-path)=
### VOCABULARIES_ORCID_ORG_IDS_MAPPING_PATH

```{eval-rst}
Path to the CSV file for mapping ORCiD organization IDs to affiliation IDs.

The path can be specified as either an absolute path or a relative path within the
Flask app instance folder (i.e. ``current_app.instance_path``).

The CSV file should have the following columns:

- `org_scheme`: The ORCiD organization ID.
- `org_id`: The ORCiD organization ID.
- `aff_id`: The affiliation ID to map to.
```

| **Invenio RDM Default Value** | `None` |
|--------------|-----------|
| **Type** | NoneType |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L254) |

---

(vocabularies-orcid-secret-key)=
### VOCABULARIES_ORCID_SECRET_KEY

```{eval-rst}
ORCID secret key to access the s3 bucket.
```

| **Invenio RDM Default Value** | `'CHANGEME'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L243) |

---

(vocabularies-orcid-summaries-bucket)=
### VOCABULARIES_ORCID_SUMMARIES_BUCKET

```{eval-rst}
ORCID summaries bucket name.
```

| **Invenio RDM Default Value** | `'v3.0-summaries'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L245) |

---

(vocabularies-orcid-sync-max-workers)=
### VOCABULARIES_ORCID_SYNC_MAX_WORKERS

```{eval-rst}
ORCID max number of simultaneous workers/connections.
```

| **Invenio RDM Default Value** | `32` |
|--------------|-----------|
| **Type** | int |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L247) |

---

(vocabularies-orcid-sync-since)=
### VOCABULARIES_ORCID_SYNC_SINCE
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L249) |

```
{'days': 1}
```

---

(vocabularies-resource-config)=
### ***VOCABULARIES_RESOURCE_CONFIG**

```{eval-rst}
Configure the resource.
```

| **Invenio RDM Default Value** | `VocabulariesResourceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L37) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(vocabularies-service-config)=
### ***VOCABULARIES_SERVICE_CONFIG**

```{eval-rst}
Configure the service.
```

| **Invenio RDM Default Value** | `VocabulariesServiceConfig` |
|--------------|-----------|
| **Type** | unknown |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L40) |
| **Set by** | {py:func}`~oarepo_config.configure_generic_parameters` |

---

(vocabularies-subjects-euroscivoc-file-url)=
### VOCABULARIES_SUBJECTS_EUROSCIVOC_FILE_URL

```{eval-rst}
Subject EuroSciVoc file download link.
```

| **Invenio RDM Default Value** | `'https://publications.europa.eu/resource/distribution/euroscivoc/rdf/skos_ap_eu/EuroSciVoc-skos-ap-e...` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L225) |

---

(vocabularies-subjects-gemet-file-url)=
### VOCABULARIES_SUBJECTS_GEMET_FILE_URL
| **Invenio RDM Default Value** | `'https://www.eionet.europa.eu/gemet/latest/gemet.rdf.gz'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L228) |

---

(vocabularies-subjects-nvs-file-url)=
### VOCABULARIES_SUBJECTS_NVS_FILE_URL

```{eval-rst}
Subject NVS-P02 file download link.
```

| **Invenio RDM Default Value** | `'http://vocab.nerc.ac.uk/collection/P02/current/?_profile=nvs&_mediatype=application/rdf+xml'` |
|--------------|-----------|
| **Type** | str |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L233) |

---

(vocabularies-subjects-schemes)=
### VOCABULARIES_SUBJECTS_SCHEMES
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L164) |

```
{'gnd': {'datacite': 'GND',
         'label': l'GND',
         'validator': <function is_gnd at 0x10b4ac3b0>},
 'url': {'label': l'URL', 'validator': <function is_url at 0x10b453c10>}}
```

---

(vocabularies-types-search)=
### VOCABULARIES_TYPES_SEARCH
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L219) |

```
{'facets': [], 'sort': ['name', 'count']}
```

---

(vocabularies-types-sort-options)=
### VOCABULARIES_TYPES_SORT_OPTIONS
| **Invenio RDM Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | [invenio-vocabularies](https://github.com/inveniosoftware/invenio-vocabularies/blob/master/invenio_vocabularies/config.py#L207) |

```
{'count': {'fields': ['count'], 'title': l'Number of entries'},
 'name': {'fields': ['id'], 'title': l'Name'}}
```

---

(vocabulary-type-ui-resource)=
### VOCABULARY_TYPE_UI_RESOURCE
| **Default Value** | `'oarepo_vocabularies.ui.resources.vocabulary_type.resource:VocabularyTypeUIResource'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(vocabulary-type-ui-resource-config)=
### VOCABULARY_TYPE_UI_RESOURCE_CONFIG
| **Default Value** | `'oarepo_vocabularies.ui.resources.vocabulary_type.config:VocabularyTypeUIResourceConfig'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(webpackext-manifest-path)=
### WEBPACKEXT_MANIFEST_PATH
| **Default Value** | `'dist/manifest.json'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(webpackext-npm-pkg-cls)=
### ***WEBPACKEXT_NPM_PKG_CLS**
| **Type** | configured by function |
|--------------|-----------|
| **Source** | [oarepo-config](https://github.com/oarepo/oarepo-config/blob/master/oarepo_config/ui.py#L25) |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(webpackext-project)=
### ***WEBPACKEXT_PROJECT**
| **Default Value** | `'oarepo_ui.webpack:project'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |
| **Set by** | {py:func}`~oarepo_config.configure_ui` |

---

(webpackext-project-builddir)=
### WEBPACKEXT_PROJECT_BUILDDIR
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/assets'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(webpackext-project-distdir)=
### WEBPACKEXT_PROJECT_DISTDIR
| **Default Value** | `'/Users/m/Workspaces/repositories/feat-convert-old-catchall/oarepo-config/.venv/var/instance/static/...` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(webpackext-project-disturl)=
### WEBPACKEXT_PROJECT_DISTURL
| **Default Value** | `'/static/dist'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

(workflows)=
### WORKFLOWS
| **Default Value** | `<dict>` |
|--------------|-----------|
| **Type** | dict |
| **Source** | unknown |

```
{}
```

---

(workflows-default-workflow)=
### WORKFLOWS_DEFAULT_WORKFLOW
| **Default Value** | `'individual'` |
|--------------|-----------|
| **Type** | str |
| **Source** | unknown |

---

