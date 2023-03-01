n = str(input('digite seu nome completo')).strip()
print('analisando seu nome')
print(n.title())
print('seu nome em maiusculo é {}'.format(n.upper()))
print('seu nome em minusculo é {}'.format(n.lower()))
#print('seu nome tem ao todo {} letras '.format(len(n)-n.count(' ')))#
s= n.split()
print('seu primeiro nome é {} e possui {} letras '.format(s[0],len(s[0])))
