#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""18 declencheurs concrets pour « Pourquoi directeur ? » — a cocher, a comprendre, a raconter."""

import pathlib, asyncio

D = pathlib.Path("/workspace/prepa-directeur")

# (famille_couleur, famille_titre, [(situation, ce_que_ca_revele, la_phrase)])
FAMILLES = [
    ("bleu", "A · LE SUIVI QUI SE PERD", "Le domaine le plus fréquent en REP+. Presque tout le monde l'a vécu.", [
        ("<b>Les AESH et les emplois du temps.</b> Trois AESH se partageaient six élèves. Personne n'avait le tableau de qui accompagne qui, ni sur quels créneaux. Quand une AESH était absente, on l'apprenait le matin, devant l'élève.",
         "Personne ne pilotait. Ce n'est pas un manque de moyens : c'est un manque d'organisation.",
         "« J'ai vu qu'une AESH absente, on l'apprenait le matin — et l'élève restait sans aide. Il fallait quelqu'un pour tenir ce tableau. »"),
        ("<b>Le dossier oublié.</b> Un élève avait un PPS depuis deux ans. Personne ne savait plus quels aménagements étaient prévus, ni s'ils étaient seulement appliqués en classe.",
         "Un dossier rangé n'est pas un dossier appliqué. Il faut quelqu'un qui vérifie.",
         "« Un élève avait des aménagements décidés depuis deux ans. Personne ne savait s'ils étaient appliqués. Ça se vérifie, ça. »"),
        ("<b>L'élève qui sort du dispositif.</b> Un élève suivi en CP pour des difficultés de langage n'avait plus aucun suivi en CE1. Le passage s'était fait sans transmission.",
         "La continuité ne se fait pas toute seule : elle se décide et s'organise.",
         "« Un élève suivi en CP n'avait plus rien en CE1. Le dossier n'avait pas suivi. C'est ça qu'il faut organiser. »"),
        ("<b>Les PPRE jamais réévalués.</b> Des PPRE signés en début d'année, jamais rouverts ensuite. Les objectifs étaient les mêmes en juin qu'en septembre.",
         "Un document qui n'est pas relu ne sert à rien.",
         "« On signait des PPRE en septembre. Plus personne ne les rouvrait. Un PPRE qui n'est pas réévalué, c'est du papier. »"),
    ]),
    ("vert", "B · LES FAMILLES", "En REP+ à Mayotte, c'est le sujet le plus sensible — et le plus parlant pour un inspecteur.", [
        ("<b>La famille qui ne vient plus.</b> Une mère avait arrêté de venir aux réunions après une remarque mal formulée. Son fils a décroché en trois mois. Personne n'était allé la chercher.",
         "Une famille perdue ne revient pas seule. Il faut aller vers elle.",
         "« Une mère a arrêté de venir après une phrase maladroite. Son fils a décroché en trois mois. Personne n'est allé la chercher. »"),
        ("<b>Le conflit qui monte faute d'explication.</b> Un père s'est mis à crier devant l'école parce qu'il n'avait jamais compris pourquoi son fils redoublait. L'information n'avait été donnée qu'à l'écrit.",
         "Une décision non expliquée devient une injustice.",
         "« Un père a crié devant l'école : il n'avait jamais compris pourquoi son fils redoublait. On lui avait écrit, il n'avait pas pu lire. »"),
        ("<b>La langue.</b> Des familles ne lisaient pas le français. On leur envoyait des courriers qu'elles ne pouvaient pas lire. Personne n'avait pensé à une autre forme.",
         "Communiquer, ce n'est pas envoyer. C'est être compris.",
         "« On envoyait des courriers à des familles qui ne les lisaient pas. Personne ne s'était demandé comment elles allaient comprendre. »"),
        ("<b>La famille qui se sent jugée.</b> Une famille ne venait plus aux rendez-vous parce qu'elle avait l'impression qu'on parlait de son enfant uniquement pour le reprocher.",
         "Le rapport aux familles se construit, il ne se décrète pas.",
         "« Une famille ne venait plus : elle avait le sentiment qu'on ne la convoquait que pour se plaindre. Il fallait changer la façon de faire. »"),
    ]),
    ("violet", "C · LE COLLECTIF QUI NE SE PARLE PLUS", "Là, on voit que tu penses en directeur et pas seulement en enseignant.", [
        ("<b>Le conseil des maîtres vidé de son sens.</b> Le conseil des maîtres durait vingt minutes, on y réglait les plannings et les sorties. Le projet d'école n'y était jamais évoqué.",
         "Une instance existe ; encore faut-il qu'elle serve à quelque chose.",
         "« Le conseil des maîtres servait à faire les plannings. Le pédagogique n'y était jamais abordé. »"),
        ("<b>Deux classes qui font la même chose sans le savoir.</b> Deux enseignants du même cycle préparaient le même projet de sortie, chacun de son côté, en même temps.",
         "Sans coordination, l'énergie se dépense deux fois.",
         "« Deux collègues préparaient la même sortie chacun de son côté. Un directeur, ça se coordonne. »"),
        ("<b>La décision prise sans les intéressés.</b> Une répartition de classes avait été décidée sans consulter les enseignants. Elle a été abandonnée en deux semaines.",
         "Une décision sans les équipes ne tient pas. C'est aussi le risque à ne pas reproduire.",
         "« Une décision de répartition a été prise sans nous. Elle a tenu deux semaines. Une équipe ne se passe pas d'être associée. »"),
        ("<b>Le nouvel enseignant laissé seul.</b> Un collègue est arrivé en cours d'année. On lui a donné ses clés et sa classe. Au bout d'un mois, il a demandé sa mutation.",
         "Accueillir ne s'improvise pas — et un départ coûte cher aux élèves.",
         "« Un collègue est arrivé en cours d'année et a demandé sa mutation au bout d'un mois. Personne ne l'avait accompagné. »"),
    ]),
    ("rouge", "D · L'ÉVÉNEMENT QUI A TOUT RÉVÉLÉ", "Le plus fort. À n'utiliser que si c'est vrai, et sans en faire un drame.", [
        ("<b>Le harcèlement découvert trop tard.</b> Un élève était harcelé depuis des mois. On l'a su quand il a refusé de venir à l'école. Les signaux existaient : il ne mangeait plus, il restait seul, il changeait de chemin. Personne ne les avait reliés.",
         "En REP+, le harcèlement ne se voit pas dans les couloirs : il se voit dans les ruptures.",
         "« Un élève harcelé depuis des mois ; on l'a su quand il a refusé de venir. Les signaux étaient là, mais personne ne les avait reliés. »"),
        ("<b>L'incident qui révèle un trou d'organisation.</b> Un élève s'est blessé dans la cour. On a cherché la trousse de secours pendant dix minutes. Personne ne savait où elle était.",
         "Un directeur ne fait pas le cours : il fait en sorte que tout ne s'arrête pas au premier imprévu.",
         "« Un élève s'est blessé, on a cherché la trousse de secours dix minutes. C'est ce genre de chose qu'un directeur tient. »"),
        ("<b>L'alerte qui n'a pas circulé.</b> Une information importante sur un élève n'est jamais arrivée à l'enseignant concerné — elle s'était arrêtée sur un bureau.",
         "Le circulation de l'information est un travail, pas un hasard.",
         "« Une information sur un élève n'est jamais arrivée à son enseignant. Elle s'était arrêtée en route. Ça, c'est le métier de directeur. »"),
    ]),
    ("or", "E · LA CONTINUITÉ ENTRE LES NIVEAUX", "Très efficace en primaire : ça montre que tu vois l'école de la PS au CM2, pas ta seule classe.", [
        ("<b>Le passage GS-CP sans transmission.</b> Rien ne se transmettait entre la maternelle et le CP. Chaque enseignant redécouvrait ses élèves en septembre, en recommençant les évaluations.",
         "La continuité est le cœur du cycle, et personne ne la porte naturellement.",
         "« Rien ne se transmettait entre la GS et le CP. En septembre, on redécouvrait tout. La continuité, c'est un pilotage. »"),
        ("<b>Le projet d'école qui ne vit pas.</b> Un projet d'école voté il y a trois ans, et personne ne se souvenait d'un seul de ses axes.",
         "Un projet qu'on écrit et qu'on n'anime pas meurt la première année.",
         "« Un projet d'école, trois ans, et plus personne ne sait ce qu'il contient. Un projet doit être animé, sinon il meurt. »"),
        ("<b>Le CP qui n'a pas préparé le CE1.</b> Une classe avait des habitudes de travail que le CE1 ne reprenait pas. Les élèves perdaient deux mois à se réadapter.",
         "Le directeur est le seul qui voit toute la chaîne des niveaux.",
         "« Des habitudes de travail construites au CP n'étaient pas reprises au CE1. Les élèves perdaient deux mois. »"),
    ]),
    ("gris", "F · LES MOYENS ET LE MATÉRIEL", "Moins « noble », mais très crédible : c'est du réel, pas du discours.", [
        ("<b>La coopérative opaque.</b> La coopérative avait de l'argent, mais personne ne savait ce qu'elle finançait, ni selon quels critères. Les demandes n'obtenaient pas les mêmes réponses selon qui demandait.",
         "La transparence budgétaire, c'est un geste de directeur, pas une qualité personnelle.",
         "« La coopérative avait de l'argent, personne ne savait selon quels critères. C'est de la transparence, ça se construit. »"),
        ("<b>Le matériel qui n'arrive pas.</b> Deux classes attendaient des manuels depuis un an. Personne ne relançait, personne ne savait où en était la commande.",
         "Le suivi des commandes est ingrat, et nécessaire.",
         "« Deux classes attendaient des manuels depuis un an. Personne ne relançait. Ça, c'est du suivi. »"),
    ]),
]

