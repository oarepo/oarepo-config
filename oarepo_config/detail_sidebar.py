# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT
"""Configuration of the boxes in the record detail page sidebar."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from .base import get_constant_from_caller, set_constants_in_caller

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence


DETAIL_SIDEBAR_TEMPLATES: dict[str, str] = {
    "manage_menu": "invenio_app_rdm/records/details/side_bar/manage_menu.html",
    "versions": "invenio_app_rdm/records/details/side_bar/versions.html",
    "external_resources": "invenio_app_rdm/records/details/side_bar/external_resources.html",
    "communities": "invenio_app_rdm/records/details/side_bar/communities.html",
    "keywords_subjects": "invenio_app_rdm/records/details/side_bar/keywords_subjects.html",
    "details": "invenio_app_rdm/records/details/side_bar/details.html",
    "locations": "invenio_app_rdm/records/details/side_bar/locations.html",
    "licenses": "invenio_app_rdm/records/details/side_bar/licenses.html",
    "citations": "invenio_app_rdm/records/details/side_bar/citations.html",
    "export": "oarepo_ui/record_detail/side_bar/export.html",
    "technical_metadata": "invenio_app_rdm/records/details/side_bar/technical_metadata.html",
    "metrics": "invenio_app_rdm/records/details/side_bar/metrics.html",
}
"""Symbolic names of the known sidebar boxes and their templates."""

DEFAULT_DETAIL_SIDEBAR = [
    "manage_menu",
    "versions",
    "external_resources",
    "communities",
    "keywords_subjects",
    "details",
    "licenses",
    "citations",
    "export",
    "metrics",
    "technical_metadata",
]
"""Boxes set by [`configure_ui`][oarepo_config.configure_ui], in this order."""

REST = "..."

_MOVE_RE = re.compile(r"^\s*(\S+)\s+(?:(before|after)\s+(\S+)|(first|last))\s*$")


def update_detail_sidebar(  # noqa: PLR0913
    current: Sequence[str],
    *,
    known: Mapping[str, str] | None = None,
    templates: Mapping[str, str] | None = None,
    order: Sequence[str] | None = None,
    move: Sequence[str] | None = None,
    remove: Sequence[str] | None = None,
) -> list[str]:
    """Return `current` (a list of template paths) with the changes applied.

    `known` maps box names to templates of `current` (e.g. as registered by earlier
    calls), taking precedence over
    [`DETAIL_SIDEBAR_TEMPLATES`][oarepo_config.detail_sidebar.DETAIL_SIDEBAR_TEMPLATES];
    templates that have no name are named by their path.
    """
    # mapping of box name to template
    boxes = _name_boxes(current, known or {})

    for name, path in (templates or {}).items():
        # one template under two names would render the same box twice
        if other := next((n for n, p in boxes.items() if p == path and n != name), None):
            raise ValueError(f"Sidebar template '{path}' of box '{name}' is already used by box '{other}'")
        boxes[name] = path  # replaces in place, a new name is appended
    if order is not None:
        boxes = _reorder(boxes, order)
    for spec in move or ():
        boxes = _move(boxes, spec)
    for name in remove or ():
        _check_box(boxes, name)
        del boxes[name]
    return list(boxes.values())


def _name_boxes(current: Sequence[str], known: Mapping[str, str]) -> dict[str, str]:
    """Return box name -> template for the templates of `current`, in their order."""
    names_by_path = {path: name for name, path in DETAIL_SIDEBAR_TEMPLATES.items()}
    names_by_path.update({path: name for name, path in known.items()})
    return {names_by_path.get(path, path): path for path in current}


def _check_box(boxes: Mapping[str, str], name: str) -> None:
    """Raise if `name` is not a box of the sidebar."""
    if name not in boxes:
        raise ValueError(f"Unknown sidebar box '{name}'. Known boxes: {', '.join(boxes)}")


def _reorder(boxes: Mapping[str, str], order: Sequence[str]) -> dict[str, str]:
    """Return `boxes` in `order`, with `REST` standing for the boxes not listed."""
    if len(set(order)) != len(order):
        raise ValueError(f"Sidebar order contains duplicates: {list(order)}")
    for name in order:
        if name != REST:
            _check_box(boxes, name)
    rest = [name for name in boxes if name not in order]
    names: list[str] = []
    for name in order:
        names.extend(rest if name == REST else [name])
    return {name: boxes[name] for name in names}


def _move(boxes: Mapping[str, str], spec: str) -> dict[str, str]:
    """Return `boxes` with one move (`"<box> before|after <box>"`, `"<box> first|last"`) applied."""
    match = _MOVE_RE.match(spec)
    if not match:
        raise ValueError(
            f"Cannot parse sidebar move '{spec}', expected '<box> before|after <box>' or '<box> first|last'"
        )
    name, where, anchor, end = match.groups()
    _check_box(boxes, name)
    names = [n for n in boxes if n != name]
    if end == "first":
        names.insert(0, name)
    elif end == "last":
        names.append(name)
    else:
        _check_box(boxes, anchor)
        if anchor == name:
            raise ValueError(f"Sidebar box '{name}' cannot be moved relative to itself")
        names.insert(names.index(anchor) + (where == "after"), name)
    return {n: boxes[n] for n in names}


def configure_detail_sidebar(
    *,
    templates: dict[str, str] | None = None,
    order: list[str] | None = None,
    move: list[str] | None = None,
    remove: list[str] | None = None,
    model: str | None = None,
) -> None:
    """Change the boxes shown in the sidebar of the record detail page.

    The boxes are referred to by symbolic names (see
    [`DETAIL_SIDEBAR_TEMPLATES`][oarepo_config.detail_sidebar.DETAIL_SIDEBAR_TEMPLATES]):
    `manage_menu`, `versions`, `external_resources`, `communities`,
    `keywords_subjects`, `details`, `locations`, `licenses`,
    `citations`, `export`, `technical_metadata`, `metrics`. A box
    registered via `templates` is referred to by its new name.

    The changes are applied to the current sidebar, in this order:
    `templates`, `order`, `move`, `remove`. Must be called *after*
    [`configure_ui`][oarepo_config.configure_ui] and any other `configure_*`
    function that adds a box. Can be called multiple times.

    Args:
        templates: Box name -> template. An existing box gets the new
            template in place; a new box is appended at the end.
        order: The new order of the boxes. `"..."` stands for all the
            boxes not listed, in their current order; without it, the boxes
            not listed are removed.
        move: Moves applied one after another, each one of
            `"<box> before <box>"`, `"<box> after <box>"`,
            `"<box> first"` or `"<box> last"`.
        remove: Boxes to remove.
        model: Change only the sidebar of this model (the model name). Its
            sidebar starts as a copy of the global one.

    Invenio configuration variables set:

    * `APP_RDM_DETAIL_SIDE_BAR_TEMPLATES` - without `model`.
    * `OAREPO_UI_SIDEBAR_TEMPLATES[model]` - with `model`.
    * `_OAREPO_CONFIG_DETAIL_SIDEBAR_TEMPLATES` - internal: the boxes registered via
      `templates`, per sidebar (model name, `None` for the global one),
      so that later calls know their names.

    Example:
        ```python
        config.configure_ui(...)

        config.configure_detail_sidebar(
            templates={
                "locations": "datasets/record_detail/side_bar/locations.html",
                "licenses": "datarepo/records/details/side_bar/licenses.html",
            },
            move=["locations after details"],
        )
        ```

    """
    sidebar = get_constant_from_caller("APP_RDM_DETAIL_SIDE_BAR_TEMPLATES")
    if sidebar is None:
        raise ValueError(
            "APP_RDM_DETAIL_SIDE_BAR_TEMPLATES must be set, please configure UI before configuring the sidebar."
        )
    # names registered by earlier calls, per sidebar (None is the global one)
    registered = dict(get_constant_from_caller("_OAREPO_CONFIG_DETAIL_SIDEBAR_TEMPLATES", {}))
    model_sidebars = dict(get_constant_from_caller("OAREPO_UI_SIDEBAR_TEMPLATES", {}))
    known = registered.get(None, {})
    if model is not None and model in model_sidebars:
        sidebar = model_sidebars[model]
        known = registered.get(model, {})

    # known must not contain this call's templates yet: the current sidebar is named by the
    # earlier registrations, so that a re-registered box is replaced, not added twice
    sidebar = update_detail_sidebar(sidebar, known=known, templates=templates, order=order, move=move, remove=remove)
    registered[model] = {**known, **(templates or {})}

    constants: dict[str, object] = {"_OAREPO_CONFIG_DETAIL_SIDEBAR_TEMPLATES": registered}
    if model is None:
        constants["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] = sidebar
    else:
        model_sidebars[model] = sidebar
        constants["OAREPO_UI_SIDEBAR_TEMPLATES"] = model_sidebars
    set_constants_in_caller(constants)
