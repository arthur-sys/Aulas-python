tentativas = 0
from random import randint
pc = randint(0,10)
print('tente descobrir o numero escolhido pelo computador entre 0 e 10')
vc =int(input('digite um numero'))
while vc != pc:
    vc =int(input('O computador não escolheu  {} tente novamente'.format(vc)))
    tentativas += 1
print('voce acertou com {} tentativas'.format(tentativas+1))
