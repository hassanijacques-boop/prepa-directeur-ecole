#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige et complete la partie 'textes officiels' du site :
   - corrige l'URL du decret 2023-777
   - ajoute le decret 2022-541 (decharges) et le decret 2026-821 (le plus recent)
   - ajoute un bloc 'la chaine des textes' dans la section Rilhac
"""

import pathlib

P = pathlib.Path("/workspace/prepa-directeur/index.html")
t = P.read_text(encoding="utf-8")
n0 = len(t)
modifs = []

# ─── 1. NAV + plan : ne plus figer 2023-777 seul ───
for vieux, neuf in [
    ("Loi Rilhac + décret 2023-777", "Loi Rilhac + ses décrets"),
    ("Apprendre la loi Rilhac et le décret 2023-777.", "Apprendre la loi Rilhac et ses décrets d'application."),
]:
    c = t.count(vieux)
    t = t.replace(vieux, neuf)
    modifs.append(f"«{vieux[:38]}…» → {c} remplacement(s)")

# ─── 2. Corriger l'URL du décret 2023-777 ───
old_url = "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047962452"
new_url = "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047968636"
c = t.count(old_url)
t = t.replace(old_url, new_url)
modifs.append(f"URL 2023-777 corrigée : {c} occurrence(s)")

# ─── 3. Insérer les 2 décrets manquants après le bloc 2023-777 ───
ancre = """      <div class="url">https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047968636</div>
    </div>"""
assert t.count(ancre) == 1, f"ancre decrets: {t.count(ancre)}"

NOUVEAUX = ancre + """

    <div class="ref">
      <div class="rt">Décret n° 2022-541 du 13 avril 2022 — régime des décharges de service des directeurs d'école</div>
      <div class="ref-meta"><span class="tag loi">DÉCRET</span><span class="tag bo">JORF</span></div>
      <div class="rd">⭐ <strong>Le texte des DÉCHARGES.</strong> Il fixe le temps dont dispose le directeur
        pour exercer sa fonction autrement qu'en classe, selon la taille de l'école.
        Pris en application de l'article <strong>L. 411-2</strong> du code de l'éducation.
        <br><em>C'est la réponse à « combien d'heures de décharge pour combien de classes ? »</em></div>
      <div class="url">https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045554668</div>
    </div>

    <div class="ref" style="border-left:4px solid #c0392b">
      <div class="rt">🔥 Décret n° 2026-821 du 25 août 2026 — modifie le régime des décharges</div>
      <div class="ref-meta"><span class="tag loi">DÉCRET</span><span class="tag bo">LE PLUS RÉCENT</span></div>
      <div class="rd">⚠️ <strong>Si le jury demande « quel est le dernier texte ? », c'est CELUI-LÀ.</strong><br>
        Publié le <strong>25 août 2026</strong>, il <strong>modifie le décret n° 2022-541 du 13 avril 2022</strong>
        et apporte une évolution ciblée au régime de <strong>décharge d'enseignement</strong> des directeurs
        d'école maternelle, élémentaire et primaire : de <strong>nouvelles possibilités de décharges de service</strong>.
        <br><em>Visas : article L. 411-2 du code de l'éducation · décret n° 2008-775 du 30 juillet 2008.</em></div>
      <div class="url">https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054750205</div>
    </div>"""

t = t.replace(ancre, NOUVEAUX)
modifs.append("décrets 2022-541 et 2026-821 ajoutés")

# ─── 4. Bloc « la chaîne des textes » à la fin de la section Rilhac ───
m = t.find('id="rilhac"')
fin = t.find("</section>", m)
assert m > 0 and fin > m

CHRONO = """
      <div class="bloc" style="margin-top:20px">
        <div class="bt">🧭 La chaîne complète des textes — les 5 références à citer</div>
        <p>La loi Rilhac seule ne suffit pas : elle a besoin de <strong>décrets d'application</strong>.
        Voilà l'ordre, et ce que fait chacun. <strong>Si tu ne retiens qu'une chose : cite le dernier.</strong></p>

        <table class="ps-grille">
          <tr><th style="width:8%">#</th><th style="width:38%">Le texte</th><th>Ce qu'il fait</th></tr>
          <tr><td><strong>1</strong></td>
              <td><strong>Loi n° 2021-1716 du 21 décembre 2021</strong><br><em>loi Rilhac</em></td>
              <td><strong>Crée la fonction</strong> de directrice ou directeur d'école et fonde l'<strong>autorité fonctionnelle</strong>.</td></tr>
          <tr><td><strong>2</strong></td>
              <td><strong>Décret n° 2022-541 du 13 avril 2022</strong></td>
              <td>Fixe le <strong>régime des décharges de service</strong> : le temps libéré pour diriger, selon la taille de l'école.</td></tr>
          <tr><td><strong>3</strong></td>
              <td><strong>Décret n° 2023-777 du 14 août 2023</strong></td>
              <td>Précise les <strong>missions</strong> du directeur, en application de l'article L. 411-2.</td></tr>
          <tr><td><strong>4</strong></td>
              <td><strong>Circulaire BO 2024 Hebdo 15</strong><br><em>MENH2407075C</em></td>
              <td>Fixe les <strong>modalités d'évaluation</strong> des directeurs (article 14 du décret de 2023).</td></tr>
          <tr style="background:#fef2f2"><td><strong>5</strong></td>
              <td><strong>Décret n° 2026-821 du 25 août 2026</strong> 🔥</td>
              <td><strong>Modifie les décharges</strong> : nouvelles possibilités de décharge d'enseignement. <strong>Le texte le plus récent.</strong></td></tr>
        </table>

        <div class="callout" style="border-color:var(--rouge);background:#fef2f2">
          <strong>⚠️ La correction à ne pas rater</strong><br>
          Jusqu'ici ce site ne citait que le décret de <strong>2023</strong>. Or il existe désormais un texte
          <strong>plus récent</strong> : le <strong>décret n° 2026-821 du 25 août 2026</strong>, qui touche aux
          <strong>décharges de service</strong>.<br><br>
          <strong>Si le jury dit « le décret de 2026 » ou « les décharges », tu dois savoir de quoi il parle.</strong>
        </div>

        <div class="callout" style="border-color:var(--bleu);background:#eff6ff">
          <strong>💬 Ce que tu réponds si on te demande le dernier texte</strong><br>
          « Le dernier texte, c'est le <strong>décret n° 2026-821 du 25 août 2026</strong>. Il modifie le décret de
          2022 sur les <strong>décharges de service</strong> des directeurs d'école et ouvre de nouvelles possibilités
          de décharge. La loi Rilhac de 2021 a créé la fonction ; le décret de 2023 en a précisé les
          <strong>missions</strong> ; celui de 2026 ajuste les <strong>moyens en temps</strong>. »
        </div>
      </div>
"""
t = t[:fin] + CHRONO + "\n    " + t[fin:]
modifs.append("bloc « chaîne des textes » ajouté dans la section Rilhac")

# ─── 5. Fiche de références : compléter la ligne ───
vieux_ref = "La fonction de directeur</td><td>Loi Rilhac 2021-1716 + décret 2023-777"
if vieux_ref in t:
    t = t.replace(vieux_ref, "La fonction de directeur</td><td>Loi Rilhac 2021-1716 + décrets 2022-541, 2023-777 et <strong>2026-821</strong>")
    modifs.append("fiche de références complétée")

P.write_text(t, encoding="utf-8")
print(f"  ✅ index.html : {n0//1024} Ko → {len(t)//1024} Ko")
for m in modifs:
    print("   ·", m)
