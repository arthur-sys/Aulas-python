import random
from time import sleep
print('vamos jogar jokenpo')
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
itens = ('pedra','papel','tesoura')
pc = random.randint(0,2)
pessoa = int(input('qual sua jogada'))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)
print('o computador escolheu {}'.format(itens[pc]))
print('Voce escolheu {}'.format(itens[pessoa]))
if pc == 0:
    if pessoa == 0:
        print('deu impate tente novamente')
    elif pessoa == 1:
        print('parabéns voce ganhou')
    elif pessoa == 2:
        print('tente novamente o computador ganhou')
    else:
        print('jogada invalida,tente outra vez')
elif pc == 1:
    if pessoa == 0:
        print('tente novamente o computador ganhou')
    elif pessoa == 1:
        print('deu impate tente novamente')
    elif pessoa == 2:
        print('parabéns voce ganhou')
    else:
        print('jogada invalida,tente outra vez')
elif pc == 2:
    if pessoa == 0:
        print('parabéns voce ganhou')
    elif pessoa == 1:
        print('tente novamente o computador ganhou')
    elif pessoa == 2:
        print('parabéns voce ganhou')
    else:
        print('jogada invalida,tente outra vez')
