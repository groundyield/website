# Public Updates

**Source of truth** for the homepage Updates section and [updates.rss](updates.rss).  
Newest first. Do not silently edit old entries — append corrections.

**Process rule:** Do not claim a URL “shipped” until it returns HTTP 200 on **www.groundyield.org** (cache-bust if needed). Repo-only is not live.  
**Deploy rule:** See [DEPLOY.md](DEPLOY.md) — production must equal full `main`; partial file deploys are banned.  
**Verify:** `./scripts/live-verify.sh` (must pass before claiming live).

---

## 27 Jul 2026 — Meta: paper ≠ truth; G0.5; review freeze; proportional risk

- Honest admission: prior gap round added **process**, not field answers (checklist still open).
- **G0.5** wind-down honesty before Rumbacaca re-entry claim / trip start.
- Ceiling: 30 days after G1 must publish number or dated deferral (not infinite placeholder).
- Modular scale: **bounds $ at risk**, does **not** remove theft/water total-loss (P=12 risks).
- Relational whiplash (big-farm memory → 0.25 ha) + PT pocket line.
- **Review-loop freeze** until G0.5 or G1 or public pause — [STRATEGIC_GAPS.md](STRATEGIC_GAPS.md) §0 · [NEXT.md](NEXT.md).

## 27 Jul 2026 — Strategic gaps closed in writing (Plan B, trip scope, scars, ceiling)

- Cross-read of VALUE_AND_MONEY / LESSONS / SECURITY / WHY_FAILED surfaced **thinking** holes, not polish.
- **[STRATEGIC_GAPS.md](STRATEGIC_GAPS.md)** companion: growth **Plan B** (stop at few units if markets fail); trip = **listen-first** (no install default); LESSONS open tables for **pay/herds/land** (operator must fill — not invented); charter vs “near impossible” reconciled; selection fairness process; **financial ceiling required before unit capital**.
- Patches: VALUE_AND_MONEY, LESSONS_MZ, CHARTER, PARTNERSHIPS, GROUND_TRIP, NEXT, WHO.

## 27 Jul 2026 — Review fixes: PT parity, shared nav, scars in X/blog

- **PT:** risk/theft summary, docs library + white paper/roadmap links, recent updates teaser, shared nav.
- **Shared nav:** `site-nav.css` on public pages (home, docs, whitepaper, roadmap, units, day1, pt).
- **Scars before post:** [X_THREAD_DAY1.md](X_THREAD_DAY1.md) now includes LESSONS (~ZAR 10m / KSA / not claiming ha) as post 2/9; [BLOG_DAY1.md](BLOG_DAY1.md) + [day1.html](day1.html) scars section.
- **NEXT.md:** paper freeze — no more strategy docs this window; G1/G2 human only.
- OG image eyeballed: brand text card, no fake farm photo (OK for share).

## 27 Jul 2026 — Living white paper + proposed roadmap

- **[WHITEPAPER.md](WHITEPAPER.md)** / **[whitepaper.html](whitepaper.html)** — v0.1-draft living thesis: problem, method, current evidence (0 units), open questions. Revises with data; revision log + UPDATES.
- **[ROADMAP.md](ROADMAP.md)** / **[roadmap.html](roadmap.html)** — v0.1 proposed phases 0–3, milestones, parallel AI/Starlink/remote tracks, evidence snapshot. Checkmarks as gates close; not a forecast.
- Wired home nav, docs library, PLAN, README, sitemap, live-verify.

## 27 Jul 2026 — Site UX cleanup (less messy)

- **Problem:** homepage became a long flat dump (40+ doc links, many same-day updates) while building fast.
- **Fix:** simplified **[index.html](index.html)** — nav, short status card, **6 start paths**, short sections, ~5 latest updates only.
- **New [docs.html](docs.html)** — full library grouped (start / farm / risk / AI / field / ops).
- **[SITE_UX.md](SITE_UX.md)** — rules so we don’t re-mess the landing page. PT + units nav tightened. sitemap + live-verify include docs.html.

## 27 Jul 2026 — Remote ops path (sensors, cameras, solenoids)

