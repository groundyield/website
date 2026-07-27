# Unit Economics v0

**GroundYield public planning model**  
Last updated: 27 July 2026

This document turns [UNIT.md](UNIT.md) cost bands into **illustrative** income and payback scenarios.  
**These are not forecasts and not promises.** They exist so partners can stress-test assumptions before field data replaces them.

Currency: **USD** unless noted. Exchange for MZN will be restated when we publish real quotes.

---

## 1. Cost anchors (from UNIT.md)

| Scenario | Year-0 package (irrigation + S1 inputs + storage + advice + 15% contingency) |
|----------|-----------------------------------------------------------------------------|
| Low | ~$1,270 |
| Mid | ~$2,025 |
| High | ~$2,985 |

Optional poultry module: **+$195 – $510** (not in core payback unless activated).

Plot size assumption: **0.25 – 0.5 ha** per modular unit.

---

## 2. Yield & price assumptions (placeholders)

Replace every row with Vilanculos field numbers after baseline collection.

### Maize (staple illustration)

| Variable | Conservative | Base | Optimistic | Source status |
|----------|--------------|------|------------|---------------|
| Baseline yield | 0.8 t/ha | 1.2 t/ha | 1.5 t/ha | **Placeholder** |
| Treated yield | 1.6 t/ha | 2.4 t/ha | 3.0 t/ha | **Placeholder** (~100% uplift at base) |
| Farm-gate price | $150 / t | $200 / t | $250 / t | **Placeholder** |
| Area in maize | 0.25 ha | 0.30 ha | 0.35 ha | Design choice |

*Charter target is 80–100%+ vs **local baseline**, not vs these placeholders.*

### Irrigated vegetables (cash illustration)

| Variable | Conservative | Base | Optimistic | Source status |
|----------|--------------|------|------------|---------------|
| Net margin / season (0.1–0.2 ha beds) | $150 | $350 | $700 | **Placeholder** |
| Seasons per year (with irrigation) | 1 | 2 | 3 | Depends on water + labor |

Tourism demand in Vilanculos can support higher prices **only if** access and quality are real — verify on trip.

---

## 3. Simple annual cash illustration (base case)

**Not a business plan.** One possible mid configuration:

| Line | USD |
|------|-----|
| Incremental maize gross value (0.3 ha × 1.2 t/ha extra × $200/t) | 72 |
| Vegetable net margin (2 seasons × $350) | 700 |
| **Illustrative incremental gross margin** | **~772** |
| Season operating costs (seed, fert, labor, advice — mid) | ~220 |
| **Illustrative annual surplus vs doing nothing** | **~550** |

Against mid Year-0 capital **~$2,025**:

| Metric | Illustration |
|--------|----------------|
| Simple payback (surplus ÷ capital) | ~3.7 years |
| If vegetable channel is weak (surplus ~$200/yr) | ~10 years |
| If high case margins (~$1,200/yr surplus) | ~1.7 years |

**Takeaway for design:** irrigation capital only pays if **cash crops + reliable water + markets** work. Staple yield gains alone may not repay solar kits quickly — they still matter for food security and charter impact.

---

## 4. Decision rules (public)

1. **Do not scale to 30–60 units** on capital payback stories without Season 1 field economics.  
2. Publish **actual** costs and incomes per unit; retire this v0 model in place.  
3. Separate **impact metrics** (yield, food, resilience) from **cash payback**.  
4. If mid-case surplus &lt; $200/year after Season 1, redesign package (cheaper pump, shared irrigation, different crop mix) **openly**.  
5. Poultry module judged on its own cycle economics, not rolled into crop miracles.

---

## 5. Sensitivity (what moves the needle)

| Lever | Effect |
|-------|--------|
| Pump / solar kit price | Dominant capital driver |
| Dry-season vegetable access to hotels/markets | Dominant revenue driver |
| Water reliability | Caps seasons per year |
| Post-harvest loss reduction | Improves staple calories + sellable grain |
| Fertilizer price shocks | Hits operating margin fast |
| Shared irrigation across plots | Can cut per-unit capital |

---

## 6. What we will publish instead of this doc (later)

| Artifact | When |
|----------|------|
| Real BOM quotes (CSV) | After ground trip |
| `data/baselines.csv` | Before intervention claims |
| Per-unit season P&amp;L | Each season close |
| Cohort summary (30–60 units) | End of Season 1 |

---

## 7. Worked example template (blank)

```
Unit ID:
Area (ha):
Capital spent (USD):
Operating cost season (USD):
Baseline yield (crop, unit):
Season yield:
Gross sales (USD):
Home consumption value (optional):
Net (sales − operating):
Notes / failures:
```

Copy into season logs under `data/` when live.

---

**Status:** v0 — transparent planning fiction until field data  
**Related:** [UNIT.md](UNIT.md) · [SEASON.md](SEASON.md) · [CHARTER.md](CHARTER.md) · [DATA.md](DATA.md)
