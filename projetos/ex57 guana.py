s = str(input('informe qual é seu sexo: [M/F]')).strip()
while s not in 'MmFf':
    s = str(input('dados invalidos.por favor informe seu sexo:'))
print('sexo {} resgistrado com sucesso '.format(s))
