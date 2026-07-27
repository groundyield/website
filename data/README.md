# Public Data

Field numbers for the GroundYield pilot live here.

## Status

**No real field data yet.** Foundation phase.

Baselines and quotes will be added during and after the ground trip. This folder holds **schemas and empty templates** so the public record has a clear home.

## Principles

See [DATA.md](../DATA.md):

- Real numbers, including failures  
- Baseline before impact claims  
- Clear units and currency  
- Append updates; do not rewrite history silently  
- Prefer unit IDs over full names ([CONSENT.md](../CONSENT.md))  
- Integrity / anti-fraud rules: [INTEGRITY.md](../INTEGRITY.md)

## Files

| File | Purpose |
|------|---------|
| `schema-baseline.csv` | Header for pre-intervention baseline rows |
| `baseline-examples.csv` | **EXAMPLE-ONLY** rows showing shape — not real yields |
| `schema-unit-registry.csv` | Ghost-unit killer — planned/installed/active units ([INTEGRITY.md](../INTEGRITY.md)) |
| `schema-unit-season.csv` | Per-unit per-season inputs, yields, income |
| `quotes-template.csv` | Dated supplier quotes (machine-readable) |
| `unit-bom-v0.csv` | Modular unit BOM (planning) |
| `unit-cost-summary-v0.csv` | Cost band summary (planning) |
| `baselines.csv` | *(create when first real row exists)* |
| `quotes-YYYY-MM.csv` | *(optional monthly quote exports)* |

## Formats

- UTF-8 CSV  
- Dates as ISO `YYYY-MM-DD`  
- Currency labeled (`MZN`, `USD`, `ZAR`)  
- Missing values left **blank** (never invent `0`)  
- Truth marks in notes when useful: **F** fact · **E** estimate · **H** hearsay  

## Offline capture

Paper forms and interview scripts: [field/FIELD_KIT.md](../field/FIELD_KIT.md)

---

Last updated: 27 July 2026
