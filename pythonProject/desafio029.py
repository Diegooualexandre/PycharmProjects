v = float(input('Digite a velocidade do carro (em Km/h): '))
m = 7*(v-80)
if v >80:
    print(f'Você está a mais de 80 Km/h e foi multado em: R$ {m:.2f}')
else:
    if v == 80:
        print('Você está no limite de velocidade. Se ultrapassar será multado!')
    else:
        print('Obrigado por respeitar os limites de velocidade.Boa Viajem!')