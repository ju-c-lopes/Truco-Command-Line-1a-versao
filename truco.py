from baralho import Baralho
from player import Player
from cards import Card

res_time_1, res_time_2 = 0, 0


def mostrar_mesa(p1, p2, p3, p4, tb):
    print('{:>8}{:>58}'.format('\u2593', '\u2593'))
    # format(player_1[0].printed_card(), player_3[0].printed_card()))
    print('{:>5}{:>64}'.format('\u2593', '\u2593'))
    # format(player_1[1].printed_card(), player_3[1].printed_card()))
    print('{:>2}{:>70}'.format('\u2593', '\u2593'))
    # format(player_1[2].printed_card(), player_3[2].printed_card()))
    print('\n\n')
    print('{:>32} | {} |'.format('', tb[0].printed_card()))
    print('\n\n')
    print('{:>2}{:>70}'.format('\u2593', '\u2593'))
    # format(player_2[2].printed_card(), player_4[2].printed_card()))
    print('{:>5}{:>64}'.format('\u2593', '\u2593'))
    # format(player_2[1].printed_card(), player_4[1].printed_card()))
    print('{:>8}{:>58}'.format('\u2593', '\u2593'))
    # format(player_2[0].printed_card(), player_4[0].printed_card()))


def truco():
    """Jogo de truco"""
    # valores = [["4", 1], ["5", 2], ["6", 3], ["7", 4], ["Q", 5],
    #            ["J", 6], ["K", 7], ["A", 8], ["2", 9], ["3", 10]]
    # naipes = {'ouro': ['\u2666', 1], 'espada': ['\u2660', 2],
    #           'copas': ['\u2665', 3], 'paus': ['\u2663', 4]}
    #
    # baralho = Baralho(valores, naipes)

    resposta = input('=========\nDupla?\n(s) para sim, (n) para não ')
    dupla = False
    if resposta == 's':
        dupla = True
    # implementar

    # a lista vazia representa o jogador esperando a receber cartas que serão dadas
    player_1 = Player('Marcos', [])   # input('Digite seu nome: '), [])
    player_2 = Player('Rogério', [])   # input('Digite seu nome: '), [])
    player_3 = Player('Anderson', [])   # input('Digite seu nome: '), [])
    player_4 = Player('Manoel', [])   # input('Digite seu nome: '), [])

    time_1 = [[player_1, player_3], res_time_1]
    time_2 = [[player_2, player_4], res_time_2]

    jogadores = [player_1, player_2, player_3, player_4]

    if dupla:
        jogo = [time_1, time_2]
        while jogo[0][1] < 12 or jogo[1][1] < 12:
            print(f'\ntime 1: {jogo[0][1]} pts\ntime 2: {jogo[1][1]} pts\n')
            input('Pressione enter para continuar...')
            jogar(jogadores, jogo)

    print('\nACABOU ! ! !')

    # rodada(jogadores)


