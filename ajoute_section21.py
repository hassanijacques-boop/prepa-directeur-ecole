#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute la section 21 : L'ENTRETIEN PRELIMINAIRE AVEC L'IEN (avis favorable ou non)."""

import pathlib

P = pathlib.Path("/workspace/prepa-directeur/index.html")
t = P.read_text(encoding="utf-8")
n0 = len(t)

# ── 1. NAV : insérer #preliminaire en 21, décaler carte et textes ──
nav_old = """      <a href="#oral"><span class="n">20</span> 🗣️ Se présenter &amp; simulation complète</a>
      <a href="#carte"><span class="n">21</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">22</span> 📚 Textes officiels &amp; liens directs</a>"""
nav_new = """      <a href="#oral"><span class="n">20</span> 🗣️ Se présenter &amp; simulation complète</a>
      <a href="#preliminaire"><span class="n">21</span> 🤝 L'entretien préliminaire avec l'IEN</a>
      <a href="#carte"><span class="n">22</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">23</span> 📚 Textes officiels &amp; liens directs</a>"""
assert t.count(nav_old) == 1, f"nav {t.count(nav_old)}"
t = t.replace(nav_old, nav_new)

# ── 2. CSS ──
CSS = """
  /* ════════ SECTION 21 — ENTRETIEN PRÉLIMINAIRE IEN ════════ */
  .pi-duo{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));margin:16px 0}
  .pi-carte{border-radius:13px;padding:16px 18px;border:1px solid var(--line);background:#fff}
  .pi-carte .tt{font-weight:800;font-size:.82rem;letter-spacing:.6px;text-transform:uppercase;margin-bottom:9px}
  .pi-carte ul{margin:0;padding-left:17px;font-size:.87rem;line-height:1.65}
  .pi-carte.neutre{border-top:4px solid var(--muted)} .pi-carte.neutre .tt{color:var(--muted)}
  .pi-carte.vert{border-top:4px solid var(--vert);background:#f7fdf9} .pi-carte.vert .tt{color:var(--vert)}
  .pi-4q{display:grid;gap:11px;margin:15px 0}
  .pi-4q .q{background:#fbfcfe;border:1px solid var(--line);border-left:4px solid var(--bleu);
    border-radius:10px;padding:12px 15px}
  .pi-4q .q .t{font-weight:800;color:var(--navy);font-size:.9rem;margin-bottom:4px}
  .pi-4q .q .d{font-size:.86rem;color:var(--muted);line-height:1.6}
  .pi-dialogue{background:linear-gradient(135deg,#f8fafc,#fbfcfe);border:1px solid var(--line);
    border-radius:14px;padding:18px 20px;margin:16px 0}
  .pi-dialogue .tour{margin-bottom:14px;padding-left:14px;border-left:3px solid #cbd5e1}
  .pi-dialogue .tour:last-child{margin-bottom:0}
  .pi-dialogue .tour .qui{font-size:.72rem;font-weight:800;letter-spacing:.8px;
    text-transform:uppercase;color:var(--bleu);margin-bottom:4px}
  .pi-dialogue .tour p{margin:0;font-size:.92rem;line-height:1.7}
  .pi-dialogue .tour .pause{display:inline-block;font-size:.76rem;font-weight:700;color:var(--or);
    background:#fffbeb;border:1px dashed var(--or);border-radius:6px;padding:1px 7px;margin:5px 4px 0 0}
  .pi-sim{background:#12294d;border-radius:16px;padding:20px;margin:18px 0;color:#fff}
  .pi-sim .haut{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;
    font-size:.74rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#93c5fd}
  .pi-sim .quest{font-size:1.03rem;line-height:1.55;font-weight:600;background:rgba(255,255,255,.07);
    border-radius:11px;padding:15px 17px;margin-bottom:13px;min-height:70px}
  .pi-sim .boutons{display:flex;gap:9px;flex-wrap:wrap}
  .pi-sim button{border:none;border-radius:9px;padding:10px 16px;font-weight:800;font-size:.85rem;
    cursor:pointer;font-family:inherit}
  .pi-sim .b1{background:#2563eb;color:#fff}
  .pi-sim .b2{background:#b8860b;color:#fff}
  .pi-rep{display:none;margin-top:13px;background:rgba(184,134,11,.16);border-left:4px solid var(--or);
    border-radius:9px;padding:13px 16px;font-size:.88rem;line-height:1.68;color:#fef3c7}
  .pi-rep.on{display:block}
  .pi-rep b{color:#fbbf24}
  .pi-pos{display:grid;gap:8px;margin:14px 0}
  .pi-pos .l{background:#f0fdf4;border:1px solid #bbf7d0;border-left:4px solid var(--vert);
    border-radius:9px;padding:10px 14px;font-size:.87rem}
  .pi-pos .l b{color:var(--vert)}
  .pi-pos .l.neg{background:#fef2f2;border-color:#fecaca;border-left-color:var(--rouge)}
  .pi-pos .l.neg b{color:var(--rouge)}
  .pi-qs{display:grid;gap:10px;margin:14px 0}
  .pi-qs .item{background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:11px 14px;
    font-size:.88rem;line-height:1.6}
  .pi-qs .item .n{display:inline-block;background:var(--bleu);color:#fff;font-weight:800;
    font-size:.72rem;border-radius:50%;width:19px;height:19px;text-align:center;line-height:19px;margin-right:7px}
  .pi-jours{display:grid;gap:10px;margin:15px 0}
  .pi-jours .j{display:flex;gap:12px;background:#fbfcfe;border:1px solid var(--line);border-radius:10px;padding:12px 15px}
  .pi-jours .j .d{flex:0 0 82px;font-weight:800;font-size:.8rem;color:var(--bleu);text-transform:uppercase}
  .pi-jours .j .c{flex:1;font-size:.88rem;line-height:1.6}
"""
t = t.replace("</style>", CSS + "</style>", 1)

