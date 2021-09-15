import random
a1 = input('Nome do primeiro estudante: ')
a2 = input('Nome do segundo estudante: ')
a3 = input('Nome do terceiro estudante: ')
a4 = input('Nome do quarto estudante: ')
l = [a1,a2,a3,a4]
e = random.choice(l)
print(f'Estudante sorteado foi: {e}')
