maior= 0
menor = 0
n1 = int(input('digite um valor'))
n2 = int(input('digite outro valor'))
opcao = 0
while opcao !=6:
    print('''
    [ 1 ] Somar
    [ 2 ] mutiplicar
    [ 3 ] Qual é o maior valor
    [ 4 ] Qual é o menor valor
    [ 5 ] Novos numeros
    [ 6 ] Sair do programa
    ''')
    opcao = int(input('>>>>>>> Qual sua opção'))
    if opcao ==1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif opcao ==2:
        print('{} X {} = {}'.format(n1,n2,n1*n2))
    elif opcao==3:
        if n1 > n2:
            maior =n1
        elif n2 > n1 :
            maior=n2
        print('O maior valor é {}'.format(maior))
    elif opcao ==4:
        if n1< n2:
            menor=n1
        elif n2 < n1:
            menor =n2
        print('O menor valor é {}'.format(menor))
    elif opcao ==5:
        n1 = int(input('digite um valor'))
        n2 = int(input('digite outro valor'))
    else:
        print('opção invalida,tente novamente')
print('programa finalizado')
