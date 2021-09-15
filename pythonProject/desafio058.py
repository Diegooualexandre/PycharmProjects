# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
# Autor: Diego L. Alexandre | Data: 15/07/2021
import random
n = int(input(' Digite um número entre 0 e 5: '))
z = random.randint(0, 10)
cont = 1
while n != z:
    if n != z:
        cont += 1
        n = int(input(' Digite um número entre 0 e 5: '))
print(f'({z}) Parabéns! Você acertou depois de {cont} tentativas.')
print('-FIM-')
