from baralho import Baralho
from player import Player
# from cards import Card
from colorama import Fore, Back

res_time_1, res_time_2 = 0, 0


def mostrar_mesa(mesa, tb, i, rodada):
    def linha2(i):
        if rodada > 0:
            print(Back.YELLOW + Fore.YELLOW + ('{}'.format('\u2593')) * 40 + Back.RESET)
        elif i == 0 and mesa[0][2]:
            print(
                Back.YELLOW + 
                '{:>10}{}'.format(' ', mesa[0][0].printed_card()) + 
                Back.YELLOW + Fore.BLUE +
                '{:>21}{}'.format(' ', '\u2593' * 2) + 
                Back.YELLOW + '{:>5}'.format(' ') +
                Back.RESET + Fore.RESET)
        elif i >= 1 and mesa[i][2]:
            print(
                Back.YELLOW + 
                '{:>10}{}'.format(' ', mesa[0][0].printed_card()) + 
                Back.YELLOW + 
                '{:>16}{}'.format(' ', mesa[1][0].printed_card()) + 
                Back.YELLOW + '{:>10}'.format(' ') +
                Back.RESET)
        else:
            print(
                Back.YELLOW + Fore.BLUE + 
                '{:>7}{:>28}{:>5}'.format('\u2593' * 2, '\u2593' * 2, ' ') + 
                Back.RESET)
    
    def linha3(i):
        if rodada > 1:
            print('{:>7}'.format(' '), end="")
            print(
                Back.YELLOW + Fore.YELLOW + 
                ('{}'.format('\u2593')) * 40 + 
                Back.RESET)
        elif rodada == 1 and i == 0 and mesa[0][2]:
            print('{:>7}'.format(' '), end="")
            print(
                Back.YELLOW + 
                '{:>8}{}'.format(' ',  mesa[0][0].printed_card()) + 
                Back.YELLOW + Fore.BLUE + 
                '{:>27}{:>3}'.format('\u2593' * 2, ' ') + 
                Back.RESET + Fore.RESET)
        elif rodada == 1 and i >= 1 and mesa[1][2]:
            print('{:>7}'.format(' '), end="")
            print(
                Back.YELLOW + 
                '{:>8}{}'.format(' ', mesa[0][0].printed_card()) + 
                Back.YELLOW + '{:>20}{}'.format(' ', mesa[1][0].printed_card()) + 
                Back.YELLOW + '{:>8}'.format(' ') + Back.RESET)
        else:
            print('{:>7}'.format(' '), end="")
            print(
                Back.YELLOW + Fore.BLUE + 
                '{:>5}{:>32}{:>3}'.format('\u2593' * 2, '\u2593' * 2, ' ') + 
                Back.RESET)
        #print('{:>7}'.format(' '), end="")

    def linha4(i):
        if rodada < 2:
            print('{:>7}'.format(' '), end="")
            print(Back.YELLOW + Fore.BLUE + '{:>3}{:>36}{:>1}'.format('\u2593' * 2, '\u2593' * 2, ' ') + Back.RESET)
        elif rodada == 2 and i == 0 and mesa[0][2]:
            print('{:>7}'.format(' '), end="")
            print(
                Back.YELLOW + 
                '{:>8}{}'.format(' ',  mesa[0][0].printed_card()) + 
                Back.YELLOW + Fore.BLUE + 
                '{:>29}{:>1}'.format('\u2593' * 2, ' ') + 
                Back.RESET + Fore.RESET)
        elif rodada == 2 and i >= 1 and mesa[1][2]:
            print('{:>7}'.format(' '), end="")
            print(
                Back.YELLOW + 
                '{:>8}{}'.format(' ', mesa[0][0].printed_card()) + 
                Back.YELLOW + '{:>22}{}'.format(' ', mesa[1][0].printed_card()) + 
                Back.YELLOW + '{:>6}'.format(' ') + Back.RESET)

    def print_tombo():
        print('{:>7}'.format(' '), end="")
        print(Back.YELLOW + Fore.YELLOW + ('{}'.format('\u2593')) * 40 + Back.RESET)
        print('{:>7}'.format(' '), end="")
        # format(player_1[1].printed_card(), player_3[1].printed_card()))
        print(Back.YELLOW + '{:>16}   {}'.format(' ', tb.printed_card()) + Back.YELLOW + '{:>19}'.format(' ') + Back.RESET)
        print('{:>7}'.format(' '), end="")
        print(Back.YELLOW + Fore.YELLOW + ('{}'.format('\u2593')) * 40 + Back.RESET)
        print('{:>7}'.format(' '), end="")

    def linha7(i):
        if (i < 2 and rodada == 2) or rodada < 2:
            print(Back.YELLOW + Fore.BLUE + '{:>3}{:>36}{:>1}'.format('\u2593' * 2, '\u2593' * 2, ' ') + Back.RESET)
            print('{:>7}'.format(' '), end="")
        elif rodada == 2 and i == 2 and mesa[2][2]:
            print(
                Back.YELLOW + Fore.BLUE +
                '{:>1}{}'.format(' ', '\u2593' * 2) + 
                Back.YELLOW + '{:>29}{}'.format(' ', mesa[2][0].printed_card()) + 
                Back.YELLOW + '{:>6}'.format(' ') + 
                Back.RESET + Fore.RESET)
            print('{:>7}'.format(' '), end="")
        elif rodada == 2 and i == 3 and mesa[3][2]:
            print(
                Back.YELLOW + 
                '{:>8}{}'.format(' ', mesa[3][0].printed_card()) + 
                Back.YELLOW + '{:>22}{}'.format(' ', mesa[2][0].printed_card()) + 
                Back.YELLOW + '{:>6}'.format(' ') + Back.RESET)
            print('{:>7}'.format(' '), end="")
        # print(Back.YELLOW + Fore.BLUE + '{:>3}{:>36}{:>1}'.format('\u2593' * 2, '\u2593' * 2, ' ') + Back.RESET)
        # print('{:>7}'.format(' '), end="")

    def linha8(i):
        if rodada > 1:
            print(Back.YELLOW + Fore.YELLOW + ('{}'.format('\u2593')) * 40 + Back.RESET)
            print('{:>7}'.format(' '), end="")
        elif rodada == 1 and i == 2 and mesa[2][2]:
            print(
                Back.YELLOW + Fore.BLUE +
                '{:>3}{}'.format(' ', '\u2593' * 2) + 
                Back.YELLOW + Fore.BLUE + 
                '{:>25}{}'.format(' ',  mesa[2][0].printed_card()) + 
                Back.YELLOW + '{:>8}'.format(' ') +
                Back.RESET + Fore.RESET)
            print('{:>7}'.format(' '), end="")
        elif rodada == 1 and i == 3 and mesa[3][2]:
            print(
                Back.YELLOW + 
                '{:>8}{}'.format(' ',  mesa[3][0].printed_card()) + 
                Back.YELLOW +
                '{:>20}{}'.format(' ',  mesa[2][0].printed_card()) + 
                Back.YELLOW + '{:>8}'.format(' ') +
                Back.RESET)
            print('{:>7}'.format(' '), end="")
        else:
            print(Back.YELLOW + Fore.BLUE + '{:>5}{:>32}{:>3}'.format('\u2593' * 2, '\u2593' * 2, ' ') + Back.RESET)
            print('{:>7}'.format(' '), end="")
            
    def linha9(i):
        if rodada > 0:
            print(Back.YELLOW + Fore.YELLOW + ('{}'.format('\u2593')) * 40 + Back.RESET)
        elif i < 2:
            print(
                Back.YELLOW + Fore.BLUE + 
                '{:>7}{:>28}{:>5}'.format('\u2593' * 2, '\u2593' * 2, ' ') + 
                Back.RESET)
        elif i == 2 and mesa[2][2]:
            # linha2(i - 1)
            print(
                Back.YELLOW + Fore.BLUE +
                '{:>5}{}'.format(' ', '\u2593' * 2) + 
                Back.YELLOW + 
                '{:>21}{}'.format(' ', mesa[2][0].printed_card()) + 
                Back.YELLOW + '{:>10}'.format(' ') +
                Back.RESET)
        elif i == 3 and mesa[3][2]:
            print(
                Back.YELLOW + 
                '{:>10}{}'.format(' ', mesa[3][0].printed_card()) + 
                Back.YELLOW + 
                '{:>16}{}'.format(' ', mesa[2][0].printed_card()) + 
                Back.YELLOW + '{:>10}'.format(' ') +
                Back.RESET + Fore.RESET)

    #-------------------------------------------- IMPRIMINDO MESA --------------------------------------------------
    print(mesa[0][1].nome, '{:>40}'.format(' '), mesa[1][1].nome if len(mesa) > 2 else '')
    print('{:>7}'.format(' '), end="")

    print(Back.YELLOW + Fore.YELLOW + ('{}'.format('\u2593')) * 40 + Back.RESET)
    print('{:>7}'.format(' '), end="")

    #---------------------------------------------------------------------------------------------------------------
    linha2(i)
    linha3(i)
    linha4(i)
    print_tombo()
    linha7(i)
    linha8(i)
    linha9(i)
    #---------------------------------------------------------------------------------------------------------------

    print('{:>7}'.format(' '), end="")
    print(Back.YELLOW + Fore.YELLOW + ('{}'.format('\u2593')) * 40 + Back.RESET)
    print(mesa[3][1].nome if len(mesa) > 2 else '', '{:>40}'.format(' '), mesa[2][1].nome if len(mesa) > 2 else mesa[1][1].nome)


