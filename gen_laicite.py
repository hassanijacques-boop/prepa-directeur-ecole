#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Briefing LAÏCITÉ ET NEUTRALITÉ pour l'entretien — les 3 points + cas pratiques."""

import pathlib, asyncio

D = pathlib.Path("/workspace/prepa-directeur")

PRINCIPES = [
    ("bleu", "1. LA NEUTRALITÉ",
     "L'État et ses agents ne prennent parti pour aucune croyance, aucune opinion.",
     "L'enseignant ne manifeste pas ses convictions religieuses, politiques ou philosophiques.",
     "« L'école publique est neutre : elle n'annonce aucune vérité, elle apprend à en chercher une. »"),
    ("vert", "2. LA LIBERTÉ DE CONSCIENCE",
     "Chacun est libre de croire ou de ne pas croire. L'école ne force aucune adhésion.",
     "Un élève ne peut pas être noté, jugé ou écarté selon sa religion — ni selon son absence de religion.",
     "« Mon rôle n'est pas de dire ce qu'il faut croire, mais de garantir que chacun puisse apprendre sans renier ce qu'il est. »"),
    ("or", "3. L'ÉGALITÉ",
     "Tous les élèves sont traités de la même façon, sans distinction d'origine ni de religion.",
     "Aucun traitement de faveur, aucun traitement défavorable.",
     "« La même règle pour tous, appliquée de la même façon à tous. »"),
]

TROIS_POINTS = [
    ("bleu", "① LA NEUTRALITÉ DES OPINIONS",
     "Ce que je montre, ce que je dis",
     ["Je ne portais pas de signe d'appartenance religieuse, politique ou syndicale.",
      "Je n'affiche pas mes convictions : ni dans mes mots, ni sur mes vêtements, ni sur mes affaires.",
      "Je ne réponds pas « et vous, qu'est-ce que vous en pensez ? » quand un élève m'interroge sur mes croyances.",
      "Je peux dire : « Ma conviction personnelle ne compte pas ici. Ce qui compte, c'est ce que tu apprends. »"],
     "« Mes opinions m'appartiennent et restent à la porte de la classe. »"),
    ("vert", "② LA NEUTRALITÉ DE L'ENSEIGNEMENT",
     "Ce que j'enseigne, et comment",
     ["Le contenu est celui des programmes : il est <b>laïque, objectif et exigeant</b>.",
      "<b>Aucun prosélytisme</b> : je ne cherche à convaincre personne d'adhérer à quoi que ce soit.",
      "Le <b>fait religieux</b> s'enseigne comme un fait : en histoire, en français, en arts — <b>jamais comme une vérité</b>.",
      "Je développe l'<b>esprit critique</b> : apprendre à douter, vérifier, argumenter."],
     "« J'enseigne des savoirs, pas des croyances. Et le fait religieux s'explique, il ne se prêche pas. »"),
    ("or", "③ LA NEUTRALITÉ DU COMPORTEMENT",
     "Ce que je fais, dans les faits",
     ["Je traite <b>tous les élèves de la même façon</b> : ni faveur, ni sévérité particulière.",
      "Je ne fais <b>aucune remarque</b> sur la religion supposée d'un élève ou de sa famille.",
      "Je <b>protège</b> un élève moqué pour ses croyances — ou pour son absence de croyance.",
      "Je <b>ne confonds pas</b> laïcité et hostilité au religieux : un élève croyant n'est pas un problème."],
     "« Le risque, ce n'est pas le croyant : c'est le traitement inégal. C'est ça que je surveille. »"),
]

QUI = [
    ("Enseignants", "Agents publics de l'État", "Neutralité <b>totale</b> : aucune manifestation de convictions", "✅ Oui", "Statut général de la fonction publique + déontologie"),
    ("Le directeur", "Agent public + responsable de l'école", "Neutralité <b>+ garantie</b> : il fait respecter la laïcité dans toute l'école", "✅ Oui, renforcée", "Loi Rilhac + code de l'éducation"),
    ("Les élèves", "Usagers du service public", "Loi de 2004 : <b>signes religieux ostensibles interdits</b> à l'école publique", "⚠️ Différent", "Loi du 15 mars 2004"),
    ("Les AESH", "Agents publics (contractuels de droit public)", "Neutralité : <b>même obligation que les enseignants</b>", "✅ Oui", "Statut + contrat"),
    ("Les parents", "Usagers", "Pas de neutralité — mais <b>pas de trouble</b> à l'ordre scolaire", "❌ Non, mais…", "Règlement intérieur"),
    ("Intervenants extérieurs", "Prestataires", "Neutralité <b>imposée par le contrat</b> et la charte signée", "✅ Oui", "Contrat + charte d'intervention"),
    ("Accompagnateurs bénévoles", "Bénévoles, pas agents", "Pas de neutralité — mais <b>discrétion</b> et pas de prosélytisme", "⚠️ Atténuée", "Charte des bénévoles"),
]

