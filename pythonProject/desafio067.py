#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo
# Autor: Diego L. Alexandre | Data: 16/07/2021
while True:
    n = int(input('Digite o valor: '))
    if n < 0:
        break
    else:
        print('===' * 4)
        print(f'Tabuada de {n}')
        for c in range(1, 11):
            s = n * c
            print(f'{n} x {c:2} = {s}')
        print('==='*4)
print('FIM')



