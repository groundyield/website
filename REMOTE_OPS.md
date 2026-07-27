# Remote ops & smart unit path (future)

**Track, verify, and (carefully) control modular units from afar**  
Last updated: 27 July 2026  
**Status:** **Future design** — not Season 0/1 default BOM · no remote kit installed · **0 units**  

Related: [SYSTEM.md](SYSTEM.md) · [UNIT.md](UNIT.md) · [KPI_AND_DATA.md](KPI_AND_DATA.md) · [AI_FIELD_PATH.md](AI_FIELD_PATH.md) · [EXISTING_TOOLS.md](EXISTING_TOOLS.md) · [SECURITY_THEFT.md](SECURITY_THEFT.md) · [field/STARLINK_APPROACH.md](field/STARLINK_APPROACH.md) · [RISK_AND_GAPS.md](RISK_AND_GAPS.md) · [IRRIGATION.md](IRRIGATION.md)

---

## 0. Honest frame

| Truth | Implication |
|-------|-------------|
| Operator is often **remote** (KSA HSE work) | Care path and data path must not assume Jacques on plot daily |
| Humans on the ground stay first-class | Custodian, training, community legitimacy — sensors don’t replace trust |
| Sensors can **lie, die, or get stolen** | Remote data is **supporting evidence**, not automatic gospel |
| “Smarter / less human” is a **later phase** | After water, seed, baseline, and simple phone logs work |

**One-line stance:**

> We start **human + phone + public CSV**. We add **cameras, sensors, and solenoids** only when a unit has survived training and theft design — and we always keep a **human override** and a **manual fallback**.

---

## 1. Goal of remote ops

| Goal | Not the goal |
|------|----------------|
| See **kit still there** and **pump ran** without flying in | Fully autonomous farm with zero local people |
| Spot **anomalies** early (dry soil, no power, open gate) | Replace yield weighing with “AI estimated harvest” alone |
| **Verify** farmer-reported irrigation/events with second source | Spy on households without consent |
| Optional **remote valve/pump schedule** with local kill switch | Cloud-only control that fails closed and burns crop |
| Less **routine** travel for Jacques | Abandon communities when signal dies |

---

## 2. Architecture (layers)

```
┌──────────────────────────────────────────────────────────────┐
│  REMOTE DASHBOARD (operator / later partners)                 │
│  unit_id · last seen · soil · pump · photo · alerts · audit   │
├──────────────────────────────────────────────────────────────┤
│  AI OPS (optional)                                            │
│  anomaly detect · image “kit present?” · draft alerts         │
│  NEVER sole yield claim · escalate to human                   │
├──────────────────────────────────────────────────────────────┤
│  CONNECTIVITY                                                 │
│  Phone data · LoRa/hub · school Starlink · store-and-forward  │
├──────────────────────────────────────────────────────────────┤
│  EDGE (on unit / compound)                                    │
│  Sensors · camera · solenoid/valve · pump controller · RTC    │
│  Local schedule if cloud offline                              │
├──────────────────────────────────────────────────────────────┤
│  HUMAN LAYER (always)                                         │
│  Custodian · manual valve · paper log · expert panel          │
└──────────────────────────────────────────────────────────────┘
```

Fits SYSTEM layers A–D: remote stack sits on **A (physical add-ons)** + **B (connectivity)** + **C (AI ops)** + **D (public summaries, not raw private video)**.

---

## 3. Maturity stages (do not skip)

| Stage | Name | When | What’s live | Verification from afar | Human load |
|-------|------|------|-------------|------------------------|------------|
| **R0** | **Manual** | Now → first units | Paper/WhatsApp logs, photos on demand | Trust + spot visits | High local |
| **R1** | **Phone telemetry** | After G6 ≥1 unit stable | Structured WhatsApp forms; geotagged photos; weekly checklist | Soft remote — photo timestamps | Medium |
| **R2** | **Sense** | After R1 + theft OK | Soil moisture and/or tank level, pump current or run-hours, simple rain gauge | Dual source vs farmer log | Lower routine checks |
| **R3** | **See** | High-theft or multi-unit | Low-power camera (event or daily still) — **consent** | “Kit present / green cover” AI assist | Spot only |
| **R4** | **Control** | After R2 reliable | Solenoid / latching valve or pump relay on schedule + **local override** | Run-time logs F | Local for repairs |
| **R5** | **Fleet** | Many units | Multi-unit dashboard, shared spares, ranked alerts | Sample field audits | Specialists |

**Hard rule:** No R4 control without R0 custodian trained and **manual irrigation path** if electronics die.

**Gate idea (future):** claim “remote-verified irrigation” only when R2+ data and method published — add as **G7 Remote** when first pilot is real (not yet in [GATES](field/GATES.md) as binding).

