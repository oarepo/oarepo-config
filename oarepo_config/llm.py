#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-checks (see https://github.com/oarepo/oarepo-checks).
#
# oarepo-checks is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for oarepo-checks."""

from __future__ import annotations

from .base import get_constant_from_caller, set_constants_in_caller

OAREPO_CHECKS_DEFAULT_CHAT_EINFRA_CLIENT = "chat_einfra"


def configure_llm(  # noqa: PLR0913
    api_token: str | None = None,
    *,
    enabled: bool = True,
    client_name: str = OAREPO_CHECKS_DEFAULT_CHAT_EINFRA_CLIENT,
    api_url: str = "https://llm.ai.e-infra.cz/v1/chat/completions",
    model: str = "gpt-oss-120b",
    fallback_community: str | None = None,
    as_default: bool = True,
) -> None:
    """Set up the LLM client(s) used by oarepo-checks' AI-assisted record validation.

    ``oarepo-checks`` can validate a record's metadata by sending it to a
    Large Language Model and checking the response (its ``"llm"`` check,
    shown to users as "AI validation") before a record may be published.
    This registers one such LLM client (built-in support is for
    chat.ai.e-infra.cz) that the check can use.

    Call it once per LLM client/token you want available - each call reads
    back and extends whatever a previous call already registered (via
    :func:`get_constant_from_caller`), it does not replace it. This also
    means, when calling it more than once, that **whichever call has
    ``as_default=True`` last wins** as the default client.

    Requires the optional ``oarepo-checks`` package to be installed;
    without it, calling this raises an ``ImportError`` explaining that the
    package needs to be installed first.

    Args:
        api_token: Bearer token for the ``ChatEInfraClient``
            (chat.ai.e-infra.cz). If not given, this call only touches
            ``CHECKS_ENABLED``/``CHECKS_GENERIC_COMMUNITY``/the default
            client marker below, without registering a new client under
            ``client_name``. Typically read from the deployment's
            ``variables``/``.env``/environment via
            :func:`load_configuration_variables`, not hardcoded.
        enabled: Set to ``False`` to skip configuring the LLM subsystem
            entirely (nothing else below is set).
        client_name: The key this client is registered under in
            ``OAREPO_CHECKS_LLM_CLIENTS``. Use a different name per call
            if you are registering more than one client.
        api_url: The ``ChatEInfraClient`` API endpoint to send requests to.
        model: The model name the ``ChatEInfraClient`` requests.
        fallback_community: Slug of the community used for checks that
            aren't tied to a specific community. If given, overrides
            whatever a previous call already set; if not given, an
            already-set value is kept, defaulting to
            ``"llm-settings-community"`` if no call has provided one yet.
        as_default: Mark ``client_name`` as the client checks use when
            they don't request one by name (``OAREPO_CHECKS_DEFAULT_LLM_CLIENT``).

    Invenio configuration variables set:

    * ``CHECKS_ENABLED`` - the ``enabled`` argument above.
    * ``OAREPO_CHECKS_LLM_CLIENTS`` - only if ``enabled``; extended (not
      replaced) with a ``ChatEInfraClient`` entry under ``client_name``,
      only if ``api_token`` was given.
    * ``OAREPO_CHECKS_DEFAULT_LLM_CLIENT`` - only if ``enabled`` and
      ``as_default``; set to ``client_name``.
    * ``CHECKS_GENERIC_COMMUNITY`` - only if ``enabled``; ``fallback_community``
      if given, else an already-set value, else ``"llm-settings-community"``.

    Example:

    .. code-block:: python

        env = config.load_configuration_variables()
        config.configure_llm(
            api_token=env.get(
                "INVENIO_LLM_API_TOKEN"
            )
        )

        # registering a second, non-default client:
        config.configure_llm(
            api_token=env.get(
                "INVENIO_LLM_BACKUP_API_TOKEN"
            ),
            client_name="chat_einfra_backup",
            as_default=False,
        )

    """
    try:
        from oarepo_checks.llm_client import ChatEInfraClient
    except ImportError as e:
        raise ImportError("Please install oarepo-checks to use llm configuration") from e

    CHECKS_ENABLED = enabled
    if CHECKS_ENABLED:
        OAREPO_CHECKS_LLM_CLIENTS = dict(get_constant_from_caller("OAREPO_CHECKS_LLM_CLIENTS") or {})

        if as_default:
            OAREPO_CHECKS_DEFAULT_LLM_CLIENT = client_name

        if fallback_community:
            CHECKS_GENERIC_COMMUNITY = fallback_community
        else:
            CHECKS_GENERIC_COMMUNITY = get_constant_from_caller("CHECKS_GENERIC_COMMUNITY") or "llm-settings-community"

        if api_token and client_name not in OAREPO_CHECKS_LLM_CLIENTS:
            OAREPO_CHECKS_LLM_CLIENTS[client_name] = ChatEInfraClient(
                api_token=api_token,
                api_url=api_url,
                model=model,
            )

    set_constants_in_caller(locals())
