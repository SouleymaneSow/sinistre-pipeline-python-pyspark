from .sinistre import Sinistre


class SinistreVol(Sinistre):
    """
    Classe héritée pour les sinistres de type vol.
    """

    def est_frauduleux(self):
        """
        Un sinistre vol est considéré comme frauduleux si le montant dépasse 10 000 €.
        """
        return self.montant > 10000 and self.type_sinistre.lower() == "vol"