def truco():
    """Jogo de truco"""

    resposta = input('=========\nDupla?\n(s) para sim, (n) para não ').lower()
    dupla = True if resposta == 's' else False

    # a lista vazia representa o jogador esperando a receber cartas que serão distribuídas
    player_1 = Player(nome='Marcos', cartas=[], time=0)   # input('Digite seu nome: '), [])
    player_2 = Player(nome='Rogério', cartas=[], time=1)   # input('Digite seu nome: '), [])
    player_3 = Player(nome='Anderson', cartas=[], time=0)   # input('Digite seu nome: '), [])
    player_4 = Player(nome='Manoel', cartas=[], time=1)   # input('Digite seu nome: '), [])

    if dupla:
        time_1 = [
            [
                player_1, 
                player_3
            ],
            res_time_1
        ]
        time_2 = [
            [
                player_2, 
                player_4
            ],
            res_time_2
        ]
        
        jogadores = [
            player_1,
            player_2,
            player_3,
            player_4,
        ]

        jogo = [
            time_1, 
            time_2
        ]
    else:
        time_1 = [
            [player_1], 
            res_time_1
        ]
        time_2 = [
            [player_2], 
            res_time_2
        ]
        
        jogadores = [
            player_1,
            player_2
        ]

        jogo = [
            time_1, 
            time_2
        ]

    # Inicio do jogo após a definição dos jogadores
    # Enquanto a pontuação de qualquer um dos times não for igual ou superar 12 pontos, o jogo continua
    while jogo[0][1] < 12 and jogo[1][1] < 12:
        print("condição while principal")
        print(f'\ntime 1: {jogo[0][1]} pts\ntime 2: {jogo[1][1]} pts\n')
        input('Pressione enter para continuar...')
        jogar(jogadores, jogo)
        # Implementar a rotatividade a cada rodada entre jogadores
        troca = []
        for i in range(len(jogadores)):
            troca.append(jogadores[(i + 1) % len(jogadores)])
        jogadores = troca
        # mostrar_mesa()

    print('\nACABOU ! ! !')

    # rodada(jogadores)


