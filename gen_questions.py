#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CARTE 4 developpee — les questions de l'inspecteur + elements de reponse."""

import pathlib, asyncio

D = pathlib.Path("/workspace/prepa-directeur")

# (num, question, ce_qu_il_teste, [elements], exemple, a_eviter)
QS = [
    ("1", "« Racontez-moi votre parcours. »",
     "La clarté. Il vérifie que tu sais résumer 24 ans en 2 minutes, et que ce résumé a un fil.",
     ["<b>Trois temps seulement :</b> l'ancrage → la spécialisation → aujourd'hui.",
      "<b>L'ancrage (2001-2015)</b> : maître à la maternelle de Koungou, puis les écoles de Koungou (Plage, Baobab, Trévani, Majicavo-Koropa).",
      "<b>La spécialisation (2015-2026)</b> : soutien spécialisé, unité pour élèves allophones, certification <b>français langue seconde</b> (2016), puis <b>six ans en SEGPA</b> à M'Tsamboro.",
      "<b>Aujourd'hui</b> : CM1-CM2 à La Rose, Bandraboua, en REP+, et <b>référent harcèlement</b>."],
     "Le fil à énoncer : <i>« Ce qui traverse tout ça, c'est les élèves qui ont le plus de mal. »</i>",
     "❌ Énumérer les écoles une par une. C'est un CV lu à voix haute, et il l'a déjà sous les yeux."),

    ("2", "« Pourquoi voulez-vous être directeur ? »",
     "La motivation réelle. C'est la question qui élimine le plus.",
     ["<b>Le déclencheur</b> : une situation précise que tu as vue dans ton école — un sujet qui n'avançait pas faute de quelqu'un pour le porter.",
      "<b>La conviction</b> : <i>« un directeur ne fait pas la classe aux autres — il crée les conditions pour que chacun puisse faire la sienne »</i>.",
      "<b>Le projet</b> : <b>deux ou trois priorités</b>, pas dix. Par exemple les familles, puis les élèves à besoins particuliers.",
      "Les trois, dans cet ordre. Si tu en oublies un, ça s'entend."],
     "Nomme <b>un</b> sujet réel : le suivi des AESH, la continuité entre cycles, la relation avec les familles.",
     "❌ « Pour progresser » · ❌ « je m'ennuie dans ma classe » · ❌ « pour avoir de l'autorité » · ❌ « parce que personne ne veut le faire »."),

    ("3", "« Qu'est-ce qu'un directeur d'école ? »",
     "Ton niveau de lecture du cadre. Attention : ce n'est pas un principal de collège.",
     ["<b>Un professeur des écoles chargé de la direction de l'école</b> — ce n'est pas un chef d'établissement.",
      "Il a une <b>autorité fonctionnelle</b> : organiser, coordonner, animer.",
      "Il n'a <b>pas d'autorité hiérarchique</b> sur ses collègues enseignants.",
      "Il est <b>garant du fonctionnement</b>, de la <b>sécurité</b> et de la <b>mise en œuvre du projet d'école</b>.",
      "Cadre : <b>loi Rilhac</b> (21 décembre 2021) et <b>décret 2023-777</b>."],
     "<i>« Je ne peux pas obliger un collègue. Je peux organiser, expliquer, et si ça bloque, alerter l'IEN. »</i>",
     "❌ « C'est le chef de l'école » · ❌ confondre avec principal ou proviseur."),

    ("4", "« Racontez-moi une situation difficile et comment vous l'avez gérée. »",
     "Ta fiabilité et ton sang-froid. Il veut du concret, pas une théorie.",
     ["<b>Structure en 4 temps :</b> la situation (2 phrases) → ce que j'ai fait → ce que ça a produit → ce que j'en ai appris.",
      "Choisis <b>une situation réellement vécue</b>, pas la plus impressionnante : la plus <b>vraie</b>.",
      "Dis <b>ce que TU as fait</b> — pas ce que l'équipe a fait, pas ce que le directeur aurait dû faire.",
      "Termine par <b>ce que tu en as tiré</b> : c'est ça qu'il écoute."],
     "<b>Trois pistes dans ton parcours :</b> un élève allophone que personne n'arrivait à inclure · une famille en conflit · un élève de SEGPA en rupture · une situation de harcèlement (tu es référent, c'est ton terrain).",
     "❌ « Je n'ai jamais eu de situation difficile. » Soit tu n'as pas vu, soit tu ne veux pas dire — les deux inquiètent."),

    ("5", "« Quelles sont vos limites pour ce métier ? »",
     "Ta lucidité. Un candidat qui ne voit aucune limite inquiète plus qu'il ne rassure.",
     ["<b>Nomme UNE limite réelle</b>, calmement, sans t'excuser.",
      "Ajoute aussitôt <b>ce que tu fais pour la combler</b> : la formation, le tutorat, l'observation d'un directeur en poste.",
      "Formule-le comme un <b>apprentissage en cours</b>, jamais comme un aveu d'échec.",
      "Limites crédibles : la gestion budgétaire de la coopérative · la conduite d'un conseil d'école · l'écrit administratif · les procédures que tu n'as jamais eu à appliquer."],
     "<i>« La gestion budgétaire de la coopérative, je ne l'ai jamais faite. Je sais tenir un budget de classe, mais pas celui d'une école. C'est justement ce que j'attends de la formation. »</i>",
     "❌ « Aucune » · ❌ « Je suis trop perfectionniste » (c'est une fausse limite, il le sait)."),

    ("6", "⚠️ LA QUESTION PIÈGE — « Quel regard portez-vous sur votre école actuelle ? »",
     "Ta loyauté et ta discrétion. Il cherche à savoir si tu régleras tes problèmes en parlant.",
     ["<b>Parle des problèmes, jamais des personnes.</b> C'est la règle absolue.",
      "Sujets sûrs : le suivi des AESH · la continuité entre les cycles · la communication avec les familles · les locaux · l'absentéisme · les effectifs.",
      "Formule toujours en <b>« ce qui manque »</b>, jamais en <b>« ce qui est mal fait »</b>.",
      "Et termine par ce que <b>ton école fait bien</b> — un directeur critique tout le monde, sauf lui."],
     "<i>« Ce qui manque dans mon école, c'est un outil commun pour suivre les élèves à besoins particuliers. Sur le reste, l'équipe est solide et on travaille bien ensemble. »</i>",
     "❌ Critiquer ton directeur · ❌ critiquer tes collègues · ❌ critiquer la mairie · ❌ « ici rien ne marche »."),

    ("7", "« Comment travaillez-vous avec les familles ? »",
     "Ta capacité à tenir la relation. En REP+, c'est un point central.",
     ["<b>Aller vers elles</b> — ne pas attendre que le conflit arrive.",
      "<b>Expliquer</b> ce que fait l'école et pourquoi : une famille qui comprend devient une alliée.",
      "<b>Recevoir</b> : un rendez-vous, une écoute, une trace écrite de ce qui a été dit.",
      "En REP+, anticiper : la distance, la langue, les horaires de travail, la confiance à construire."],
     "Une rencontre qui a débloqué une situation : un appel, une explication en shikomori, un rendez-vous où la famille s'est sentie écoutée.",
     "❌ « Je convoque les parents quand il y a un problème. » La convocation n'est pas une relation."),

    ("8", "« Si vous êtes nommé dans une école difficile, que faites-vous les trois premiers mois ? »",
     "Ton sens des priorités. Un débutant qui annonce un grand projet dès l'arrivée fait peur.",
     ["<b>Semaines 1-2 : écouter.</b> Entretiens individuels avec chaque enseignant, sans ordre du jour.",
      "<b>Semaine 3 : un conseil des maîtres léger</b> — pas de grand chantier, juste poser le cadre de travail.",
      "<b>Mois 1-2 : stabiliser</b> l'essentiel — sécurité, plannings, informations aux familles, remplacements.",
      "<b>Mois 3 : construire</b> le projet avec l'équipe, pas contre elle.",
      "Et une règle : <b>ne jamais critiquer le prédécesseur</b> devant l'équipe."],
     "<i>« Mon premier mois, je ne change rien. J'écoute, je comprends comment l'école fonctionne, et je stabilise ce qui doit l'être. »</i>",
     "❌ « Je mets en place mon projet dès la rentrée. » Une équipe ne se réforme pas en trois semaines."),

    ("9", "« Que ferez-vous pour les élèves à besoins particuliers ? »",
     "Ta connaissance du dispositif — et c'est TON terrain : SEGPA, FLS, harcèlement.",
     ["<b>Réunir</b> : l'équipe éducative est le lieu où on décide ensemble — pas le bureau du directeur.",
      "<b>Formaliser</b> : <b>PPS</b> (handicap, MDPH), <b>PAP</b> (troubles des apprentissages), <b>PPRE</b> (difficultés scolaires).",
      "<b>Suivre les AESH</b> : qui accompagne qui, sur quels temps, avec quel emploi du temps. C'est là que tout se perd.",
      "Appuyer sur ton expérience : <b>six ans de SEGPA</b>, la certification <b>français langue seconde</b>, le <b>référent harcèlement</b>."],
     "<i>« En SEGPA, j'ai appris que le plus difficile n'est pas l'élève : c'est de faire travailler ensemble l'enseignant, l'AESH et la famille sur le même objectif. »</i>",
     "❌ « Je demanderai plus d'AESH. » Un directeur ne décide pas des notifications MDPH — il ne peut pas le promettre."),

    ("10", "« Avez-vous des questions ? »",
     "Ton intérêt réel pour le métier. Répondre « non » est une occasion manquée.",
     ["<b>1.</b> « Quelles sont les difficultés que vous voyez le plus souvent chez les directeurs qui débutent dans la circonscription ? »",
      "<b>2.</b> « Comment accompagnez-vous un directeur qui prend sa première fonction ? »",
      "<b>3.</b> « Sur le suivi des AESH et des élèves à besoins particuliers, quel est votre regard sur la circonscription ? »",
      "<b>4.</b> (si la conversation s'y prête) « Y a-t-il des écoles où vous pensez qu'un débutant serait bien accompagné par son équipe ? »"],
     "Ces questions disent : <i>« je pense au métier, pas au poste »</i>. C'est exactement ce qu'il veut entendre.",
     "❌ « Non, j'ai tout ce qu'il me faut. » · ❌ Demander une école précise."),
]

