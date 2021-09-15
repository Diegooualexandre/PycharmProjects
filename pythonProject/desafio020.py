'''import random
a1 = input(' Digite o nome do 1º estudante: ')
a2 = input(' Digite o nome do 2º estudante: ')
a3 = input(' Digite o nome do 3º estudante: ')
a4 = input(' Digite o nome do 4º estudante: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print(f'A ordem de apresentação será {lista}')'''

from random import shuffle
a1 = input(' Digite o nome do 1º estudante: ')
a2 = input(' Digite o nome do 2º estudante: ')
a3 = input(' Digite o nome do 3º estudante: ')
a4 = input(' Digite o nome do 4º estudante: ')
lista = [a1,a2,a3,a4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')
