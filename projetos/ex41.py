from datetime import date
ano = int(input('digite o ano de seu nascimento para saber qual sua categoria'))
atual = date.today().year
resp = atual-ano
if resp <=9:
    print('Mirim')
elif resp <=14:
    print('Infantil')
elif resp <=19:
    print('Junior')
elif resp == 20:
    print('Sênior')
else:
    print('Master')
