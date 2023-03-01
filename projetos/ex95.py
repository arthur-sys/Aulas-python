time =[]
dados={}
ngols=[]

while True:
    dados.clear()
    Jogador=str(input('Nome do jogador:'))
    dados['Jogador']=Jogador
    partidas=int(input('Numero de partidas:'))
    ngols.clear()
    for c in range(0,partidas):
        gg=(int(input(f'Numero de Gols na {c+1}ºpartida:')))
        ngols.append(gg)
    dados['Gols']=ngols
    Total=sum(ngols)
    dados['Total']=Total
    time.append(dados.copy())
    resp=str(input('quer continuar[S/N]')).upper()[0]
    if resp == 'N':
        break

print('-='*20)
print('cod',end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print('-='*20)
for k,v in enumerate(time):
    print(f'{k:>3} ',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print( )
while True:
    busca = int(input('mostrar qual jogador?'
                      '[999 para parar]'))
    if busca==999:
        break
    if busca>= len(dados):
        print(f'ERRRO!NÃO EXISTE JOGADOR COM O CÓDIGO {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR{time[busca]["Jogador"]}:')
        for i,g in enumerate(time[busca]["Gols"]):
            print(f'No jogo {i} fez {g} gols.')
    print('-'*40)
print('volte sempre')
