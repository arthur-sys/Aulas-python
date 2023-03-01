vogal=''
lista =('carro', 'casa', 'animal','caderno', 'moto',
        'bicicleta','pneu','rua','apartamento','arma')
for c in lista:
    print(f'\nNa palavra {c} temos ',end=' ' )
    for letra in c:
        if letra in 'aeiou':
            print(letra,end=' ')
