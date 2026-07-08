# oarepo-config

Helper library for writing a clean, high-level `invenio.cfg` for
[OARepo](https://github.com/oarepo/oarepo)/Invenio-RDM based repositories.

Instead of hand-assembling dozens of loosely related Flask/Invenio config
constants, `invenio.cfg` calls a small number of `configure_*()` functions.
Each function computes a group of related constants (reading values from
the environment where necessary) and injects them **directly into the
global namespace of `invenio.cfg`** — as if you had written
`SOME_CONSTANT = ...` yourself. This keeps `invenio.cfg` short and
declarative while still producing a normal, fully introspectable Invenio
config module.

## Installation

```bash
pip install oarepo-config
```

It is normally pulled in transitively as part of an `oarepo-app`
installation, but can also be used standalone. Requires Python 3.14 and
`oarepo[rdm,tests]` 14.x (see `pyproject.toml`).

## Configuration sources and precedence

This section is for whoever **deploys/operates** an instance (sets up
`variables`, `.env`, or the process environment) — for how
`invenio.cfg` itself *consumes* these values in code, see
[Reading configuration variables in `invenio.cfg`](#reading-configuration-variables-in-invenio.cfg)
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

## Quick start

```python
# invenio.cfg
import oarepo_config as config
from invenio_i18n import lazy_gettext as _

# i18n helpers (marshmallow error messages, etc.)
config.initialize_i18n()

config.configure_generic_parameters(
    languages=(("cs", _("Czech")),),
)

config.configure_ui(
    code="myrepo",
    name=_("My Repository"),
    description=_("Description of my repository"),
)

config.configure_communities()

config.configure_cron()

config.configure_stats()

# Feel free to add/override plain CONFIG_VARIABLE = value assignments
# below, or wrap them with config.override_configuration() to source them
# from the environment.
```

## Function reference

### `initialize_i18n`

```python
initialize_i18n()
```

Patches Marshmallow so validation error messages go through
`flask_babel.lazy_gettext`, enabling translated API error responses. No
arguments, no config constants set — call once, early.

### `initialize_glitchtip`

```python
initialize_glitchtip(dsn: str | None = None, deployment_version: str | None = None)
```

Wires up [Glitchtip](https://glitchtip.com/) (Sentry-compatible) error
reporting. Requires the optional `oarepo-glitchtip` package; if it is not
installed, calling this raises `ImportError`. (In the CESNET data
repository this is currently disabled in `invenio.cfg` — commented out —
because of a Sentry SDK / Python version incompatibility, see
[inveniosoftware/invenio-logging#73](https://github.com/inveniosoftware/invenio-logging/issues/73).)

### `configure_generic_parameters`

```python
configure_generic_parameters(
    languages=(("cs", _("Czech")),),
    use_path_pid_ids=False,
)
```

The big one — sets the bulk of infrastructure-level Flask/Invenio config:
hosts/URLs, security headers, local-login/security feature flags, the
SQLAlchemy DB URI, i18n locale/timezone, S3/file storage, OpenSearch
connection & index prefix, Redis-backed caches (app cache, session cache,
communities-identities cache), Celery broker/result backend, the secret
key, DataCite test mode, mail sender, default identifier/name/affiliation/
funder vocabulary schemes, and deposit form file quotas.

Parameters:
* `languages` — tuple of `(code, lazy label)` pairs for
  `I18N_LANGUAGES` (English is added separately by Invenio itself).
* `use_path_pid_ids` — if `True`, patches several `RDM*ResourceConfig`
  classes' `url_prefix` to accept `<path:pid_value>` instead of the
  default converter, for PIDs that themselves contain slashes.

Reads (via `load_configuration_variables()`) — see the
[environment variables](#environment-variables) table below for the full
list; most notably `INVENIO_SECRET_KEY`, `INVENIO_DATABASE_*`,
`INVENIO_S3_*`, `INVENIO_OPENSEARCH_*`, `INVENIO_REDIS_*`,
`INVENIO_RABBIT_*`.

Should generally be called **first**, since it seeds
`APP_DEFAULT_SECURE_HEADERS` and the `VOCABULARIES_*_SCHEMES` /
`VOCABULARIES_DATASTREAM_*` dicts that other functions (`configure_ui`,
`configure_datastreams`) extend.

### `configure_ui`

```python
configure_ui(
    code="myrepo",
    name=_("My Repository"),
    subtitle="",
    description="",
    support_contact="",
    keywords="",
    use_default_frontpage=False,
    show_frontpage_intro=True,
    analytics=False,
    languages=(("cs", _("Czech")),),
)
```

Branding, theme and front-end wiring: `APP_THEME`, site name/title/
description/keywords (`REPOSITORY_NAME`, `REPOSITORY_DESCRIPTION`, ...),
frontpage visibility, template overrides, the pnpm/rspack asset build
pipeline, the record-detail sidebar layout, and (if
`analytics="matomo"` and not running as `"local development"`) Matomo
tracking, which requires `INVENIO_MATOMO_ANALYTICS_URL` and
`INVENIO_MATOMO_ANALYTICS_SITE_ID` to be set.

Also appends the licensebuttons.net origin to the `content_security_policy`
built by `configure_generic_parameters()` — **call
`configure_generic_parameters()` before `configure_ui()`**, otherwise this
silently extends an empty dict.

`REPOSITORY_NAME` set here is later required by `configure_oai()`.

### `configure_communities`

```python
configure_communities(communities_roles=None)
```

Sets `COMMUNITIES_REGISTER_UI_BLUEPRINT = True`, a
`COMMUNITIES_PERMISSION_POLICY` (a workflow-aware policy if
`oarepo_communities`/`oarepo_workflows` are installed, otherwise the plain
Invenio default), and `COMMUNITIES_ROLES`.

`communities_roles` lets you fully replace the default 3-role list
(`owner` / `curator` / `member`) with your own — pass a list of dicts with
`name`, `title`, `description`, and the `is_owner` / `can_manage` /
`can_curate` / `can_manage_roles` flags Invenio-Communities expects. The
CESNET data repository, for example, adds a fourth `submitter` role and
lets `owner` manage roles below it (see the example at the bottom).

### `register_workflow`

```python
register_workflow(
    workflow_code: str,
    workflow_name: str | LazyString,
    permissions_policy: str | DefaultWorkflowPermissions,
    requests_policy: str | WorkflowRequestPolicy,
)
```

Low-level, single-workflow registration primitive provided directly by
this package. Requires `oarepo_workflows` (and `oarepo_requests` for the
default `REQUESTS_PERMISSION_POLICY`) to be installed. Appends one
`Workflow(...)` entry to `WORKFLOWS` and defaults
`REQUESTS_PERMISSION_POLICY` to
`CreatorsFromWorkflowRequestsPermissionPolicy` if not already set.

`permissions_policy` / `requests_policy` accept either an
import-path string or the class object itself; each is validated to be a
subclass of `DefaultWorkflowPermissions` / `WorkflowRequestPolicy`
respectively.

> **Note:** this is *not* the API used in the CESNET data repository's
> `invenio.cfg`. That repository instead uses the higher-level
> `configure_workflows(IndividualWorkflow(...), CommunityWorkflow(...))`
> helper from the separate `oarepo_app.config` package, which builds on
> top of the same `WORKFLOWS` constant. Use whichever fits — `register_workflow`
> if you need one-off, fully custom workflows; `oarepo_app`'s
> `configure_workflows` if the individual/community workflow shape it
> models fits your repository.

### `configure_cron`

```python
configure_cron(**extra_cron_items)
```

Sets `CELERY_BEAT_SCHEDULE`, merged (via `merge_with_caller`) on top of
any `CELERY_BEAT_SCHEDULE` you already defined earlier in `invenio.cfg`.
Ships with sensible defaults: indexer queue management (every 10s),
session/IP cleanup, stats event processing/aggregation, daily
communities-cache clearing, and expired access-request-token cleanup.
Pass additional `name=schedule_dict` keyword arguments to add your own
periodic tasks, or override a default entry by passing the same key.

### `configure_stats`

```python
configure_stats(enable: bool = True)
```

Sets `STATS_REGISTER_RECEIVERS = enable` (toggles whether stats event
receivers are wired up) and always pulls in the default
`STATS_EVENTS` / `STATS_AGGREGATIONS` / `STATS_QUERIES` /
`STATS_PERMISSION_FACTORY` from `invenio_app_rdm.config` — those four are
set regardless of `enable`.

### `configure_vocabulary`

```python
configure_vocabulary(code: str, **kwargs)
```

Adds one entry to `INVENIO_VOCABULARY_TYPE_METADATA[code] = kwargs`,
merging into (rather than replacing) whatever was set by previous calls.
Call once per custom vocabulary type. `kwargs` typically include
`name`, `description`, and `props` describing the vocabulary's extra
fields for the UI/admin forms — see the
[OARepo reference docs](https://nrp-cz.github.io/docs/customize/configure/reference#configure_vocabulary)
for the full shape.

```python
config.configure_vocabulary(
    code="languages",
    name=_("Languages"),
    description=_("Language definitions vocabulary."),
    props={
        "alpha3Code": {
            "description": _("ISO 639-2 standard 3-letter language code"),
            "label": _("Alpha3 code (English)"),
            "multiple": False,
            "placeholder": "eng, cze...",
            "search": False,
        },
    },
    dump_options=True,
)
```

### `configure_datastreams`

```python
configure_datastreams(
    readers: dict[str, Any] | None = None,
    writers: dict[str, Any] | None = None,
    transformers: dict[str, Any] | None = None,
)
```

Registers custom vocabulary-datastream readers/writers/transformers
(used by `invenio vocabularies import` style fixture loading). Each dict
value may be an import-path string or the object itself — resolved via
`obj_or_import_string`. Results are merged into
`VOCABULARIES_DATASTREAM_READERS` / `_WRITERS` / `_TRANSFORMERS`, which
`configure_generic_parameters()` seeds with `invenio_app_rdm`'s defaults —
call `configure_generic_parameters()` first if you rely on those defaults
still being present.

### `configure_jobs`

```python
configure_jobs(permission_policy=None, logging_level=None)
```

Configures `invenio-jobs`: `APP_LOGS_PERMISSION_POLICY` (defaults to an
administration-only policy requiring `oarepo_runtime`) and
`JOBS_LOGGING_LEVEL` (defaults to `"INFO"`).

### `configure_oai`

```python
configure_oai()
```

Sets `OAISERVER_REPOSITORY_NAME` from the already-configured
`REPOSITORY_NAME`. **Must be called after `configure_ui()`** — it reads
`REPOSITORY_NAME` back via `get_constant_from_caller()` and raises
`ValueError("REPOSITORY_NAME must be set, please configure UI before configuring OAI.")`
if it isn't set yet. Takes no other arguments; most other OAI-PMH
settings (`OAISERVER_ID_FETCHER`, `OAISERVER_RECORD_CLS`, etc.) live in
`initial_rdm_config.py` instead (see
[below](#initial_configurationpy--initial_rdm_configpy)).

### `configure_einfra_oidc`

```python
configure_einfra_oidc()
```

Wires up login via CESNET e-INFRA (Perun) OIDC. Requires the optional
`oarepo-oidc-einfra` package — if missing, this **prints a message and
calls `sys.exit(1)`** (a hard process exit, not an exception) rather than
failing gracefully, so only call it where that dependency is guaranteed to
be installed, or guard the call yourself.

Behaviour is controlled by `INVENIO_REMOTE_AUTH_ENABLED` (`true`/`yes`/`1`,
case-insensitive):
* **enabled** — registers the `e-infra` entry in `OAUTHCLIENT_REMOTE_APPS`
  (merged with anything already there), builds an `EINFRA` config dict
  from `INVENIO_EINFRA_CONSUMER_KEY` / `INVENIO_EINFRA_CONSUMER_SECRET`
  plus every `EINFRA_*` constant exported by
  `oarepo_oidc_einfra.config`, and forces `USERPROFILES_READ_ONLY = True`
  (profile data is sourced from e-INFRA, not editable locally).
* **disabled** (default) — `OAUTHCLIENT_REMOTE_APPS` is left as-is
  (merged with an empty dict, i.e. a no-op).

### `add_model`

```python
add_model(model_package_name: str)
```

Registers a compiled OARepo data model for global/cross-model search.
Imports `MODEL_DEFINITION` from `<model_package_name>` and appends it to
`GLOBAL_SEARCH_MODELS`. If the import fails (e.g. the model package hasn't
been generated/compiled yet), the failure is only **logged as an error**,
not raised — `invenio.cfg` will still load successfully, just without that
model registered for global search. This is distinct from actually
registering the model's blueprints/services, which model packages
typically do themselves via `<model>.register()` (see the
`datasets_model.register()` call in the example below) — `add_model()`
only affects the `GLOBAL_SEARCH_MODELS` cross-model search list.

### `load_configuration_variables` / `override_configuration`

```python
load_configuration_variables() -> DictWithGetAttr
override_configuration(env: dict[str, Any] | None = None) -> None
```

See [Configuration sources and precedence](#configuration-sources-and-precedence)
and [Reading configuration variables in `invenio.cfg`](#reading-configuration-variables-in-invenio.cfg).

## Ordering

Because several functions read back constants set by earlier ones, a safe
call order in `invenio.cfg` is:

1. `initialize_i18n()` / `initialize_glitchtip()` (no dependencies)
2. `configure_generic_parameters()` (seeds `APP_DEFAULT_SECURE_HEADERS`,
   vocabulary schemes, datastream readers/writers/transformers)
3. `configure_ui()` (extends `APP_DEFAULT_SECURE_HEADERS`, sets
   `REPOSITORY_NAME`)
4. `configure_oai()` (needs `REPOSITORY_NAME`)
5. `configure_communities()`, workflow registration, `configure_cron()`,
   `configure_stats()`, `configure_vocabulary()`,
   `configure_datastreams()`, `configure_jobs()`,
   `configure_einfra_oidc()`, `add_model()` — order among these mostly
   doesn't matter, except that anything relying on
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

## Reading configuration variables in `invenio.cfg`

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

Upstream (inside the `oarepo` metapackage, where this code originally
lived as `oarepo.config`), these two modules are registered as
`invenio_config.module` entry points and load automatically before
`invenio.cfg` itself, at `[invenio_config.module] oarepo = ...` /
`invenio_app_rdm = ...`. **As of this standalone `oarepo-config` package,
`pyproject.toml` does not yet declare that `[project.entry-points]`
section**, so these two modules are not currently wired up to load
automatically — if you need their constants, import them explicitly from
`invenio.cfg` (`from oarepo_config.initial_rdm_config import *`, or
individual names) until the entry points are added.

## Full example

Adapted from a production `invenio.cfg` (CESNET catch-all data
repository), showing most of the functions together:

```python
import oarepo_config as config
from invenio_i18n import lazy_gettext as _
from oarepo_app.config import CommunityWorkflow, IndividualWorkflow, configure_workflows

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
        dict(name="owner", title=_("Community owner"), is_owner=True,
             can_manage=True, can_curate=True,
             can_manage_roles=["owner", "curator", "member", "submitter"]),
        dict(name="curator", title=_("Curator"), can_manage=True,
             can_curate=True, can_manage_roles=["member", "submitter"]),
        dict(name="submitter", title=_("Submitter"), can_manage=True,
             can_manage_roles=[]),
        dict(name="member", title=_("Member")),
    ]
)

# Higher-level workflow helper from oarepo_app, built on the same
# WORKFLOWS constant that register_workflow() would populate directly.
configure_workflows(
    IndividualWorkflow(
        publish_without_review=False,
        review_required=True,
        self_review_enabled=True,
        draft_creation_roles=["submitter"],
        publish_without_review_roles=["direct-publisher"],
    ),
    CommunityWorkflow(
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

## Known gaps (as of this package's initial extraction from `oarepo`)

These are observations from reading the current source, useful if you're
picking up the standalone-package conversion work:

* `oarepo_config/jobs.py`, `oarepo_config/oai.py` and
  `oarepo_config/datastreams.py` still import their helpers via
  `from oarepo.config.base import ...` (the old in-monorepo module path)
  instead of the local `from .base import ...` used everywhere else in
  this package. This currently works only because the `oarepo` metapackage
  dependency happens to ship its own (older) `oarepo.config.base`, which
  `configure_jobs()`/`configure_oai()`/`configure_datastreams()` end up
  using instead of this package's own `base.py`.
* `pyproject.toml` has no `[project.entry-points."invenio_config.module"]`
  section, so `initial_configuration.py` / `initial_rdm_config.py` are not
  auto-loaded (see [above](#initial_configurationpy--initial_rdm_configpy)).
