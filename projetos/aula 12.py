n = str(input('qual é seu nome ')).strip().title()
if n == 'Gustavo':
    print('que nome bonito')
    #estrutura simples#
elif n == 'pedro' or n == 'maria':
    print('seu nome é comum')
    #condicional alinhada#
elif n in 'ana julia isa ':
       print('seu nome é comp')
else:
    print('seu nome é diferente')
    #estrutura composta#
print('bom dia {} '.format(n))
