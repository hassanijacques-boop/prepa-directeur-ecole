#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integre dans le site la section 23 « Procédures » + les 4 modèles copiables."""

import pathlib, html as H, sys

D = pathlib.Path("/workspace/prepa-directeur")
sys.path.insert(0, str(D))
from procedure_data import ETAPES, CIRCUITS, DOCS, QUI, CAS_CM2, MODELES, SEMAINE, PAS

P = D / "index.html"
t = P.read_text(encoding="utf-8")
n0 = len(t)

# ─── contenus ───
etapes = "".join(
    '<div class="ps-etape"><div class="num">%s</div><div class="corps">'
    '<strong>%s</strong><br>%s</div><div class="duree">%s</div></div>' % (n, ttl, d, q)
    for n, ttl, d, q, w in ETAPES)

circuits = "".join(
    '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (a, b, c, d)
    for a, b, c, d in CIRCUITS)

docs = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (a, b, c) for a, b, c in DOCS)
qui = "".join('<tr><td style="width:26%%"><b>%s</b></td><td>%s</td></tr>' % (a, b) for a, b in QUI)
cas = "".join('<tr><td style="width:48%%">%s</td><td>%s</td></tr>' % (a, b) for a, b in CAS_CM2)
pas = "".join('<tr><td style="width:40%%">❌ %s</td><td>%s</td></tr>' % (a, b) for a, b in PAS)
sem = "".join("<li>%s</li>" % x for x in SEMAINE)

modeles = ""
for num, titre, texte in MODELES:
    modeles += ('<div class="mdl"><div class="mdl-h"><span class="mdl-t">Modèle %s — %s</span>'
                '<button class="mdl-b" onclick="mdlCopier(this)">📋 Copier</button></div>'
                '<pre class="mdl-pre">%s</pre></div>' % (num, titre, H.escape(texte)))

SECTION = """
  <!-- ══════════ 23. PROCÉDURES — ÉLÈVE EN GRANDE DIFFICULTÉ ══════════ -->
  <section id="procedure">
    <div class="kicker">Section 23 — Les procédures que le directeur doit connaître</div>
    <h2>🆘 Un élève en grande difficulté — de l'alerte à la MDPH</h2>

    <div class="callout" style="border-color:var(--rouge);background:#fef2f2">
      <strong>⚠️ Le mot « signalement » envoie dans le mauvais circuit</strong><br>
      « Signalement » = <strong>protection de l'enfance</strong> (danger). Ici, il s'agit d'une
      <strong>saisine de la MDPH</strong> et/ou d'un <strong>dossier CDOEA</strong>.
      <strong>Ce n'est pas la même porte, ni les mêmes interlocuteurs.</strong>
    </div>

    <div class="bloc">
      <div class="bt">🔀 A. Les 3 « signalements » — lequel est le bon ?</div>
      <table class="ps-grille">
        <tr><th>Type</th><th>Situation</th><th>Circuit</th><th>Ici ?</th></tr>
        __CIRCUITS__
      </table>
    </div>

    <div class="bloc">
      <div class="bt">📋 B. La procédure en 8 étapes</div>
      <div class="ps-etapes">__ETAPES__</div>
      <div class="callout" style="border-color:var(--bleu);background:#eff6ff">
        <strong>⭐ Le point que presque personne ne connaît</strong><br>
        L'<strong>enseignant référent ne se saisit pas directement</strong>. Il intervient
        <strong>quand un dossier MDPH est en cours</strong>, pour convoquer l'<strong>ESS</strong>
        et suivre le <strong>PPS</strong>.<br>
        → <strong>Sans MDPH déposée par la famille, il n'y a pas d'enseignant référent à convoquer.</strong>
      </div>
    </div>

    <div class="bloc">
      <div class="bt">👥 C. Qui fait quoi</div>
      <table class="ps-grille">__QUI__</table>
    </div>

    <div class="bloc">
      <div class="bt">📄 D. Les documents — qui sert à quoi</div>
      <table class="ps-grille">
        <tr><th style="width:18%">Document</th><th>Pour qui</th><th style="width:28%">Qui le décide</th></tr>
        __DOCS__
      </table>
    </div>

    <div class="bloc">
      <div class="bt">🚨 E. Le cas d'un élève de CM2 à niveau CP — il y a urgence</div>
      <div class="callout" style="border-color:var(--or);background:#fffbeb">
        <strong>Un élève de CM2 qui lit au niveau CP, avec des difficultés depuis le CP, n'est pas
        « en difficulté » : c'est un élève qu'on n'a pas réussi à faire entrer dans la lecture.</strong><br>
        Il entre au collège dans quelques mois. <strong>Si rien n'est fait maintenant, le dossier n'existera pas.</strong>
      </div>
      <p><strong>Trois hypothèses — trois destinations différentes :</strong></p>
      <table class="ps-grille">__CAS__</table>
      <div class="callout" style="border-color:var(--rouge);background:#fef2f2">
        <strong>⚠️ Deux dossiers EN PARALLÈLE, pas l'un après l'autre</strong><br>
        <strong>1.</strong> L'<strong>équipe éducative tout de suite</strong> → PPRE, RASED, information MDPH.<br>
        <strong>2.</strong> Le <strong>dossier CDOEA dès maintenant</strong> : les dossiers de pré-orientation
        SEGPA se préparent <strong>au premier trimestre</strong> — et il est en CM2.
      </div>
      <div class="bt" style="margin-top:14px">✅ Les 5 gestes du directeur, cette semaine</div>
      <ul>__SEM__</ul>
    </div>

    <div class="bloc">
      <div class="bt">🚫 F. Ce que ce n'est pas</div>
      <table class="ps-grille">__PAS__</table>
    </div>

    <div class="bloc">
      <div class="bt">✉️ G. Les 4 modèles prêts à copier</div>
      <p>Clique sur <strong>📋 Copier</strong>, puis colle dans ton traitement de texte.
      <strong>Les champs entre <code>{ }</code> sont à remplacer.</strong></p>
      __MODELES__
    </div>

    <div class="callout" style="border-color:var(--or);background:#fffbeb">
      <strong>📌 Et à Mayotte</strong><br>
      <strong>MDPH de Mayotte</strong> — dossier déposé <strong>par la famille</strong>, avec le GEVA-Sco de l'école.<br>
      <strong>CDOEA</strong> — commission d'orientation vers les enseignements adaptés, dossier <strong>scolaire</strong>.<br>
      → <strong>Passe par la circonscription (IEN)</strong> pour les formulaires à jour : c'est lui qui les a.
    </div>
  </section>
"""

