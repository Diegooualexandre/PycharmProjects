'''Programa que ler dois numeros e os compara entre si
    Autor: Diego L. Alexandre
    Data: 10/07/2021
'''
num1 = int(input('Insira primeiro número: '))
num2 = int(input('Insira segundo número: '))
if num1 > num2:
    print(f'O primeiro valor {num1} é maior que o segundo valor {num2}')
elif num1 < num2:
    print(f'O segundo valor {num2} é maior que o primeiro valor {num1}')
elif num1 == num2:
    print(f'São iguais os dois valores: {num1} é igual a {num2}')
