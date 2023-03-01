frase = str(input('digite uma frase')).strip().upper()
div = frase.split()
junto =''.join(div)
inverso= ''
for c in range(len(junto)-1,-1,-1):
    inverso+=junto[c]
if inverso==junto:
    print('essa plavra é um palindromo ')
else:
    print('essa palavra não éum palindromo ')
