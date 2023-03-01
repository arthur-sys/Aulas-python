pesomaior = 0
pesomenor = 0
for p in range(1,6):
    peso = float(input('peso da {} º pessoa:'.format(p)))
    if p == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso liquido foi de {}'.format(pesomaior))
print('O menor peso liquido foi de {}'.format(pesomenor))

