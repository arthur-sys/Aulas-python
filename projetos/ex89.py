lista=list()
while True:
    nome=(str(input('nome:')))
    nota1=(float(input('nota 1')))
    nota2=(float(input('nota 2')))
    media =(nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])
    resp =' '
    while resp not in 'SN' :
        resp=str(input('deseja continuar?')).upper().strip()
    if resp == 'N':
        break
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc=int(input('mostranota de qual aluno (999 interrompe:'))
    if opc<=len(lista)-1:
        print(f'notas de {lista[opc][0]} sao {lista[opc][1]}')
    if opc == 999:
        break