def jogar(jogadores, jogo):
    # distribuir cartas
    valores = [
        ["4", 1], 
        ["5", 2], 
        ["6", 3], 
        ["7", 4], 
        ["Q", 5],
        ["J", 6], 
        ["K", 7], 
        ["A", 8], 
        ["2", 9], 
        ["3", 10]
    ]
    naipes = {
        'ouro': ['\u2666', 1], 
        'espada': ['\u2660', 2],
        'copas': ['\u2665', 3], 
        'paus': ['\u2663', 4]
    }

    baralho = Baralho(valores, naipes)
    baralho.embaralhar()

    # Distribuição das cartas, 3 para cada jogador
    for _ in range(3):
        baralho.distribui_carta(jogadores[0].cartas)
        baralho.distribui_carta(jogadores[1].cartas)
        if len(jogadores) > 2:
            baralho.distribui_carta(jogadores[2].cartas)
            baralho.distribui_carta(jogadores[3].cartas)
    print(jogadores[0].nome, ': ', jogadores[0].cartas) # APAGAR
    print(jogadores[1].nome, ': ', jogadores[1].cartas) # APAGAR
    if len(jogadores) > 2:
        print(jogadores[2].nome, ': ', jogadores[2].cartas) # APAGAR
        print(jogadores[3].nome, ': ', jogadores[3].cartas) # APAGAR
    
    tombo = Player('mesa', [])
    tombo = baralho.distribui_carta(tombo.cartas)
    
    # mao fará o re-cálculo dos pesos das cartas de acordo com o tombo
    mao(tombo, jogadores)

    print()
    mostrar_mesa([[0, jogadores[i], 0] for i in range(len(jogadores))], tombo, 0, 0)

    p1, p2 = 0, 0  # Pontos para controlar quem está ganhando a rodada
    empate, mostrar_maior = False, False
    jogadores_aux = jogadores.copy()
    pontos = 1
    for i in range(3):
        pontos = pontos
        print(pontos)
        mesa = volta(jogadores_aux, tombo, i, pontos)
        
        # If caso retorno da mesa seja uma fuga
        if isinstance(mesa[0], Player):
            print('\n\nRetornou Jogador que fugiu: ', mesa[0], ' pontos: ', mesa[1])
            # verifica jogador que fugiu e pontua para o outro time
            # mesa[0] é o jogador
            # mesa[1] são os pontos
            if mesa[0] in jogo[0][0]:
                jogo[1][1] += mesa[1]
            else:
                jogo[0][1] += mesa[1]
            break

        mesa_aux = mesa[0].copy()
        pontos = mesa[1]
        print("mesa depois de volta + pontos: ", mesa, pontos)
        maior = None

        # Ver jogo amarrado (empate) ou definiar a maior
        if ver_amarrado(mesa_aux):
            print('amarrou')
            empate = True
        else:
            maior = max(mesa_aux)
            mostrar_maior = True if empate else False
        
        if empate and not mostrar_maior and p1 == 0 and p2 == 0:
            continue
        elif empate and (p1 == 1 or p2 == 1):
            if p1 == 1:
                p1 += 1
            else:
                p2 += 1
        
            # maior[1] é o nome do jogador que está com carta maior
            # jogo[0][x] é o time que receberá a pontuação
        elif maior[1] in jogo[0][0]:
            print("jogo[0][0] ", jogo[0][0])
            #jogo[0][1] += 1
            p1 += 1
            print(jogo[0][1])
        elif maior[1] in jogo[1][0]:
            print("jogo[0][1]", jogo[0][1])
            #jogo[1][1] += 1
            p2 += 1
            print(jogo[1][1])

        print(f'Rodada {i + 1} terminou\n'
              f'Mesa: {mesa}\n'
              f'tombo: {tombo}\n'
              f'Maior: {maior}\n'
              f'times: {jogo}\n'
              f'\np1: {p1} | p2: {p2}')

        #print("\nPrintando mesa 0: ", mesa[0][0])
        # APAGAR
        for k in range(len(jogadores)):
            #for c in range()
            if tombo.valor[0] == '3' and mesa[0][k][0].valor[0] == '4':
                print('----------------QUATRO________________\n') #APAGAR


        input('\nPressione enter pra continuar...')
        if empate and (p1 == 1 or p2 == 1):
            if p1 > p2:
                jogo[0][1] += pontos
            else:
                jogo[1][1] += pontos
            break
        if p1 == 2 or p2 == 2:
            if p1 > p2:
                jogo[0][1] += pontos
            else:
                jogo[1][1] += pontos
            break

        print()
        #print(f'Rodada {i + 1} terminou\n'
              #f'Mesa: {mesa}\n'
              #f'tombo: {tombo}\n'
              #f'Maior: {maior}\n'
              #f'times: {jogo}\n'
              #f'\np1: {p1} | p2: {p2}')
        # mostrar_mesa(mesa[0], mesa[1], mesa[2], mesa[3], tombo)

        proxima_rodada = jogadores_aux.index(maior[1])
        jogadores_troca = []
        for i in range(len(jogadores_aux)):
            jogadores_troca.append(jogadores_aux[(i + 1 + proxima_rodada) % len(jogadores_aux)])
        jogadores_aux = jogadores_troca

    # esvaziar cartas dos jogadores e zerar acoes
    for i in range(len(jogadores)):
        jogadores[i].reiniciar_acao()
        jogadores[i].cartas = []


