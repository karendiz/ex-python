# Um programa que realize a união do conteúdo de três listas contendo valores inteiros,
# garantindo ao mesmo tempo que o resultado não contenha valores duplicados.
# Utilizando os tipos de dados list e set resolva o problema.
# Você pode utilizar valores arbitrários dentro das listas.

lista1 = ['Maçã', 'Laranja', 'Uva', 'Maçã', 'Limão', 'Abacate', 'Kiwi', 'Abacaxi']
lista2 = ['Pera', 'Tomate', 'Melancia','Caqui', 'Kiwi', 'Uva', 'Laranja', 'Limão']
lista3 = ['Abacate', 'Banana', 'Melancia', 'Pera', 'Amora', 'Maçã', 'Tomate', 'Caqui']
lista1 = set(lista1)
lista2 = set(lista2)
lista3 = set(lista3)
print(lista1 | lista2 | lista3)