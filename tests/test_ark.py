# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT
"""Tests for the ARK persistent identifier configuration."""

from __future__ import annotations

import sys
import types
from typing import Any

import pytest

import oarepo_config
from oarepo_config.detail_sidebar import DEFAULT_DETAIL_SIDEBAR, DETAIL_SIDEBAR_TEMPLATES

LICENSES = "datarepo/records/details/side_bar/licenses.html"


def _paths(*names: str) -> list[str]:
    return [DETAIL_SIDEBAR_TEMPLATES[name] for name in names]


def _run_cfg(code: str, **cfg_globals: Any) -> dict[str, Any]:
    """Run `code` as if it was invenio.cfg and return its globals."""
    cfg_globals["config"] = oarepo_config
    exec(code, cfg_globals)  # noqa: S102
    return cfg_globals


@pytest.fixture(autouse=True)
def ark_installed(monkeypatch):
    monkeypatch.setitem(sys.modules, "oarepo_ark", sys.modules.get("oarepo_ark") or types.ModuleType("oarepo_ark"))


def test_configure_ark_sets_constants():
    cfg = _run_cfg(
        "config.configure_ark(default_shoulder='r1', naan='12345', shoulders={'theses': 't1'}, show_in_sidebar=False)"
    )
    assert cfg["ARK_NAAN"] == "12345"
    assert cfg["ARK_DEFAULT_SHOULDER"] == "r1"
    assert cfg["ARK_SHOULDERS"] == {"theses": "t1"}
    assert cfg["ARK_HANDLERS"] == {}
    assert "ARK_DEFAULT_HANDLER" not in cfg
    assert "APP_RDM_DETAIL_SIDE_BAR_TEMPLATES" not in cfg


def test_configure_ark_puts_box_after_licenses():
    # calling it twice must not add the box twice
    cfg = _run_cfg(
        "config.configure_ark(default_shoulder='r1')\nconfig.configure_ark(default_shoulder='r1')\n",
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths(*DEFAULT_DETAIL_SIDEBAR),
    )
    names = DEFAULT_DETAIL_SIDEBAR.copy()
    names.insert(names.index("licenses") + 1, "ark")
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == _paths(*names)


def test_configure_ark_after_replaced_licenses():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(templates={'licenses': LICENSES})\n"
        "config.configure_ark(default_shoulder='r1')\n",
        LICENSES=LICENSES,
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details", "licenses", "citations"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == [*_paths("details"), LICENSES, *_paths("ark", "citations")]


def test_configure_ark_without_licenses_appends():
    cfg = _run_cfg("config.configure_ark(default_shoulder='r1')", APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details"))
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == _paths("details", "ark")


def test_ark_box_can_be_moved_by_configure_detail_sidebar():
    cfg = _run_cfg(
        "config.configure_ark(default_shoulder='r1')\nconfig.configure_detail_sidebar(move=['ark first'])\n",
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details", "licenses"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == _paths("ark", "details", "licenses")


def test_configure_ark_requires_ui():
    with pytest.raises(ValueError, match="configure UI before"):
        _run_cfg("config.configure_ark(default_shoulder='r1')")


def test_configure_ark_requires_oarepo_ark(monkeypatch):
    monkeypatch.setitem(sys.modules, "oarepo_ark", None)  # makes the import fail
    with pytest.raises(ImportError, match="add oarepo-ark"):
        _run_cfg("config.configure_ark(default_shoulder='r1', show_in_sidebar=False)")
