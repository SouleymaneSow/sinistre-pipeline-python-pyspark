from pyspark.sql.functions import col, lit, when


def nettoyer_montant(df, mediane):
    return df.withColumn(
        "montant_clean",
        when((col("montant") < 0) | col("montant").isNull(), lit(mediane)).otherwise(
            col("montant")
        ),
    )


def nettoyer_age(df, age_defaut=18, age_min=18, age_max=80):
    return df.withColumn(
        "age_clean",
        when(
            (col("age") < age_min) | (col("age") > age_max) | col("age").isNull(),
            lit(age_defaut),
        ).otherwise(col("age")),
    )


def nettoyer_date(df, date_reference):
    return df.withColumn(
        "date_sinistre_clean",
        when(
            col("date_sinistre") > lit(date_reference) | col("date_sinistre").isNull(),
            lit(date_reference),
        ).otherwise(col("date_sinistre")),
    )


def nettoyer_type_sinistre(df, types_valides, type_defaut="Autre"):
    return df.withColumn(
        "type_sinistre_clean",
        when(col("type_sinistre").isin(types_valides), col("type_sinistre")).otherwise(
            lit(type_defaut)
        ),
    )
