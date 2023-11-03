from cards import Card


class Player:
    """Jogador de um jogo de baralho"""

    def __init__(self, nome, cartas, time=None):
        self.nome = nome
        self.cartas = cartas
        self.acao = {
            '3': False,
            '6': False,
            '9': False,
            '12': False
        }
        self.time = time
        
    def reiniciar_acao(self):
        for k in self.acao.keys():
            self.acao[k] = False
        
    def __repr__(self):
        return self.nome
