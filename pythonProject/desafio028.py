import random
n = int(input(' Digite um número entre 0 e 5: '))
z = random.randint(0, 5)
if n == z:
    print(f'({z}) Parabéns! Você acertou.')
else:
    print(f'({z}) Poxa, você errou...')