GESTES = [
    ("Rappeler le cadre", "À la rentrée, en conseil des maîtres, en réunion de parents. La <b>Charte de la laïcité</b> est affichée dans l'école.", "Le cadre se rappelle <b>avant</b> l'incident, pas pendant."),
    ("Recueillir les faits", "Qui, quoi, quand, où, devant qui. Des faits, <b>pas des impressions</b>. Par écrit.", "On ne tranche jamais sur un ouï-dire."),
    ("Dialoguer", "Avec l'élève seul, puis avec la famille. <b>Expliquer la règle</b>, écouter ce qui bloque.", "Un entretien calme désarme plus qu'une sanction."),
    ("Tracer et saisir", "Écrire l'incident, la réponse apportée. Saisir l'<b>IEN</b> si la situation dépasse l'école.", "Ce qui n'est pas écrit n'existe pas."),
    ("Faire vivre la laïcité", "Ne pas la réduire à des interdits : <b>EMC</b>, enseignement du fait religieux, débats réglés, conseils d'élèves.", "⚠️ C'est le point qui distingue un directeur d'un gardien."),
]

CAS = [
    ("Un élève de CM2 arrive avec un signe religieux ostensible",
     "Entretien <b>individuel et calme</b>. J'explique la règle (loi de 2004) et je propose un <b>temps pour l'enlever</b>, sans humiliation. J'appelle la famille le jour même. Je note. Si le refus persiste : <b>IEN</b>.",
     "Lui arracher ou l'exclure devant la classe"),
    ("Un parent demande que son enfant soit dispensé d'un cours (natation, éducation à la sexualité, sortie)",
     "Distinguer : la <b>dispense n'est pas un droit général</b>. On écoute la demande, on explique l'obligation scolaire, on cherche ce qui pose problème. Certaines dispenses existent (ex. éducation à la sexualité : <b>droit de retrait</b> prévu par les textes) — je vérifie avant de répondre.",
     "Répondre « oui » ou « non » sans vérifier le texte"),
    ("Une AESH porte un signe religieux",
     "Elle est <b>soumise à la neutralité</b> comme tout agent public. Le directeur lui en parle <b>en premier</b>, seul, avec respect. Si ça persiste, l'employeur (l'État) est saisi.",
     "Laisser passer en disant « ce n'est pas mon personnel »"),
    ("Un intervenant extérieur (sport, musique) fait du prosélytisme",
     "Je <b>mets fin à l'activité</b> immédiatement, je le signale à l'IEN et à l'organisme. La charte signée est opposable.",
     "Attendre la fin du cycle pour ne pas déranger"),
    ("Un enseignant donne son opinion politique en classe",
     "Je lui parle <b>en tête-à-tête</b>, sans le mettre en difficulté devant les élèves. S'il récidive, <b>IEN</b> — car je n'ai pas de pouvoir disciplinaire.",
     "Le reprendre devant la classe"),
    ("Une famille demande un menu confessionnel à la cantine",
     "La restauration relève de la <b>mairie</b>. Le directeur peut transmettre, pas décider. Posture : « je transmets à la commune, mais l'école ne gère pas les menus ».",
     "Promettre un menu que l'école ne peut pas fournir"),
    ("Un élève refuse de serrer la main d'une enseignante",
     "J'interroge avant d'accuser. Si c'est pour un motif religieux, j'explique la règle du <b>vivre ensemble</b> et je propose une alternative (salutation verbale). Je note.",
     "Y voir immédiatement une provocation"),
    ("Des élèves se moquent d'un camarade pour sa religion (ou son athéisme)",
     "C'est un <b>cas de harcèlement</b>. Protocole : protéger l'élève, ne pas le confronter à l'auteur, informer les familles, réunir l'équipe, surveiller les temps non couverts, tracer. <b>pHARe</b>.",
     "Traiter ça comme une simple dispute"),
]

