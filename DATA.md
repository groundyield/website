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

## Current Status

No field data yet.  
Foundation phase — baselines will be collected during and after the ground trip.

**Planning tables (not field measurements):**
- [`data/unit-bom-v0.csv`](data/unit-bom-v0.csv) — modular unit BOM bands
- [`data/unit-cost-summary-v0.csv`](data/unit-cost-summary-v0.csv) — Year-0 low/mid/high totals
- Narrative: [UNIT.md](UNIT.md), [ECONOMICS.md](ECONOMICS.md)

When field data exists it will appear under `data/` and on the website Updates section.

---

Last updated: 27 July 2026
