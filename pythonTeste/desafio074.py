# Programa que cria 5 números aleatórios
# Autor: Diego L. Alexandre | Data: 01/08/2021
from random import randint
aleaorio = (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
print(aleaorio)
print('--' * 16)
print(f'Maior valor da Tupla: {max(aleaorio)}')
print(f'Menor valor da Tupla: {min(aleaorio)}')
