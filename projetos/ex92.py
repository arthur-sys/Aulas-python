from datetime import date
atual=date.today().year
dados= dict()
dados['Nome']=str(input('Nome:'))
ano=int(input('Ano de nascimento:'))
idade =atual-ano
dados['Idade']=idade
dados['CTPS']=int(input('Carteira de Trabalho (0 não tem)'))
if dados['CTPS']!=0:
    contratração=int(input('Ano de contratação'))
    dados['Contratação']=contratração
    Salario=float(input('Salario: R$'))
    dados['Salario']=Salario
    dados['Aposentadoria']=(contratração+35)-ano
print('=-'*20)
print(dados)
for c,v in dados.items():
    print(f'{c} tem o valor {v}')

