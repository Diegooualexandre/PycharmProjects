salario = float(input(' Digite o salário do funcionário: R$ '))
if salario > 1250:
    novo = salario + (salario * 10/100)
if salario <= 1250:
    novo = salario + (salario * 15/100)
print(f' Salário antigo: {salario:.2f}\n Novo salário: R$ {novo:.2f}')
