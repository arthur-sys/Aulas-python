quant = 0
val=list()
par=list()
impar=list()
while True:
    n=int(input('digite um valor'))
    val.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = " "
    while resp not in 'SN' :
        resp=str(input('deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print (f'A lista completa é {val}')
print (f'A lista  de pares é {par}')
print (f'A lista  de impar é {impar}')


