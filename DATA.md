# Data Standards

How GroundYield will publish numbers.

## Principles

- Publish real numbers, not only success stories
- Include failures and negative results
- Make data understandable without specialized software
- Prefer simple formats (tables, plain text, CSV later)

## What Will Be Tracked (per unit / per season)

| Category | Examples |
|----------|----------|
| **Inputs** | Seed type & cost, fertilizer, irrigation equipment, labor |
| **Baseline** | Local typical yields before intervention |
| **Outputs** | Actual yields (kg/ha or local equivalent) |
| **Income** | Cash crop sales, poultry/goat income |
| **Losses** | Post-harvest loss estimates |
| **Failures** | What broke, what was changed, cost of mistakes |

## Publication Rules

1. Baseline is recorded before claiming improvement
2. Units are identified consistently (even if anonymized for privacy)
3. Currency and units are stated clearly
4. Updates are added to the public record rather than rewritten history
5. Household and personal data follow [CONSENT.md](CONSENT.md)
6. Secondary statistics used on the site are listed in [SOURCES.md](SOURCES.md)
7. Anti-fraud / integrity rules (ghost units, dual evidence for headlines, truth marks F/E/H) are in **[INTEGRITY.md](INTEGRITY.md)** — treat that doc as binding for data claims

## Current Status

No field data yet.  
Foundation phase — baselines start on the ground window ([GROUND_TRIP.md](GROUND_TRIP.md)).  
Schemas live under [data/](data/). Registry: [units.html](units.html) = **0**.

Master plan: [PLAN.md](PLAN.md). Integrity: [INTEGRITY.md](INTEGRITY.md).

When data exists it will appear in `data/`, UPDATES, and the site.

---

Last updated: 27 July 2026
