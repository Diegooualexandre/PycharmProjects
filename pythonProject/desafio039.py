'''
    Programa que lê a idade de jovem e informa estatus de alistamento militar
    Autor: Diego L. Alexandre
    Data: 10/07/2021
'''
from datetime import date
atual = date.today().year
ano = int(input('Digite ano de nascimento: '))
idade= atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if idade == 18:
    print(f'Você precisa se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta(m) {saldo} ano(s) para seu alistamento.')
    alistamento = atual + saldo
    print(f'Seu alistamento será no ano de {alistamento}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    alistamento = atual - saldo
    print(f'Seu alistamento foi no ano de {alistamento}')
