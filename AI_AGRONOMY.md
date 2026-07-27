# AI Agronomy Advice — Design v0

**GroundYield public design note**  
Last updated: 27 July 2026

Phone-based advice is part of the core package. This document says **what it is**, **what it is not**, and **how we will measure it** so the pilot does not oversell “AI.”

---

## Goal

Give smallholders **timely, local, actionable** guidance on planting, water, nutrients, pests, and harvest — in a form they already use — and publish whether that guidance correlated with better outcomes.

---

## What it is (Season 1 intent)

| Layer | Description |
|-------|-------------|
| **Channel** | WhatsApp primary; SMS fallback for basic phones |
| **Languages** | Portuguese first; English secondary; local languages via human partners when needed |
| **Content** | Season calendar prompts, micro-dosing reminders, irrigation scheduling heuristics, pest ID triage, “when to sell / store” |
| **AI role** | Draft answers, translate, summarize field notes, flag risky advice for human review |
| **Human role** | Local extension / trusted partner verifies critical recommendations early on |

**Design principle:** AI accelerates and documents advice; **it does not silently replace local agronomy judgment** in Season 1.

---

## What it is not

- Not a fully autonomous farm robot or closed proprietary black box  
- Not medical/veterinary diagnosis without referral paths  
- Not a substitute for soil tests where those are feasible  
- Not a guarantee of the 80–100%+ yield target (that target is whole-package + measurement)  
- Not offline-only at v0 (offline packs are a later improvement)

---

## User journey (single farmer / unit)

1. **Enroll** unit ID + crop plan + approximate location (privacy-minimized)  
2. **Baseline** captured (yield practice, last season story) — see `DATA.md`  
3. **Weekly prompts** aligned to [SEASON.md](SEASON.md) calendar  
4. **On-demand Q&A** via chat (photo optional for pest/disease triage)  
5. **Escalation** when model confidence low → human partner  
6. **Season close** — outcomes logged publicly (anonymized as needed)

---

## Technical sketch (implementation-agnostic)

| Component | v0 choice | Notes |
|-----------|-----------|--------|
| Messaging | WhatsApp Business / Cloud API or manual ops | Start manual if volume is tiny |
| Model | Hosted LLM with tool/context injection | Prefer providers that allow clear data policy |
| Knowledge | GroundYield docs + local field notes | UNIT, SEASON, supplier notes |
| Logging | Append-only advice log (internal) + public outcome data | Publish outcomes, not private chat dumps |
| Cost | Target **$0–20 / unit / season** (see UNIT.md) | Track actual API + staff time |

Exact vendor choices will be published when selected. Open by default: prompts, evaluation notes, and failure cases.

---

## Safety & quality rules

1. **No fertilizer rates above published package** without a documented reason  
2. **Pesticide advice** stays conservative; prefer IPM and local regs  
3. **Water advice** never ignores pump and well limits  
4. **Every automated recommendation** can be traced to a prompt version + date  
5. **Farmer can opt out** of AI channel and still stay in the pilot with human-only support  

---

## How we measure “advice worked”

| Metric | How |
|--------|-----|
| Engagement | % of units that opened/replied to weekly prompts |
| Usefulness | Simple mid/end season survey (1–5 + free text) |
| Outcome link | Yield and income vs baseline — **not** attributed to AI alone |
| Harm flags | Count of bad advice incidents and corrections (published) |
| Cost | USD per active unit per season |

If AI adds cost without engagement or outcomes, we **cut or redesign** it publicly.

---

## Privacy

- Prefer unit IDs over personal names in public datasets  
- Chat logs are not open by default (privacy + safety)  
- Photos of people require consent; fields/crops preferred  
- Community agreements can tighten these rules further  

---

## Build sequence

| Step | When |
|------|------|
| Manual WhatsApp playbook (scripts, not bot) | Before first units |
| Structured weekly messages | First planting season |
| LLM-assisted replies with human review | Once volume justifies |
| Automated logging + evaluation dashboard | After first 5–10 units |
| Open evaluation report | End of Season 1 |

---

## Related

- [UNIT.md](UNIT.md) — cost band for advice layer  
- [SEASON.md](SEASON.md) — what to say when  
- [DATA.md](DATA.md) — public outcome metrics  
- [CHARTER.md](CHARTER.md) — transparency commitments  

**Status:** v0 design  
**Next:** Draft Portuguese WhatsApp weekly script for maize + one cash crop; pick channel tooling after ground trip.
