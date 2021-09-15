#Programa que calcula o fatorial de um número qualquer
# Autor: Diego L. Alexandre | Data: 15/07/2021.
num = int(input('Digite número: '))
contador = num  #porque o fatorial de n começa com n. ex: fatorial de 5 começa com 5 e decresce(5,4,3,2 e 1).
fatorial = 1
print(f'Calculando fatorial de {num}! ', end=' ')
while contador > 0:
    print(f'{contador}', end='')
    print(f' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')


