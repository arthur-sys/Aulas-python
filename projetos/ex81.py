quant = 0
val=list()
while True:
    n=int(input('digite um valor'))
    val.append(n)
    quant+=1
    resp = " "

    while resp not in 'SN' :
        resp=str(input('deseja continuar?')).strip().upper()[0]
    if resp == 'N':
        break

print (f'Foram digitados {quant}º valores')
print (f'Voce digitou os valores{sorted(val,reverse=True)}')
if 5 in val:
    print ('o valor 5 faz parte da lista ')
else:
    print ('O valor 5 não foi encontrado na lista ')