ERREURS = [
    ("« La laïcité, c'est interdire les religions »", "La laïcité <b>garantit</b> la liberté de conscience. Elle interdit à l'État de prendre parti — pas aux élèves de croire."),
    ("« Ça ne me concerne pas, c'est le rôle de l'IEN »", "Le directeur est <b>le garant de la laïcité dans son école</b>. Ne rien faire, c'est déjà une décision."),
    ("« J'interdirais tout signe, pour être tranquille »", "Un directeur n'invente pas de règle. Il applique <b>le droit existant</b> — et il le connaît."),
    ("« La laïcité, c'est mon affaire personnelle »", "C'est une <b>obligation de fonction</b>, pas une opinion. Et elle s'applique à toi en premier."),
    ("« Avec ces familles, c'est impossible »", "C'est un <b>jugement sur les personnes</b>. Le jury l'entend comme un renoncement."),
]

TEXTES = [
    ("Constitution, article 1<sup>er</sup>", "« La France est une République indivisible, <b>laïque</b>, démocratique et sociale. Elle assure l'égalité devant la loi de tous les citoyens sans distinction d'origine, de race ou de religion. Elle <b>respecte toutes les croyances</b>. »"),
    ("Loi du 9 décembre 1905", "Séparation des Églises et de l'État. Article 1<sup>er</sup> : « La République assure la <b>liberté de conscience</b>. Elle garantit le libre exercice des cultes… »"),
    ("Loi du 15 mars 2004", "Dans les écoles, collèges et lycées publics, le port de <b>signes ou tenues manifestant ostensiblement une appartenance religieuse</b> est interdit aux élèves."),
    ("Code de l'éducation, art. L. 111-1", "L'école <b>respecte la personne et les convictions</b> de l'élève, et fait partager les valeurs de la République."),
    ("Loi n° 83-634 du 13 juillet 1983, art. 25", "Le fonctionnaire exerce ses fonctions avec <b>dignité, impartialité, intégrité et probité</b> — et est tenu à la <b>neutralité</b>."),
    ("Charte de la laïcité à l'école (2013)", "15 articles affichés dans toutes les écoles. C'est <b>l'outil de dialogue</b> avec les élèves et les familles."),
    ("Loi du 24 août 2021", "Conforte le respect des principes de la République : renforce la formation des personnels et le traitement des atteintes à la laïcité."),
]

