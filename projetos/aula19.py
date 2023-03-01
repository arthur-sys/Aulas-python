pesso={'nome':'arthur','sexo':'M','idade':20}
print(pesso['nome'])
print(f'o {pesso["nome"]} tem {pesso["idade"]} anos')
print(pesso.keys())
print(pesso.values())
print(pesso.items())
for k in pesso.keys():
    print(k)
for b in pesso.values():
    print(b)
for c,v in pesso.items():
    print(f'{c}={v}')
del pesso['sexo']
print(pesso)
pesso['nome']='mike'
print(pesso["nome"])
