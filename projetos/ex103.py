def ficha(jog='<desconhecido>',gol=0):
    print(f'o jogador {jog} fez {gol} Gols no campeonato')

n=str(input('nome do jogador'))
g=str(input('numero de Gols'))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)



