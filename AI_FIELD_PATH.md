# AI field path — how we unfreeze, show value, and escalate to experts

**GroundYield · intelligence layer (public)**  
Last updated: 27 July 2026  
**Status:** Staged unfreeze **L0–L1 open now** · **L2–L3 still gated** · not a live farm advice service for enrolled units yet  

Related: [AI_AGRONOMY.md](AI_AGRONOMY.md) · [ADVICE_SCRIPTS.md](ADVICE_SCRIPTS.md) · [SYSTEM.md](SYSTEM.md) · [field/GATES.md](field/GATES.md) · [field/STARLINK_APPROACH.md](field/STARLINK_APPROACH.md) · [RISK_AND_GAPS.md](RISK_AND_GAPS.md) · [CONSENT.md](CONSENT.md) · [WHO.md](WHO.md)

---

## 1. The honest problem

Farmers (and you) need **help choosing** under uncertainty:

- Plant now or wait for rain?  
- This leaf damage — water, pest, or nutrient?  
- Irrigate today or save pump hours?  
- Sell green or store?  

**Bad pattern (we refuse):** drop a chatbot, claim “AI will fix yields,” send chemical rates with no human, no expert, no log.  
**Good pattern:** AI **speeds choice and triage**; **humans and experts own high-risk decisions**; community **sees the demo** before anyone depends on it.

---

## 2. How AI helps people make the *correct* choice

AI does not “know the farm better than the farmer.” It helps by **structuring the decision**.

| Decision job | What AI does well | What it must not do alone |
|--------------|-------------------|---------------------------|
| **Clarify the question** | “Is this about water, pest, or timing?” | Invent a diagnosis from a blurry photo |
| **Offer a short menu** | 2–4 plausible options + what to observe next | One confident wrong answer |
| **Attach local package rules** | Microdose ceiling, season calendar, unit BOM | Exceed published rates without reason |
| **Remind and schedule** | Planting windows, irrigation cadence, store/sell prompts | Guarantee yield |
| **Flag danger** | “This needs a human / don’t spray unknown product” | Prescribe restricted pesticides casually |
| **Translate** | PT ↔ EN; simple language | Hide uncertainty in fancy English |
| **Log the choice** | Date, unit_id, advice version (internal) | Publish private chats |

### Choice helper (the thing we *show* people)

Every serious answer follows **CHOICE**:

1. **C**ontext — crop, stage, water source, last rain (ask if missing)  
2. **H**ypotheses — 2–3 possible causes (not one)  
3. **O**ptions — what you can do this week (cheap first)  
4. **I**f unsure — photo + escalate to expert group  
5. **C**eiling — never above published package / local law  
6. **E**xit — farmer can ignore AI and stay in pilot  

**Demo line (PT, community meeting):**

> O telemóvel não planta por si. Ajuda a **escolher**: o que verificar, o que evitar, e quando chamar uma pessoa. Se a resposta for perigosa ou incerta, **para** e vai para especialistas.

**Demo line (EN):**

> The phone doesn’t farm for you. It helps you **choose**: what to check, what to avoid, and when to call a person. If the answer is risky or uncertain, it **stops** and goes to experts.

---

## 3. Staged unfreeze (replaces a single on/off freeze)

| Level | Name | Allowed | Not allowed | Gate to enter |
|-------|------|---------|-------------|---------------|
| **L0** | **Ops AI** | Draft docs, translate, trip notes, code, plan stress-tests | Farmer agronomy as “official advice” | Already open |
| **L1** | **Show & choose demo** | Public demos, school hub sessions, paper/phone walkthroughs of CHOICE; **no** enrolled-unit chemical rates | Claiming live pilot advice; personalized fertilizer/pesticide prescriptions as GroundYield service | **Open now** (this doc) |
| **L2** | **AI draft + human/expert review** | WhatsApp/SMS to **enrolled** units; AI drafts; **human sends** after review | Unsupervised auto-send of rates | **G5-A** — see below |
| **L3** | **Instant field AI + expert backup** | On-phone (signal or Starlink hub) short answers; auto-escalate hard cases | Silent full autonomy; no expert path | **G5-B** — panel live + SLA + log |

