# -*- coding: utf-8 -*-
"""Contenus partagés : procédure « élève en grande difficulté » (MDPH / RASED / CDOEA).
Utilisé par le PDF et par l'intégration dans le site."""

# ─── les 8 étapes ───
ETAPES = [
    ("1", "DOCUMENTER",
     "Évaluations, productions d'élève, comparaison avec les attendus de fin de cycle, <b>historique depuis le CP</b>.",
     "L'enseignant",
     "Sans traces écrites, aucun dossier ne tient."),
    ("2", "INFORMER ET ASSOCIER LES PARENTS",
     "Rendez-vous, explication claire, écoute. <b>Rien ne se fait sans eux.</b>",
     "Le directeur",
     "C'est la famille qui dépose la MDPH — pas l'école."),
    ("3", "AMÉNAGER EN CLASSE",
     "Différenciation, PPRE. C'est la réponse de droit commun, et elle doit <b>exister avant</b> tout dossier.",
     "L'enseignant",
     "Un dossier MDPH sans aménagement préalable est incomplet."),
    ("4", "RÉUNIR L'ÉQUIPE ÉDUCATIVE",
     "⭐ <b>C'est le directeur qui la convoque.</b> Parents, enseignant, RASED, psychologue scolaire, médecin scolaire si besoin.",
     "Le directeur",
     "C'est le pivot de toute la procédure."),
    ("5", "DÉCIDER EN ÉQUIPE ÉDUCATIVE",
     "PPRE renforcé · saisine du RASED · <b>et si suspicion de trouble : informer les parents de leur droit de saisir la MDPH</b>.",
     "L'équipe",
     "On informe d'un droit — on ne l'impose pas."),
    ("6", "LES PARENTS DÉPOSENT LA MDPH",
     "Formulaire MDPH + certificat médical + <b>GEVA-Sco</b> rempli par l'école.",
     "Les parents",
     "L'école ne peut pas déposer à leur place."),
    ("7", "LA MDPH ÉVALUE ET NOTIFIE",
     "PPS, AESH, ULIS, matériel pédagogique adapté…",
     "La MDPH",
     "Délais longs : anticiper."),
    ("8", "L'ENSEIGNANT RÉFÉRENT CONVOQUE L'ESS",
     "L'<b>équipe de suivi de la scolarisation</b> : c'est là qu'il voit l'élève et suit le PPS.",
     "L'enseignant référent",
     "⭐ Il n'intervient qu'APRÈS la MDPH."),
]

# ─── les 3 circuits ───
CIRCUITS = [
    ("Signalement de danger", "Maltraitance, danger pour l'enfant",
     "<b>CRIP · procureur · 119</b>", "❌ Pas ce cas"),
    ("Saisine MDPH", "Suspicion de <b>handicap</b> ou trouble persistant",
     "<b>Équipe éducative → GEVA-Sco → MDPH</b>", "✅ Cas n°1"),
    ("Orientation SEGPA", "<b>Grande difficulté scolaire</b> en fin de CM2",
     "<b>Dossier CDOEA</b>", "✅ Cas n°2"),
]

# ─── les documents ───
DOCS = [
    ("PPRE", "difficultés scolaires <b>sans</b> trouble identifié", "l'équipe pédagogique"),
    ("PAP", "<b>trouble des apprentissages</b> (dyslexie, dysorthographie…)", "sur avis du <b>médecin scolaire</b>"),
    ("GEVA-Sco", "<b>évaluation des besoins</b>, transmise à la MDPH", "<b>directeur + équipe éducative</b>"),
    ("PPS", "si la MDPH reconnaît un <b>handicap</b>", "la MDPH"),
    ("ESS", "le suivi du PPS", "l'<b>enseignant référent</b>"),
    ("Dossier CDOEA", "orientation <b>SEGPA</b>", "l'école + la commission"),
]

