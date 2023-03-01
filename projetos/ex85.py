num =[[],[]]
for c in range(0,7):
    n = int(input(f'digite o {c+1}º valor'))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(sorted(num[0]))
print(sorted(num[1]))


