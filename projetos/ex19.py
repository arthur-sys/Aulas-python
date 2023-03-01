import random
q = str(input("primeiro aluno"))
w = str(input("segundo aluno"))
e = str(input("terceiro aluno"))
r = str(input("quarto aluno"))
lista = [q,w,e,r]
r = random.choice(lista)
print("o aluno escolhido foi {}".format(r))
