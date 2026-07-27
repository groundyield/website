# Supplier & quote log v0

**Purpose:** Replace planning ranges in [UNIT.md](UNIT.md) with **dated, sourced quotes**.  
**Status:** Template only — no field quotes yet.

Truth rules match [GROUND_TRIP.md](GROUND_TRIP.md): fact / estimate / hearsay; units and date; no private names without consent.

---

## How to log a quote

1. One row per item (or clear kit bundle).  
2. Currency + tax/VAT stated.  
3. Delivery location and lead time.  
4. Contact channel (phone/WhatsApp/email) kept **private** if needed; public log can say “Vilanculos installer A”.  
5. After 3+ solid quotes in a category, update UNIT.md mid band and note the date.

---

## Irrigation (capital)

| Date | Item | Spec | Unit price | Qty | Total | Currency | Source (public) | Lead time | Notes (fact/est) | Status |
|------|------|------|------------|-----|-------|----------|-----------------|-----------|------------------|--------|
| | Solar panels | kWp | | | | | | | | open |
| | Pump + controller | type/depth | | | | | | | | open |
| | Pipe / fittings | for 0.25–0.5 ha | | | | | | | | open |
| | Install labour | | | | | | | | | open |

## Crop inputs (operating)

| Date | Item | Spec | Price | Currency | Source | Notes | Status |
|------|------|------|-------|----------|--------|-------|--------|
| | Hybrid/improved seed | crop, variety | | | | | open |
| | Fertilizer | NPK/urea, bag size | | | | | open |
| | Crop protection | | | | | | open |

## Storage

| Date | Item | Spec | Price | Currency | Source | Notes | Status |
|------|------|------|-------|----------|--------|-------|--------|
| | Hermetic bags | brand, capacity | | | | | open |

## Livestock (optional modules)

| Date | Item | Spec | Price | Currency | Source | Notes | Status |
|------|------|------|-------|----------|--------|-------|--------|
| | Day-old / started birds | | | | | | open |
| | Feed | | | | | | open |

---

## Kit bundles (preferred when sold as package)

| Date | Kit name | Includes | Price | Currency | Source | vs UNIT mid (~$2,025) | Status |
|------|----------|----------|-------|----------|--------|----------------------|--------|
| | | | | | | | open |

---

## Dead ends

| Date | Lead | Why closed |
|------|------|------------|
| | | |

---

## Machine-readable later

When quotes stabilize, mirror into `data/quotes-YYYY-MM.csv` with columns:

`date,category,item,spec,price,currency,qty,total,source_public,lead_time_days,notes,status`

---

Last updated: 27 July 2026  
Related: [UNIT.md](UNIT.md) · [GROUND_TRIP.md](GROUND_TRIP.md) · [ECONOMICS.md](ECONOMICS.md)
