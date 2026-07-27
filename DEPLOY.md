# Deploy — GroundYield website

**Goal:** Production always equals `main` on this repo. No partial uploads.

---

## Canonical path (required)

1. **Source of truth:** `github.com/groundyield/website` branch **`main`**
2. **Host:** Vercel project **`groundyield`** (team: Jacques Theron’s projects)
3. **Domains:** `www.groundyield.org` (canonical) · apex redirects to www

### Git connection (done 27 Jul 2026)

Vercel project **groundyield** is linked to **`github.com/groundyield/website`**, production branch **`main`**, repository root. Every push to `main` deploys the full tree — including binaries (`og-image.png`, icons, field PDF).

If the link is ever broken: Settings → Git → connect `groundyield/website` again (not the sluiper fork).

---

## Hard rules

| Rule | Why |
|------|-----|
| **Never** deploy a partial file set to production | Replaces the whole deployment; missing files 404 (`pt.html`, `og-image.png`, etc.) |
| **Never** claim “shipped” until live HTTP 200 | Repo-only is not production |
| Prefer **Git push → Vercel** over CLI/file upload | Full tree, reproducible |
| Edit content on **GitHub `main`**, not only on Vercel | Avoid live/repo drift |

### Ship-check (preferred)

```bash
./scripts/ship-check.sh
```

Runs data template checks + production live-verify. Do not mark UPDATES “live” until this passes.

### Live-verify checklist (after every deploy)

Open these and confirm **200** (hard refresh if needed):

- [ ] `https://www.groundyield.org/`
- [ ] `https://www.groundyield.org/pt.html`
- [ ] `https://www.groundyield.org/robots.txt`
- [ ] `https://www.groundyield.org/sitemap.xml`
- [ ] `https://www.groundyield.org/updates.rss`
- [ ] `https://www.groundyield.org/favicon.svg`
- [ ] `https://www.groundyield.org/og-image.png`
- [ ] `https://www.groundyield.org/apple-touch-icon.png`
- [ ] `https://www.groundyield.org/icon-512.png`

Only then add a line to [UPDATES.md](UPDATES.md).

---

## Static surface that must ship together

| Path | Role |
|------|------|
| `index.html` | English landing |
| `pt.html` | Portuguese landing |
| `404.html` | Not found |
| `robots.txt` | Crawlers |
| `sitemap.xml` | Discovery |
| `updates.rss` | Feed |
| `favicon.svg` | Icon |
| `og-image.png` | 1200×630 share card |
| `apple-touch-icon.png` | iOS |
| `icon-512.png` | PWA / schema logo |
| `vercel.json` | Headers / clean URLs |

Markdown docs (`PLAN.md`, `UNIT.md`, …) live on **GitHub**; the site links to them. They do not need to be “hosted” as HTML unless we choose to later.

---

## Emergency: CLI / file deploy

Only if Git integration is broken. You must include **every** file in the table above (binaries included). Uploading only `index.html` **will** drop `pt.html` and images.

```bash
# From a full local clone of main — never from a sparse folder
vercel --prod --cwd .
```

---

## Content update workflow

1. Edit on a branch or directly on `main` (small ops fixes OK on main for now).
2. Push to GitHub.
3. Wait for Vercel production deploy (or Redeploy).
4. Run live-verify checklist.
5. Append [UPDATES.md](UPDATES.md); mirror top entry on `index.html` + `updates.rss` if user-facing.

---

## Known failure mode (27 Jul 2026)

Partial production deploys left `robots.txt` / `sitemap` OK but **`/` 404** or **`og-image.png` 404**. Root cause: deploy payload ≠ full `main` tree. Cure: Git-connected full redeploy from `main`.

---

Last updated: 27 July 2026
