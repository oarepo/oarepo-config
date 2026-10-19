# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT
"""Tests for the record detail sidebar configuration."""

from __future__ import annotations

from typing import Any

import pytest

import oarepo_config
from oarepo_config.detail_sidebar import DEFAULT_DETAIL_SIDEBAR, DETAIL_SIDEBAR_TEMPLATES, update_detail_sidebar

LOCATIONS = "datasets/record_detail/side_bar/locations.html"
LICENSES = "datarepo/records/details/side_bar/licenses.html"


def _paths(*names: str) -> list[str]:
    return [DETAIL_SIDEBAR_TEMPLATES[name] for name in names]


def _run_cfg(code: str, **cfg_globals: Any) -> dict[str, Any]:
    """Run ``code`` as if it was invenio.cfg and return its globals."""
    cfg_globals["config"] = oarepo_config
    exec(code, cfg_globals)  # noqa: S102
    return cfg_globals


def test_templates_replace_in_place_and_append_new():
    sidebar = update_detail_sidebar(
        _paths("details", "licenses"), templates={"licenses": LICENSES, "locations": LOCATIONS}
    )
    assert sidebar == [DETAIL_SIDEBAR_TEMPLATES["details"], LICENSES, LOCATIONS]


def test_order_with_rest():
    sidebar = update_detail_sidebar(_paths(*DEFAULT_DETAIL_SIDEBAR), order=["metrics", "...", "manage_menu"])
    rest = [name for name in DEFAULT_DETAIL_SIDEBAR if name not in ("metrics", "manage_menu")]
    assert sidebar == _paths("metrics", *rest, "manage_menu")


def test_order_without_rest_drops_unlisted():
    assert update_detail_sidebar(_paths(*DEFAULT_DETAIL_SIDEBAR), order=["details", "export"]) == _paths(
        "details", "export"
    )


def test_move():
    sidebar = update_detail_sidebar(
        _paths("details", "licenses", "citations"),
        move=["citations first", "details last", "licenses after details", "citations before licenses"],
    )
    assert sidebar == _paths("details", "citations", "licenses")


def test_remove():
    assert update_detail_sidebar(_paths("details", "licenses"), remove=["licenses"]) == _paths("details")


def test_unnamed_template_is_named_by_path():
    assert update_detail_sidebar(["my/box.html", *_paths("details")], move=["my/box.html last"]) == [
        *_paths("details"),
        "my/box.html",
    ]


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"order": ["nope", "..."]}, "Unknown sidebar box 'nope'"),
        ({"move": ["ark after details"]}, "call configure_ark first"),
        ({"move": ["details behind licenses"]}, "Cannot parse sidebar move"),
        ({"move": ["details after details"]}, "relative to itself"),
        ({"remove": ["metrics"]}, "Unknown sidebar box 'metrics'"),
        ({"order": ["details", "details"]}, "duplicates"),
        ({"templates": {"a": "x.html", "b": "x.html"}}, "already used by box 'a'"),
    ],
)
def test_errors(kwargs, message):
    with pytest.raises(ValueError, match=message):
        update_detail_sidebar(_paths("details", "licenses"), **kwargs)


def test_configure_sidebar_requires_ui():
    with pytest.raises(ValueError, match="configure UI before"):
        _run_cfg("config.configure_detail_sidebar(move=['details first'])")


def test_configure_sidebar_global():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(templates={'locations': LOCATIONS}, move=['locations after details'])\n"
        "config.configure_detail_sidebar(move=['locations first'])\n",
        LOCATIONS=LOCATIONS,
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details", "licenses"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == [LOCATIONS, *_paths("details", "licenses")]
    assert "OAREPO_UI_SIDEBAR_TEMPLATES" not in cfg


def test_configure_sidebar_replaces_default_box():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(templates={'licenses': LICENSES})\n"
        "config.configure_detail_sidebar(move=['licenses first'])\n",
        LICENSES=LICENSES,
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details", "licenses", "citations"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == [LICENSES, *_paths("details", "citations")]


def test_configure_sidebar_model():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(model='datasets', remove=['licenses'])\n"
        "config.configure_detail_sidebar(model='datasets', move=['citations first'])\n",
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details", "licenses", "citations"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == _paths("details", "licenses", "citations")
    assert cfg["OAREPO_UI_SIDEBAR_TEMPLATES"] == {"datasets": _paths("citations", "details")}


def test_configure_sidebar_multiple_calls():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(templates={'locations': LOCATIONS})\n"
        "config.configure_detail_sidebar(templates={'licenses': LICENSES})\n"
        "config.configure_detail_sidebar(move=['locations after details'])\n"
        "config.configure_detail_sidebar(order=['licenses', '...'])\n"
        "config.configure_detail_sidebar(remove=['citations'])\n",
        LOCATIONS=LOCATIONS,
        LICENSES=LICENSES,
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details", "licenses", "citations"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == [LICENSES, DETAIL_SIDEBAR_TEMPLATES["details"], LOCATIONS]


def test_configure_sidebar_reregistered_box_is_replaced():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(templates={'loc': 'a.html'})\n"
        "config.configure_detail_sidebar(templates={'loc': 'b.html'})\n"
        "config.configure_detail_sidebar(move=['loc first'])\n",
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == ["b.html", *_paths("details")]


def test_configure_sidebar_models_have_own_names():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(model='m1', templates={'loc': 'a.html'})\n"
        "config.configure_detail_sidebar(model='m2', templates={'loc': 'b.html'})\n"
        "config.configure_detail_sidebar(model='m1', move=['loc first'])\n"
        "config.configure_detail_sidebar(model='m2', move=['loc first'])\n",
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details"),
    )
    assert cfg["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] == _paths("details")
    assert cfg["OAREPO_UI_SIDEBAR_TEMPLATES"] == {
        "m1": ["a.html", *_paths("details")],
        "m2": ["b.html", *_paths("details")],
    }


def test_configure_sidebar_model_inherits_global_names():
    cfg = _run_cfg(
        "config.configure_detail_sidebar(templates={'loc': 'a.html'})\n"
        "config.configure_detail_sidebar(model='m1', move=['loc first'])\n",
        APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details"),
    )
    assert cfg["OAREPO_UI_SIDEBAR_TEMPLATES"] == {"m1": ["a.html", *_paths("details")]}


def test_configure_sidebar_template_under_second_name_is_rejected():
    with pytest.raises(ValueError, match=r"'x\.html' of box 'licenses' is already used by box 'extra'"):
        _run_cfg(
            "config.configure_detail_sidebar(templates={'extra': 'x.html'})\n"
            "config.configure_detail_sidebar(templates={'licenses': 'x.html'})\n",
            APP_RDM_DETAIL_SIDE_BAR_TEMPLATES=_paths("details", "licenses"),
        )
