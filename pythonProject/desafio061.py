#Programa que calcula o primeiro termo e a razão de uma PA só que usando laço While
#Refazendo o Desafio 051
# Autor: Diego L. Alexandre | Data: 15/07/2021.
print('Gerador de PA')
print('-='* 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')
