tot=mais1000=menor=cont=0
barato = ''
while True :
    print('-'*20)
    nomep = str(input('qual o nome do produto'))
    preco = int(input('qual o valor ? R$'))
    cont += 1
    continuar = ' '
    tot += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        menor = preco
        barato = nomep
    else:
        if preco < menor:
            menor =  preco
            barato = nomep
    print('-'*20)
    while continuar not in 'SN':
        continuar=str(input('deseja continuar:[S/N]')).strip().upper()
    if continuar =='N':
        break
print(f'O total gasto na compra foi {tot}')
print(mais1000,end=' ')
print('produtos custam'if mais1000 !=1 else'produto custa',end=' ')
print('mais que R$1.000')
print(f'{barato} é o produto mais barato')
