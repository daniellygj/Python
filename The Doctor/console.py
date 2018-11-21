def printf(a):
    print(a)
    print('=-' * 30)  # Falta do que fazer


def readsite(link):  # Lê um site e retorna com os textos
    from urllib.request import urlopen
    sla = urlopen(link)
    sla1 = sla.read()
    return sla1.decode('utf-8')


def read(arquivo):  # Lê um arquivo e o imprime
    a = open(arquivo, 'r')
    for linha in a:
        print(linha, end='')
    a.close()


def write(arquivo, texto):  # Escreve no arquivo
    open(arquivo, 'w')
    arquivo.writelines(texto)


def bubble_sort(x):  # O próprio nome ja diz
    for c in range(len(x)):
        troca = False
        for c2 in range(1, len(x)-c):
            if x[c2] < x[c2 - 1]:
                x[c2], x[c2 - 1] = x[c2 - 1], x[c2]  # No pythonzinho da pra fazer assim. Isso so troca de lugar
                troca = True
        if not troca:
            break
    return x

# By Danny
