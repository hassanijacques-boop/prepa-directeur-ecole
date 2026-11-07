#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1) PDF « Procedure eleve en grande difficulte » (7 pages)
   2) Integration dans le site : section 23 + modeles copiables."""

import pathlib, asyncio, html as H

D = pathlib.Path("/workspace/prepa-directeur")
import sys
sys.path.insert(0, str(D))
from procedure_data import (ETAPES, CIRCUITS, DOCS, QUI, CAS_CM2, MODELES, SEMAINE, PAS)


# ════════════════════════════════════════════════════════════════
#  PARTIE PDF
# ════════════════════════════════════════════════════════════════
CSS_PDF = """
@page { size: A4 portrait; margin: 12mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1c2331; margin: 0;
  font-size: 9.4pt; line-height: 1.45; }
.pg { page-break-after: always; }
.pg:last-child { page-break-after: auto; }
.ent { border-bottom: 3px solid #12294d; padding-bottom: 8px; margin-bottom: 11px; }
.ent .t1 { font-size: 1.22rem; font-weight: 800; color: #12294d; }
.ent .t2 { font-size: .78rem; color: #5b6779; margin-top: 2px; }
h2 { font-size: .8rem; letter-spacing: .6px; text-transform: uppercase; color: #12294d;
  border-bottom: 2px solid #e2e8f0; padding-bottom: 4px; margin: 13px 0 7px;
  page-break-after: avoid; }
table { width: 100%; border-collapse: collapse; font-size: .78rem; margin: 7px 0; }
th { background: #12294d; color: #fff; padding: 5px 7px; text-align: left; font-size: .65rem;
  text-transform: uppercase; letter-spacing: .4px; }
td { border-bottom: 1px solid #e2e8f0; padding: 5px 7px; vertical-align: top; }
tr { page-break-inside: avoid; }

.et { display: flex; gap: 9px; border: 1px solid #e2e8f0; border-left: 4px solid #2563eb;
  border-radius: 8px; padding: 7px 11px; margin-bottom: 5px; page-break-inside: avoid;
  background: #fff; }
.et .n { flex: 0 0 20px; height: 20px; border-radius: 50%; background: #2563eb; color: #fff;
  font-weight: 800; font-size: .68rem; display: flex; align-items: center; justify-content: center; }
.et .c { flex: 1; font-size: .8rem; }
.et .c b.t { color: #12294d; font-size: .8rem; }
.et .c .d { color: #334155; }
.et .c .w { color: #92400e; font-size: .74rem; }
.et .q { flex: 0 0 88px; text-align: right; font-size: .68rem; color: #5b6779; font-weight: 700; }

.alerte { background: #fef2f2; border: 1px solid #fecaca; border-left: 4px solid #c0392b;
  border-radius: 8px; padding: 9px 12px; font-size: .84rem; margin: 9px 0; color: #7f1d1d; }
.info { background: #eff6ff; border: 1px solid #bfdbfe; border-left: 4px solid #2563eb;
  border-radius: 8px; padding: 9px 12px; font-size: .84rem; margin: 9px 0; }
.or { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #b8860b;
  border-radius: 8px; padding: 9px 12px; font-size: .84rem; margin: 9px 0; }

.mod { border: 1px solid #cbd5e1; border-radius: 8px; background: #fbfcfe; padding: 10px 13px;
  page-break-inside: auto;
  font-family: "DejaVu Sans Mono", monospace; font-size: 7.6pt; line-height: 1.45;
  white-space: pre-wrap; color: #1c2331; }
.mod-t { background: #12294d; color: #fff; border-radius: 8px 8px 0 0; padding: 6px 13px;
  font-size: .78rem; font-weight: 800; margin-top: 10px; }
.mod-t + .mod { border-radius: 0 0 8px 8px; border-top: none; margin-top: 0; }
.note { font-size: .74rem; color: #5b6779; margin-top: 5px; }
ul { margin: 5px 0; padding-left: 17px; font-size: .82rem; }
ul li { margin-bottom: 3px; }
"""


def page_entete(t1, t2):
    return '<div class="ent"><div class="t1">%s</div><div class="t2">%s</div></div>' % (t1, t2)


etapes_html = "".join(
    '<div class="et"><div class="n">%s</div><div class="c"><b class="t">%s</b> — '
    '<span class="d">%s</span><div class="w">→ %s</div></div>'
    '<div class="q">%s</div></div>' % (n, t, d, w, q)
    for n, t, d, q, w in ETAPES)

circuits_html = "".join(
    '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (a, b, c, d)
    for a, b, c, d in CIRCUITS)

docs_html = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (a, b, c)
                    for a, b, c in DOCS)

qui_html = "".join('<tr><td style="width:26%%"><b>%s</b></td><td>%s</td></tr>' % (a, b)
                   for a, b in QUI)

cas_html = "".join('<tr><td style="width:48%%">%s</td><td>%s</td></tr>' % (a, b)
                   for a, b in CAS_CM2)

semaine_html = "".join('<li>%s</li>' % x for x in SEMAINE)
pas_html = "".join('<tr><td style="width:38%%">❌ %s</td><td>%s</td></tr>' % (a, b) for a, b in PAS)

modeles_html = ""
for num, titre, texte in MODELES:
    modeles_html += ('<div class="pg">' + page_entete("MODÈLE %s" % num, titre) +
                     '<div class="mod-t">%s</div><div class="mod">%s</div>' % (titre, H.escape(texte)) +
                     '<p class="note">Les champs entre { } sont à remplacer. Ce modèle est un point de départ : '
                     'adapte-le au ton de ton école et à la situation réelle.</p></div>')

PAGE1 = page_entete("LA PROCÉDURE EN UNE PAGE",
                    "Un élève en grande difficulté persistante — de l'alerte à la MDPH") + """
<div class="alerte">
  <b>⚠️ Le mot « signalement » envoie dans le mauvais circuit.</b><br>
  « Signalement » = <b>protection de l'enfance</b> (danger). Ici, il s'agit d'une
  <b>saisine de la MDPH</b> et/ou d'un <b>dossier CDOEA</b>.
</div>
<h2>Les 8 étapes</h2>
""" + etapes_html + """
<div class="info">
  <b>⭐ Le point que presque personne ne connaît</b><br>
  L'<b>enseignant référent ne se saisit pas directement</b>. Il intervient <b>quand un dossier MDPH
  est en cours</b>, pour convoquer l'<b>ESS</b> et suivre le <b>PPS</b>.<br>
  → <b>Sans MDPH déposée par la famille, il n'y a pas d'enseignant référent à convoquer.</b>
</div>
"""

PAGE2 = page_entete("LES 3 CIRCUITS ET LES DOCUMENTS", "Ne pas se tromper de porte") + """
<h2>Les 3 « signalements » — lequel est le bon ?</h2>
<table><tr><th>Type</th><th>Situation</th><th>Circuit</th><th>Ici ?</th></tr>""" + circuits_html + """</table>
<h2>Les documents — qui sert à quoi</h2>
<table><tr><th style="width:18%">Document</th><th>Pour qui</th><th style="width:26%">Qui le décide</th></tr>""" + docs_html + """</table>
<h2>Qui fait quoi</h2>
<table>""" + qui_html + """</table>
<h2>❌ Ce que ce n'est pas</h2>
<table>""" + pas_html + """</table>
"""

PAGE3 = page_entete("LE CAS D'UN ÉLÈVE DE CM2 À NIVEAU CP", "Cinq ans de retard : il y a urgence") + """
<div class="or">
  <b>Un élève de CM2 qui lit au niveau CP, avec des difficultés depuis le CP, n'est pas
  « en difficulté » : c'est un élève qu'on n'a pas réussi à faire entrer dans la lecture.</b><br>
  Il entre au collège dans quelques mois. <b>Si rien n'est fait maintenant, le dossier n'existera pas.</b>
</div>
<h2>Trois hypothèses — trois destinations différentes</h2>
<table><tr><th style="width:48%">Hypothèse</th><th>Vers quoi ça mène</th></tr>""" + cas_html + """</table>
<div class="alerte">
  <b>⚠️ Deux dossiers EN PARALLÈLE, pas l'un après l'autre</b><br>
  1. <b>L'équipe éducative tout de suite</b> → PPRE, RASED, information MDPH.<br>
  2. <b>Le dossier CDOEA dès maintenant</b> : les dossiers de pré-orientation SEGPA se préparent
  <b>au premier trimestre</b> — et il est en CM2.
</div>
<h2>Les 5 gestes du directeur, cette semaine</h2>
<ul>""" + semaine_html + """</ul>
<div class="info">
  <b>💬 La phrase à dire au collègue</b><br>
  « Ce n'est pas un signalement. On réunit une équipe éducative, on documente, on aménage.
  Si on pense à un trouble, on informe les parents qu'ils peuvent déposer un dossier MDPH —
  avec notre GEVA-Sco. C'est la MDPH qui saisit ensuite l'enseignant référent.
  Et en parallèle, on prépare le dossier SEGPA, parce qu'il est en CM2. »
</div>
"""

PAGE_PROC = ("<div class=\"pg\">" + PAGE1 + "</div>"
             + "<div class=\"pg\">" + PAGE2 + "</div>"
             + "<div class=\"pg\">" + PAGE3 + "</div>")

html_pdf = """<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Procédure élève en grande difficulté</title><style>%s</style></head><body>
%s
%s
</body></html>""" % (CSS_PDF, PAGE_PROC, modeles_html)

(D / "procedure_pdf.html").write_text(html_pdf, encoding="utf-8")
print("  ✅ procedure_pdf.html — %d Ko" % (len(html_pdf) // 1024))


async def build_pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        p = await b.new_page()
        await p.goto("file://%s/procedure_pdf.html" % D, wait_until="load")
        await p.wait_for_timeout(700)
        await p.pdf(path=str(D / "PROCEDURE_ELEVE_EN_DIFFICULTE.pdf"),
                    format="A4", print_background=True)
        await b.close()

asyncio.run(build_pdf())
import fitz
f = D / "PROCEDURE_ELEVE_EN_DIFFICULTE.pdf"
d = fitz.open(f)
print("  ✅ %s — %d pages — %d Ko" % (f.name, d.page_count, f.stat().st_size // 1024))
for i in range(d.page_count):
    d[i].get_pixmap(dpi=100).save("/tmp/pr_p%d.png" % (i + 1))
