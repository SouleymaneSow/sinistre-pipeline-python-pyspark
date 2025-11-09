"""
run_inference.py — Script principal pour exécuter le pipeline PySpark complet :
lecture, nettoyage, validation métier, agrégation, écriture.
"""

from pyspark.sql import SparkSession

from src.pipeline.aggregator import aggregate_data
from src.pipeline.cleaner import clean_dataframe
from src.pipeline.reader import read_parquet
from src.pipeline.writer import write_parquet


def main():
    # 🔧 Initialisation de la session Spark
    spark = SparkSession.builder.appName("PipelineSinistres").getOrCreate()

    print("📥 Lecture des données...")
    df_raw = read_parquet(spark, "data/sinistres.parquet")

    print("🧹 Nettoyage des données...")
    df_clean = clean_dataframe(df_raw)

    print("📊 Agrégation des données...")
    df_agg = aggregate_data(df_clean)

    print("📤 Écriture des résultats...")
    write_parquet(df_agg, "data/sinistres_aggregated.parquet")

    print("✅ Pipeline exécuté avec succès.")


if __name__ == "__main__":
    main()
