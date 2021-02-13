soma_lambda = lambda numero1, numero2: numero1 + numero2;

print(soma_lambda(1,2))

valor = lambda: 3 + 2
def valor ( ):    return 3 + 2

bom_dia = lambda: print('Bom dia')
bom_dia()

numeros = [0, 2, 3, 4, 5, 7]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
for par in pares:
    print(par)

numeros = [0, 2, 3, 4, 5, 7]
pares = filter(lambda valor: valor % 2 == 0, numeros)
for par in pares:
    print(par)