**Old “full freeze”** = blocked L1–L3.  
**Now:** **L0 + L1 unfrozen.** L2/L3 stay gated so we don’t harm crops or trust.

When G5-A or G5-B lifts, record **who + date** in [ADVICE_SCRIPTS.md](ADVICE_SCRIPTS.md) and [UPDATES.md](UPDATES.md).

---

## 4. Expert group (“if crop or AI hits a problem”)

### Why

Instant AI fails on: rare diseases, chemical selection, well limits, conflict land, anything safety-critical.  
History of pump/tech projects without training already failed ([WHY_OTHERS_FAILED.md](WHY_OTHERS_FAILED.md)). Experts are the **counter**, not optional PR.

### Target panel (recruit; not claimed onboard until named on WHO)

| Seat | Role | Min for G5-A | Ideal |
|------|------|--------------|-------|
| **A1 Agronomy** | Crops, nutrients, pests — MZ or southern Africa experience | 1 reviewer | 2 |
| **A2 Water / irrigation** | Pumps, scheduling, well limits | Optional at G5-A | 1 |
| **A3 Markets** | Sell/store, local offtake | Optional | 1 |
| **A4 Livestock** (if poultry/goats) | Basic referral only | If module runs | 1 |
| **Ops** | Jacques / local partner routes tickets | Always | — |

**Not claimed:** We do **not** have a full panel signed as of this date. Recruitment is **open**.

### How experts work

```
Farmer / field photo
        │
        ▼
   AI CHOICE draft (instant if L3)
        │
   ┌────┴────┐
   │ Soft?   │ Hard / chemical / low confidence / farmer requests human
   ▼         ▼
 Reply     Expert ticket (WhatsApp group or shared inbox)
 (L3)         │
              ▼
         Expert reply (target 24–48h when panel live)
              │
              ▼
         Log: date · unit_id · topic · AI version · expert id · outcome note
```

| Rule | Detail |
|------|--------|
| **No orphan tickets** | Every hard case has an owner within 24h or “paused — no expert” public status |
| **Experts can override AI** | Always; log the override |
| **Experts can say “I don’t know”** | Preferred to guessing |
| **Volunteer vs paid** | State clearly on WHO when people join |
| **No result veto by funders** | Same as INTEGRITY |

### Recruit message (short)

```
Subject: GroundYield — expert panel (Mozambique modular pilot)

We're running an open modular farm pilot near Vilanculos (0 units live).
We need agronomy (and optionally irrigation/markets) reviewers so AI drafts
never go to farmers unsupervised on high-risk topics.

Ask: review draft WhatsApp scripts + escalate hard field cases (async).
Public credit optional. No ghost units, no fake yields.

Docs: https://www.groundyield.org · team@groundyield.org
```

Track prospects in [field/CONTACT_LOG.md](field/CONTACT_LOG.md); name accepted experts on [WHO.md](WHO.md) with consent.

---

## 5. Instant on phone (signal or Starlink)

### Channels

| Channel | When | Notes |
|---------|------|--------|
| **WhatsApp** | Primary once L2+ | Most phones; manual first |
| **SMS** | Fallback | Short only |
| **Starlink school hub** | Shared Wi‑Fi | Demo + training + photo upload; not required for every farmer at home |
| **Offline pack** | No signal | Paper season card + “send photo when online” ([field/FIELD_KIT.md](field/FIELD_KIT.md)) |

Starlink **does not** replace AI safety. It only improves **upload and demo access** ([field/STARLINK_APPROACH.md](field/STARLINK_APPROACH.md)).

### Instant (L3) scope — safe list

**May answer quickly (with uncertainty language):**

