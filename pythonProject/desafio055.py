# Programa que mostra o peso das pessoas
# Autor: Diego L. Alexandre | Data: 14/07/2021
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite {c}º peso(kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f' O maior peso registrado é {maior} Kg')
print(f' O menor peso registrado é {menor} Kg')
