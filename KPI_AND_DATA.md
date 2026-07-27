# KPIs & data collection

**What we measure · how we collect · how accurate it must be**  
Last updated: 27 July 2026  
**Status:** Field-ready spec · **0** field rows yet · truth marks **F / E / H** bind all numbers  

Related: [DATA.md](DATA.md) · [INTEGRITY.md](INTEGRITY.md) · [CHARTER.md](CHARTER.md) · [field/BASELINE_FORM.md](field/BASELINE_FORM.md) · [AI_FIELD_PATH.md](AI_FIELD_PATH.md) · [EXISTING_TOOLS.md](EXISTING_TOOLS.md) · [SOURCES.md](SOURCES.md) · [CONSENT.md](CONSENT.md)

---

## 0. Rules before any KPI claim

| Rule | Meaning |
|------|---------|
| **No % yield claim without baseline** | Gate **G3** — local baseline for that unit |
| **No unit count without registry** | Gate **G6** — [units.html](https://www.groundyield.org/units.html) + CSV |
| **Truth marks** | **F** = measured/observed · **E** = estimate · **H** = hearsay |
| **Dual evidence for headlines** | Photo + number, or second witness, for big public claims ([INTEGRITY](INTEGRITY.md)) |
| **Consent** | Personal names/photos only with consent |
| **Don’t invent app precision** | Weather from an app is **H or E** until checked against a local gauge or multi-source agree |

---

## 1. KPI list (by purpose)

### A. Trust & process (always on — even at 0 units)

| KPI ID | KPI | Why | Target (Season 0–1) | Data needed | How collect | Accuracy needed |
|--------|-----|-----|---------------------|-------------|-------------|-----------------|
| **P1** | Public unit count | Anti ghost units | = registry rows | `unit_id`, status, install date | Registry CSV + units.html same week as install | **Exact count F** — zero tolerance for inflation |
| **P2** | Baseline coverage | Anti fake uplift | 100% of claimed impact units | Baseline row per unit_id | [BASELINE_FORM](field/BASELINE_FORM.md) → CSV | Method + date **required**; value may be E if farmer recall |
| **P3** | Quote coverage | Real costs | ≥1 priced quote before G2 band update | Supplier, item, price, date, currency | Photo of quote + SUPPLIERS row | Price **F** as written; delivery may be E |
| **P4** | Integrity incidents | Trust | Publish each material one | Date, type, correction | UPDATES + issue | Factual log, not polished |
| **P5** | Gate honesty | No skip | G0–G6 match public claims | Checklist | [GATES.md](field/GATES.md) | Binary F |

### B. Household / agronomy outcomes (only after units)

| KPI ID | KPI | Why | Design aim (not guarantee) | Data needed | How collect | Accuracy needed |
|--------|-----|-----|----------------------------|-------------|-------------|-----------------|
| **Y1** | Staple yield (kg/ha or local unit) | Core impact | Test large uplift vs **local** baseline | Crop, area, harvest mass or bags, moisture if possible | Weigh bags or count standard bags × known kg; area paced/measured | **Area ±10%**; **mass ±15%** for public F; else mark E |
| **Y2** | Yield vs baseline (%) | Headline metric | Only after Y1 + baseline | Both seasons methods comparable | Same unit method if possible | Report **range** if E; never fake precision |
| **Y3** | Cash-crop yield / volume | Income path | Market-dependent | Crop, kg sold + retained | Sales note + residual estimate | Sold kg **F** if receipt/count; retained often E |
| **Y4** | Crop failure / write-off | Honesty | Publish rate | Area lost, cause | Photo + note | Cause may be H/E; area F if measured |
| **W1** | Irrigation events / season | Did water happen? | Log use | Date, hours or mm estimate, source | Farmer log or simple tick sheet | Count of events **F** if logged same week; mm usually E |
| **W2** | Water source reliability | Feasibility | Functional through dry spell | Dry-ups, depth notes | Interview + observation | F when observed dry; E for depth without measure |
| **I1** | Input cost per unit / season | Economics | Within quoted band ±30% first season | Seed, fert, fuel/solar opex, labor, other | Receipts + farmer recall | Receipts F; recall E; always currency + date |
| **I2** | Capex actual vs quote | Procurement | Variance public | BOM lines | Invoices vs SUPPLIERS | Line **F** when invoice |
| **M1** | Farm-gate price | Offtake reality | Log local prices | Crop, unit, price, place, date | Buyer interview / market walk | **F** that day/place only — not national |
| **M2** | Cash income from unit | Household | Positive contribution *if* market works | Sales revenue − variable costs (simple) | Notebook + consent | Revenue F if counted; profit often E |
| **L1** | Post-harvest loss % | Storage module | Directionally down vs baseline story | Loss estimate method | Hermetic bag count / spoilage note | Usually **E** — say so |
| **T1** | Theft / vandalism incidents | Security design | 0 preferred; publish if >0 | Asset, serial, date | [SECURITY_THEFT](SECURITY_THEFT.md) path | Incident **F**; value band E OK |
| **T2** | Kit uptime (days working / days intended) | Ops quality | High after training | Breakdown days | Simple outage log | F if logged weekly |

### C. Advice / AI / connectivity (if used)

| KPI ID | KPI | Why | Target | Data needed | How collect | Accuracy |
|--------|-----|-----|--------|-------------|-------------|----------|
| **A1** | Enrolled units on advice channel | Reach | Only real enrollees | unit_id, channel, consent date | Ops list (private) + public count | Exact F |
| **A2** | Reply / engagement rate | Usefulness proxy | Track only | Messages sent vs replies | Channel stats | F counts |
| **A3** | Usefulness score (1–5) | Farmer view | Survey end season | Score + free text | 3-question survey | Self-report E |
| **A4** | Harm / bad-advice flags | Safety | 0 serious; all published | Incident note | Expert/ops log | F count |
| **A5** | Expert ticket SLA | Panel works | e.g. % answered &lt;48h | Open/close times | Ticket sheet | F timestamps |
| **A6** | External app used (name/version) | Don’t double-build | Log what farmers use | App name, purpose | Interview | F name |
| **C1** | Starlink hub hours (if any) | Connectivity claim | Written metrics | Hours available / month | School log | F if logged |

### D. Operator / pilot health

| KPI ID | KPI | Why | Data | Collect | Accuracy |
|--------|-----|-----|------|---------|----------|
| **O1** | Days on ground / year | Remote risk | Calendar | GROUND_TRIP | F |
| **O2** | Capital spent on units (band) | Runway honesty | Totals | Private ledger → public band when set | F when published |
| **O3** | Stop-rule triggers | Safety | Event log | SAFETY / UPDATES | F |

---

## 2. Minimum data pack (what to collect when)

### Phase 0 — this trip (no unit yet)

| Collect | Tool | Mark | KPI |
|---------|------|------|-----|
| Intro / meeting log | GROUND_TRIP | F | P5 / G1 |
| ≥1 supplier quote | SUPPLIERS + photo | F | P3 / G2 |
| Farmer recall yield (bags, area story) | BASELINE_FORM | E or H | path to P2 |
| Market / lodge price sample | BUYER_INTERVIEW | F that day | M1 |
| Theft pattern notes | SECURITY checklist | H/E | T1 design |
| Water source observation | Notes + photo | F/E | W2 |
| What apps people already use | Interview | F names | A6 |

### Before / at first install

| Collect | Mark | KPI |
|---------|------|-----|
| unit_id, GPS band or village (privacy-min), area_ha | F | P1 |
| Baseline yield method + value | E→F over time | P2, Y2 |
| Serials photos of kit | F | T1 |
| Capex actuals | F/E | I2 |
| Consent for advice channel | F | A1 |

### Through season

| Collect | Frequency | KPI |
|---------|-----------|-----|
| Planting date | Once | Y*, A6 (vs app calendar) |
| Irrigation log | Weekly tick | W1 |
| Input costs | When bought | I1 |
| Pest/disease events + photos | As needed | Y4, A4 |
| Rain notes (local) | Weekly or event | Compare to apps |
| Sales | When sold | M1, M2 |
| Failures | Same week | Y4, T2 |

### Season close

| Collect | KPI |
|---------|-----|
| Harvest mass / bags | Y1 |
| Loss estimate | L1 |
| Income simple | M2 |
| Usefulness survey if AI used | A3 |
| Public season row | schema-unit-season |

---

## 3. Accuracy standards (plain language)

| Claim type | Minimum bar | If you can’t meet it |
|------------|-------------|----------------------|
| “N units deployed” | Registry F exact | Don’t say N |
| “Yield +X%” | Baseline + treated, comparable method; state F/E | Say “not measured” |
| “Costs $X” | Quote or invoice date + currency | Planning band only, labeled |
| “Rain was low” | Local note or multi-source weather E | Don’t blame weather without source |
| “AI improved yield” | **Never sole cause** — package + weather + market | Report engagement/harm only |
| “Market price is X” | Date + place F | Don’t nationalize one quote |
| Theft value | Serial + photo F; $ band E OK | Still publish incident |

**Rounding:** money to whole currency unit; yields to sensible kg (not fake decimals); % to whole number unless measured carefully.

**Area:** pace  or tape preferred; phone GPS area is **E** until calibrated.

**Bags → kg:** use local standard bag weight **stated** (e.g. “50 kg bag as sold”) — if unknown, keep bags and mark E for kg/ha.

---

## 4. Collection roles

| Who | Collects | Does not |
|-----|----------|----------|
| **Household / custodian** | Daily/weekly ticks, photos, sales notes | Invent baseline for grants |
| **Jacques / field ops** | Quotes, registry, public CSV, integrity | Fake zeros into successes |
| **Expert panel** (when live) | Hard-case diagnosis notes | Quietly delete bad AI outcomes |
| **School hub** (if Starlink) | Hours log | Claim farm yield |

Forms: [field/FIELD_KIT.md](field/FIELD_KIT.md) · schemas in [data/](data/).

---

## 5. Existing apps & data (don’t rebuild the weather)

**Policy:** Prefer **good existing tools** for planting calendars, rain, and satellite context. GroundYield owns **unit registry, costs, baselines, outcomes, integrity** — not a second weather satellite.

Full catalogue: **[EXISTING_TOOLS.md](EXISTING_TOOLS.md)**.

| Need | Use existing? | GroundYield still measures |
|------|---------------|----------------------------|
| Rain / forecast | Yes — apps + open weather | Local rain notes when critical; compare |
| Planting date windows | Yes — calendar apps + our SEASON.md | **Actual** plant date per unit (F) |
| Pest libraries | Yes — ID apps as **assist** | Outcome + expert on hard cases |
| Yield / cost / income | **No — we collect** | Core KPIs Y*, I*, M* |
| Unit count / baselines | **No — we collect** | Integrity-critical |

AI layer should **call or point to** these tools, not re-implement CHIRPS or a global weather model.

---

## 6. KPI dashboard (public v0 — when data exists)

Start as a markdown table in UPDATES or `data/kpi-season-1.md`:

| KPI | Value | Mark | Date | Source row |
|-----|-------|------|------|------------|
| P1 units | 0 | F | … | units.csv |
| … | | | | |

No dashboard theatre with empty charts.

---

## 7. Trip checklist (data)

- [ ] Baseline form blanks printed  
- [ ] Quote photo workflow  
- [ ] Ask: which phone apps for rain/planting already?  
- [ ] One market price F sample  
- [ ] No % yield language on X  

---

Last updated: 27 July 2026
