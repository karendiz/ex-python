n = 10;  # definir tamanho do conjunto
conjunto = set();  # define um conjunto vazio
for i in range(n):  # vai de elemento a elemento
    conjunto.add(i);  # adiciona o elemento 'i' ao conjunto
print('O conjunto criado foi: \n');
print(conjunto);  # imprime o conjunto

for item in conjunto:  # cria um laço for que itera sobre o conjunto
    print(item);  # imprime elemento a elemento

li = ['Maça', 'Laranja', 'Uva', 'Maça', 'Abacate', 'Laranja']
c = set(li)
print(c)

s = {'Maça', 'Uva', 'Abacate', 'Laranja', 'Abacaxi'}
s.add('Melancia')
s