def volta(jogadores, tombo, rodada, pts):

    pontos = pts
    mesa = [[] for _ in range(len(jogadores))]

    for i in range(len(jogadores)):

        print(f'{jogadores[i]}\n\n{jogadores[i].nome.upper()} joga:\n')
        acao_truco = verificar_acao(jogadores, i)
        ac = acao_truco[0]
        chamada_acao = acao_truco[1]
        
        print(chamada_acao, end="")
        acao = input()
                     
        while acao != ac and 'j' and acao != 'f' and acao != '':
            print(chamada_acao, end="")
            acao = input()

        if acao == 't':
            trucada = chamar_truco(jogadores, i, mesa, pts)
            pontos = trucada[0]
            print("-"*10, "OBSERVAR", "-"*10)
            print("Chamou truco, ver pontos: ", pontos)
            acao = trucada[1]
            jogadores[i].acao['3'] = True
            if len(jogadores) > 2:
                jogadores[(i + 2) % len(jogadores)].acao['3'] = True

            # if not em caso a ação for uma recusa ou fuga
            # o i aponta para o jogador que fugiu
            if not acao:
                i = (i + 1) % len(jogadores)
        elif acao == 's':
            trucada = chamar_seis(jogadores, i, mesa, pts)
            pontos = trucada[0]
            print("-"*10, "OBSERVAR", "-"*10)
            print("Chamou seis, ver pontos: ", pontos)
            acao = trucada[1]
            jogadores[i].acao['3'] = False
            jogadores[i].acao['6'] = True
            jogadores[(i + 1) % len(jogadores)].acao['3'] = False
            if len(jogadores) > 2:
                jogadores[(i + 2) % len(jogadores)].acao['3'] = False
                jogadores[(i + 2) % len(jogadores)].acao['6'] = True
                jogadores[(i + 3) % len(jogadores)].acao['3'] = False

            # if not em caso a ação for uma recusa ou fuga
            # o i aponta para o jogador que fugiu
            if not acao:
                i = (i + 1) % len(jogadores)
        elif acao == 'n':
            trucada = chamar_seis(jogadores, i, mesa, pts)
            pontos = trucada[0]
            print("-"*10, "OBSERVAR", "-"*10)
            print("Chamou seis, ver pontos: ", pontos)
            acao = trucada[1]
            jogadores[i].acao['6'] = False
            jogadores[i].acao['9'] = True
            jogadores[(i + 1) % len(jogadores)].acao['6'] = False
            if len(jogadores) > 2:
                jogadores[(i + 2) % len(jogadores)].acao['6'] = False
                jogadores[(i + 2) % len(jogadores)].acao['9'] = True
                jogadores[(i + 3) % len(jogadores)].acao['6'] = False

            # if not em caso a ação for uma recusa ou fuga
            # o i aponta para o jogador que fugiu
            if not acao:
                i = (i + 1) % len(jogadores)
        elif acao == 'd':
            trucada = chamar_seis(jogadores, i, mesa, pts)
            pontos = trucada[0]
            print("-"*10, "OBSERVAR", "-"*10)
            print("Chamou seis, ver pontos: ", pontos)
            acao = trucada[1]
            jogadores[i].acao['9'] = False
            jogadores[i].acao['12'] = True
            jogadores[(i + 1) % len(jogadores)].acao['9'] = False
            if len(jogadores) > 2:
                jogadores[(i + 2) % len(jogadores)].acao['9'] = False
                jogadores[(i + 2) % len(jogadores)].acao['12'] = True
                jogadores[(i + 3) % len(jogadores)].acao['9'] = False

            # if not em caso a ação for uma recusa ou fuga
            # o i aponta para o jogador que fugiu
            if not acao:
                i = (i + 1) % len(jogadores)
        if acao == 'j' or acao == '':
            if len(jogadores[i].cartas) != 1:
                indice = int()

                while True:
                    escolha = input(f'Qual das {str(len(jogadores[i].cartas))} você quer jogar? ')
                    try:
                        escolha = int(escolha)
                        if escolha in range(1, len(jogadores[i].cartas) + 1):
                            break
                    except:
                        if escolha == '':
                            escolha = len(jogadores[i].cartas)
                            break
                        else:
                            print('Você precisa escolher uma carta entre 1 e ', end="")
                            for x in range(1, len(jogadores[i].cartas) + 1):
                                print(f'{x}, ', end="")
                            print()

                for j in range(len(jogadores)):
                    if j == i:
                        carta = [jogadores[j].cartas.pop(escolha - 1), jogadores[j], True]
                        indice = j
                    elif j > i:
                        carta = [None, jogadores[j], False]
                        # mesa.append(carta)
                    else:
                        carta = mesa[j]
                    mesa[j] = carta
                    
                mostrar_mesa(mesa, tombo, indice, rodada)
            else:
                indice = int()
                for j in range(len(jogadores)):
                    if j == i:
                        carta = [jogadores[j].cartas.pop(), jogadores[j], True]
                        indice = j
                    elif j > i:
                        carta = [None, jogadores[j], False]
                    else:
                        carta = mesa[j]
                    mesa[j] = carta
                    
                print("-" * 60)
                mostrar_mesa(mesa, tombo, indice, rodada)
        else: # IMPLEMENTAR para fugir (f)
            return [jogadores[i], pontos]

    return [mesa, pontos]


