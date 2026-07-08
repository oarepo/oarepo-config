from __future__ import annotations

from typing import TYPE_CHECKING

from invenio_i18n import lazy_gettext as _

from .base import (
    get_constant_from_caller,
    load_configuration_variables,
    set_constants_in_caller,
)

if TYPE_CHECKING:
    from typing import Any


def configure_ui(
    code="myrepo",
    name=_("My Repository"),
    subtitle="",
    description="",
    support_contact="",
    keywords="",
    use_default_frontpage=False,
    show_frontpage_intro=True,
    analytics=False,
    languages=(("cs", _("Czech")),),
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

    Should be called after :func:`configure_generic_parameters` (it
    builds on settings that function prepares) and before
    :func:`configure_oai` (which needs the repository name set here).
    """
    env = load_configuration_variables()

    DEPLOYMENT_VERSION = env.get("INVENIO_DEPLOYMENT_VERSION", "local development")

    APP_THEME = [code, "oarepo", "semantic-ui"]
    APP_DEFAULT_SECURE_HEADERS: dict[str, Any] = get_constant_from_caller(
        "APP_DEFAULT_SECURE_HEADERS", {}
    )
    APP_DEFAULT_SECURE_HEADERS["content_security_policy"]["default-src"].append(
        # hack for displaying images from another source (this one is for licenses specifically)
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
    """Front page intro section visibility"""

    # hack:
    # Invenio has problems with order of loading templates. If invenio-userprofiles is loaded
    # before invenio-theme, the userprofile page will not work because base settings page
    # will be taken from userprofiles/semantic-ui/userprofiles/settings/base.html which is faulty.
    # If invenio-theme is loaded first, SETTINGS_TEMPLATE is filled, then userprofiles will use
    # it and the UI loads correctly.
    # This line just makes sure that SETTINGS_TEMPLATE and HEADER_TEMPLATE is always set up.
    SETTINGS_TEMPLATE = "invenio_theme/page_settings.html"
    HEADER_TEMPLATE = "invenio_theme/header.html"
    SEARCH_UI_SEARCH_TEMPLATE = "invenio_app_rdm/records/search.html"

    if (
        analytics
        and analytics == "matomo"
        and DEPLOYMENT_VERSION != "local development"
    ):
        MATOMO_ANALYTICS_TEMPLATE = "oarepo_ui/matomo_analytics.html"
        MATOMO_ANALYTICS_URL = env.INVENIO_MATOMO_ANALYTICS_URL
        MATOMO_ANALYTICS_SITE_ID = env.INVENIO_MATOMO_ANALYTICS_SITE_ID
        APP_DEFAULT_SECURE_HEADERS["content_security_policy"]["default-src"].append(
            env.INVENIO_MATOMO_ANALYTICS_URL
        )

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
    RECORDS_UI_ENDPOINTS = []
    # UPPY uploader is default for us
    APP_RDM_DEPOSIT_NG_FILES_UI_ENABLED = True

    WEBPACKEXT_NPM_PKG_CLS = "pynpm:PNPMPackage"
    DASHBOARD_RECORD_CREATE_URL = "/uploads/new"

    # todo: consult using app_rdm ones @mirekys
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

    set_constants_in_caller(locals())
