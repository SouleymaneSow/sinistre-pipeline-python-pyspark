import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from src.pipeline.aggregator import aggreger_par_client
from src.pipeline.cleaner import nettoyer_montant


@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder.master("local")
        .appName("TestPipeline")
        .config("spark.driver.extraClassPath", "")
        .config("spark.executor.extraClassPath", "")
        .config("spark.sql.warehouse.dir", "file:///C:/temp")
        .config("spark.local.dir", "file:///C:/temp")
        .config("spark.io.compression.codec", "none")
        .config("spark.hadoop.fs.defaultFS", "file:///")
        .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "1")
        .config("spark.ui.showConsoleProgress", "false")
        .getOrCreate()
    )


@pytest.fixture
def sample_data(spark):
    """Crée un DataFrame de test."""
    schema = StructType(
        [
            StructField("client_id", StringType(), False),
            StructField("type_sinistre", StringType(), False),
            StructField("montant", IntegerType(), True),
        ]
    )

    data = [
        ("C0001", "vol", 5000),
        ("C0001", "accident", 3000),
        ("C0002", "bris de glace", None),
        ("C0003", "incendie", 15000),
    ]

    return spark.createDataFrame(data, schema)


def test_pipeline_complet(spark, sample_data, tmp_path):
    # Sauvegarder les données de test directement en mémoire
    df = sample_data
    assert df.count() == 4

    # Nettoyer les montants
    df_clean = nettoyer_montant(df, mediane=5000)
    assert df_clean.count() == 4

    # Agréger par client
    df_aggrege = aggreger_par_client(df_clean)
    assert "total" in df_aggrege.columns
    assert df_aggrege.count() == 3  # 3 clients uniques

    # Vérifier les agrégations
    result = df_aggrege.collect()
    client1_row = next(row for row in result if row.client_id == "C0001")
    assert client1_row.total == 8000  # 5000 + 3000
