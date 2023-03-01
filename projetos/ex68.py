import random
from time import sleep
tipo = comp = cont = 0
print('='*20)
print('Vamos jogar PAR OU IMPAR')
sleep(1)
while True:
    numpc = random.randint(1,20)
    print('='*20)
    valor = int(input('Diga um valor:'))
    pessoa = str(input('Voce escolhe [P/I]:')).upper().strip()
    if pessoa == 'I':
        comp = 'Par'
    elif pessoa=='P':
        comp = 'Impar'
    resultado = valor + numpc
    if resultado % 2 == 0:
        tipo = 'Par'
    else:
        tipo = 'Impar'
    print('-'*20)
    print(f'voce jogou {valor} e o computador {numpc}.Total de {resultado} deu {tipo} ')
    print('-'*20)
    if tipo != comp:
        print('você Venceu!')
        print('vamos jogar novamente...')
        cont += 1
    else:
        print('GAME OVER!',end=' ')
        print(f'voce ganhou {cont}',end=' ')
        print('vez' if cont == 1 else'vezes')
        break




