vet = []

positivo = 0
media = 0
for c in range(0, 6):
    vet.append(float(input()))
    if vet[c] > 0:
        positivo += 1
        media += vet[c]
media /= positivo
print(positivo,'valores positivos\n%.1f' %media)
