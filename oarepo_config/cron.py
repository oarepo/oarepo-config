# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Configuration for periodic (scheduled) background tasks."""

from __future__ import annotations

from datetime import timedelta
from typing import Any

from celery.schedules import crontab
from invenio_stats.tasks import StatsAggregationTask, StatsEventTask

from .base import get_constant_from_caller, merge_with_caller, set_constants_in_caller


def _collections_cron_items(enabled: bool) -> dict[str, Any]:
    """Return the scheduled jobs needed by community collections."""
    if not enabled:
        return {}
    return {
        "update-collections-size": {
            "task": "invenio_rdm_records.collections.tasks.update_collections_size",
            "schedule": timedelta(hours=1),
        },
    }


def _file_integrity_cron_items(check_days: int | None) -> dict[str, Any]:
    """Return the scheduled jobs for periodic file checksum verification."""
    if check_days is None:
        return {}
    if check_days < 1:
        raise ValueError("file_integrity_check_days must be a positive number of days or None")
    return {
        "file-checks": {
            "task": "invenio_files_rest.tasks.schedule_checksum_verification",
            "schedule": timedelta(hours=1),
            "kwargs": {
                "batch_interval": {"hours": 1},
                "frequency": {"days": check_days},
                # 0 = spread the files evenly over the batches of one period
                "max_count": 0,
                # honours FILES_REST_CHECKSUM_VERIFICATION_URI_PREFIXES
                "files_query": "invenio_app_rdm.utils.files.checksum_verification_files_query",
            },
        },
        "file-integrity-report": {
            "task": "invenio_app_rdm.tasks.file_integrity_report",
            "schedule": crontab(minute=0, hour=7),  # Every day at 07:00 UTC
        },
    }


def configure_cron(file_integrity_check_days: int | None = None, **extra_cron_items: Any) -> None:
    """Set up the periodic (scheduled) background tasks the repository needs.

    The repository relies on a number of jobs that must run automatically
    in the background on a regular basis - for example, cleaning up old
    sessions, aggregating usage statistics, or clearing caches. This
    function sets up a sensible set of such jobs out of the box:

    * keeping the search index queues healthy (every 10 seconds)
    * cleaning up expired user sessions and old IP address logs
    * processing and aggregating usage statistics (hourly)
    * clearing the communities cache (daily)
    * removing expired file-access-request tokens (daily)
    * lifting expired embargoes (daily)
    * expiring requests past their expiration date, e.g. community
      invitations (daily)
    * purging drafts that were discarded more than an hour ago (hourly)
    * deleting job logs older than `JOBS_LOGGING_RETENTION_DAYS` (daily)
    * refreshing the sitemap (daily)
    * updating the statistics of user e-mail domains (every 4 hours)
    * recounting community collections (hourly) - only if
      `COMMUNITIES_COLLECTIONS_ENABLED` was set to `True` earlier in
      `invenio.cfg`

    Compared to upstream InvenioRDM, `reindex-stats` is left out on
    purpose: OARepo models do not index usage statistics into the record
    documents, so there is nothing to refresh.

    Args:
        file_integrity_check_days: Turns on periodic fixity checking: every
            stored file gets its checksum re-computed once per this many
            days (spread evenly over hourly batches), and a daily e-mail
            reports the files that are missing or corrupted to
            `APP_RDM_ADMIN_EMAIL_RECIPIENT`
            (`INVENIO_APP_RDM_ADMIN_EMAIL_RECIPIENT` in the environment).
            Off (`None`) by default, because it reads every file back from
            the storage - on an S3 deployment make sure that this traffic
            is acceptable, and that the checksums of multipart uploads can
            be verified, before enabling it. Upstream InvenioRDM uses 14
            days, Zenodo 180.
        **extra_cron_items: Additional scheduled jobs to add (or to
            override, if the name matches one of the built-in jobs
            above), one keyword per job. Each value follows Celery's
            "beat schedule" format, e.g.:

            ```python
            config.configure_cron(
                my_job={
                    "task": "my_package.tasks.my_task",
                    "schedule": timedelta(
                        minutes=30
                    ),
                },
            )
            ```

    Invenio configuration variables set:

    * `CELERY_BEAT_SCHEDULE` - merged with any schedule already
      defined earlier in `invenio.cfg`; entries from
      `**extra_cron_items` win over the built-in defaults listed
      above when their names collide.

    """
    collections_enabled = bool(get_constant_from_caller("COMMUNITIES_COLLECTIONS_ENABLED", default=False))

    CELERY_BEAT_SCHEDULE = merge_with_caller(
        "CELERY_BEAT_SCHEDULE",
        {
            "indexer": {
                "task": "invenio_records_resources.tasks.manage_indexer_queues",
                "schedule": timedelta(seconds=10),
            },
            "accounts_sessions": {
                "task": "invenio_accounts.tasks.clean_session_table",
                "schedule": timedelta(minutes=60),
            },
            "accounts_ips": {
                "task": "invenio_accounts.tasks.delete_ips",
                "schedule": timedelta(hours=6),
            },
            # indexing of statistics events & aggregations
            "stats-process-events": {
                **StatsEventTask,
                "schedule": crontab(minute="25,55"),  # Every hour at minute 25 and 55
            },
            "stats-aggregate-events": {
                **StatsAggregationTask,
                "schedule": crontab(minute="0"),  # Every hour at minute 0
            },
            # "reindex-stats" (StatsRDMReindexTask) is intentionally not scheduled:
            # OARepo models do not index usage statistics into record documents.
            # Invenio communities provides some caching that has the potential to be never removed,
            # therefore, we need a cronjob to ensure that at least once per day we clear the cache
            "clear-cache": {
                "task": "invenio_communities.tasks.clear_cache",
                "schedule": crontab(minute="0", hour="1"),  # Every day at 01:00 UTC
            },
            "clean-access-request-tokens": {
                "task": "invenio_rdm_records.requests.access.tasks.clean_expired_request_access_tokens",
                "schedule": crontab(minute="4", hour="0"),
            },
            "lift_embargos": {
                "task": "invenio_rdm_records.services.tasks.update_expired_embargos",
                "schedule": crontab(minute=0, hour=0),
            },
            "expire_requests": {
                "task": "invenio_requests.tasks.check_expired_requests",
                "schedule": crontab(minute=3, hour=0),
            },
            # hard-delete drafts that were discarded (soft-deleted) more than an hour ago
            "draft_resources": {
                "task": "invenio_drafts_resources.services.records.tasks.cleanup_drafts",
                "schedule": timedelta(minutes=60),
            },
            "delete-job-logs": {
                "task": "invenio_jobs.logging.tasks.delete_logs",
                "schedule": crontab(minute=5, hour=0),
            },
            "update_sitemap": {
                "task": "invenio_sitemap.tasks.update_sitemap_cache",
                "schedule": crontab(minute=0, hour=2),
            },
            "update_domain_status": {
                "task": "invenio_accounts.tasks.update_domain_status",
                "schedule": timedelta(hours=4),
            },
            **_collections_cron_items(collections_enabled),
            **_file_integrity_cron_items(file_integrity_check_days),
            **extra_cron_items,
        },
    )

    set_constants_in_caller(locals())
