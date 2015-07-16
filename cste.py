#!/usr/bin/python3
## @file cste.py
#  @package cste
#  @brief Generals constants for python application
#  @author Jeremy HERGAULT (reneca)
#          Jean-Philippe HAYES
#  @version 1.0
#  @date 2015-07-15
#
#  This file is part of Polycarnet, which is a carnet de suivi genrator
#  Copyright (C) 2015  HERGAULT Jeremy, Alexandre, Thierry ( reneca )
#
#  Polycarnet is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Polycarnet is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Polycarnet. If not, see <http://www.gnu.org/licenses/>.

import string
import json
from collections import OrderedDict

# Key for asking
uniqKey = "U6L8ICR"

# Vars
headerSess = OrderedDict()
headerSess = {
	'User-Agent'		: 'Tamamanapoil/2.0',
	'Accept'		: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language'	: 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding'	: 'gzip, deflate',
	'Connection'		: 'keep-alive',
	'Cache-Control'		: 'max-age=0'
}

# Constantes
assocValue = {
"travail en autonomie_G1" : { "name" : "", "notions" : "", "niveau" : "", "comm" : "" },
"travail en autonomie_G2" : { "name" : "", "notions" : "", "niveau" : "", "comm" : "" },

# Commun
"Anglais_TD1" : { "name" : "Anglais", "notions" : "Analyse de documents", "niveau" : "Moyen", "comm" : "TD pour préparation à l'examen" },
"Anglais_TD2" : { "name" : "Anglais", "notions" : "Analyse de documents", "niveau" : "Moyen", "comm" : "TD pour préparation à l'examen" },
"Anglais_CC" : { "name" : "Anglais", "notions" : "Controle final d'anglais", "niveau" : "Moyen", "comm" : "Controle terminal passé dans de bonnes conditions" },
"Ang_gr nonToeic" : { "name" : "Anglais", "notions" : "Cours pratique à l'oral", "niveau" : "Moyen", "comm" : "Cours très intéressent car plus vivant" },

"Projet professionnel_CM" : { "name" : "Projet professionnel", "notions" : "Analyse de la création d'un projet professionnel", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Projet professionnel_TD1" : { "name" : "Projet professionnel", "notions" : "Réalisation d'un projet professionnel", "niveau" : "Bon", "comm" : "Partie pratique intéressente" },
"Projet professionnel_TD2" : { "name" : "Projet professionnel", "notions" : "Réalisation d'un projet professionnel", "niveau" : "Bon", "comm" : "Partie pratique intéressente" },
"Projet professionnel_TD" : { "name" : "Projet professionnel", "notions" : "Réalisation d'un projet professionnel", "niveau" : "Bon", "comm" : "Partie pratique intéressente" },
"Projet professionnel_CT" : { "name" : "Projet professionnel CT", "notions" : "Controle terminal", "niveau" : "Bon", "comm" : "Controle terminal" },

"M2M_TP" : { "name" : "TP M2M", "notions" : "TP sur l'integrations d'une plateforme", "niveau" : "Très bon", "comm" : "TP M2M très instructif sur l'integration inter-programmes" },
"M2M_CM" : { "name" : "M2M", "notions" : "Cours sur les réseau télécom et etudes des architectures", "niveau" : "Très bon", "comm" : "Cours très intéressent" },
"M2M_CT" : { "name" : "M2M CT", "notions" : "Controle terminal de M2M", "niveau" : "Très bon", "comm" : "Controle sur présentation oral qui est plus pertinent qu'un controle écrit" },

"Ecriture_Pilot_CM" : { "name" : "Ecriture de pilotes", "notions" : "Ecriture d'un pilote en C", "niveau" : "Très bon", "comm" : "Cours très intéressent" },
"Ecriture_Pilot_TD" : { "name" : "Ecriture de pilotes", "notions" : "Analyse d'architectures", "niveau" : "Très bon", "comm" : "Cours très intéressent" },
"Ecriture_Pilot_TP" : { "name" : "TP Ecriture de pilotes", "notions" : "Ecriture de pilote en C et assembleur sur plateforme réel", "niveau" : "Très bon", "comm" : "TP permettant de programmer un vrai microcontroleur d'une manière bas niveau" },

"Dev_Mobil1_CM" : { "name" : "Développement mobile", "notions" : "Cours de présentation général d'Android", "niveau" : "Très bon", "comm" : "Cours assez long sur des notions génériques" },
"Dev_Mobil1_TP" : { "name" : "TP Développement mobile", "notions" : "Développement sur plateforme Android", "niveau" : "Très bon", "comm" : "TP très interressent qui permet de prendre la main rapidement sur la programmation android" },
"Dev_Mobiles_CT" : { "name" : "Développement mobile CT", "notions" : "Controle terminal Android", "niveau" : "Très bon", "comm" : "Controle assez difficile sur des notions devants êtres aprises par coeur" },

"Dev_Mobil2_CM" : { "name" : "Développement mobile 2", "notions" : "Etude Solution développement mobile en HTML5/CSS/Javascript", "niveau" : "Très bon", "comm" : "Cours très court. Peu de notions ont été abordées" },
"Dev_Mobil2_TP" : { "name" : "TP Développement mobile 2", "notions" : "Réalisation TP sur Cordova", "niveau" : "Très bon", "comm" : "TP la aussi très court qui n'ont pas permis de manipuler beaucoup cordova. Dommage" },

"Fiabilité_Syst_CM" : { "name" : "Fiabilité des systèmes", "notions" : "Etude fiabilité des systèmes", "niveau" : "Bon", "comm" : "Cours inutile reprenant le cours d'année 4" },
"Fiabilité_Syst_TD" : { "name" : "Fiabilité des systèmes", "notions" : "Exercices sur la fiabilité de systèmes", "niveau" : "Bon", "comm" : "Cours inutile reprenant le cours d'année 4" },

"Tec_Fil_CM" : { "name" : "Technologie sans fil", "notions" : "Etude des technologies sans fil", "niveau" : "Bon", "comm" : "Cours peu centré sur les technologies sans fil mais plus sur les problématiques réseaux" },
"Tec_Fil_TD" : { "name" : "Technologie sans fil", "notions" : "Exercice sur les technologies sans fil", "niveau" : "Bon", "comm" : "Cours peu centré sur les technologies sans fil mais plus sur les problématiques réseaux" },
"Tec_Fil_TP" : { "name" : "TP Technologie sans fil", "notions" : "TP de programmation sur des technologies sans fil", "niveau" : "Bon", "comm" : "TP qui as permis de découvrir beaucoup de notions" },
"Tech_Fil_CT" : { "name" : "Technologie sans fil CT", "notions" : "Controle terminal technologies sans fil", "niveau" : "Bon", "comm" : "Controle terminal" },

"Ad_Systeme_CM" : { "name" : "Administration des systèmes", "notions" : "Cours sur les systèmes UNIX et Windows", "niveau" : "Très bon", "comm" : "Cours intéressent mais qui arrive un peu tard dans la formation" },
"Ad_Systeme_TP" : { "name" : "TP Administration des systèmes", "notions" : "TP sur l'installation d'un serveur sous Windows et UNIX", "niveau" : "Très bon", "comm" : "TP intéressent mais qui arrive un peu tard dans la formation" },

"Ad_Web_CM" : { "name" : "Administration Web", "notions" : "Etude des technologies HTML5/CSS3/Javascript", "niveau" : "Très bon", "comm" : "Cours présentant assez bien les technologies Web" },
"Ad_Web_TP" : { "name" : "TP Administration Web", "notions" : "Création d'un projet en HTML5/CSS3/Javascript", "niveau" : "Très bon", "comm" : "TP beaucoup trop dense dans un emplois du temps déjà surchargé" },

"Strategie_Entrep_CM" : { "name" : "Stratégie entreprise", "notions" : "Cours sur l'organisation d'une entreprise", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Strategie_Entrep_TD" : { "name" : "Stratégie entreprise", "notions" : "Exercices sur l'organisation d'une entreprise", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Strategie_Entrep_CT" : { "name" : "Stratégie entreprise CT", "notions" : "Controle terminal", "niveau" : "Bon", "comm" : "Controle terminal" },

"Marketing_CM" : { "name" : "Marketing", "notions" : "Cours sur l'etude marketing d'une entreprise", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Marketing_TD" : { "name" : "Marketing", "notions" : "Réalisation d'une etude marketing", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Marketing_CT" : { "name" : "Marketing CT", "notions" : "Controle terminal", "niveau" : "Bon", "comm" : "Controle terminal" },

"Bus_Plan_CM Preteseille" : { "name" : "Business plan", "notions" : "Cours sur la réalisation d'un business plan", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Bus_Plan_TD Pretesseille" : { "name" : "Business plan", "notions" : "Réalisation d'un business plan", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Business_Plan_CT" : { "name" : "Business plan CT", "notions" : "Controle terminal", "niveau" : "Bon", "comm" : "Controle terminal" },

"Instrumentation_cde_CM" : { "name" : "Instrumentation de la commande", "notions" : "Cours sur LabView (remise à niveau)", "niveau" : "Bon", "comm" : "Cours intéressent sur les asservissements" },
"Inst_cde_TP1" : { "name" : "Instrumentation de la commande", "notions" : "TP sur maquette réel pour asservissement sur LabView", "niveau" : "Bon", "comm" : "TP intéressent sur les maquettes réelles" },
"Inst_cde_TP2" : { "name" : "Instrumentation de la commande", "notions" : "TP sur maquette réel pour asservissement sur LabView", "niveau" : "Bon", "comm" : "TP intéressent sur les maquettes réelles" },

"// & Rep1_CM" : { "name" : "Parallèle et Répartie", "notions" : "Cours sur la programmation parallèle et rapartie", "niveau" : "Très bon", "comm" : "Cours qui est encore jeune mais qui présente tout les aspects de la programmation parallèle et répartie" },
"// & Rep2_TD" : { "name" : "Parallèle et Répartie", "notions" : "Cours sur la programmation parallèle et rapartie", "niveau" : "Très bon", "comm" : "Cours qui est encore jeune mais qui présente tout les aspects de la programmation parallèle et répartie" },
"// & Rep2_TP" : { "name" : "TP Parallèle et Répartie", "notions" : "TP sur les threads, fork, OpenMP,...", "niveau" : "Très bon", "comm" : "TP ou l'on revoit des notions déjà vu en 3ème année" },
"// & Rep_CT" : { "name" : "Parallèle et Répartie CT", "notions" : "Controle terminal", "niveau" : "Très bon", "comm" : "Controle terminal" },

"Appli_Mult_CM" : { "name" : "Application multimedia", "notions" : "Etude de codecs et formatage de données multimedia", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Appli_Mult_TD" : { "name" : "Application multimedia", "notions" : "Etude de codecs et formatage de données multimedia", "niveau" : "Bon", "comm" : "Cours intéressent" },
"Appli_Mult_TP" : { "name" : "Application multimedia", "notions" : "TP sur des logiciels de traitement d'image, son, video", "niveau" : "Bon", "comm" : "TP intéressent qui permet de manipuler des logiciels" },
"Appli_mult_CT" : { "name" : "Application multimedia CT", "notions" : "Controle terminal", "niveau" : "Bon", "comm" : "Controle terminal" },

"Outils_Fo_CM" : { "name" : "Outils formels", "notions" : "Langage B", "niveau" : "Mauvais", "comm" : "Cours inutile. Nous n'avons rien appris à part un langage de programmation que nous ne réutiliserons pas" },
"Outils_Fo_TD" : { "name" : "Outils formels", "notions" : "Langage B", "niveau" : "Mauvais", "comm" : "Cours inutile. Nous n'avons rien appris à part un langage de programmation que nous ne réutiliserons pas" },
"Outils_Fo_TP" : { "name" : "Outils formels", "notions" : "Langage B", "niveau" : "Mauvais", "comm" : "Cours inutile. Nous n'avons rien appris à part un langage de programmation que nous ne réutiliserons pas" },
"OutilsFormels_CT" : { "name" : "Outils formels CT", "notions" : "Controle terminal", "niveau" : "Mauvais", "comm" : "Controle terminal raté" },

"PFE_analyse modèle" : { "name" : "Cahier d'analyse du modèle PFE", "notions" : "Mise en place d'un modèle", "niveau" : "Bon", "comm" : "Bon encadrement pour la réalisation de ce document" },
"PFE_cahier de spécif" : { "name" : "Cahier de spécification PFE", "notions" : "Rédaction du cahier de spécification", "niveau" : "Bon", "comm" : "Bon encadrement pour la réalisation de ce document" },
"PFE_livrable" : { "name" : "Livrables PFE", "notions" : "Préparation des livrables", "niveau" : "Bon", "comm" : "Bon encadrement pour la réalisation de ce document, mais on aurait aimé avoir la présentation plus tôt" },
"Soutenance PFE" : { "name" : "Soutenance PFE", "notions" : "Soutenance à l'oral", "niveau" : "Bon", "comm" : "Bonne présentation" },

# Domotique
"Domotique_CM" : { "name" : "Domotique", "notions" : "", "niveau" : "Bon", "comm" : "" },
"Domotique_TD" : { "name" : "Domotique", "notions" : "", "niveau" : "Bon", "comm" : "" },
"Domotique_TP" : { "name" : "Domotique", "notions" : "", "niveau" : "Bon", "comm" : "" },
"Domotique_CT" : { "name" : "Domotique CT", "notions" : "", "niveau" : "Bon", "comm" : "" },

"Gest Energie_CM" : { "name" : "Gestion de l'énergie", "notions" : "", "niveau" : "Bon", "comm" : "" },
"Gest Energie_TP" : { "name" : "Gestion de l'énergie", "notions" : "", "niveau" : "Bon", "comm" : "" },

"Auto Hab1_CM" : { "name" : "Automatisation de l'habitation", "notions" : "", "niveau" : "Bon", "comm" : "" },
"Auto Hab2_CM" : { "name" : "Automatisation de l'habitation 2", "notions" : "", "niveau" : "Bon", "comm" : "" },
"Auto Hab2_TP" : { "name" : "Automatisation de l'habitation", "notions" : "", "niveau" : "Bon", "comm" : "" },
"Auto Hab_CT" : { "name" : "Automatisation de l'habitation CT", "notions" : "", "niveau" : "Bon", "comm" : "" },

# Automobile
"Véhicule_int_CM" : { "name" : "Véhicule intelligent", "notions" : "Cours sur les véhicules automatisés", "niveau" : "Très bon", "comm" : "Cours très intéressent, très formateur" },
"véhicule_int_TP" : { "name" : "TP Véhicule intelligent", "notions" : "TP sur RTMaps pour la compréhension d'algorithmes de controles", "niveau" : "Très bon", "comm" : "TP très intéressent" },
"Véhicule_int_CT" : { "name" : "Véhicule intelligent CT", "notions" : "Controle terminal", "niveau" : "Très bon", "comm" : "Controle terminal" },

"Norm_auto_CM" : { "name" : "Norme automobile", "notions" : "Cours sur les normes automobiles", "niveau" : "Bon", "comm" : "Cours très intéressent, très formateur" },
"Norm_auto_TD" : { "name" : "Norme automobile", "notions" : "Exercices sur les normes automobiles", "niveau" : "Bon", "comm" : "Cours très intéressent, très formateur" },
"Norm_auto_TP" : { "name" : "TP Norme automobile", "notions" : "TP sur RTMaps", "niveau" : "Bon", "comm" : "TP très intéressent" },
"Normes Automobile_CT" : { "name" : "Norme automobile CT", "notions" : "Controle terminal", "niveau" : "Bon", "comm" : "Controle terminal" },

"Routage_CM" : { "name" : "Routage", "notions" : "Etude d'algorithmes de déplacements", "niveau" : "Bon", "comm" : "Cours assez abstrait" },
"Routage_TP" : { "name" : "Routage", "notions" : "TP sur l'étude Macro/Micro de routes, intersections,...", "niveau" : "Bon", "comm" : "TP sur un problème concret" }
}

# Valeurs a ne pas traiter
skipValue = [ "java.util.ArrayList/4159755760", "com.adesoft.gwt.core.client.rpc.data.planning.SquareEvent/3694954416", "java.lang.Integer/3438268394", "java.lang.String/2004016611",
"Shannon", "Boole", "Unix B", "Unix A", "Windows B", "Windows A", "Pascal", "STD 8", "TP Systèmes", "Chaîne Production", "Von Neumann", "Lovelace", "S 228-229", "C.R.L.", "Turing", "STD 10", "S Auto 2", "STD 6", "STD 9", "Babbage", "Mezzanine", "S Info A", "STD 7", "STD 4", "STD 5", "STD 8",
"DOUAM CLEMENT", "JEANTIN SYLVIE", "BROCKOP BJORN", "LEBOCEY PIERRE", "LAMATY PHILIPPE", "RAVEAUX ROMAIN", "LISSY ALEXANDRE", "MOFID YASSINE", "CONTE DONATELLO", "CHEMLA JEAN-PAUL", "JACQUES SEBASTIEN", "MISCOPEIN LAURENT", "MONMARCHE ANTOINE", "MOHAMAD SUZANNE", "! INTERVENANT EXTERIEUR", "CAPDEVIELLE MARIANNE EMILIE", "MEICHEL PASCAL", "MARTINEAU PATRICK", "RAGOT NICOLAS", "LESCIEUX MATTHIEU", "GAUCHER PIERRE", "AMARY SANDRINE", "DABOUIS QUENTIN", "RAMEL JEAN-YVES", "BELAIR SYLVIE", "MAKRIS PASCAL", "PRETESEILLE MICHAEL", "NDIAYE ISMAILA", "PEREZ RASTELLI JOSHUE", "DUPRAT CHRISTINE", "ROLLAND ALEXIS",
"Réunion_Rentrée_D2I5", "Evasys", "Réunion de bilan", "conférence..", "Point Tuteurs", "réunion information", "Table ronde smart city", "Strategie_Entrep_CT rattrapage"
]

# End of file

