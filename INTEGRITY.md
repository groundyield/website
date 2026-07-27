# Integrity & anti-fraud — from day one

**GroundYield top-level policy**  
Last updated: 27 July 2026  
**Accountable person:** Jacques Theron ([WHO.md](WHO.md))

Transparency without integrity is a marketing brochure.  
This document is **how we fight fraud, self-deception, and gaming** before the first unit is installed — not after a scandal.

Related: [CHARTER.md](CHARTER.md) · [DATA.md](DATA.md) · [WHO.md](WHO.md) · [SUPPLIERS.md](SUPPLIERS.md) · [CONSENT.md](CONSENT.md) · [GROUND_TRIP.md](GROUND_TRIP.md) · [RISK_AND_GAPS.md](RISK_AND_GAPS.md)

---

## 1. Why this is a top topic

Development and ag projects fail trust in predictable ways:

| Failure mode | What the public sees |
|--------------|----------------------|
| **Ghost units** | “60 units deployed” — few exist on the ground |
| **Baseline fraud** | Fake low baselines so any harvest looks like a win |
| **Cherry-picked yields** | Best plot published; failures private |
| **Quote / procurement fraud** | Inflated invoices, kickbacks, related-party suppliers hidden |
| **Photo theater** | Other farms’ pictures, old seasons, staged bags |
| **Money fog** | Unclear who paid, what for, and what remained |
| **Identity abuse** | Outsiders claiming to collect “for GroundYield” |
| **Silent rewrites** | Bad numbers quietly edited out of history |

We treat these as **design constraints**, not afterthoughts.

---

## 2. Non-negotiables

1. **Named accountability** — one human is responsible for published numbers (Jacques Theron, until an entity + officers exist).  
2. **Baseline before impact** — no “% increase” without a dated local baseline for that unit or explicit “placeholder / not field”.  
3. **Failures stay public** — dead ends, equipment fails, and bad seasons stay in the log.  
4. **No silent rewrites** — corrections are **dated and visible** ([UPDATES.md](UPDATES.md), note on source doc).  
5. **Truth marks** — every field number is **F** (fact) · **E** (estimate) · **H** (hearsay) when captured ([GROUND_TRIP.md](GROUND_TRIP.md)).  
6. **Money above USD 500 named** before spend on pilot activities ([WHO.md](WHO.md)).  
7. **No funder pre-clearance of results** — data publishes whether or not it flatters a funder.  
8. **Unit IDs over hero stories** — prefer reproducible rows over anonymous “success narratives”.  
9. **Anyone can challenge** — wrong number → public issue or email; we answer on the record.  
10. **Stop rules** — if asked to hide costs, fake yields, or rush land deals, we **stop** ([PARTNERSHIPS.md](PARTNERSHIPS.md), [SAFETY.md](SAFETY.md)).

---

## 3. Threat model (who might cheat, including us)

| Actor | Incentive | Controls (summary) |
|-------|-----------|-------------------|
| **Us (operator)** | Look successful; raise money later | Public ledger, correction duty, COI disclosure, no private performance reports |
| **Household / group** | Please the project; keep inputs coming | Baseline + harvest methods agreed; dual check on big claims; no humiliation-based enforcement |
| **Supplier / broker** | Inflate prices; sell wrong gear | Dated quotes, multiple sources, public cost tables, related-party disclosure |
| **Land intermediary** | Sell access they don’t control | Local legitimacy checks; no payment for land on first meeting; written access model |
| **Funder / partner** | Prefer pretty dashboards | Contractual / public rule: no pre-publication review of results |
| **Impostor** | Use our name for scams | Public contact only team@groundyield.org; “we never ask for fees to join” rule |
| **Future staff / agents** | Cut corners under pressure | This policy + unit registry + dual control on cash when team grows |

We assume **good people under pressure** will be tempted. Systems > vibes.

---

## 4. Controls by domain

### 4.1 Unit registry (ghost-unit killer)

When units exist, maintain a public registry (CSV or table) with at least:

| Field | Rule |
|-------|------|
| `unit_id` | Stable ID (e.g. `U-2026-014`) |
| Location area | Village/area — **not** home GPS by default |
| Status | planned / installed / active / paused / exited |
| Install date | ISO date or blank |
| Package version | Link to UNIT BOM revision |
| Baseline row? | Link or `none yet` |
| Notes | Failures, pauses |

**Claim rule:** We do not claim “N units deployed” above the count of registry rows with `status` in {installed, active} unless we also publish the registry snapshot date.

### 4.2 Yield & baseline integrity

| Control | Practice |
|---------|----------|
| Method written | Local unit (saco, lata…) kept; kg/ha conversion method in notes |
| Same plot | Baseline and treated yields refer to the **same unit_id** (or explicit comparison design) |
| Season labeled | Year / season string required |
| Dual evidence for headline claims | For any public “% increase” used in fundraising or press: **two** of {weigh event, photo set with date context, third-party witness, buyer receipt} |
| No retrospective baseline | Baseline dated **before** or at install — not invented after a good harvest |
| Placeholders labeled | ECONOMICS.md-style placeholders stay marked **Placeholder** until field-backed |

### 4.3 Money & procurement

