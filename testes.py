from idlelib.MultiCall import r

x = float(input('Digite um valor para x: '))
y = float(input('Digite um valor para y: '))
r = float(input('Digite um valor para r: '))

circ = Círculo('x','y', 'r')

area = 3.14 * (r ** 2)
diametro = 2 * r
circunferencia = 2 * 3.14 * diametro


class calculo (Círculo):
    pass

#Principal
print("O eixo do círculo em y é de: {}".format(y))
print("O eixo do círculo em x é de: {}" .format(x))
print("O raio do círculo é de: {}".format(r))
print('A área do círculo é de: ',area)
print('A circunferência é de: ',circunferencia)
print('O diâmetro do círculo é de: ',diametro)