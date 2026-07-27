# Site UX rules (keep it usable)

**GroundYield public pages**  
Last updated: 27 July 2026  

Related: [index.html](index.html) · [docs.html](docs.html) · [PLAN.md](PLAN.md) · [README.md](README.md)

---

## Review findings (why it felt messy)

| Problem | Fix |
|---------|-----|
| Homepage was a **wall of 40+ .md links** | **docs.html** library by category; home shows **6 paths** |
| **15+ same-day update cards** | Home shows **~5 latest** → full log in UPDATES.md / RSS |
| No **navigation** | Primary nav on home + docs |
| Duplicate links (e.g. AI twice) | Removed on cleanup |
| Repo grew to **40+ root markdown files** | Fine for operators; **not** all on the landing page |
| Long status paragraph | Short **status card** |

---

## Information architecture

```
/                 → story + status + 6 start paths + short sections
/docs.html        → full library (grouped)
/units.html       → registry count (integrity)
/day1.html        → shareable essay
/pt.html          → Portuguese short page
GitHub *.md       → deep detail (PLAN, RISK, field/, …)
```

**Audiences**

| Who | Land on | Read first |
|-----|---------|------------|
| Public / press | `/` | Status, Who, Integrity, Registry |
| Community / partner | `/` + VALUE_AND_MONEY | pt.html if PT |
| Operator (Jacques) | NEXT.md, GROUND_TRIP | field/ |
| Auditor / critic | INTEGRITY, units, SOURCES | RISK_AND_GAPS |

---

## Rules for future edits

1. **Homepage is not a changelog dump** — max ~5 update teasers.  
2. **Homepage is not a full repo index** — link **docs.html**.  
3. New policy doc → add to **docs.html** in the right group + PLAN doc map; home only if it is a “start here” path.  
4. Prefer **one card / one idea** over long multi-topic paragraphs.  
5. Keep **ship-check needles** honest (status, UNIT, INTEGRITY, registry 0, field PDFs).  
6. PT page stays **short**; deep docs stay EN with PT entry points.  
7. Field ops noise (X drafts, packing lists) stays in **field/** and NEXT — not nav chrome.

---

## Still optional later

- Shared CSS file (less copy-paste across HTML)  
- Collapsible “for operators” on docs  
- Auto-generate docs.html from a small YAML index  
- Portuguese docs hub stub  

---

Last updated: 27 July 2026
