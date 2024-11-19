# Projet APP_SCOLAIRE

# Application de Gestion Scolaire - Collège Bilingue Fogang et les Génies

Cette application web est conçue pour faciliter la gestion des données scolaires au Collège Bilingue Fogang et les Génies.  Elle permet aux enseignants, à l'administration , à l'administrateur principal  et aux parents d'accéder à des fonctionnalités spécifiques pour un suivi efficace des élèves et de leur performance académique.

## Objectif

L'objectif principal de ce projet est de créer une application web intuitive et fiable pour :

* **Simplifier la gestion des données scolaires :** Centraliser les informations sur les élèves, les enseignants, les classes et les notes.
* **Améliorer le suivi des performances des élèves :**  Fournir des outils pour suivre l'évolution des notes des élèves et identifier les domaines à améliorer.
* **Faciliter la communication entre les enseignants, l'administration et les parents :** Permettre un accès facile et sécurisé aux données scolaires pour les différents acteurs.
* **Automatiser certaines tâches administratives :**  Automatiser le calcul des moyennes et la génération de rapports.

## Fonctionnalités Principales

L'application offre un large éventail de fonctionnalités, notamment :

**Pour l'Administration et l'Administrateur Principal :**

* **Authentification sécurisée :**  Accès sécurisé aux données scolaires avec gestion des rôles et permissions.
* **Gestion des comptes :**  Création et gestion des comptes des enseignants et des administrateurs.
* **Gestion des classes :**  Gestion des informations sur les classes (nom, niveau, année scolaire).
* **Suivi de la présence des élèves :**  Enregistrement et suivi de la présence journalière des élèves.
* **Visualisation des performances :**  Accès aux visualisations des performances des élèves (séquentielles, trimestrielles et annuelles) pour suivre leur progrès et prendre des décisions éclairées.


**Pour les Enseignants :**

* **Authentification sécurisée :**  Accès sécurisé au système avec gestion des rôles et permissions.
* **Saisie des notes :**  Saisie des notes des élèves pour chaque matière et pour chaque type d'évaluation (séquentielle, trimestrielle et annuelle).
* **Visualisation des performances de leurs élèves :**  Suivi de la progression des élèves.

**Pour tous les parents:**

* **Interface utilisateur intuitive :**  Navigation facile et accès clair aux informations.
* **Génération de graphiques :**  Visualisation claire des données sous forme de graphiques.
* **Statistiques descriptives :**  Calcul automatique des statistiques descriptives (moyenne, médiane, écart type).


## Instructions d’utilisation

1.  **Installation :**  L'application est développée en Python et utilise Streamlit et MySQL. Assurez-vous d'avoir Python et les bibliothèques nécessaires installées. Installez les packages Python suivants : `pip install streamlit mysql-connector-python matplotlib seaborn`.  
2.  **Configuration de la base de données MySQL :**  Créez une base de données MySQL selon la structure détaillée dans le fichier `collegefoganggenies_db.sq.sql`.  Remplissez la base de données avec les informations nécessaires concernant les élèves, les enseignants et les classes.
3.  **Lancement de l'application :** Exécutez le fichier `app.py` avec Streamlit : `streamlit run app.py`.
4.  **Authentification :** Connectez-vous au système en utilisant vos identifiants (enseignant, administrateur ou administrateur principal).  Les identifiants sont définis dans la base de données.
5.  **Navigation :** Utilisez le menu latéral pour naviguer entre les différentes pages de l'application.


## Technologies Utilisées

* **Langage de programmation :** Python
* **Framework web :** Streamlit
* **Base de données :** MySQL
* **Bibliothèques Python :** `mysql-connector-python`, `matplotlib`, `seaborn`, `statistics`


