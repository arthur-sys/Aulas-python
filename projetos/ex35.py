print('vamos descobrir se voce sabe fazer um triangulo ')
a = float(input('digite o valor da primeira reta'))
b = float(input('digite o valor da segunda reta'))
c = float(input('digite o valor da terceira reta'))
if  a < b + c and b < a + c or c< b + a :
    print('os seguimentos podem formar um triangulo ')
else:
    print('os seguimentos não podem formar um triangulo ')