FAUX = [
    "« J'ai vu que le directeur avait de l'autorité, je voudrais ça. » → ça parle de toi, pas des élèves.",
    "« Mon directeur ne faisait pas son travail, je ferais mieux. » → c'est une critique, pas une motivation.",
    "« J'aime bien organiser, gérer des plannings. » → c'est un goût, pas un déclencheur. Aucun exemple.",
    "« Pour que ma voix compte dans les décisions. » → vrai, mais ça se retourne contre toi : ça dit « je veux du pouvoir ».",
    "« Parce que c'est la suite logique de ma carrière. » → la carrière n'est pas une raison, l'élève en est une.",
    "« Je m'entends bien avec la mairie / j'ai des relations. » → ce n'est pas ce qu'il évalue, et ça sonne comme un réseau.",
]

CSS = """
@page { size: A4 portrait; margin: 12mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1c2331; margin: 0;
  font-size: 9.8pt; line-height: 1.5; }
h1 { font-size: 1.35rem; color: #12294d; margin: 0 0 3px; }
.sub { color: #5b6779; font-size: .81rem; margin: 0; }
.cover { border-bottom: 3px solid #12294d; padding-bottom: 10px; margin-bottom: 13px; }
.tagc { display: inline-block; background: #b8860b; color: #fff; font-size: .65rem; font-weight: 800;
  letter-spacing: .8px; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; margin-bottom: 7px; }

.test { background: #f0f7ff; border: 1px solid #bfdbfe; border-radius: 12px; padding: 13px 17px; margin: 13px 0; }
.test h3 { margin: 0 0 8px; font-size: .84rem; color: #2563eb; letter-spacing: .5px; text-transform: uppercase; }
.test ol { margin: 0; padding-left: 20px; font-size: .87rem; }
.test ol li { margin-bottom: 5px; }
.test ol li b { color: #12294d; }

.struct { background: #f8fafc; border-left: 4px solid #12294d; border-radius: 9px;
  padding: 11px 15px; margin: 13px 0; font-size: .87rem; }
.struct b { color: #12294d; }
.struct .box { margin-top: 7px; font-size: .85rem; color: #334155; line-height: 1.7; }

.fam { margin-top: 15px; }
.fam-h { display: flex; align-items: center; gap: 9px; margin-bottom: 3px; page-break-after: avoid; }
.fam-h .bar { flex: 0 0 5px; height: 26px; border-radius: 3px; background: var(--fc); }
.fam-h h2 { margin: 0; font-size: .95rem; color: var(--fc); letter-spacing: .3px; }
.fam-sub { font-size: .78rem; color: #5b6779; margin: 0 0 8px 14px; font-style: italic;
  page-break-after: avoid; }

.sit { border: 1px solid #e2e8f0; border-left: 4px solid var(--fc); border-radius: 10px;
  padding: 10px 13px; margin-bottom: 8px; background: #fff; page-break-inside: avoid; }
.sit-h { display: flex; gap: 9px; align-items: flex-start; margin-bottom: 5px; }
.case { flex: 0 0 auto; width: 15px; height: 15px; border: 2px solid var(--fc); border-radius: 3px; margin-top: 2px; }
.sit-h .tx { flex: 1; font-size: .87rem; line-height: 1.5; }
.rev { font-size: .8rem; color: #475569; font-style: italic; padding-left: 24px; margin-bottom: 5px; }
.dire { background: #fffbeb; border-left: 3px solid #b8860b; border-radius: 6px;
  padding: 6px 10px; margin-left: 24px; font-size: .84rem; color: #422006; }
.dire b { font-size: .66rem; letter-spacing: .6px; text-transform: uppercase; color: #92400e; display: block; margin-bottom: 2px; }

.faux { background: #fef2f2; border: 1px solid #fecaca; border-radius: 11px; padding: 13px 16px; margin-top: 15px; }
.faux h3 { margin: 0 0 8px; font-size: .84rem; color: #c0392b; letter-spacing: .5px; text-transform: uppercase; }
.faux ul { margin: 0; padding-left: 18px; font-size: .84rem; }
.faux li { margin-bottom: 5px; color: #7f1d1d; }

.choix { background: #12294d; color: #fff; border-radius: 13px; padding: 16px 20px; margin-top: 15px; }
.choix h3 { margin: 0 0 9px; font-size: .86rem; color: #fbbf24; letter-spacing: .6px; text-transform: uppercase; }
.choix p { margin: 0 0 8px; font-size: .86rem; line-height: 1.55; }
.choix .ligne { border-bottom: 1px solid rgba(255,255,255,.3); height: 26px; }
.choix .lab { font-size: .68rem; color: #93c5fd; letter-spacing: .5px; text-transform: uppercase; margin-top: 9px; }
"""


