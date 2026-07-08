# oarepo-config

Helper library for writing a clean, high-level `invenio.cfg` for
[OARepo](https://github.com/oarepo/oarepo)/Invenio-RDM based repositories.
Instead of hand-assembling dozens of Flask/Invenio config constants,
`invenio.cfg` calls a small number of `configure_*()` functions; each one
computes a group of related settings and writes them directly into
`invenio.cfg`'s own configuration, as if you had set them by hand.

📖 **[Full documentation](https://oarepo.github.io/oarepo-config/)** —
API reference (every parameter and every Invenio variable each function
sets), environment variables, call ordering, a full example, and how the
package works internally.

## Installation

```bash
pip install oarepo-config
```

It is normally pulled in transitively as part of an `oarepo-app`
installation, but can also be used standalone. Requires Python 3.14 and
`oarepo[rdm,tests]` 14.x (see `pyproject.toml`).

## Quick start

```python
# invenio.cfg
import oarepo_config as config
from invenio_i18n import lazy_gettext as _

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

Values are read from a `variables`/`.env` file or the process environment
(`INVENIO_*`) — see
[Configuration sources and precedence](https://oarepo.github.io/oarepo-config/guide.html#configuration-sources-and-precedence)
for the loading rules, and
[Ordering](https://oarepo.github.io/oarepo-config/guide.html#ordering) for
why the calls above are in this order.

## Functions

Call these directly at module level in `invenio.cfg` (see
[how it works internally](https://oarepo.github.io/oarepo-config/guide.html#how-it-works-internally-functions-that-write-to-your-module)
for why). Click a function for its full parameter docs and the exact list
of Invenio config variables it sets.

| Function | What it does |
|---|---|
| [`initialize_i18n()`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.initialize_i18n) | Enable translated validation error messages. |
| [`initialize_glitchtip(dsn=None, deployment_version=None)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.initialize_glitchtip) | Set up error reporting to Glitchtip/Sentry (optional dependency). |
| [`configure_generic_parameters(languages=..., use_path_pid_ids=False)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_generic_parameters) | Core infrastructure: URLs, security headers, login, database, S3, OpenSearch, Redis, Celery, secret key, default identifier/vocabulary schemes. Call this first. |
| [`configure_ui(code=..., name=..., ...)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_ui) | Branding, theme, page templates, front page and analytics. |
| [`configure_communities(communities_roles=None)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_communities) | Community roles and who can do what inside a community. |
| [`register_workflow(workflow_code, workflow_name, permissions_policy, requests_policy)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.register_workflow) | Register a submission/review workflow records can go through. |
| [`configure_cron(**extra_cron_items)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_cron) | Scheduled background jobs (`CELERY_BEAT_SCHEDULE`). |
| [`configure_stats(enable=True)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_stats) | Usage statistics (record views, downloads, ...). |
| [`configure_vocabulary(code, **kwargs)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_vocabulary) | Declare a custom controlled vocabulary. |
| [`configure_datastreams(readers=None, writers=None, transformers=None)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_datastreams) | Register custom vocabulary-import sources. |
| [`configure_jobs(permission_policy=None, logging_level=None)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_jobs) | Who can view "Jobs" admin logs, and how verbose they are. |
| [`configure_oai()`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_oai) | OAI-PMH repository name. Call after `configure_ui()`. |
| [`configure_einfra_oidc()`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.configure_einfra_oidc) | "Log in with e-INFRA" (CESNET/Perun) single sign-on. |
| [`add_model(model_package_name)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.add_model) | Register a data model for global/cross-model search. |
| [`load_configuration_variables()`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.load_configuration_variables) | Read the deployment's `INVENIO_...` configuration values. |
| [`override_configuration(env=None)`](https://oarepo.github.io/oarepo-config/api.html#oarepo_config.override_configuration) | Set arbitrary config constants straight from `INVENIO_<X>` env vars. |

## Documentation

The [full documentation site](https://oarepo.github.io/oarepo-config/)
covers everything that doesn't fit here: the complete environment
variable reference, call-ordering rules, a full production `invenio.cfg`
example, and how the "write into `invenio.cfg`'s globals" mechanism
works internally. Build it locally with `./docs/build.sh` (add `--open`
or `--serve`).
