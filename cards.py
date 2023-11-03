# def definir_peso():
#     """Configura o peso das cartas"""
#     definir = input('Alterar força -> digite (s)\nManter configuração -> digite (m)\nCancelar(c) ').lower()
#     if definir == 's':
#         print('Defina o peso para a sequência de cartas:')
#         for i in range(0, len(Card.valores)):
#             Card.valores[i][1] = int(input('{:>2}: '.format(Card.valores[i][0])))
#
#         for naipe, v in Card.naipes.items():
#             v[1] = int(input(f'Defina o peso do naipe {v[0]}: '))
#
#     elif definir == 'c':
#         Card.valores = [['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8],
#                         ['9', 9], ['10', 10], ['J', 11], ['Q', 12], ['K', 13], ['A', 14]]
#         Card.naipes = {'espada': ['\u2660', 2], 'copas': ['\u2665', 3],
#                        'ouro': ['\u2666', 1], 'paus': ['\u2663', 4]}
#     else:
#         pass
#
#     print('\n----------------OBS----------------'
#           '\nPara configurar a força das cartas, use o método definir_peso()'
#           '\nPara ver as cartas do baralho, digite <nome_do_baralho>.get()'
#           '\n')
#     input('Pressione qualquer tecla para continuar...')

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Card:
    """
    Representa uma carta do jogo

    OBS: para cada jogo, as cartas tem um peso próprio.
    a variável valores contém em cada índice uma lista de 2 índices, onde:
        -> o primeiro índice é o valor que a carta contém, e
        -> o segundo índice é o peso da carta
    Como cada jogo tem suas próprias regras, o peso deve ser configurado de maneira adequada
    para o jogo em questão.

    Nesta implementação, foi dado valores generalizados.
    """
    
    valores = [['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['10', 10],
               ['J', 11], ['Q', 12], ['K', 13], ['A', 14]]
    naipes = {'espada': ['\u2660', 2], 'copas': ['\u2665', 3], 'ouro': ['\u2666', 1], 'paus': ['\u2663', 4]}

    def __init__(self, valor, naipe):
        """Inicializa valor e naipe da carta do jogo"""
        if valor is not None:
            for carta in Card.valores:
                # print(isinstance(valor, list))
                if valor in carta and not isinstance(valor, list):
                    self.valor = carta
                else:
                    self.valor = valor
            #print(naipe)
            if naipe is not None and not isinstance(naipe, list):
                self.naipe = Card.naipes[naipe]
            else:
                self.naipe = naipe

    def get_valor(self):
        """Retorna valor"""
        return self.valor[1]

    def get_naipe(self):
        """Retorna naipe"""
        return self.naipe[1]

    def get_card(self):
        return self.valor, self.naipe

    def printed_card(self):

        if self.naipe[0] == '\u2666' or self.naipe[0] == '\u2665':
            return Fore.RED + Back.WHITE + f'{self.valor[0]}{self.naipe[0]}' + Fore.RESET + Back.RESET
        else:
            return Fore.BLACK + Back.WHITE + f'{self.valor[0]}{self.naipe[0]}' + Fore.RESET + Back.RESET

    def __repr__(self):
        """retorna o valor legivel do objeto carta"""
        return '{}'.format(self.printed_card())

    def __gt__(self, other):
        """Comparar se uma carta é maior que outra"""
        if self.get_valor() != other.get_valor():
            return self.get_valor() > other.get_valor()
        else:
            return self.get_naipe() > other.get_naipe()

    def __ge__(self, other):
        """Comparar se uma carta é maior ou igual a outra e se não é manilha"""
        if self.get_valor() == other.get_valor() and self.get_valor() != 11:
            return True
        return False
