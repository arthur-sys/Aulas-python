from time import sleep
print('='*20)
print(' 10 termos de uma PA ')
print('='*20)
sleep(1)
ter = int(input('primeiro termo'))
raz = int(input('razão'))
dec = ter+(10-1)*raz
for c in range(ter,dec + raz,raz):
    print('{}'.format(c),end='-')

