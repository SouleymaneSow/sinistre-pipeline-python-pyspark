# 🧮 Sinistre Pipeline – Portfolio Data Engineering

![Python](https://img.shields.io/badge/python-3.11-blue)
![PySpark](https://img.shields.io/badge/pyspark-3.5-orange)
![CI](https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark/actions/workflows/ci.yml/badge.svg)

Bienvenue sur mon portfolio technique. Je suis **Souleymane Sow**, Data Engineer passionné par l’automatisation, la structuration et l’optimisation de pipelines distribués.

---

## 🎯 Objectif du projet

Ce projet PySpark traite des sinistres d’assurance en plusieurs étapes :
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
## 🧪 Technologies

- Python 3.11
- PySpark 3.5
- Pandas 2.3
- Pytest 8.4
- GitHub Actions
- VSCode + Conda

---

## 🧱 Structure du projet

- `src/` : modules Python et PySpark
- `tests/` : tests unitaires et d’intégration
- `scripts/` : génération de données parquet
- `data/` : fichier sinistres.parquet
- `.github/workflows/` : CI/CD GitHub Actions

---

## 🧪 Générer les données parquet de test

Le script [`scripts/generate_parquet.py`](scripts/generate_parquet.py) permet de générer un fichier Parquet simulé avec options en ligne de commande :
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
-  Analyse du Spark UI pour identifier les shuffles et goulets d’étranglement

---

## 📂 Voir le code sur GitHub
👉 https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark/tree/main

---

## 📄 Fiche projet PDF
👉 [Télécharger la fiche projet PDF](fiche_sinistre_pipeline.pdf)
