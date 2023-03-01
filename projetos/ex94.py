quantidade=media=soma=0
mulheres=' '
dados={}
lista=list()
while True:
    dados.clear()
    dados['Nome']=str(input('nome:')).title()
    quantidade+=1
    Sexo= ' '
    while Sexo not in 'MF':
      Sexo=str(input('sexo:[M/F]')).upper().strip()[0]
    dados['Sexo']=Sexo
    dados['Idade']=int(input('Idade:'))
    soma+=dados['Idade']
    media=soma/quantidade
    lista.append(dados.copy())
    resp =' '
    while resp not in 'SN':
        resp=str(input('quer continuar?')).upper().strip()[0]
    if resp == 'N':
        break
print('=-'*20)
print(f'o grupo tem {quantidade} pessoas.')
print(f'a média de idade é {media:5.2f}')
print('AS mulheres cadastradas foram',end=' ')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}',end=' ')
print( )
print('Lista das pessoas que estão acima da média: ', end='')
for p in lista:
    if p['Idade']>= media:
        print('  ')
        for k,v in p.items():
            print(f'{k}={v}:',end='')
        print( )
print('Fim')


