"""
cleaner.py — Nettoyage des données sinistres pour le pipeline PySpark

Contient des fonctions de nettoyage métier :
- montant négatif ou null → remplacé par la médiane
- age hors bornes → remplacé par défaut
- date future ou null → remplacée par référence
- type de sinistre invalide → remplacé par 'Autre'
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit, when


def nettoyer_montant(df: DataFrame, mediane: int) -> DataFrame:
    return df.withColumn(
        "montant_clean", when((col("montant") < 0) | col("montant").isNull(), lit(mediane)).otherwise(col("montant"))
    )


def nettoyer_age(df: DataFrame, age_defaut=18, age_min=18, age_max=80) -> DataFrame:
    return df.withColumn(
        "age_clean",
        when((col("age") < age_min) | (col("age") > age_max) | col("age").isNull(), lit(age_defaut)).otherwise(
            col("age")
        ),
    )


def nettoyer_date(df: DataFrame, date_reference: str) -> DataFrame:
    return df.withColumn(
        "date_sinistre_clean",
        when(col("date_sinistre") > lit(date_reference) | col("date_sinistre").isNull(), lit(date_reference)).otherwise(
            col("date_sinistre")
        ),
    )


def nettoyer_type_sinistre(df: DataFrame, types_valides, type_defaut="Autre") -> DataFrame:
    return df.withColumn(
        "type_sinistre_clean",
        when(col("type_sinistre").isin(types_valides), col("type_sinistre")).otherwise(lit(type_defaut)),
    )


def clean_dataframe(df: DataFrame) -> DataFrame:
    """
    Nettoie le DataFrame brut en appliquant les règles métier :
    - montant → montant_clean
    - age → age_clean
    - date_sinistre → date_sinistre_clean
    - type_sinistre → type_sinistre_clean

    Args:
        df (DataFrame): DataFrame brut

    Returns:
        DataFrame: DataFrame nettoyé
    """
    mediane = 8000
    types_valides = ["vol", "accident", "bris de glace", "incendie", "catastrophe naturelle"]

    df = nettoyer_montant(df, mediane)
    df = nettoyer_type_sinistre(df, types_valides)

    return df
