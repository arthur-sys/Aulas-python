from random import randint
from operator import itemgetter
jogo ={'jogador1':randint(1,6),
       'jogador2':randint(1,6),
       'jogador3':randint(1,6),
       'jogador4':randint(1,6),
       'jogador5':randint(1,6),}
print('valores sorteados')
rank=dict()
for c,v in jogo.items():
    print((f'{c} tirou {v} no dado'))
rank=sorted(jogo.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]}.')



