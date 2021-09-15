# Crie um programa que leia dois valores e mostre um menu na tela um menu de opções:
# [ 1 ] somar - [ 2 ] multiplicar - [ 3 ] maior - [ 4 ] novos números - [ 5 ] sair do programa
# Autor: Diego L. Alexandre | Data: 15/07/2021
from time import sleep
n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
option = 0
while option != 5:
    print('''
    [1] SOMA
    [2] MULTIPLICAÇÃO
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    option = int(input('Digite opção[de 1 a 5]: '))
    if option == 1:
        soma = n1 + n2
        print(f'SOMA [{n1}+{n2}] = {soma}')
    elif option == 2:
        multi = n1 * n2
        print(f'MULTIPLICAÇÃO [{n1}x{n2}] = {multi}')
    elif option == 3:
        if n1 > n2:
            print(f'Maior número[entre {n1} & {n2}] é {n1}')
        elif n1 < n2:
            print(f'Maior número[entre {n1} & {n2}] é {n2}')
        elif n1 == n2:
            print(f'Os números são iguais.')
    elif option == 4:
        print('Digite os números novamente!')
        n1 = int(input('Digite 1º número: '))
        n2 = int(input('Digite 2º número: '))
    elif option == 5:
        print('Saindo do Sistema.')
    else:
        print('Opção Inválida.Tente de novo!')
    print('-='*20)
    sleep(2)
print('FIM')