- Season calendar “what week is it for maize?”  
- Microdose **reminder** of published package (not invent higher rates)  
- Irrigation **heuristic** (“check soil finger test; don’t run dry well”)  
- “Send a daylight photo of the leaf + whole plant”  
- Store vs sell **questions to ask** the market (not a price guarantee)  

**Must escalate (no instant chemical prescription):**

- Any pesticide product choice / mix rates  
- Fertilizer **above** package  
- Livestock disease that could be zoonotic  
- Well collapse / electrical pump wiring  
- Conflict, land dispute, threats  

### Field demo flow (L1 — do this on the trip)

1. Show phone + simple question (e.g. yellow leaves on maize).  
2. Walk **CHOICE** on paper or screen — 3 hypotheses, not one magic answer.  
3. Say: *when unsure → photo → person (expert group when live).*  
4. Offer **opt-in waitlist** for L2 — not enrollment into AI dependency.  
5. Never spray / apply products in the demo from AI text alone.

---

## 6. Gates (G5 split)

| Gate | Meaning | Evidence |
|------|---------|----------|
| **G5-A** | L2 live: AI draft + human/expert send to enrolled units | ≥1 named agronomy reviewer on WHO **or** documented Jacques+qualified review date; consent path; freeze section in ADVICE_SCRIPTS updated |
| **G5-B** | L3 live: instant field answers + expert SLA | G5-A done; expert ticket path tested; safe/unsafe topic list published; harm log exists |
| **G5** (legacy name) | Means **at least G5-A** | Do not claim “AI live” for only L1 demos |

[GATES.md](field/GATES.md) points here for G5 detail.

---

## 7. How we *show* value without lying

| Show | Honest claim | Forbidden claim |
|------|--------------|-----------------|
| CHOICE demo on yellow leaf | “Helps sort options and when to ask a person” | “AI diagnosed your disease and will raise yield 100%” |
| Season reminder | “Reduces forgotten steps” | “Guarantees harvest” |
| Expert escalation sketch | “Hard problems go to people” | “24/7 agronomist already staffed” (until true) |
| Starlink hub session | “Faster photo upload / training access” | “Every farmer has Starlink at home” |

**Measurement later (L2+):** engagement, usefulness survey, harm flags, cost/unit — [AI_AGRONOMY.md](AI_AGRONOMY.md).  
AI is never the sole claimed cause of yield change.

---

## 8. Operator checklist (trip + next 30 days)

### This trip (L1)

- [ ] Run ≥1 **CHOICE demo** (Rumbacaca or school) — log date in GROUND_TRIP  
- [ ] Collect waitlist contacts only with consent (private notes)  
- [ ] Ask: *who do you trust for crop advice today?* (map local experts)  
- [ ] No L2 messages with rates  

### Next 30 days (toward G5-A)

- [ ] Send expert recruit email to ≥5 candidates  
- [ ] Name first reviewer on WHO when accepted  
- [ ] Review ADVICE_SCRIPTS with that person  
- [ ] Pick WhatsApp ops method (manual OK)  
- [ ] Public UPDATES line when G5-A lifts  

### Before G5-B (instant)

- [ ] Ticket template + response SLA written  
- [ ] Safe/unsafe topic list laminated for field  
- [ ] Test escalation once (fake case)  
- [ ] Starlink hub only if payer/path written  

---

## 9. Kill / pause rules (AI-specific)

| Trigger | Action |
|---------|--------|
| Harmful advice used and crop/person harmed | **Pause L2/L3** · public correction · expert review |
| No expert available >7 days and hard cases queue | Pause high-risk topics; L1 demos only |
| Pressure to auto-send chemicals for “engagement” | **Refuse** · INTEGRITY |
| Farmers treat AI as sole authority | Retrain messaging; strengthen escalation language |

---

## 10. One-line public stance

> **We unfreeze AI in stages.** First we **show** how it helps you choose. Then AI **drafts** and people **check**. Then, with experts on call, the phone can answer **fast** in the field — and still stop when a human is needed.

Last updated: 27 July 2026