CSS = """
@page { size: A4 portrait; margin: 13mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1c2331; margin: 0;
  font-size: 9.5pt; line-height: 1.48; }
.cov { border-bottom: 3px solid #12294d; padding-bottom: 10px; margin-bottom: 14px; }
.tagc { display: inline-block; background: #12294d; color: #fff; font-size: .64rem; font-weight: 800;
  letter-spacing: .9px; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; margin-bottom: 7px; }
h1 { font-size: 1.34rem; color: #12294d; margin: 0 0 3px; }
.sub { color: #5b6779; font-size: .8rem; margin: 0; }
h2 { font-size: .86rem; color: #12294d; letter-spacing: .5px; text-transform: uppercase;
  border-bottom: 2px solid #e2e8f0; padding-bottom: 5px; margin: 16px 0 9px; page-break-after: avoid; }
h3 { font-size: .78rem; letter-spacing: .6px; text-transform: uppercase; margin: 12px 0 6px;
  page-break-after: avoid; }

.alerte { background: #fef2f2; border: 1px solid #fecaca; border-left: 4px solid #c0392b;
  border-radius: 9px; padding: 11px 14px; font-size: .87rem; margin-bottom: 12px; color: #7f1d1d; }
.info { background: #eff6ff; border: 1px solid #bfdbfe; border-left: 4px solid #2563eb;
  border-radius: 9px; padding: 11px 14px; font-size: .87rem; margin: 11px 0; }

.g3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 11px 0; page-break-inside: avoid; }
.pc { border: 1px solid #e2e8f0; border-top: 4px solid var(--c); border-radius: 10px; padding: 9px 11px; background: #fff; }
.pc .t { font-size: .72rem; font-weight: 800; letter-spacing: .6px; color: var(--c); margin-bottom: 6px; }
.pc .a { font-size: .82rem; font-weight: 700; color: #12294d; margin-bottom: 5px; line-height: 1.4; }
.pc .b { font-size: .79rem; color: #475569; line-height: 1.5; margin-bottom: 6px; }
.pc .d { font-size: .74rem; font-style: italic; color: #1e3a8a; background: #f8fafc;
  border-radius: 6px; padding: 6px 8px; }

.pt { border: 1px solid #e2e8f0; border-left: 5px solid var(--c); border-radius: 11px;
  padding: 12px 15px; margin-bottom: 10px; page-break-inside: avoid; background: #fff; }
.pt .h { display: flex; align-items: baseline; gap: 9px; margin-bottom: 3px; }
.pt .h .t { font-size: .88rem; font-weight: 800; color: var(--c); }
.pt .h .s { font-size: .74rem; color: #5b6779; font-style: italic; }
.pt ul { margin: 6px 0 7px; padding-left: 17px; font-size: .84rem; }
.pt ul li { margin-bottom: 4px; }
.pt .ph { background: #fffbeb; border-left: 3px solid #b8860b; border-radius: 6px;
  padding: 7px 10px; font-size: .83rem; color: #422006; }

table { width: 100%; border-collapse: collapse; font-size: .78rem; margin: 8px 0; }
th { background: #12294d; color: #fff; padding: 6px 7px; text-align: left; font-size: .67rem;
  text-transform: uppercase; letter-spacing: .4px; }
td { border-bottom: 1px solid #e2e8f0; padding: 6px 7px; vertical-align: top; }
tr { page-break-inside: avoid; }
tbody tr:nth-child(even) td, table tr:nth-child(even) td { background: #fbfcfe; }

.gest { display: grid; gap: 7px; margin: 9px 0; }
.gest .g { display: flex; gap: 10px; background: #fbfcfe; border: 1px solid #e2e8f0;
  border-radius: 9px; padding: 8px 12px; font-size: .83rem; page-break-inside: avoid; }
.gest .g .n { flex: 0 0 20px; height: 20px; border-radius: 50%; background: #2563eb; color: #fff;
  font-weight: 800; font-size: .7rem; display: flex; align-items: center; justify-content: center; }
.gest .g .c b { color: #12294d; }
.gest .g .w { font-size: .77rem; color: #92400e; }

.erreur { background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 11px 14px; }
.erreur p { margin: 0 0 7px; font-size: .84rem; }
.erreur p:last-child { margin: 0; }
.erreur .x { color: #991b1b; font-weight: 800; }
.erreur .v { color: #166534; }

.txt { display: grid; gap: 7px; margin: 9px 0; }
.txt .i { background: #f8fafc; border-left: 3px solid #12294d; border-radius: 7px;
  padding: 8px 12px; font-size: .81rem; page-break-inside: avoid; }
.txt .i b.n { color: #12294d; display: block; margin-bottom: 2px; }

.fin { background: #12294d; color: #fff; border-radius: 12px; padding: 15px 18px; margin-top: 14px; }
.fin h3 { color: #fbbf24; margin: 0 0 8px; }
.fin p { margin: 0 0 7px; font-size: .85rem; line-height: 1.55; }
.fin b { color: #93c5fd; }
"""


COUL3 = {"bleu": "#2563eb", "vert": "#1a7a4a", "or": "#b8860b"}

principes_html = "".join(
    '<div class="pc" style="--c:%s"><div class="t">%s</div><div class="a">%s</div>'
    '<div class="b">%s</div><div class="d">%s</div></div>' % (COUL3[c], n, d, e, ph)
    for c, n, d, e, ph in PRINCIPES)

points_html = "".join(
    '<div class="pt" style="--c:%s"><div class="h"><span class="t">%s</span>'
    '<span class="s">%s</span></div><ul>%s</ul><div class="ph">\U0001F4AC %s</div></div>'
    % (COUL3[c], n, s, "".join("<li>%s</li>" % x for x in el), ph)
    for c, n, s, el, ph in TROIS_POINTS)

qui_html = "".join(
    '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td>'
    '<td><span style="font-size:.72rem;color:#5b6779">%s</span></td></tr>' % (a, b, c_, d, e)
    for a, b, c_, d, e in QUI)

gestes_html = "".join(
    '<div class="g"><div class="n">%d</div><div class="c"><b>%s</b> — %s'
    '<div class="w">\u2192 %s</div></div></div>' % (i + 1, a, b, c_)
    for i, (a, b, c_) in enumerate(GESTES))

cas_html = "".join(
    '<tr><td><b>%s</b></td><td>%s</td><td style="color:#991b1b">%s</td></tr>' % (a, b, c_)
    for a, b, c_ in CAS)

erreurs_html = "".join(
    '<p><span class="x">\u274C %s</span><br><span class="v">\u2705 %s</span></p>' % (a, b)
    for a, b in ERREURS)

