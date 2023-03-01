import datetime
atual =datetime.date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano =int(input('em que ano a {} º pessoa nasceu'.format(c)))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade '.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade '.format(totmenor))
