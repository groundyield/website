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
check "/field/GroundYield_Field_OnePager_EN_PT.pdf"
check "/field/GroundYield_Field_Forms_EN_PT.pdf"
check "/units.html"

echo "----------------------------------------"
curl -sL --max-time 25 "${BASE}/" -o /tmp/gy_home.out

for needle in "Jacques Theron" "pt.html" "UNIT.md" "SEASON.md" "Field one-pager" "Field forms" "FIELD_KIT" "INTEGRITY" "Fighting fraud" "Zero units" "design targets" "units.html" "updates.rss"; do
  if grep -q "$needle" /tmp/gy_home.out; then
    echo "OK   homepage contains: ${needle}"
  else
    echo "FAIL homepage missing: ${needle}"
    FAIL=1
  fi
done

# RSS should not be a one-line stub and should mention recent substance
curl -sL --max-time 25 "${BASE}/updates.rss" -o /tmp/gy_rss.out
rss_items=$(grep -c '<item>' /tmp/gy_rss.out || true)
if [[ "${rss_items}" -lt 4 ]]; then
  echo "FAIL updates.rss has fewer than 4 items (got ${rss_items})"
  FAIL=1
else
  echo "OK   updates.rss item count: ${rss_items}"
fi
if ! grep -q "Field one-pager\|field one-pager\|offline" /tmp/gy_rss.out; then
  echo "FAIL updates.rss missing field/offline entry"
  FAIL=1
else
  echo "OK   updates.rss mentions field/offline handout"
fi

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
