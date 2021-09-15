n1 = int(input(' Digite primeiro número: '))
n2 = int(input(' Digite segundo número: '))
n3 = int(input(' Digite terceiro número: '))
maior = n1
if n2 > n1 and n3 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f' O maior número é {maior}')
