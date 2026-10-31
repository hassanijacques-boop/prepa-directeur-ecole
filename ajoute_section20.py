#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute au site prepa-directeur une section 20 : SE PRESENTER + SIMULATION COMPLETE.
Insertion verifiee, sans toucher au reste du fichier."""

import pathlib, re, sys

P = pathlib.Path("/workspace/prepa-directeur/index.html")
t = P.read_text(encoding="utf-8")
orig_len = len(t)

# ═══════════════════════════════ 1. NAV ═══════════════════════════════
nav_old = """      <a href="#simulateur"><span class="n">19</span> 🎤 Simulateur d'entretien</a>
      <a href="#carte"><span class="n">20</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">21</span> 📚 Textes officiels &amp; liens directs</a>"""
nav_new = """      <a href="#simulateur"><span class="n">19</span> 🎤 Simulateur d'entretien</a>
      <a href="#oral"><span class="n">20</span> 🗣️ Se présenter &amp; simulation complète</a>
      <a href="#carte"><span class="n">21</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">22</span> 📚 Textes officiels &amp; liens directs</a>"""
assert t.count(nav_old) == 1, f"nav: {t.count(nav_old)}"
t = t.replace(nav_old, nav_new)

# ═══════════════════════════════ 2. CSS ═══════════════════════════════
CSS = """
  /* ════════ SECTION 20 — SE PRÉSENTER ════════ */
  .ps-etapes{display:grid;gap:10px;margin:16px 0}
  .ps-etape{display:flex;gap:12px;align-items:flex-start;background:#fbfcfe;
    border:1px solid var(--line);border-left:4px solid var(--bleu);border-radius:10px;padding:11px 14px}
  .ps-etape .num{flex:0 0 30px;height:30px;border-radius:50%;background:var(--bleu);color:#fff;
    font-weight:800;font-size:.85rem;display:flex;align-items:center;justify-content:center}
  .ps-etape .corps{flex:1;font-size:.89rem}
  .ps-etape .corps strong{color:var(--navy)}
  .ps-etape .duree{flex:0 0 auto;font-size:.72rem;font-weight:800;color:var(--muted);
    background:#eef2f7;padding:3px 9px;border-radius:99px;white-space:nowrap}
  .ps-pitch{background:linear-gradient(135deg,#f0f7ff,#fbfcfe);border:1px solid #bfdbfe;
    border-radius:14px;padding:18px 20px;margin:16px 0;font-size:.94rem;line-height:1.75}
  .ps-pitch p{margin:0 0 11px}
  .ps-pitch p:last-child{margin-bottom:0}
  .ps-pitch .ouverture{font-weight:800;color:var(--bleu)}
  .ps-3c{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));margin:15px 0}
  .ps-c{border-radius:12px;padding:14px 16px;border:1px solid var(--line);background:#fff}
  .ps-c .t{font-weight:800;font-size:.78rem;letter-spacing:.6px;text-transform:uppercase;margin-bottom:6px}
  .ps-c p{font-size:.87rem;margin:0}
  .ps-c.c1{border-left:4px solid var(--bleu)} .ps-c.c1 .t{color:var(--bleu)}
  .ps-c.c2{border-left:4px solid var(--or)} .ps-c.c2 .t{color:var(--or)}
  .ps-c.c3{border-left:4px solid var(--vert)} .ps-c.c3 .t{color:var(--vert)}
  .ps-non{display:grid;gap:8px;margin:14px 0}
  .ps-non div{background:#fef2f2;border:1px solid #fecaca;border-left:4px solid var(--rouge);
    border-radius:9px;padding:10px 13px;font-size:.87rem;color:#7f1d1d}
  .ps-non div b{color:var(--rouge)}
  /* simulateur */
  .ps-sim{background:var(--navy);border-radius:16px;padding:22px 20px;margin:18px 0;color:#fff}
  .ps-sim .entete{display:flex;justify-content:space-between;align-items:center;gap:12px;
    flex-wrap:wrap;margin-bottom:14px}
  .ps-sim .etape-courante{font-size:.74rem;font-weight:800;letter-spacing:1px;
    text-transform:uppercase;color:#93c5fd}
  .ps-sim .chrono{font-variant-numeric:tabular-nums;font-weight:800;font-size:1.5rem;
    background:rgba(255,255,255,.1);border-radius:10px;padding:5px 14px;letter-spacing:1px}
  .ps-sim .chrono.alerte{background:#b91c1c;animation:pulse 1s infinite}
  @keyframes pulse{50%{opacity:.65}}
  .ps-sim .question{font-size:1.06rem;line-height:1.55;font-weight:600;
    background:rgba(255,255,255,.07);border-radius:11px;padding:15px 17px;margin-bottom:14px;min-height:74px}
  .ps-sim .barre{display:flex;gap:9px;flex-wrap:wrap}
  .ps-sim button{border:none;border-radius:9px;padding:10px 16px;font-weight:800;font-size:.85rem;
    cursor:pointer;font-family:inherit;transition:.15s}
  .ps-sim button:hover{transform:translateY(-1px)}
  .ps-sim .b1{background:#2563eb;color:#fff}
  .ps-sim .b2{background:rgba(255,255,255,.16);color:#fff}
  .ps-sim .b3{background:#b8860b;color:#fff}
  .ps-aide{display:none;margin-top:14px;background:rgba(184,134,11,.16);border-left:4px solid var(--or);
    border-radius:9px;padding:13px 16px;font-size:.88rem;line-height:1.65;color:#fef3c7}
  .ps-aide.on{display:block}
  .ps-aide b{color:#fbbf24}
  .ps-prog{display:flex;gap:5px;margin-top:14px}
  .ps-prog i{flex:1;height:5px;border-radius:99px;background:rgba(255,255,255,.18);transition:.2s}
  .ps-prog i.fait{background:#4ade80}
  .ps-prog i.now{background:#60a5fa}
  .ps-grille{width:100%;border-collapse:collapse;font-size:.85rem;margin:14px 0}
  .ps-grille th{background:var(--navy);color:#fff;padding:9px 11px;text-align:left;font-size:.76rem;
    text-transform:uppercase;letter-spacing:.5px}
  .ps-grille td{border-bottom:1px solid var(--line);padding:9px 11px;vertical-align:top}
  .ps-grille tr:nth-child(even) td{background:#fbfcfe}
"""
assert t.count("</style>") >= 1
t = t.replace("</style>", CSS + "</style>", 1)

