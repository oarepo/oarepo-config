#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Helper functions for writing a clean, high-level ``invenio.cfg``.

Instead of hand-assembling dozens of Flask/Invenio config constants,
``invenio.cfg`` calls a small number of ``configure_*()`` functions from
this package. Each one computes a group of related settings and writes
them directly into ``invenio.cfg``'s own configuration, as if you had
set them by hand::

    import oarepo_config as config
    from invenio_i18n import (
        lazy_gettext as _,
    )

    config.initialize_i18n()

    config.configure_generic_parameters(
        languages=(("cs", _("Czech")),),
    )

    config.configure_ui(
        code="myrepo",
        name=_("My repository"),
        description=_(
            "Description of my repository"
        ),
    )

    config.configure_communities()
    config.configure_cron()
    config.configure_stats()

    # Feel free to add/override plain CONFIG_VARIABLE = value assignments
    # below, or use config.configure_vocabulary(...), config.add_model(...),
    # config.register_workflow(...), etc. for further options.

See the project's README for the full list of available functions, the
order they should be called in, and the environment variables they read.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from .datastreams import configure_datastreams
from .einfra import configure_einfra_oidc
from .jobs import configure_jobs

try:
    from oarepo_glitchtip import initialize_glitchtip
except ImportError:

    def initialize_glitchtip(dsn: str | None = None, deployment_version: str | None = None) -> None:  # noqa: ARG001
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

        Invenio configuration variables set: implemented entirely in
        the separate ``oarepo-glitchtip`` package, so the exact set of
        variables it writes is documented there, not here.

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
