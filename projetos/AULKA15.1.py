num = s =  0
while True:
    num = int(input('digite um numero'))
    if num ==999:
        break
    s+=num
print(f'A soma vale {s:-^10}')
