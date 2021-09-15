print('*'*24)
print(f'*'*2+'Jogos de adivinhação'+'*'*2)
print('*'*24)
secret_number = 42
total_attempts = 3
my_round = 1
for my_round in range(1, total_attempts+1):
    print(f'Attempt {my_round} of {total_attempts} ')
    c = int(input(' Wtrite Attempt: '))
    score = c == secret_number
    bigger = c > secret_number
    taller = c < secret_number
    if score:
        print('Congratulations! You score the secret number.')
        break
    elif bigger:
        print('Wrong. Attempt is bigger than secret number')
    elif taller:
        print('Wrong. You attempt is taller than secret number.')
print('Game Over')
