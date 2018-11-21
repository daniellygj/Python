from console import readsite

x = readsite('http://dontpad.com/apenastestezinhos.txt')
lista = []
opcoes = []
listinha = []

def printf():
    if '[ENTER]' not in line and '[QTDOPCAO]' not in line and '[OPCAO]' not in line and '[SEPARADOR]'not in line and '[EXERCICIOS]' not in line and '[OPC]' not in line and '[ESCOLHA' not in line:
        print(line)


def enter():
    if '[ENTER]' in line:
        input('\nAperte enter para continuar\n')

def separador():
    if line in '[SEPARADOR]':
        print('=-' * 50)

def pegaropc(lista):
    opcoes = []
    for line in x.split('\n'):
        if '[OPCAO]' in line:
            opcoes.append(line[7:])
    for c in opcoes[2:]:

        print(c)
    opcaozinha = input('Escolha uma das opções acima: \n')

    if opcaozinha not in lista:
        print('Opção inválida, tente novamente.')
        print('=-' * 50, '\n')
        opcaozinha = pegaropc(lista)
    return str(opcaozinha)



def escolha(opc, qtd):
    for line in x.split('\n'):
        esc = '[ESCOLHA' + opc + ']'
        if esc in line:
            listinha.append(line[10:])

    for c in listinha:
        if c in '[SEPARADOR]':
            print('=-' * 50)
        elif c in '[ENTER]':
            input('\nAperte enter para continuar\n')
        else:
            print(c)


for line in x.split('\n'):
    if '[QTDOPCAO]' in line:
        qtd = int(line[10:])
        for c in range(1, qtd + 1):
            if '0' not in lista:
                lista.append('0')
            lista.append(str(c))

    if line in '[OPC]':
        opcoes = []

        opc = pegaropc(lista)
        if opc == '0':
            break
        listinha = []
        escolha(opc, qtd)
    else:
        separador()
        printf()
        enter()
