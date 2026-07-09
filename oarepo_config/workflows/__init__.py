#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-config (see https://github.com/oarepo/oarepo-config).
#
# oarepo-config is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Configuration for workflows."""

from __future__ import annotations

from .low_level import register_workflow
from .simplified import BaseWorkflowSettings, CommunityWorkflow, IndividualWorkflow, configure_workflows

__all__ = (
    "BaseWorkflowSettings",
    "CommunityWorkflow",
    "IndividualWorkflow",
    "configure_workflows",
    "register_workflow",
)
