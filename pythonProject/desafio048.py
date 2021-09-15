# Programa que mostra soma de todos os números ímpares e multiplos de 3
# Autor: Diego L. Alexandre | Data: 13/07/2021
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma} ')
