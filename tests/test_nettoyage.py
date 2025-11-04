import pandas as pd

from src.utils.nettoyage import nettoyer_montant


def test_nettoyer_montant():
    serie = pd.Series([1000, -500, None, "abc", 2500])
    resultat = nettoyer_montant(serie)
    assert all(resultat >= 0)
    assert resultat.isna().sum() == 0
