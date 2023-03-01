from random import randint
pc = randint(0,10)
print('tente advinhar o numero de 0 a 10 que o computador pensou')
acertou = False
palpites = 0
while not acertou:
    joga= int(input('qual seu palpite'))
    palpites+=1
    if joga==pc:
        acertou=True
    else:
        if joga>pc:
            print('menos,tente mais uma vez')
        elif joga<pc:
            print('mais,tente mais uma vez')
print('Acertou com {} tentativas'.format(palpites))
