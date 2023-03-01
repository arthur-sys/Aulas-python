salario = float(input('qual o valor do seu salario para calcular seu aumento'))
if salario > 1250.00:
    print('seu aumento sera de {}'.format(salario*0.10 +salario))
else:
    print('seu aumento sera de {}'.format(salario*0.15+salario))

