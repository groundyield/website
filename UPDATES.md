# Public Updates

**Source of truth** for the homepage Updates section and [updates.rss](updates.rss).  
Newest first. Do not silently edit old entries — append corrections.

**Process rule:** Do not claim a URL “shipped” until it returns HTTP 200 on **www.groundyield.org** (cache-bust if needed). Repo-only is not live.

---

## 27 Jul 2026 — Full static deploy fix + orphaned docs

- Deploy package includes `robots.txt`, `sitemap.xml`, `updates.rss`, favicon, icons, `pt.html`, `og-image.png` (not only `index.html`).
- Public Documents on the site now links SEASON, AI_AGRONOMY, PARTNERSHIPS (were README-only).
- Sitemap lists `/` and `/pt.html`.

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
