n = str(input('digite uma frase')).strip().upper()
print('A letra A aparece {} vezes na frase '.format(n.count('A')))
print('A primeira letra A apareceu apareceu na posição {} '.format(n.find('A')+1))
print('A ultima letra A apareceu apareceu na posição {} '.format(n.rfind('A')+1))
