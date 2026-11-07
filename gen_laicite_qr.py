#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Q&R laïcité — cas concrets pour un directeur d'école."""

import pathlib, asyncio

D = pathlib.Path("/workspace/prepa-directeur")

# (famille, [ (question, reponse, [gestes], confusion, texte) ])
FAM = [
    ("bleu", "A · LES ÉLÈVES", [
        ("Une élève de CM2 arrive avec un voile.",
         "La loi du 15 mars 2004 interdit à l'école publique les signes ou tenues manifestant <b>ostensiblement</b> une appartenance religieuse. Le directeur doit agir — mais d'abord <b>par le dialogue</b>.",
         ["Entretien <b>individuel et calme</b>, jamais devant la classe.",
          "J'explique <b>la règle</b> et je laisse un <b>temps</b> pour l'enlever, sans humiliation.",
          "J'informe la <b>famille le jour même</b> et je propose un rendez-vous.",
          "Je <b>trace</b> : date, faits, ce que j'ai dit, la réponse."],
         "Lui arracher le foulard, la renvoyer chez elle, ou la laisser entrer « pour ne pas créer d'incident » — les deux sont des fautes.",
         "Loi du 15 mars 2004"),
        ("Elle refuse de l'enlever, et la famille soutient son refus.",
         "La scolarité n'est <b>pas rompue automatiquement</b>. Le directeur poursuit le dialogue et <b>saisit l'IEN</b> : c'est l'échelon supérieur qui décide de la suite.",
         ["Je <b>réunis la famille</b> avec l'IEN si possible.",
          "Je continue à <b>accueillir l'élève</b> dans l'attente : elle reste une élève de l'école.",
          "Je <b>relate par écrit</b> chaque étape au fur et à mesure.",
          "Je <b>protège l'élève</b> des remarques des autres pendant tout ce temps."],
         "Prononcer une exclusion : ce n'est pas le pouvoir du directeur, et ce n'est pas automatique.",
         "Procédure : dialogue → IEN → DASEN"),
        ("Une élève porte un bandana « pour cacher ses cheveux », pas par religion.",
         "Le critère n'est pas l'objet, c'est <b>l'intention manifestée</b>. Un bandana peut être licite — sauf s'il manifeste ostensiblement une appartenance religieuse.",
         ["J'<b>interroge</b> avant de conclure : pourquoi, depuis quand, que dit la famille ?",
          "Je <b>ne présume pas</b> : une coiffure, un bandana de sport, un bonnet n'ont rien d'interdit en soi.",
          "Si le doute persiste, j'en <b>parle à l'IEN</b> plutôt que de trancher seul."],
         "Interdire « par précaution ». Une interdiction sans base est une faute — et c'est exactement ce qui donne le sentiment d'arbitraire.",
         "Loi de 2004 : le critère est le <b>caractère ostensible</b>"),
        ("Deux élèves se moquent d'une camarade voilée, ou d'un camarade qui ne croit pas.",
         "C'est du <b>harcèlement</b>, pas une simple dispute. Le directeur applique le protocole, pas une punition rapide.",
         ["Je <b>protège</b> l'élève visé, et je ne le confronte pas à ses auteurs.",
          "Je <b>réunis l'équipe</b> et j'informe les familles.",
          "Je <b>surveille les temps non couverts</b> : cour, couloirs, cantine, entrée.",
          "Je <b>trace</b> et je m'appuie sur le dispositif <b>pHARe</b>."],
         "Traiter ça comme un conflit ordinaire entre enfants.",
         "Protocole harcèlement · pHARe"),
        ("Un élève refuse d'assister au cours d'éducation à la sexualité.",
         "Ce n'est pas un droit général de dispense. Un <b>droit de retrait</b> existe pour ce thème précis, prévu par les textes — le directeur le vérifie et l'applique s'il s'applique.",
         ["J'<b>écoute</b> la famille et je demande la raison exacte.",
          "Je <b>vérifie le texte applicable</b> avant de répondre — je ne réponds jamais de mémoire sur un droit.",
          "Je <b>propose un accueil alternatif</b> pendant l'heure concernée plutôt qu'une absence."],
         "Répondre « oui » ou « non » sans avoir vérifié : c'est là qu'on se trompe.",
         "À vérifier au cas par cas dans les textes en vigueur"),
        ("Un élève demande à ne pas faire piscine « pour raison religieuse ».",
         "La religion <b>n'est pas un motif de dispense d'EPS</b>. En revanche, un aménagement peut exister pour raison de santé ou de pudeur, sur avis médical.",
         ["Je <b>distingue</b> : santé (dispense possible) / religion (pas un motif).",
          "Je <b>cherche une solution</b> : tenue adaptée, organisation, dialogue avec l'enseignant d'EPS.",
          "Je <b>ne laisse pas</b> l'élève s'installer dans une non-participation durable."],
         "Accorder la dispense « pour éviter le conflit » : ça crée un précédent et ça isole l'élève.",
         "Obligation scolaire · EPS obligatoire"),
    ]),
    ("rouge", "B · LES ADULTES DE L'ÉCOLE — le cœur de ta question", [
        ("Une collègue enseignante porte le voile en classe.",
         "⚠️ <b>Ce n'est pas la loi de 2004.</b> Un enseignant est un <b>agent public</b> : il est soumis à une obligation de <b>neutralité totale</b> — pas seulement aux signes « ostensibles ». <b>Aucun signe d'appartenance, quelle que soit sa taille.</b>",
         ["Entretien <b>en tête-à-tête d'abord</b> : jamais devant les élèves, jamais devant les collègues.",
          "Je <b>rappelle le cadre</b> avec respect et sans accusation.",
          "Je <b>trace</b> l'entretien et ce qui a été dit.",
          "Si le refus persiste, je <b>signale à l'IEN</b> — car <b>je n'ai pas de pouvoir hiérarchique</b>."],
         "La <b>sanctionner</b> : tu ne peux pas (pas d'autorité hiérarchique). La <b>couvrir</b> : tu ne dois pas. Le seul geste juste est : parler, tracer, signaler.",
         "Neutralité des agents publics — loi n° 83-634 du 13 juillet 1983, art. 25"),
        ("Et si l'enseignante dit : « c'est mon droit, je suis croyante. »",
         "Le droit de croire est <b>entier</b> et protégé. Ce qui est limité, c'est <b>l'exercice de sa fonction</b> avec un signe d'appartenance.",
         ["Je formule la distinction : « Ta croyance est libre. Ta fonction est neutre. »",
          "Je ne me place pas sur le terrain de la foi, mais sur celui du <b>statut</b>.",
          "Je propose les ressources : <b>référent laïcité</b>, formation, accompagnement."],
         "Entrer dans un débat théologique. Ça ne se gagne jamais, et ça sort du cadre.",
         "Liberté de conscience ≠ neutralité de la fonction"),
        ("Un collègue fait du prosélytisme : il parle de sa religion aux élèves.",
         "C'est une atteinte au principe de neutralité <b>et</b> à la liberté de conscience des élèves. C'est plus grave qu'un signe, parce que ça agit sur les élèves.",
         ["J'<b>interromps</b> : entretien immédiat, faits précis, datés.",
          "Je <b>protège les élèves</b> : je vérifie qu'aucun n'a subi de pression.",
          "Je <b>signale à l'IEN</b> — c'est lui qui a le pouvoir d'agir.",
          "Je <b>trace</b> avec précision : un signalement sans faits ne sert à rien."],
         "Attendre « de voir si ça recommence ». Chaque semaine d'attente expose des élèves.",
         "Neutralité · liberté de conscience des élèves"),
        ("Une AESH porte le voile.",
         "L'AESH est un <b>agent public</b> (contractuel de droit public) : <b>même obligation de neutralité</b> que l'enseignant.",
         ["Je lui parle <b>seule, en premier</b>, avec respect — c'est un adulte qui travaille.",
          "Je <b>rappelle le cadre</b> de sa fonction.",
          "Je <b>signale</b> à l'IEN et à l'employeur si nécessaire.",
          "Je <b>ne la laisse pas</b> sans accompagnement : elle peut avoir besoin d'être orientée."],
         "« Ce n'est pas mon personnel, ce n'est pas mon affaire. » Faux : dans l'école, c'est le directeur qui garantit le cadre.",
         "Agent public contractuel de droit public → neutralité"),
        ("Le directeur lui-même — est-ce que ça te concerne ?",
         "<b>Oui, et en premier.</b> Tu es agent public, et tu es de plus <b>le garant</b> de la laïcité dans ton école. Ton exemple vaut plus que dix circulaires.",
         ["Je ne porte aucun signe d'appartenance dans l'exercice de mes fonctions.",
          "Je ne manifeste pas mes convictions devant les élèves ni devant l'équipe.",
          "Je <b>dis à mon équipe</b> que j'applique la règle à moi-même d'abord."],
         "Penser que la laïcité ne concerne que les autres. C'est la première chose que l'IEN regarde.",
         "Statut + fonction de garant"),
    ]),
    ("vert", "C · LES FAMILLES ET LES TIERS", [
        ("Une mère voilée vient chercher son enfant / assister à une réunion.",
         "⚠️ <b>Elle peut entrer.</b> Les parents ne sont <b>pas</b> soumis à la neutralité : ce sont des <b>usagers</b>. Aucun texte n'interdit le voile aux parents dans l'enceinte de l'école.",
         ["Je l'<b>accueille normalement</b> — c'est la règle.",
          "Si un collègue s'y oppose, <b>je le recadre</b> : l'interdiction n'existe pas.",
          "Je <b>rappelle le cadre</b> à l'équipe en conseil des maîtres pour éviter les erreurs."],
         "Interdire l'entrée à une mère voilée. C'est une faute — et c'est exactement ce qui fait dire aux familles que la laïcité les vise.",
         "Parents = usagers, non soumis à la neutralité"),
        ("Une mère voilée veut accompagner une sortie scolaire.",
         "Elle le <b>peut</b>. Les parents accompagnateurs ne sont pas des agents publics : pas d'obligation de neutralité. Ils sont tenus à la <b>discrétion</b> et au respect du cadre.",
         ["J'<b>accepte</b> et je le dis clairement à l'équipe.",
          "Je <b>fixe le cadre</b> : pas de prosélytisme pendant l'activité, respect du programme.",
          "Je <b>trace</b> la règle dans le document d'organisation des sorties."],
         "Refuser « par principe ». C'est une discrimination, et ça se retourne contre l'école.",
         "Parents accompagnateurs ≠ agents publics"),
        ("Un intervenant extérieur (sport, musique, théâtre) fait du prosélytisme.",
         "Il est tenu par le <b>contrat</b> et la <b>charte</b> signée avec l'école. Le directeur peut <b>mettre fin à l'intervention</b>.",
         ["Je <b>mets fin</b> à la séance immédiatement si des élèves sont exposés.",
          "Je <b>signale</b> à l'IEN et à l'organisme employeur.",
          "Je <b>vérifie</b> que la charte d'intervention a bien été signée avant toute intervention."],
         "Attendre la fin du cycle pour « ne pas déranger ».",
         "Contrat + charte d'intervention"),
        ("Une famille demande un menu confessionnel à la cantine.",
         "La restauration scolaire relève de la <b>commune</b>. Le directeur <b>transmet</b>, il ne décide pas.",
         ["J'<b>écoute</b> la demande sans la juger.",
          "Je <b>transmets</b> à la mairie et je le dis à la famille.",
          "J'<b>explique</b> que l'école ne gère pas les menus."],
         "Promettre un menu, ou répondre sèchement « il n'y en a pas ». Les deux créent un conflit.",
         "Compétence communale"),
        ("Une famille demande une dispense de piscine pour sa fille « par pudeur religieuse ».",
         "Voir la question A6 : la religion n'est pas un motif de dispense d'EPS. Mais <b>écouter</b> et <b>chercher un aménagement</b> (tenue, organisation) fait partie du métier.",
         ["Je <b>reçois</b> la famille et j'écoute ce qui gêne réellement.",
          "Je <b>cherche une solution pratique</b> avec l'enseignant d'EPS.",
          "Je <b>ne laisse pas</b> la situation s'installer sans réponse."],
         "Renvoyer la famille sans explication : elle reviendra, ou l'élève décrochera.",
         "Obligation scolaire"),
    ]),
    ("or", "D · LES RÉFLEXES DU DIRECTEUR", [
        ("Que fais-je en premier, dans tous les cas ?",
         "<b>J'écoute avant d'appliquer.</b> Un fait mal compris produit une décision injuste — et une décision injuste abîme la laïcité plus qu'un signe.",
         ["Je <b>sépare les faits</b> des impressions : qui, quoi, quand, où, devant qui.",
          "Je <b>parle à la personne concernée d'abord</b>, jamais d'elle d'abord.",
          "Je <b>trace</b> avant d'agir, pas après.",
          "Je <b>me demande</b> : « est-ce que j'aurais fait pareil pour un autre élève ? »"],
         "Agir vite pour « montrer que je tiens le cadre ». La précipitation est le meilleur moyen de mal appliquer.",
         "—"),
        ("Quels sont mes pouvoirs réels — et mes limites ?",
         "Le directeur a une <b>autorité fonctionnelle</b>, <b>pas hiérarchique</b>. Sur un adulte, il ne peut ni sanctionner ni noter : il <b>parle</b>, il <b>trace</b>, il <b>signale</b>.",
         ["Sur un <b>élève</b> : entretien, dialogue famille, procédure, IEN.",
          "Sur un <b>adulte</b> : entretien, rappel du cadre, trace, <b>signalement à l'IEN</b>.",
          "Sur un <b>tiers</b> : contrat, charte, fin d'intervention, signalement.",
          "Dans <b>tous</b> les cas : la trace écrite."],
         "Croire qu'on peut « régler » un adulte soi-même. C'est l'erreur qui fait perdre un directeur débutant.",
         "Loi Rilhac : autorité fonctionnelle ≠ hiérarchique"),
        ("Comment éviter l'application inégale — le vrai risque ?",
         "En se posant la question <b>à chaque fois</b>. La laïcité se dégrade non pas dans les textes, mais dans <b>la manière</b> : qui on reprend, qui on regarde, qui on soupçonne.",
         ["Je <b>vérifie la symétrie</b> : est-ce que je fais la même remarque à tout le monde ?",
          "Je <b>ne commente jamais</b> l'apparence d'un élève devant les autres.",
          "Je <b>rappelle à l'équipe</b> que la règle s'applique à tous, également.",
          "Je <b>trace</b> aussi les situations où je n'ai <b>rien</b> fait : ça montre la cohérence."],
         "Laisser un collègue traiter certains élèves plus durement « parce que c'est culturel ». Ça, c'est la dérive.",
         "Principe d'égalité — Constitution, art. 1<sup>er</sup>"),
        ("Et si moi, personnellement, je trouve ça injuste ?",
         "Tu as le droit de le penser, et beaucoup le pensent. Mais <b>en fonction</b>, tu appliques le cadre — et tu peux le faire <b>avec humanité</b>, ce qui n'est pas la même chose que l'appliquer mal.",
         ["J'applique la règle, <b>sans humilier</b>.",
          "Je <b>dis à mon équipe</b> ce que je pense du risque d'inégalité — sans jamais contester le cadre devant les élèves.",
          "Je <b>choisis mes mots</b> : la façon d'appliquer une règle peut la rendre supportable ou insupportable."],
         "Contester le cadre devant les élèves ou devant l'inspecteur. Ce n'est pas ton rôle, et ça fragilise ta position.",
         "Obligation de loyauté du fonctionnaire"),
    ]),
]

