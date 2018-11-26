vet = []
qtd = int(input())
cont = 0

for c in range(0, qtd):
    vet.append(input())

for c in range(0, qtd):
    if '1' in vet[c]:
        x = vet[c].count('1')
        cont += 2 * x
    if '2' in vet[c]:
        x = vet[c].count('2')
        cont += 5 * x
    if '3' in vet[c]:
        x = vet[c].count('3')
        cont += 5 * x
    if '4' in vet[c]:
        x = vet[c].count('4')
        cont += 4 * x
    if '5' in vet[c]:
        x = vet[c].count('5')
        cont += 5 * x
    if '6' in vet[c]:
        x = vet[c].count('6')
        cont += 6 * x
    if '7' in vet[c]:
        x = vet[c].count('7')
        cont += 3 * x
    if '8' in vet[c]:
        x = vet[c].count('8')
        cont += 7 * x
    if '9' in vet[c]:
        x = vet[c].count('9')
        cont += 6 * x
    if '0' in vet[c]:
        x = vet[c].count('0')
        cont += 6 * x
    print(cont, "leds")
    cont = 0
