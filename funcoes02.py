def soma(a,b):
    s = a + b
    print(s)

#Programa Principal
soma(4,5)
soma(8,9)
soma(2,1)

def contador(*núm):
    print(núm)


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

def contador(*núm):
    for valor in núm:
        print(valor, end='')
    print('FIM!')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