REPONSE_TYPE = """
<div class="rt">
  <div class="rt-t">La trame de réponse à réutiliser pour TOUTE question</div>
  <div class="rt-4">
    <div><b>1. Je nomme</b><span>De quoi je parle, en une phrase.</span></div>
    <div><b>2. Je partage</b><span>Ce que j'ai vu / vécu, concrètement.</span></div>
    <div><b>3. J'agis</b><span>Ce que j'ai fait, ou ce que je ferais.</span></div>
    <div><b>4. Je trace</b><span>Ce que j'en retiens, et comment je vérifie.</span></div>
  </div>
  <p class="rt-note">Si tu appliques cette trame, <b>aucune réponse ne dure plus de 2 minutes</b> et aucune ne part dans le vague.</p>
</div>
"""


def qcard(num, q, teste, elements, exemple, eviter):
    lis = "".join(f"<li>{e}</li>" for e in elements)
    qcls = " piege" if "PIÈGE" in q else ""
    return f"""
<div class="qc{qcls}">
  <div class="qc-h"><div class="n">{num}</div><h3>{q}</h3></div>
  <div class="teste"><b>Ce qu'il teste :</b> {teste}</div>
  <ul class="els">{lis}</ul>
  <div class="ex"><b>L'exemple à donner</b><p>{exemple}</p></div>
  <div class="ev">{eviter}</div>
</div>"""


