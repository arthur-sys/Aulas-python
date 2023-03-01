val=list()
while True:
    n=(int(input('digite um valor')))
    if n not in val:
        val.append(n)
        print ('valor adicionado com sucesso ...')
    else:
        print('valor duplicado!não vou adicionar.. ')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('deseja continuar?[S/N]')).upper().strip()
    if resp == 'N':
        break
print (f'voce digitou os valores{sorted(val)}')
