from datetime import date
ano = int(input('qual ano gostaria de analisar? Coloque 0 para analisar o anao atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0 :
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto '.format(ano))
