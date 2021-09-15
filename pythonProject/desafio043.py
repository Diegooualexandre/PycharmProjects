'''
    Programa que calcula o IMC
    Autor: Diego L.Alexandre
    Data: 10/07/2021
'''
peso = float(input('Digite o peso: '))
altura = float(input(' Digite altura: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print(f'IMC:{imc:.1f} | Abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'IMC:{imc:.1f} | Peso ideal')
elif 25 <= imc < 30:
    print(f'IMC:{imc:.1f} | Sobrepeso')
elif 30 <= imc < 40:
    print(f'IMC:{imc:.1f} | Obeso')
elif imc >= 40:
    print(f'IMC:{imc:.1f} | Obesidade Mórbida')