COUL = {"bleu": "#2563eb", "rouge": "#c0392b", "vert": "#1a7a4a", "or": "#b8860b"}

SYNTH = [
    ("Les élèves", "Loi du 15 mars 2004", "Signes <b>ostensibles</b> interdits", "Entretien → famille → IEN", "bleu"),
    ("Enseignants", "Neutralité (statut)", "<b>Aucun</b> signe, sans exception", "Entretien → IEN", "rouge"),
    ("AESH", "Neutralité (agent public)", "<b>Aucun</b> signe", "Entretien → IEN + employeur", "rouge"),
    ("Le directeur", "Neutralité + garantie", "<b>Aucun</b> signe", "Son exemple d'abord", "rouge"),
    ("Les parents", "Usagers", "<b>Aucune</b> interdiction", "Accueil normal", "vert"),
    ("Accompagnateurs", "Bénévoles", "<b>Aucune</b> interdiction", "Cadre de discrétion", "vert"),
    ("Intervenants", "Contrat + charte", "Neutralité <b>contractuelle</b>", "Fin d'intervention + signalement", "vert"),
]


def bloc_qr(f, i, item):
    q, rep, gestes, conf, txt = item
    g = "".join("<li>%s</li>" % x for x in gestes)
    t = '<div class="txtx"><b>Texte :</b> %s</div>' % txt if txt and txt != "—" else ""
    return ('<div class="qr" style="--c:%s">'
            '<div class="qh"><span class="qn">%d</span><span class="qt">%s</span></div>'
            '<div class="rep">%s</div>'
            '<div class="lab">Ce que je fais</div><ul>%s</ul>'
            '<div class="conf"><b class="cl">⚠️ La confusion à éviter</b> %s</div>%s</div>') % (
            COUL[f], i, q, rep, g, conf, t)


