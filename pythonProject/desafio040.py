'''
    Programa que calcula a média do aluno
    Autor: Diego L. Alexandre
    Data: 10/07/2021
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print(f'Media: {media}\n Status: Reprovado')
elif 5 < media <= 6.9:
    print(f'Media: {media}\n Status: Recuperação')
elif media >= 7:
    print(f'Media: {media}\n Status: Aprovado')
