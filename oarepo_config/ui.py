#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for the repository UI."""

from __future__ import annotations

import dataclasses
from typing import Any, ClassVar

from invenio_i18n import lazy_gettext as _

from .base import (
    get_constant_from_caller,
    load_configuration_variables,
    set_constants_in_caller,
)


@dataclasses.dataclass
class CSP:
    """Content Security Policy configuration."""

    default_src: list[str] = dataclasses.field(default_factory=list)
    """Fallback for any directive below that is left unset."""

    script_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for JavaScript."""

    script_src_elem: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for ``<script>`` elements. Falls back to :attr:`script_src`."""

    script_src_attr: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for inline event handler attributes. Falls back to :attr:`script_src`."""

    style_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for CSS."""

    style_src_elem: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for ``<style>`` elements. Falls back to :attr:`style_src`."""

    style_src_attr: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for inline style attributes. Falls back to :attr:`style_src`."""

    img_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for images."""

    font_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for fonts."""

    connect_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for fetch/XHR/WebSocket/EventSource calls (e.g. REST API endpoints)."""

    object_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for ``<object>``, ``<embed>`` and ``<applet>`` plugins."""

    media_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for ``<audio>``, ``<video>`` and ``<embed>`` media."""

    frame_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for nested browsing contexts (``<iframe>``)."""

    frame_ancestors: list[str] = dataclasses.field(default_factory=list)
    """Sources allowed to embed this page; the modern replacement for ``X-Frame-Options``."""

    child_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for nested browsing contexts and workers."""

    worker_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for Web Workers."""

    manifest_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for the application manifest."""

    prefetch_src: list[str] = dataclasses.field(default_factory=list)
    """Valid sources that may be prefetched."""

    form_action: list[str] = dataclasses.field(default_factory=list)
    """Valid targets for ``<form>`` submissions."""

    base_uri: list[str] = dataclasses.field(default_factory=list)
    """Valid sources for the document's ``<base>`` element."""

    report_to: list[str] = dataclasses.field(default_factory=list)
    """``Report-To`` group name(s) to send CSP reports to; the modern replacement for :attr:`report_uri`."""

    report_uri: str | None = None
    """URL to send CSP violation reports to."""

    report_only: bool = False
    """Report violations without enforcing the policy. Requires :attr:`report_uri`."""

    nonce_in: list[str] = dataclasses.field(default_factory=list)
    """Directives (e.g. ``["script-src"]``) that receive a per-request nonce, exposed as ``csp_nonce()``."""

    #: Fields that map to Talisman's standalone CSP options rather than to a
    #: directive inside the ``content_security_policy`` dict.
    _NON_DIRECTIVE_FIELDS: ClassVar[frozenset[str]] = frozenset({"report_uri", "report_only", "nonce_in"})

    #: Directives that CSP does not let ``default-src`` stand in for.
    _NO_DEFAULT_SRC: ClassVar[frozenset[str]] = frozenset({"base-uri", "form-action", "frame-ancestors", "report-to"})

    #: Directives that CSP resolves through a more specific directive before
    #: it ever considers ``default-src``.
    _FALLBACK_PARENT: ClassVar[dict[str, str]] = {
        "script-src-elem": "script-src",
        "script-src-attr": "script-src",
        "style-src-elem": "style-src",
        "style-src-attr": "style-src",
        "worker-src": "child-src",
        "frame-src": "child-src",
    }

    def apply_defaults(self, headers: dict[str, Any]) -> dict[str, Any]:
        """Resolve this policy against the ``content_security_policy`` already in *headers*.

        Directives set here are merged with the sources already configured for
        them (or, lacking those, with the sources of the directive they'd fall
        back to, e.g. ``default-src`` for ``connect_src``), so that setting one
        directive doesn't silently drop defaults the app still needs. Unset
        directives keep the configured value as-is. Same for ``report_uri``,
        ``report_only`` and ``nonce_in``.

        The result replaces the CSP keys in *headers* rather than merging into
        them: ``headers.update(csp.apply_defaults(headers))``.

        Raises:
            ValueError: If report-only mode ends up enabled without any
                ``report_uri``, which Flask-Talisman rejects.

        """
        existing = self._existing_policy(headers)
        resolved = self._resolve_policy(existing)

        options: dict[str, Any] = {}
        if resolved:
            options["content_security_policy"] = resolved

        report_uri = self.report_uri or headers.get("content_security_policy_report_uri")
        report_only = self.report_only or bool(headers.get("content_security_policy_report_only"))
        nonce_in = list(self.nonce_in or headers.get("content_security_policy_nonce_in") or [])

        if report_only and not report_uri:
            raise ValueError(
                "report_only requires a report_uri, set on the CSP or already configured in APP_DEFAULT_SECURE_HEADERS."
            )
        if report_uri:
            options["content_security_policy_report_uri"] = report_uri
        if report_only:
            options["content_security_policy_report_only"] = True
        if nonce_in:
            options["content_security_policy_nonce_in"] = nonce_in

        return options

    def _resolve_policy(self, existing: dict[str, list[str]]) -> dict[str, list[str]]:
        """Combine the configured sources with the ones set on this policy."""
        resolved: dict[str, list[str]] = {}
        for field in dataclasses.fields(self):
            if field.name in self._NON_DIRECTIVE_FIELDS:
                continue
            directive = field.name.replace("_", "-")
            configured = existing.get(directive, [])
            own = getattr(self, field.name)
            if own:
                # an explicit directive overrides the fallback it would
                # otherwise inherit, so bring those sources back into it
                defaults = configured or self._inherited_sources(directive, existing)
                sources = list(dict.fromkeys([*own, *defaults]))
            else:
                sources = configured
            if sources:
                resolved[directive] = sources

        # keep directives Talisman understands but this class does not model,
        # including the source-less ones such as 'upgrade-insecure-requests'
        for directive, sources in existing.items():
            resolved.setdefault(directive, list(sources))

        return resolved

    def _inherited_sources(self, directive: str, existing: dict[str, list[str]]) -> list[str]:
        """Return the sources of the first directive *directive* falls back to."""
        if directive in self._NO_DEFAULT_SRC:
            return []
        seen = {directive}
        current = self._FALLBACK_PARENT.get(directive, "default-src")
        while current not in seen:
            seen.add(current)
            if existing.get(current):
                return existing[current]
            current = self._FALLBACK_PARENT.get(current, "default-src")
        return []

    @staticmethod
    def _existing_policy(headers: dict[str, Any]) -> dict[str, list[str]]:
        """Read the configured policy from *headers*, normalised to source lists."""
        policy = headers.get("content_security_policy") or {}
        if isinstance(policy, str):
            raise TypeError("only dict policies are supported, got str")
        return {
            directive: sources.split() if isinstance(sources, str) else list(sources)
            for directive, sources in policy.items()
        }


