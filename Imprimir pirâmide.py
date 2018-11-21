'''
Crie uma função em Python ou Javascript que receba um número como parâmetro e imprima uma pirâmide de underscores e asteriscos no console.

Por exemplo: para a entrada 6, a saída deve ser a seguinte:

_____*_____
____***____
___*****___
__*******__
_*********_
***********

Com a altura da pirâmide igual ao número fornecido na entrada.
'''

def imprimir(qtd, i):
    for j in range(qtd, 0, -1):
        print(f"{'_' * (j-1)}{'*' * i}{'_' * (j-1)}")
        i += 2

qtd = int(input(""))

imprimir(qtd, 1)

