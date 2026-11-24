# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Configuration for collections."""

from __future__ import annotations

from .base import set_constants_in_caller


def configure_collections(
    communities_collections_enabled: bool = True,
    max_trees: int = 10,
    max_collections_per_tree: int = 100,
) -> None:
    """Configure collections feature.

    Collections are curated, browsable subsets of a community's records.
    They are saved searches. Each collection stores a search query, and its records are whatever that query matches.
    A record is never added to a collection by hand.
    """
    COMMUNITIES_COLLECTIONS_ENABLED = communities_collections_enabled
    COLLECTIONS_MAX_DEPTH = 1
    COLLECTIONS_COMMUNITY_SLUG = "global"
    COLLECTIONS_MAX_TREES = max_trees
    COLLECTIONS_MAX_COLLECTIONS_PER_TREE = max_collections_per_tree
    set_constants_in_caller(locals())
