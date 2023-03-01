from datetime import date
def voto(nasc):
    anoatual=date.today().year
    idade =anoatual-nasc
    if idade >=18:
        return f' com {idade} anos: Voto Obrigatorio'
    elif 16 <= idade <18 :
        return f' com {idade} anos: Voto Opcional'
    elif idade <16:
        return f' com {idade} anos: não vota'
    elif idade<=65:
        return f' com {idade} anos: Voto Opcional'


n = int(input('digite o ano de seu nascimento'))
print({voto(n)})

