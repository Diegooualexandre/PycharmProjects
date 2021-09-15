# Programa que mostra o peso das pessoas
# Autor: Diego L. Alexandre | Data: 14/07/2021
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher20 = 0
for p in range(1, 5):
    print(f'---- {p}ºPESSOA ----')
    nome = str(input('Digite nome: ')).strip()
    idade = int(input('Digite idade: '))
    sexo = str(input('SEXO [M/F]')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Fm' and idade < 20:
        total_mulher20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é {media_idade}')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}')
print(f'Ao todo temos {total_mulher20} mulheres com idade menor de 20 anos.')
