#!/usr/bin/env bash
# Live-verify checklist for www.groundyield.org
# Usage: ./scripts/live-verify.sh
# Exit 0 only if all required paths return HTTP 200 and homepage looks healthy.

set -euo pipefail

BASE="${BASE_URL:-https://www.groundyield.org}"
FAIL=0

check() {
  local path="$1"
  local code
  code=$(curl -sL -o /tmp/gy_verify.out -w "%{http_code}" --max-time 25 "${BASE}${path}")
  local size
  size=$(wc -c </tmp/gy_verify.out | tr -d ' ')
  if [[ "$code" != "200" ]]; then
    echo "FAIL ${path} HTTP ${code} (bytes=${size})"
    FAIL=1
  else
    echo "OK   ${path} HTTP ${code} (bytes=${size})"
  fi
}

echo "Verifying ${BASE}"
echo "----------------------------------------"

check "/"
check "/pt.html"
check "/robots.txt"
check "/sitemap.xml"
check "/updates.rss"
check "/favicon.svg"
check "/og-image.png"
check "/apple-touch-icon.png"
check "/icon-512.png"

echo "----------------------------------------"
# Content signals on homepage
if ! grep -q "Jacques Theron" /tmp/gy_verify.out 2>/dev/null; then
  # re-fetch home for content check
  curl -sL --max-time 25 "${BASE}/" -o /tmp/gy_home.out
else
  cp /tmp/gy_verify.out /tmp/gy_home.out 2>/dev/null || curl -sL --max-time 25 "${BASE}/" -o /tmp/gy_home.out
fi
curl -sL --max-time 25 "${BASE}/" -o /tmp/gy_home.out

for needle in "Jacques Theron" "pt.html" "UNIT.md" "SEASON.md"; do
  if grep -q "$needle" /tmp/gy_home.out; then
    echo "OK   homepage contains: ${needle}"
  else
    echo "FAIL homepage missing: ${needle}"
    FAIL=1
  fi
done

if grep -qi "placeholder" /tmp/gy_home.out; then
  echo "FAIL homepage contains 'placeholder'"
  FAIL=1
fi

if grep -qi "Not found — GroundYield" /tmp/gy_home.out; then
  echo "FAIL homepage looks like 404 page"
  FAIL=1
fi

echo "----------------------------------------"
if [[ "$FAIL" -ne 0 ]]; then
  echo "RESULT: FAILED — do not update UPDATES.md as shipped"
  exit 1
fi
echo "RESULT: PASSED — safe to log as live"
exit 0
