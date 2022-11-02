class Card:
    """Representa uma carta do jogo"""

    def __init__(self, valor, naipe):
        """Inicializa valor e naipe da carta do jogo"""
        self.valor = valor
        self.suit = naipe

    def get_rank(self):
        """Retorna valor"""
        return self.valor

    def get_suit(self):
        """Retorna naipe"""
        return self.suit

    def get_card(self):
        return '{}{}'.format(self.valor, self.suit)

    def __eq__(self, other):
        """self == other"""
        return self.valor == other.valor and self.suit == other.suit

    def __repr__(self):
        """retorna o valor legivel do objeto carta"""
        return '{}{}'.format(self.valor, self.suit)
