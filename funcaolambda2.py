from functools import reduce


def somaQuadrados(a, b):
    somaQ = a**2 + b**2
    return somaQ
print(somaQuadrados(2,3))

somaQuadrados2 = lambda a, b: a**2 + b**2
print(somaQuadrados2(2,3))

x = lambda f : f/2
print(x(10))

lista = [1, 2, 3, 4, 5, 6]
lista1 = list(map(lambda x: x**2, lista)) #eleva ao quadrado os elementos de lista para criar lista1
print("lista = ", lista,"\n\nlista1 = ", lista1)

lista0 = [1,2,3,4,5,6,7,8,9,10]
lista2 = list(map(lambda x: x*2, lista))
print("lista0 = ", lista,"\n\nlista2 = ", lista1)

lista = [1, 2, 3, 4, 5, 6]
produto = reduce(lambda x,y: x * y, lista) #retorna o produto de todos os elemento de lista
print("lista = ", lista,"\n\nproduto = ", produto)

lista = [1, 2, 3, 4, 5, 6,7,8,9,10]
soma = reduce(lambda x,y: x + y, lista) #retorna o produto de todos os elemento de lista
print("lista = ", lista,"\n\nproduto = ", soma)