# ─── qui fait quoi ───
QUI = [
    ("L'enseignant", "repère, documente, aménage, alerte le directeur"),
    ("Le directeur", "⭐ <b>convoque l'équipe éducative</b>, rédige le compte-rendu, veille au <b>GEVA-Sco</b>, fait le lien avec la famille"),
    ("Les parents", "<b>seuls à pouvoir déposer la MDPH</b> — l'école ne peut pas le faire à leur place"),
    ("Le RASED", "maître E <i>(apprentissages)</i> · maître G <i>(psychologique)</i> · <b>psychologue scolaire</b>"),
    ("Le médecin scolaire", "avis médical, peut établir un <b>PAP</b>"),
    ("L'enseignant référent", "organise l'<b>ESS</b>, suit le <b>PPS</b>"),
    ("La MDPH", "évalue et <b>notifie</b> les droits"),
]

# ─── le cas CM2 ───
CAS_CM2 = [
    ("Trouble spécifique des apprentissages <i>(dyslexie sévère)</i>",
     "<b>PAP</b> ou <b>MDPH</b> → <b>ULIS TSLA</b>"),
    ("Déficience cognitive", "<b>MDPH</b> → <b>ULIS</b>"),
    ("Grande difficulté scolaire sans trouble identifié",
     "<b>SEGPA</b> via le <b>CDOEA</b>"),
]