# ── 3. SECTION ──
SECTION = r"""
  <!-- ══════════ 21. ENTRETIEN PRÉLIMINAIRE AVEC L'IEN ══════════ -->
  <section id="preliminaire">
    <div class="kicker">Section 21 — La porte d'entrée : l'avis de l'inspecteur</div>
    <h2>🤝 L'entretien préliminaire avec l'IEN</h2>

    <div class="callout" style="border-color:var(--or);background:#fffbeb">
      <strong>⚠️ Ce n'est pas le même entretien que le jury</strong><br>
      Tu passes d'abord <strong>un entretien seul avec l'inspecteur</strong>. Son but n'est pas de te classer :
      c'est de décider s'il donne un <strong>avis favorable</strong> à ta candidature sur la liste d'aptitude.
      <strong>Sans avis favorable, tu ne vas pas plus loin.</strong> Ce n'est donc pas une compétition — c'est une porte.
    </div>

    <!-- ── A. DEUX ENTRETIENS ── -->
    <div class="bloc">
      <div class="bt">🆚 A. Ne pas confondre les deux entretiens</div>
      <div class="pi-duo">
        <div class="pi-carte neutre">
          <div class="tt">1. L'entretien préliminaire (celui de lundi)</div>
          <ul>
            <li><strong>Avec qui :</strong> l'IEN, <strong>seul</strong></li>
            <li><strong>Où :</strong> son bureau, en tête-à-tête</li>
            <li><strong>Durée :</strong> 20 à 40 minutes</li>
            <li><strong>But :</strong> <strong>rendre un avis</strong> — favorable ou non</li>
            <li><strong>Nature :</strong> une <strong>conversation</strong>, pas une épreuve</li>
            <li><strong>Ce qu'il évalue :</strong> ta <strong>fiabilité</strong> et ta <strong>lucidité</strong></li>
          </ul>
        </div>
        <div class="pi-carte vert">
          <div class="tt">2. L'entretien devant la commission (plus tard)</div>
          <ul>
            <li><strong>Avec qui :</strong> 3 membres — IA-DASEN, un IEN, un directeur d'école</li>
            <li><strong>Où :</strong> une salle, en face à face</li>
            <li><strong>Durée :</strong> 30 à 40 minutes</li>
            <li><strong>But :</strong> être <strong>inscrit</strong> sur la liste d'aptitude</li>
            <li><strong>Nature :</strong> une <strong>épreuve</strong>, avec mises en situation</li>
            <li><strong>Ce qu'il évalue :</strong> ta <strong>posture</strong> et ton <strong>projet</strong></li>
          </ul>
        </div>
      </div>
      <div class="callout" style="border-color:var(--bleu);background:#eff6ff">
        <strong>🔑 La conséquence pratique</strong><br>
        Lundi, <strong>on ne te demande pas de dérouler un projet d'école sur 3 ans.</strong>
        On te demande de montrer que tu es <strong>quelqu'un de sérieux, qui sait de quoi il parle, et qui ne se raconte pas d'histoires</strong>.
        Le projet, c'est pour la commission.
      </div>
    </div>

    <!-- ── B. CE QUE L'IEN CHERCHE ── -->
    <div class="bloc">
      <div class="bt">🔍 B. Les 4 questions que l'IEN se pose vraiment</div>
      <p>Il ne te connaît pas. Il a ton dossier sous les yeux, mais pas toi. Il cherche à combler ce vide — et il
      se pose quatre questions. <strong>Tout ce que tu dis doit y répondre.</strong></p>
      <div class="pi-4q">
        <div class="q"><div class="t">1. « Est-ce qu'il sait ce qu'est le métier ? »</div>
          <div class="d">Pas le concours, pas le titre : le <strong>quotidien</strong>. Les AESH, les parents,
          les travaux, la coopérative, les absences à remplacer, les réunions qui n'en finissent pas.
          <strong>Cite une situation concrète que tu as vécue ou observée.</strong></div></div>
        <div class="q"><div class="t">2. « Est-ce qu'il est fiable ? »</div>
          <div class="d">Il confiera une école à quelqu'un qui <strong>tient ses délais, écrit proprement, respecte
          le secret professionnel et garde son calme en situation de crise</strong>. La fiabilité se voit dans la
          façon dont tu parles : précis, daté, sans exagération.</div></div>
        <div class="q"><div class="t">3. « Est-ce qu'il sera accepté par l'équipe ? »</div>
          <div class="d">Un directeur rejeté par ses collègues est un échec pour l'inspecteur aussi.
          Il cherche quelqu'un qui <strong>écoute, ne méprise personne, et ne critique pas son école actuelle</strong>.</div></div>
        <div class="q"><div class="t">4. « Est-ce qu'il est lucide sur lui-même ? »</div>
          <div class="d">Un candidat qui ne voit aucune de ses limites inquiète plus qu'il ne rassure.
          <strong>Nommer une limite, calmement, est un signe de maturité</strong> — pas de faiblesse.</div></div>
      </div>
    </div>

    <!-- ── C. LE PIÈGE ── -->
    <div class="bloc">
      <div class="bt">🪤 C. Le piège de ce format</div>
      <div class="callout" style="border-color:var(--rouge);background:#fef2f2">
        <strong>On est tellement content d'être reçu qu'on surjoue.</strong><br>
        On parle vite, on veut convaincre, on empile les arguments. <strong>Un inspecteur se méfie de celui qui
        parle bien et ne dit rien.</strong><br><br>
        <strong>La bonne posture : calme, lente, concrète.</strong> Une idée par réponse. Des exemples, pas des adjectifs.
        Et des silences — un silence n'est pas un trou, c'est de la maîtrise.
      </div>
      <table class="ps-grille">
        <tr><th style="width:50%">❌ Ce qui inquiète l'IEN</th><th>✅ Ce qui le rassure</th></tr>
        <tr><td>« Je veux fédérer, donner du sens, impulser une dynamique »</td><td>« Dans mon école, le suivi des AESH se faisait sur un cahier. J'ai proposé un tableau partagé. »</td></tr>
        <tr><td>« Je suis prêt, j'ai tout lu »</td><td>« Je connais le cadre. Sur le terrain, je vais devoir apprendre. »</td></tr>
        <tr><td>Critiquer son directeur ou son école actuelle</td><td>Parler des <strong>problèmes</strong>, jamais des <strong>personnes</strong></td></tr>
        <tr><td>Demander une école précise dès la première phrase</td><td>Parler du métier d'abord, du poste ensuite — et seulement si on t'interroge</td></tr>
      </table>
    </div>

    <!-- ── D. LA CONVERSATION ── -->
    <div class="bloc">
      <div class="bt">💬 D. La conversation en 3 minutes — registre différent du jury</div>
      <p><strong>Ne récite pas le pitch de 90 secondes.</strong> Ici, tu parles à une personne, pas à une commission.
      Tu fais des phrases plus courtes, tu laisses des ouvertures pour qu'il puisse t'interrompre.
      <span style="color:var(--or);font-weight:700">Les ⏸ sont des endroits où tu t'arrêtes.</span></p>

      <div class="pi-dialogue">
        <div class="tour">
          <div class="qui">Toi — l'ouverture</div>
          <p>« Je suis professeur des écoles depuis 2016. Avant ça, j'étais déjà dans l'Éducation nationale depuis 2001,
          comme maître à Koungou. Donc ça fait vingt-quatre ans que je suis dans cette institution. »
          <span class="pause">⏸ pause</span></p>
        </div>
        <div class="tour">
          <div class="qui">Toi — le fil</div>
          <p>« Ce qui traverse mon parcours, c'est les élèves qui ont le plus de mal. J'ai une licence de psychologie,
          une certification en français langue seconde, et j'ai passé six ans en SEGPA. Aujourd'hui j'ai un CM1-CM2
          à La Rose, à Bandraboua, en REP+. »
          <span class="pause">⏸ pause</span></p>
        </div>
        <div class="tour">
          <div class="qui">Toi — la raison</div>
          <p>« Ce que j'ai vu, c'est que dans une école certains sujets n'avancent que si quelqu'un les porte.
          Le suivi des AESH, la relation avec les familles, le projet d'école. Quand quelqu'un s'en occupe, ça avance.
          Quand personne ne s'en occupe, ça s'arrête. »
          <span class="pause">⏸ pause</span></p>
        </div>
        <div class="tour">
          <div class="qui">Toi — l'honnêteté</div>
          <p>« Je ne vais pas vous dire que je connais le métier de directeur. Je connais celui d'enseignant, et
          j'en connais les difficultés. Le reste, c'est ce que je viens apprendre — et je suis prêt à être évalué là-dessus. »
          <span class="pause">⏸ pause</span></p>
        </div>
        <div class="tour">
          <div class="qui">Toi — la disponibilité</div>
          <p>« Voilà ce que je peux vous dire. Si vous avez des questions, je suis à votre disposition. »</p>
        </div>
      </div>

      <div class="callout" style="border-color:var(--vert);background:#f0fdf4">
        <strong>✅ Pourquoi cette version et pas le pitch de 90 s</strong><br>
        Elle est <strong>plus courte</strong> (2 minutes), elle <strong>s'arrête</strong> pour laisser l'inspecteur entrer,
        et elle finit par une <strong>offre</strong> (« je suis à votre disposition ») plutôt qu'une conclusion.
        <strong>Tu ouvres la conversation au lieu de la fermer.</strong>
      </div>
    </div>

    <!-- ── E. LES 12 QUESTIONS ── -->
    <div class="bloc">
      <div class="bt">❓ E. Les 12 questions qu'il peut te poser — entraîne-toi</div>
      <p>Une question tombe, <strong>tu réponds à voix haute</strong>, puis tu compares avec la réponse proposée.
      Ce sont des questions de <strong>conversation</strong>, pas d'épreuve : reste simple et concret.</p>

      <div class="pi-sim">
        <div class="haut">
          <span>Entretien préliminaire — entraînement</span>
          <span id="pi-num">Question 1 / 12</span>
        </div>
        <div class="quest" id="pi-quest">Appuie sur « Question suivante » pour commencer.</div>
        <div class="boutons">
          <button class="b1" onclick="piSuivant()">▶ Question suivante</button>
          <button class="b2" onclick="piRep()">💡 Voir la réponse proposée</button>
        </div>
        <div class="pi-rep" id="pi-rep"></div>
      </div>
    </div>

    <!-- ── F. LES QUESTIONS À POSER ── -->
    <div class="bloc">
      <div class="bt">🎯 F. Les questions que TU dois poser — le point le plus négligé</div>
      <div class="callout" style="border-color:var(--bleu);background:#eff6ff">
        <strong>Il va te demander : « Avez-vous des questions ? »</strong><br>
        Répondre « non » est une occasion manquée — et cela peut passer pour un manque d'intérêt.
        <strong>Prépare-en trois.</strong> Elles montrent que tu penses au métier, pas au poste.
      </div>
      <div class="pi-qs">
        <div class="item"><span class="n">1</span><strong>« Quelles sont les difficultés que vous voyez le plus souvent chez les directeurs qui débutent dans la circonscription ? »</strong>
          — <em>Elle montre que tu anticipes les difficultés réelles.</em></div>
        <div class="item"><span class="n">2</span><strong>« Comment accompagnez-vous un directeur qui prend sa première fonction ? »</strong>
          — <em>Elle montre que tu sais que tu auras besoin d'être accompagné.</em></div>
        <div class="item"><span class="n">3</span><strong>« Sur le suivi des élèves à besoins particuliers et des AESH, quel est votre regard sur la circonscription ? »</strong>
          — <em>C'est ton terrain. Elle te remet sur ton point fort.</em></div>
        <div class="item"><span class="n">4</span><strong>« Y a-t-il des écoles où vous pensez qu'un débutant serait bien accompagné par son équipe ? »</strong>
          — <em>À poser seulement si la conversation s'y prête.</em></div>
      </div>
    </div>

    <!-- ── G. LES SIGNAUX ── -->
    <div class="bloc">
      <div class="bt">⚖️ G. Ce qui fait pencher l'avis</div>
      <div class="pi-pos">
        <div class="l"><b>✅ FAVORABLE — 1.</b> Tu donnes <strong>un chiffre précis</strong> sur ton école : nombre d'élèves, nombre d'AESH, taux d'absence. Ça prouve que tu regardes ton école en directeur, pas en passager.</div>
        <div class="l"><b>✅ FAVORABLE — 2.</b> Tu racontes <strong>une situation et ce que TU as fait</strong> — pas ce que l'équipe a fait, pas ce que le directeur aurait dû faire.</div>
        <div class="l"><b>✅ FAVORABLE — 3.</b> Tu nommes <strong>une limite</strong> calmement : « la gestion budgétaire de la coopérative, je ne l'ai jamais faite ».</div>
        <div class="l"><b>✅ FAVORABLE — 4.</b> Tu distingues <strong>autorité fonctionnelle et hiérarchique</strong> — la loi Rilhac. C'est le test de lecture du cadre.</div>
        <div class="l"><b>✅ FAVORABLE — 5.</b> Tu <strong>poses des questions sur le métier</strong>, pas sur le poste.</div>
        <div class="l neg"><b>❌ DÉFAVORABLE — 1.</b> Tu critiques <strong>ton école actuelle ou ton directeur</strong>. Il en conclura que tu feras pareil avec la suivante.</div>
        <div class="l neg"><b>❌ DÉFAVORABLE — 2.</b> Tu restes <strong>dans le vague</strong> : « fédérer », « impulser », « donner du sens », sans un seul exemple.</div>
        <div class="l neg"><b>❌ DÉFAVORABLE — 3.</b> Tu parles <strong>du poste et de l'école</strong> avant d'avoir parlé du métier. Ça sent l'opportunité, pas la vocation.</div>
      </div>
    </div>

    <!-- ── H. PRÉPARATION ── -->
    <div class="bloc">
      <div class="bt">🗓️ H. La préparation quand on a peu de jours</div>
      <p><strong>Avant de réviser quoi que ce soit :</strong> relis <strong>ta fiche de candidature</strong>. C'est le document
      qu'il aura sous les yeux. <strong>Tout ce que tu diras doit être cohérent avec ce qui est écrit.</strong></p>
      <div class="pi-jours">
        <div class="j"><div class="d">Aujourd'hui</div><div class="c">
          <strong>Écris 3 situations vécues</strong> — une par feuille, en 5 lignes : ce qui s'est passé, ce que tu as fait, ce que ça a changé.
          C'est ta matière première. <strong>Sans ça, tu parleras en généralités.</strong></div></div>
        <div class="j"><div class="d">J-2</div><div class="c">
          <strong>Les 12 questions, à voix haute.</strong> Deux passages. Enregistre-toi sur les 4 plus difficiles et réécoute.
          Objectif : <strong>2 minutes par réponse maximum</strong>.</div></div>
        <div class="j"><div class="d">J-1</div><div class="c">
          <strong>Les 4 signaux favorables</strong> + <strong>les 3 questions à poser</strong>. Trouve <strong>trois chiffres</strong>
          sur ton école. Prépare tes vêtements. <strong>Couche-toi tôt.</strong></div></div>
        <div class="j"><div class="d">Le matin</div><div class="c">
          Relis <strong>seulement</strong> : la conversation en 3 minutes, les 3 questions à poser, et tes 3 chiffres.
          <strong>Rien d'autre.</strong> Arrive <strong>15 minutes avant</strong>. Emporte ta fiche de candidature.</div></div>
      </div>
      <div class="callout" style="border-color:var(--or);background:#fffbeb">
        <strong>🕋 Et une chose que beaucoup oublient</strong><br>
        Si tu ne sais pas répondre à une question, dis-le : <strong>« Je ne sais pas, mais voilà comment je chercherais. »</strong>
        Un inspecteur préfère toujours ça à une réponse inventée. <strong>C'est même souvent ce qui décide de l'avis.</strong>
      </div>
    </div>
  </section>
"""

