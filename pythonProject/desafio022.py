n = input(' Digite nome completo: ')
d= n.split()
print(f' Nome com todas as letras maiúsculas: {n.upper()}')
print(f' Nome com todas as letras minúsculas: {n.lower()}')
print(f" Quantas letras ao todo(com espaços) é: {len(n)}")
print(f" Quantas letras ao todo(sem espaços) é: {len(n)-n.count(' ')}")
print(f' Mostre lista Nomes: {d}')
print(f' Mostre o Nome: {d[0]} \n Qte letras nome: {len(d[0])}')
print(f' Mostre o Sobrenome: {d[1]}\n Qte letras sobrenome: {len(d[1])}')



