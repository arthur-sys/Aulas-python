galera =[]
dados =[]
tot=totalm=0
for c in range(0,3):
    dados.append(str(input('nome')))
    dados.append(int(input('idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1]>=21:
        print (f'{p[0]} é maior de idade')
        totalm+=1
    else:
        tot+=1
        print (f'{p[0]} é maior de idade')
print(f' Temos {totalm} maiores de idade '
      f'e {tot} mesnores de idade')
