import math
co = float(input(' Digite o cateto oposto: '))
ca = float(input(' Digite o cateto adjacente: '))
'''h = (co**2+ca**2)**(1/2)'''
h = math.hypot(co,ca)
print(f'A hipotenusa vai medir {h}')

'''from math import hypot
co = float(input(' Digite o cateto oposto: '))
ca = float(input(' Digite o cateto adjacente: '))
h = hypot(co,ca)
print(f'A hipotenusa vai medir {h}')'''