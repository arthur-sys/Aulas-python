print('vamos descobrir se voce sabe fazer um triangulo ')
a = float(input('digite o seguimentos da primeira reta'))
b = float(input('digite o seguimentos da segunda reta'))
c = float(input('digite o seguimentos da terceira reta'))
if  a < b + c and b < a + c or c< b + a :
    print('os seguimentos podem formar um triangulo ', end='')
    if a == b == c:
        print('equilátero')
    elif a != b !=  c != a:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('os seguimentos não podem formar um triangulo ')

