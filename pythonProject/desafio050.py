# Programa que mostra a tabuada
# Autor: Diego L. Alexandre | Data: 13/07/2021
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite número: '))
    if num % 2 == 0:
       cont = cont + 1
       soma = soma + num
print(f'A soma dos dos {cont} números pares é {soma}')