textes_html = "".join(
    '<div class="i"><b class="n">%s</b>%s</div>' % (a, b) for a, b in TEXTES)

html = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Laïcité et neutralité — briefing entretien</title>
<style>__CSS__</style></head><body>

<div class="cov">
  <div class="tagc">Briefing entretien — inspecteur</div>
  <h1>Laïcité et neutralité de l'enseignant</h1>
  <p class="sub">Les 3 principes · les 3 points de la neutralité · qui est soumis à quoi · 8 cas pratiques · les textes</p>
</div>

<div class="alerte">
  <b>⚠️ Pourquoi l'inspecteur pose cette question — et pourquoi c'est piégeux</b><br>
  Le directeur est <b>le garant de la laïcité dans son école</b>. En posant cette question, il vérifie
  trois choses : que tu <b>connais le cadre</b>, que tu sais <b>le faire appliquer sans brutalité</b>,
  et que tu ne confonds pas <b>laïcité</b> avec <b>hostilité au religieux</b>.<br><br>
  <b>L'erreur classique :</b> répondre uniquement par des interdictions. Un directeur qui ne parle
  que d'interdiction n'a pas compris le métier.
</div>

<h2>Les 3 principes de la laïcité</h2>
<div class="g3">__PRINCIPES__</div>

<h2>⭐ Les 3 points de la NEUTRALITÉ de l'enseignant</h2>
<div class="info">
  <b>C'est très probablement ce que l'inspecteur a appelé « les 3 points ».</b>
  La neutralité ne se réduit pas aux signes : elle porte sur <b>ce que je dis</b>, <b>ce que j'enseigne</b>
  et <b>ce que je fais</b>. Si tes notes disaient plutôt « neutralité / liberté de conscience / égalité »,
  ce sont les 3 principes ci-dessus — deux triades justes, deux questions différentes.
</div>
__POINTS__

<h2>Qui est soumis à quoi — la question que peu de candidats savent traiter</h2>
<table>
  <tr><th style="width:19%">Qui</th><th style="width:20%">Statut</th><th>Obligation</th><th style="width:15%">Neutr.&nbsp;?</th><th style="width:22%">Fondement</th></tr>
  __QUI__
</table>

<h2>Ce que fait le directeur — 5 gestes concrets</h2>
<div class="gest">__GESTES__</div>

<h2>8 situations qu'il peut te faire traiter</h2>
<table>
  <tr><th style="width:26%">La situation</th><th>Ce que tu fais</th><th style="width:22%">Ce qu'il ne faut pas faire</th></tr>
  __CAS__
</table>

<h2>Les 5 erreurs qui feraient perdre l'avis</h2>
<div class="erreur">__ERREURS__</div>

<h2>Les 7 textes à savoir citer</h2>
<div class="txt">__TEXTES__</div>

<div class="fin">
  <h3>Les 3 phrases à retenir</h3>
  <p><b>1.</b> « La laïcité ne m'oblige pas à taire ce que je crois : elle m'oblige à ne pas m'en servir. »</p>
  <p><b>2.</b> « Le risque, ce n'est pas l'élève croyant : c'est le traitement inégal. C'est ça que je surveille. »</p>
  <p><b>3.</b> « Un directeur ne réduit pas la laïcité à des interdits : il en fait une règle du vivre ensemble — et ça s'apprend. »</p>
</div>

</body></html>"""

html = (html.replace("__CSS__", CSS).replace("__PRINCIPES__", principes_html)
            .replace("__POINTS__", points_html).replace("__QUI__", qui_html)
            .replace("__GESTES__", gestes_html).replace("__CAS__", cas_html)
            .replace("__ERREURS__", erreurs_html).replace("__TEXTES__", textes_html))

(D / "laicite.html").write_text(html, encoding="utf-8")
print(f"  \u2705 laicite.html — {len(html)//1024} Ko")


async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        p = await b.new_page()
        await p.goto(f"file://{D}/laicite.html", wait_until="load")
        await p.wait_for_timeout(700)
        await p.pdf(path=str(D / "LAICITE_NEUTRALITE_BRIEFING.pdf"), format="A4", print_background=True)
        await b.close()

asyncio.run(pdf())
import fitz
f = D / "LAICITE_NEUTRALITE_BRIEFING.pdf"
d = fitz.open(f)
print(f"  \u2705 {f.name} — {d.page_count} pages — {f.stat().st_size//1024} Ko")
for i in range(d.page_count):
    d[i].get_pixmap(dpi=105).save(f"/tmp/lc_p{i+1}.png")
