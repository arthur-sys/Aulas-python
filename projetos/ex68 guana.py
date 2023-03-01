from random import randint
v = 0
while True:
    jog = int(input('digite um numero'))
    pc =randint(1,10)
    total = jog + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    print(f'voce jogou {jog} eo computador {pc}.Total de {total}')
    if tipo =='P':
        if total % 2==0:
            print('voce venceu')
            v+=1
        else:
            print('GAME OVER')
            break
    elif tipo == 'I':
        if total %2==1:
            print('Voce venceu')
            v += 1
        else:
            print('GAME OVER ')
            break
    print('vamos jogar novamente')
print(f'SE FUDEU!voce venceu {v} vezes')
