primeiro = int(input('primeiro termo'))
raz = int(input('razão'))
ter =primeiro
c = 1
total =0
mais = 10
while mais!=0:
    total=total+mais
    while c <=total:
        print('{} - '.format(ter),end='')
        ter+=1
        c +=1
    print ('pausa')
    mais = int(input('qauntos termos voce quer mostrar a mais '))
print('fim')