# ─── les modèles de courriers (texte brut, copiable) ───
MODELES = [
    ("1", "Courrier aux parents — information sur la MDPH",
     """Madame, Monsieur,

Votre enfant {Prénom NOM}, scolarisé(e) en CM2 à l'école {nom de l'école}, rencontre des
difficultés persistantes en lecture, constatées depuis le CP.

Nous avons mis en place les aménagements suivants : {PPRE / différenciation / ...}.
Malgré ces aménagements, les difficultés restent importantes.

Dans ce cadre, nous vous informons qu'il est possible, si vous le souhaitez, de déposer
un dossier auprès de la Maison départementale des personnes handicapées (MDPH).

Cette démarche est à votre initiative : l'école ne peut pas la faire à votre place.
Si vous engagez cette démarche, l'école vous transmettra un document d'évaluation des
besoins (GEVA-Sco), préparé avec l'équipe éducative.

Nous restons à votre entière disposition pour en parler, au moment qui vous conviendra.

Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.

                                              Le directeur / la directrice
                                              {Nom, signature, cachet}

Copie : dossier de l'élève — note de la date de remise en main propre ou d'envoi."""),

    ("2", "Convocation à une équipe éducative",
     """Objet : convocation à une équipe éducative

Madame, Monsieur,

Une équipe éducative est réunie le {date} à {heure}, à l'école {nom de l'école},
afin de faire le point sur la situation de votre enfant {Prénom NOM},
scolarisé(e) en {classe} depuis {date}.

Personnes convoquées :
  - {Nom}, directeur / directrice de l'école
  - {Nom}, enseignant(e) de la classe
  - {Nom}, psychologue scolaire
  - {Nom}, maître E du RASED (si pertinent)
  - {Nom}, médecin scolaire (si pertinent)
  - vous-mêmes

Ordre du jour :
  1. Difficultés constatées et observations en classe
  2. Aménagements déjà mis en place
  3. Bilan des évaluations et des suivis
  4. Propositions : aménagements, PPRE, saisine du RASED
  5. Information sur les démarches possibles (MDPH, orientation adaptée)

Votre présence est indispensable : aucune décision concernant votre enfant ne sera
prise en votre absence.

Un compte-rendu vous sera adressé après la réunion.

Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.

                                              Le directeur / la directrice
                                              {Nom, signature, cachet}"""),

    ("3", "Compte-rendu d'équipe éducative",
     """ÉQUIPE ÉDUCATIVE — COMPTE-RENDU

École : ______________________     Date : ____ / ____ / ______     Durée : ______
Élève : ______________________     Né(e) le : ____ / ____ / ______
Classe : ______________            Enseignant(e) : ______________________

PERSONNES PRÉSENTES
  - ____________________________________________________
  - ____________________________________________________
PERSONNES EXCUSÉES
  - ____________________________________________________

1. MOTIF DE LA RÉUNION
   ____________________________________________________________________

2. ÉLÉMENTS PRÉSENTÉS
   - Observations en classe : ______________________________________
   - Évaluations / niveau atteint : _________________________________
   - Bilans existants (orthophonie, psychologie, médical) : _________
   - Historique depuis le CP : ______________________________________

3. CE QUI A DÉJÀ ÉTÉ MIS EN PLACE
   ____________________________________________________________________

4. ANALYSE PARTAGÉE
   ____________________________________________________________________

5. DÉCISIONS PRISES
   [ ] Aménagements pédagogiques : __________________________________
   [ ] PPRE : objectifs _____________________________________________
   [ ] Saisine du RASED : ___________________________________________
   [ ] Avis médical / demande de PAP : _____________________________
   [ ] Information donnée à la famille sur la MDPH :   oui / non
       (date et forme : ____________________________________________)
   [ ] Dossier CDOEA (orientation adaptée) :             oui / non
   [ ] Autre : ______________________________________________________

6. SUIVI — QUI FAIT QUOI ET QUAND
   __________________________________  avant le ____ / ____ / ______
   __________________________________  avant le ____ / ____ / ______

7. PROCHAINE RÉUNION PRÉVUE LE : ____ / ____ / ______

Signature du directeur / de la directrice : ____________________________

Diffusion : famille · enseignant · RASED · médecin scolaire · dossier de l'élève"""),

    ("4", "Demande de bilan au RASED",
     """Objet : demande d'intervention du RASED

À l'attention de {Nom du psychologue scolaire / du maître E}

École : ______________________   Circonscription : ______________________

Élève concerné(e) : {Prénom NOM}, né(e) le ____ / ____ / ______, classe de {classe}

Motif de la demande :
  Difficultés persistantes en {lecture / écriture / mathématiques}, constatées depuis
  {classe / CP}, résistant aux aménagements mis en place en classe.

Ce qui a déjà été fait :
  - PPRE : _________________________________________________________
  - Différenciation en classe : ____________________________________
  - Maintien / redoublement : ______________________________________

Éléments joints :
  [ ] Productions d'élève
  [ ] Résultats d'évaluations
  [ ] Compte-rendu de l'équipe éducative du ____ / ____ / ______

Demande : un bilan et un avis sur la nature des difficultés, afin d'orienter
les aménagements et, le cas échéant, d'informer la famille des démarches possibles.

                                              Le directeur / la directrice
                                              {Nom, signature, cachet}

Avis de la famille :  accord / refus  (signature) ______________________"""),
]

# ─── les 5 gestes de la semaine ───
SEMAINE = [
    "Convoquer l'<b>équipe éducative</b> par écrit (parents + enseignant + RASED + psychologue scolaire).",
    "Demander le <b>bilan du RASED</b> si l'élève a déjà été suivi — sinon, l'activer.",
    "Informer les parents <b>par écrit</b> de leur droit de déposer un dossier MDPH — <b>sans le faire à leur place</b>.",
    "Ouvrir le <b>dossier CDOEA</b> : c'est le circuit de l'orientation adaptée.",
    "<b>Tout tracer</b> : compte-rendu d'équipe éducative, courriers, dates de remise.",
]

# ─── ce que ce n'est pas ───
PAS = [
    ("un signalement à la CRIP", "il n'y a pas de danger — ce serait une erreur grave de circuit"),
    ("un diagnostic", "le directeur ne diagnostique rien : il réunit, documente et oriente"),
    ("une décision de l'école sur l'AESH", "c'est la <b>MDPH</b> qui notifie ; l'école transmet le GEVA-Sco"),
    ("une démarche faite par l'école seule", "la MDPH est saisie <b>par la famille</b>"),
]
