def validarjogada(aux):
    player = input(f'\nplayer {aux}: ')
    while len(player) > 3:
        print("Jogada inválida, tente novamente.")
        player = input(f'\nplayer {aux}: ')
    while player in jogadas:
        print('Essa jogada já foi feita, faça outra ')
        player = input(f'\nplayer {aux}: ')
    while player[0] not in '123' or player[2] not in '123':
        print('Utilize apenas os números 1, 2, e 3. Digite novamente.')
        player = input(f'\nplayer {aux}: ')
    while player[1] != ';':
        print("Utilize (;) para separar os numeros")
        player = input(f'\nplayer {aux}: ')
    jogadas.append(player)
    return player


def printmatriz():
    cont = 0
    for c in range(0, 3):
        for c2 in range(0, 3):
            print(matriz[c][c2], end=' ')
            cont += 1
            if cont == 3:
                print('\n', end='')
                cont = 0


def verificarmatriz(sla, player):
    global win
    global pontuacao1
    global pontuacao2
    if matriz[0][0] == sla and matriz[1][1] == sla and matriz[2][2] == sla or matriz[0][2] == sla and matriz[1][1] == sla and matriz[2][0] == sla or matriz[0][0] == sla and matriz[1][0] == sla and matriz[2][0] == sla or matriz[0][1] == sla and matriz[1][1] == sla and matriz[2][1] == sla or matriz[0][2] == sla and matriz[1][2] == sla and matriz[2][2] == sla or  matriz[0][0] == sla and matriz[0][1] == sla and matriz[0][2] == sla or matriz[1][0] == sla and matriz[1][1] == sla and matriz[1][2] == sla or  matriz[2][0] == sla and matriz[2][1] == sla and matriz[2][2] == sla:
        win = True
        print(f"Jogador {player} venceu a batalha, mas não a guerra!!\n")
        if player == '1':
            pontuacao1 += 1
        elif player == '2':
            pontuacao2 += 1
        printpontuacao()
    return win


def printpintuacao():
    print(f'''Pontuação:
    Player 1: {pontuacao1}
    Player 2: {pontuacao2}\n''')

def deuvelha():
    if len(jogadas) == 9:
        return True
    return False


def jogarnovamente():
    escolha = input('Deseja jogar novamente? [S][N] ').lower()
    try:
        while escolha not in 'ns':
            print("Opção inválida, tente novamente. ")
            escolha = input('Deseja jogar novamente? [S][N] ').lower()
    except ValueError:
        print("Opção inválida, tente novamente. ")
        escolha = input('Deseja jogar novamente? [S][N] ').lower()
    return escolha


def verificarvencedor():
    if pontuacao1 > pontuacao2:
        print("O Jogador 1 venceu a guerra muahhahah!!")
    elif pontuacao2 > pontuacao1:
        print("O jogador 2 venceu a guerra muhahahah!!")


pontuacao1 = pontuacao2 = 0
jogadas = []
matriz = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


print('''\nPlayer 1 = O
Player 2 = X \n''')

while True:
    win = False
    sair = False
    printmatriz()
    print("\nDigite a posição que deseja jogar")

    player1 = validarjogada(1)
    aux = int(player1[0])
    aux1 = int(player1[2])
    matriz[int(aux) - 1][int(aux1) - 1] = 'O'
    printmatriz()
    win = verificarmatriz('O', '1')

    if win:
        sair = True
        opc = jogarnovamente()
        if opc == 'n':
            verificarvencedor()
            break
        if opc == 's':
            matriz = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            jogadas = []
            continue


    if deuvelha():
        print('Empate!')
        printpontuacao()
        opc = jogarnovamente()
        sair = True
        if opc == 'n':
            verificarvencedor()
            break
        if opc == 's':
            continue


    player2 = validarjogada(2)
    aux = int(player2[0])
    aux1 = int(player2[2])
    matriz[int(aux) - 1][int(aux1) - 1] = 'X'
    printmatriz()
    win = verificarmatriz('X', '2')

    if win:
        opc = jogarnovamente()
        sair = True
        if opc == 'n':
            verificarvencedor()
            break
        if opc == 's':
            matriz = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            jogadas = []
            continue


    if deuvelha():
        print('Empate!')
        opc = jogarnovamente()
        sair = True
        if opc == 'n':
            break
        if opc == 's':
            matriz = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            jogadas = []
            continue
