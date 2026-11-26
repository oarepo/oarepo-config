# SPDX-FileCopyrightText: 2025 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Configuration for oarepo-oidc-einfra module."""

from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING, Any

from .base import (
    load_configuration_variables,
    merge_with_caller,
    set_constants_in_caller,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    try:
        from oarepo_oidc_einfra.perun.entitlements import EntitlementsParser  # type: ignore[reportMissingImports]
    except ImportError:
        type EntitlementsParser = Callable  # type: ignore[no-redef]


def configure_einfra_oidc(entitlements_parser: EntitlementsParser | None = None) -> None:
    """Set up "Log in with e-INFRA" (CESNET/Perun) for the repository.

    Args:
        entitlements_parser: A callable that parses the user's entitlements.

    This enables single sign-on through the CESNET e-INFRA identity
    provider, so users can log in with their e-INFRA/Perun account
    instead of (or in addition to) a local username and password. It
    also makes user profile information (name, e-mail, ...) read-only
    locally, since it is then managed by e-INFRA instead.

    Requires the optional `oarepo-oidc-einfra` package to be
    installed - if it is missing, this function prints a message and
    stops the application from starting.

    Whether e-INFRA login is actually turned on is controlled by the
    `INVENIO_REMOTE_AUTH_ENABLED` setting (`true`/`yes`/`1` to
    enable it, anything else - including leaving it unset - disables
    it). When enabled, the client credentials
    `INVENIO_EINFRA_CONSUMER_KEY` and `INVENIO_EINFRA_CONSUMER_SECRET`
    must also be provided (see the deployment's `variables`/`.env`
    configuration).

    Invenio configuration variables set:

    * `OAUTHCLIENT_REMOTE_APPS` - always updated (merged with any
      existing value); gets an `"e-infra"` entry only when e-INFRA
      login is enabled.
    * `EINFRA` - only when e-INFRA login is enabled; the e-INFRA
      client credentials and endpoint configuration.
    * `USERPROFILES_READ_ONLY` - only when e-INFRA login is enabled;
      forced to `True`.

    Example:
        ```python
        config.configure_einfra_oidc()
        ```

    Make sure to set `INVENIO_REMOTE_AUTH_ENABLED=true` and provide
    `INVENIO_EINFRA_CONSUMER_KEY` and `INVENIO_EINFRA_CONSUMER_SECRET`
    in your deployment's `variables` or environment.

    """
    remote_apps, constants = _einfra_login_config("EINFRA_LOGIN_APP", entitlements_parser)
    constants["OAUTHCLIENT_REMOTE_APPS"] = merge_with_caller("OAUTHCLIENT_REMOTE_APPS", remote_apps)
    set_constants_in_caller(constants)


def configure_cesid_oidc(entitlements_parser: EntitlementsParser | None = None) -> None:
    """Set up "Log in with CESiD" (CESNET identity provider) for the repository.

    Args:
        entitlements_parser: A callable that parses the user's entitlements.

    This enables single sign-on through the CESNET CESiD identity
    provider (`https://login.cesid.cesnet.cz/`), so users can log in
    with their CESiD account instead of (or in addition to) a local
    username and password. It also makes user profile information
    (name, e-mail, ...) read-only locally, since it is then managed
    by CESiD instead. This is a rebranded `configure_einfra_oidc` - use
    one or the other, not both (they register the same `"e-infra"` app).

    Requires the optional `oarepo-oidc-einfra` package to be
    installed - if it is missing, this function prints a message and
    stops the application from starting.

    Whether CESiD login is actually turned on is controlled by the
    `INVENIO_REMOTE_AUTH_ENABLED` setting (`true`/`yes`/`1` to
    enable it, anything else - including leaving it unset - disables
    it). When enabled, the client credentials
    `INVENIO_EINFRA_CONSUMER_KEY` and `INVENIO_EINFRA_CONSUMER_SECRET`
    must also be provided (see the deployment's `variables`/`.env`
    configuration).

    Invenio configuration variables set:

    * `OAUTHCLIENT_REMOTE_APPS` - always updated (merged with any
      existing value); gets an `"e-infra"` entry (the CESiD-branded
      app) only when CESiD login is enabled.
    * `EINFRA` - only when CESiD login is enabled; the client
      credentials and endpoint configuration.
    * `USERPROFILES_READ_ONLY` - only when CESiD login is enabled;
      forced to `True`.

    Example:
        ```python
        config.configure_cesid_oidc()
        ```

    Make sure to set `INVENIO_REMOTE_AUTH_ENABLED=true` and provide
    `INVENIO_EINFRA_CONSUMER_KEY` and `INVENIO_EINFRA_CONSUMER_SECRET`
    in your deployment's `variables` or environment.

    """
    remote_apps, constants = _einfra_login_config("CESID_LOGIN_APP", entitlements_parser)
    constants["OAUTHCLIENT_REMOTE_APPS"] = merge_with_caller("OAUTHCLIENT_REMOTE_APPS", remote_apps)
    constants["EINFRA_ENTITLEMENT_ISSUER"] = "iam.cesid.cesnet.cz"
    set_constants_in_caller(constants)


def _einfra_login_config(
    login_app_name: str, entitlements_parser: EntitlementsParser | None
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return `(remote apps to merge, other constants)` for one of the oarepo-oidc-einfra login apps.

    Both e-INFRA and CESiD apps are registered under the same `"e-infra"` key and share
    the `EINFRA` configuration - they differ only in the user-facing branding and URLs.
    """
    try:
        import oarepo_oidc_einfra
        from oarepo_oidc_einfra import config as oarepo_einfra_config
    except ImportError:
        print("Please install oarepo-oidc-einfra to use E-INFRA/CESiD OIDC login.")  # noqa: T201
        sys.exit(1)

    remote_apps: dict[str, Any] = {}
    constants: dict[str, Any] = {}
    if _remote_auth_enabled():
        env = load_configuration_variables()
        remote_apps["e-infra"] = getattr(oarepo_oidc_einfra, login_app_name)
        # needed for disconnect
        constants["EINFRA"] = dict(
            consumer_key=env.INVENIO_EINFRA_CONSUMER_KEY,
            consumer_secret=env.INVENIO_EINFRA_CONSUMER_SECRET,
            **{
                k[len("EINFRA_") :].lower(): getattr(oarepo_einfra_config, k)
                for k in dir(oarepo_einfra_config)
                if k.startswith("EINFRA_")
            },
        )
        # do not allow users to change profile info, we take this from the identity provider
        constants["USERPROFILES_READ_ONLY"] = True

    if entitlements_parser is not None:
        constants["EINFRA_ENTITLEMENTS_PARSER"] = entitlements_parser

    return remote_apps, constants


def _remote_auth_enabled() -> bool:
    """Return True if `INVENIO_REMOTE_AUTH_ENABLED` is set to a truthy value."""
    return os.environ.get("INVENIO_REMOTE_AUTH_ENABLED", "no").lower() in ("true", "yes", "1")
