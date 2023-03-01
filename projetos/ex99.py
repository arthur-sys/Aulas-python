from time import sleep
def maior(*num):
    maior=cont=0
    print('-='*20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}',end=' ',flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior=valor
        cont+=1

    print(f'foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('-='*20)


maior(2,3,5,8,6)
maior()




