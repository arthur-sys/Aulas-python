print('olha ai bigode')
print('descubra se passou de ano')
n1=float(input('digite a primeira nota:'))
n2=float(input('digite a segunda nota:'))
media=(n1+n2)/2
faltas=int(input('quantas falta possui?'))
if media>=7 and faltas<=25:
    print(f'parabéns voce passou com a média {media}.')
elif faltas>=25:
    print('voce repetiu por falta')
else:
    print('vai estudar muleke você repetiu de ano ')
