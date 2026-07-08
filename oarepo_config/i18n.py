def initialize_i18n():
    """Enable translated validation error messages.

    Makes sure that when a user submits invalid data (for example, a
    required field is missing), the error message shown to them is
    translated into their chosen language instead of always being shown
    in English. Takes no parameters; call it once, near the top of
    ``invenio.cfg``.
    """
    from flask_babel import lazy_gettext as _
    from marshmallow_i18n_messages import add_i18n_to_marshmallow

    add_i18n_to_marshmallow(_)
