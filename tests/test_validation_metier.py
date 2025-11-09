# tests/test_validation_metier.py

"""test_validation_metier.py — Tests de validation métier sur les données nettoyées."""
from scripts.generate_parquet import generate_data
from src.pipeline.cleaner import clean_dataframe


def test_validation_metier(spark):
    """🧪 Tests de validation métier sur les données nettoyées."""
    # Génération de données brutes et nettoyage
    data, columns = generate_data(n_samples=100)
    df_raw = spark.createDataFrame(data, schema=columns)
    df_clean = clean_dataframe(df_raw)

    # ✅ Règles métier
    assert df_clean.filter("montant_clean < 0").count() == 0, "Montants négatifs détectés"
    assert df_clean.filter("montant_clean IS NULL").count() == 0, "Montants nuls détectés"
    assert df_clean.select("client_id").dropna().count() == df_clean.count(), "Client_id null détecté"
    assert df_clean.select("type_sinistre").dropna().count() == df_clean.count(), "Type_sinistre null détecté"
    assert df_clean.columns == ["client_id", "type_sinistre", "montant", "montant_clean", "type_sinistre_clean"]

    # 🔍 Règles métier supplémentaires
    assert df_clean.select("type_sinistre_clean").distinct().count() <= 5, "Trop de types de sinistres"
    assert df_clean.groupBy("client_id").count().filter("count > 1").count() == 0, "Doublons détectés"
    assert df_clean.filter("montant_clean > 20000").count() == 0, "Montant trop élevé"
