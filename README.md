# GroundYield

**Open modular high-productivity farm pilot**  
Vilanculos, Inhambane Province, Mozambique

Raising real yields on the ground. Transparent data. Community first.  
**Integrity over optics** — [INTEGRITY.md](INTEGRITY.md) (anti-fraud from day one).

## Live

| | |
|---|---|
| Website | [www.groundyield.org](https://www.groundyield.org) |
| **Doc library** | [docs.html](https://www.groundyield.org/docs.html) (grouped — not the homepage dump) |
| X | [@GroundYield](https://x.com/GroundYield) |
| Contact | [team@groundyield.org](mailto:team@groundyield.org) |
| This repo | [github.com/groundyield/website](https://github.com/groundyield/website) |
| UX rules | [SITE_UX.md](SITE_UX.md) |

Canonical host: **www**. Apex redirects to www.

## Deploy (read this)

**Production must equal this repo’s `main` branch.**  
Full rules, checklist, and failure modes: **[DEPLOY.md](DEPLOY.md)**.

- Connect Vercel project `groundyield` → GitHub `groundyield/website` → branch `main`
- **Never** upload a partial file set to production (drops `pt.html` / images)
- Do not mark updates “live” until the [DEPLOY.md](DEPLOY.md) URL checklist returns HTTP 200

## Who runs this

**Jacques Theron** — founder / operator. Self-funded; no legal entity yet.  
Prior Vilanculos-scale farming (failed/left; ~ZAR 10m operator-disclosed loss) — **[LESSONS_MZ.md](LESSONS_MZ.md)**.  
Funding, conflicts, corrections: **[WHO.md](WHO.md)**.

## Documents

**Start here:** [**PLAN.md**](PLAN.md) (master open plan) · [SYSTEM.md](SYSTEM.md) · [RISK_AND_GAPS.md](RISK_AND_GAPS.md) · [LESSONS_MZ.md](LESSONS_MZ.md) · [WHY_OTHERS_FAILED.md](WHY_OTHERS_FAILED.md) · [SECURITY_THEFT.md](SECURITY_THEFT.md) · [NEXT.md](NEXT.md)

| File | Purpose |
|------|--------|
| [**PLAN.md**](PLAN.md) | **Master open plan** — problem, package, phases, risks, doc map |
| [SYSTEM.md](SYSTEM.md) | Physical + Starlink + AI roles |
| [CHARTER.md](CHARTER.md) | Binding process vs design aims |
| [LESSONS_MZ.md](LESSONS_MZ.md) | Prior MZ farming failure → why modular/open |
| [WHY_OTHERS_FAILED.md](WHY_OTHERS_FAILED.md) | **Why many tried before — failure modes** |
| [SECURITY_THEFT.md](SECURITY_THEFT.md) | **Crime / theft / how we control assets** |
| [RISK_AND_GAPS.md](RISK_AND_GAPS.md) | **Full risk assessment · gap analysis · mitigations** |
| [INTEGRITY.md](INTEGRITY.md) | Anti-fraud (top policy) |
| [WHO.md](WHO.md) | Accountability, funding, conflicts |
| [UNIT.md](UNIT.md) | Modular unit BOM + cost bands |
| [IRRIGATION.md](IRRIGATION.md) · [ECONOMICS.md](ECONOMICS.md) · [SEASON.md](SEASON.md) | Design deep dives |
| [VALUE_AND_MONEY.md](VALUE_AND_MONEY.md) | **Why communities join · capital protection · scale funding** |
| [AI_FIELD_PATH.md](AI_FIELD_PATH.md) | **AI unfreeze path · expert panel · field phone** |
| [AI_AGRONOMY.md](AI_AGRONOMY.md) · [ADVICE_SCRIPTS.md](ADVICE_SCRIPTS.md) | Advice design (L2 send until G5-A) |
| [PARTNERSHIPS.md](PARTNERSHIPS.md) · [UNIT_AGREEMENT_DRAFT.md](UNIT_AGREEMENT_DRAFT.md) | Community / terms draft |
| [GROUND_TRIP.md](GROUND_TRIP.md) · [TRIP_BUDGET.md](TRIP_BUDGET.md) · [SAFETY.md](SAFETY.md) | Trip |
| [field/](field/) | Offline kit, contacts, Starlink approach, gates |
| [SUPPLIERS.md](SUPPLIERS.md) · [DATA.md](DATA.md) · [SOURCES.md](SOURCES.md) | Quotes & measurement |
| [KPI_AND_DATA.md](KPI_AND_DATA.md) | **KPIs, how to collect, accuracy bars** |
| [EXISTING_TOOLS.md](EXISTING_TOOLS.md) | **Existing apps (rain, planting) — don’t rebuild** |
| [REMOTE_OPS.md](REMOTE_OPS.md) | **Future: remote monitor/control (sensors, cameras)** |
| [CONSENT.md](CONSENT.md) · [CONTRIBUTING.md](CONTRIBUTING.md) | Consent & help |
| [TRACTION.md](TRACTION.md) · [OUTREACH.md](OUTREACH.md) | Attention without hype |
| [UPDATES.md](UPDATES.md) · [DEPLOY.md](DEPLOY.md) | Changelog · production |
| [PT.md](PT.md) / [pt.html](pt.html) · [day1.html](day1.html) · [units.html](units.html) | Public pages |
| [LICENSE](LICENSE) | MIT |

### After every production deploy

```bash
./scripts/ship-check.sh   # check-data + live-verify
```

CI also runs `check-data` and file presence checks on every push to `main`.

## What this is

A transparent pilot of modular farm units for smallholders:

- Solar irrigation
- Improved seeds + micro-dosing fertilizer
- AI agronomy advice (**after review** — frozen for live send now)
- Hermetic storage
- Optional poultry & goat modules
- Optional school connectivity path (Starlink) — not a farm substitute

Planning cost band (Year 0, first unit): **~$1,270–$2,985 USD** — see [UNIT.md](UNIT.md).

Everything material is published openly: design, costs, yields, incomes, and failures.  
**Master plan:** [PLAN.md](PLAN.md) · **0 units** on [units.html](https://www.groundyield.org/units.html).

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
