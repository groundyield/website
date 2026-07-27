# What we will do — and the role of Starlink + AI

**GroundYield operating model (public)**  
Last updated: 27 July 2026  
**Stage:** Phase 0 · paper ready · ground window opening · **0 units · 0 baselines**

This is the single map of **work**, **connectivity**, and **AI**.  
It does not claim results. Targets stay aspirational until measured ([CHARTER.md](CHARTER.md)).

| Deep dives | |
|------------|--|
| Starlink / schools approach | [field/STARLINK_APPROACH.md](field/STARLINK_APPROACH.md) |
| AI agronomy design | [AI_AGRONOMY.md](AI_AGRONOMY.md) |
| Gates G0–G6 | [field/GATES.md](field/GATES.md) |
| Integrity / anti-fraud | [INTEGRITY.md](INTEGRITY.md) |

---

## 1. One-sentence model

> **Physical modular farm units** close the yield gap; **Starlink** (where real) makes rural schools and hubs online so people can learn and we can publish data without lying about “offline forever”; **AI** drafts and organizes advice and ops — **humans** own rates, consent, and installs.

Neither Starlink nor AI replaces land, water, seed, or trust.

---

## 2. What we will actually do (layers)

Think in four layers. Only layer A is “the farm pilot.” B–D support it without becoming the product.

```
┌─────────────────────────────────────────────────────────────┐
│  D. PUBLIC TRUTH LAYER                                      │
│     Website · GitHub · unit registry · UPDATES · X notes    │
│     (what the world can verify)                             │
├─────────────────────────────────────────────────────────────┤
│  C. INTELLIGENCE LAYER                                      │
│     AI: draft advice, translate, summarize, flag risk       │
│     Humans: agronomist review, extension, operator          │
│     FREEZE on live farmer advice until G5                   │
├─────────────────────────────────────────────────────────────┤
│  B. CONNECTIVITY LAYER                                      │
│     Starlink at school/community hubs (1–3 pilots first)    │
│     Phone data / Wi‑Fi where it already exists              │
│     Offline field pack when signal dies                     │
├─────────────────────────────────────────────────────────────┤
│  A. PHYSICAL LAYER (the pilot)                              │
│     Land access · solar irrigation · seed · fertilizer      │
│     storage · optional poultry · measured baselines         │
└─────────────────────────────────────────────────────────────┘
```

### Layer A — Physical (core)

| Work | Output |
|------|--------|
| Community + land access | Legitimate use, not a land grab |
| Modular unit package | [UNIT.md](UNIT.md) BOM — irrigation, inputs, storage |
| Baselines then seasons | [DATA.md](DATA.md) · CSV rows · F/E/H marks |
| Supplier quotes | [SUPPLIERS.md](SUPPLIERS.md) — real prices replace planning bands |
| Failures | Public log — broken pumps, bad seed, dead ends |

**Without A, Starlink and AI are theatre.**

### Layer B — Connectivity (Starlink + phones)

| Work | Output |
|------|--------|
| School-first Starlink pilots (1–3) | Teaching/admin access; public install metrics |
| Optional community hours on same hub | Written rules; not unlimited free for everyone |
| Operator / field phone data | WhatsApp, photo upload, when available |
| Offline pack | PDFs/forms when offline ([field/FIELD_KIT.md](field/FIELD_KIT.md)) |

**Starlink is not “internet for the brand.”** It is **rural digital access** with education as the primary public good. Farm data rides along later.

### Layer C — Intelligence (AI + humans)

| Work | Output |
|------|--------|
| **Now (allowed)** | Draft docs, translate, summarize trip notes, stress-test plans, code/site |
| **After G5 only** | WhatsApp/SMS agronomy prompts to enrolled units |
| Always | Human veto on fertilizer/pesticide/water rates |

### Layer D — Public truth

