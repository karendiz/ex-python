lista = ['Arroz', 'Feijão', 'Massa', 'Açucar', 'Sal']

i = 0
while i < len(lista):
    if lista[i] == 'Feijão':
        lista[i] = 'Lentilha'
    print(lista[i])
    i += 1

lista = ['Maria', '23', 'Porto Alegre']
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[-1])

n = lista.index('Porto Alegre')
print(n)

nomes = [(1, 'Pedro'), (2, 'Maria'), (3, 'Manoela')]
dicionario = dict(nomes)
del dicionario[0]
