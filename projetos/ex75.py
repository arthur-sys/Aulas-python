num = (int(input('Digite um numro')),
       int(input('Digite um numro')),
       int(input('Digite um numro')),
       int(input('Digite um numro')))
print(f'voce digitou os valore {num}')
contar=(num.count(9))
print(f'o valor 9 apareceu {contar}',end=' ')
print('vez 'if (contar) == 1 else 'vezes')
if 3 in num:
       print(f'o valor 3 apareceu na {num.index(3)}º posição')
else:
       print('o valor 3 não foi digitado em nenhuma posição')
print(f'os valores pares digitados foram',end=' ')
for n in num:
       if n % 2 ==0:
              print(n, end=' ')





