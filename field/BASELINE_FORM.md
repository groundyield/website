# Baseline capture form v0 (paper → CSV)

Fill **one form per plot / unit interest**. Type into [`data/schema-baseline.csv`](../data/schema-baseline.csv) when online.  
Blank = unknown. Never invent `0`. Mark each number **F / E / H**.

Example shape (not real field data): [`data/baseline-examples.csv`](../data/baseline-examples.csv)

---

## Header

| Field | Value |
|-------|-------|
| Date (YYYY-MM-DD) | |
| Location (village / area, not GPS of home) | |
| Temporary ID (e.g. FARM-01) | |
| Interviewer | |
| Language | PT / EN / other: |
| Consent for public anonymized yield? | yes / no / later |
| Consent for photos of people? | yes / no |

---

## Crop baseline (repeat block if multiple crops)

| Field | CSV column | Value | F/E/H |
|-------|------------|-------|-------|
| Crop | `crop` | | |
| Local yield amount | `local_yield_value` | | |
| Local unit (saco, lata, kg…) | `local_yield_unit` | | |
| kg/ha estimate (only if convertible) | `yield_kg_ha_estimate` | | |
| Season / year referred to | `season_year` | | |
| Water source | `water_source` | rainfed / well / river / other: | |
| Seed type | `seed_type` | | |
| Fertilizer used | `fertilizer_used` | none / type+approx: | |
| Storage method | `storage_method` | | |
| Recorded date | `recorded_date` | | |
| Source | `source` | interview / observation / secondary | |

**Conversion method** (if kg/ha filled):  
_________________________________________________________________

**Notes** (constraints, market, labour — no private names):  
_________________________________________________________________
_________________________________________________________________

---

## Market snapshot (optional same day)

| Item | Value | F/E/H |
|------|-------|-------|
| Farm-gate crop | | |
| Price + unit + currency | | |
| Buyer type (market / hotel / middleman) | | |
| Season of that price | | |

---

## Constraints (tick all that apply)

- [ ] Water / drought  
- [ ] Seed quality or access  
- [ ] Fertilizer cost  
- [ ] Pests / disease  
- [ ] Labour  
- [ ] Storage losses  
- [ ] Market / transport  
- [ ] Tenure / land access  
- [ ] Other: _______________

---

## Operator checklist

- [ ] Row ready for `schema-baseline.csv`  
- [ ] No full name in public CSV  
- [ ] Dead-end or follow-up noted in GROUND_TRIP  

Last updated: 27 July 2026