CSS = """
@page { size: A4 portrait; margin: 12mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1c2331; margin: 0;
  font-size: 10.3pt; line-height: 1.52; }
h1 { font-size: 1.42rem; color: #12294d; margin: 0 0 3px; }
.sub { color: #5b6779; font-size: .82rem; margin: 0 0 12px; }
.cover { border-bottom: 3px solid #12294d; padding-bottom: 10px; margin-bottom: 14px; }
.tagc { display: inline-block; background: #12294d; color: #fff; font-size: .66rem; font-weight: 800;
  letter-spacing: .8px; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; margin-bottom: 7px; }

.rt { background: #f0f7ff; border: 1px solid #bfdbfe; border-radius: 12px; padding: 13px 16px; margin: 14px 0 18px; }
.rt-t { font-weight: 800; color: #2563eb; font-size: .8rem; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 9px; }
.rt-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 9px; }
.rt-4 div { background: #fff; border: 1px solid #dbeafe; border-radius: 8px; padding: 8px 10px; }
.rt-4 b { display: block; font-size: .76rem; color: #12294d; margin-bottom: 3px; }
.rt-4 span { font-size: .74rem; color: #5b6779; line-height: 1.4; }
.rt-note { margin: 10px 0 0; font-size: .8rem; color: #1e3a8a; }

.qc { border: 1px solid #e2e8f0; border-left: 5px solid #2563eb; border-radius: 11px;
  padding: 14px 17px; margin-bottom: 13px; background: #fff; page-break-inside: avoid; }
.qc.piege { border-left-color: #c0392b; background: #fffbfb; }
.qc-h { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 7px; }
.qc-h .n { flex: 0 0 26px; height: 26px; border-radius: 50%; background: #12294d; color: #fff;
  font-weight: 800; font-size: .78rem; display: flex; align-items: center; justify-content: center; }
.qc.piege .qc-h .n { background: #c0392b; }
.qc-h h3 { margin: 0; font-size: .94rem; color: #12294d; line-height: 1.35; }
.qc.piege .qc-h h3 { color: #991b1b; }

.teste { font-size: .84rem; color: #5b6779; background: #f8fafc; border-radius: 7px;
  padding: 6px 10px; margin-bottom: 8px; }
.teste b { color: #12294d; }
.els { margin: 0 0 9px; padding-left: 18px; font-size: .9rem; }
.els li { margin-bottom: 5px; }
.els li b { color: #12294d; }
.ex { background: #fffbeb; border-left: 3px solid #b8860b; border-radius: 7px; padding: 7px 11px; margin-bottom: 6px; }
.ex b { font-size: .71rem; letter-spacing: .6px; text-transform: uppercase; color: #92400e; }
.ex p { margin: 4px 0 0; font-size: .89rem; line-height: 1.55; color: #422006; }
.ev { background: #fef2f2; border-left: 3px solid #c0392b; border-radius: 7px;
  padding: 8px 12px; font-size: .86rem; color: #7f1d1d; }

.fin { background: #12294d; color: #fff; border-radius: 13px; padding: 16px 19px; margin-top: 16px; }
.fin h3 { margin: 0 0 8px; font-size: .92rem; color: #93c5fd; letter-spacing: .5px; text-transform: uppercase; }
.fin p { margin: 0 0 7px; font-size: .86rem; line-height: 1.55; }
.fin p:last-child { margin: 0; }
.fin b { color: #fbbf24; }
"""

