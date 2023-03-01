estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf']=str(input('unidade federativa'))
    estado['siglas']=str(input('sigla do estado'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k , v in e.items():
        print(k,v)
