idademed = 0
count = 0
maioridh = 0
nomevelh = 0
mulher20 = 0
for c in range(1,5):
    nome = str(input('digite seu nome')).strip()
    idad = int(input('digite sua idade'))
    sexo = str(input('SEXO [M/F]: ')).strip()
    count +=idad
    if c == 1 and sexo in 'Mm':
        maioridh = idad
        nomevelh =nome
    if sexo in 'Mm' and idad>maioridh:
        maioridh = idad
        nomevelh =nome
    if sexo in 'Ff' and idad >20:
        mulher20+= 1

idademed+= count/4
print('a media de idade do grupo é {}'.format(idademed))
print('p homem mais velho tem {} e se chama {}'.format(maioridh,nomevelh))
print('ao todo são {} mulheres com mais de 20 anos '.format(mulher20))




