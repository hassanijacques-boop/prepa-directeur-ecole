#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integre dans prepa-directeur une section 22 « Laïcité » :
   briefing (3 principes, 3 points, qui/quoi, 5 gestes, 7 textes)
   + les 20 cas concrets en accordéon (clic pour révéler).
   Le CSS des deux documents est RE-ÉCRIT sous #laicite pour ne pas casser le site."""

import pathlib, re

D = pathlib.Path("/workspace/prepa-directeur")
HTML_SITE = D / "index.html"

t = HTML_SITE.read_text(encoding="utf-8")
n0 = len(t)


# ═══════════ 1. Extraire style + corps des 2 documents ═══════════
def extraire(fichier):
    s = (D / fichier).read_text(encoding="utf-8")
    css = "\n".join(re.findall(r"<style>(.*?)</style>", s, re.S))
    corps = re.search(r"<body>(.*?)</body>", s, re.S).group(1)
    # retirer le bloc de couverture (le site a le sien)
    # suppression PRECISE de l'en-tete de couverture : de <div class="cov"> jusqu'au </p> puis </div>
    corps = re.sub(r'<div class="cov">.*?</p>\s*</div>', "", corps, count=1, flags=re.S)
    return css, corps


css1, corps1 = extraire("laicite.html")
css2, corps2 = extraire("laicite_qr.html")

# re-titrer les h2 du briefing pour qu'ils s'intègrent dans la section
corps1 = corps1.replace("<h2>Les 3 principes de la laïcité</h2>",
                        "<h3 class='lz'>① Les 3 principes de la laïcité</h3>")
corps1 = corps1.replace("<h2>⭐ Les 3 points de la NEUTRALITÉ de l'enseignant</h2>",
                        "<h3 class='lz'>② Les 3 points de la neutralité de l'enseignant</h3>")
corps1 = corps1.replace("<h2>Qui est soumis à quoi — la question que peu de candidats savent traiter</h2>",
                        "<h3 class='lz'>③ Qui est soumis à quoi</h3>")
corps1 = corps1.replace("<h2>Ce que fait le directeur — 5 gestes concrets</h2>",
                        "<h3 class='lz'>④ Ce que fait le directeur — 5 gestes</h3>")
corps1 = corps1.replace("<h2>8 situations qu'il peut te faire traiter</h2>",
                        "<h3 class='lz'>⑤ 8 situations à traiter</h3>")
corps1 = corps1.replace("<h2>Les 5 erreurs qui feraient perdre l'avis</h2>",
                        "<h3 class='lz'>⑥ Les 5 erreurs à ne pas commettre</h3>")
corps1 = corps1.replace("<h2>Les 7 textes à savoir citer</h2>",
                        "<h3 class='lz'>⑦ Les 7 textes à savoir citer</h3>")
corps2 = corps2.replace("<h2 style=\"color:#12294d\">Le tableau de synthèse — à retenir en premier</h2>",
                        "<h3 class='lz'>⑧ Le tableau de synthèse — à retenir en premier</h3>")
corps2 = re.sub(r'<h2 style="color:(#[0-9a-f]{6});border-bottom-color:#[0-9a-f]{6}">([^<]+)</h2>',
                r"<h3 class='lz' style='color:\1'>\2</h3>", corps2)

# ═══════════ 2. Ré-écrire le CSS sous #laicite ═══════════
def scoper(css):
    css = re.sub(r"@page\s*\{[^}]*\}", "", css)          # pas de @page dans le site
    css = re.sub(r"@keyframes[^{]*\{(?:[^{}]|\{[^}]*\})*\}", "", css)
    sortie = []
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        sel, decl = m.group(1).strip(), m.group(2).strip()
        if not sel or sel.startswith("@"):
            continue
        if sel == "*" or sel.startswith("*"):
            continue
        parties = []
        for s in sel.split(","):
            s = s.strip()
            if not s:
                continue
            if s == "body":
                parties.append("#laicite")
            elif s.startswith("html") or s.startswith(":root"):
                continue
            else:
                parties.append("#laicite " + s)
        if parties:
            sortie.append(", ".join(parties) + " { " + decl + " }")
    return "\n".join(sortie)


CSS_SCOPED = scoper(css1) + "\n" + scoper(css2)

# ═══════════ 3. CSS propre au site (accordéon + titres) ═══════════
CSS_SITE = """
  /* ════════ SECTION 22 — LAÏCITÉ ════════ */
  #laicite h3.lz { font-size: .86rem; color: #2563eb; letter-spacing: .5px;
    text-transform: uppercase; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px;
    margin: 20px 0 9px; page-break-after: avoid; }
  #laicite .qr { cursor: pointer; transition: .15s; }
  #laicite .qr:hover { border-color: #93c5fd; }
  #laicite .qr .rep, #laicite .qr ul, #laicite .qr .conf,
  #laicite .qr .txtx, #laicite .qr .lab { display: none; }
  #laicite .qr.open .rep, #laicite .qr.open .lab,
  #laicite .qr.open ul, #laicite .qr.open .conf,
  #laicite .qr.open .txtx { display: block; }
  #laicite .qr-hint { font-size: .72rem; font-weight: 700; color: #2563eb;
    margin-top: 2px; }
  #laicite .qr.open .qr-hint { display: none; }
  #laicite .lz-barre { display: flex; gap: 8px; flex-wrap: wrap; margin: 10px 0 14px; }
  #laicite .lz-barre button { border: none; border-radius: 9px; padding: 9px 15px;
    font-weight: 800; font-size: .83rem; cursor: pointer; font-family: inherit;
    background: #12294d; color: #fff; }
  #laicite .lz-barre button.alt { background: #eef2f7; color: #12294d; }
"""

