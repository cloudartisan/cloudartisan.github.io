#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

export HUGO_CACHEDIR="${HUGO_CACHEDIR:-${REPO_ROOT}/.hugo_cache}"

exec hugo "$@"
