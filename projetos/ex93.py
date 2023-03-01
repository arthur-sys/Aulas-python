dados={}
ngols=[]
Jogador=str(input('Nome do jogador:'))
dados['Jogador']=Jogador
partidas=int(input('Numero de partidas:'))
for c in range(0,partidas):
    gg=(int(input(f'Numero de Gols na {c+1}ºpartida:')))
    ngols.append(gg)
dados['Gols']=ngols
Total=sum(ngols)
dados['Total']=Total
print('-='*20)
print(f'{dados}')
print('-='*20)
for v,c in dados.items():
    print(f'O campo {v} tem o valor {c}')
print('-='*20)
print(f'O jogador {Jogador} jogou {partidas} partidas')
for i,v in enumerate(dados['Gols']):
    print(f' =>Na partida {i},fez {v} Gols')
print(f'Foi um total de {Total} Gols.')