def bloc_famille(coul, titre, sub, sitis):
    items = []
    for txt, rev, dire in sitis:
        items.append(f"""<div class="sit">
      <div class="sit-h"><div class="case"></div><div class="tx">{txt}</div></div>
      <div class="rev">↳ {rev}</div>
      <div class="dire"><b>Ce que tu dirais</b>{dire}</div>
    </div>""")
    return f"""<div class="fam" style="--fc:{COUL[coul]}">
    <div class="fam-h"><div class="bar"></div><h2>{titre}</h2></div>
    <p class="fam-sub">{sub}</p>
    {''.join(items)}</div>"""


COUL = {"bleu": "#2563eb", "vert": "#1a7a4a", "violet": "#7c3aed",
        "rouge": "#c0392b", "or": "#b8860b", "gris": "#5b6779"}

CONSEILS = {
    "bleu": "Le domaine le plus fréquent en REP+. Presque tout le monde l'a vécu.",
    "vert": "En REP+ à Mayotte, c'est le sujet le plus sensible — et le plus parlant pour un inspecteur.",
    "violet": "Là, on voit que tu penses en directeur et pas seulement en enseignant.",
    "rouge": "Le plus fort. À n'utiliser que si c'est vrai, et sans en faire un drame.",
    "or": "Très efficace en primaire : ça montre que tu vois l'école de la PS au CM2, pas ta seule classe.",
    "gris": "Moins « noble », mais très crédible : c'est du réel, pas du discours.",
}