qr_html = []
n = 0
for f, titre, items in FAM:
    qr_html.append('<h2 style="color:%s;border-bottom-color:%s">%s</h2>' % (COUL[f], COUL[f], titre))
    for it in items:
        n += 1
        qr_html.append(bloc_qr(f, n, it))
qr_html = "".join(qr_html)

synth_html = "".join(
    '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (a, b, c, d)
    for a, b, c, d, _ in SYNTH)

CSS = """
@page { size: A4 portrait; margin: 13mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1c2331; margin: 0;
  font-size: 9.4pt; line-height: 1.46; }
.cov { border-bottom: 3px solid #12294d; padding-bottom: 9px; margin-bottom: 12px; }
.tagc { display: inline-block; background: #c0392b; color: #fff; font-size: .63rem; font-weight: 800;
  letter-spacing: .9px; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; margin-bottom: 6px; }
h1 { font-size: 1.3rem; color: #12294d; margin: 0 0 3px; }
.sub { color: #5b6779; font-size: .79rem; margin: 0; }
h2 { font-size: .8rem; letter-spacing: .7px; text-transform: uppercase;
  border-bottom: 2px solid #e2e8f0; padding-bottom: 4px; margin: 15px 0 8px; page-break-after: avoid; }
table { width: 100%; border-collapse: collapse; font-size: .76rem; margin: 8px 0 4px; }
th { background: #12294d; color: #fff; padding: 6px 7px; text-align: left; font-size: .65rem;
  text-transform: uppercase; letter-spacing: .4px; }
td { border-bottom: 1px solid #e2e8f0; padding: 5px 7px; vertical-align: top; }
tr { page-break-inside: avoid; }
.qr { border: 1px solid #e2e8f0; border-left: 5px solid var(--c); border-radius: 10px;
  padding: 10px 13px; margin-bottom: 9px; background: #fff; page-break-inside: avoid; }
.qh { display: flex; gap: 8px; align-items: flex-start; margin-bottom: 6px; }
.qn { flex: 0 0 21px; height: 21px; border-radius: 50%; background: var(--c); color: #fff;
  font-weight: 800; font-size: .68rem; display: flex; align-items: center; justify-content: center; }
.qt { flex: 1; font-size: .88rem; font-weight: 700; color: #12294d; line-height: 1.35; }
.rep { font-size: .83rem; background: #f8fafc; border-radius: 7px; padding: 7px 10px; margin-bottom: 7px; }
.lab { font-size: .64rem; font-weight: 800; letter-spacing: .7px; text-transform: uppercase;
  color: var(--c); margin-bottom: 3px; }
ul { margin: 0 0 7px; padding-left: 17px; font-size: .81rem; }
ul li { margin-bottom: 3px; }
.conf { background: #fef2f2; border-left: 3px solid #c0392b; border-radius: 6px;
  padding: 6px 10px; font-size: .79rem; color: #7f1d1d; }
.conf .cl { display: block; font-size: .64rem; letter-spacing: .6px; text-transform: uppercase;
  color: #c0392b; margin-bottom: 3px; }
.txtx { font-size: .73rem; color: #5b6779; margin-top: 6px; font-style: italic; }
.txtx b { color: #12294d; font-style: normal; }

.intro { background: #eff6ff; border: 1px solid #bfdbfe; border-left: 4px solid #2563eb;
  border-radius: 9px; padding: 11px 14px; font-size: .85rem; margin: 10px 0 12px; }
.intro b { color: #12294d; }
.fin { background: #12294d; color: #fff; border-radius: 11px; padding: 14px 17px; margin-top: 12px; }
.fin h3 { color: #fbbf24; margin: 0 0 7px; font-size: .8rem; letter-spacing: .6px; text-transform: uppercase; }
.fin p { margin: 0 0 6px; font-size: .84rem; line-height: 1.5; }
.fin b { color: #93c5fd; }
"""

html = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Laïcité — questions-réponses, cas concrets</title>
<style>__CSS__</style></head><body>

<div class="cov">
  <div class="tagc">Entretien préliminaire · laïcité</div>
  <h1>Laïcité — les cas concrets du directeur</h1>
  <p class="sub">Élèves et voile · collègues et voile · AESH · parents · intervenants — 20 questions, la réponse, le geste, la confusion à éviter</p>
</div>

<div class="intro">
  <b>⚠️ La distinction qui gouverne tout ce document</b><br>
  <b>Les élèves</b> relèvent de la <b>loi de 2004</b> : seuls les signes <b>ostensibles</b> sont interdits.<br>
  <b>Les adultes de l'école</b> relèvent de la <b>neutralité des agents publics</b> : <b>aucun signe</b>, sans exception.<br>
  <b>Les parents</b> ne relèvent d'<b>aucune</b> interdiction : ce sont des usagers.<br><br>
  Confondre ces trois régimes, c'est la faute la plus fréquente — et c'est celle qui fait le plus de dégâts.
</div>

<h2 style="color:#12294d">Le tableau de synthèse — à retenir en premier</h2>
<table>
  <tr><th style="width:19%">Qui</th><th style="width:26%">Régime</th><th style="width:25%">Signes</th><th>Ce que fait le directeur</th></tr>
  __SYNTH__
