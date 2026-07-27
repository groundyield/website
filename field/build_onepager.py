\
# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, ListFlowable, ListItem)
from reportlab.lib.enums import TA_LEFT

ACCENT = colors.HexColor("#1f8a5c")
INK = colors.HexColor("#1a2332")
MUTED = colors.HexColor("#5b6b80")
LINE = colors.HexColor("#d8dfe6")

styles = getSampleStyleSheet()

def mk(name, parent, **kw):
    s = ParagraphStyle(name, parent=styles[parent], **kw)
    styles.add(s)
    return s

mk("GYTitle", "Title", fontName="Helvetica-Bold", fontSize=22, leading=25,
   textColor=INK, spaceAfter=2, alignment=TA_LEFT)
mk("GYTagline", "Normal", fontName="Helvetica", fontSize=10.5, leading=14,
   textColor=MUTED, spaceAfter=10)
mk("GYH2", "Heading2", fontName="Helvetica-Bold", fontSize=11, leading=13,
   textColor=ACCENT, spaceBefore=10, spaceAfter=4, upperCase=0)
mk("GYBody", "Normal", fontName="Helvetica", fontSize=9.7, leading=13.5,
   textColor=INK, spaceAfter=4)
mk("GYNote", "Normal", fontName="Helvetica-Oblique", fontSize=8.6, leading=12,
   textColor=MUTED, spaceAfter=4)
mk("GYBullet", "Normal", fontName="Helvetica", fontSize=9.7, leading=13.5,
   textColor=INK, leftIndent=0)
mk("GYFoot", "Normal", fontName="Helvetica", fontSize=8.2, leading=11,
   textColor=MUTED)

def header(title, tagline):
    return [
        Paragraph(title, styles["GYTitle"]),
        Paragraph(tagline, styles["GYTagline"]),
        HRFlowable(width="100%", thickness=1.1, color=ACCENT, spaceAfter=10),
    ]

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, styles["GYBullet"]), leftIndent=12, spaceAfter=3) for i in items],
        bulletType="bullet", bulletColor=ACCENT, start="→", bulletFontSize=9,
    )

def contact_table(rows):
    t = Table(rows, colWidths=[38*mm, 118*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME", (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 9.4),
        ("TEXTCOLOR", (0,0), (0,-1), MUTED),
        ("TEXTCOLOR", (1,0), (1,-1), INK),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("LINEBELOW", (0,0), (-1,-2), 0.4, LINE),
    ]))
    return t

# ---------------------------------------------------------------- EN PAGE
en = []
en += header("GroundYield", "Open modular farm pilot &middot; Vilanculos, Inhambane Province, Mozambique")

en.append(Paragraph("What this is", styles["GYH2"]))
en.append(Paragraph(
    "A transparent pilot of modular farm units for smallholders: solar irrigation, improved seed "
    "and micro-dosed fertilizer, phone-based agronomy advice, hermetic storage, and optional "
    "poultry/goat modules. Every cost, yield, income figure, and failure is published openly &mdash; "
    "the model is designed to be copied, not owned.", styles["GYBody"]))

en.append(Paragraph("Season 1 commitments", styles["GYH2"]))
en.append(bullets([
    "30&ndash;60 modular units in the Vilanculos area",
    "Target 80&ndash;100%+ yield increase on staple crops &mdash; measured against a <b>local baseline</b>, not national averages",
    "Raise household income via cash crops and poultry",
    "Publish costs, yields, incomes and failures in real time",
]))

en.append(Paragraph("Planning cost (Year 0, per unit)", styles["GYH2"]))
en.append(Paragraph(
    "&#126;USD 1,270&ndash;2,985 &mdash; a planning range, not a raised budget or an offer of payment. "
    "Full bill of materials: UNIT.md on the project repository.", styles["GYBody"]))

en.append(Paragraph("Who is behind this", styles["GYH2"]))
en.append(Paragraph(
    "<b>Jacques Theron</b> &mdash; founder / operator. GroundYield is self-funded; there is no "
    "registered legal entity yet, stated plainly on purpose. Funding, conflicts of interest, and "
    "corrections policy are public in WHO.md.", styles["GYBody"]))

en.append(Paragraph("What we are not asking today", styles["GYH2"]))
en.append(Paragraph(
    "No money is requested and no agreement is final. We are here to listen, understand local "
    "conditions and priorities, and consider partnership only under a written, consented community "
    "agreement (see PARTNERSHIPS.md and CONSENT.md).", styles["GYNote"]))

en.append(Spacer(1, 8))
en.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceAfter=8))
en.append(Paragraph("Contact &amp; public record", styles["GYH2"]))
en.append(contact_table([
    ["Website", "www.groundyield.org"],
    ["Email", "team@groundyield.org  (Portuguese welcome)"],
    ["GitHub", "github.com/groundyield/website  (all documents, data, and source code)"],
    ["X", "@GroundYield"],
]))
en.append(Spacer(1, 10))
en.append(Paragraph(
    "This page is a field summary only. The full plan, charter, unit design, economics, data "
    "standards, consent policy and accountability page are public on the GitHub repository above. "
    "Printed 27 July 2026 &mdash; check the website for the current version.",
    styles["GYFoot"]))