def chamar_truco(jogadores, i, mesa, pts):
    pontos = pts
    print('OBSERVA')
    print(f'{jogadores[(i + 1) % len(jogadores)].nome} aceita? ')
    acao = input('digite: (r) para recusar / (a) para aceitar / (s) para chamar seis: ').lower()
    for j in range(2):
        if j == 0:
            jogador = jogadores[(i + 1) % len(jogadores)]
        else:
            jogador = jogadores[(i + 3) % len(jogadores)]
        if acao == 's':
            seis = chamar_seis(jogadores, i, mesa, 3)
            pontos = seis[0]
            continuar = seis[1]
            break
        elif acao == 'a' or acao == '':
            print(f'{jogador.nome} aceitou.\n\n')
            pontos = 3
            continuar = 'j'
            break
        elif acao == 'r':
            print(f'{jogadores[(i + 3) % len(jogadores)].nome} aceita? ')
            acao = input('digite: (r) para recusar / (a) para aceitar / (s) para chamar seis: ').lower()
            if acao == 'r':
                continuar = False
                break
    return (pontos, continuar)


def chamar_seis(jogadores, i, mesa, pts):
    pontos = pts
    print('OBSERVA')
    print(f'{jogadores[(i + 1) % len(jogadores)].nome} aceita? ')
    acao = input('digite: (r) para recusar / (a) para aceitar / (n) para chamar nove: ').lower()
    
    # Loop for para ver ação do outro time
    for j in range(2):
        if j == 0:
            jogador = jogadores[(i + 1) % len(jogadores)]
        else:
            jogador = jogadores[(i + 3) % len(jogadores)]
        if acao == 'n':
            nove = chamar_nove(jogadores, i, mesa, 6)
            pontos = nove[0]
            continuar = nove[1]
            break
        elif acao == 'a' or acao == '':
            print(f'{jogador.nome} aceitou.\n\n')
            pontos = 6
            continuar = 'j'
            break
        elif acao == 'r':
            print(f'{jogadores[(i + 3) % len(jogadores)].nome} aceita? ')
            acao = input('digite: (r) para recusar / (a) para aceitar / (n) para chamar nove: ').lower()
            if acao == 'r':
                continuar = False
                break
    return (pontos, continuar)


