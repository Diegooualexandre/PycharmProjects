# Programa que mostra o grupo da maioridade
# Autor: Diego L. Alexandre | Data: 13/07/2021
totmaior = 0
totmenor = 0
from datetime import date
for c in range(1, 8):
    nasc = int(input(f'Digite {c}º ano de nascimento com 4 dígitos: '))
    atual = date.today().year - nasc
    if atual > 18:
        totmaior += 1
    elif atual < 18:
        totmenor += 1
print(f' Existe(m):\n {totmaior} pessoa(s) maior(es) de idade\n {totmenor} pessoa(s) maior(es) de idade')
