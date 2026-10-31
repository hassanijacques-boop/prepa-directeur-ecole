#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere 4 cartes mentales + 1 fiche de poche (A4, recopiables a la main) puis le PDF."""

import pathlib, asyncio

D = pathlib.Path("/workspace/prepa-directeur")

# (id_couleur, titre_branche, [mots_cles])
CARTES = [
    {
        "num": "1",
        "centre": "L'ENTRETIEN<br>PRÉLIMINAIRE<br><span>avec l'IEN</span>",
        "sous_titre": "Ce qui se joue, et comment s'y tenir",
        "branches": [
            ("bleu", "QUI · OÙ · COMBIEN", [
                "l'IEN, <b>seul</b>", "son bureau, tête-à-tête",
                "<b>20 à 40 min</b>", "une conversation, pas une épreuve"]),
            ("rouge", "CE QUI SE JOUE", [
                "un <b>AVIS</b> : favorable ou non", "pas un classement",
                "sans avis favorable → <b>pas de candidature</b>",
                "→ c'est une <b>porte</b>, pas une compétition"]),
            ("vert", "CE QU'IL CHERCHE", [
                "sait-il le <b>métier</b> ?", "est-il <b>fiable</b> ?",
                "sera-t-il <b>accepté par l'équipe</b> ?", "est-il <b>lucide</b> sur lui ?"]),
            ("or", "LA POSTURE", [
                "<b>calme</b> · <b>lent</b> · <b>concret</b>",
                "une idée par réponse", "des <b>exemples</b>, pas des adjectifs",
                "des <b>silences</b> = la maîtrise"]),
            ("violet", "CE QUI FAIT PENCHER", [
                "des <b>chiffres</b> sur mon école", "une <b>situation vécue</b> + ce que j'ai fait",
                "une <b>limite nommée</b> calmement", "<b>fonctionnelle ≠ hiérarchique</b>",
                "des questions sur le <b>métier</b>"]),
            ("gris", "LES PIÈGES", [
                "❌ critiquer mon école / mon directeur",
                "❌ le <b>vague</b> : « fédérer », « impulser »",
                "❌ parler du <b>poste</b> avant du métier",
                "❌ « aucune limite »"]),
        ],
    },
    {
        "num": "2",
        "centre": "MA<br>PRÉSENTATION<br><span>le fil, en 3 minutes</span>",
        "sous_titre": "Ce que je dis, dans l'ordre — et où je m'arrête",
        "branches": [
            ("bleu", "1. L'OUVERTURE", [
                "professeur des écoles <b>depuis 2016</b>",
                "Éducation nationale <b>depuis 2001</b>",
                "commencé maître à <b>Koungou</b>",
                "→ <b>24 ans</b> dans l'institution", "<i class='pz'>— pause</i>"]),
            ("vert", "2. LE FIL", [
                "<b>licence de psychologie</b>",
                "<b>certification français langue seconde</b>",
                "<b>6 ans en SEGPA</b> (M'Tsamboro)",
                "→ « les élèves qui ont le plus de mal »", "<i class='pz'>— pause</i>"]),
            ("or", "3. AUJOURD'HUI", [
                "<b>CM1-CM2</b> à La Rose, Bandraboua",
                "école en <b>REP+</b>",
                "<b>référent harcèlement</b>",
                "label <b>pHARe niveau 1</b>", "<i class='pz'>— pause</i>"]),
            ("violet", "4. LA RAISON", [
                "« certains sujets n'avancent que si <b>quelqu'un les porte</b> »",
                "le suivi des <b>AESH</b>", "la relation avec les <b>familles</b>",
                "le <b>projet d'école</b>", "<i class='pz'>— pause</i>"]),
            ("rouge", "5. L'HONNÊTETÉ", [
                "je ne connais pas le métier de <b>directeur</b>",
                "je connais celui d'<b>enseignant</b>",
                "« le reste, c'est ce que je viens <b>apprendre</b> »",
                "« prêt à être <b>évalué</b> là-dessus »"]),
            ("gris", "6. LA SORTIE", [
                "« je suis à votre <b>disposition</b> »",
                "une <b>offre</b>, pas une conclusion",
                "→ j'ouvre la conversation",
                "→ je ne la ferme pas"]),
        ],
    },
    {
        "num": "3",
        "centre": "LE MÉTIER<br>ET LE CADRE<br><span>ce que je dois savoir dire</span>",
        "sous_titre": "La loi Rilhac, les missions, et ce qui engage ma responsabilité",
        "branches": [
            ("rouge", "LA FONCTION", [
                "<b>professeur des écoles</b> chargé de la direction",
                "autorité <b>FONCTIONNELLE</b>",
                "<b>PAS</b> d'autorité <b>hiérarchique</b>",
                "<b>loi Rilhac</b> (21 déc. 2021)",
                "<b>décret 2023-777</b>"]),
            ("bleu", "PILOTER", [
                "<b>projet d'école</b> (3 ans, validé par l'IEN)",
                "animer le <b>conseil des maîtres</b>",
                "préparer le <b>conseil d'école</b>",
                "→ je <b>anime</b>, je n'écris pas seul"]),
            ("vert", "LES ÉLÈVES À BESOINS", [
                "<b>équipe éducative</b> = on décide ensemble",
                "<b>PPS</b> (handicap, MDPH)", "<b>PAP</b> · <b>PPRE</b>",
                "<b>AESH</b> : suivi et emploi du temps",
                "→ je <b>réunis</b> et je <b>formalise</b>"]),
            ("or", "LES MOYENS", [
                "<b>coopérative</b> = association (OCCE)",
                "<b>compte bancaire séparé</b>",
                "<b>budget voté en conseil d'école</b>",
                "→ <b>jamais</b> pour le fonctionnement de l'école"]),
            ("violet", "LA SÉCURITÉ", [
                "<b>registre de sécurité</b>",
                "<b>2 exercices d'évacuation / an</b>",
                "<b>PPMS</b> (mise en sûreté)",
                "surveiller les <b>temps non couverts</b>"]),
            ("gris", "ORGANISER", [
                "répartition des classes", "plannings et services",
                "absences et <b>remplacements</b>",
                "liens avec la <b>mairie</b> et les <b>familles</b>"]),
        ],
    },
    {
        "num": "4",
        "centre": "LES<br>QUESTIONS<br><span>ce qu'on me demande</span>",
        "sous_titre": "Ce qu'il me posera, ce que je dois poser, et ce qu'il ne faut jamais dire",
        "branches": [
            ("bleu", "CE QU'IL ME POSERA", [
                "« Racontez-moi votre <b>parcours</b> »",
                "« <b>Pourquoi</b> directeur ? »",
                "« Qu'est-ce qu'un <b>directeur d'école</b> ? »",
                "« Une situation <b>difficile</b> vécue ? »",
                "« Vos <b>limites</b> ? »"]),
            ("rouge", "LA QUESTION PIÈGE", [
                "« Quel regard sur votre <b>école actuelle</b> ? »",
                "→ parler des <b>problèmes</b>",
                "→ <b>jamais</b> des personnes",
                "→ ne pas critiquer mon directeur"]),
            ("vert", "CE QUE JE DOIS POSER", [
                "les <b>difficultés</b> des directeurs débutants",
                "comment <b>vous accompagnez</b> un débutant",
                "votre regard sur les <b>AESH</b>",
                "→ jamais « non » à cette question"]),
            ("or", "NE JAMAIS DIRE", [
                "❌ « pour <b>progresser</b> »",
                "❌ « je <b>m'ennuie</b> dans ma classe »",
                "❌ « pour avoir de l'<b>autorité</b> »",
                "❌ « parce que <b>personne ne veut</b> le faire »",
                "❌ « pour la <b>prime</b> »"]),
            ("violet", "SI JE NE SAIS PAS", [
                "« Je ne sais pas,",
                "mais voilà comment je <b>chercherais</b>. »",
                "→ un inspecteur préfère <b>ça</b>",
                "→ à une réponse <b>inventée</b>"]),
            ("gris", "LES 3 PREMIERS MOIS", [
                "<b>écouter</b> avant d'agir",
                "entretiens <b>individuels</b>",
                "un conseil des maîtres <b>sans ordre du jour lourd</b>",
                "stabiliser : <b>sécurité · plannings · familles</b>"]),
        ],
    },
]

