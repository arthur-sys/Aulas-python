n = str(input('digite seu nome completo:')).strip()
print('muito prazer em te conheceer !')
divis = n.split()
print('seu primeiro nome é {}'.format(divis[0]))
print('seu ultimo  nome é {}'.format(divis[len(divis)-1]))