SECTION = (SECTION.replace("__CIRCUITS__", circuits).replace("__ETAPES__", etapes)
                  .replace("__QUI__", qui).replace("__DOCS__", docs)
                  .replace("__CAS__", cas).replace("__SEM__", sem)
                  .replace("__PAS__", pas).replace("__MODELES__", modeles))

# ─── CSS ───
CSS = """
  /* ════════ SECTION 23 — PROCÉDURES ════════ */
  #procedure .mdl { margin: 12px 0 18px; }
  #procedure .mdl-h { display: flex; justify-content: space-between; align-items: center;
    gap: 10px; background: #12294d; border-radius: 9px 9px 0 0; padding: 8px 13px; }
  #procedure .mdl-t { color: #fff; font-weight: 800; font-size: .79rem; }
  #procedure .mdl-b { border: none; border-radius: 6px; padding: 5px 12px; cursor: pointer;
    font-family: inherit; font-weight: 800; font-size: .74rem; background: #2563eb; color: #fff; }
  #procedure .mdl-b.copie { background: #1a7a4a; }
  #procedure .mdl-pre { margin: 0; background: #fbfcfe; border: 1px solid #cbd5e1;
    border-top: none; border-radius: 0 0 9px 9px; padding: 12px 14px; font-size: .72rem;
    line-height: 1.5; white-space: pre-wrap; overflow-x: auto;
    font-family: "DejaVu Sans Mono", Consolas, monospace; color: #1c2331; }
  #procedure ul li { font-size: .87rem; margin-bottom: 5px; }
"""

# ─── insertion ───
nav_old = """      <a href="#laicite"><span class="n">22</span> 🕊️ Laïcité et neutralité</a>
      <a href="#carte"><span class="n">23</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">24</span> 📚 Textes officiels &amp; liens directs</a>"""
nav_new = """      <a href="#laicite"><span class="n">22</span> 🕊️ Laïcité et neutralité</a>
      <a href="#procedure"><span class="n">23</span> 🆘 Procédures : élève en difficulté</a>
      <a href="#carte"><span class="n">24</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">25</span> 📚 Textes officiels &amp; liens directs</a>"""
assert t.count(nav_old) == 1, "nav"
t = t.replace(nav_old, nav_new)

t = t.replace("</style>", CSS + "</style>", 1)

anchor = "  <!-- ══════════ 24. TEXTES OFFICIELS ══════════ -->"
assert t.count(anchor) == 1, "ancre"
t = t.replace(anchor, SECTION + "\n  <!-- ══════════ 25. TEXTES OFFICIELS ══════════ -->")

JS = r"""
<script>
/* ══════════ PROCÉDURES — copier un modèle ══════════ */
function mdlCopier(btn){
  var pre = btn.closest('.mdl').querySelector('.mdl-pre');
  var txt = pre.innerText;
  var fin = function(){ btn.textContent = '✅ Copié'; btn.classList.add('copie');
    setTimeout(function(){ btn.textContent = '📋 Copier'; btn.classList.remove('copie'); }, 1800); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(txt).then(fin).catch(function(){ mdlFallback(pre, fin); });
  } else { mdlFallback(pre, fin); }
}
function mdlFallback(pre, fin){
  var r = document.createRange(); r.selectNodeContents(pre);
  var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  try { document.execCommand('copy'); fin(); } catch(e){ alert('Sélectionne le texte à la main.'); }
  s.removeAllRanges();
}
</script>
"""
assert t.count("</body>") == 1
t = t.replace("</body>", JS + "\n</body>")

P.write_text(t, encoding="utf-8")
print("  ✅ index.html : %d Ko → %d Ko (+%d Ko)" % (n0 // 1024, len(t) // 1024, (len(t) - n0) // 1024))
print("  modèles : %d · étapes : %d" % (len(MODELES), len(ETAPES)))
