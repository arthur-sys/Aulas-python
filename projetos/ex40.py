print('digite suas notas para calcular sua média ')
n1 = float(input('digite sua primeira nota'))
n2 = float(input('digite sua segunda nota'))
media = (n1+n2)/2
if media < 5.0:
   print('sua média foi {}{:.2f}{} e você esta reprovado '.format('\033[37m', media ,'\033[m'))
elif  media == 5.0 or media < 6.9:
    print('sua média foi {}{:.2f}{} e você esta de recuperação'.format('\033[31m', media, '\033[m'))
elif media == 6.9 or media < 7:
        print('sua média foi {}{:.2f}{} e você esta de recuperação'.format('\033[31m', media, '\033[m'))
elif media >= 7:
    print('sua média foi {}{:.2f}{} e você esta aprovado'.format('\033[1;34m', media, '\033[m'))
