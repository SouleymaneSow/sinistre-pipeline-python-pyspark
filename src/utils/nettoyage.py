import numpy as np
import pandas as pd


def nettoyer_montant(serie):
    """
    Nettoie une série de montants :
    - Convertit en numérique
    - Supprime les valeurs négatives
    - Remplace les NaN par la médiane

    Args:
        serie (pd.Series): Série de montants

    Returns:
        pd.Series: Série nettoyée
    """
    serie = pd.to_numeric(serie, errors="coerce")
    serie = serie.where(serie >= 0, np.nan)
    mediane = serie.median()
    return serie.fillna(mediane)
