lista = ('lapis', 1.75,
         'borracha', 2,
         'caderno', 15.90,
         'pasta', 10.99,
         'mochila', 50.77)
print('-'*40)
print (f'{"listagem de preços":^40}')
print('-'*40)
for pos in range(0,len(lista)):
    if pos % 2==0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$:{lista[pos]:>7.2f}')

