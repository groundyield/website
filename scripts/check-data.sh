#!/usr/bin/env bash
# Validate public data templates before claiming field numbers.
# Usage: ./scripts/check-data.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0

need_header() {
  local file="$1"
  local expected="$2"
  if [[ ! -f "$file" ]]; then
    echo "FAIL missing $file"
    FAIL=1
    return
  fi
  local got
  got=$(head -1 "$file" | tr -d '\r')
  if [[ "$got" != "$expected" ]]; then
    echo "FAIL $file header mismatch"
    echo "  expected: $expected"
    echo "  got:      $got"
    FAIL=1
  else
    echo "OK   header $file"
  fi
}

echo "Checking data templates"
echo "----------------------------------------"

need_header "data/schema-baseline.csv" \
  "unit_id,location,crop,local_yield_value,local_yield_unit,yield_kg_ha_estimate,season_year,water_source,seed_type,fertilizer_used,storage_method,notes,recorded_date,source"

need_header "data/quotes-template.csv" \
  "date,category,item,spec,price,currency,qty,total,source_public,lead_time_days,delivery_location,vat_included,truth,notes,status"

# baseline-examples must only contain EXAMPLE rows if present
if [[ -f data/baseline-examples.csv ]]; then
  if tail -n +2 data/baseline-examples.csv | grep -v '^[[:space:]]*$' | grep -qv 'EXAMPLE'; then
    echo "FAIL baseline-examples.csv has non-EXAMPLE data rows"
    FAIL=1
  else
    echo "OK   baseline-examples.csv only EXAMPLE rows (or empty body)"
  fi
fi

# If baselines.csv exists, it must not contain EXAMPLE-ONLY demo IDs as real data
if [[ -f data/baselines.csv ]]; then
  if grep -q 'EXAMPLE-ONLY' data/baselines.csv; then
    echo "FAIL data/baselines.csv contains EXAMPLE-ONLY — move demos to baseline-examples.csv"
    FAIL=1
  else
    rows=$(tail -n +2 data/baselines.csv | grep -cve '^[[:space:]]*$' || true)
    echo "OK   data/baselines.csv present ($rows data rows)"
  fi
else
  echo "OK   data/baselines.csv not yet created (no field data)"
fi

# unit BOM files should exist
for f in data/unit-bom-v0.csv data/unit-cost-summary-v0.csv data/schema-unit-season.csv; do
  if [[ -f "$f" ]]; then
    echo "OK   present $f"
  else
    echo "FAIL missing $f"
    FAIL=1
  fi
done

echo "----------------------------------------"
if [[ "$FAIL" -ne 0 ]]; then
  echo "RESULT: FAILED"
  exit 1
fi
echo "RESULT: PASSED"
exit 0
