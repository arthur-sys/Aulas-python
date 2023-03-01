maiores18=homens=mulher20=0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade=int(input('Idade'))
    sexo =' '
    while sexo not in 'MF':
        sexo =str(input('Sexo[M/f]')).upper().strip()
        if idade >18:
            maiores18+= 1
        if sexo =='M':
            homens+=1
        if sexo =='F' and idade<20:
            mulher20+=1
    print('-'*20)
    continuar =' '
    while continuar not in 'SN':
        continuar = str(input('deseja continuar [S/N]')).strip().upper()
    if continuar == 'N':
         break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {maiores18}')
print(f'Ao todo temos {homens}',end=' ')
print('homem cadastrados'if homens == 1 else 'homens cadastrados')
print(f'E temos {mulher20}',end=' ')
print('mulher'if mulher20 == 1 else 'mulheres',end=' ')
print('com menos de 20 anos')

