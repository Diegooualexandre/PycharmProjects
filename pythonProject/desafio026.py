f = str(input('Digite Frase: ')).strip().upper()
print(f'A letra A aparece: {f.count("A")} vezes')
print(f'Letra "a" aparece pela primeira vez na posição: {f.find("A")+1}\n')
print(f'Letra "a" aparece pela ultima vez na posição  : {f.rfind("A")+1} ')



