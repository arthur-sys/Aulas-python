import math
x = float(input("escreva um angulo"))
n = math.radians(x)
sen = math.sin(n)
cos = math.cos(n)
tan =math.tan(n)
print("o angulo {} tem sen {:.2f}, cos {:.2f} e tan {:.2f}".format(x,sen,cos,tan))
