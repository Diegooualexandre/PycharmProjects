# Tupla com contagem por extenso de zero a vinte.
# Autor: Diego L. Alexandre | 31/07/2021

num = int(input('Digite número entre 0 e 20: '))
contagem = ['zero', 'um', 'dois','três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'vinte']

while True:
    if 0 <= num <= 20:
        for c in range(0, len(contagem)):
            if num == c:
                print(contagem[c])
        break
    else:
        num = int(input('Digite número entre 0 e 20: '))
print('-FIM-')
