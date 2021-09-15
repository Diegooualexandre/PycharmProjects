from random import randint
victory = 0
while True:
    player = int(input('Digite valor: '))
    computer = randint(0, 11)
    total = player + computer
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f' Você Jogou: {player} | Computador Jogou: {computer} | Total: {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('PAR | VOCÊ GANHOU')
            victory += 1
        else:
            print('IMPAR | VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('IMPAR | VOCÊ GANHOU')
            victory += 1
        else:
            print('PAR | VOCÊ PERDEU')
            break
        print('Vamos jogar novamente!')
    print(f'NUMERO DE VITÓTIAS: {victory}\nGAMER OVER')


