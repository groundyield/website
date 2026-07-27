# Public Updates

**Source of truth** for the homepage Updates section and [updates.rss](updates.rss).  
Newest first. Do not silently edit old entries — append corrections.

**Process rule:** Do not claim a URL “shipped” until it returns HTTP 200 on **www.groundyield.org** (cache-bust if needed). Repo-only is not live.  
**Deploy rule:** See [DEPLOY.md](DEPLOY.md) — production must equal full `main`; partial file deploys are banned.  
**Verify:** `./scripts/live-verify.sh` (must pass before claiming live).

---

## 27 Jul 2026 — Traction strategy published

- **[TRACTION.md](TRACTION.md)** added: public promotion rules (anti-hype, evidence-first).
- Defines primary audiences, X content pillars, long-form approach, direct outreach style, and metrics we actually care about.
- Explicit bans on FOMO language, paid amplification before real data, and manufacturing progress.
- Linked from README documents table.

## 27 Jul 2026 — Correction: early “shipped” claims + charter restraint

- **Correction (append-only):** On day one, some UPDATES/site claims briefly treated assets or pages as live while production still returned 404 (partial deploys / wrong Git link). That violated our own “HTTP 200 before shipped” rule. Production now equals `groundyield/website` `main` and passes `scripts/live-verify.sh` — but the process miss stands as a real data point.
- **Charter:** Season 1 unit/yield figures restated as **aspirational design targets**, not measured results. Binding commitments are process/integrity only ([CHARTER.md](CHARTER.md)).
- **Agronomy freeze:** [ADVICE_SCRIPTS.md](ADVICE_SCRIPTS.md) / pocket scripts **must not** be sent to real farmers until agronomist + local review.
- **Money honesty:** [WHO.md](WHO.md) now states runway is not disclosed yet and describes stop scenario if self-funding ends.
- **Reality line:** zero units, zero field baselines, trip dates still open — published on the homepage deliberately.

## 27 Jul 2026 — Integrity & anti-fraud (top policy)

- **[INTEGRITY.md](INTEGRITY.md)** published as a top-level public policy: threat model (ghost units, fake baselines, cherry-picked yields, procurement abuse, photo theater, impostors), controls, measurement protocol, and how to report errors/`IMPOSTOR`.
- Charter commitment **#6 — Integrity over optics**; homepage section “Fighting fraud from day one”.
- Linked from WHO, DATA, README, field kit hard rules.
- Headline claim rule: dual evidence before using % wins in press/fundraising.

## 27 Jul 2026 — Trip ops layer (budget, safety, agreements)

- [TRIP_BUDGET.md](TRIP_BUDGET.md) — travel ops envelope separate from unit capital; actuals table empty until return.
- [SAFETY.md](SAFETY.md) — contingency, check-ins, stop rules, device/data safety (private emergency numbers stay offline).
- Field: [PACKING_LIST.md](field/PACKING_LIST.md), [DAILY_LOG.md](field/DAILY_LOG.md), [BUYER_INTERVIEW.md](field/BUYER_INTERVIEW.md).
- [UNIT_AGREEMENT_DRAFT.md](UNIT_AGREEMENT_DRAFT.md) — plain-language partnership outline (**not** a signed contract).
- `scripts/check-data.sh` validates CSV headers and blocks EXAMPLE rows in real baselines.
- Still open: fixed travel dates, filled budget numbers, inbox spot-check.

## 27 Jul 2026 — Field kit (offline ops pack)

- Full offline pack under [field/FIELD_KIT.md](field/FIELD_KIT.md): interview scripts (leader / farmer / supplier), plain-language consent, baseline paper form → CSV, WhatsApp pocket scripts.
- Printable **[field/GroundYield_Field_Forms_EN_PT.pdf](field/GroundYield_Field_Forms_EN_PT.pdf)** (4 pages): consent ticks, interview prompts, baseline blanks, quote table.
- Data templates: [data/quotes-template.csv](data/quotes-template.csv), [data/baseline-examples.csv](data/baseline-examples.csv) (example-only rows).
- GROUND_TRIP pre-trip items for interviews/baseline/consent/quotes marked ready; dates and budget still open.

## 27 Jul 2026 — Vercel Git connected to groundyield/website

- Production project **groundyield** is linked to **`github.com/groundyield/website`** (not the sluiper fork), production branch **`main`**.
- Full-tree deploy from `main` verified live: homepage, `pt.html`, robots, sitemap, RSS, favicon, OG image, icons, field PDF — all HTTP 200.
- **Correction** to the earlier deploy note: the “ops remaining” Git connect gap is **closed**. Partial file deploys remain banned ([DEPLOY.md](DEPLOY.md)).

## 27 Jul 2026 — Field one-pager (offline EN+PT)

- [field/GroundYield_Field_OnePager_EN_PT.pdf](field/GroundYield_Field_OnePager_EN_PT.pdf) — printable two-page handout for community/supplier first contact (no signal required).
- Framed: local baseline (not national averages); planning cost band not an offer of payment; named accountability; “what we are not asking today.”
- Previews + rebuild script under `field/`. Linked from the site docs list and trip checklist.

## 27 Jul 2026 — Irrigation options + live-verify script

- [IRRIGATION.md](IRRIGATION.md): per-unit kit vs shared headworks (capital + governance).
- `scripts/live-verify.sh` automates the DEPLOY.md URL checklist.
- Site documents list links IRRIGATION + DEPLOY.

## 27 Jul 2026 — Deploy process locked in docs

- **[DEPLOY.md](DEPLOY.md)** added: Git → Vercel as the only supported production path; live-verify checklist; explicit ban on partial uploads.
- README points to DEPLOY.md.
- *(Historical note at write time: Git connect + binary assets were still open. Closed the same day — see entry “Vercel Git connected…” above.)*

## 27 Jul 2026 — Full static surface + orphaned docs

- Site Public Documents links SEASON, AI_AGRONOMY, PARTNERSHIPS.
- Sitemap lists `/` and `/pt.html`.
- Homepage and `pt.html` verified live after restore.

## 27 Jul 2026 — Ops + Portuguese page + supplier/advice templates

- Notification path confirmed (GitHub merge mail to operator).
- **pt.html** Portuguese landing (must be on domain, not only GitHub).
- **SUPPLIERS.md** quote log template; **ADVICE_SCRIPTS.md** WhatsApp/SMS PT scripts v0.

## 27 Jul 2026 — Named accountability

- **Jacques Theron** published as founder / operator in WHO.md and on the site.

## 27 Jul 2026 — Trust + social assets

- WHO.md: funding rules, COI, partner table, corrections policy.
- OG/Twitter large card image, apple-touch and 512 icons, JSON-LD Organization.
- CONTRIBUTING.md, CONSENT.md, Portuguese summary (PT.md), UPDATES.md, 404 page.
- Yield-gap claim linked to published sources (FAO / national analysis range).

## 27 Jul 2026 — Economics & design stack

- UNIT.md modular BOM (~USD 1,270–2,985 Year-0 planning band).
- ECONOMICS.md, SEASON.md, AI_AGRONOMY.md, PARTNERSHIPS.md.
- Machine-readable BOM CSVs under `data/`.

## 27 Jul 2026 — Public launch

- Website, GitHub, and X live.
- PLAN, CHARTER, DATA standards published.
- Foundation phase. Ground trip planned: South Africa → Zimbabwe → Mozambique.

---

When you add an update: edit this file, mirror the top entry on `index.html`, and add an `<item>` to `updates.rss`.