- **[REMOTE_OPS.md](REMOTE_OPS.md)** — future design to track/verify units from afar (e.g. KSA): stages **R0 manual → R1 phone → R2 sensors → R3 camera → R4 solenoid control → R5 fleet**.
- Maps signals to KPIs (pump hours, soil, theft camera); AI for anomalies not fake yield; manual override always; consent for cameras; theft rules apply to shiny boxes.
- **Not** Season 0 core BOM. Prove dirt + trust first. Wired SYSTEM, UNIT optional module, PLAN, risks, homepage.

## 27 Jul 2026 — KPIs + reuse existing weather/planting apps

- **[KPI_AND_DATA.md](KPI_AND_DATA.md)** — full KPI list (process, yield, water, cost, market, theft, AI, operator); what data; how to collect; accuracy bars (e.g. area ±10%, mass ±15% for public F); phase pack for trip → season close.
- **[EXISTING_TOOLS.md](EXISTING_TOOLS.md)** — **don’t rebuild** rain satellites or generic calendars; use phone weather, Open-Meteo, CHIRPS-class context, extension calendars, pest apps as assist; GroundYield owns unit registry, baselines, costs, outcomes. AI must **name the source**.
- DATA.md, AI_FIELD_PATH, PLAN, README, homepage linked.

## 27 Jul 2026 — AI staged unfreeze (show value · experts · phone)

- **[AI_FIELD_PATH.md](AI_FIELD_PATH.md)** — how AI helps farmers **choose** (CHOICE framework); staged levels **L0–L1 open now**, **L2/L3 gated**.
- **L1:** community/school demos — phone helps options + when to ask a person; **not** live chemical rates for enrolled units.
- **Expert panel:** recruit agronomy (+ optional water/markets); ticket path when crop or AI is stuck; seats tracked on [WHO.md](WHO.md) when accepted.
- **L3 target:** instant on-phone answers when there is signal or Starlink hub Wi‑Fi, with auto-escalate on hard cases — only after **G5-B**.
- Gates split: **G5-A** (reviewed send) / **G5-B** (instant + experts). SYSTEM, ADVICE_SCRIPTS, AI_AGRONOMY, PLAN, NEXT, risks updated. Honest: panel **not staffed yet**.

## 27 Jul 2026 — Full risk assessment + gap analysis

- **[RISK_AND_GAPS.md](RISK_AND_GAPS.md)** — scored risk register (strategy, community/land, theft, agronomy, markets, finance, integrity, AI/Starlink, trip); trap map from history; gap table vs G0–G6; trip actions §5.1; **hard checklist before unit capital** §5.2; kill criteria; residual risks we accept; one-page operator card.
- Wired from PLAN §9, GATES, NEXT, README, homepage, failure/theft docs. Re-score after field trip.

## 27 Jul 2026 — Why others failed + theft control

- **[WHY_OTHERS_FAILED.md](WHY_OTHERS_FAILED.md)** — synthesis of why many agri attempts in Mozambique failed: logistics, cost ramps, land conflict, skills, thin markets, mega-programme under-delivery, and **solar/pump theft**.
- **[SECURITY_THEFT.md](SECURITY_THEFT.md)** — first-class asset control: stake before steel, earn>steal, moveable kit, serials, annex clauses, incident path, trip checklist. No armed-guard brand as default; no guarantee of zero crime.
- **[SOURCES.md](SOURCES.md)** expanded with citable entry points (Mosagrius/Ecology & Society; Energypedia/Practica solar barriers — theft + training failure).
- Wired into PLAN risks/doc map, UNIT design principles, SAFETY, VALUE_AND_MONEY, LESSONS_MZ, GATES, README, homepage.

## 27 Jul 2026 — Community value + money model

- **[VALUE_AND_MONEY.md](VALUE_AND_MONEY.md)** — from the community’s POV: why work with us, what’s in it for them, what protects capital/operator, how surplus and open replication fund the next community.
- Ownership models A–D (grant pilot, co-invest, loan kit, phased transfer). Forbidden: debt traps, fake yields for grants, join-up fees.
- Linked from PLAN, ECONOMICS, PARTNERSHIPS, UNIT_AGREEMENT, README, homepage, PT summary.

## 27 Jul 2026 — Portuguese site review + pt.html parity

