vel = float(input('digite a velocidade que o carro esta '))
if vel > 80:
    print('voce foi multado em {} R$'.format((vel - 80)*7.00))
else:
    print('tenha um bom dia e dirija com segurança')
