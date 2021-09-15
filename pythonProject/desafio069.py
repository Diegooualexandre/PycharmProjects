tot18 = tothomem = tot20 = 0
while True:
    idade = int(input('Digite idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sex == 'M':
        tothomem += 1
    if sex == 'F' and idade < 20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        print('---' * 8)
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        print('---' * 8)
    if resp in 'N':
        break
print(F'|TOTAL PESSOAS MAIORES DE 18 ANOS: {tot18} pessoas|')
print(F'|TOTAL DE HOMENS: {tothomem}|')
print(F'|TOTAL PESSOAS MULHERES ABAIXO DE 20 ANOS: {tot20} mulheres|')