- Full PT audit: [docs/PT_REVIEW.md](docs/PT_REVIEW.md).
- **Finding:** [PT.md](PT.md) was mostly honest; **[pt.html](pt.html)** lagged badly (status, scars, freeze, PLAN/LESSONS, doc list).
- **Fix:** rebuild pt.html to match EN critical claims (zero units, Rumbacaca, ~ZAR 10m disclosure, AI freeze, design aims, master plan links).
- Deep technical docs remain English with PT entry points (intentional). Optional next: PLAN/CHARTER/WHO/LESSONS short PT packs for field paper.

## 27 Jul 2026 — Master open plan consolidation (gap fix)

- **[PLAN.md](PLAN.md)** rewritten as the **master open plan**: status snapshot, mission, package, binding vs aims, phases with exit criteria, risks/gaps, capital/time honesty, full doc map, success/failure definitions, non-goals.
- Aligned with [CHARTER.md](CHARTER.md), [SYSTEM.md](SYSTEM.md), [LESSONS_MZ.md](LESSONS_MZ.md), [field/GATES.md](field/GATES.md).
- [README.md](README.md) doc table de-duplicated; start-here pointers. [PT.md](PT.md) brought in line (0 units, aspirational metas, Rumbacaca, freeze).
- Homepage roadmap + PLAN link updated. Remaining work is field execution, not more plan chapters.

## 27 Jul 2026 — Operator history: prior MZ scale farming failure

- **[LESSONS_MZ.md](LESSONS_MZ.md)** — Jacques discloses prior Vilanculos-area farming (~3,500 ha own era), Toro Ranch partnership context (much larger scale, livestock, national delivery), exit ~5 years post-COVID (costs + bad choices), operator-disclosed loss order **~ZAR 10 million**.
- **Not a claim of current control** of those hectares or businesses. GroundYield registry remains **0 units**.
- Return focus: **Rumbacaca** community (existing trust). Current livelihood: HSE shutdowns, Anabeeb, KSA.
- WHO + homepage updated. Design implication: modular + open because empire-scale opaque farming already failed once.
- X copy: [X_RETURN.md](X_RETURN.md).

## 27 Jul 2026 — SYSTEM.md: what we do + Starlink + AI roles

- **[SYSTEM.md](SYSTEM.md)** — single map of physical farm units, connectivity (school-first Starlink hubs), and AI (ops now; farmer advice only after G5).
- Four layers: physical → connectivity → intelligence → public truth. Offline field kit stays first-class.
- Starlink: education hubs + later data upload; not a substitute for irrigation/seed. AI: draft/triage with human veto; freeze unchanged.
- PLAN.md phases updated to match. Deep dives remain STARLINK_APPROACH + AI_AGRONOMY.

## 27 Jul 2026 — Starlink approach (rural schools first)

- **[field/STARLINK_APPROACH.md](field/STARLINK_APPROACH.md)** — how to engage Starlink without overpromising communities.
- Model: school-first connectivity pilot (1–3 sites), education partner + power plan + public metrics; farm data upload is secondary.
- Constraints: confirm MZ coverage, power, who pays month 13; no free-dish promises before written path.
- Ready email draft to Starlink Business + honest PT/EN script for schools.
- **No Starlink agreement exists.**

## 27 Jul 2026 — Local businesses contact list (desk)

- **[field/LOCAL_CONTACTS.md](field/LOCAL_CONTACTS.md)** — walk/call list for Vilanculos (hardware, market agro, lodges/restaurants for offtake, extension), Inhambane, Maputo national, SA corridor.
- First-15 walk-ins prioritized for week 1 on the ground.
- All leads **H/secondary** — verify in person; quotes still zero until written prices land in SUPPLIERS.

## 27 Jul 2026 — Ground window next ~2 weeks + X field post pack

- Operator states presence on the corridor within **the next ~2 weeks** (provisional **~27 Jul – 10 Aug 2026**; day-by-day still open).
- [GROUND_TRIP.md](GROUND_TRIP.md): status → field window opening; decision log B (full corridor, may compress); public log line dated.
- **[X_FIELD_2WEEKS.md](X_FIELD_2WEEKS.md)**: leaving posts, daily field-note template, quote/meeting/baseline/dead-end variants, end wrap — honesty-first, no yield claims.
- Homepage status updated. Still zero units / zero baselines until measured.
- X cadence: Day-1 thread (if not posted) → leaving posts → daily notes while on the ground.

