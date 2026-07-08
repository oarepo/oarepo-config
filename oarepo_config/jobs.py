from oarepo.config.base import set_constants_in_caller


def configure_jobs(permission_policy=None, logging_level=None):
    """Set up the "Jobs" feature (manually or automatically run administrative tasks).

    Invenio-jobs lets administrators run and monitor maintenance tasks
    (such as re-indexing or fixing up data) from the admin panel, and
    view their logs. This decides who is allowed to view those job logs
    and how detailed the logs are.

    Args:
        permission_policy: Who is allowed to view job logs. By default,
            only administrators can. Pass your own permission policy
            class (or its import path as a string) to change this.
        logging_level: How detailed the job logs should be, e.g.
            ``"DEBUG"``, ``"INFO"`` (the default), ``"WARNING"``.
    """
    from invenio_jobs.services.permissions import (
        JobLogsPermissionPolicy as InvenioJobLogsPermissionPolicy,
    )
    from oarepo_runtime.services.generators import AdministrationWithQueryFilter

    class JobLogsPermissionPolicy(InvenioJobLogsPermissionPolicy):
        """Permission policy for job logs."""

        can_read = [AdministrationWithQueryFilter()]

    # invenio-jobs configuration
    APP_LOGS_PERMISSION_POLICY = permission_policy or JobLogsPermissionPolicy
    JOBS_LOGGING_LEVEL = logging_level or "INFO"
    set_constants_in_caller(locals())
