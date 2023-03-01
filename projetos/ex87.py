matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar=maio=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'digite um valor para [{l},{c}]:'))
print('=-' * 20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 ==0:
            spar+=matriz[l][c]
    print()
print('=-'*20)
print(f'a soma dos numeros pares é {spar}')
for l in range(0,3):
    scol+=matriz[l][2]
print(f'a soma da 3 coluna é {scol}')
for c in range (0,3):
    if c ==0:
        maio = matriz[l][c]
    elif matriz[l][c]>maio:
        maio= matriz[l][c]
print(f'o maior  valor segunda linha é {maio}')


