# 🧮 Sinistre Pipeline – Portfolio Data Engineering

![Python](https://img.shields.io/badge/python-3.11-blue)
![PySpark](https://img.shields.io/badge/pyspark-3.5-orange)
![CI](https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark/actions/workflows/ci.yml/badge.svg)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/imports-isort-blue.svg)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

📄 [Télécharger la fiche projet PDF](fiche_sinistre_pipeline.pdf)

Bienvenue sur mon portfolio technique. Je suis **Souleymane Sow**, Data Engineer passionné par l’automatisation, la structuration et l’optimisation de pipelines distribués.

---

## 🎯 Objectif du projet

Ce projet PySpark traite des sinistres d’assurance en plusieurs étapes :
- Nettoyage des montants
- Détection de fraude
- Agrégation par client
- Sauvegarde en Parquet
- Tests unitaires et CI/CD
- Automatisation des commandes avec Makefile

---

## 📊 Fonctionnalités principales

- Génération de données de test via CLI
- Pipeline PySpark modulaire et optimisé
- Détection de sinistres frauduleux
- Sauvegarde en Parquet
- Tests unitaires avec Pytest
- CI/CD GitHub Actions
- Automatisation des commandes avec Makefile

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
- `docs/`: index.md, fiche technique du projet et documentation

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

## Qualité & Validation

Le projet inclut deux types de tests :
- **Tests techniques** (`tests/test_spark_validation.py`) : vérifient le schéma, la présence de données et l’absence de nulls.
- **Tests métier** (`tests/test_validation_metier.py`) : vérifient les règles métier (montants valides, types de sinistres, absence de doublons).

La documentation est générée automatiquement avec **pdoc** :

```bash
make docs
```
---

## 📦 Installation et 🚀 Lancer le projet
Cloner le dépôt et créer l’environnement :
```bash
 - git clone https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark.git
 - cd sinistre-pipeline-python-pyspark
 - conda create -n sinistre_env python=3.11
 - conda activate sinistre_env
 - pip install -r requirements.txt
```
---

## ⚙️ Automatisation avec Makefile

Toutes les commandes du projet sont centralisées dans un **Makefile** pour simplifier l’exécution :
- `make lint` : vérifie la qualité du code avec pre-commit (linting, formatage, hooks)
- `make generate` : Génération des données Parquet (`scripts/generate_parquet.py`)
- `make run` : lance le pipeline complet (`scripts/run_inference.py`)
- `make test-technique` : exécute uniquement les tests techniques (schéma, colonnes, nullabilité)
- `make test-metier` : exécute uniquement les tests métier (règles métier, montants, sinistres)
- `make test-all` : exécute l’ensemble des tests
- `make docs` : génère la documentation avec **pdoc**

👉 Cela permet d’automatiser toutes les étapes (pipeline, tests, documentation) avec des commandes simples et reproductibles.

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

## Lien vers la fiche projet
👉 📄 [Voir la fiche projet PDF](fiche_sinistre_pipeline.pdf)