| Work | Output |
|------|--------|
| Unit registry | [units.html](https://www.groundyield.org/units.html) — count only real rows |
| Changelog | [UPDATES.md](UPDATES.md) · RSS |
| Field notes | X + GROUND_TRIP — same-day honesty |

---

## 3. Starlink — exact role

### What Starlink is for

| Use case | Priority | Why |
|----------|----------|-----|
| **Rural school connectivity** | **#1** | Clear community benefit; measurable (access hours, not vibes) |
| **Community hub** (shared hours) | #2 | One dish, more users; needs governance |
| **Operator field base** | #3 | Upload baselines, quotes, photos when in sparse areas |
| **Later: farmer training sessions** | #4 | Video/extension materials at the hub |
| **Later: unit data sync** | #5 | Only after units exist |

### What Starlink is not for

- A substitute for solar irrigation or seed  
- A promise to every village on first meeting  
- Marketing content without install metrics  
- Running unreviewed AI advice at scale before G5  

### How Starlink and the farm pilot touch

```
School hub online (Starlink)
    → teachers/students use for learning
    → optional evenings: farmer training / market prices (consented)
    → operator uses hub or own kit to publish GROUND_TRIP / CSV
    → only after units: enrolled farmers may use phone data OR hub Wi‑Fi
         to receive reviewed advice (AI-drafted, human-cleared)
```

Full partnership discipline: [field/STARLINK_APPROACH.md](field/STARLINK_APPROACH.md)  
**No agreement exists today.**

### Minimum viable Starlink pilot (if path opens)

| Item | Spec |
|------|------|
| Sites | 1–3 rural schools near Vilanculos area |
| Power | Solar + battery sized for dish + lights/charging (site survey first) |
| Owner of subscription | Written (school / district / sponsor) before install |
| Metrics published | Uptime, power failures, cost payer, incidents |
| Gate | Local education intro + coverage map + written commercial/program path |

---

## 4. AI — exact role

### Two clocks

| Clock | AI does | AI must not |
|-------|---------|-------------|
| **Ops clock (now)** | Draft docs, translate EN↔PT, summarize interviews, organize contacts, site/code | Invent field numbers; claim G1–G6 done |
| **Advice clock (after G5)** | Draft WhatsApp prompts, pest photo triage, translate farmer questions | Send unreviewed rates; replace extension; hide chat risk |

**G5 freeze** remains: [ADVICE_SCRIPTS.md](ADVICE_SCRIPTS.md) not for live farmers until agronomist + local review.

### AI in the daily system (target architecture)

```
Farmer phone (WhatsApp/SMS)
        │
        ▼
┌───────────────────┐     ┌─────────────────────┐
│  Message gateway  │────▶│  Human review queue │  ◀── agronomist / operator
│  (manual at v0)   │     │  (required Season 1)│
└───────────────────┘     └──────────┬──────────┘
        │                            │
        │    ┌──────────────┐        │
        └───▶│  LLM draft   │────────┘
             │  + UNIT/SEASON│
             │  + local notes│
             └──────────────┘
                     │
                     ▼
             Internal advice log
                     │
                     ▼
             Public outcomes only
             (yields/costs — not private chats)
```

**v0 on this trip:** almost everything is **manual** (forms, notebooks, you). AI helps you write and organize offline/online — not auto-reply to farmers.

### AI + Starlink together

| If offline | If online (phone or Starlink hub) |
|------------|-------------------------------------|
| Paper forms, one-pager, pocket scripts (frozen for send) | Upload photos, sync CSV, publish UPDATES |
| AI on your laptop when you have power (draft notes) | Later: farmers message hub hours / own data |
| No claim that “AI works offline for the village” | No claim that connectivity alone raises yields |

Connectivity multiplies **publishing and learning**. AI multiplies **drafting and triage**. **Physics and relationships** still do the farming.

---

## 5. End-to-end journey (one community, honest)

| Step | What happens | Starlink? | AI? |
|------|----------------|-----------|-----|
| 1. Intro | Meet leaders/school — no money ask, no free dish promise | No | Optional: translate materials |
| 2. Consent | [CONSENT_SCRIPT.md](field/CONSENT_SCRIPT.md) | No | No |
| 3. Baseline | Paper → later CSV | Upload when online | Summarize notes later |
| 4. Quotes | Hardware/agro/lodges | Upload quotes | Organize tables |
| 5. School interest | Power survey; no promise | Coverage check | — |
| 6. Starlink path | Only if written path | Install + metrics | Publish report drafts |
| 7. First units | Registry row | Optional hub nearby | Still freeze advice unless G5 |
| 8. Season advice | Enrolled units only | Phone or hub Wi‑Fi | Draft → human → send |
| 9. Public results | Yields/costs/failures | Publish from anywhere online | Help write UPDATES; never invent |

---

## 6. Phase map (what “we will do” means in time)

### This ground window (~2 weeks)

| Do | Don’t |
|----|--------|
| Intros, quotes, baseline **starts** | Install modular units at scale |
| Map rural schools + power (Starlink readiness) | Promise Starlink installs |
| X field notes (honest) | Yield marketing |
| Use AI for notes/docs | Live agronomy bots |

### Phase 1 — First units (after land + capital)

| Do | Don’t |
|----|--------|
| 1–few units, registry live | Claim 30–60 done |
| Human advice + maybe reviewed scripts | Unreviewed pesticide advice |
| Starlink only if Phase 0 path closed | Connectivity as vanity |

### Phase 2 — Season 1 proof

| Do | Don’t |
|----|--------|
| Measure vs **local** baseline | National-average games |
| AI advice under G5 rules + logs | Black-box “AI increased yields 100%” |
| Publish failures | Silent rewrites |

---

## 7. What success looks like (tech + field)

| Layer | Success | Failure (publish anyway) |
|-------|---------|---------------------------|
| Physical | Real quotes + baselines + later units | No land; we say so |
| Starlink | 1 school online with public uptime log | No deal; communities not promised |
| AI | Reviewed advice helps some units; measured | Advice wrong → correction + freeze tighten |
| Public | Registry matches reality | Ghost unit attempt → blocked by process |

---

## 8. One diagram — money and attention (keep clean)

```
Self-funding / later named funders (WHO.md)
        │
        ├── Trip ops (TRIP_BUDGET) ──▶ meetings, quotes, baselines
        ├── Unit capital (UNIT) ─────▶ pumps, seed, storage
        ├── School connectivity ─────▶ Starlink kit + power + fees
        └── Ops tools ───────────────▶ phones, AI API cost, site

Starlink and AI budgets stay visible and separate from “yield miracle” stories.
```

---

## 9. Open decisions (fill as reality arrives)

| Decision | Owner | Status |
|----------|--------|--------|
| Starlink: buy vs education program vs partner intro | Jacques + Starlink reply | Open |
| Who pays month 13 on school kit | School / sponsor / us | Open |
| Agronomist for G5 review | TBD | Open |
| WhatsApp Business vs manual | Ops | Open until volume |
| First 1–3 school candidates | Local education intro | Open |

---

## 10. Bottom line

1. **We farm and measure** — modular units, baselines, quotes, public failures.  
2. **Starlink** — rural **school/community hubs** first (small, documented); farm data rides later.  
3. **AI** — ops and drafting now; **farmer advice only after G5** with humans in the loop.  
4. **Offline** stays first-class (paper kit) so we never pretend connectivity equals impact.  
5. **Integrity** — no ghost schools, no ghost units, no invented yield from “AI + satellite.”

If connectivity or AI never lands, the farm pilot can still be honest.  
If the farm never lands, Starlink+AI must not become a substitute story.

---

Related: [PLAN.md](PLAN.md) · [UNIT.md](UNIT.md) · [field/STARLINK_APPROACH.md](field/STARLINK_APPROACH.md) · [AI_AGRONOMY.md](AI_AGRONOMY.md) · [field/GATES.md](field/GATES.md)
