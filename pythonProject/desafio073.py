# Tupla do Campeonato brasileiro
# 5 primeiros colocador | z-4 | lista em ordem alfabética | posição da chapecoense
# Autor: Diego Alexandre | 31/07/2021.
campeonato = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Atlético-PR', 'Flamengo',
              'Ceara', 'Atlético-GO', 'Bahia', 'Corinthians', 'Fluminense', 'Santos', 'Juventude',
              'Internacional', 'São Paulo', 'Cuiabá', 'Sport', 'América-MG', 'Grêmio', 'Chapecoense')
print('''MENU
[1] 5 Primeiros Colocados(G-5)
[2] Zona do Rebaixamento(Z-4)
[3] Posição da Chapecoense
[4] Lista em ordem alfabética''')
print('-------'*5)
option = int(input('Digite a opção do menu [de 1 a 4]: '))
print('-------'*5)
while True:
    if option == 1:
        for c in campeonato[0:5]:
            print(c)
        break
    elif option == 2:
        for c in campeonato[-4:]:  # [-4: ] ele começa em -4 e vai até o final. Seria o mesmo que colocar [16:20]
            print(c)
        break
    elif option == 3:
        for c in range(len(campeonato)):
            if c == campeonato.index('Chapecoense'):
                print(f'Chapecoense: {c+1}ª Posição')
        break
    elif option == 4:
        print(sorted(campeonato))
        break
    else:
        option = int(input('Digite a opção do menu [de 1 a 3]: '))
print('- FIM -')
