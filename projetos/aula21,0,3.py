def teste():
    x= 8#variavel local
    print(f'na função teste,n vale {n}')
    print(f'x vale {x}')


#programa principal
n=2#variavel global
print(f'no programa principal n vale {n}')
teste()
