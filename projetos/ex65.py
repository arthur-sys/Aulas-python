resp = 'S'
cont = 0
soma = 0
media = 0
maior = 0
menor = 0
novo = 0
while resp == 'S':
    num = int(input('digite um numero:'))
    resp =str(input('deseja continuar[S/N]')).upper().strip()
    cont += 1
    soma += num
    media = (soma/cont)
    if novo == 1:
        maior =num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor =num
print('voce digitu {} numeros '.format(cont),end='')
print(',a soma entre eles é {}'.format(soma),end='')
print(',a média é {}'.format(media),end='')
print(',o maior deles é {}'.format(maior),end=' ')
print('e o menor deles é {}'.format(menor),end=' ')
print('Fim.')
