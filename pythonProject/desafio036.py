''' Programa que calcula se empréstimo bancário é aprovado ou não.
    Auto: Diego Alexandre
    Data: 10/07/2021
'''
preco_casa = float(input(' Digite valor do imóvel: R$  '))
salario = float(input(' Digite salário: R$ '))
tempo = int(input(' Digite Qte de anos a pagar: '))
prestacao_mensal = preco_casa/(tempo*12)
valida = 30/100*salario
print(f' Valor da prestação mensal é: R$ {prestacao_mensal:.2f}\n')
print('-'*40)
if prestacao_mensal <= valida:
    print('APROVADA: Sua solicitação de empréstimo foi aprovada com sucesso. ')
else:
    print('NEGADA: Sua solicitação de empréstimo foi recusada junto a instituição bancária.')
