# Supplier & quote log v0

**Purpose:** Replace planning ranges in [UNIT.md](UNIT.md) with **dated, sourced quotes**.  
**Status:** Desk leads listed · **zero field quotes** with price yet.

Truth rules match [GROUND_TRIP.md](GROUND_TRIP.md): fact / estimate / hearsay; units and date; no private names without consent.

---

## How to log a quote

1. One row per item (or clear kit bundle).  
2. Currency + tax/VAT stated.  
3. Delivery location and lead time.  
4. Contact channel (phone/WhatsApp/email) kept **private** if needed; public log can say “Vilanculos installer A”.  
5. After 3+ solid quotes in a category, update UNIT.md mid band and note the date.

---

## Desk research leads (not quotes)

**Truth: H/secondary** — found via public web 27 Jul 2026.  
**Not prices.** Not endorsement. Not “available in Vilanculos.”  
Use as **call list** on the trip / outreach. Close into quote tables only with a dated written quote.

**Expanded local walk-in list (Vilanculos + corridor):** [field/LOCAL_CONTACTS.md](field/LOCAL_CONTACTS.md)

### Irrigation / solar water (SA + regional)

| Lead (public) | Why relevant | Public entry | Region note | Status |
|---------------|--------------|--------------|-------------|--------|
| Futurepump | Smallholder solar irrigation pumps (shared widely in E/S Africa) | https://futurepump.com | Confirm MZ/SA dealers | lead |
| Lorentz | Solar water pumping systems (commercial / agri) | https://www.lorentz.de | SA distributor network — verify | lead |
| Local solar installers (Maputo / Inhambane) | Site install + panels | *find on trip* | Prefer installers who service Vilanculos | open |

### Seed / fertilizer (Mozambique)

| Lead (public) | Why relevant | Public entry | Region note | Status |
|---------------|--------------|--------------|-------------|--------|
| SEMOC (Sementes de Moçambique) | National seed company / improved seed channel | search: SEMOC Mozambique seed | Availability by province TBD | lead |
| Input agro-dealers (Inhambane / Vilanculos town) | NPK, urea, hybrid maize | *walk market on trip* | Prefer dated till receipt | open |
| Provincial agriculture / extension desk | Variety recommendations | *office visit* | Not a commercial supplier | lead |

### Hermetic storage

| Lead (public) | Why relevant | Public entry | Region note | Status |
|---------------|--------------|--------------|-------------|--------|
| PICS Global (hermetic bags) | Smallholder grain storage bags used across Africa | https://picsglobal.com | Find authorized retailer; avoid counterfeits | lead |
| GrainPro hermetic bags | Commercial hermetic liners | https://www.grainpro.com | Import/lead time TBD | lead |
| Local agro-dealers | May stock generic hermetic / triple bags | *trip* | Verify brand authenticity | open |

### How these become real quotes

1. Email/call using [field/OUTREACH_EMAIL.md](field/OUTREACH_EMAIL.md) template B.  
2. Require written price + currency + VAT + lead time + delivery to Vilanculos area.  
3. Paste into tables below with date and **F** if written.  
4. Log dead ends (no reply / no delivery to MZ) in Dead ends.

---

## Irrigation (capital) — field quotes

| Date | Item | Spec | Unit price | Qty | Total | Currency | Source (public) | Lead time | Notes (fact/est) | Status |
|------|------|------|------------|-----|-------|----------|-----------------|-----------|------------------|--------|
| | Solar panels | kWp | | | | | | | | open |
| | Pump + controller | type/depth | | | | | | | | open |
| | Pipe / fittings | for 0.25–0.5 ha | | | | | | | | open |
| | Install labour | | | | | | | | | open |

## Crop inputs (operating) — field quotes

| Date | Item | Spec | Price | Currency | Source | Notes | Status |
|------|------|------|-------|----------|--------|-------|--------|
| | Hybrid/improved seed | crop, variety | | | | | open |
| | Fertilizer | NPK/urea, bag size | | | | | open |
| | Crop protection | | | | | | open |

## Storage — field quotes

| Date | Item | Spec | Price | Currency | Source | Notes | Status |
|------|------|------|-------|----------|--------|-------|--------|
| | Hermetic bags | brand, capacity | | | | | open |

## Livestock (optional modules)

| Date | Item | Spec | Price | Currency | Source | Notes | Status |
|------|------|------|-------|----------|--------|-------|--------|
| | Day-old / started birds | | | | | | open |
| | Feed | | | | | | open |

---

## Kit bundles (preferred when sold as package)

| Date | Kit name | Includes | Price | Currency | Source | vs UNIT mid (~$2,025) | Status |
|------|----------|----------|-------|----------|--------|----------------------|--------|
| | | | | | | | open |

---

## Dead ends

| Date | Lead | Why closed |
|------|------|------------|
| | | |

---

## Machine-readable

Template: [data/quotes-template.csv](data/quotes-template.csv)

`date,category,item,spec,price,currency,qty,total,source_public,lead_time_days,delivery_location,vat_included,truth,notes,status`

---

Last updated: 27 July 2026 (desk leads added; still zero priced quotes)  
Related: [UNIT.md](UNIT.md) · [GROUND_TRIP.md](GROUND_TRIP.md) · [ECONOMICS.md](ECONOMICS.md) · [field/GATES.md](field/GATES.md)