COUL = {"bleu": "#2563eb", "rouge": "#c0392b", "vert": "#1a7a4a",
        "or": "#b8860b", "violet": "#7c3aed", "gris": "#5b6779"}


def carte_html(c):
    br = c["branches"]
    gauche, droite = br[:3], br[3:]

    def bloc(b, sens):
        coul, titre, mots = b
        lis = "".join(f"<li>{m}</li>" for m in mots)
        return f"""<div class="br {sens}" style="--c:{COUL[coul]}">
          <div class="bt">{titre}</div><ul>{lis}</ul></div>"""

    return f"""
<div class="page">
  <div class="entete">
    <div class="num">{c['num']}</div>
    <div><h2>{c['sous_titre']}</h2>
    <div class="leg">Carte mentale {c['num']} sur 4 — à recopier à la main</div></div>
  </div>
  <div class="map">
    <div class="col">{''.join(bloc(b,'g') for b in gauche)}</div>
    <div class="centre"><div class="noyau">{c['centre']}</div></div>
    <div class="col">{''.join(bloc(b,'d') for b in droite)}</div>
  </div>
  <div class="pied">Recopie-la en 5 minutes : le noyau au centre, les 6 branches autour, les mots-clés seulement.</div>
</div>"""


POCHE = """
<div class="page poche">
  <div class="entete">
    <div class="num">✓</div>
    <div><h2>La fiche de poche — à relire dans la salle d'attente</h2>
    <div class="leg">Une seule feuille. Rien d'autre le matin de l'entretien.</div></div>
  </div>

  <div class="pk">
    <div class="pk-t">1. Mon ouverture — 1 minute</div>
    <p>Professeur des écoles <b>depuis 2016</b>, Éducation nationale <b>depuis 2001</b>.
    Licence de <b>psychologie</b>, certification <b>français langue seconde</b>,
    <b>6 ans en SEGPA</b>. Aujourd'hui <b>CM1-CM2 à La Rose</b>, Bandraboua, REP+.
    <b>Référent harcèlement</b>, label pHARe niveau 1.</p>
  </div>

  <div class="pk">
    <div class="pk-t">2. Ma raison — en une phrase</div>
    <p>« Dans une école, certains sujets n'avancent que si <b>quelqu'un les porte</b> :
    le suivi des <b>AESH</b>, la relation avec les <b>familles</b>, le <b>projet d'école</b>.
    Je veux être celui qui porte. »</p>
  </div>

  <div class="pk">
    <div class="pk-t">3. Mon honnêteté — la phrase à ne pas oublier</div>
    <p>« Je ne connais pas le métier de directeur. Je connais celui d'enseignant.
    Le reste, <b>c'est ce que je viens apprendre</b> — et je suis prêt à être évalué là-dessus. »</p>
  </div>

  <div class="pk">
    <div class="pk-t">4. Mes 3 chiffres sur mon école <span style="font-weight:400">(à remplir)</span></div>
    <p class="fill">Nombre d'élèves : ____________ &nbsp;·&nbsp; Nombre d'AESH : ____________ &nbsp;·&nbsp;
    Élèves à besoins particuliers : ____________</p>
  </div>

  <div class="pk">
    <div class="pk-t">5. Mes 3 situations vécues <span style="font-weight:400">(à remplir — 5 mots chacune)</span></div>
    <p class="fill">1. ______________________________________________<br>
    2. ______________________________________________<br>
    3. ______________________________________________</p>
  </div>

  <div class="pk">
    <div class="pk-t">6. Mes 3 questions à lui poser</div>
    <p>1. Les difficultés les plus fréquentes des <b>directeurs débutants</b> ?<br>
    2. Comment <b>accompagnez-vous</b> un directeur qui prend sa première fonction ?<br>
    3. Votre regard sur le suivi des <b>AESH / élèves à besoins particuliers</b> ?</p>
  </div>

  <div class="pk rouge-fond">
    <div class="pk-t">7. Les 3 interdits</div>
    <p>❌ Critiquer mon école ou mon directeur &nbsp;·&nbsp;
    ❌ Le vague sans exemple &nbsp;·&nbsp;
    ❌ « Pour progresser »</p>
  </div>

  <div class="pk vert-fond">
    <div class="pk-t">8. Si je ne sais pas</div>
    <p>« <b>Je ne sais pas</b>, mais voilà comment je chercherais. »</p>
  </div>
</div>
"""