def configure_ui(  # noqa PLR0915
    code: str = "myrepo",
    name: str | Any = "My Repository",
    subtitle: str = "",
    description: str = "",
    support_contact: str = "",
    keywords: str = "",
    use_default_frontpage: bool = False,
    show_frontpage_intro: bool = True,
    analytics: str | bool = False,
    languages: tuple[tuple[str, str], ...] = (("en", "English"),),
    csp: CSP | None = None,
) -> None:
    """Set up the repository's branding, name and general look-and-feel.

    Configures what visitors see: the repository's name and description
    shown in the browser tab/search results/front page, the theme, the
    page layout templates, and (optionally) analytics tracking.

    Args:
        code: A short, technical, all-lowercase identifier for this
            repository (e.g. ``"myrepo"``); used internally to select
            the repository's own theme files.
        name: The repository's display name, shown in the browser title
            and on the front page, e.g. ``_("My Repository")``.
        subtitle: A short subtitle/tagline shown next to the name.
        description: A longer description of the repository, used for
            SEO and on the front page.
        support_contact: Contact information (e.g. an e-mail address)
            shown to users who need help.
        keywords: Keywords describing the repository's content, used for
            SEO.
        use_default_frontpage: Whether to use Invenio's generic front
            page. Most repositories provide a custom front page, so this
            defaults to ``False``.
        show_frontpage_intro: Whether to show the introductory text
            section on the front page.
        analytics: Set to ``"matomo"`` to enable Matomo web analytics
            tracking (only takes effect on deployed, non-local
            instances; requires the Matomo URL/site ID to be configured
            in the deployment's environment). ``False`` (the default)
            disables analytics.
        languages: Extra UI languages to offer, as a tuple of
            ``(language_code, label)`` pairs. English is always
            available and does not need to be listed. This should
            normally match what was passed to
            :func:`configure_generic_parameters`.
        csp: Content Security Policy configuration. Only the sources passed
            here are recorded; the ones the deployment already allows (set up
            by :func:`configure_generic_parameters`) are added on top of them
            by :meth:`CSP.apply_defaults`.

    Should be called after :func:`configure_generic_parameters` (it
    builds on settings that function prepares) and before
    :func:`configure_oai` (which needs the repository name set here).

    Example:

    .. code-block:: python

        config.configure_ui(
            code="myrepo",
            name=_("My Repository"),
            description=_(
                "A repository for my data"
            ),
            support_contact="support@example.com",
            csp=CSP(
                # where the UI's JavaScript may fetch data from,
                # e.g. an external REST API
                connect_src=[
                    "'self'",
                    "https://api.example.com",
                ],
            ),
        )

    Invenio configuration variables set, grouped by area:

    Versioning
        * ``DEPLOYMENT_VERSION``

    Theme & security
        * ``APP_THEME``
        * ``APP_DEFAULT_SECURE_HEADERS`` - extends the value prepared by
          :func:`configure_generic_parameters`.

    Page layout templates
        * ``INSTANCE_THEME_FILE``
        * ``BASE_TEMPLATE``, ``ADMINISTRATION_THEME_BASE_TEMPLATE``,
          ``COVER_TEMPLATE``
        * ``THEME_CSS_TEMPLATE``, ``THEME_JAVASCRIPT_TEMPLATE``
        * ``HEADER_TEMPLATE``, ``THEME_HEADER_TEMPLATE``,
          ``THEME_HEADER_LOGIN_TEMPLATE``, ``THEME_FOOTER_TEMPLATE``
        * ``THEME_TRACKINGCODE_TEMPLATE``, ``THEME_FRONTPAGE_TEMPLATE``
        * ``SETTINGS_TEMPLATE``, ``SEARCH_UI_SEARCH_TEMPLATE``

    Analytics
        * ``MATOMO_ANALYTICS_TEMPLATE``, ``MATOMO_ANALYTICS_URL``,
          ``MATOMO_ANALYTICS_SITE_ID`` - only if ``analytics="matomo"``
          and this is not a local-development deployment.

    Branding
        * ``THEME_FRONTPAGE``, ``THEME_LOGO``, ``THEME_FRONTPAGE_LOGO``
        * ``THEME_SITENAME``, ``THEME_FRONTPAGE_TITLE``,
          ``THEME_SHOW_FRONTPAGE_INTRO_SECTION``

    Repository metadata (SEO & front page)
        * ``REPOSITORY_NAME``, ``REPOSITORY_DESCRIPTION``,
          ``REPOSITORY_SUPPORT_CONTACT``, ``REPOSITORY_SUBTITLE``,
          ``REPOSITORY_KEYWORDS``

    Build pipeline
        * ``JAVASCRIPT_PACKAGES_MANAGER``, ``ASSETS_BUILDER``,
          ``WEBPACKEXT_NPM_PKG_CLS``, ``WEBPACKEXT_PROJECT``

    Records & deposit UI
        * ``RECORDS_UI_ENDPOINTS``,
          ``APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED``,
          ``DASHBOARD_RECORD_CREATE_URL``
        * ``APP_RDM_DETAIL_SIDE_BAR_TEMPLATES``

    Search UI
        * ``THEME_SEARCH_ENDPOINT``, ``SEARCH_UI_SEARCH_VIEW``

    """
    env = load_configuration_variables()

    DEPLOYMENT_VERSION = env.get("INVENIO_DEPLOYMENT_VERSION", "local development")

    APP_THEME = [code, "oarepo", "semantic-ui"]
    APP_DEFAULT_SECURE_HEADERS: dict[str, Any] = get_constant_from_caller("APP_DEFAULT_SECURE_HEADERS", {})
    APP_DEFAULT_SECURE_HEADERS["content_security_policy"]["default-src"].append(
        # Fix for displaying images from another source (this one is for licenses specifically)
        "https://licensebuttons.net/"
    )

    INSTANCE_THEME_FILE = "./less/theme.less"

    # Template config
    BASE_TEMPLATE = "page.html"
    ADMINISTRATION_THEME_BASE_TEMPLATE = "invenio_app_rdm/administration_page.html"
    COVER_TEMPLATE = "invenio_app_rdm/page_cover.html"
    THEME_CSS_TEMPLATE = "css.html"
    THEME_JAVASCRIPT_TEMPLATE = "javascript.html"
    HEADER_TEMPLATE = "header.html"
    THEME_HEADER_TEMPLATE = "header.html"
    THEME_HEADER_LOGIN_TEMPLATE = "invenio_app_rdm/header_login.html"
    THEME_FOOTER_TEMPLATE = "footer.html"
    THEME_TRACKINGCODE_TEMPLATE = "oarepo_ui/trackingcode.html"
    THEME_FRONTPAGE_TEMPLATE = "frontpage.html"

    # Invenio has problems with order of loading templates. If invenio-userprofiles is loaded
    # before invenio-theme, the userprofile page will not work because base settings page
    # will be taken from userprofiles/semantic-ui/userprofiles/settings/base.html which is faulty.
    # If invenio-theme is loaded first, SETTINGS_TEMPLATE is filled, then userprofiles will use
    # it and the UI loads correctly.
    # This line just makes sure that SETTINGS_TEMPLATE and HEADER_TEMPLATE is always set up.
    SETTINGS_TEMPLATE = "invenio_theme/page_settings.html"
    HEADER_TEMPLATE = "invenio_theme/header.html"
    SEARCH_UI_SEARCH_TEMPLATE = "invenio_app_rdm/records/search.html"

    if analytics == "matomo" and DEPLOYMENT_VERSION != "local development":
        MATOMO_ANALYTICS_TEMPLATE = "oarepo_ui/matomo_analytics.html"
        MATOMO_ANALYTICS_URL = env.INVENIO_MATOMO_ANALYTICS_URL
        MATOMO_ANALYTICS_SITE_ID = env.INVENIO_MATOMO_ANALYTICS_SITE_ID
        APP_DEFAULT_SECURE_HEADERS["content_security_policy"]["default-src"].append(env.INVENIO_MATOMO_ANALYTICS_URL)

    # UI Branding & copywriting
    THEME_FRONTPAGE = use_default_frontpage
    THEME_LOGO = "images/invenio-rdm.svg"
    THEME_FRONTPAGE_LOGO = None
    THEME_SITENAME = _(name)
    THEME_FRONTPAGE_TITLE = name
    THEME_SHOW_FRONTPAGE_INTRO_SECTION = show_frontpage_intro

    # SEO & Front-page information
    REPOSITORY_NAME = name
    REPOSITORY_DESCRIPTION = description
    REPOSITORY_SUPPORT_CONTACT = support_contact
    REPOSITORY_SUBTITLE = subtitle
    REPOSITORY_KEYWORDS = keywords

    # Build pipeline config
    JAVASCRIPT_PACKAGES_MANAGER = "pnpm"
    ASSETS_BUILDER = "rspack"
    WEBPACKEXT_NPM_PKG_CLS = "pynpm:PNPMPackage"
    WEBPACKEXT_PROJECT = "oarepo_ui.webpack:project"

    # Do not add default records UI as we provide our own compatibility layer
    RECORDS_UI_ENDPOINTS: list = []  # type: ignore[var-annotated]
    # UPPY uploader is default for us
    APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED = True

    WEBPACKEXT_NPM_PKG_CLS = "pynpm:PNPMPackage"
    DASHBOARD_RECORD_CREATE_URL = "/uploads/new"

    # TODO: consult using app_rdm ones @mirekys
    APP_RDM_DETAIL_SIDE_BAR_TEMPLATES = [
        "invenio_app_rdm/records/details/side_bar/external_resources.html",
        "invenio_app_rdm/records/details/side_bar/keywords_subjects.html",
        "invenio_app_rdm/records/details/side_bar/details.html",
        "invenio_app_rdm/records/details/side_bar/licenses.html",
        "oarepo_ui/record_detail/side_bar/export.html",
        "invenio_app_rdm/records/details/side_bar/citations.html",
        "invenio_app_rdm/records/details/side_bar/manage_menu.html",
        "invenio_app_rdm/records/details/side_bar/technical_metadata.html",
    ]

    from invenio_search_ui import config as search_ui_config
    from invenio_theme import config as theme_config

    THEME_LOGO = "images/theme-logo.png"

    THEME_SEARCH_ENDPOINT = theme_config.THEME_SEARCH_ENDPOINT
    SEARCH_UI_SEARCH_VIEW = search_ui_config.SEARCH_UI_SEARCH_VIEW

    if csp is not None:
        APP_DEFAULT_SECURE_HEADERS.update(csp.apply_defaults(APP_DEFAULT_SECURE_HEADERS))

    set_constants_in_caller(locals())
