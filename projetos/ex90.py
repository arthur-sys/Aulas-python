aluno = dict()
aluno['nome']=str(input('Nome:'))
aluno['media']=float(input(f'a média de {aluno["nome"]}'))
if aluno['media']>=7:
    aluno['situação']='aprovado'
elif 5<=aluno['media']<7:
    aluno['situação']='recuperação'
else:
    aluno['situação']='reprovado'
print('='*20)
for c,v in aluno.items():
    print(f'{c} é igual a {v}')
