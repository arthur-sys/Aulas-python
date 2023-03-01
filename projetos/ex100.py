from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista')
    for cont in range(0,5):
        n = (randint(1,10))
        lista.append(n)
        print(f'{n}',end=' ',flush=True)
        sleep(0.5)
    print('pronto')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2==0:
            soma += valor
    print(f'somando os valores pares de {lista}. Temos {soma} ')
numero=list()
sorteio(numero)
somapar(numero)

