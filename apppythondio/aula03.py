a = int(input('primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('terceiro valor: '))
if a > b and a > c:
    print(f'maior valor: {a}')
elif b > a and b > c:
    print(f'O maior é: {b}')
else:
    print(f'O maior é: {c}')
print('-FIM-')
