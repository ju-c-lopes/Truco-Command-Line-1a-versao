from random import shuffle
from cards import Card, definir_peso


class Baralho:
    """Representa um baralho de 52 cartas"""

    # valores e naipes são variáveis da classe Baralho
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = ['espada', 'copas', 'ouro', 'paus']

    def __init__(self, jogo='any', cards=None):
        """Inicializa baralho"""
        print('\nPersonalizar a força das cartas?\n')
        definir_peso()
        self.baralho = []  # baralho está inicialmente vazio
        if jogo == 'any':
            for i in range(0, 4):  # iterar naipes do Baralho
                for j in range(0, 13):  # iterar valores do Baralho
                    # Inclui Carta com certo valor e naipe no baralho
                    carta = Card(Baralho.valores[j], Baralho.naipes[i])
                    self.baralho.append(carta)
            self.baralho.sort()

        else:
            for i in range(0, 4):  # naipes e valores são Baralho
                for j in cards:  # variáveis da classe
                    # Inclui Carta com certo valor e naipe no baralho
                    carta = Card(j, Baralho.naipes[i])
                    self.baralho.append(carta)
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
        ver_baralho = []
        for carta in self.baralho:
            ver_baralho.append(carta.printed_card())
        return ver_baralho

    def __len__(self):
        """Mostra o tamanho da lista baralho, ou seja, quantas cartas o baralho tem"""
        return len(self.baralho)

    def __repr__(self):
        """Representação de string canônica de baralho"""
        return 'Baralho({})'.format(Baralho.get(self))

    def __eq__(self, other):
        """Mostra se dois objetos baralhos são iguais"""
        return self.baralho == other.baralho
