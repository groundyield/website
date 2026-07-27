# Field interview scripts v0

**Languages:** Portuguese primary with farmers/leaders; English for operator notes.  
**Truth marks:** write **F** (fact observed/quoted), **E** (estimate), **H** (hearsay) on every number.  
**IDs:** assign temporary IDs (`LOC-01`, `FARM-03`) — no full names in public files without consent.

Related: [CONSENT_SCRIPT.md](CONSENT_SCRIPT.md) · [BASELINE_FORM.md](BASELINE_FORM.md) · [CONSENT.md](../CONSENT.md)

---

## 0. Opening (always)

**PT**

> Bom dia. Chamo-me Jacques Theron. Trabalho no piloto aberto GroundYield (agricultura modular, dados públicos). Não pedimos dinheiro hoje. Queremos aprender como a produção e o mercado funcionam aqui, e se um piloto de unidades com rega solar faria sentido. Posso fazer algumas perguntas? Pode parar a qualquer momento.

**EN (operator):** Hand the one-pager. Confirm language preference. Note location + date.

---

## 1. Community leader / association (15–25 min)

| # | Prompt (PT) | Capture |
|---|-------------|---------|
| 1 | Quem decide sobre acesso à terra para um piloto de agricultura? | Roles, not only titles |
| 2 | Que associações de agricultores existem perto de Vilanculos? | Names of **orgs** only if public |
| 3 | Quais as principais culturas e dificuldades desta zona? | List + F/E/H |
| 4 | Há rega (poços, rios, furos)? Quem gere a água? | Water governance |
| 5 | O turismo compra produtos locais? Que culturas? | Market signal |
| 6 | Que preocupações teria com um projecto de fora? | Land, water, elite capture |
| 7 | Quem mais devo ouvir antes de avançar? | Introductions path |
| 8 | Preferem contacto por telefone, WhatsApp, ou reunião? | Channel |

**Close (PT):** Obrigado. Vamos publicar o que aprendermos de forma geral (sem nomes privados). Contacto: team@groundyield.org

---

## 2. Farmer / household plot (20–35 min)

Do **not** start with income. Build trust; income only with explicit consent later.

| # | Prompt (PT) | Maps to baseline |
|---|-------------|------------------|
| 1 | Que culturas plantou na última época? | crop |
| 2 | Qual a área aproximada (ha ou passos/local)? | notes |
| 3 | Quanto colheu? (saco, lata, kg — anote a unidade local) | local_yield_value + unit |
| 4 | Foi ano normal, mau ou bom? | notes + E |
| 5 | Chuva só, ou rega? Fonte de água? | water_source |
| 6 | Que semente usou? (própria / mercado / projecto) | seed_type |
| 7 | Usou fertilizante? Que tipo e quanto (mesmo aproximado)? | fertilizer_used |
| 8 | Onde guarda a colheita? Perdas por insectos/humidade? | storage_method |
| 9 | A quem vende? Preço aproximado e época? | notes (market) |
| 10 | O que mais limita a produção aqui? | notes (constraint) |
| 11 | Se tivesse rega fiável na estação seca, o que plantaria? | interest (not commitment) |
| 12 | Aceitaria partilhar números anónimos (unidade ID) em público? | consent flag |

**Conversion note:** Always keep the **local unit**. Convert to kg/ha later with method written in notes (E).

---

## 3. Supplier / installer (10–20 min)

| # | Prompt | Capture for SUPPLIERS / quotes CSV |
|---|--------|-------------------------------------|
| 1 | Item + exact spec (kWp, pump head, bag size) | spec |
| 2 | Unit price + currency + VAT? | price, currency |
| 3 | Delivery to Vilanculos / install site? | lead time, notes |
| 4 | Warranty / spare parts | notes |
| 5 | Typical install time | notes |
| 6 | Kit bundle price if sold as package | kit row |
| 7 | Public company name OK? | source_public |

Mark every price **F** only if written quote or clear verbal with date; else **E**.

---

## 4. What not to promise

- Fixed yield doubles  
- Free equipment without process  
- Jobs or land deals on first meeting  
- That the pilot is already fully funded for every household  

---

## 5. After the interview

- [ ] Consent status recorded  
- [ ] Baseline form started (even partial)  
- [ ] Quotes logged with date  
- [ ] One sentence public-safe summary for [GROUND_TRIP.md](../GROUND_TRIP.md) Notes Log  
- [ ] Private full names only in offline notes  

Last updated: 27 July 2026
