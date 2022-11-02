from random import shuffle
from cards import Card


class Baralho:
    """Representa um baralho de 52 cartas"""

    # valores e naipes são variáveis da classe Baralho
    valores = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

    # Naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self, jogo='any', cards=tuple(valores)):
        """Inicializa baralho"""
        self.baralho = []  # baralho está inicialmente vazio
        if jogo == 'any':
            for naipe in Baralho.naipes:  # naipes e valores são Baralho
                for valor in Baralho.valores:  # variáveis da classe
                    # Inclui Carta com certo valor e naipe no baralho
                    self.baralho.append(Card(valor, naipe).get_card())
            self.baralho.sort()

        else:
            for naipe in Baralho.naipes:
                for valor in cards:
                    self.baralho.append(Card(valor, naipe).get_card())
            self.baralho.sort()

    def distribui_carta(self, player):
        """Distribui (remove e retorna) carta do topo do baralho"""
        carta = self.baralho.pop()
        player.append(carta)
        return carta

    def embaralhar(self):
        """Mistura o baralho"""
        shuffle(self.baralho)

    def get(self):
        return self.baralho

    def __len__(self):
        """Mostra o tamanho da lista baralho, ou seja, quantas cartas o baralho tem"""
        return len(self.baralho)

    def __repr__(self):
        """Representação de string canônica de baralho"""
        return 'Baralho({})'.format(self.baralho)

    def __eq__(self, other):
        """Mostra se dois objetos baralhos são iguais"""
        return self.baralho == other.baralho
