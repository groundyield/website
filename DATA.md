# Data Standards

How GroundYield will publish numbers.

**Full KPI list, collection methods, accuracy bars:** **[KPI_AND_DATA.md](KPI_AND_DATA.md)**  
**Use existing weather/calendar apps — don’t rebuild:** **[EXISTING_TOOLS.md](EXISTING_TOOLS.md)**

## Principles

- Publish real numbers, not only success stories
- Include failures and negative results
- Make data understandable without specialized software
- Prefer simple formats (tables, plain text, CSV later)
- Mark every field number **F / E / H** (fact / estimate / hearsay)

## What Will Be Tracked (per unit / per season)

| Category | Examples | KPI pack |
|----------|----------|----------|
| **Inputs** | Seed type & cost, fertilizer, irrigation equipment, labor | I1, I2 |
| **Baseline** | Local typical yields before intervention | P2, Y2 |
| **Outputs** | Actual yields (kg/ha or local equivalent) | Y1–Y4 |
| **Income** | Cash crop sales, poultry/goat income | M1, M2 |
| **Losses** | Post-harvest loss estimates | L1 |
| **Water / kit** | Irrigation events, uptime, theft | W1, W2, T1, T2 |
| **Advice / tools** | Engagement, harm flags, apps used | A1–A6 |
| **Failures** | What broke, what was changed, cost of mistakes | Y4, P4 |

## Publication Rules

1. Baseline is recorded before claiming improvement
2. Units are identified consistently (even if anonymized for privacy)
3. Currency and units are stated clearly
4. Updates are added to the public record rather than rewritten history
5. Household and personal data follow [CONSENT.md](CONSENT.md)
6. Secondary statistics used on the site are listed in [SOURCES.md](SOURCES.md)
7. Anti-fraud / integrity rules (ghost units, dual evidence for headlines, truth marks F/E/H) are in **[INTEGRITY.md](INTEGRITY.md)** — treat that doc as binding for data claims
8. Accuracy minimums in [KPI_AND_DATA.md](KPI_AND_DATA.md) §3 — if unmet, mark E or don’t claim

## Current Status

No field data yet.  
Foundation phase — baselines start on the ground window ([GROUND_TRIP.md](GROUND_TRIP.md)).  
Schemas live under [data/](data/). Registry: [units.html](units.html) = **0**.

Master plan: [PLAN.md](PLAN.md). Integrity: [INTEGRITY.md](INTEGRITY.md).

When data exists it will appear in `data/`, UPDATES, and the site.

---

Last updated: 27 July 2026
