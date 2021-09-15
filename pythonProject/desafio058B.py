# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
# Autor: Diego L. Alexandre | Data: 15/07/2021
from random import randint
computador = randint(0, 10)
acerto = False
cont = 0
while not acerto:
    player = int(input('Qual é o seu palpite? '))
    cont += 1
    if player == computador:
        acerto = True
    elif player < computador:
        print('Mais...Tente de novo.')
    else:
        print('Menos...Tente de novo.')
print(f'Computador escolheu número: {computador}')
print(f'Parabéns! Você acertou depois de {cont} tentativas.')
