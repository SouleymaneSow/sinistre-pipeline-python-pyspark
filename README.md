# 🧮 Sinistre Pipeline – PySpark + Python

![Python](https://img.shields.io/badge/python-3.11-blue)
![PySpark](https://img.shields.io/badge/pyspark-3.5-orange)
![CI](https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark/actions/workflows/ci.yml/badge.svg)


# 👨‍💻 Auteur
Souleymane Sow – Data Engineer passionné par l’automatisation, la structuration et l'optimisation de pipelines distribués.

---

## 🎯 Objectif
Ce projet implémente un pipeline complet de traitement de sinistres :
- Nettoyage des montants
- Détection de fraude
- Agrégation par client
- Sauvegarde en Parquet
- Tests unitaires et CI/CD

---

## 📊 Fonctionnalités principales

- Génération de données de test via CLI
- Pipeline PySpark modulaire et optimisé
- Détection de sinistres frauduleux
- Sauvegarde en Parquet
- Tests unitaires avec Pytest
- CI/CD GitHub Actions

---

## 🧠 Technologies
- Python 3.11.14
- PySpark 3.5
- Pandas
- Pytest
- GitHub Actions
- VSCode + Conda

---

## 🧱 Structure du projet

- `scripts/` : utilitaires, dont `generate_parquet.py` pour créer les données parquet
- `data/` : dossier contenant le fichier `sinistres.parquet` généré d’entrée
- `src/models/` : classes Python avec héritage (`Sinistre`, `SinistreVol`)
- `src/utils/` : fonctions de nettoyage (`nettoyer_montant`)
- `src/pipeline/` : modules PySpark (`reader`, `cleaner`, `aggregator`, `writer`)
- `tests/` : tests unitaires avec `pytest`
- `.github/workflows/` : CI/CD avec GitHub Actions

---

## 🧪 Générer les données parquet de test

Le script [`scripts/generate_parquet.py`](scripts/generate_parquet.py) permet de générer un fichier Parquet simulé via des  options en ligne de commande :
- `--samples` : nombre d’échantillons à générer
- `--output` : chemin du fichier de sortie
- `--validate` : active la validation des données

Exemple :
```bash
python scripts/generate_parquet.py --samples 1000 --output data/sinistres.parquet --validate
```
---

## 📦 Installation et 🚀 Lancer le projet
Cloner le dépôt et créer l’environnement :
  git clone https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark.git
  cd sinistre-pipeline-python-pyspark
  conda create -n sinistre_env python=3.11
  conda activate sinistre_env
  pip install -r requirements.txt

---

## ⚙️ Optimisations Spark

- `cache()` pour éviter les recalculs
- `broadcast()` pour optimiser les jointures avec petites tables
- `repartition()` pour équilibrer les partitions
- Analyse du Spark UI pour identifier les shuffles et goulets d’étranglement

---

### 📂 Sources supportées par le pipeline
- Parquet

- CSV

- JSON

- SQL (Spark SQL, JDBC)

- XML, Avro, Delta Lake

---

## 🧪 Lancer les tests:
  python -m pytest tests/

---

## ⚙️ CI/CD:
Le workflow GitHub Actions se déclenche à chaque push ou pull request de la branche main

---

## 📄 Fiche projet PDF
👉 [Télécharger la fiche projet PDF](fiche_sinistre_pipeline.pdf)
