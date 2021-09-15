print('*'*24)
print(f'*'*2+'Jogos de adivinhação'+'*'*2)
print('*'*24)
secret_number = 42
c = int(input('Write number: '))
print(f'Number submitted: {c}')
if c == secret_number:
    print('Congratulations! You discover the number.')
elif c > secret_number:
    print('Failed. Appointment is bigger than secret number')
elif c < secret_number:
    print('Failed.Appointment is minor than secret number')
