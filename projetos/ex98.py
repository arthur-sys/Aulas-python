from time import sleep
def contator(i,f,p):
    print('~'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p<0:
        p*=-1
    if p ==0:
        p=1
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont+=p
        print('Fim')
    else:
        cont=i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont-=p
        print('Fim')


contator(1,10,1)
contator(10,0,2)
print('sua vez de personalizar')
ini=int(input('Inicio: '))
fim=int(input('Fim: '))
pas=int(input('Passo: '))
contator(ini,fim,pas)



