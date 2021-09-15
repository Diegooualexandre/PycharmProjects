#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
tupla = ('Padawan', 'Jedi', 'Sith', 'Alderaan', 'Coruscant',
         'Anakin', 'Padme', 'Obiwan', 'Chewebacca', 'Luke',
         'Leia', 'Yoda', 'Tatooine', 'Ahsoka', 'Luminara')
print(tupla)
print('-' * 153)
for palavra in tupla:
    print(f'\nPara cada palavra {palavra.upper()}, temos as vogais:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')