# Guide

Reference material that doesn't fit on the [front page](index.md): how
configuration values are loaded, the order to call functions in, the
full list of environment variables, a full example `invenio.cfg`, how
the package works internally, and known gaps. For a one-line-per-function
summary with links into the {doc}`API reference <api>`, see the
[front page](index.md).

## Configuration sources and precedence

This section is for whoever **deploys/operates** an instance (sets up
`variables`, `.env`, or the process environment) — for how
`invenio.cfg` itself *consumes* these values in code, see
[Reading configuration variables in invenio.cfg](#reading-configuration-variables-in-invenio-cfg)
further down.

Several functions (`configure_generic_parameters`, `configure_ui`,
`configure_einfra_oidc`) pull values from the environment via
`load_configuration_variables()`. Values are merged from multiple sources,
**lowest to highest priority**:

1. A `variables` file located next to `invenio.cfg` itself (i.e. in the
   Invenio instance directory — found via `INVENIO_INSTANCE_PATH` if set,
   otherwise by walking the call stack for a frame whose filename ends in
   `invenio.cfg`).
2. A `variables` file in the current working directory (conventionally the
   repository root you run commands from).
3. A `.env` file in the current working directory (overrides `variables`).
4. If `INVENIO_CONFIG_PATH` is set, every `*.json` / `*.yaml` / `*.yml`
   file found recursively under that directory, processed in alphabetical
   path order. Keys are upper-cased and prefixed with `INVENIO_` if not
   already prefixed.
5. Actual process environment variables starting with `INVENIO_` (highest
   priority — always wins).

Every value is passed through `transform_value()`: the literal strings
`"True"`/`"False"` become booleans, and anything that parses as JSON
(numbers, `[...]`, `{...}`, quoted strings) is converted; otherwise the
raw string is kept. This matters when editing `variables`/`.env` by hand —
e.g. `INVENIO_S3_ACCESS_KEY=aa` stays the string `"aa"`, but
`INVENIO_OPENSEARCH_USE_SSL=False` becomes the Python boolean `False`, and
`INVENIO_SOME_LIST=["a", "b"]` becomes an actual list.

## Reading configuration variables in invenio.cfg

This section is for whoever **writes/maintains** `invenio.cfg` or other
`configure_*()` helpers — for the on-disk/env-var precedence rules an
operator needs to know, see
[Configuration sources and precedence](#configuration-sources-and-precedence)
above.

`load_configuration_variables()` returns a dict-with-attribute-access.
**Accessing a missing variable as an attribute (`env.INVENIO_SECRET_KEY`)
raises `AttributeError`** — so any variable a `configure_*()` function
reads without a `.get(..., default)` fallback is effectively **required**.
Keep this in mind if you write your own `configure_*()`-style helper:
prefer `env.get("INVENIO_FOO", default)` for optional settings, and plain
attribute access only for settings the deployment must provide.

`override_configuration(env=None)` is a separate, opt-in escape hatch: for
every loaded variable named `INVENIO_<X>`, it strips the `INVENIO_` prefix
and sets `<X>` directly as a config constant in `invenio.cfg` — i.e. it
lets ops set arbitrary Flask config keys (e.g.
`INVENIO_RDM_ARCHIVE_DOWNLOAD_ENABLED=false` in `variables`/`.env`) without
touching Python code. It is not called automatically by anything else in
this package; call it yourself (typically last, so it wins over everything
set by `configure_*()` calls above it) if you want that behaviour.

## Ordering

Because several functions read back constants set by earlier ones, a safe
call order in `invenio.cfg` is:

1. `initialize_i18n()` / `initialize_glitchtip()` (no dependencies)
2. `configure_generic_parameters()` (seeds `APP_DEFAULT_SECURE_HEADERS`,
   vocabulary schemes, datastream readers/writers/transformers)
3. `configure_ui()` (extends `APP_DEFAULT_SECURE_HEADERS`, sets
   `REPOSITORY_NAME`)
4. `configure_oai()` (needs `REPOSITORY_NAME`)
5. `configure_communities()`, `configure_workflows()` (or the low-level
   `register_workflow()`), `configure_cron()`,
   `configure_stats()`, `configure_vocabulary()`,
   `configure_datastreams()`, `configure_jobs()`,
   `configure_einfra_oidc()`, `configure_llm()`, `add_model()` — order
   among these mostly doesn't matter, except that anything relying on
   `VOCABULARIES_DATASTREAM_*` defaults should still come after step 2.
6. Any plain `CONSTANT = value` overrides, and `override_configuration()`
   if used, last — so they win over everything above.

## Environment variables

Consumed via `load_configuration_variables()` (see loading order above).
Required unless noted otherwise — accessing a required-but-unset variable
raises `AttributeError` when `invenio.cfg` is imported.

| Variable | Used by | Notes |
|---|---|---|
| `INVENIO_SECRET_KEY` | `configure_generic_parameters` | Flask `SECRET_KEY` |
| `INVENIO_UI_HOST`, `INVENIO_UI_PORT` | `configure_generic_parameters` | fallback for `SITE_UI_URL` if `INVENIO_SITE_UI_URL` unset |
| `INVENIO_API_HOST`, `INVENIO_API_PORT` | `configure_generic_parameters` | fallback for `SITE_API_URL` if `INVENIO_SITE_API_URL` unset |
| `INVENIO_SITE_UI_URL`, `INVENIO_SITE_API_URL` | `configure_generic_parameters` | optional, overrides host/port composition |
| `INVENIO_DATABASE_USER/PASSWORD/HOST/PORT/DBNAME` | `configure_generic_parameters` | fallback for `SQLALCHEMY_DATABASE_URI` |
| `INVENIO_SQLALCHEMY_DATABASE_URI` | `configure_generic_parameters` | optional, overrides the above |
| `INVENIO_S3_PROTOCOL/HOST/PORT` | `configure_generic_parameters` | fallback for `S3_ENDPOINT_URL` |
| `INVENIO_S3_ENDPOINT_URL` | `configure_generic_parameters` | optional, overrides the above |
| `INVENIO_S3_ACCESS_KEY`, `INVENIO_S3_SECRET_KEY` | `configure_generic_parameters` | required, min length enforced by MinIO/S3 itself |
| `INVENIO_OPENSEARCH_HOST/PORT` | `configure_generic_parameters` | `SEARCH_HOSTS` |
| `INVENIO_OPENSEARCH_USE_SSL/VERIFY_CERTS/ASSERT_HOSTNAME/SHOW_WARN` | `configure_generic_parameters` | `SEARCH_CLIENT_CONFIG` |
| `INVENIO_OPENSEARCH_CA_CERTS_PATH` | `configure_generic_parameters` | optional |
| `INVENIO_SEARCH_INDEX_PREFIX` | `configure_generic_parameters` | required |
| `INVENIO_REDIS_HOST`, `INVENIO_REDIS_PORT` | `configure_generic_parameters` | required |
| `INVENIO_REDIS_CACHE_DB` | `configure_generic_parameters` | fallback for `CACHE_REDIS_URL` |
| `INVENIO_REDIS_SESSION_DB` | `configure_generic_parameters` | fallback for `ACCOUNTS_SESSION_REDIS_URL` |
| `INVENIO_REDIS_COMMUNITIES_CACHE_DB` | `configure_generic_parameters` | fallback for `COMMUNITIES_IDENTITIES_CACHE_REDIS_URL` |
| `INVENIO_REDIS_CELERY_RESULT_DB` | `configure_generic_parameters` | fallback for `CELERY_RESULT_BACKEND` |
| `INVENIO_CACHE_REDIS_URL`, `INVENIO_ACCOUNTS_SESSION_REDIS_URL`, `INVENIO_COMMUNITIES_IDENTITIES_CACHE_REDIS_URL`, `INVENIO_CELERY_RESULT_BACKEND` | `configure_generic_parameters` | optional, override the `INVENIO_REDIS_*_DB` composition above |
| `INVENIO_RABBIT_USER/PASSWORD/HOST/PORT` | `configure_generic_parameters` | fallback for `CELERY_BROKER_URL` |
| `INVENIO_CELERY_BROKER_URL` | `configure_generic_parameters` | optional, overrides the above |
| `INVENIO_ACCOUNTS_LOCAL_LOGIN_ENABLED` | `configure_generic_parameters` | required |
| `INVENIO_SECURITY_REGISTERABLE/RECOVERABLE/CHANGEABLE/CONFIRMABLE/LOGIN_WITHOUT_CONFIRMATION` | `configure_generic_parameters` | required |
| `INVENIO_MAIL_DEFAULT_SENDER` | `configure_generic_parameters` | optional (defaults to a placeholder test address) |
| `INVENIO_MAIL_SUPPRESS_SEND` | `configure_generic_parameters` | optional |
| `INVENIO_DEPLOYMENT_VERSION` | `configure_ui` | optional, defaults to `"local development"`; also gates whether Matomo analytics is wired up |
| `INVENIO_MATOMO_ANALYTICS_URL`, `INVENIO_MATOMO_ANALYTICS_SITE_ID` | `configure_ui` | required only if `analytics="matomo"` and not local dev |
| `INVENIO_REMOTE_AUTH_ENABLED` | `configure_einfra_oidc` | optional, default disabled |
| `INVENIO_EINFRA_CONSUMER_KEY`, `INVENIO_EINFRA_CONSUMER_SECRET` | `configure_einfra_oidc` | required only if e-INFRA login is enabled |
| `INVENIO_CONFIG_PATH` | `load_configuration_overrides` | optional, extra directory of `.json`/`.yaml`/`.yml` overrides |
| `INVENIO_INSTANCE_PATH` | `load_configuration_variables` | optional, explicit path to the instance dir containing `invenio.cfg`/`variables` |

## `initial_configuration.py` / `initial_rdm_config.py`

Two additional modules ship plain module-level constants rather than
`configure_*()` functions:

* `oarepo_config.initial_configuration` — currently just
  `THEME_FRONTPAGE = False`.
* `oarepo_config.initial_rdm_config` — a large block of RDM/OAI-PMH
  defaults (OAI server fetchers/classes, dashboard/communities/requests
  routes, citation styles incl. `iso690-author-date-cs`, person/org and
  identifier schemes incl. `scopusid`/`researcherid`/`vedidk`/`ico`, IIIF
  preview settings, etc.) intended to replace pieces of
  `invenio-app-rdm`'s own defaults.

## Full example

Adapted from a production `invenio.cfg` (CESNET catch-all data
repository), showing most of the functions together:

```python
import oarepo_config as config
from invenio_i18n import lazy_gettext as _

config.initialize_i18n()

config.configure_generic_parameters(
    languages=(("cs", _("Czech")),),
)

config.configure_ui(
    code="datarepo",
    name=_("CESNET Data Repository"),
    description=_("Catch-all repository for Czech scientific data"),
)

config.configure_communities(
    communities_roles=[
        dict(
            name="owner",
            title=_("Community owner"),
            is_owner=True,
            can_manage=True,
            can_curate=True,
            can_manage_roles=["owner", "curator", "member", "submitter"],
        ),
        dict(
            name="curator",
            title=_("Curator"),
            can_manage=True,
            can_curate=True,
            can_manage_roles=["member", "submitter"],
        ),
        dict(name="submitter", title=_("Submitter"), can_manage=True, can_manage_roles=[]),
        dict(name="member", title=_("Member")),
    ]
)

# Preferred, higher-level workflow helper - builds the same "WORKFLOWS"
# constant that the low-level register_workflow() would populate directly,
# from IndividualWorkflow()/CommunityWorkflow() definitions instead.
config.configure_workflows(
    config.IndividualWorkflow(
        publish_without_review=False,
        review_required=True,
        self_review_enabled=True,
        draft_creation_roles=["submitter"],
        publish_without_review_roles=["direct-publisher"],
    ),
    config.CommunityWorkflow(
        code="community",
        label=_("Default Community Workflow"),
        community_curator_roles=["curator", "owner"],
    ),
)

config.configure_cron()
config.configure_stats()

# custom model, registered separately from GLOBAL_SEARCH_MODELS
from datasets import datasets_model

datasets_model.register()

# e-INFRA OIDC login, toggled by INVENIO_REMOTE_AUTH_ENABLED
env = config.load_configuration_variables()
if env.get("INVENIO_REMOTE_AUTH_ENABLED", "no").lower() in ("true", "yes", "1"):
    config.configure_einfra_oidc()

# AI-assisted record validation (oarepo-checks), optional - only configured
# if a token is available
if env.get("INVENIO_LLM_API_TOKEN"):
    config.configure_llm(api_token=env["INVENIO_LLM_API_TOKEN"])

# plain overrides after all config.* calls
RDM_RECORDS_MAX_FILES_COUNT = 100
RDM_FILES_DEFAULT_QUOTA_SIZE = 1000 * (10**9)
```

## How it works internally: functions that write to your module

Every `configure_*()` / `initialize_*()` / `register_*()` function ends by
calling an internal helper, `set_constants_in_caller()`, which walks two
stack frames up (past itself and past the `configure_*` function) and
assigns every UPPERCASE `local()` variable of that function directly into
the **globals of the module that called it**. In practice that module is
always `invenio.cfg`.

```python
import oarepo_config as config

config.configure_ui(code="myrepo", name="My Repository")
# is roughly equivalent to writing, by hand, all of:
#   APP_THEME = [...]
#   THEME_SITENAME = ...
#   REPOSITORY_NAME = ...
#   ... etc.
# directly at module level in invenio.cfg
```

Three consequences of this design that matter when using the package:

* **Call these functions directly from `invenio.cfg`** (at module level, or
  from a function that is itself *defined inside* `invenio.cfg`). Wrapping
  a call in a helper function that lives in a different importable module
  will make the constants land in the wrong module's globals, because the
  frame lookup targets whichever module's frame is two levels up.
* Functions that build on top of previously-set constants
  (`configure_oai()` needs `REPOSITORY_NAME`, `configure_ui()` extends
  `APP_DEFAULT_SECURE_HEADERS`) read them back via
  `get_constant_from_caller(name, default)` — so **call order in
  `invenio.cfg` matters**. See [Ordering](#ordering) above.
* Dict/list/set-valued constants that already exist are extended rather
  than clobbered, via `merge_with_caller(name, value)` — dicts are shallow
  merged (new keys win), sequences are concatenated, sets are unioned. This
  lets you pre-declare a partial `CELERY_BEAT_SCHEDULE` or
  `OAUTHCLIENT_REMOTE_APPS` before calling the relevant `configure_*()` and
  have it combined with the defaults instead of overwritten.
