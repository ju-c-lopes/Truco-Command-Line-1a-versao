from cards import Card


class Player:
    """Jogador de um jogo de baralho"""

    def __init__(self, nome, cartas):
        self.nome = nome
        self.cartas = cartas

    def __repr__(self):
        return self.nome
