'''
    Programa que lê o ano de nascimento de Atleta e mostra sua categoria
    Autor: Diego . Alexandre
    Data: 10/07/2021
'''
from datetime import date
nascimento = int(input('Digite ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade <= 9:
    print(f' Idade do Atleta: {idade}\n Categoria: Mirim')
elif idade <= 14:
    print(f' Idade do Atleta: {idade}\n Categoria: Infantil')
elif idade <= 19:
    print(f' Idade do Atleta: {idade}\n Categoria: Junior')
elif idade <= 20:
    print(f' Idade do Atleta: {idade}\n Categoria: Senior')
elif idade > 20:
    print(f' Idade do Atleta: {idade}\n Categoria: Master')
