for i in range(1,10):
    print(3*i)


###################
x = 1
while x<=3:
    print(x)
    x = x + 1


###################
numeroFim = int(input('Digite o número para a condição de parada: '))
x = 1
while x<=numeroFim:
    print(x)
    x = x + 1


###################
contador = 1
soma = 0
while contador <= 5:
    numero = int(input('Digite o número a ser acumulado: '))
    soma = soma + numero
    contador = contador + 1
print('Soma: ', soma)


###################
soma = 0
while True:
    parada = int(input('Digite um valor para a soma ou 0 para sair: '))
    if parada == 0:
        break
    soma = soma + parada
print('Soma: ', soma)


###################
tabuada = 1
while tabuada <= 10:
    numero = 0
    while numero <=10:
        multiplicacao = tabuada * numero
        print(tabuada, '*',numero,'=', multiplicacao)
        numero = numero + 1
    print('-----')
    tabuada = tabuada + 1


###################
listaString = ['item1','item2','item3','item4','item5']
#Exemplo1
for item in listaString:
    print(item)
#Exemplo2
print('------------')
for i in range(0, len(listaString)):
    print(listaString[i])