def chamar_nove(jogadores, i, mesa, pts):
    pontos = pts
    print('OBSERVA')
    print(f'{jogadores[(i + 1) % len(jogadores)].nome} aceita? ')
    acao = input('digite: (r) para recusar / (a) para aceitar / (d) para chamar doze: ').lower()
    
    # Loop for para ver ação do outro time
    for j in range(2):
        if j == 0:
            jogador = jogadores[(i + 1) % len(jogadores)]
        else:
            jogador = jogadores[(i + 3) % len(jogadores)]
        if acao == 'd':
            doze = chamar_doze(jogadores, i, mesa, 9)
            pontos = doze[0]
            continuar = doze[1]
            break
        elif acao == 'a' or acao == '':
            print(f'{jogador.nome} aceitou.\n\n')
            pontos = 9
            continuar = 'j'
            break
        elif acao == 'r':
            print(f'{jogadores[(i + 3) % len(jogadores)].nome} aceita? ')
            acao = input('digite: (r) para recusar / (a) para aceitar / (d) para chamar doze: ').lower()
            if acao == 'r':
                continuar = False
                break
    return (pontos, continuar)


def chamar_doze(jogadores, i, mesa, pts):
    pontos = pts
    print('OBSERVA')
    print(f'{jogadores[(i + 1) % len(jogadores)].nome} aceita? ')
    acao = input('digite: (r) para recusar / (a) para aceitar: ').lower()
    
    # Loop for para ver ação do outro time
    for j in range(2):
        if j == 0:
            jogador = jogadores[(i + 1) % len(jogadores)]
        else:
            jogador = jogadores[(i + 3) % len(jogadores)]
        if acao == 'a' or acao == '':
            print(f'{jogador.nome} aceitou.\n\n')
            pontos = 12
            continuar = 'j'
            break
        elif acao == 'r':
            print(f'{jogadores[(i + 3) % len(jogadores)].nome} aceita? ')
            acao = input('digite: (r) para recusar / (a) para aceitar: ').lower()
            if acao == 'r':
                continuar = False
                break
    return (pontos, continuar)


