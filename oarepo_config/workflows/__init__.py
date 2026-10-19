# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

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
