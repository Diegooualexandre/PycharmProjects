import math
a = float(input(' Digite valor do angulo: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print(f'O Angulo de {a}º tem:\n o Seno de {seno:.2f}º\n cosseno de {cosseno:.2f}º\n tangente de {tangente:.2f}º')
