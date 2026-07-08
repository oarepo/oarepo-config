#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo (see https://github.com/oarepo/oarepo).
#
# oarepo is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for oarepo-oidc-einfra module."""
import os
import sys

from .base import merge_with_caller, load_configuration_variables, set_constants_in_caller


def configure_einfra_oidc() -> None:
    """Set up "Log in with e-INFRA" (CESNET/Perun) for the repository.

    This enables single sign-on through the CESNET e-INFRA identity
    provider, so users can log in with their e-INFRA/Perun account
    instead of (or in addition to) a local username and password. It
    also makes user profile information (name, e-mail, ...) read-only
    locally, since it is then managed by e-INFRA instead.

    Requires the optional ``oarepo-oidc-einfra`` package to be
    installed - if it is missing, this function prints a message and
    stops the application from starting.

    Whether e-INFRA login is actually turned on is controlled by the
    ``INVENIO_REMOTE_AUTH_ENABLED`` setting (``true``/``yes``/``1`` to
    enable it, anything else - including leaving it unset - disables
    it). When enabled, the client credentials
    ``INVENIO_EINFRA_CONSUMER_KEY`` and ``INVENIO_EINFRA_CONSUMER_SECRET``
    must also be provided (see the deployment's ``variables``/``.env``
    configuration).
    """
    try:
        from oarepo_oidc_einfra import EINFRA_LOGIN_APP
        from oarepo_oidc_einfra import config as oarepo_einfra_config
    except ImportError:
        print("Please install oarepo-oidc-einfra to use E-INFRA OIDC login.")
        sys.exit(1)

    env = load_configuration_variables()
    if os.environ.get("INVENIO_REMOTE_AUTH_ENABLED", "no").lower() in (
        "true",
        "yes",
        "1",
    ):
        OAUTHCLIENT_REMOTE_APPS = merge_with_caller("OAUTHCLIENT_REMOTE_APPS", {"e-infra": EINFRA_LOGIN_APP})
        # needed for disconnect
        EINFRA = dict(
            consumer_key=env.INVENIO_EINFRA_CONSUMER_KEY,
            consumer_secret=env.INVENIO_EINFRA_CONSUMER_SECRET,
            **{
                k[len("EINFRA_") :].lower(): getattr(oarepo_einfra_config, k)
                for k in dir(oarepo_einfra_config)
                if k.startswith("EINFRA_")
            },
        )
        # do not allow users to change profile info, we take this from EINFRA
        USERPROFILES_READ_ONLY = True
    else:
        OAUTHCLIENT_REMOTE_APPS = merge_with_caller("OAUTHCLIENT_REMOTE_APPS", {})
    set_constants_in_caller(locals())
