'''
    Programa que calcula o valor pago pelo produto
    Autor: Diego L. Alexandre
    Data: 10/07/2021
'''
valor = float(input('Digite o valor do produto: R$ '))
print('''Escolha uma opção:
         [1] Á Vista (Dinheiro/Cheque)
         [2] Á Vista (Cartão)
         [3] 2x no Cartão
         [4] 3x ou mais no Cartão''')
opcao = int(input('Digite opção: '))
if opcao == 1:
    a = valor - valor * (10/100)
    print(f'Sua compra será paga em 1x de R$ {valor:.2f} + 10% de desconto')
    print(f'Sua compra de RS {valor:.2f} vai custar R$ {a:.2f} ao final')
elif opcao == 2:
    b = valor - valor * (5 / 100)
    print(f'Sua compra será paga em 1x de R$ {valor:.2f} + 5% de desconto')
    print(f'Sua compra de RS {valor:.2f} vai custar R$ {b:.2f} ao final')
elif opcao == 3:
    n_parcela = valor / 2
    print(f'Sua compra será paga em 2x de R$ {n_parcela:.2f}')
    print(f'Sua compra vai custar R$ {valor:.2f} ao final')
elif opcao == 4:
    num_parcelas = int(input('Quantidade de Parcelas: '))
    n_parcela = (valor + valor * (20/100)) / num_parcelas
    c = n_parcela * num_parcelas
    print(f'Sua compra será paga em {num_parcelas}x de R$ {n_parcela:.2f}')
    print(f'Sua compra de RS {valor:.2f} vai custar R$ {c:.2f} ao final')
else:
    print('Opção Inválida. Tente Novamente!')