def jogar(jogadores, jogo):
    # distribuir cartas
    valores = [["4", 1], ["5", 2], ["6", 3], ["7", 4], ["Q", 5],
               ["J", 6], ["K", 7], ["A", 8], ["2", 9], ["3", 10]]
    naipes = {'ouro': ['\u2666', 1], 'espada': ['\u2660', 2],
              'copas': ['\u2665', 3], 'paus': ['\u2663', 4]}

    baralho = Baralho(valores, naipes)
    baralho.embaralhar()

    # Distribuição das cartas, 3 para cada jogador
    for i in range(0, 3):
        baralho.distribui_carta(jogadores[0].cartas)
        baralho.distribui_carta(jogadores[1].cartas)
        baralho.distribui_carta(jogadores[2].cartas)
        baralho.distribui_carta(jogadores[3].cartas)

    tombo = Card(["3", 10], ['\u2666', 1])
    # baralho.distribui_carta(tombo)

    # verificar manilhas
    for i in range(0, 3):
        print(tombo.valor[0])

        if tombo.valor[0] == '3':
            if jogadores[0].cartas[i].valor[0] == '4':
                jogadores[0].cartas[i] = 11
        elif jogadores[0].cartas[i].valor[1] == tombo.valor[1] + 1:
            jogadores[0].cartas[i].valor[1] = 11

        if tombo.valor[0] == '3':
            if jogadores[1].cartas[i].valor[0] == '4':
                jogadores[1].cartas[i] = 11
        elif jogadores[1].cartas[i].valor[1] == tombo.valor[1] + 1:
            jogadores[1].cartas[i].valor[1] = 11

        if tombo.valor[0] == '3':
            if jogadores[2].cartas[i].valor[0] == '4':
                jogadores[2].cartas[i] = 11
        elif jogadores[2].cartas[i].valor[1] == tombo.valor[1] + 1:
            jogadores[2].cartas[i].valor[1] = 11

        if tombo.valor[0] == '3':
            if jogadores[3].cartas[i].valor[0] == '4':
                jogadores[3].cartas[i] = 11
        elif jogadores[3].cartas[i].valor[1] == tombo.valor[1] + 1:
            jogadores[3].cartas[i].valor[1] = 11

    p1, p2 = 0, 0
    for i in range(0, 3):
        mesa = volta(jogadores)
        maior = mesa[-1]
        for j in range(len(mesa) - 1):
            if mesa[j][0] > maior[0]:  # IMPLEMENTAR MAIOR OU IGUAL
                maior = mesa[j]

        if maior[1] in jogo[0][0]:
            jogo[0][1] += 1
            p1 += 1
            print(jogo[0][1])
        elif maior[1] in jogo[1][0]:
            jogo[1][1] += 1
            p2 += 1
            print(jogo[1][1])

        print(f'Rodada {i + 1} terminou\n'
              f'Mesa: {mesa}\n'
              f'Tombo: {tombo}\n'
              f'Maior: {maior}\n'
              f'times: {jogo}\n'
              f'\np1: {p1} | p2: {p2}')

        for k in range(4):
            if tombo.valor[0] == '3' and mesa[k][0].valor[0] == '4':
                print('----------------QUATRO________________\n')

        input('\nPressione enter pra continuar...')
        if p1 == 2 or p2 == 2:
            break

    for i in range(0, 4):
        jogadores[i].cartas = []
    return jogo[0][1], jogo[1][1]


def volta(jogadores):

    mesa = []

    for i in range(0, 4):

        print(f'\n{jogadores[i].nome.upper()} joga:\n')
        acao = input('AGUARDANDO RESPOSTA...\n'
                     'digite:(j) para jogar carta / '
                     '(t) para truco / (f) para fugir')
        if acao == 't':
            chamar_truco(jogadores, i, mesa)
        elif acao == 'j' or acao == '':
            if len(jogadores[i].cartas) != 1:
                escolha = int(input(f'Qual das {str(len(jogadores[i].cartas))} '
                              'você quer jogar? '))
                carta = [jogadores[i].cartas.pop(escolha - 1),    # (int(escolha) - 1),
                         jogadores[i]]
                mesa.append(carta)
                print('\n{:>15} jogou a carta\n{:>55}'
                      .format(jogadores[i].nome, carta[0].printed_card()))
            else:
                carta = [jogadores[i].cartas.pop(), jogadores[i]]
                mesa.append(carta)
                print('\n{:>15} jogou a carta\n{:>55}'
                      .format(jogadores[i].nome, carta[0].printed_card()))
        else:
            return  # 1, jogadores[i]

    return mesa


def chamar_truco(jogadores, i, mesa):
    print('OBSERVA')
    print(f'{jogadores[i - 1].nome} aceita? ')
    acao = input('digite: (recusa) / (aceita) / (seis)')
    if acao == 'seis':
        chamar_seis(jogadores, i, mesa)
    elif acao == 'aceita':
        print(f'{jogadores[i - 1].nome} aceitou.\n\n'
              f'{jogadores[i].nome}\n')
        escolha = input(f'Qual das {str(len(jogadores[i].cartas))} '
                        'você quer jogar? ')
        mesa.append(jogadores[i].cartas.pop(int(escolha) - 1))


def chamar_seis(jogadores, i, mesa):
    print(f'{jogadores[i].nome} aceita? ')
    acao = input('digite: (recusa) / (aceita) / (nove)')
    if acao == 'nove':
        chamar_nove(jogadores, i, mesa)
    elif acao == 'aceita':
        mesa.append(jogadores[i].cartas.pop())
    else:
        pass


def chamar_nove(jogadores, i, mesa):
    print(f'{jogadores[i - 1].nome} aceita? ')
    acao = input('digite: (recusa) / (aceita) / (doze)')
    if acao == 'doze':
        chamar_doze(jogadores, i, mesa)
    elif acao == 'aceita':
        mesa.append(jogadores[i].cartas.pop())
    else:
        pass


def chamar_doze(jogadores, i, mesa):

    print(f'{jogadores[i - 1].nome} aceita? ')
    acao = input('digite: (recusa) / (aceita)')
    if acao == 'aceita':
        mesa.append(jogadores[i].cartas.pop())
    else:
        pass