anchor = "  <!-- ══════════ 21. TEXTES OFFICIELS ══════════ -->"
assert t.count(anchor) == 1, f"ancre {t.count(anchor)}"
t = t.replace(anchor, SECTION + "\n  <!-- ══════════ 23. TEXTES OFFICIELS ══════════ -->")

# ── 4. JS du drill ──
JS = r"""
<script>
/* ══════════════ ENTRAÎNEMENT — ENTRETIEN PRÉLIMINAIRE (12 questions) ══════════════ */
(function(){
  const Q = [
    {q:"Racontez-moi votre parcours.",
     r:"<b>2 minutes, trois temps :</b> l'ancienneté (2001, maître à Koungou) → le fil (psychologie, français langue seconde, six ans de SEGPA = les élèves qui ont le plus de mal) → aujourd'hui (CM1-CM2 à La Rose, REP+, référent harcèlement).<br><br>⏸ <b>Arrête-toi</b> et laisse-le rebondir. Ne raconte pas ta vie."},
    {q:"Pourquoi voulez-vous être directeur ?",
     r:"<b>Une seule raison, concrète :</b> il y a des sujets qui n'avancent que si quelqu'un les porte.<br><br>Donne <b>un exemple précis</b> vu dans ton école. Puis : « je veux être celui qui porte ».<br><br>⚠️ Jamais « progresser », « m'ennuyer », « avoir de l'autorité »."},
    {q:"Qu'est-ce qu'un directeur d'école ?",
     r:"Un <b>professeur des écoles chargé de la direction</b>. Il a une <b>autorité fonctionnelle</b> — organiser, coordonner, animer — et <b>pas d'autorité hiérarchique</b> sur ses collègues enseignants.<br><br>Il est garant du fonctionnement, de la sécurité, et de la mise en œuvre du projet d'école."},
    {q:"Concrètement, qu'est-ce qui vous intéresse dans ce métier ?",
     r:"<b>Le fait de créer les conditions</b> pour que chaque enseignant puisse faire sa classe.<br><br>Dis-le avec tes mots : « un directeur ne fait pas la classe aux autres ». Et ajoute ce qui t'attire vraiment — le pilotage, l'humain, l'organisation."},
    {q:"Comment voyez-vous votre rôle auprès de l'équipe ?",
     r:"<b>Écouter d'abord, décider ensuite, tracer toujours.</b><br><br>Un exemple vécu de désaccord réglé par la parole. Et la règle : je ne critique jamais un collègue devant les autres."},
    {q:"Que feriez-vous si un enseignant refusait d'appliquer une décision du conseil des maîtres ?",
     r:"1. Je <b>reparle</b> : je comprends son refus.<br>2. Je <b>rappelle le cadre</b> : la décision a été prise collectivement.<br>3. Si le refus persiste, j'<b>alerte l'IEN</b> — car <b>je n'ai pas de pouvoir hiérarchique</b>, donc je ne peux pas le contraindre.<br><br>C'est LA réponse qui prouve que tu connais la loi Rilhac."},
    {q:"Racontez-moi une situation difficile que vous avez vécue et comment vous l'avez gérée.",
     r:"Prends <b>une vraie situation</b> — un conflit avec un parent, un élève en grande difficulté, une équipe divisée.<br><br><b>Structure en 4 temps :</b> la situation (2 phrases) → ce que j'ai fait → ce que ça a produit → ce que j'en ai appris.<br><br>C'est la question qui teste ta <b>fiabilité</b>. Prépare-la à l'avance."},
    {q:"Quelles sont vos limites pour ce métier ?",
     r:"<b>Nomme-en une, calmement.</b> Exemples honnêtes : la gestion budgétaire de la coopérative, la conduite d'un conseil d'école, l'écrit administratif.<br><br>Puis : « c'est ce que j'attends de la formation et du tutorat ».<br><br>⚠️ <b>Ne dis jamais « aucune »</b> : cela inquiète plus que ça ne rassure."},
    {q:"Comment travaillez-vous avec les familles ?",
     r:"<b>Aller vers elles</b>, ne pas attendre le conflit. Une famille qui comprend ce qu'on fait devient une alliée.<br><br>Donne un exemple : une rencontre, un appel, une explication qui a débloqué une situation.<br><br>En REP+, c'est un point central : montre que tu le sais."},
    {q:"Quel regard portez-vous sur votre école actuelle ?",
     r:"⚠️ <b>Question piège.</b> Parle des <b>problèmes</b>, jamais des <b>personnes</b>.<br><br>Bons exemples : le suivi des AESH, la continuité entre les niveaux, la communication avec les familles, les locaux.<br><br>❌ Ne critique jamais ton directeur actuel ni tes collègues."},
    {q:"Si vous êtes nommé dans une école difficile, que faites-vous les trois premiers mois ?",
     r:"<b>Écouter avant d'agir.</b> Entretiens individuels avec chaque enseignant → un conseil des maîtres sans ordre du jour lourd → je stabilise l'essentiel (sécurité, plannings, informations aux familles) → je construis le projet avec l'équipe, pas contre elle.<br><br>Et je ne critique jamais le prédécesseur devant l'équipe."},
    {q:"Avez-vous des questions ?",
     r:"<b>Ne réponds jamais non.</b> Trois questions prêtes :<br>1. Les difficultés les plus fréquentes des directeurs débutants dans la circonscription.<br>2. Comment vous accompagnez un directeur qui prend sa première fonction.<br>3. Votre regard sur le suivi des AESH et des élèves à besoins particuliers."}
  ];
  let i = 0;
  const $ = id => document.getElementById(id);
  function montre(){
    $("pi-quest").textContent = Q[i].q;
    $("pi-num").textContent = `Question ${i+1} / ${Q.length}`;
    $("pi-rep").innerHTML = Q[i].r;
    $("pi-rep").classList.remove("on");
  }
  window.piSuivant = function(){
    i = (i + 1) % Q.length;
    montre();
  };
  window.piRep = function(){ $("pi-rep").classList.toggle("on"); };
  montre();
  $("pi-quest").textContent = "Appuie sur « ▶ Question suivante » pour commencer.";
})();
</script>
"""

assert t.count("</body>") == 1
t = t.replace("</body>", JS + "\n</body>")

P.write_text(t, encoding="utf-8")
print(f"  ✅ {n0//1024} Ko → {len(t)//1024} Ko  (+{(len(t)-n0)//1024})")
