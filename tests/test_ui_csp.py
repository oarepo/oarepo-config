#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Tests for CSP.apply_defaults()."""

from __future__ import annotations

from typing import Any

import pytest

from oarepo_config.ui import CSP


def _headers(**content_security_policy: Any) -> dict[str, Any]:
    """Build an APP_DEFAULT_SECURE_HEADERS-like mapping with the given CSP directives."""
    return {
        "content_security_policy": content_security_policy,
        "content_security_policy_report_only": False,
        "content_security_policy_report_uri": None,
    }


def test_apply_defaults_on_empty_csp_and_headers_returns_nothing():
    assert CSP().apply_defaults(_headers()) == {}


def test_apply_defaults_keeps_unset_directives_unchanged():
    headers = _headers(**{"default-src": ["'self'"], "script-src": ["'self'", "blob:"]})

    resolved = CSP().apply_defaults(headers)

    assert resolved["content_security_policy"] == {
        "default-src": ["'self'"],
        "script-src": ["'self'", "blob:"],
    }


def test_apply_defaults_merges_own_sources_with_directive_already_configured():
    headers = _headers(**{"script-src": ["'self'", "blob:"]})

    resolved = CSP(script_src=["https://cdn.example.com"]).apply_defaults(headers)

    assert resolved["content_security_policy"]["script-src"] == [
        "https://cdn.example.com",
        "'self'",
        "blob:",
    ]


def test_apply_defaults_falls_back_to_default_src_when_directive_unconfigured():
    headers = _headers(**{"default-src": ["'self'"]})

    resolved = CSP(connect_src=["https://api.example.com"]).apply_defaults(headers)

    assert resolved["content_security_policy"]["connect-src"] == [
        "https://api.example.com",
        "'self'",
    ]


def test_apply_defaults_dedupes_sources_keeping_own_first():
    headers = _headers(**{"default-src": ["'self'", "https://api.example.com"]})

    resolved = CSP(connect_src=["https://api.example.com"]).apply_defaults(headers)

    assert resolved["content_security_policy"]["connect-src"] == [
        "https://api.example.com",
        "'self'",
    ]


def test_apply_defaults_preserves_directives_not_modeled_by_csp():
    headers = _headers(**{"default-src": ["'self'"], "upgrade-insecure-requests": []})

    resolved = CSP().apply_defaults(headers)

    assert "upgrade-insecure-requests" in resolved["content_security_policy"]


def test_apply_defaults_normalizes_space_separated_string_sources():
    headers = _headers(**{"default-src": "'self' https://example.com"})

    resolved = CSP(connect_src=["https://api.example.com"]).apply_defaults(headers)

    assert resolved["content_security_policy"]["connect-src"] == [
        "https://api.example.com",
        "'self'",
        "https://example.com",
    ]


def test_apply_defaults_rejects_string_content_security_policy():
    headers = _headers()
    headers["content_security_policy"] = "default-src 'self'"

    with pytest.raises(TypeError):
        CSP().apply_defaults(headers)


def test_apply_defaults_script_src_elem_falls_back_to_script_src_not_default_src():
    headers = _headers(**{"default-src": ["'self'"], "script-src": ["https://scripts.example.com"]})

    resolved = CSP(script_src_elem=["https://cdn.example.com"]).apply_defaults(headers)

    assert resolved["content_security_policy"]["script-src-elem"] == [
        "https://cdn.example.com",
        "https://scripts.example.com",
    ]


def test_apply_defaults_script_src_elem_falls_back_to_default_src_when_script_src_unset():
    headers = _headers(**{"default-src": ["'self'", "fonts.googleapis.com"]})

    resolved = CSP(script_src_elem=["https://cdn.example.com"]).apply_defaults(headers)

    assert resolved["content_security_policy"]["script-src-elem"] == [
        "https://cdn.example.com",
        "'self'",
        "fonts.googleapis.com",
    ]


def test_apply_defaults_frame_src_falls_back_to_child_src_before_default_src():
    headers = _headers(**{"default-src": ["'self'"], "child-src": ["https://frames.example.com"]})

    resolved = CSP(frame_src=["https://embed.example.com"]).apply_defaults(headers)

    assert resolved["content_security_policy"]["frame-src"] == [
        "https://embed.example.com",
        "https://frames.example.com",
    ]


@pytest.mark.parametrize("directive", ["base_uri", "frame_ancestors", "form_action"])
def test_apply_defaults_directives_do_not_inherit_default_src(directive):
    headers = _headers(**{"default-src": ["'self'", "https://example.com"]})

    resolved = CSP(**{directive: ["'self'"]}).apply_defaults(headers)

    key = directive.replace("_", "-")
    assert resolved["content_security_policy"][key] == ["'self'"]


def test_apply_defaults_own_report_uri_overrides_configured_one():
    headers = _headers()
    headers["content_security_policy_report_uri"] = "https://old.example.com/csp"

    resolved = CSP(report_uri="https://new.example.com/csp").apply_defaults(headers)

    assert resolved["content_security_policy_report_uri"] == "https://new.example.com/csp"


def test_apply_defaults_falls_back_to_configured_report_uri():
    headers = _headers()
    headers["content_security_policy_report_uri"] = "https://old.example.com/csp"

    resolved = CSP().apply_defaults(headers)

    assert resolved["content_security_policy_report_uri"] == "https://old.example.com/csp"


def test_apply_defaults_own_nonce_in_overrides_configured_one():
    headers = _headers()
    headers["content_security_policy_nonce_in"] = ["style-src"]

    resolved = CSP(nonce_in=["script-src"]).apply_defaults(headers)

    assert resolved["content_security_policy_nonce_in"] == ["script-src"]


def test_apply_defaults_report_only_requires_a_report_uri():
    with pytest.raises(ValueError, match="report_uri"):
        CSP(report_only=True).apply_defaults(_headers())


def test_apply_defaults_report_only_accepts_report_uri_already_configured():
    headers = _headers()
    headers["content_security_policy_report_uri"] = "https://example.com/csp"

    resolved = CSP(report_only=True).apply_defaults(headers)

    assert resolved["content_security_policy_report_only"] is True
    assert resolved["content_security_policy_report_uri"] == "https://example.com/csp"
