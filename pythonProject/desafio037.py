''' Programa que pega um número inteiro qualquer e converte para outras bases numéricas
    Autor: Diego Alexandre
    Data: 10/07/2021
'''
num = int(input('Insira número: '))
print('''Escolha uma das opções para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
option = int(input('Digite sua opção: '))
if option == 1:
      print(f' Número:{num} | Convertido para Binário: {bin(num)[2:]}')
elif option == 2:
      print(f' Número:{num} | Convertido para Octal: {oct(num)[2:]}')
elif option == 3:
      print(f' Número:{num} | Convertido para Exadecimal: {hex(num)[2:]}')
else:
      print('Opção inválida. Por favor,tente novamente.')
