def fatorial(num,show=False):
    '''
    calcula fatotial n
    :param num: n a ser calculado
    :param show:(opcional)mostrar conta ou não
    :return:o valor do fatorial 
    '''
    f = 1

    for c in range(num,0,-1):
        if show:
            print(f'{c} ',end='')
            if c>1:
                print(f' x ',end='')
            else:
                print('=',end='')
        f*=c
    return f




print(fatorial(5,))
