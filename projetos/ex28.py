import random
lista = [0,1,2,3,4,5]
pc= random.choice(lista)
#pc = random.randint(1,5)#
print('tente descobrir o numero escolhido pelo computador entre 0 e 5')
print(pc)
vc =int(input('dgite um numero'))
if  pc == vc  :
    print('parabéns voce é um vidente')
else:
    print('parabéns voce é uma pessoa comum ')


