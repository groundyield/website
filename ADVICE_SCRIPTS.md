# Agronomy advice scripts v0 (WhatsApp / SMS)

**Language:** Portuguese primary (Mozambique). English notes for operators.  
**Channel:** Manual WhatsApp first ([AI_AGRONOMY.md](AI_AGRONOMY.md)).  
**Offline pocket copy:** [field/POCKET_SCRIPTS.md](field/POCKET_SCRIPTS.md) · full kit [field/FIELD_KIT.md](field/FIELD_KIT.md)

---

## Freeze status (staged — see [AI_FIELD_PATH.md](AI_FIELD_PATH.md))

| Level | Status | Meaning |
|-------|--------|---------|
| **L0** Ops AI | **Open** | Internal drafting, translate, plan work |
| **L1** Show & choose demo | **Open** | Community demos of CHOICE helper; **no** enrolled-unit chemical rates as “pilot advice” |
| **L2** AI draft + human send | **CLOSED** until **G5-A** | Scripts below not cleared for live enrolled units |
| **L3** Instant field + experts | **CLOSED** until **G5-B** | No unsupervised instant rates |

| | |
|---|---|
| **Live enrolled send (L2)** | **DRAFT ONLY — NOT CLEARED** |
| **Why still closed** | No enrolled users; no named agronomy reviewer on WHO yet; no legal review of advice/data practice |
| **Allowed now** | Internal rewrite; expert recruitment; **L1 demos** (show how AI helps choose — see AI_FIELD_PATH) |
| **Not allowed** | Messaging real farmers with fertilizer/pesticide/water **rates** from these drafts as GroundYield service |

Safety bullets below are **intent**, not a substitute for licensed extension advice or legal counsel ([CONSENT.md](CONSENT.md)).

When **G5-A** lifts, replace this table with: reviewer name/org + date + “L2 open”.  
When **G5-B** lifts: add expert SLA + “L3 open”.

---

## Safety rules (every message — when live)

- No fertilizer rates above the published package without a written reason.  
- Prefer “observe and send a photo” over guessing pests.  
- Water advice never exceeds pump/well limits.  
- Escalate uncertain cases to a human partner.  
- Farmer can opt out of the channel anytime.

---

## Enrollment (copy/paste)

**PT**

```
Olá — aqui é o GroundYield (piloto aberto em Vilanculos).
Vamos enviar lembretes simples da época e responder perguntas sobre a sua unidade.
Responda SIM para continuar, ou PARE para sair.
Os dados públicos usam ID da unidade, não o seu nome completo, salvo se consentir.
Contacto: team@groundyield.org
```

**EN (operator note):** Confirm consent language before first send; see [CONSENT.md](CONSENT.md).

---

## Weekly backbone (maize-focused season)

Adjust months using [SEASON.md](SEASON.md) and local rains.

### Pre-plant / land prep

```
GroundYield · Unidade {ID}
Esta semana: preparar o terreno e confirmar semente + fertilizante (microdose).
Envie foto do talhão se quiser feedback.
Pergunta: já tem semente melhorada para esta época? (sim/não)
```

### Planting week

```
GroundYield · Unidade {ID}
Plantio: registe a data de sementeira (AAAA-MM-DD) e a cultura.
Microdose: seguir o pacote da unidade — não exceder as doses combinadas.
Precisa de ajuda com espaçamento? Responda ESPAÇO.
```

### Mid-season

```
GroundYield · Unidade {ID}
Controlo: ervas, pragas, água.
Se ver folhas danificadas, envie 1 foto à luz do dia.
Não aplique produto novo sem confirmar o nome do produto.
```

### Pre-harvest / storage

```
GroundYield · Unidade {ID}
Colheita a aproximar-se: planear secagem e sacos herméticos.
Objectivo: reduzir perdas pós-colheita.
Quando colher, diga-nos kg aproximados + data (mesmo estimativa).
```

### Cash crops (veg, irrigated)

```
GroundYield · Unidade {ID}
Hortícolas: rega regular > excesso pontual.
Mercado: anote preço de venda e comprador (hotel/mercado/vizinho) para o registo público da unidade.
```

---

## Short FAQ replies (PT)

| Trigger | Reply sketch |
|---------|----------------|
| Água / bomba | Verificar painel limpo, ligações, nível do poço. Não forçar a bomba a seco. |
| Fertilizante | Só microdose do pacote. Enviar foto do saco se dúvida. |
| Praga | Foto + local na planta. Evitar pesticida largo sem identificação. |
| Preço | Registar preço e data; não prometemos preço de mercado. |
| PARE | Confirmado — sem mais mensagens. Pode voltar com SIM. |

---

## Logging (internal)

For each week, note: unit ID, message version, reply rate, escalations, any bad-advice correction (publish corrections publicly).

---

## Build sequence

1. Manual sends to first units  
2. Weekly templates above  
3. LLM-assisted drafts with human review  
4. Evaluation report end of Season 1  

---

Last updated: 27 July 2026  
Related: [AI_AGRONOMY.md](AI_AGRONOMY.md) · [SEASON.md](SEASON.md) · [CONSENT.md](CONSENT.md)
