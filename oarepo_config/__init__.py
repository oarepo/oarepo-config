#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Helper classes for better invenio.cfg config file.

To use the configuration, you need to put the following to invenio.cfg:

from invenio_i18n import lazy_gettext as _
from oarepo import config

# glitchtip for reporting incidents
config.initialize_glitchtip()

# i18n
config.initialize_i18n()

env = config.load_configuration_variables()

config.configure_generic_parameters(
    env,
    code="myrepo",
    name=_("My repository"),
    description=_("Description of my repository"),
)

# use the config.<something> here to create high-level configuration of the repository
# or use CONFIG_VARIABLE=VALUE to directly set the configuration variables

config.register_workflow(...)
config.configure_cron(...)
config.configure_vocabulary(...)
config.add_model(...)
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from .datastreams import configure_datastreams
from .einfra import configure_einfra_oidc
from .jobs import configure_jobs

try:
    from oarepo_glitchtip import initialize_glitchtip
except ImportError:

    def initialize_glitchtip(
        dsn: str | None = None, deployment_version: str | None = None
    ) -> None:
        """Set up automatic error reporting to Glitchtip/Sentry.

        Requires the optional ``oarepo-glitchtip`` package; without it,
        calling this raises an ``ImportError`` explaining that the
        package needs to be installed first.

        Args:
            dsn: The Glitchtip/Sentry project URL (DSN) errors should be
                sent to.
            deployment_version: A label identifying this deployment
                (e.g. a git commit or release tag), included with
                reported errors so they can be traced back to a
                specific version.
        """
        raise ImportError("oarepo-glitchtip is not installed")


from .base import load_configuration_variables, override_configuration
from .communities import configure_communities
from .cron import configure_cron
from .generic_parameters import configure_generic_parameters
from .i18n import initialize_i18n
from .models import add_model
from .oai import configure_oai
from .stats import configure_stats
from .ui import configure_ui
from .vocabulary import configure_vocabulary
from .workflows import register_workflow

try:
    __version__ = version("oarepo-config")
except PackageNotFoundError:
    __version__ = "0.0.0dev0+unknown"

__all__ = (
    "__version__",
    "add_model",
    "configure_communities",
    "configure_cron",
    "configure_datastreams",
    "configure_einfra_oidc",
    "configure_generic_parameters",
    "configure_jobs",
    "configure_oai",
    "configure_stats",
    "configure_ui",
    "configure_vocabulary",
    "initialize_glitchtip",
    "initialize_i18n",
    "load_configuration_variables",
    "override_configuration",
    "register_workflow",
)
