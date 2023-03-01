def teste(b):
    global a
    a=8
    b+=4
    c=2
    c=2#escopo local
    print(f'a dentro vale {a}')
    print(f'b dentro vale {b}')
    print(f'c dentro vale {c}')




a=5#escopo global
teste(a)
print(f'a fora vale {a}')
