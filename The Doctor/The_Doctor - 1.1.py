from console import readsite

x = readsite('http://dontpad.com/apenastestezinhos/TheDoctor-V1.1.txt.txt')

opcoes = []
listinha = []
opc = 1


def printf():
    inicio = x.find('[IMPRIMIR]') + 10
    fim = x.find('[FIMIMPRIMIR]')
    aux = x[inicio:fim]
    saida = aux.split('\n')
    imprimir(saida)


def imprimir(nsei):
    for d in nsei:
        if d == '':
            continue
        elif d in'[ESPACO]':
            print('\n')
        elif d in'[SEPARADOR]':
            print('=-' * 50)
        elif d in '[ENTER]':
            input('\nAperte enter para continuar\n')
        else:
            print(d)


def montarmenu():
    for linha in x.split('\n'):
        if '[OPCAO]' in linha:
            inicio = x.find('[OPCAO]')+8
            fim = x.find('[FIMOPCAO]')
            aux = (x[inicio: fim])
            menu = aux.split('\n')
    imprimir(menu)

    escolher = input('Escolha uma das opções acima: ')

    while escolher not in opcoes:
        print("\nOpção inválida, tente novamente. ")
        print('-=' * 50)
        imprimir(menu)
        escolher = input('Escolha uma das opções acima: ')
    return escolher


def escolha(opc):
    esc = '[ESCOLHA' + opc + ']'
    fimesc = '[FIMESCOLHA' + opc + ']'
    inicio = x.find(esc) +10
    fim = x.find(fimesc)
    aux = x[inicio:fim]
    saida = aux.split('\n')
    imprimir(saida)


for line in x.split('\n'):
    if line == '':
        continue
    elif '[OPCAO]' in line:
        qtdopc = line.find('[OPCAO]') + 7
        qtd = int(line[qtdopc:])
        for c in range(0, qtd+1):
            opcoes.append(str(c))
        menu = []
        opc = montarmenu()
        escolha(opc)
        while True:
            opc = montarmenu()
            if opc == '0':
                break
            escolha(opc)
    elif '[IMPRIMIR]' in line:
        printf()

