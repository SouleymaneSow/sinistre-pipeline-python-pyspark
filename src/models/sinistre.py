class Sinistre:
    """
    Classe de base représentant un sinistre.

    Attributs :
        date (str) : Date du sinistre
        montant (float) : Montant du sinistre
        type_sinistre (str) : Type de sinistre (vol, accident, etc.)
    """

    def __init__(self, date, montant, type_sinistre):
        self.date = date
        self.montant = montant
        self.type_sinistre = type_sinistre

    def est_frauduleux(self):
        """
        Méthode par défaut : un sinistre n'est pas considéré comme frauduleux.
        """
        return False
