p1 = input().strip().lower()
p2 = input().strip().lower()
p3 = input().strip().lower()

if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print('aguia')
        elif p3 == 'onivoro':
            print("pomba")
    elif p2 == 'mamifero':
        if p3 == 'onivoro':
            print("homem")
        elif p3 == 'herbivoro':
            print("vaca")
elif p1 == 'invertebrado':
    if p2 == 'inseto':
        if p3 == 'hematofago':
            print("pulga")
        elif p3 == 'herbivoro':
            print("lagarta")
    elif p2 == 'anelideo':
        if p3 == 'hematofago':
            print("sanguessuga")
        elif p3 == 'onivoro':
            print("minhoca")