CSS = """
@page { size: A4 portrait; margin: 11mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1c2331; margin: 0; }
.page { page-break-after: always; height: 274mm; display: flex; flex-direction: column; }
.page:last-child { page-break-after: auto; }
.entete { display: flex; gap: 12px; align-items: center; border-bottom: 3px solid #12294d;
  padding-bottom: 8px; margin-bottom: 12px; }
.num { flex: 0 0 42px; height: 42px; border-radius: 50%; background: #12294d; color: #fff;
  font-weight: 800; font-size: 1.25rem; display: flex; align-items: center; justify-content: center; }
.entete h2 { margin: 0; font-size: 1.02rem; color: #12294d; line-height: 1.25; }
.leg { font-size: .7rem; color: #5b6779; margin-top: 2px; letter-spacing: .3px; }

.map { flex: 1; display: grid; grid-template-columns: 1fr 0.86fr 1fr; gap: 14px; align-items: stretch; }
.col { display: flex; flex-direction: column; justify-content: space-evenly; gap: 10px; height: 100%; }

.br { border: 1px solid #e2e8f0; border-radius: 10px; padding: 11px 13px 11px 15px;
  background: #fbfcfe; position: relative; }
.br.g { border-left: 5px solid var(--c); }
.br.d { border-right: 5px solid var(--c); }
.br::after { content: ""; position: absolute; top: 50%; width: 12px; height: 1.5px;
  background: #cbd5e1; }
.br.g::after { right: -13px; }
.br.d::after { left: -13px; }
.bt { font-size: .74rem; font-weight: 800; letter-spacing: .7px; color: var(--c);
  text-transform: uppercase; margin-bottom: 4px; }
.br ul { margin: 0; padding-left: 14px; font-size: .78rem; line-height: 1.55; }
.br li { margin-bottom: 2px; }
.br li b { color: #12294d; }
.br li .pz { font-style: normal; font-weight: 700; font-size: .66rem;
  letter-spacing: .8px; text-transform: uppercase; color: #b8860b; }

.centre { display: flex; align-items: center; justify-content: center; }
.noyau { background: #12294d; color: #fff; border-radius: 18px; padding: 26px 16px;
  text-align: center; font-weight: 800; font-size: 1.02rem; line-height: 1.3;
  letter-spacing: .5px; box-shadow: 0 3px 14px rgba(18,41,77,.28); width: 100%; }
.noyau span { display: block; font-size: .68rem; font-weight: 600; color: #93c5fd;
  margin-top: 6px; letter-spacing: 0; }

.pied { font-size: .66rem; color: #5b6779; text-align: center; margin-top: 8px;
  border-top: 1px dashed #cbd5e1; padding-top: 6px; }

/* ── fiche de poche ── */
.poche .pk { border: 1px solid #e2e8f0; border-left: 5px solid #2563eb; border-radius: 10px;
  padding: 14px 18px; margin-bottom: 12px; background: #fbfcfe; }
.poche .pk-t { font-size: .8rem; font-weight: 800; letter-spacing: .6px; color: #2563eb;
  text-transform: uppercase; margin-bottom: 3px; }
.poche .pk p { margin: 0; font-size: .95rem; line-height: 1.62; }
.poche .pk p.fill { color: #5b6779; letter-spacing: .5px; }
.poche .rouge-fond { border-left-color: #c0392b; background: #fef2f2; }
.poche .rouge-fond .pk-t { color: #c0392b; }
.poche .vert-fond { border-left-color: #1a7a4a; background: #f0fdf4; }
.poche .vert-fond .pk-t { color: #1a7a4a; }
"""

