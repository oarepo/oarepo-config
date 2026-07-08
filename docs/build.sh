#!/usr/bin/env bash
#
# Build the Sphinx API documentation for oarepo-config locally.
#
# Usage:
#   ./docs/build.sh          build the HTML docs into docs/_build/html
#   ./docs/build.sh --open   ...and open them in the default browser
#   ./docs/build.sh --serve  ...and serve them with auto-rebuild on change
#   ./docs/build.sh vars     regenerate variables.md from oarepo_config functions
#
# Reuses the repository's own .venv (the same one ./run.sh sets up for
# tests) if one already exists, so it also picks up the "oarepo[rdm,tests]"
# dependency you already have installed instead of re-resolving it.
#
# (C) 2026 CESNET, z.s.p.o.
# oarepo-config is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.
#
set -euo pipefail

# oarepo/oarepo-config releases (including the pinned "oarepo[rdm,tests]"
# dependency) are published to CESNET's package index, not just PyPI - uv/pip
# need to know about it to resolve the project's dependencies at all. Same
# defaults as .runner.sh, so this works out of the box in a fresh checkout;
# override the env vars yourself if your index URL differs.
export UV_EXTRA_INDEX_URL=${UV_EXTRA_INDEX_URL:-"https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple"}
export PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL:-"https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple"}

docs_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(dirname "${docs_dir}")"
build_dir="${docs_dir}/_build/html"

cd "${repo_root}"

if command -v uv >/dev/null 2>&1; then
    # Deliberately uv venv / uv pip install (like .runner.sh), not "uv run":
    # this project depends on pre-release versions of "oarepo", which uv's
    # project/lockfile resolver (used by "uv run") refuses by default and
    # additionally tries to resolve *all* optional-dependency groups
    # together. "uv pip install" behaves like plain pip and only resolves
    # what you actually ask it to install.
    if [ ! -d ".venv" ]; then
        echo "==> Creating a virtual environment with uv" >&2
        uv venv --python=python3.14 --seed
    fi
    # shellcheck disable=SC1091
    source .venv/bin/activate
    echo "==> Installing documentation dependencies with uv" >&2
    uv pip install --quiet --prerelease allow -e ".[docs]"
else
    echo "==> uv not found, falling back to a plain virtualenv in .venv" >&2
    if [ ! -d ".venv" ]; then
        python3 -m venv .venv
    fi
    # shellcheck disable=SC1091
    source .venv/bin/activate
    pip install --quiet --upgrade pip
    pip install --quiet -e ".[docs]"
fi

mode="${1:-build}"

case "${mode}" in
    vars)
        echo "==> Regenerating variables.md from oarepo_config functions" >&2
        export DYLD_FALLBACK_LIBRARY_PATH=${DYLD_FALLBACK_LIBRARY_PATH:-/opt/homebrew/lib}
        python "${docs_dir}/mkvars.py"
        ;;
    --serve)
        echo "==> Serving docs with live-reload at http://127.0.0.1:8000" >&2
        sphinx-autobuild "${docs_dir}" "${build_dir}"
        ;;
    --open | build | "")
        echo "==> Building HTML documentation" >&2
        sphinx-build -b html "${docs_dir}" "${build_dir}"
        echo "==> Documentation built at ${build_dir}/index.html" >&2
        if [ "${mode}" = "--open" ]; then
            case "$(uname -s)" in
                Darwin) open "${build_dir}/index.html" ;;
                Linux) xdg-open "${build_dir}/index.html" >/dev/null 2>&1 || true ;;
                *) echo "Open ${build_dir}/index.html manually." >&2 ;;
            esac
        fi
        ;;
    *)
        echo "Unknown option: ${mode}" >&2
        echo "Usage: $0 [--open|--serve]" >&2
        exit 1
        ;;
esac
