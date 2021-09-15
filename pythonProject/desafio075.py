#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.
num = (int(input('1º número: ')), int(input('2º número: ')), int(input('3º número: ')), int(input('4º número: ')))
cont = 0
print(f'Tupla: {num}')
print('--' * 16)
print(f'Número 9 aparece: {num.count(9)} vezes')
if 3 in num:
    print(f'Posição do 1º número 3 digitado: {num.index(3)+1}')
else:
    print(f'valor 3 não encontrado na tupla.')
print(f'Qte valores pares digitados: ', end='')
for c in num:
    if c % 2 == 0:
        cont += 1
        print(c, end=' ')
