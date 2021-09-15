# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)
# Autor: Diego L. Alexandre | Data: 16/07/2021.
cont = n = soma = 0
while n != 999:
    if n != 999:
        cont += 1
        soma += n
        n = int(input('Digite número: '))
    elif n == 999:
        break
print(f'Qtde números digitados: {cont} números.\nSoma números digitados: {soma}')
print('FIM')



''' ..............Resposta do Guanabara..........................................
soma = cont = 0
While True:
    num = int(input('Digite número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A Soma dos {cont} valores foi {soma}')
'''
