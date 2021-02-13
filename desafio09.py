# reduce() - Sua utilidade está na aplicação de uma função a todos
# os valores do conjunto, de forma a agregá-los todos em um único valor.

from functools import reduce

lista = [1, 2, 3, 4, 5, 6,7,8,9,10]
soma = reduce(lambda x,y: x + y, lista) #retorna o produto de todos os elemento de lista
print("lista = ", lista,"\n\nproduto = ", soma)
