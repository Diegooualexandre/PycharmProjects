"""n = input(' Digite número entre 0 e 9999: ')
m = n[0:1]
c = n[1:2]
d = n[2:3]
u = n[3:4]
print(f' Número digitado: {n}\n Milhar: {m}\n Centena: {c}\n Dezena: {d}\n Unidade: {u}')"""

num = int(input(' Digite número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f' Analisando o número {num}')
print(f' Unidade: {u}\n Dezena : {d}\n Centena: {c}\n Milhar : {m}')
