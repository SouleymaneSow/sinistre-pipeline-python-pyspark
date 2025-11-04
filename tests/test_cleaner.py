import pytest
from pyspark.sql import SparkSession

from src.pipeline.cleaner import nettoyer_montant


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[1]").appName("Test").getOrCreate()


def test_nettoyage_montant_spark(spark):
    df = spark.createDataFrame([(1, -100), (2, None), (3, 200)], ["id", "montant"])
    df_clean = nettoyer_montant(df, mediane=150)
    # Vérifie qu'il n'y a plus de valeurs négatives
    assert df_clean.filter("montant_clean < 0").count() == 0
    # Vérifie qu'il n'y a plus de valeurs nulles
    assert df_clean.filter("montant_clean IS NULL").count() == 0
    # Vérifie que la médiane est bien appliquée à l'id 2
    assert df_clean.filter("id = 2").collect()[0]["montant_clean"] == 150
