
from random import randint
lista =list()
jogos = list()
print('-'*30)
print('JOGA NA MEGA SENA ')
print('-'*30)
quant = int(input('quantos jogos quer que eu sorteie'))
tot = 0
while tot <=quant:
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
            if cont>=6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        print(lista)
        tot+=1
print(quant)
for i,l in enumerate(jogo):
    print(f'{i+1}:{l}')

