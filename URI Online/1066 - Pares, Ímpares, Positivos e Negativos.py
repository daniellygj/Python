vet = []

par = 0
impar  = 0
positivo = 0
negativo  = 0

for c in range(0, 5):
    vet.append(int(input()))
    if vet[c] > 0:
        positivo += 1
    if vet[c] < 0:
        negativo += 1
    if vet[c] % 2 == 0:
        par += 1
    if vet[c] % 2 != 0:
        impar += 1

print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(par, impar, positivo, negativo))
