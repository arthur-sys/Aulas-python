num = 0
soma = 0
quantos = 0
num = int(input('digite um numero {999 para parar}'))
while num !=999:
    quantos+= 1
    soma += num
    num = int(input('digite um numero {999 para parar}'))
print('voce digitou {} numeros'.format(quantos),end= ' ')
print ('e a soma entre eles é {}'.format(soma))
