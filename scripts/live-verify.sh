#!/usr/bin/env bash
# Live-verify checklist for www.groundyield.org
# Usage: ./scripts/live-verify.sh
# Exit 0 only if all required paths return HTTP 200, bodies look real, homepage healthy.

set -euo pipefail

BASE="${BASE_URL:-https://www.groundyield.org}"
FAIL=0
CB="cb=$(date +%s)"

check() {
  local path="$1"
  local code size
  code=$(curl -sL -o /tmp/gy_verify.out -w "%{http_code}" --max-time 25 "${BASE}${path}?${CB}")
  size=$(wc -c </tmp/gy_verify.out | tr -d ' ')
  if [[ "$code" != "200" ]]; then
    echo "FAIL ${path} HTTP ${code} (bytes=${size})"
    FAIL=1
  elif [[ "$size" -lt 10 ]]; then
    echo "FAIL ${path} HTTP ${code} but body too small (bytes=${size})"
    FAIL=1
  else
    echo "OK   ${path} HTTP ${code} (bytes=${size})"
  fi
}

# Expect Content-Type substring and optional magic bytes (hex)
check_typed() {
  local path="$1"
  local ctype_want="$2"
  local magic_hex="${3:-}"
  local code size ctype
  code=$(curl -sL -D /tmp/gy_hdr -o /tmp/gy_verify.out -w "%{http_code}" --max-time 25 "${BASE}${path}?${CB}")
  size=$(wc -c </tmp/gy_verify.out | tr -d ' ')
  ctype=$(grep -i '^content-type:' /tmp/gy_hdr | tail -1 | tr -d '\r' | cut -d' ' -f2- || true)
  if [[ "$code" != "200" ]]; then
    echo "FAIL ${path} HTTP ${code} (bytes=${size})"
    FAIL=1
    return
  fi
  if [[ -n "$ctype_want" ]] && ! echo "$ctype" | grep -qi "$ctype_want"; then
    echo "FAIL ${path} Content-Type '${ctype}' (want ~${ctype_want})"
    FAIL=1
    return
  fi
  if [[ -n "$magic_hex" ]]; then
    local got
    got=$(xxd -p -l $(( ${#magic_hex} / 2 )) /tmp/gy_verify.out 2>/dev/null | tr -d '\n')
    if [[ "$got" != "$magic_hex"* ]] && [[ "$got" != "$magic_hex" ]]; then
      # PNG is 89504e47; SVG often 3c737667; PDF is 25504446
      # Also fail if body is base64 of PDF (starts with 4a564245 = JVBE)
      if [[ "$got" == 4a564245* ]]; then
        echo "FAIL ${path} body is base64 text, not binary PDF (got ${got})"
        FAIL=1
        return
      fi
      if [[ "$magic_hex" == "25504446" && "$got" != "25504446"* ]]; then
        echo "FAIL ${path} not a PDF (magic ${got}, want 25504446)"
        FAIL=1
        return
      fi
      if [[ "$magic_hex" == "89504e47" && "$got" != "89504e47"* ]]; then
        echo "FAIL ${path} not a PNG (magic ${got})"
        FAIL=1
        return
      fi
    fi
  fi
  echo "OK   ${path} HTTP ${code} type=${ctype} bytes=${size}"
}

echo "Verifying ${BASE}"
echo "----------------------------------------"

check "/"
check "/pt.html"
check "/robots.txt"
check_typed "/sitemap.xml" "xml"
check_typed "/updates.rss" "xml\|rss\|text"
check_typed "/favicon.svg" "svg\|image"
check_typed "/og-image.png" "png\|image" "89504e47"
check_typed "/apple-touch-icon.png" "png\|image" "89504e47"
check_typed "/icon-512.png" "png\|image" "89504e47"
check_typed "/field/GroundYield_Field_OnePager_EN_PT.pdf" "pdf\|octet" "25504446"
check_typed "/field/GroundYield_Field_Forms_EN_PT.pdf" "pdf\|octet" "25504446"
check "/units.html"
check "/day1.html"
check "/docs.html"
check "/whitepaper.html"
check "/roadmap.html"

echo "----------------------------------------"
curl -sL --max-time 25 "${BASE}/?${CB}" -o /tmp/gy_home.out

for needle in "Jacques Theron" "pt.html" "UNIT.md" "SEASON.md" "Field one-pager" "Field forms" "FIELD_KIT" "INTEGRITY" "Fighting fraud" "Zero units" "Ground window" "units.html" "updates.rss" "docs.html"; do
  if grep -q "$needle" /tmp/gy_home.out; then
    echo "OK   homepage contains: ${needle}"
  else
    echo "FAIL homepage missing: ${needle}"
    FAIL=1
  fi
done

curl -sL --max-time 25 "${BASE}/docs.html?${CB}" -o /tmp/gy_docs.out
for needle in "Document library" "PLAN.md" "KPI_AND_DATA" "REMOTE_OPS" "FIELD_KIT"; do
  if grep -q "$needle" /tmp/gy_docs.out; then
    echo "OK   docs.html contains: ${needle}"
  else
    echo "FAIL docs.html missing: ${needle}"
    FAIL=1
  fi
done

echo "----------------------------------------"
curl -sL --max-time 25 "${BASE}/pt.html?${CB}" -o /tmp/gy_pt.out
for needle in "Jacques Theron" "zero unidades" "Rumbacaca" "INTEGRITY" "PLAN.md" "LESSONS" "AI_FIELD_PATH" "Registo"; do
  if grep -qi "$needle" /tmp/gy_pt.out; then
    echo "OK   pt.html contains: ${needle}"
  else
    echo "FAIL pt.html missing: ${needle}"
    FAIL=1
  fi
done

curl -sL --max-time 25 "${BASE}/updates.rss?${CB}" -o /tmp/gy_rss.out
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
