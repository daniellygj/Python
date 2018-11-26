def aumento(a, b):
    reajuste = a * b
    Nsalario = salario + reajuste
    print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual:' %(Nsalario, reajuste), p)


salario = float(input())

if salario <= 400.00:
    p = '15 %'
    aumento(salario, 0.15)
elif salario <= 800.00:
    p = '15 %'
    aumento(salario, 0.12)
elif salario <= 1200.00:
    p = '10 %'
    aumento(salario, 0.10)
elif salario <= 2000.00:
    p = '7 %'
    aumento(salario, 0.07)
else:
    p = '4 %'
    aumento(salario, 0.04)
