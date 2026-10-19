# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Tests for e-INFRA OIDC configuration."""

from __future__ import annotations

from oarepo_config import einfra
from oarepo_config.base import DictWithGetAttr


def test_disabled(monkeypatch):
    """Disabled remote authentication preserves existing OIDC applications."""
    globals()["OAUTHCLIENT_REMOTE_APPS"] = {"existing": object()}
    monkeypatch.delenv("INVENIO_REMOTE_AUTH_ENABLED", raising=False)
    monkeypatch.setattr(einfra, "load_configuration_variables", DictWithGetAttr)

    einfra.configure_einfra_oidc()

    assert set(globals()["OAUTHCLIENT_REMOTE_APPS"]) == {"existing"}


def test_enabled(monkeypatch):
    """Enabled remote authentication registers e-INFRA and locks local profiles."""
    parser = object()
    globals()["OAUTHCLIENT_REMOTE_APPS"] = {}
    monkeypatch.setenv("INVENIO_REMOTE_AUTH_ENABLED", "true")
    monkeypatch.setattr(
        einfra,
        "load_configuration_variables",
        lambda: DictWithGetAttr(
            INVENIO_EINFRA_CONSUMER_KEY="key",
            INVENIO_EINFRA_CONSUMER_SECRET="secret",  # noqa: S106
        ),
    )

    einfra.configure_einfra_oidc(entitlements_parser=parser)

    assert "e-infra" in globals()["OAUTHCLIENT_REMOTE_APPS"]
    assert globals()["EINFRA"]["consumer_key"] == "key"
    assert globals()["USERPROFILES_READ_ONLY"] is True
    assert globals()["EINFRA_ENTITLEMENTS_PARSER"] is parser
