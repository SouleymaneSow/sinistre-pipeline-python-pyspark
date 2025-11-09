"""
test_spark_validation.py — Tests de validation technique sur le fichier sinistres.parquet généré
"""

from pyspark.sql.types import IntegerType, StringType, StructField, StructType


def test_schema(spark):
    """✅ Vérifie que le schéma du fichier Parquet est conforme."""
    df = spark.read.parquet("data/sinistres.parquet")

    expected_schema = StructType(
        [
            StructField("client_id", StringType(), True),
            StructField("type_sinistre", StringType(), True),
            StructField("montant", IntegerType(), True),
        ]
    )

    assert df.schema == expected_schema, "❌ Schéma incorrect"


def test_count(spark):
    """🔢 Vérifie que le fichier contient des données."""
    df = spark.read.parquet("data/sinistres.parquet")
    assert df.count() > 0, "❌ Le fichier Parquet est vide"


# ✅ Vérification stricte des colonnes non-nulles et du schéma
def test_colonnes_non_nulles(spark):
    """🚫 Vérifie qu’il n’y a pas de nulls dans les colonnes non-nullables."""
    df = spark.read.parquet("data/sinistres.parquet")
    assert df.filter("client_id IS NULL OR type_sinistre IS NULL").count() == 0, "❌ Données invalides détectées"
    assert df.columns == ["client_id", "type_sinistre", "montant"], "Schéma des colonnes incorrect"
