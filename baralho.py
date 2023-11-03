from random import shuffle
from cards import Card


def definir_peso():
    """Configura o peso das cartas"""
    definir = input('Alterar força -> digite (s)\nManter configuração -> digite (m)\nCancelar(c) ').lower()
    if definir == 's':
        print('Defina o peso para a sequência de cartas:')
        for i in range(0, len(Card.valores)):
            Card.valores[i][1] = int(input('{:>2}: '.format(Card.valores[i][0])))

        for naipe, v in Card.naipes.items():
            v[1] = int(input(f'Defina o peso do naipe {v[0]}: '))

    elif definir == 'c':
        Card.valores = [
            ['2', 2],
            ['3', 3], 
            ['4', 4], 
            ['5', 5], 
            ['6', 6], 
            ['7', 7], 
            ['8', 8],
            ['9', 9], 
            ['10', 10], 
            ['J', 11], 
            ['Q', 12], 
            ['K', 13], 
            ['A', 14]
        ]
        Card.naipes = {
            'espada': ['\u2660', 2],
            'copas': ['\u2665', 3],
            'ouro': ['\u2666', 1],
            'paus': ['\u2663', 4]
        }
    else:
        pass

    print('\n----------------OBS----------------'
          '\nPara configurar a força das cartas, use o método definir_peso()'
          '\nPara ver as cartas do baralho, digite <nome_do_baralho>.get()'
          '\n')
    input('Pressione qualquer tecla para continuar...')


class Baralho:
    """Representa um baralho de 52 cartas"""

    # valores e naipes são variáveis da classe Baralho
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = ['espada', 'copas', 'ouro', 'paus']

    def __init__(self, val=None, naipes=None):
        """Inicializa baralho"""
        #self.baralho = []  # baralho está inicialmente vazio
        if val is None:
            self.baralho = [Card(Baralho.valores[j], Baralho.naipes[i]) for i in range(4) for j in range(len(Baralho.valores))]
            self.baralho.sort()
        else:
            #print(naipes)
            self.baralho = []
            for naipe in naipes:  # iterar naipes do Baralho
                #print('Valor', val) APAGAR
                #print('Naipe: ', naipe) APAGAR
                
                for j in range(0, len(val)):  # iterar valores do Baralho
                    # Inclui Carta com certo valor e naipe no baralho
                    #print(naipes[naipe])
                    carta = Card(val[j], naipe)
                    self.baralho.append(carta)
            self.baralho.sort()

    def distribui_carta(self, player):
        """Distribui (remove e retorna) carta do topo do baralho"""
        carta = self.baralho.pop()
        player.append(carta)
        #print('def distribui carta: ',carta.get_valor(), carta.get_naipe()) APAGAR
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
