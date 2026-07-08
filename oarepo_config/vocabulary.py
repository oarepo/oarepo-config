from typing import Any

from .base import get_constant_from_caller, set_constants_in_caller


def configure_vocabulary(code: str, **kwargs: Any) -> None:
    """Declare a custom controlled vocabulary (a fixed list of allowed values).

    Vocabularies are controlled lists of values that records can pick
    from, such as languages, resource types or licenses. Call this once
    for each additional vocabulary type your repository needs, to
    describe it and any extra properties it should have.

    Args:
        code: A short, unique identifier for the vocabulary, e.g.
            ``"languages"``.
        **kwargs: Extra details describing the vocabulary, typically
            including ``name`` (its display name), ``description``, and
            ``props`` (a description of any extra fields each entry in
            the vocabulary should have, and how they appear in forms).
            See the
            `OARepo reference docs <https://nrp-cz.github.io/docs/customize/configure/reference#configure_vocabulary>`_
            for the full list of supported keys.

    Calling this multiple times with different ``code`` values adds
    multiple vocabularies; it does not replace previously configured
    ones.
    """
    INVENIO_VOCABULARY_TYPE_METADATA = get_constant_from_caller(
        "INVENIO_VOCABULARY_TYPE_METADATA", {}
    )
    INVENIO_VOCABULARY_TYPE_METADATA[code] = kwargs

    set_constants_in_caller(locals())
