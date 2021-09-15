# Programa que mostra se é primo
# Autor: Diego L. Alexandre | Data: 13/07/2021
num = int(input('Digite numero: '))
print('''AVISO!
Numeros na cor ROXA  : SÃO DIVISÍVEIS 
Numeros na cor BRANCA: NÃO SÃO DIVISÍVEIS''')
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m O número {num} foi divisível {total} vezes')
if total == 2:
    print(' Portanto, ele é um número primo.')
else:
    print('Ele não é primo')
