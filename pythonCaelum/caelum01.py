numero = 45
chute = int(input('Digite número: '))
if chute == numero:
    print(f'Número digitado {chute}. Parabéns! Você acertou.')
elif chute > numero:
    print(f'Numero digitado: {chute}. Você errou! chute está acima do numero.')
elif chute < numero:
    print(f'Numero digitado: {chute}. Você errou! chute digitado é menor que numero')