# ---------------------------------------------------------------- PT PAGE
pt = []
pt += header("GroundYield", "Piloto aberto de agricultura modular &middot; Vilanculos, Prov&iacute;ncia de Inhambane, Mo&ccedil;ambique")

pt.append(Paragraph("O que &eacute;", styles["GYH2"]))
pt.append(Paragraph(
    "Um piloto transparente de unidades agr&iacute;colas modulares para pequenos produtores: irriga&ccedil;&atilde;o "
    "solar, sementes melhoradas e fertilizante em microdose, aconselhamento agron&oacute;mico por telefone, "
    "armazenamento herm&eacute;tico, e m&oacute;dulos opcionais de aves/cabras. Todos os custos, produ&ccedil;&otilde;es, "
    "rendimentos e falhas s&atilde;o publicados abertamente &mdash; o modelo foi desenhado para ser copiado, n&atilde;o apropriado.",
    styles["GYBody"]))

pt.append(Paragraph("Compromissos da &Eacute;poca 1", styles["GYH2"]))
pt.append(bullets([
    "30&ndash;60 unidades modulares na zona de Vilanculos",
    "Meta de aumento de 80&ndash;100%+ na produ&ccedil;&atilde;o de culturas de base &mdash; medida face a uma "
    "<b>linha de base local</b>, n&atilde;o m&eacute;dias nacionais",
    "Aumento do rendimento familiar via culturas de rendimento e aves",
    "Publica&ccedil;&atilde;o de custos, produ&ccedil;&otilde;es, rendimentos e falhas em tempo real",
]))

pt.append(Paragraph("Custo planeado (Ano 0, por unidade)", styles["GYH2"]))
pt.append(Paragraph(
    "&#126;1.270&ndash;2.985 USD &mdash; uma faixa de planeamento, n&atilde;o um or&ccedil;amento levantado nem uma "
    "oferta de pagamento. Lista completa de materiais: UNIT.md no reposit&oacute;rio do projeto.",
    styles["GYBody"]))

pt.append(Paragraph("Quem &eacute; respons&aacute;vel", styles["GYH2"]))
pt.append(Paragraph(
    "<b>Jacques Theron</b> &mdash; fundador / operador. O GroundYield &eacute; autofinanciado; ainda n&atilde;o "
    "existe entidade jur&iacute;dica registada, dito claramente de prop&oacute;sito. Financiamento, conflitos de "
    "interesse e pol&iacute;tica de corre&ccedil;&otilde;es s&atilde;o p&uacute;blicos em WHO.md.",
    styles["GYBody"]))

pt.append(Paragraph("O que n&atilde;o pedimos hoje", styles["GYH2"]))
pt.append(Paragraph(
    "N&atilde;o pedimos dinheiro e nenhum acordo &eacute; final. Estamos aqui para ouvir, compreender as "
    "condi&ccedil;&otilde;es e prioridades locais, e considerar parceria apenas sob um acordo comunit&aacute;rio "
    "escrito e consentido (ver PARTNERSHIPS.md e CONSENT.md).",
    styles["GYNote"]))

pt.append(Spacer(1, 8))
pt.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceAfter=8))
pt.append(Paragraph("Contacto e registo p&uacute;blico", styles["GYH2"]))
pt.append(contact_table([
    ["Site", "www.groundyield.org"],
    ["Email", "team@groundyield.org  (português bem-vindo)"],
    ["GitHub", "github.com/groundyield/website  (todos os documentos e dados)"],
    ["X", "@GroundYield"],
]))
pt.append(Spacer(1, 10))
pt.append(Paragraph(
    "Esta p&aacute;gina &eacute; apenas um resumo de terreno. O plano completo, carta de compromissos, desenho "
    "da unidade, economia, normas de dados, pol&iacute;tica de consentimento e p&aacute;gina de responsabiliza&ccedil;&atilde;o "
    "est&atilde;o p&uacute;blicos no reposit&oacute;rio GitHub acima. Impresso em 27 de julho de 2026 &mdash; "
    "verifique o site para a vers&atilde;o atual.",
    styles["GYFoot"]))

doc = SimpleDocTemplate(
    "/sessions/eager-confident-euler/mnt/outputs/groundyield/GroundYield_Field_OnePager_EN_PT.pdf",
    pagesize=A4,
    topMargin=18*mm, bottomMargin=16*mm, leftMargin=20*mm, rightMargin=20*mm,
    title="GroundYield Field One-Pager",
    author="GroundYield",
)

from reportlab.platypus import PageBreak
story = en + [PageBreak()] + pt
doc.build(story)
print("built")
