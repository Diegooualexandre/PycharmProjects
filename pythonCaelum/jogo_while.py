print('*'*24)
print(f'*'*2+'Jogos de adivinhação'+'*'*2)
print('*'*24)
secret_number = 42
number_of_attempt = 3
my_round = 1
while number_of_attempt > 0:
    print(f'Round {my_round} of {number_of_attempt} attempt')
    c = int(input(' Write number: '))
    print(f'You write: {c}')
    score = c == secret_number
    bigger = c > secret_number
    taller = c < secret_number
    if score:
        print('You have score the number! Congratulations.')
        break
    elif bigger:
        print('Wrong attempt. Your attempr is bigger than number')
    elif taller:
        print('Wrong. Your attempt is taller than number')
    my_round = my_round + 1
    number_of_attempt = number_of_attempt - 1
print('Game Over')