html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Les questions de l'inspecteur — éléments de réponse</title>
<style>{CSS}</style></head><body>

<div class="cover">
  <div class="tagc">Carte mentale 4 — développée</div>
  <h1>Les questions de l'inspecteur — éléments de réponse</h1>
  <p class="sub">Entretien préliminaire avec l'IEN · Jacques Hassani Moustoifa · 10 questions, ce qu'il teste derrière, et quoi répondre</p>
</div>

<div class="rt" style="background:#fffbeb;border-color:#fde68a">
  <div class="rt-t" style="color:#92400e">Comment lire cette fiche</div>
  <p style="margin:0;font-size:.85rem">Ce ne sont pas des réponses à réciter. Ce sont des <b>éléments</b> : les points à faire figurer,
  et ceux à éviter. Tu les dis <b>avec tes mots</b>, dans l'ordre que tu veux.
  <b>Une seule règle : ne dis jamais quelque chose que tu ne peux pas illustrer par un exemple vécu.</b></p>
</div>

{REPONSE_TYPE}

{''.join(qcard(*q) for q in QS)}

<div class="fin">
  <h3>Les 3 réflexes qui sauvent</h3>
  <p><b>1. Si tu ne sais pas :</b> « Je ne sais pas, mais voilà comment je chercherais. » Un inspecteur préfère toujours ça à une réponse inventée.</p>
  <p><b>2. Si tu t'emballes :</b> arrête-toi. Un silence n'est pas un trou, c'est de la maîtrise. Le jury a besoin de respirer.</p>
  <p><b>3. Si on te pousse sur un sujet que tu ne maîtrises pas :</b> reviens au concret. « Ce que je peux dire, c'est ce que j'ai vu dans mon école : … »</p>
</div>

</body></html>"""

(D / "questions_inspecteur.html").write_text(html, encoding="utf-8")
print(f"  ✅ questions_inspecteur.html — {len(html)//1024} Ko")


async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        p = await b.new_page()
        await p.goto(f"file://{D}/questions_inspecteur.html", wait_until="load")
        await p.wait_for_timeout(800)
        await p.pdf(path=str(D / "QUESTIONS_INSPECTEUR_ELEMENTS_REPONSE.pdf"),
                    format="A4", print_background=True)
        await b.close()

asyncio.run(pdf())
import fitz
f = D / "QUESTIONS_INSPECTEUR_ELEMENTS_REPONSE.pdf"
d = fitz.open(f)
print(f"  ✅ {f.name} — {d.page_count} pages — {f.stat().st_size//1024} Ko")
for i in range(d.page_count):
    d[i].get_pixmap(dpi=105).save(f"/tmp/q_p{i+1}.png")