# ═══════════════════════════════ 3. SECTION HTML ═══════════════════════════════
SECTION = r"""
  <!-- ══════════ 20. SE PRÉSENTER & SIMULATION COMPLÈTE ══════════ -->
  <section id="oral">
    <div class="kicker">Section 20 — Le premier round : ta présentation</div>
    <h2>🗣️ Se présenter et simuler l'entretien complet</h2>

    <div class="callout" style="border-color:var(--rouge);background:#fef2f2">
      <strong>⚠️ La vérité sur cet entretien</strong><br>
      Le jury ne cherche pas le candidat qui sait tout. Il cherche celui qui <strong>comprend le métier</strong>,
      qui <strong>sait de quoi il parle</strong>, et qui <strong>ne se raconte pas d'histoires</strong>.
      Une présentation floue fait perdre l'entretien avant la première question de fond.
    </div>

    <!-- ── A. DÉROULÉ ── -->
    <div class="bloc">
      <div class="bt">⏱️ A. Le déroulé réel — ce qui t'attend</div>
      <p>L'entretien dure en général <strong>30 à 40 minutes</strong>. Voici son ordre réel. Il ne change presque jamais.</p>
      <div class="ps-etapes">
        <div class="ps-etape"><div class="num">1</div><div class="corps">
          <strong>L'accueil et la présentation</strong><br>
          « Présentez-vous. » C'est <em>toujours</em> la première question. Elle donne le ton de tout le reste.</div>
          <div class="duree">2 min</div></div>
        <div class="ps-etape"><div class="num">2</div><div class="corps">
          <strong>La motivation</strong><br>
          « Pourquoi voulez-vous être directeur ? » La question qui élimine le plus de candidats.</div>
          <div class="duree">5 min</div></div>
        <div class="ps-etape"><div class="num">3</div><div class="corps">
          <strong>Les mises en situation</strong><br>
          « Un parent vous agresse devant l'école. Que faites-vous ? » On évalue ta réaction, pas ta culture.</div>
          <div class="duree">15 min</div></div>
        <div class="ps-etape"><div class="num">4</div><div class="corps">
          <strong>Les questions de fond</strong><br>
          Juridique, pilotage, AESH, projet d'école, sécurité. Le directeur du jury creuse là où tu es faible.</div>
          <div class="duree">10 min</div></div>
        <div class="ps-etape"><div class="num">5</div><div class="corps">
          <strong>La clôture</strong><br>
          « Avez-vous quelque chose à ajouter ? » <strong>Ne réponds jamais non.</strong> C'est une dernière occasion.</div>
          <div class="duree">1 min</div></div>
      </div>
    </div>

    <!-- ── B. PRÉSENTATION ── -->
    <div class="bloc">
      <div class="bt">⚡ B. La présentation en 90 secondes — la structure en 5 blocs</div>
      <p>Ne raconte pas ta vie. <strong>90 secondes, cinq blocs, aucun mot inutile.</strong></p>
      <div class="ps-etapes">
        <div class="ps-etape"><div class="num">1</div><div class="corps">
          <strong>Qui tu es, en une phrase</strong><br>
          Nom, fonction, années d'ancienneté. Rien d'autre.</div><div class="duree">10 s</div></div>
        <div class="ps-etape"><div class="num">2</div><div class="corps">
          <strong>Le fil de ton parcours</strong><br>
          Une phrase qui relie tes expériences. Pas une liste : <em>un fil</em>.</div><div class="duree">20 s</div></div>
        <div class="ps-etape"><div class="num">3</div><div class="corps">
          <strong>Où tu en es aujourd'hui</strong><br>
          Ta classe, ton école, ce que tu y fais en plus de l'enseignement.</div><div class="duree">20 s</div></div>
        <div class="ps-etape"><div class="num">4</div><div class="corps">
          <strong>Le déclencheur</strong><br>
          <strong>Le bloc décisif.</strong> Une situation concrète que tu as vue, et qui t'a fait dire : « il faut quelqu'un ».</div><div class="duree">25 s</div></div>
        <div class="ps-etape"><div class="num">5</div><div class="corps">
          <strong>Ce que tu viens chercher</strong><br>
          Apprendre le métier. Pas un titre, pas une promotion.</div><div class="duree">15 s</div></div>
      </div>

      <div class="callout" style="border-color:var(--or);background:#fffbeb">
        <strong>💡 Le modèle rédigé avec TON parcours</strong> — à adapter, pas à réciter mot à mot
      </div>

      <div class="ps-pitch">
        <p><span class="ouverture">Je m'appelle Jacques Hassani Moustoifa.</span> Je suis professeur des écoles
        depuis 2016, mais je travaille à l'Éducation nationale depuis 2001 — j'ai commencé comme maître
        à l'école maternelle de Koungou.</p>
        <p>Mon parcours a un fil : <strong>les élèves qui ont le plus de mal.</strong> J'ai une licence de
        psychologie, une certification complémentaire en <strong>français langue seconde</strong> pour les
        élèves allophones, et j'ai passé <strong>six ans en SEGPA</strong> au collège de M'Tsamboro.</p>
        <p>Cette année, j'enseigne en <strong>CM1-CM2 à l'école La Rose, à Bandraboua</strong>, qui est en REP+.
        Je suis aussi <strong>référent harcèlement</strong>, et l'école a obtenu le label <strong>pHARe niveau 1</strong>.</p>
        <p>Si je candidate, c'est pour une raison précise. Dans une école, il y a des sujets qui n'avancent
        que si quelqu'un les porte : <strong>le suivi des AESH, la relation avec les familles, le projet d'école.</strong>
        J'ai vu des choses se faire parce qu'un directeur s'en occupait — et d'autres s'arrêter parce que
        personne ne s'en occupait.</p>
        <p><strong>Je veux être celui qui porte.</strong> Et je sais ce que je viens chercher :
        apprendre le métier, pas prendre un titre.</p>
      </div>

      <div class="callout" style="border-color:var(--vert);background:#f0fdf4">
        <strong>✅ Pourquoi ce modèle fonctionne</strong><br>
        Il tient en 75 secondes. Il y a <strong>trois preuves concrètes</strong> (psychologie, FLS, SEGPA) qui
        ne sont pas des diplômes décoratifs : elles disent quelque chose des élèves que tu sais prendre en charge.
        Et il finit sur une phrase <strong>humble et ambitieuse à la fois</strong>.
      </div>
    </div>

    <!-- ── C. MOTIVATION ── -->
    <div class="bloc">
      <div class="bt">🎯 C. « Pourquoi directeur ? » — la réponse en 3 cercles</div>
      <p>C'est <strong>la question qui élimine le plus</strong>. Une bonne réponse tient en trois cercles,
      dans cet ordre. Si tu en oublies un, ça s'entend.</p>
      <div class="ps-3c">
        <div class="ps-c c1"><div class="t">1. Le déclencheur</div>
          <p><strong>Une situation vécue, précise, datée.</strong> Pas une idée générale.
          « Dans mon école, le suivi des AESH était fait sur un cahier, et personne ne savait qui suivait qui. »</p></div>
        <div class="ps-c c2"><div class="t">2. La conviction</div>
          <p><strong>Ce que tu crois du métier.</strong> « Un directeur ne fait pas la classe aux autres :
          il crée les conditions pour que chacun puisse faire la sienne. »</p></div>
        <div class="ps-c c3"><div class="t">3. Le projet</div>
          <p><strong>Deux ou trois priorités concrètes.</strong> Pas dix. « D'abord la communication avec
          les familles. Ensuite le suivi des élèves à besoins particuliers. »</p></div>
      </div>
      <div class="callout" style="border-color:var(--bleu);background:#eff6ff">
        <strong>🔑 La règle des 3 cercles</strong><br>
        Le <strong>déclencheur</strong> prouve que tu es ancré dans le réel.<br>
        La <strong>conviction</strong> prouve que tu as réfléchi au métier.<br>
        Le <strong>projet</strong> prouve que tu ne viens pas les mains vides.<br>
        <strong>Les trois, ensemble, font une réponse crédible.</strong> Un seul des trois, et le jury sent le vide.
      </div>
    </div>

    <!-- ── D. CE QU'IL NE FAUT PAS DIRE ── -->
    <div class="bloc">
      <div class="bt">🚫 D. Ce qu'il ne faut <u>jamais</u> dire</div>
      <p>Chacune de ces phrases a déjà fait échouer des candidats. Le jury les connaît par cœur.</p>
      <div class="ps-non">
        <div><b>« Pour progresser dans ma carrière. »</b> → le jury entend : « je veux le poste, pas le travail ».</div>
        <div><b>« Parce que je m'ennuie dans ma classe. »</b> → le jury entend : « je fuis quelque chose ».</div>
        <div><b>« Pour avoir de l'autorité / être le chef. »</b> → un directeur a une <strong>autorité fonctionnelle</strong>, pas hiérarchique. C'est une erreur de qualification qui disqualifie.</div>
        <div><b>« Parce que personne ne veut le faire dans mon école. »</b> → tu te présentes comme un choix par défaut.</div>
        <div><b>« Pour la prime / l'indemnité. »</b> → même si c'est vrai, ce n'est jamais un argument.</div>
        <div><b>« Pour ne plus travailler avec tel collègue. »</b> → le jury comprend que tu régleras tes problèmes par la fuite.</div>
        <div><b>« Je ferai comme mon ancien directeur »</b> (ou « surtout pas comme lui ») → dans les deux cas, tu montres que tu n'as pas de projet propre.</div>
      </div>
    </div>

    <!-- ── E. ERREURS ── -->
    <div class="bloc">
      <div class="bt">⚠️ E. Les 5 erreurs qui font échouer</div>
      <div class="grid">
        <div class="card"><div class="ct">1️⃣ Parler de soi, jamais des élèves</div>
          <p>Toute réponse qui ne mentionne pas un élève, une famille ou une équipe est une réponse à côté.</p></div>
        <div class="card"><div class="ct">2️⃣ Ne pas connaître la loi Rilhac</div>
          <p><strong>Autorité fonctionnelle</strong> et non hiérarchique. Si tu confonds, le jury conclut que tu n'as pas lu le cadre.</p></div>
        <div class="card"><div class="ct">3️⃣ Confondre directeur et principal</div>
          <p>Un directeur d'école n'est pas le chef d'établissement d'un collège. Il n'a ni la même autorité ni les mêmes moyens.</p></div>
        <div class="card"><div class="ct">4️⃣ Rester dans le vague</div>
          <p>« Je veux fédérer », « créer du lien », « impulser une dynamique » : sans un seul exemple, c'est du vide. Le jury le note.</p></div>
        <div class="card"><div class="ct">5️⃣ Promettre l'impossible</div>
          <p>« Je réglerai le problème des remplacements. » Un directeur ne le peut pas. Promettre, c'est se décrédibiliser.</p></div>
      </div>
    </div>

    <!-- ── F. SIMULATEUR ── -->
    <div class="bloc">
      <div class="bt">🎤 F. La simulation complète — 5 étapes, comme le vrai entretien</div>
      <p>Cette simulation suit <strong>l'ordre réel</strong> de l'entretien. Une question tombe, tu réponds
      <strong>à voix haute</strong>, puis tu compares avec le modèle. <strong>Ne regarde le modèle qu'après avoir parlé.</strong></p>

      <div class="ps-sim">
        <div class="entete">
          <div>
            <div class="etape-courante" id="ps-etape-nom">Étape 1 / 5 — La présentation</div>
            <div style="font-size:.78rem;color:#94a3b8;margin-top:3px" id="ps-question-num">Question 1</div>
          </div>
          <div class="chrono" id="ps-chrono">1:30</div>
        </div>
        <div class="question" id="ps-question">Appuie sur « Démarrer » pour commencer la simulation.</div>
        <div class="barre">
          <button class="b1" onclick="psSuivant()">▶ Question suivante</button>
          <button class="b2" onclick="psChrono()">⏱️ Chrono</button>
          <button class="b3" onclick="psAide()">💡 Voir le modèle</button>
        </div>
        <div class="ps-aide" id="ps-aide"></div>
        <div class="ps-prog" id="ps-prog"></div>
      </div>

      <div class="callout" style="border-color:var(--bleu);background:#eff6ff">
        <strong>📱 Comment s'entraîner pour de vrai</strong><br>
        1. Réponds <strong>debout, à voix haute</strong> — jamais dans ta tête.<br>
        2. <strong>Enregistre-toi</strong> avec ton téléphone, puis réécoute : tu entendras tes hésitations.<br>
        3. Respecte le chrono : passé le temps, le jury t'arrête.<br>
        4. Demande à quelqu'un de te poser les questions <strong>sans regarder l'écran</strong>.
      </div>
    </div>

    <!-- ── G. GRILLE ── -->
    <div class="bloc">
      <div class="bt">📊 G. La grille d'auto-évaluation — note-toi après chaque passage</div>
      <table class="ps-grille">
        <tr><th style="width:26%">Critère</th><th>Ce que le jury observe</th><th style="width:12%">/5</th></tr>
        <tr><td><strong>Clarté</strong></td><td>Est-ce que je réponds à la question posée ? Est-ce que je me perds ?</td><td></td></tr>
        <tr><td><strong>Concret</strong></td><td>Est-ce que je donne au moins un exemple vécu, précis, daté ?</td><td></td></tr>
        <tr><td><strong>Posture</strong></td><td>Est-ce que je parle comme un futur directeur, sans autoritarisme ?</td><td></td></tr>
        <tr><td><strong>Cadre</strong></td><td>Est-ce que je distingue autorité fonctionnelle et hiérarchique ?</td><td></td></tr>
        <tr><td><strong>Élèves</strong></td><td>Est-ce que l'intérêt des élèves est présent dans ma réponse ?</td><td></td></tr>
      </table>
      <p><strong>Moins de 15/25 :</strong> refais la simulation. <strong>20/25 et plus :</strong> tu es prêt.</p>
    </div>

    <!-- ── H. CLÔTURE ── -->
    <div class="bloc">
      <div class="bt">🔚 H. La clôture — « Avez-vous quelque chose à ajouter ? »</div>
      <div class="callout" style="border-color:var(--rouge);background:#fef2f2">
        <strong>Ne réponds jamais « non ».</strong> C'est la dernière impression que le jury garde de toi.
      </div>
      <div class="ps-pitch">
        <p><span class="ouverture">Oui, une chose.</span> Je n'ai pas l'expérience du poste, je ne vais pas
        le prétendre. Mais j'ai passé vingt-quatre ans dans cette institution, dont six avec les élèves les
        plus en difficulté. Ce que je viens chercher, c'est d'apprendre le métier auprès de ceux qui le font —
        et je suis prêt à être évalué là-dessus.</p>
        <p><strong>Merci de votre écoute.</strong></p>
      </div>
      <div class="ps-3c">
        <div class="ps-c c1"><div class="t">Ne pas</div><p>Résumer tout l'entretien. Tu répéterais et tu perdrais en force.</p></div>
        <div class="ps-c c2"><div class="t">Ne pas</div><p>Ajouter une information que tu avais oubliée et qui change tout. C'est trop tard.</p></div>
        <div class="ps-c c3"><div class="t">Faire</div><p><strong>Une phrase de synthèse</strong> + <strong>une preuve d'humilité</strong> + <strong>un remerciement</strong>. C'est tout.</p></div>
      </div>
    </div>

    <div class="callout" style="border-color:var(--or);background:#fffbeb">
      <strong>🕋 Et le matin de l'entretien</strong><br>
      Relis seulement <strong>la présentation de 90 secondes</strong> et <strong>les 3 cercles</strong>. Pas tout le site.
      Arrive <strong>15 minutes avant</strong>. Emporte <strong>une copie de ta fiche de candidature</strong>.
      Et souviens-toi : un candidat qui dit « je ne sais pas, mais voilà comment je chercherais » est
      <strong>plus crédible</strong> qu'un candidat qui invente.
    </div>
  </section>
"""

