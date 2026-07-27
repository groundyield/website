# GroundYield

**Open modular high-productivity farm pilot**  
Vilanculos, Inhambane Province, Mozambique

Raising real yields on the ground. Transparent data. Community first.  
**Integrity over optics** — [INTEGRITY.md](INTEGRITY.md) (anti-fraud from day one).

## Live

| | |
|---|---|
| Website | [www.groundyield.org](https://www.groundyield.org) |
| X | [@GroundYield](https://x.com/GroundYield) |
| Contact | [team@groundyield.org](mailto:team@groundyield.org) |
| This repo | [github.com/groundyield/website](https://github.com/groundyield/website) |

Canonical host: **www**. Apex redirects to www.

## Deploy (read this)

**Production must equal this repo’s `main` branch.**  
Full rules, checklist, and failure modes: **[DEPLOY.md](DEPLOY.md)**.

- Connect Vercel project `groundyield` → GitHub `groundyield/website` → branch `main`
- **Never** upload a partial file set to production (drops `pt.html` / images)
- Do not mark updates “live” until the [DEPLOY.md](DEPLOY.md) URL checklist returns HTTP 200

## Who runs this

**Jacques Theron** — founder / operator. Self-funded; no legal entity yet.  
Full funding rules, conflicts, and corrections policy: **[WHO.md](WHO.md)**.

## Documents

| File | Purpose |
|------|--------|
| [PLAN.md](PLAN.md) | Full public plan — problem, approach, phases |
| [CHARTER.md](CHARTER.md) | Binding public commitments and Season 1 targets |
| [UNIT.md](UNIT.md) | Modular Unit v0 — BOM + cost bands |
| [IRRIGATION.md](IRRIGATION.md) | Per-unit vs shared irrigation design |
| [ECONOMICS.md](ECONOMICS.md) | Illustrative unit economics (not forecasts) |
| [SEASON.md](SEASON.md) | Crop & season calendar |
| [AI_AGRONOMY.md](AI_AGRONOMY.md) | Phone/AI advice design |
| [PARTNERSHIPS.md](PARTNERSHIPS.md) | Community & land principles |
| [WHO.md](WHO.md) | Accountability, funding, conflicts |
| [**INTEGRITY.md**](INTEGRITY.md) | **Anti-fraud & integrity (top policy)** |
| [**TRACTION.md**](TRACTION.md) | **How we seek attention without hype** |
| [PT.md](PT.md) / [pt.html](pt.html) | **Resumo em português** (site + markdown) |
| [SUPPLIERS.md](SUPPLIERS.md) | Quote log template for field prices |
| [ADVICE_SCRIPTS.md](ADVICE_SCRIPTS.md) | WhatsApp/SMS scripts (PT) v0 |
| [CONSENT.md](CONSENT.md) | Privacy, consent, safeguarding |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to help |
| [DATA.md](DATA.md) | What we measure and how we publish it |
| [SOURCES.md](SOURCES.md) | Citations for public claims |
| [UPDATES.md](UPDATES.md) | Changelog (source of truth) |
| [GROUND_TRIP.md](GROUND_TRIP.md) | Trip checklist (SA → ZW → MZ) |
| [TRIP_BUDGET.md](TRIP_BUDGET.md) | Travel ops budget envelope |
| [SAFETY.md](SAFETY.md) | Trip safety & contingency |
| [UNIT_AGREEMENT_DRAFT.md](UNIT_AGREEMENT_DRAFT.md) | Partnership outline (draft, not a contract) |
| [field/](field/) | **Offline field kit** — PDFs, interviews, forms |
| [DEPLOY.md](DEPLOY.md) | **How production is deployed (Git → Vercel)** |
| [data/](data/) | CSV schemas + BOM tables |
| [LICENSE](LICENSE) | MIT — open by design |

### After every production deploy

```bash
./scripts/live-verify.sh
./scripts/check-data.sh
```

## What this is

A transparent pilot of modular farm units for smallholders:

- Solar irrigation
- Improved seeds + micro-dosing fertilizer
- AI agronomy advice
- Hermetic storage
- Optional poultry & goat modules

Planning cost band (Year 0, first unit): **~$1,270–$2,985 USD** — see [UNIT.md](UNIT.md).

Everything is published openly: design, costs, yields, incomes, and failures.

## Public Charter (Season 1)

- 30–60 modular units in Vilanculos
- Target 80–100%+ yield increase on staples vs **local baseline**
- Raise household income via cash crops + poultry
- Full public data from day one
- Replicable open model

## Repo layout

| Path | Notes |
|------|--------|
| `index.html` | Public landing page (static) |
| `pt.html` | Portuguese landing |
| `404.html` | Not-found page |
| `CNAME` | Preferred host `www.groundyield.org` (live host is Vercel) |
| `og-image.png` | 1200×630 social share card |
| `favicon.svg`, `apple-touch-icon.png`, `icon-512.png` | Icons |
| `vercel.json` | Static headers |
| `DEPLOY.md` | Deploy rules |

## Local preview

```bash
npx serve .
```

Open `http://localhost:3000` (or the port shown).

## Status

**Foundation phase.**  
Public identity, unit design, economics, trust docs, and Portuguese summary are in the repo and on the site surface.  
**Ops:** keep Vercel Git-linked to `main` so production cannot drift.  
Next: ground trip, land, community, baselines, real supplier quotes.

---

Open by design. 2026.
