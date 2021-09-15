# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
# Autor: Diego L. Alexandre | Data: 15/07/2021
sex = str(input('Digite Sexo [M/F]: ')).strip().upper()[0]
while sex not in 'MnFf':
    sex = str(input('Dados inválidos. Digite seu sexo novamente [M/F]: ')).strip().upper()[0]
print(f'SEXO: {sex}')
