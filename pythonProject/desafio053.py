# Programa que mostra se é palíndromo
# Autor: Diego L. Alexandre | Data: 13/07/2021
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
print(f'Você digitou a frase {junto}')
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print(f'A palavra digitada é um Palíndromo!')
else:
    print('A palavra digitada não é um palíndromo')
