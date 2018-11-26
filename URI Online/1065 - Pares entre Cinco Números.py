vet = []

par = 0
for c in range(0, 5):
    vet.append(int(input()))
    if vet[c] % 2 == 0:
        par += 1

print('{} valores pares'.format(par))
