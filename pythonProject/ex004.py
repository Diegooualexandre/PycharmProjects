d = input('Digite algo: ')
print(type(d))
print(f'Só tem espaço? {d.isspace()}')
print(f'É um número?{d.isnumeric()}')
print(f'É alfabetico?{d.isalpha()}')
print(f'É alfanumérico?{d.isalnum()}')
print(f'Está em maiúscula?{d.isupper()}')
print(f'Está em minúscula?{d.islower()}')
print(f'Está capitalizada?{d.istitle()}')
