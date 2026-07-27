# -*- coding: utf-8 -*-
"""Build printable multi-page field forms PDF (EN prompts + PT scripts + blanks)."""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak,
)
from reportlab.lib.enums import TA_LEFT

OUT = Path(__file__).resolve().parent / "GroundYield_Field_Forms_EN_PT.pdf"

ACCENT = colors.HexColor("#1f8a5c")
INK = colors.HexColor("#1a2332")
MUTED = colors.HexColor("#5b6b80")
LINE = colors.HexColor("#d8dfe6")

styles = getSampleStyleSheet()

def mk(name, parent, **kw):
    s = ParagraphStyle(name, parent=styles[parent], **kw)
    styles.add(s)
    return s

mk("T", "Title", fontName="Helvetica-Bold", fontSize=18, leading=21, textColor=INK, spaceAfter=2)
mk("Tag", "Normal", fontName="Helvetica", fontSize=9.5, leading=12, textColor=MUTED, spaceAfter=8)
mk("H", "Heading2", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=ACCENT, spaceBefore=8, spaceAfter=3)
mk("B", "Normal", fontName="Helvetica", fontSize=9, leading=12, textColor=INK, spaceAfter=3)
mk("N", "Normal", fontName="Helvetica-Oblique", fontSize=8, leading=10.5, textColor=MUTED, spaceAfter=3)
mk("F", "Normal", fontName="Helvetica", fontSize=8, leading=10, textColor=MUTED)

def hr():
    return HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8)

def blank_line(label, width_hint="_" * 42):
    return Paragraph(f"<b>{label}</b> {width_hint}", styles["B"])

def tick_row(items):
    # items: list of short labels
    cells = [[Paragraph(f"☐ {i}", styles["B"]) for i in items]]
    t = Table(cells, colWidths=[170 / max(len(items), 1) * mm] * len(items) if False else None)
    # fixed simple flow as paragraphs instead
    return Paragraph(" · ".join(f"☐ {i}" for i in items), styles["B"])

