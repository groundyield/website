#!/usr/bin/env bash
# Run before claiming anything "shipped" or "live".
# Usage: ./scripts/ship-check.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0

echo "=== 1/2 data templates ==="
if ! bash scripts/check-data.sh; then
  FAIL=1
fi

echo ""
echo "=== 2/2 production live-verify ==="
if ! bash scripts/live-verify.sh; then
  FAIL=1
fi

echo ""
if [[ "$FAIL" -ne 0 ]]; then
  echo "SHIP-CHECK: FAILED — do not update UPDATES.md as live/shipped"
  exit 1
fi
echo "SHIP-CHECK: PASSED — safe to log as live"
exit 0
