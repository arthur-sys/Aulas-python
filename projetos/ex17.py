import math
co = float(input("comprimento do cateto oposto:"))
ca = float(input("comprimento do cateto adjacente:"))
hip = math.hypot(co,ca)
print("a hipotenusa vai medir {}".format(hip))

'''co = float(input("comprimento do cateto oposto:"))
ca = float(input("comprimento do cateto adjacente:"))
hip = (co**2+ca**2)**(1/2)
print("a hipotenusa vai medir {}".format(hip))'''