html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>18 déclencheurs concrets — pourquoi directeur</title>
<style>{CSS}</style></head><body>

<div class="cover">
  <div class="tagc">Carte 4 · question 2 — développée</div>
  <h1>« Pourquoi directeur ? » — 18 déclencheurs concrets</h1>
  <p class="sub">Coche ceux qui te parlent. Garde-en deux. Raconte-les avec tes mots.</p>
</div>

<div class="test">
  <h3>Le test en 3 questions — un bon déclencheur y répond trois fois « oui »</h3>
  <ol>
    <li><b>Est-ce que j'ai AGI</b>, ou seulement regardé ? <span style="color:#5b6779">Si tu n'as rien fait, ce n'est pas un déclencheur : c'est une opinion.</span></li>
    <li><b>Est-ce que ça concerne des ÉLÈVES ?</b> <span style="color:#5b6779">Pas des adultes, pas l'organisation pour l'organisation.</span></li>
    <li><b>Est-ce que je peux le raconter en 30 secondes</b>, avec un chiffre ou une date ? <span style="color:#5b6779">Si c'est trop long, c'est trop flou.</span></li>
  </ol>
</div>

<div class="struct">
  <b>La structure pour le raconter — 5 phrases, jamais plus</b>
  <div class="box">
    1. <b>J'ai vu</b> … <i>(la situation, en une phrase)</i><br>
    2. <b>Je m'attendais à</b> … <i>(ce qui aurait dû se passer)</i><br>
    3. <b>Mais</b> … <i>(ce qui n'allait pas)</i><br>
    4. <b>Alors j'ai</b> … <i>(ce que TOI tu as fait)</i><br>
    5. <b>Et j'en ai tiré</b> : c'est le rôle du directeur de faire ça pour toute l'école.
  </div>
</div>

{''.join(bloc_famille(c, t, CONSEILS[c], s) for c, t, _sub, s in FAMILLES)}

<div class="faux">
  <h3>❌ Les faux déclencheurs — ceux qui te feraient perdre</h3>
  <ul>{''.join(f'<li>{f}</li>' for f in FAUX)}</ul>
</div>

<div class="choix">
  <h3>Maintenant : choisis le tien</h3>
  <p>Relis tes cases cochées. <b>Garde celle qui remplit les trois conditions</b> : tu as agi · ça concerne des élèves · ça tient en 30 secondes.
  <b>Écris-la ici, à la main. C'est ce que tu diras lundi.</b></p>
  <div class="lab">1. J'ai vu…</div><div class="ligne"></div>
  <div class="lab">2. Je m'attendais à…</div><div class="ligne"></div>
  <div class="lab">3. Mais…</div><div class="ligne"></div>
  <div class="lab">4. Alors j'ai…</div><div class="ligne"></div>
  <div class="lab">5. Et j'en ai tiré…</div><div class="ligne"></div>
</div>

</body></html>"""

(D / "declencheurs.html").write_text(html, encoding="utf-8")
print(f"  ✅ declencheurs.html — {len(html)//1024} Ko")


async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        p = await b.new_page()
        await p.goto(f"file://{D}/declencheurs.html", wait_until="load")
        await p.wait_for_timeout(700)
        await p.pdf(path=str(D / "DECLENCHEURS_POURQUOI_DIRECTEUR.pdf"),
                    format="A4", print_background=True)
        await b.close()

asyncio.run(pdf())
import fitz
f = D / "DECLENCHEURS_POURQUOI_DIRECTEUR.pdf"
d = fitz.open(f)
print(f"  ✅ {f.name} — {d.page_count} pages — {f.stat().st_size//1024} Ko")
for i in range(d.page_count):
    d[i].get_pixmap(dpi=105).save(f"/tmp/dc_p{i+1}.png")
