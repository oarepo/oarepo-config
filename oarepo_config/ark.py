# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT
"""Configuration for ARK persistent identifiers (oarepo-ark)."""

from __future__ import annotations

from typing import Any

from .base import get_constant_from_caller, set_constants_in_caller
from .detail_sidebar import DETAIL_SIDEBAR_TEMPLATES, update_detail_sidebar


def configure_ark(  # noqa: PLR0913
    *,
    default_shoulder: str,
    shoulders: dict[str, str] | None = None,
    naan: str = "99999",
    handlers: dict[str, type | str] | None = None,
    default_handler: type | str | None = None,
    public_resolver: str | None = None,
    support: dict[str, str] | None = None,
    show_in_sidebar: bool = True,
) -> None:
    """Give every record published as public an ARK (Archival Resource Key).

    Requires the optional `oarepo-ark` package. If this function is not
    called, the package is installed but inert: no ARKs are minted and the
    `/ark:...` resolver answers 404.

    Must be called *after* [`configure_ui`][oarepo_config.configure_ui], because it
    appends the ARK box to the detail page sidebar that `configure_ui` sets; calling it
    earlier raises an error (unless `show_in_sidebar` is `False`).

    Args:
        default_shoulder: The shoulder used for all models, e.g. `"r1"`
            (consonants followed by one digit). Required.
        shoulders: Per-model shoulder overrides, keyed by the model's
            service id (the model name, or its `base_name`).
        naan: Your NAAN from https://arks.org/. Defaults to the test NAAN
            `"99999"`. Can be overridden per environment by the
            `INVENIO_ARK_NAAN` environment variable.
        handlers: Per-model handler class (or its import string), keyed by
            the model's service id.
        default_handler: Handler class (or its import string) of all other
            models. Defaults to oarepo-ark's `RDMRecordHandler`.
        public_resolver: Resolver used in citable ARK URLs. Defaults to
            `https://n2t.net/`; leave as is.
        support: The `erc-support` persistence statement of `?info`.
            Defaults to the site name, `Permanent: Stable Content:` and
            the site URL; leave as is.
        show_in_sidebar: Add the `ark` box (`oarepo_ark/ark_identifier.html`)
            to the detail page sidebar, after the `licenses` box. Defaults to
            `True`. Use [`configure_detail_sidebar`][oarepo_config.configure_detail_sidebar]
            to place it elsewhere.

    Invenio configuration variables set:

    * `ARK_NAAN`, `ARK_DEFAULT_SHOULDER`, `ARK_SHOULDERS`,
      `ARK_HANDLERS` - from the arguments above.
    * `ARK_DEFAULT_HANDLER`, `ARK_PUBLIC_RESOLVER`, `ARK_SUPPORT` -
      only if the corresponding argument is given.
    * `APP_RDM_DETAIL_SIDE_BAR_TEMPLATES` - the `ark` box is added if
      `show_in_sidebar` is `True`.

    Example:
        ```python
        config.configure_ui(...)

        config.configure_ark(
            naan="12345",
            default_shoulder="r1",
            shoulders={"theses": "t1"},
        )
        ```

    """
    try:
        import oarepo_ark  # noqa: F401
    except ImportError:
        raise ImportError("Please add oarepo-ark to your dependencies") from None

    constants: dict[str, Any] = {
        "ARK_NAAN": naan,
        "ARK_DEFAULT_SHOULDER": default_shoulder,
        "ARK_SHOULDERS": dict(shoulders or {}),
        "ARK_HANDLERS": dict(handlers or {}),
    }
    if default_handler is not None:
        constants["ARK_DEFAULT_HANDLER"] = default_handler
    if public_resolver is not None:
        constants["ARK_PUBLIC_RESOLVER"] = public_resolver
    if support is not None:
        constants["ARK_SUPPORT"] = support

    if show_in_sidebar:
        sidebar = get_constant_from_caller("APP_RDM_DETAIL_SIDE_BAR_TEMPLATES")
        if sidebar is None:
            raise ValueError(
                "APP_RDM_DETAIL_SIDE_BAR_TEMPLATES must be set, please configure UI before configuring ARK "
                "(or pass show_in_sidebar=False)."
            )
        # boxes registered via configure_detail_sidebar for the global sidebar (key None)
        known = get_constant_from_caller("_OAREPO_CONFIG_DETAIL_SIDEBAR_TEMPLATES", {}).get(None, {})
        # after the licenses (rights) box, or at the end if the sidebar has none
        licenses = {DETAIL_SIDEBAR_TEMPLATES["licenses"], known.get("licenses")}
        has_licenses = any(path in sidebar for path in licenses if path)
        constants["APP_RDM_DETAIL_SIDE_BAR_TEMPLATES"] = update_detail_sidebar(
            sidebar,
            known=known,
            templates={"ark": DETAIL_SIDEBAR_TEMPLATES["ark"]},
            move=["ark after licenses"] if has_licenses else None,
        )

    set_constants_in_caller(constants)