html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Cartes mentales — entretien préliminaire</title>
<style>{CSS}</style></head><body>
{''.join(carte_html(c) for c in CARTES)}
{POCHE}
</body></html>"""

(D / "cartes_mentales.html").write_text(html, encoding="utf-8")
print(f"  ✅ cartes_mentales.html — {len(html)//1024} Ko")


async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        p = await b.new_page()
        await p.goto(f"file://{D}/cartes_mentales.html", wait_until="load")
        await p.wait_for_timeout(900)
        await p.pdf(path=str(D / "CARTES_MENTALES_ENTRETIEN_IEN.pdf"),
                    format="A4", print_background=True)
        # captures pour verification
        for i, nom in ((0, "c1"), (1, "c2"), (2, "c3"), (3, "c4"), (4, "poche")):
            el = await p.query_selector_all(".page")
            if i < len(el):
                await el[i].screenshot(path=f"/tmp/cm_{nom}.png")
        await b.close()

asyncio.run(pdf())
import fitz
d = fitz.open(D / "CARTES_MENTALES_ENTRETIEN_IEN.pdf")
print(f"  ✅ CARTES_MENTALES_ENTRETIEN_IEN.pdf — {d.page_count} pages — "
      f"{(D / 'CARTES_MENTALES_ENTRETIEN_IEN.pdf').stat().st_size//1024} Ko")
