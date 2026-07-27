# Public Data

Field numbers for the GroundYield pilot live here.

## Status

**No field data yet.** Foundation phase.

Baselines will be added during and after the ground trip. Until then, this folder holds schemas and empty templates so the public record has a clear home.

## Principles

See [DATA.md](../DATA.md) in the repo root:

- Real numbers, including failures
- Baseline before impact claims
- Clear units and currency
- Append updates; do not rewrite history silently

## Planned Files

| File | Purpose |
|------|---------|
| `schema-baseline.csv` | Columns for pre-intervention baseline |
| `schema-unit-season.csv` | Per-unit per-season inputs, yields, income |
| `baselines.csv` | Filled baseline rows (when collected) |
| `units.csv` | Unit registry (IDs may be anonymized) |
| `seasons/` | Season-by-season CSVs |

## Formats

- UTF-8 CSV
- Dates as ISO `YYYY-MM-DD`
- Currency labeled per column or row (e.g. `MZN`, `USD`, `ZAR`)
- Missing values left blank (not invent `0`)

---

Last updated: 27 July 2026
