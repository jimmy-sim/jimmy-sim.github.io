#!/usr/bin/env bash
# Run from the repository root: bash scripts/publish.sh "Describe the edit" file...
set -euo pipefail

if (( $# < 2 )); then
  echo 'Usage: bash scripts/publish.sh "Describe the edit" file [file ...]' >&2
  exit 2
fi
message=$1
shift
cd "$(git rev-parse --show-toplevel)"

if ! git diff --cached --quiet; then
  echo 'Some changes are already staged. Commit or unstage them before using this helper.' >&2
  exit 1
fi
# Check the named files before staging. The helper leaves other edits alone.
git diff --check -- "$@"
git add -- "$@"
if git diff --cached --quiet; then
  echo 'No changes to publish in the named files.'
  exit 0
fi
git -c user.name='Jimmy Sim' \
    -c user.email='77947780+jimmy-sim@users.noreply.github.com' \
    commit -m "$message"
# A normal push refuses to overwrite newer remote changes.
git push origin HEAD:main
