casa = float(input('qual o valor da casa'))
salario = float(input('qual é sua renda mensal'))
anos = float(input('quantos anos deseja pagar a casa '))
parcela = (casa/anos)/12
if parcela <= (30*salario)/100:
    print("para pagar uma casa de {} em {} a prestação sera de {:.2f} emprestimo aprovado".format(casa,anos,parcela))
else:
    print("para pagar uma casa de {} em {} a prestação sera de {:.2f} emprestimo negado".format(casa,anos,parcela))