anchor = "  <!-- ══════════ 21. TEXTES OFFICIELS ══════════ -->"
assert t.count(anchor) == 1, f"ancre section: {t.count(anchor)}"
t = t.replace(anchor, SECTION + "\n" + anchor)

# ═══════════════════════════════ 4. JS ═══════════════════════════════
JS = r"""
<script>
/* ══════════════════════════════════════════════════════════════════
   SIMULATION D'ENTRETIEN — section 20 (se présenter)
   ══════════════════════════════════════════════════════════════════ */
(function(){
  const ETAPES = [
    { nom: "La présentation", duree: 90, questions: [
      { q: "Présentez-vous en 90 secondes.",
        aide: "<b>Structure :</b> qui tu es (10 s) → le fil de ton parcours (20 s) → où tu en es aujourd'hui (20 s) → le déclencheur (25 s) → ce que tu viens chercher (15 s).<br><br><b>Ton fil :</b> psychologie + français langue seconde + six ans en SEGPA = « les élèves qui ont le plus de mal ».<br><br><b>Ton déclencheur :</b> un sujet qui n'avance que si quelqu'un le porte (AESH, familles, projet d'école).<br><br><b>Fin :</b> « apprendre le métier, pas prendre un titre »." },
      { q: "Qu'est-ce qu'un directeur d'école ? (attention : ce n'est pas un principal)",
        aide: "Un <b>professeur des écoles chargé de la direction</b>. Il a une <b>autorité fonctionnelle</b> — il organise, coordonne, anime — mais <b>pas d'autorité hiérarchique</b> sur ses collègues enseignants. Il est garant du fonctionnement, de la sécurité et de la mise en œuvre du projet d'école." },
      { q: "Quel est le fil conducteur de votre parcours ?",
        aide: "Ne récite pas ton CV. Trouve <b>une seule idée</b> qui relie tout : ici, la prise en charge des élèves les plus fragiles (psychologie, FLS pour allophones, SEGPA, REP+)." }
    ]},
    { nom: "La motivation", duree: 120, questions: [
      { q: "Pourquoi voulez-vous être directeur d'école ?",
        aide: "<b>Les 3 cercles, dans l'ordre :</b><br>1. <b>Le déclencheur</b> — une situation vécue, précise.<br>2. <b>La conviction</b> — « un directeur crée les conditions pour que chacun puisse faire sa classe ».<br>3. <b>Le projet</b> — 2 ou 3 priorités, pas dix.<br><br>⚠️ Jamais : « progresser », « m'ennuyer », « avoir de l'autorité », « personne ne veut le faire »." },
      { q: "Qu'est-ce qui vous manque pour être directeur dès demain ?",
        aide: "Réponds <b>honnêtement</b>. Un candidat qui dit « rien ne me manque » inquiète. Cite : la connaissance fine des procédures, la gestion budgétaire de la coopérative, la conduite de conseils. Puis : « c'est ce que j'attends de la formation et du tutorat »." },
      { q: "Pourquoi maintenant, et pas dans trois ans ?",
        aide: "Parce qu'une situation concrète s'est présentée <b>cette année</b> — dis laquelle. Et parce que la formation se fait <b>en poste</b>, pas avant." },
      { q: "Si vous n'êtes pas retenu cette année, que faites-vous ?",
        aide: "Surtout pas « je serai déçu ». Dis : <b>je continue à préparer</b>, je demande à suivre un directeur en observation, et je représenterai ma candidature. <b>Montre que tu restes engagé.</b>" }
    ]},
    { nom: "Les mises en situation", duree: 120, questions: [
      { q: "Un parent vous agresse verbalement devant l'école, devant les autres parents. Que faites-vous ?",
        aide: "Les <b>4 réflexes</b> : je <b>sécurise</b> (j'éloigne la personne, je protège les élèves) → j'<b>alerte</b> (IEN, et forces de l'ordre si nécessaire) → je <b>trace</b> (écrit daté, factuel, sans jugement) → je <b>protège</b> (l'équipe, les élèves, et moi).<br><br>⚠️ Ne réponds jamais « je le reçois dans mon bureau pour discuter » : on ne discute pas avec une agression." },
      { q: "Un enseignant refuse d'appliquer une décision du conseil des maîtres. Que faites-vous ?",
        aide: "Je <b>reparle</b> d'abord : comprendre le refus, entendre l'argument. Puis je <b>rappelle le cadre</b> : la décision a été prise collectivement. Enfin, si le refus persiste, j'<b>alerte l'IEN</b> — car <b>je n'ai pas de pouvoir hiérarchique</b>, donc je ne peux pas l'y contraindre. C'est la réponse qui prouve que tu connais la loi Rilhac." },
      { q: "Un élève vous dit qu'il est harcelé. Que faites-vous ?",
        aide: "Réponse <b>structurée</b> : je <b>reçois l'élève seul</b> et je le crois → je <b>ne le confronte pas</b> à l'auteur → j'<b>informe</b> la famille → je <b>réunis l'équipe</b> (enseignants, AESH, infirmière si présente) → je <b>mets en place une surveillance</b> des lieux et des temps non couverts → je <b>trace</b> tout → je <b>saisis</b> le protocole pHARe et je peux faire un <b>signalement</b>.<br><br>Tu es <b>référent harcèlement</b> : c'est ton point fort, utilise-le." },
      { q: "Vous arrivez dans une école où le directeur précédent est parti en conflit avec l'équipe. Par quoi commencez-vous ?",
        aide: "<b>Écouter avant d'agir.</b> Entretiens individuels avec chaque enseignant, puis un conseil des maîtres <b>sans ordre du jour lourd</b>. On ne réforme pas une équipe blessée en trois semaines. Et on ne critique jamais le prédécesseur devant l'équipe." }
    ]},
    { nom: "Les questions de fond", duree: 90, questions: [
      { q: "Que dit la loi Rilhac sur l'autorité du directeur d'école ?",
        aide: "La loi du <b>21 décembre 2021</b> (dite loi Rilhac) a créé la fonction de directeur d'école et conforté son rôle : il dispose d'une <b>autorité fonctionnelle</b> sur les personnels de l'école, <b>sans autorité hiérarchique</b> sur les enseignants. Le <b>décret 2023-777</b> en précise les missions et les conditions d'exercice." },
      { q: "Qu'est-ce qu'un élève à besoins éducatifs particuliers, et qui décide des aménagements ?",
        aide: "Un élève dont la scolarité demande des adaptations : handicap, trouble des apprentissages, allophonie, maladie.<br>Les aménagements se décident en <b>équipe éducative</b>, puis sont formalisés dans un <b>PPS</b> (si MDPH) ou un <b>PPRE</b>/<b>PAP</b>. <b>Toi, directeur, tu réunis et tu formalises</b> — tu ne décides pas seul." },
      { q: "Comment fonctionne la coopérative scolaire ?",
        aide: "C'est une <b>association</b> (souvent OCCE) distincte de l'école. Elle a un <b>compte bancaire propre</b>, un <b>budget voté en conseil d'école</b>, et une <b>comptabilité tenue</b>. Elle sert aux projets pédagogiques — <b>jamais</b> à financer des dépenses de fonctionnement de l'école. Le directeur en est le responsable légal le plus souvent." },
      { q: "Quelles sont vos obligations en matière de sécurité de l'école ?",
        aide: "Le directeur est <b>responsable de la sécurité</b> des élèves et des personnels. Cela inclut : le <b>registre de sécurité</b>, les <b>exercices d'évacuation</b> (au moins deux par an, dont un incendie), le <b>PPMS</b> (plan particulier de mise en sûreté), le contrôle des <b>équipements</b> et des <b>issues</b>, et la <b>surveillance des temps non couverts</b>." },
      { q: "Comment élabore-t-on et fait-on vivre le projet d'école ?",
        aide: "Il se construit <b>collectivement</b> : diagnostic partagé → axes prioritaires (3 maximum) → actions et indicateurs → <b>validation par l'IEN</b> → mise en œuvre sur 3 ans avec un <b>bilan annuel</b>. Le directeur l'<b>anime</b>, il ne l'écrit pas seul." }
    ]},
    { nom: "La clôture", duree: 30, questions: [
      { q: "Avez-vous quelque chose à ajouter ?",
        aide: "<b>Ne dis jamais non.</b> Une phrase de synthèse + une preuve d'humilité + un remerciement.<br><br>Modèle : « Oui. Je n'ai pas l'expérience du poste et je ne vais pas le prétendre. Mais j'ai vingt-quatre ans dans cette institution, dont six avec les élèves les plus en difficulté. Ce que je viens chercher, c'est d'apprendre le métier auprès de ceux qui le font. Merci de votre écoute. »" }
    ]}
  ];

  let ie = 0, iq = 0, tmr = null, reste = 0;

  const $ = id => document.getElementById(id);

  function affiche(){
    const e = ETAPES[ie], q = e.questions[iq];
    $("ps-etape-nom").textContent = `Étape ${ie+1} / ${ETAPES.length} — ${e.nom}`;
    $("ps-question-num").textContent = `Question ${iq+1} sur ${e.questions.length}`;
    $("ps-question").textContent = q.q;
    $("ps-aide").innerHTML = q.aide;
    $("ps-aide").classList.remove("on");
    reste = e.duree; stopChrono(); afficheChrono();
    // barre de progression
    let h = "";
    ETAPES.forEach((s, i) => {
      h += `<i class="${i < ie ? 'fait' : (i === ie ? 'now' : '')}"></i>`;
    });
    $("ps-prog").innerHTML = h;
  }

  function afficheChrono(){
    const m = Math.floor(reste/60), s = reste % 60;
    const el = $("ps-chrono");
    el.textContent = m + ":" + String(s).padStart(2,"0");
    el.classList.toggle("alerte", reste <= 10 && reste > 0);
  }

  function tick(){
    reste--;
    if (reste < 0) { stopChrono(); return; }
    afficheChrono();
  }

  function stopChrono(){ if (tmr) { clearInterval(tmr); tmr = null; } }

  window.psSuivant = function(){
    if (iq + 1 < ETAPES[ie].questions.length) { iq++; }
    else if (ie + 1 < ETAPES.length) { ie++; iq = 0; }
    else {
      ie = 0; iq = 0;
      $("ps-question").textContent = "Simulation terminée. Recommence : la deuxième fois est toujours meilleure.";
      $("ps-aide").classList.remove("on");
      stopChrono(); return;
    }
    affiche();
  };

  window.psChrono = function(){
    if (tmr) { stopChrono(); return; }
    if (reste <= 0) { reste = ETAPES[ie].duree; }
    tmr = setInterval(tick, 1000);
  };

  window.psAide = function(){
    $("ps-aide").classList.toggle("on");
  };

  affiche();
  $("ps-question").textContent = "Prêt ? Appuie sur « ▶ Question suivante » pour commencer.";
})();
</script>
"""

assert t.count("</body>") == 1, f"body: {t.count('</body>')}"
t = t.replace("</body>", JS + "\n</body>")

P.write_text(t, encoding="utf-8")
print(f"  ✅ index.html : {orig_len//1024} Ko → {len(t)//1024} Ko  (+{(len(t)-orig_len)//1024} Ko)")
print(f"  section #oral insérée · nav renumérotée · CSS + JS ajoutés")
