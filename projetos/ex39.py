import datetime
nasc = int(input('digite o ano de seu nascimento'))
atual = datetime.date.today().year
resp = atual - nasc
if resp < 18:
    saldo = 18-resp
    print('voce terá que se alistar daqui a {} anos '.format((saldo)))
    alist = saldo + atual
    print('voce deveria se alistar no ano de {}'.format(alist))
elif resp == 18:
    print('voce terá que se alistar esse ano')
else:
    sald = resp - 18
    print('parabens voce ja se alistou há {} anos '.format(sald))
    ali = atual - sald
    print('voce deveria ter se alistado no ano de {}'.format(ali))
