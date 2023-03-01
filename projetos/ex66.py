soma = quant = 0
while True:
    num = int(input('digite um numero'))
    if num ==999:
        break
    soma+=num
    quant += 1
print(f'Foram digitados {quant} numeros',end=' ')
print(f'e a soma entre eles é igual a {soma}')
