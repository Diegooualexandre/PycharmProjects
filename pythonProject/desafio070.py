tot = totmil = cont = menor = 0
barato = ''
while True:
    nome_produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Digite preço: R$ '))
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_produto
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'Total: R$ {tot:.2f}')
print(f'{totmil} Produto(s) custando mais de R$ 1000,00')
print(f'O Produto mais barato foi {barato} e custa: R$ {menor}')
