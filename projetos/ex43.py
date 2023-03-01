peso = float(input('qual é seu peso? (KG)'))
altura = float(input('qual é sua altura? (M)'))
imc = peso/(altura**2)
print('seu IMC é igual a {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[:31m se cuide voce esta abaixo do peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('parabéns você esta com o peso normal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >=30 and imc < 35:
    print('obesidade grau 1')
elif imc >= 35 and imc < 40:
    print('obesidade grau 2')
else:
    print('obesidade grau 3')


