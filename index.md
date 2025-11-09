# 🧮 Sinistre Pipeline – Portfolio Data Engineering

![Python](https://img.shields.io/badge/python-3.11-blue)
![PySpark](https://img.shields.io/badge/pyspark-3.5-orange)
![CI](https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark/actions/workflows/ci.yml/badge.svg)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/imports-isort-blue.svg)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

📄 [Télécharger la fiche projet PDF](docs/fiche_sinistre_pipeline.pdf)

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

- `scripts/` : contenant `generate_parquet.py` pour créer les données parquet et `run_inference.py`pour exécuter le pipeline complet
- `data/` : dossier contenant le fichier `sinistres.parquet` généré d’entrée
- `src/models/` : classes Python avec héritage (`Sinistre`, `SinistreVol`)
- `src/utils/` : fonctions de nettoyage (`nettoyer_montant`)
- `src/pipeline/` : modules PySpark (`reader`, `cleaner`, `aggregator`, `writer`)
- `tests/` : tests unitaires avec `pytest`
- `.github/workflows/` : CI/CD avec GitHub Actions
- `docs/`: contenant index.md, la fiche technique du projet et documentation

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

## ⚙️ Qualité & Validation

Le projet inclut deux types de tests :
- **Tests techniques** (`tests/test_spark_validation.py`) : vérifient le schéma, la présence de données et l’absence de nulls.
- **Tests métier** (`tests/test_validation_metier.py`) : vérifient les règles métier (montants valides, types de sinistres, absence de doublons).

---

## 📦 Installation et 🚀 Lancer le projet

Cloner le dépôt, créer l’environnement, générer les données parquet, lancer le pipeline et exécuter les tests :

```bash
# 1. Cloner le dépôt
git clone https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark.git

# 2. Se placer dans le dossier du projet
cd sinistre-pipeline-python-pyspark

# 3. Créer un environnement conda avec Python 3.11
conda create -n sinistre_env python=3.11

# 4. Activer l’environnement
conda activate sinistre_env

# 5. Installer les dépendances
pip install -r requirements.txt

# 6. Générer les données de test en parquet
python -m scripts.generate_parquet

# 7. Lancer le pipeline complet
python -m scripts.run_inference

# 8. Exécuter les tests unitaires
python -m pytest tests/
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

## 📚 Documentation technique (pdoc)

La documentation détaillée du code est générée automatiquement avec **pdoc**:

```bash
make docs
```
et accessible en ligne :
- [Module pipeline](docs/src/pipeline.html)
- [Module reader](docs/src/pipeline/reader.html)
- [Module cleaner](docs/src/pipeline/cleaner.html)
- [Module aggregator](docs/src/pipeline/aggregator.html)
- [Module writer](docs/src/pipeline/writer.html)

---

## ⚙️ Optimisations Spark

- `cache()` pour éviter les recalculs
- `broadcast()` pour optimiser les jointures avec petites tables
- `repartition()` pour équilibrer les partitions
-  Analyse du Spark UI pour identifier les shuffles et goulets d’étranglement

---

## 📂 Voir le code sur GitHub
👉 [Lien pour voir le code sur Github](https://github.com/SouleymaneSow/sinistre-pipeline-python-pyspark/tree/main)

---

## Lien vers la fiche projet
👉 📄 [Voir la fiche projet PDF](docs/fiche_sinistre_pipeline.pdf)
