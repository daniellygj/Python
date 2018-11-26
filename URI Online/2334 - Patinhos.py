patinhos = 1

while patinhos != -1:
    patinhos = int(input())
    while patinhos > 10**19:
        patinhos = int(input())
    if patinhos >= 1:
        print(patinhos - 1)
    elif patinhos == 0:
        print(0)
