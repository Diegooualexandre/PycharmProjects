d = float(input(' Digite a distãncia (KM): '))
p1 = 0.5 * d
p2 = 0.45 * d
if d <= 200:
    print(f'Distância: {d} Km - Valor da Passagem: R$ {p1:.2f}')
else:
    print(f'Distância: {d} Km - Valor da Passagem: R$ {p2:.2f}')