</table>

__QR__

<div class="fin">
  <h3>Les 3 règles d'or du directeur</h3>
  <p><b>1.</b> « Je parle d'abord à la personne, jamais d'elle. » — Un entretien individuel et calme avant toute décision.</p>
  <p><b>2.</b> « Je n'ai pas de pouvoir hiérarchique sur un adulte : je parle, je trace, je signale à l'IEN. » — C'est le cadre, pas une faiblesse.</p>
  <p><b>3.</b> « La même règle, appliquée de la même façon à tous. » — La laïcité se dégrade dans la manière, pas dans les textes.</p>
</div>

</body></html>"""

html = html.replace("__CSS__", CSS).replace("__SYNTH__", synth_html).replace("__QR__", qr_html)
(D / "laicite_qr.html").write_text(html, encoding="utf-8")
print("  ✅ laicite_qr.html — %d Ko · %d questions" % (len(html) // 1024, n))


async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        p = await b.new_page()
        await p.goto(f"file://{D}/laicite_qr.html", wait_until="load")
        await p.wait_for_timeout(700)
        await p.pdf(path=str(D / "LAICITE_QR_CAS_CONCRETS.pdf"), format="A4", print_background=True)
        await b.close()

asyncio.run(pdf())
import fitz
f = D / "LAICITE_QR_CAS_CONCRETS.pdf"
d = fitz.open(f)
print("  ✅ %s — %d pages — %d Ko" % (f.name, d.page_count, f.stat().st_size // 1024))
for i in range(d.page_count):
    d[i].get_pixmap(dpi=105).save(f"/tmp/qr_p{i+1}.png")
