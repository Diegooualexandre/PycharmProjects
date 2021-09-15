# num = int(input('Digite um número: '))
# cont = 0
# for c in range(1, num + 1):
#     resto = num % c
#     if resto == 0:
#         cont += 1
# if cont == 2:
#     print(f'{num} é primo')
# else:
#     print('Número não é primo')
# print('-FIM-')

for num in range(101):
    cont = 0
    for c in range(1, num + 1):
        resto = num % c
        if resto == 0:
            cont += 1
    if cont == 2:
        print(num)
