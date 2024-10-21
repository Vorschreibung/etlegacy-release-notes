#!/usr/bin/env bash
set -eo pipefail
die() {
    printf '%b\n' "$1" >&2
    exit "${2:-1}"
}

command -v pixi &>/dev/null || die "Install pixi first: https://pixi.sh/latest/"

pixi run python -- ./convert.py "$@"
