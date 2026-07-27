# Irrigation design options v0

**GroundYield** — how water gets to the modular unit.  
Last updated: 27 July 2026

Planning notes only. Real depths, salinity, and quotes from the ground trip replace this ([SUPPLIERS.md](SUPPLIERS.md), [UNIT.md](UNIT.md)).

---

## Why this doc exists

Irrigation is the **largest capital line** in the core modular unit (~USD 950–2,200 in UNIT v0). Two architectures are on the table:

1. **Per-unit kit** — every modular unit has its own solar + pump  
2. **Shared headworks** — one stronger solar/pump serves 2–6 nearby plots  

Economics and social rules differ. Season 1 may mix both if land layout forces it.

---

## Option A — Per-unit kit (default in UNIT.md)

| | |
|--|--|
| **What** | Solar array + pump + controller sized for **one** 0.25–0.5 ha unit |
| **Pros** | Simple ownership; failure isolation; easy public unit-level accounting |
| **Cons** | Higher capital per ha if many small plots; underused capacity on small beds |
| **Best when** | Plots are scattered; tenure is household-by-household; trust for sharing is low |
| **Cost anchor** | UNIT mid irrigation ~USD 1,500 |

### Design rules (A)

- Size to **peak dry-season** demand for planned crop mix, not rainy-season luck  
- Record well/surface source, static water level, and pump type in unit notes  
- Publish install quote vs UNIT band after first install  

---

## Option B — Shared headworks + plot laterals

| | |
|--|--|
| **What** | One solar + pump station; buried/main line; valves to **N** modular units (target N = 2–6) |
| **Pros** | Lower capital **per unit** if layout is compact; better pump efficiency at scale |
| **Cons** | Scheduling conflict; repair politics; harder failure attribution in public data |
| **Best when** | Contiguous land (association or family cluster); written water-sharing rules exist |
| **Cost sketch** | Headworks ~1.5–2.5× single kit; laterals cheaper per plot — **only quote after layout** |

### Design rules (B)

- **Written rotation schedule** before install (who irrigates when)  
- Each unit keeps a **meter or timed log** so public data stays per unit  
- Failures: distinguish headworks outage vs plot lateral failure in the log  
- Exit: a household leaving the cluster must not strand others without a plan  

### Illustrative split (not a quote)

| Item | Shared? | Notes |
|------|---------|--------|
| Solar + pump + controller | Yes | Sized for N plots peak |
| Main line + filters | Yes | |
| Plot valve + drip/sprinkler | No (per unit) | Unit BOM opex/capex |
| Install labour | Split | Public cost share rule |

If mid single-unit kit is ~USD 1,500 irrigation:

| N plots sharing | Headworks est. (rough) | Per-unit share of headworks |
|-----------------|------------------------|-----------------------------|
| 1 | 1,500 | 1,500 |
| 3 | 2,400–3,200 | 800–1,100 |
| 5 | 3,000–4,000 | 600–800 |

**These are order-of-magnitude only.** Field quotes override.

---

## Decision checklist (ground trip)

- [ ] Plot map: distances between candidate units (m)  
- [ ] Water source: type, depth/reliability, quality (salinity if coastal)  
- [ ] Tenure: can a shared pump sit on “neutral” or association land?  
- [ ] Preference of households: own kit vs share  
- [ ] Quote **both** Option A kit and Option B headworks if layout allows  
- [ ] Update [UNIT.md](UNIT.md) + [ECONOMICS.md](ECONOMICS.md) with real numbers  

---

## Public data implications

| Architecture | Unit ID still required? | Cost reporting |
|--------------|-------------------------|----------------|
| A per-unit | Yes | Capex on that unit |
| B shared | Yes | Headworks cost allocated (state rule: equal split / by area / by hours) |

Never hide shared subsidies inside “unit cost” without labeling.

---

## Related

- [UNIT.md](UNIT.md) — default BOM  
- [ECONOMICS.md](ECONOMICS.md) — payback sensitivity to capital  
- [SUPPLIERS.md](SUPPLIERS.md) — quote log  
- [PARTNERSHIPS.md](PARTNERSHIPS.md) — community rules  
- [GROUND_TRIP.md](GROUND_TRIP.md) — field checklist  

**Status:** v0 design choice doc — no install yet.
