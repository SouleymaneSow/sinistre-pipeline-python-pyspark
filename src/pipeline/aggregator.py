"""
aggregator.py — Module d'agrégation des sinistres par client
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import avg, count
from pyspark.sql.functions import sum as _sum


def aggregate_data(df: DataFrame) -> DataFrame:
    """
    Agrège les données par client :
    - total des sinistres
    - moyenne des montants
    - nombre de sinistres

    Args:
        df (DataFrame): DataFrame Spark nettoyé contenant les colonnes 'client_id' et 'montant_clean'

    Returns:
        DataFrame: DataFrame agrégé par client
    """
    return df.groupBy("client_id").agg(
        _sum("montant_clean").alias("total"),
        avg("montant_clean").alias("moyenne"),
        count("*").alias("nb_sinistres"),
    )
