# Programa que mostra uma PA de 10 segmentos
# Autor: Diego L. Alexandre | Data: 13/07/2021
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c)
print('End')