def mao(tombo, jogadores):

    # verificar manilhas
    for jogador in jogadores:
        for i in range(0, 3):

            if tombo.valor[0] == '3':
                if jogador.cartas[i].valor[0] == '4':
                    jogador.cartas[i].valor[1] = 11
                    print('maior tombo 3')
            elif jogador.cartas[i].valor[1] == tombo.valor[1] + 1:
                print('definido maior')
                #continue
                jogador.cartas[i].valor[1] = 11
            #print(jogador.nome, jogador.cartas[i].valor[1])


def ver_amarrado(mesa_aux):
    mesa_troca = mesa_aux.copy()
    maior1 = mesa_troca.pop(mesa_troca.index(max(mesa_troca)))
    maior2 = mesa_troca.pop(mesa_troca.index(max(mesa_troca)))
    if maior1[0].get_valor() == maior2[0].get_valor() and maior1[0].get_valor != 11:
        if maior1[1].time != maior2[1].time:
            return True
    return False

def verificar_acao(jogadores, i):
    acao_truco = {
        "t": '(t) para truco',
        "s": '(s) para chamar seis',
        "n": '(n) para chamar nove',
        "d": '(d) para chamar doze'
    }
    #if not all(jogadors):
    
    if jogadores[i - 1].acao['3']:
        ac = "s"
        acao_truco = acao_truco["s"]
    elif jogadores[i - 1].acao['6']:
        ac = "n"
        acao_truco = acao_truco["n"]
    elif jogadores[i - 1].acao['9']:
        ac = "d"
        acao_truco = acao_truco["d"]
    elif any(jogadores[i].acao.values()):
        ac = None
    else:
        acao_truco = acao_truco["t"]
        ac = "t"

    if len(jogadores) > 2 and \
    (any(jogadores[i].acao.values()) or \
    any(jogadores[(i + 2) % len(jogadores)].acao.values())):
        chamada_acao = 'AGUARDANDO RESPOSTA...\ndigite:(j) para jogar carta / (f) para fugir: '
    elif len(jogadores) < 3 and \
    any(jogadores[i].acao.values()):
        chamada_acao = 'AGUARDANDO RESPOSTA...\ndigite:(j) para jogar carta / (f) para fugir: '
    else:
        chamada_acao = 'AGUARDANDO RESPOSTA...\ndigite:(j) para jogar carta / ' + acao_truco + ' / (f) para fugir: '
    
    return [ac, chamada_acao]

if __name__ == '__main__':
    truco()
