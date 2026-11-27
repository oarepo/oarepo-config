# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Configuration for collections."""

from __future__ import annotations

from typing import Literal

from .base import set_constants_in_caller


def configure_collections(
    enabled: bool = True,
    max_trees: int = 10,
    max_collections_per_tree: int = 100,
    community_slug: Literal["global"] | None = "global",
) -> None:
    """Configure collections feature.

    Collections are curated, browsable subsets of a community's records.
    They are saved searches. Each collection stores a search query, and its records are whatever that query matches.
    A record is never added to a collection by hand.
    """
    if community_slug not in ("global", None):
        raise ValueError(f"community_slug must be 'global' or None, got {community_slug!r}")
    COMMUNITIES_COLLECTIONS_ENABLED = enabled
    COLLECTIONS_MAX_DEPTH = 1
    COLLECTIONS_COMMUNITY_SLUG = community_slug
    COLLECTIONS_MAX_TREES = max_trees
    COLLECTIONS_MAX_COLLECTIONS_PER_TREE = max_collections_per_tree
    set_constants_in_caller(locals())
