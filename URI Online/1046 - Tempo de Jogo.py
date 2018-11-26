inicial, final = input().split(" ")
inicial = int(inicial)
final = int(final)

if inicial > final:
    tempo = (24 + final) - inicial
    print("O JOGO DUROU {} HORA(S)".format(tempo))
elif inicial < final:
    tempo = final - inicial
    print("O JOGO DUROU {} HORA(S)".format(tempo))
else:
    print('O JOGO DUROU 24 HORA(S)')