def build():
    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=14 * mm, rightMargin=14 * mm,
        topMargin=12 * mm, bottomMargin=12 * mm,
        title="GroundYield Field Forms EN+PT",
        author="GroundYield",
    )
    story = []

    # ---- Page 1: Consent + rules
    story.append(Paragraph("GroundYield — Field forms", styles["T"]))
    story.append(Paragraph(
        "Offline pack · Vilanculos pilot · Print before travel · Not a funding pitch",
        styles["Tag"]))
    story.append(hr())

    story.append(Paragraph("Hard rules", styles["H"]))
    for line in [
        "Baseline before any impact claim. Local yields, not national averages.",
        "Planning cost band ≠ payment offer. No money ask on first community meeting.",
        "Mark every number F (fact) / E (estimate) / H (hearsay). Blank = unknown — never invent 0.",
        "Full names & home GPS stay private unless clear consent + need.",
    ]:
        story.append(Paragraph(f"→ {line}", styles["B"]))

    story.append(Paragraph("Consent (Portuguese — read aloud)", styles["H"]))
    story.append(Paragraph(
        "Queremos aprender e publicar de forma aberta os <b>resultados do piloto</b> "
        "(custos, produções, o que falhou), para outros poderem copiar o que funcionar. "
        "<b>Não</b> publicamos o seu nome completo nem a localização exacta da casa, salvo se autorizar. "
        "Podemos usar um <b>código de unidade</b>. Pode recusar perguntas e pedir para parar. "
        "Contacto: team@groundyield.org",
        styles["B"]))

    story.append(Paragraph("Tick with the person", styles["H"]))
    rows = [
        ["Item", "Yes", "No", "Later"],
        ["Conversation today", "☐", "☐", "☐"],
        ["Anonymized production numbers public", "☐", "☐", "☐"],
        ["Crop / equipment photos", "☐", "☐", "☐"],
        ["Photos with identifiable face", "☐", "☐", "☐"],
        ["Household income detail public", "☐", "☐", "☐"],
    ]
    t = Table(rows, colWidths=[95 * mm, 25 * mm, 25 * mm, 25 * mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (-1, -1), INK),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eef6f1")),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))
    story.append(blank_line("Date"))
    story.append(blank_line("Temp ID (e.g. FARM-01)"))
    story.append(blank_line("Location (area, not home GPS)"))
    story.append(blank_line("Interviewer"))
    story.append(Paragraph("GroundYield · field forms · page 1/4 · 27 Jul 2026", styles["F"]))

    # ---- Page 2: Opening + leader interview
    story.append(PageBreak())
    story.append(Paragraph("Interview — opening + community leader", styles["T"]))
    story.append(Paragraph("Jacques Theron · GroundYield · no money ask today", styles["Tag"]))
    story.append(hr())

    story.append(Paragraph("Opening (PT)", styles["H"]))
    story.append(Paragraph(
        "Bom dia. Chamo-me Jacques Theron. Trabalho no piloto aberto GroundYield "
        "(agricultura modular, dados públicos). <b>Não pedimos dinheiro hoje.</b> "
        "Queremos aprender como a produção e o mercado funcionam aqui, e se um piloto "
        "de unidades com rega solar faria sentido. Posso fazer algumas perguntas? "
        "Pode parar a qualquer momento.",
        styles["B"]))

    story.append(Paragraph("Leader prompts (capture short notes)", styles["H"]))
    prompts = [
        "1. Quem decide acesso à terra para um piloto?",
        "2. Associações de agricultores perto de Vilanculos?",
        "3. Principais culturas e dificuldades da zona?",
        "4. Há rega (poços/furos/rios)? Quem gere a água?",
        "5. Turismo compra produtos locais? Quais?",
        "6. Preocupações com um projecto de fora?",
        "7. Quem mais devo ouvir? (introductions)",
        "8. Melhor canal: telefone / WhatsApp / reunião?",
    ]
    for p in prompts:
        story.append(Paragraph(p, styles["B"]))
        story.append(Paragraph("_" * 95, styles["N"]))

    story.append(Paragraph("Close (PT): Obrigado. Publicamos aprendizagens gerais sem nomes privados. team@groundyield.org", styles["N"]))
    story.append(Paragraph("GroundYield · field forms · page 2/4 · 27 Jul 2026", styles["F"]))

    # ---- Page 3: Farmer interview + baseline blanks
    story.append(PageBreak())
    story.append(Paragraph("Farmer interview + baseline blanks", styles["T"]))
    story.append(Paragraph("One plot per form · map to data/schema-baseline.csv", styles["Tag"]))
    story.append(hr())

    story.append(Paragraph("Header", styles["H"]))
    for lab in ["Date", "Temp ID", "Location area", "Language", "Consent anonymized yield (Y/N/later)"]:
        story.append(blank_line(lab))

    story.append(Paragraph("Crop baseline", styles["H"]))
    headers = ["Field", "Value", "F/E/H"]
    data = [
        headers,
        ["Crop", "", ""],
        ["Local yield amount", "", ""],
        ["Local unit (saco/lata/kg)", "", ""],
        ["kg/ha estimate (if any)", "", ""],
        ["Season / year", "", ""],
        ["Water (rainfed/well/…)", "", ""],
        ["Seed type", "", ""],
        ["Fertilizer used", "", ""],
        ["Storage method", "", ""],
    ]
    t2 = Table(data, colWidths=[55 * mm, 95 * mm, 20 * mm])
    t2.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eef6f1")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("TEXTCOLOR", (0, 0), (-1, -1), INK),
    ]))
    story.append(t2)
    story.append(Spacer(1, 4))
    story.append(Paragraph("Conversion method (if kg/ha): " + "_" * 60, styles["B"]))
    story.append(Paragraph("Notes (no private names): " + "_" * 55, styles["B"]))
    story.append(Paragraph("_" * 95, styles["N"]))
    story.append(Paragraph("_" * 95, styles["N"]))

    story.append(Paragraph("Constraints (tick)", styles["H"]))
    story.append(Paragraph(
        "☐ Water  ☐ Seed  ☐ Fertilizer  ☐ Pests  ☐ Labour  ☐ Storage  ☐ Market  ☐ Tenure  ☐ Other ______",
        styles["B"]))
    story.append(Paragraph("GroundYield · field forms · page 3/4 · 27 Jul 2026", styles["F"]))

    # ---- Page 4: Supplier quote blanks + pocket scripts
    story.append(PageBreak())
    story.append(Paragraph("Supplier quotes + pocket scripts", styles["T"]))
    story.append(Paragraph("Replace UNIT.md planning bands with dated quotes", styles["Tag"]))
    story.append(hr())

    story.append(Paragraph("Quote log (one row per item)", styles["H"]))
    qh = ["Date", "Item / spec", "Price + cur", "Lead t.", "Source public", "F/E"]
    qd = [qh] + [["", "", "", "", "", ""] for _ in range(6)]
    t3 = Table(qd, colWidths=[22 * mm, 50 * mm, 28 * mm, 20 * mm, 40 * mm, 14 * mm])
    t3.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eef6f1")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(t3)

    story.append(Paragraph("WhatsApp pocket (after enrollment only)", styles["H"]))
    story.append(Paragraph(
        "<b>Opt-in:</b> Olá — GroundYield (piloto Vilanculos). Lembretes da época. "
        "SIM=continuar · PARE=sair. Dados públicos: ID unidade. team@groundyield.org",
        styles["B"]))
    story.append(Paragraph(
        "<b>Plantio:</b> GroundYield · Unidade {ID} — registe data sementeira + cultura. "
        "Não exceder doses do pacote. ESPAÇO=ajuda espaçamento.",
        styles["B"]))
    story.append(Paragraph(
        "<b>Orçamento:</b> Pedimos orçamento escrito: {item+spec}. Preço, moeda, IVA, "
        "prazo entrega Vilanculos, garantia. team@groundyield.org",
        styles["B"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Dead ends (do not delete)", styles["H"]))
    story.append(Paragraph("Date ______  Lead ______  Why closed " + "_" * 40, styles["B"]))
    story.append(Paragraph("Date ______  Lead ______  Why closed " + "_" * 40, styles["B"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Full scripts: field/INTERVIEW.md · CONSENT_SCRIPT.md · BASELINE_FORM.md · "
        "POCKET_SCRIPTS.md · SUPPLIERS.md · groundyield.org",
        styles["N"]))
    story.append(Paragraph("GroundYield · field forms · page 4/4 · 27 Jul 2026 · MIT / open pilot", styles["F"]))

    doc.build(story)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")

if __name__ == "__main__":
    build()
