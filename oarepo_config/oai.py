# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Configuration for OAI-PMH."""

from __future__ import annotations

import logging

from .base import get_constant_from_caller, set_constants_in_caller

log = logging.getLogger("config.oai")


def configure_oai(
    repository_name: str | None = None,
    admin_emails: list[str] | tuple[str, ...] | str | None = None,
    page_size: int = 50,
    resumption_token_expire_time: int = 120,
) -> None:
    """Set up OAI-PMH, the protocol other systems use to harvest records from this repository.

    OAI-PMH is a standard way for external services (e.g. national
    aggregators, other repositories) to regularly fetch a list of
    published records. This announces the repository's name and contact
    over that protocol, using the values already set via
    [`configure_ui`][oarepo_config.configure_ui], and tunes the paging of
    list responses.

    Unless `repository_name` is given, this must be called *after*
    [`configure_ui`][oarepo_config.configure_ui], since it needs the
    repository name that function sets up; calling it earlier raises an
    error explaining this.

    Args:
        repository_name: Name announced in the `Identify` response.
            Defaults to the (English) `name` passed to
            [`configure_ui`][oarepo_config.configure_ui]; pass it
            explicitly if harvesters should see a different, e.g. more
            descriptive, name.
        admin_emails: E-mail address(es) published as the repository's
            administrative contact in the `Identify` response. Defaults to
            the `support_contact` passed to
            [`configure_ui`][oarepo_config.configure_ui] if that is an
            e-mail address. Without either, the variable is left alone and
            invenio-oaiserver keeps announcing its placeholder,
            `info@inveniosoftware.org` - a warning is logged.
        page_size: Number of records returned per `ListRecords` /
            `ListIdentifiers` / `ListSets` page. invenio-oaiserver's own
            default is 10, which makes harvesting a larger repository
            needlessly slow; this defaults to 50, as on Zenodo.
        resumption_token_expire_time: How long, in seconds, a harvester
            may wait before asking for the next page. Defaults to 120
            (invenio-oaiserver's own default is 60).

    Invenio configuration variables set:

    * `OAISERVER_REPOSITORY_NAME` - the `repository_name` above, or a
      copy of `REPOSITORY_NAME` (set by
      [`configure_ui`][oarepo_config.configure_ui]).
    * `OAISERVER_ADMIN_EMAILS` - the `admin_emails` above, if known.
    * `OAISERVER_PAGE_SIZE` - the `page_size` above.
    * `OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME` - the
      `resumption_token_expire_time` above.

    Example:
        ```python
        config.configure_oai()
        # or with an explicit contact:
        config.configure_oai(
            admin_emails=[
                "repository@example.com"
            ]
        )
        ```

    """
    repo_name = repository_name or get_constant_from_caller("REPOSITORY_NAME")
    if not repo_name:
        raise ValueError(
            "REPOSITORY_NAME must be set, please configure UI before configuring OAI or pass repository_name."
        )
    OAISERVER_REPOSITORY_NAME = str(repo_name)

    if admin_emails is None:
        support_contact = str(get_constant_from_caller("REPOSITORY_SUPPORT_CONTACT") or "").strip()
        if "@" in support_contact and " " not in support_contact:
            admin_emails = [support_contact]
    elif isinstance(admin_emails, str):
        admin_emails = [admin_emails]

    if admin_emails:
        OAISERVER_ADMIN_EMAILS = list(admin_emails)
    else:
        log.warning(
            "No OAI-PMH administrator e-mail configured: pass admin_emails=[...] to configure_oai() "
            "or an e-mail address as support_contact to configure_ui()."
        )

    OAISERVER_PAGE_SIZE = page_size
    OAISERVER_RESUMPTION_TOKEN_EXPIRE_TIME = resumption_token_expire_time

    set_constants_in_caller(locals())