---

## 4. What to measure remotely (maps to KPIs)

| Signal | Sensor / device | KPI link | Remote value | Accuracy note |
|--------|-----------------|----------|--------------|---------------|
| Soil moisture | Capacitive probe(s) 1–2 depths | W1, irrigation decisions | “Irrigate / wait” | Calibrate; **E** until field-checked |
| Pump run time | Current clamp / controller pulse / flow | W1, T2 uptime | Did water package run? | **F** if logged at controller |
| Tank / well level | Float or pressure | W2 | Dry-run risk | F relative change |
| Panel voltage / battery | Charge controller telemetry | T2 | Theft vs failure triage | F electrical |
| Rain at plot | Cheap tipping gauge | Weather vs app | Local rain F | Better than app alone |
| Valve open/close | Solenoid state + schedule log | W1 | Control audit | F state |
| Presence / theft | Camera still or PIR + camera | T1 | Kit still there | Image F; AI label E |
| Canopy / greenness | Camera or phone NDVI-ish (later) | Soft crop health | Alert only | **Not** yield F |
| Harvest mass | **Still human weigh** | Y1 | Remote can’t replace | Keep scale/bags |

**Yield (Y1) stays human-measured** for public F until a published method (e.g. bag counts on camera + calibration) is proven — don’t claim scale-free remote yield early.

---

## 5. Component menu (future BOM add-on — planning bands only)

Not in core [UNIT.md](UNIT.md) v0. Optional **smart module** after site proves.

| Item | Role | Rough USD (E) | Theft / fail notes |
|------|------|---------------|---------------------|
| Soil moisture probe + logger | Sense | 30 – 120 | Cable cut; calibrate |
| Pump run sensor / smart controller | Sense | 40 – 200 | Prefer indoor controller |
| LoRa / 4G / Wi‑Fi node | Link | 40 – 150 | SIM cost; Starlink hub as backhaul |
| Solenoid or latching valve | Control | 40 – 150 | Manual bypass mandatory |
| RTC + local schedule board | Offline control | 20 – 80 | Survives cloud outage |
| Camera (trail / low-power cellular) | See | 50 – 250 | High theft value — compound only |
| Small solar for edge (if separate) | Power | 30 – 100 | Same theft rules as farm PV |
| Enclosure, earth, surge | Hardening | 20 – 80 | Lightning/coastal |

**Order of buy:** run-hours + soil → camera → solenoid.  
**Don’t** buy solenoid fleet before one unit’s R2 data is boringly reliable for a season.

Cost discipline: publish as optional line in UNIT when first quote exists (G2-style).

---

## 6. Connectivity patterns (remote without full Starlink on every plot)

| Pattern | How | Best for |
|---------|-----|----------|
| **A. Farmer phone** | Photos + form to WhatsApp/bot | R1 everywhere |
| **B. Edge → phone hotspot** | Logger uploads when phone nearby | Sparse data |
| **C. Edge → village 4G** | SIM in modem | R2–R4 if coverage |
| **D. Edge → LoRa → school Starlink hub** | Long battery, shared backhaul | Multi-unit village |
| **E. Store-and-forward** | Days of local log; dump weekly | Outages normal |

Starlink remains **school/hub first** ([STARLINK_APPROACH](field/STARLINK_APPROACH.md)), not a dish per 0.25 ha unless economics and security allow.

---

## 7. Cameras, AI, “verify without flying in”

### Cameras

| Use | Allowed when | Public data |
|-----|--------------|-------------|
| Daily still of pump house / panel rack | Written consent; no bedroom/house interior | Cropped “kit present” yes/no + date — not live public stream of people |
| Event clip on PIR | Same | Private ops; public incident summary only |
| Harvest bag photo for dual evidence | Consent | Supports INTEGRITY dual evidence |

**Privacy:** [CONSENT.md](CONSENT.md) — cameras are **not** default. Community veto wins.

### AI on remote feeds

| AI job | OK | Not OK |
|--------|----|--------|
| “Panel rack still in frame?” | Assist | Sole theft prosecution claim without human |
| “Green cover vs bare soil” | Alert | Yield % claim |
| Anomaly: pump hours = 0 for 7 days | Ticket to ops/custodian | Silent ignore |
| Summarize weekly for Jacques in KSA | Yes | Replace expert agronomy for chemicals |

Ties to [AI_FIELD_PATH](AI_FIELD_PATH.md) L0–L3: remote ops AI is **ops layer**, still escalate hard crop calls.

---

## 8. Solenoids & control (make irrigation smarter)

```
Schedule (cloud or local RTC)
    → solenoid / pump relay
    → soil moisture interlock (optional: skip if wet)
    → log run minutes
    → LOCAL MANUAL OVERRIDE (tap / bypass valve) always
```