| Control | Practice |
|---------|----------|
| Separate buckets | Trip ops ([TRIP_BUDGET.md](TRIP_BUDGET.md)) ≠ unit capital ([UNIT.md](UNIT.md)) |
| Quotes dated | [SUPPLIERS.md](SUPPLIERS.md) / `data/quotes-template.csv` with currency, VAT, truth mark |
| Prefer written quotes | Verbal = **E** until paper/photo of quote |
| Related parties | Disclose before buy ([WHO.md](WHO.md) COI) |
| Threshold | Sources > USD 500 named on WHO before spend |
| No “success fees” for fake data | Anyone paid for measurement must be disclosed; methods public |

### 4.4 Photos & stories

| Control | Practice |
|---------|----------|
| Consent | [CONSENT.md](CONSENT.md) / field consent script |
| Context | Prefer unit_id + approximate date in caption when public |
| No stock poverty porn | Dignity over drama |
| Challenge right | If a photo is mis-attributed, we correct publicly |

### 4.5 Identity & solicitation fraud

**GroundYield will never:**

- Ask households to pay a **registration fee** to “join the pilot” via random agents  
- Ask for WhatsApp money transfers to personal numbers as “GroundYield tax”  
- Promise government land titles we do not control  

**Public verification:**

- Official contact: **team@groundyield.org** · site **www.groundyield.org** · GitHub **groundyield/website**  
- If someone claims to represent us, tell them to email that address and wait for a reply **from that domain**  
- Report impostors: same email + GitHub issue with subject `IMPOSTOR`

### 4.6 Data pipeline integrity

| Control | Practice |
|---------|----------|
| Append-only public log | UPDATES + git history |
| Schema checks | `scripts/check-data.sh` — no EXAMPLE rows in real baselines |
| Live ≠ repo claim | `scripts/live-verify.sh` before “shipped” |
| AI advice | Chat logs private by default; no fake “AI said yield will double” marketing ([AI_AGRONOMY.md](AI_AGRONOMY.md)) |

---

## 5. Measurement protocol (minimum viable anti-fraud)

**Before install**

1. Consent conversation recorded (ticks + date).  
2. Baseline form for primary staple (F/E/H).  
3. Unit_id assigned; land access model noted (not necessarily public legal text).  

**At install**

4. Registry row → `installed` + date.  
5. Package components listed (what actually arrived vs BOM).  

**At harvest (or major claim)**

6. Yield capture with local units + method.  
7. For any **public headline** claim: second evidence type.  
8. Failures and losses logged the same week when possible.  

**Anytime**

9. Dead ends in GROUND_TRIP / SUPPLIERS — not deleted.  
10. Corrections in UPDATES within a reasonable time of discovery.

---

## 6. How to report fraud, errors, or impostors

| Situation | Channel |
|-----------|---------|
| Published number looks wrong | [GitHub issue](https://github.com/groundyield/website/issues) or team@groundyield.org |
| Possible fake unit / fake photo | Same — include links and dates |
| Someone using our name to take money | team@groundyield.org subject `IMPOSTOR` + local authorities if crime |
| COI / related-party concern | team@groundyield.org subject `COI` |
| Safety risk if public | Email first; we may delay public detail ([SAFETY.md](SAFETY.md)) |

**Commitment:** Material integrity reports get a **public response** (issue comment or UPDATES line) stating what we checked and what changed — or why we disagree — without doxxing reporters who ask for anonymity.

We do **not** currently pay cash bounties (no entity / budget line). Credit in UPDATES is available if the reporter wants it.

---

## 7. What we will not do to “look clean”

- Hide failed units to protect a Season 1 target  
- Move goalposts from “local baseline” to national averages mid-stream without an explicit, dated change  
- Use unaudited internal spreadsheets as the only source of truth while the public sees a highlight reel  
- Quietly delete git history of numbers  

Season 1 targets in the Charter are **targets**, not licenses to invent compliance.

---

## 8. Growth path (when we are more than one person)

Before hiring agents or spending significant third-party funds:

- [ ] Dual control on cash transfers above a set threshold  
- [ ] Written agent authority (what they may promise)  
- [ ] Unit registry review by someone who did not install that week  
- [ ] Periodic public “integrity note” (what was challenged, what held)  

Until then, Jacques Theron remains single-point accountability — which is **simpler to audit and easier to blame**. That is intentional.

---

## 9. Field checklist (print with forms)

From [field/FIELD_KIT.md](field/FIELD_KIT.md):

- [ ] No money ask on first community meeting  
- [ ] F/E/H on every number  
- [ ] Consent before names / faces / income  
- [ ] Quote date + currency + truth mark  
- [ ] Dead end logged if lead dies  
- [ ] Never invent `0` for missing data  
- [ ] **No live agronomy WhatsApp** until [ADVICE_SCRIPTS.md](ADVICE_SCRIPTS.md) freeze lifts  

### Process miss already owned (27 Jul 2026)

We claimed “shipped” for some site assets before live HTTP 200 during day-one deploys. Fixed same day; correction in [UPDATES.md](UPDATES.md). Tools: `scripts/live-verify.sh` before any future “live” claim.

---

## 10. One-sentence public line

> GroundYield fights fraud with named accountability, baselines before claims, public failures, dated corrections, and an open door to challenge every number — including ours.

---

Last updated: 27 July 2026
