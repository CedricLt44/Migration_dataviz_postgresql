# PROJET DJANGO – Module de Visualisation de Données

## 🎯 Objectif du projet

Ce projet a pour but de **centraliser, sécuriser et valoriser les données d'entreprise** souvent stockées sous forme de fichiers Excel bruts.  
Il s'inscrit dans le cadre d’un développement plus large d’un progiciel incluant ERP, CRM et fonctionnalités IA.

---

## 🗄️ Migration des données vers une base de données

Les données issues de fichiers Excel sont **nettoyées, structurées et migrées vers une base PostgreSQL** afin d'assurer :

- Une meilleure fiabilité et sécurité des données
- Une accessibilité facilitée pour les applications
- Une base saine pour l'analyse

> **Technologies utilisées** : PostgreSQL, Python (Pandas), Django ORM

---

## 🔄 Extraction, Transformation, Chargement (ETL)

Un processus ETL est mis en place pour :

- **Nettoyer et filtrer les données**
- **Automatiser** l’intégration dans la base de données
- Garantir des données exploitables pour la suite du traitement

> **Technologies utilisées** : Python, DBT, SQL, Jinja

---

## 📊 Visualisation des données

Des graphiques interactifs sont intégrés à l'application pour :

- Offrir une lecture claire et directe des indicateurs
- Compléter les outils BI existants (ex : Power BI)

Ce module ne vise **pas à remplacer** Power BI, mais à fournir une **vue rapide et intégrée** dans l'application web.

> **Technologies utilisées** : Django, Plotly, HTML/CSS

---

## 🚀 Stack technique

- **Back-end** : Python, Django
- **Base de données** : PostgreSQL
- **Transformation de données** : DBT, SQL, Jinja
- **Visualisation** : Plotly
- **Frontend** : Django templates, HTML/CSS , Tailwindcss, DAisyui

---

## 📁 Structure du projet (exemple)

- dashboard_vehicule/

  - backend/

    - templates/
      - backend/
        - base.html
        - index.html

  - dashboard/

    - templates/
      - dashboard/
        - data.html
    - models_legacy.py
    - models.py
    - views.py

  - dashboard_vehicule/

    - settings.py
    - urls.py

    - static/
      - src/
      - img/

  - manage.py
  - requirements.txt
  - package.json
  - .env

- dbt_entretien_vehicule/

  - models/
    - entretien_vehicule/
      - marts
      - sources
      - staging
  - tests/
  - dbt_project.yml

- migration/
  - migration.py
  - migration_conso.py
  - migration_immat.py
- raw/

  - conso.csv
  - Data.csv

- env/
  - (environnement virtuel Python)