| Rule | Why |
|------|-----|
| **Fail-safe** | Prefer “stay as last state” or safe off — document per site |
| **Local override** | Electronics/cloud die; crop still waterable |
| **No remote-only dependency** | Operator in KSA cannot be single point of failure |
| **Custodian trained on override first** | Before app login |
| **Audit log** | Who changed schedule (app user id) |

---

## 9. Less reliance on humans — what actually drops

| Task | R0 | R3–R4 |
|------|----|-------|
| “Did they irrigate?” | Ask / visit | Run-time log |
| “Is kit stolen?” | Visit / rumour | Camera + electrical |
| “Should we water today?” | Visit / call | Soil + schedule + optional AI draft |
| “Is yield real?” | Visit weigh | Still visit or dual photo protocol |
| Trust / land / conflict | Human forever | Human forever |
| Training first season | Human forever | Human forever |

**Residual human load we accept:** legitimacy, harvest truth, repairs, theft response, expert hard cases ([RISK_AND_GAPS](RISK_AND_GAPS.md)).

---

## 10. Security & failure modes (sensors make new traps)

| Risk | Mitigation |
|------|------------|
| Sensor/camera stolen | Same as panels: near house, mark, removable, few units ([SECURITY_THEFT](SECURITY_THEFT.md)) |
| Fake remote success | Dual source; random field audit; don’t drop visits to zero |
| SIM / cloud bill unpaid | Local schedule; store-and-forward; who pays month 13 |
| Over-automation kills crop | Moisture interlock + manual; season max run hours |
| Data privacy backlash | Consent; no public face streams |
| Complexity > benefit | Kill module if cost > value after 1 season public autopsy |

---

## 11. Implementation roadmap (later)

| Step | Prerequisite | Deliverable |
|------|--------------|-------------|
| 1 | ≥1 unit R0 working full season | Lessons on what we’d wish we saw remotely |
| 2 | G2 quotes for logger + soil probe | Optional BOM line in UNIT |
| 3 | R1 WhatsApp structured log template | KPI W1 from phone F/E |
| 4 | Pilot R2 on **one** trusted unit | Public note: method + failures |
| 5 | Consent + camera trial if theft high | Ops-only images; public summary |
| 6 | R4 solenoid on same unit | Manual override drill documented |
| 7 | Dashboard (even a spreadsheet + charts) | Jacques remote weekly review |
| 8 | Multi-unit only after 1 boring season | Fleet rules |

**Do not** start at step 6 on day one of first install.

---

## 12. What Jacques can do from KSA (target later)

| Weekly remote ritual | Source |
|----------------------|--------|
| Open unit dashboard / sheet | R2+ |
| Check alerts: no pump, dry soil, offline node | AI ops draft |
| Approve or defer schedule changes | Control log |
| Escalate expert tickets | AI_FIELD_PATH |
| Publish public weekly one-liner if material | UPDATES / X |
| Book visit only when alert + local can’t resolve | SAFETY |

Until R2 exists: **WhatsApp photos + custodian calls** remain the remote method (R0/R1).

---

## 13. Public claims (integrity)

| Claim | Allowed when |
|-------|----------------|
| “We monitor pump hours remotely” | R2 live + method public |
| “Camera verifies kit” | Consent + ops practice live |
| “Fully autonomous irrigation” | **Never claim** without long proof; prefer “scheduled + override” |
| “Remote yield verified” | Not until method in KPI_AND_DATA proven |

---

## 14. Decision checklist (before buying smart kit)

- [ ] Unit already produces with **manual** package  
- [ ] Custodian can water with electronics **off**  
- [ ] Theft plan covers new shiny boxes  
- [ ] Connectivity pattern chosen (A–E above)  
- [ ] Who pays SIM/cloud month 13  
- [ ] Consent for any camera  
- [ ] Data lands in unit_id log (not private only forever)  
- [ ] Optional BOM quote dated  

If any box unchecked → stay R0/R1.

---

## 15. One-page future picture

```
TODAY (R0):  human · phone photo · paper · public CSV
SOON (R1):   structured WhatsApp · geotag · weekly form
LATER (R2):  soil + pump hours → dashboard in KSA
THEN (R3):   camera stills · AI “kit present?”
THEN (R4):   solenoid schedule · local override · audit log
FLEET (R5):  many units · ranked alerts · shared spares

ALWAYS: custodian · consent · manual fallback · no fake remote yield
```

---

**Bottom line:** Yes — we can plan cameras, sensors, solenoids, and AI so the pilot is **smarter and less visit-dependent**. We stage it so we don’t recreate failed “tech drop” projects: **prove dirt and trust first**, then instrument, then control, always with humans for truth and override.

Last updated: 27 July 2026
