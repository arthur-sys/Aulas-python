c = 0
while True:
    num = int(input('digite um numero para saber sua tabuada '))
    print('-'*20)
    while c <10:
        c += 1
        print(f'{num} X {c} = {num*c} ')
        if num == -num:
            break
    print('-'*20)

