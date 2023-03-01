galera = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('nome:')))
    dados.append(float(input('peso:')))
    if len(galera)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]

    galera.append(dados[:])
    dados.clear()
    resp =' '
    while resp not in 'SN':
        resp = str(input('deseja continuar [S/N]')).upper().strip()
    if resp == 'N':
        break
print(len(galera))
print(f'maior peso {maior}')
for p in galera:
    if p[1]== maior:
        print(f'[{p[0]}]')
print(f'menor peso {menor}')
for p in galera:
    if p[1]== menor:
        print(f'[{p[0]}]')
