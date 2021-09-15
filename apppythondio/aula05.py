lista = [1, 3, 5, 7]
lista_animal = ['Cachorro', 'gato', 'Elefante']
print(lista)
print(lista_animal[1])
print('---'*14)
print('Abaixo usando laço for para lista_animal: ')
print('---'*14)
cont = 0
for c in lista_animal:
    print(f'{cont}º - {c}')
    cont += 1
print('---'*14)
print('função "sum()" em Python soma os termos da lista = [1, 3, 5, 7]: ')
print(sum(lista))
print('---'*14)
print('Função "max() e Min()" buscam respectivamente, o maior e menor valor da lista = [1, 3, 5, 7] ')
print(f'Maior valor da lista:', max(lista))
print(f'Menor valor da lista:', min(lista))
print('---'*14)
print('isso também vale para strings. Pegaremos o maior e menor valor da lista_animal:')
print('---'*14)
print(f'Maior valor da lista:', max(lista_animal))  # aqui vai ser gato pq começa com a letra 'g'
print(f'Menor valor da lista:', min(lista_animal))  # aqui vai ser chachorro pq começa com a letra 'c'
print('---'*14)
print('Podemos usar laço para validar se um elemento faz parte da lista: como gato ou outro como lobo.')
print('---'*14)
if 'gato' in lista_animal:
    print('exite gato na lista_animal')
else:
    print('Não existe gato na list_animal')
print('---'*14)
if 'lobo' in lista_animal:
    print('exite lobo na lista_animal')
else:
    print('Não existe lobo na list_animal')
    lista_animal.append('lobo')
    print(lista_animal)
print('---'*14)
print('Comando sort() é usado para ordenar uma lista')
print('---'*14)
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
print('---'*14)
print('Comando reverse()ordena lista de trás para frente')
lista.reverse()
lista_animal.reverse()
print(lista)
print(lista_animal)
print('---'*14)
tupla = (1, 2, 3, 4, 5, 6, 7)
print(len(tupla))
print('---'*14)
print('Comando "tuple" transforma lista em tupla')
tupla_animal = tuple(lista_animal)
print(type(lista_animal))
print(tupla_animal)
print('---'*14)
print('se você usar o parâmetro "list", isso converte tupla em lista')
nova_lista_animal = list(tupla_animal)
print(type(nova_lista_animal))
print(nova_lista_animal)
print('---'*14)