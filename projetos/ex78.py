# coding=utf-8
val =list()
maior = 0
menor = 0
for c in range(0, 5):
    val.append(int(input(f'digite o {c+1} numero:')))
    if c == 0:
        maior=menor=val[c]
    else:
        if val[c]>maior:
            maior = val[c]
        if val[c] < menor:
            menor = val[c]
print('=-'*30)
print (f'voce digitou os valores {val}')
print(f'O maior valor digitado é {maior} na posição',end=' ')
for i , v in enumerate(val):
    if v == maior:
        print (f'{i}...',end=' ')
print ()
print(f'O menor valor digitado é {menor} na posição,',end=' ')
for i , v in enumerate(val):
    if v == menor:
        print (f'{i}...',end=' ')
print()

