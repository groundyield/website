# Existing apps & data sources (use, don’t rebuild)

**How GroundYield plugs into tools that already do weather, calendars, and pest ID well**  
Last updated: 27 July 2026  
**Status:** Desk catalogue v0 · verify on ground what farmers and extension actually use in Inhambane  

Related: [KPI_AND_DATA.md](KPI_AND_DATA.md) · [AI_FIELD_PATH.md](AI_FIELD_PATH.md) · [AI_AGRONOMY.md](AI_AGRONOMY.md) · [SEASON.md](SEASON.md) · [SYSTEM.md](SYSTEM.md)

---

## 1. Principle

> **We do not build another rain satellite or generic planting-date oracle.**  
> We **use** proven apps and open data where they are good, and we **own** the thin layer that makes the pilot honest: unit IDs, baselines, costs, yields, consent, expert escalation, public failures.

| Layer | Prefer existing tools | GroundYield builds / logs |
|-------|----------------------|---------------------------|
| Weather & rain | Forecast apps, open APIs, climate explorers | Local “did it rain here?” notes when deciding irrigation |
| Seasonal calendar | National/extension calendars + apps | **Actual** plant/harvest dates per unit |
| Pest / disease ID | Photo ID apps as assist | Expert ticket when chemical or unsure |
| Market prices | Local asking + any national systems if useful | Farm-gate F samples we took |
| Agronomy chat | LLM + our package rules + experts | Scripts, freeze gates, harm log |
| Integrity | — | Registry, baselines, UPDATES |

**AI role with external apps:** recommend, deep-link, or summarize *with source named* — never strip the source and claim “GroundYield weather.”

---

## 2. What to use for what

### A. Rain & weather (high reuse)

| Tool / source | Strength | Weakness in village | How we use | Data mark |
|---------------|----------|---------------------|------------|-----------|
| **Phone weather apps** (e.g. manufacturer weather, AccuWeather, WeatherBug — whatever is already installed) | Fast forecast | Coarse grid; not field-level | Daily planning | **E/H** |
| **Windy / similar** | Rain radar & models visible | Needs data; skill to read | Operator & training demos | E |
| **Open-Meteo** (open API) | Free forecast/historical API for bots | Not a farmer brand app | Optional backend for our reminders | E |
| **CHIRPS / satellite rainfall** (via climate explorers, Google Earth Engine tutorials, regional dashboards) | Good regional rain history | Not “today on my plot” | Season context, research | E |
| **Local rain** | Truth on the plot | Labor | Optional jar/gauge or simple wet/dry log | **F** if same-day log |

**Rule:** For public claims (“drought killed the crop”), prefer **local note F** + optional app E, not app alone.

### B. Planting dates & calendars (high reuse)

| Tool / source | Strength | How we use |
|---------------|----------|------------|
| **[SEASON.md](SEASON.md)** (our indicative calendar) | Tied to pilot package | Default prompts |
| **MADER / extension seasonal advice** (when available locally) | Official, local crops | Prefer over foreign calendars |
| **FAO / digital agriculture materials** | Training content | Education at school hub |
| **Existing farmer calendar apps** (region-dependent — *list what you find on trip*) | Already on phones | Don’t fight them; align prompts |

**Rule:** App says “plant window” = **guidance E**. **Actual plant date** per unit = **F** we record (KPI path to Y*).

### C. Pest, disease, nutrient visual assist (medium reuse)

| Tool type | How we use | Hard stop |
|-----------|------------|-----------|
| Plant photo ID / extension apps (e.g. global plant doctor–style apps, regional tools) | Suggest **hypotheses** in CHOICE step | No auto pesticide prescription from app alone |
| WhatsApp photo to expert panel | Real decision support | Required for chemicals (G5 path) |

Examples to **evaluate on trip** (not endorsed until tested offline/MZ network): Plantix-class apps, any Mozambican ministry/NGO tools extension workers already push. Log real names in GROUND_TRIP → update this table.

### D. Markets & prices (local first)

| Source | Use |
|--------|-----|
| Walk markets / lodges / traders | **Primary F** samples ([BUYER_INTERVIEW](field/BUYER_INTERVIEW.md)) |
| National price info systems (if phone-accessible) | Context E only |

### E. Connectivity

| Tool | Use |
|------|-----|
| **Starlink** school hub | Access to weather sites, demos, photo upload — [STARLINK_APPROACH](field/STARLINK_APPROACH.md) |
| Mobile data | Everyday WhatsApp |
| Offline PDFs | When apps won’t load — FIELD_KIT |

---

## 3. What we will **not** rebuild

| Do not build v1 | Why |
|-----------------|-----|
| Global weather model | Open-Meteo / phone apps exist |
| Satellite processing pipeline | Out of scope for modular pilot |
| Generic “AI agronomist” with no package ceiling | Safety + integrity |
| Parallel unit registry in a closed app | Public CSV/site is the source of truth |
| Crypto / token farmer coins | Not our model |

---

## 4. How AI should use existing apps (product rules)

1. **Name the source** — “According to [Weather app / Open-Meteo], rain possible Thu — check your soil.”  
2. **Prefer local confirm** — “Did it rain on your plot? Reply SIM/NÃO.”  
3. **Calendar = soft** — “SEASON.md + local extension window; your plant date is what you send us.”  
4. **Pest app = hypothesis** — “App suggests X; send photo to expert before spray.”  
5. **Log tool used** — KPI **A6** (app name) for learning what works in Vilanculos.  
6. **Works offline-poor** — If app needs fat data, Starlink hub or evening download; else SMS tick.

Pseudo-flow:

```
Farmer question: "Plant maize this week?"
    → Pull calendar: SEASON.md + any local extension note
    → Pull weather: phone app or Open-Meteo (label source)
    → Ask: soil moisture / last rain (farmer F)
    → CHOICE answer: plant / wait / prepare only
    → If chemical or disease: escalate expert (not app-only)
```

---

## 5. Integration options (technical, later)

| Depth | When | Effort |
|-------|------|--------|
| **Human points at app** (L1 demo) | Now | Zero code |
| **Ops pastes forecast into WhatsApp** | L2 manual | Low |
| **Bot calls Open-Meteo + our unit context** | L3 | Medium |
| **Deep-link to Play Store app** | If one app dominates locally | Low |
| **Official ministry API** | If exists and stable | Evaluate |

No vendor lock-in claim until a tool is chosen and named on WHO/UPDATES.

---

## 6. Trip questions (fill this catalogue with F)

Ask farmers, agro-dealers, extension, schools:

1. What app do you open for **rain**?  
2. Who tells you **when to plant** (radio, neighbour, app, extension)?  
3. Any **pest photo** app used?  
4. Network: WhatsApp only, or enough data for maps?  
5. Would a **school Starlink evening** help download forecasts?

Log answers → append table below.

### Field findings (empty until trip)

| Date | Place | Tool named | Use | Notes |
|------|-------|------------|-----|-------|
| | | | | |

---

## 7. One-line stance

> **Best weather and calendar tools should stay best-in-class elsewhere.**  
> GroundYield measures **what happened on the unit** and uses those tools as **inputs to better choices** — with experts when it matters.

Last updated: 27 July 2026
