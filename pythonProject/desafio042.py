'''
    Programa que lê os lados do triangulo e diz de que tipo ele é
    Autor: Diego L. Alexandre
    Data: 10/07/2021
'''
l1 = int(input('Digite valor do Lado 01: '))
l2 = int(input('Digite valor do Lado 02: '))
l3 = int(input('Digite valor do Lado 03: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:

    if l1 == l2 == l3:
        print(f'Lado 01: {l1} - Lado 02: {l2} - Lado 03: {l3} \n Tipo de triângulo: Equilátero.')
    elif l1 != l2 != l3 != l1:
        print(f'Lado 01: {l1} - Lado 02: {l2} - Lado 03: {l3} \n Tipo de triângulo: Escaleno.')
    else:
        print(f'Lado 01: {l1} - Lado 02: {l2} - Lado 03: {l3} \n Tipo de triângulo: Isósceles.')
else:
    print('Não é possível formar triangulos')
