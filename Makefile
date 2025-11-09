# 📦 Makefile pour pipeline PySpark modulaire

.PHONY: lint generate run test-technique test-metier test-all docs

## 🎨 Vérification qualité du code
lint:
	@echo "🎨 Linting avec pre-commit..."
	pre-commit run --all-files

## 📁 Génération des données Parquet
generate:
	@echo "📁 Génération des données Parquet..."
	python scripts/generate_parquet.py --samples 1000 --validate

## 🚀 Exécution du pipeline complet
run:
	@echo "🚀 Exécution du pipeline PySpark..."
	python -m scripts.run_inference

## 🧪 Tests techniques uniquement
test-technique:
	@echo "🧪 Lancement des tests techniques..."
	python -m pytest tests/test_spark_validation.py

## 🧪 Tests metiers uniquement
test-metier:
	@echo "🧪 Lancement des tests metiers..."
	python -m pytest tests/test_validation_metier.py

## 🧪 Tests unitaires et Spark
test-all:
	@echo "🧪 Lancement des tests Spark..."
	python -m pytest tests/

## 📚 Génération de la documentation HTML
docs:
	@echo "📚 Génération de la documentation avec pdoc dans le dossier docs/"
	pdoc --output-dir docs src/pipeline
