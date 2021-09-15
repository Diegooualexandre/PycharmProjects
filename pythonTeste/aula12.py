nome = str(input('Qual é o seu nome: '))
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Beatriz Jessica Joana':
    print(' belo nome feminino')
else:
    print('Seu nome é bem normal...')
print(f'Tenha um bom dia, {nome}')