# ═══════════ 4. Section HTML ═══════════
SECTION = f"""
  <!-- ══════════ 22. LAÏCITÉ ET NEUTRALITÉ ══════════ -->
  <section id="laicite">
    <div class="kicker">Section 22 — La question la plus sensible de l'entretien</div>
    <h2>🕊️ Laïcité et neutralité — le briefing et les 20 cas concrets</h2>

    <div class="callout" style="border-color:var(--rouge);background:#fef2f2">
      <strong>⚠️ La distinction qui gouverne tout</strong><br>
      <strong>Les élèves</strong> relèvent de la <strong>loi de 2004</strong> : seuls les signes <strong>ostensibles</strong> sont interdits.<br>
      <strong>Les adultes de l'école</strong> relèvent de la <strong>neutralité des agents publics</strong> : <strong>aucun signe</strong>, sans exception.<br>
      <strong>Les parents</strong> ne relèvent d'<strong>aucune</strong> interdiction : ce sont des usagers.<br><br>
      <strong>Confondre ces trois régimes, c'est la faute la plus fréquente — et celle qui fait le plus de dégâts.</strong>
    </div>

    {corps1}

    <h3 class="lz" style="margin-top:26px">⑧ Les 20 cas concrets — clique sur une question pour voir la réponse</h3>
    <div class="lz-barre">
      <button onclick="lzTout(true)">Tout déplier</button>
      <button class="alt" onclick="lzTout(false)">Tout replier</button>
      <button class="alt" onclick="lzHasard()">🎲 Une question au hasard</button>
    </div>

    {corps2}

  </section>
"""

# ═══════════ 5. Insérer dans le site ═══════════
# nav : ajouter #laicite en 22 et décaler carte/textes
nav_old = """      <a href="#preliminaire"><span class="n">21</span> 🤝 L'entretien préliminaire avec l'IEN</a>
      <a href="#carte"><span class="n">22</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">23</span> 📚 Textes officiels &amp; liens directs</a>"""
nav_new = """      <a href="#preliminaire"><span class="n">21</span> 🤝 L'entretien préliminaire avec l'IEN</a>
      <a href="#laicite"><span class="n">22</span> 🕊️ Laïcité et neutralité</a>
      <a href="#carte"><span class="n">23</span> 🧭 La carte mentale des 4 réflexes</a>
      <a href="#textes"><span class="n">24</span> 📚 Textes officiels &amp; liens directs</a>"""
assert t.count(nav_old) == 1, f"nav: {t.count(nav_old)}"
t = t.replace(nav_old, nav_new)

# css
t = t.replace("</style>", CSS_SITE + "\n" + CSS_SCOPED + "\n</style>", 1)

# section : avant les textes officiels
anchor = "  <!-- ══════════ 23. TEXTES OFFICIELS ══════════ -->"
assert t.count(anchor) == 1, f"ancre: {t.count(anchor)}"
t = t.replace(anchor, SECTION + "\n  <!-- ══════════ 24. TEXTES OFFICIELS ══════════ -->")

# js accordéon
JS = r"""
<script>
/* ══════════ LAÏCITÉ — accordéon des 20 cas ══════════ */
(function(){
  var cartes = document.querySelectorAll('#laicite .qr');
  cartes.forEach(function(q){
    var h = document.createElement('div');
    h.className = 'qr-hint';
    h.textContent = '\uD83D\uDC46 Clique pour voir la réponse';
    q.appendChild(h);
    q.addEventListener('click', function(){ q.classList.toggle('open'); });
  });
  window.lzTout = function(ouvrir){
    document.querySelectorAll('#laicite .qr').forEach(function(q){
      q.classList.toggle('open', ouvrir);
    });
  };
  window.lzHasard = function(){
    var r = document.querySelectorAll('#laicite .qr');
    if (!r.length) return;
    var c = r[Math.floor(Math.random() * r.length)];
    c.classList.add('open');
    c.scrollIntoView({behavior:'smooth', block:'center'});
  };
})();
</script>
"""
assert t.count("</body>") == 1
t = t.replace("</body>", JS + "\n</body>")

HTML_SITE.write_text(t, encoding="utf-8")
print(f"  ✅ index.html : {n0//1024} Ko → {len(t)//1024} Ko  (+{(len(t)-n0)//1024} Ko)")
print(f"  CSS scopé : {len(CSS_SCOPED)//1024} Ko · accordéon : {t.count('class=\"qr\"')} cartes")
