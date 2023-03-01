times =('Atlético-MG', 'Atlético-PR', 'Avaí',
'Bahia', 'Botafogo', 'Ceará', 'Chapecoense', 'Corinthians',
'Cruzeiro', 'CSA', 'Flamengo', 'Fluminense', 'Fortaleza',
'São Paulo','Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
'Santos', 'Vasco' )
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 ultimos são {times[16:20]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print('O Time da Chapecoense se encontra na posição ',
      end=' ')
print(times.index('Chapecoense'))
