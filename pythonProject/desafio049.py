# Programa que mostra a taabuada
# Autor: Diego L. Alexandre | Data: 13/07/2021
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')