## 27 Jul 2026 — Big-wins board: quote-request pack, trip scenarios, X follow-ups

- **[NEXT.md](NEXT.md)** rewritten as ranked big wins + 7-day sprint (human actions over more docs).
- **[field/QUOTE_REQUESTS.md](field/QUOTE_REQUESTS.md)** — ready-to-send quote emails for irrigation/seed/storage leads (G2 path).
- **[X_FOLLOWUPS.md](X_FOLLOWUPS.md)** — post-launch X posts (integrity, irrigation, stage, asks).
- **[GROUND_TRIP.md](GROUND_TRIP.md)** — trip scenarios A/B/C decision helper + public log table.
- **[TRIP_BUDGET.md](TRIP_BUDGET.md)** — how to fill envelope without inventing authority.
- Production/share cards already green; next leverage is post + outbound.

## 27 Jul 2026 — Asset re-verify + PDF fix + supplier desk leads

- **Assets re-checked with curl (not tool sandbox):** `/favicon.svg`, `/og-image.png`, `/apple-touch-icon.png`, `/icon-512.png` return HTTP 200, correct `Content-Type`, valid magic bytes, and **byte-match** repo files. The third “assets are 404” report appears to be a **false positive** from a fetch environment that mishandles binary bodies — not a production outage.
- **Real bug fixed:** `field/GroundYield_Field_OnePager_EN_PT.pdf` had been stored/served as **base64 text** (`JVBER…`) instead of binary PDF. Decoded to valid `%PDF-1.4` (2 pages, extractable text). Forms PDF was already valid.
- **`live-verify.sh` hardened:** checks Content-Type + magic bytes for PNG/PDF; fails if PDF body is base64.
- **[SUPPLIERS.md](SUPPLIERS.md):** desk research **leads** (Futurepump, Lorentz, SEMOC, PICS, GrainPro, etc.) labeled H/secondary — **not quotes**, no prices. Call list for G2.

## 27 Jul 2026 — Next board, day1.html, PT launch, contact log

- **[NEXT.md](NEXT.md)** — ordered human actions to unlock G1 (intro) and G2 (quote); success metrics for the week.
- **[/day1.html](day1.html)** — shareable HTML of the day-one essay (OG tags) for X/long-form link.
- **[X_THREAD_DAY1_PT.md](X_THREAD_DAY1_PT.md)** — short Portuguese launch copy.
- **[field/CONTACT_LOG.md](field/CONTACT_LOG.md)** — public-safe outreach tracking (no private phones in git).
- Desk work is not the bottleneck; posting + outreach is.

## 27 Jul 2026 — Launch pack: OUTREACH + X thread + day-one blog

- **[OUTREACH.md](OUTREACH.md)** — promote process/honesty, not unproven charter numbers; specific non-money asks; ship-check gate before posting.
- **[X_THREAD_DAY1.md](X_THREAD_DAY1.md)** — 8-post launch thread (≤280), AI disclosure as its own beat, unit registry = 0.
- **[BLOG_DAY1.md](BLOG_DAY1.md)** — long-form day-one post including adversarial-review findings and AI disclosure.
- Linked from TRACTION + README + homepage docs. **Do not log “thread live” until the X URL exists.**

## 27 Jul 2026 — Ops rails: unit registry page, CI, ship-check, outreach

- **[/units.html](units.html)** — public unit registry with count **0** (ghost-unit killer; no rows until install).
- **GitHub Actions CI** — `scripts/check-data.sh` + required file list on every push/PR.
- **`scripts/ship-check.sh`** — data + production live-verify before any “shipped” claim.
- **[field/OUTREACH_EMAIL.md](field/OUTREACH_EMAIL.md)** — intro emails for leaders/suppliers/buyers (not agronomy).
- **[field/GATES.md](field/GATES.md)** — advance gates G0–G6; currently G0 only.
- Sitemap includes units + field PDFs.

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
