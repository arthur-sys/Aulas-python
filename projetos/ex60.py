import math
num = int(input('digite um valor para saber seu fatorial'))
resp=math.factorial(num)
c = num
print('calculando {}!'.format(num))
while c > 0:
    print('{} '.format(c),end='')
    print('x ' if c > 1 else '=',end='')
    c-= 1
print(' o fatorial de {} é {}'.format(num,resp))

