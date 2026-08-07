#!/usr/bin/env python3
#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for periodic (scheduled) background tasks."""

from __future__ import annotations

from datetime import timedelta
from typing import Any

from celery.schedules import crontab
from invenio_stats.tasks import StatsAggregationTask, StatsEventTask

from .base import merge_with_caller, set_constants_in_caller


def configure_cron(**extra_cron_items: Any) -> None:
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

    Args:
        **extra_cron_items: Additional scheduled jobs to add (or to
            override, if the name matches one of the built-in jobs
            above), one keyword per job. Each value follows Celery's
            "beat schedule" format, e.g.::

                config.configure_cron(
                    my_job={
                        "task": "my_package.tasks.my_task",
                        "schedule": timedelta(
                            minutes=30
                        ),
                    },
                )

    Invenio configuration variables set:

    * ``CELERY_BEAT_SCHEDULE`` - merged with any schedule already
      defined earlier in ``invenio.cfg``; entries from
      ``**extra_cron_items`` win over the built-in defaults listed
      above when their names collide.

    """
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
            # "reindex-stats": StatsRDMReindexTask,  # Every hour at minute 10
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
            **extra_cron_items,
        },
    )

    set_constants_in_caller(locals())
