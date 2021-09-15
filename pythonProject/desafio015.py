km = float(input(' Digite Km rodados: '))
da = int(input(' Qte Dias alugado: '))
p = da*60 + km*0.15
print(f' Tabela\n Km rodados: {km} Km \n Dias alugado: {da} dia(s)\n Total a pagar: R$ {p:.2f}')
