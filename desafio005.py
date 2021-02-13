#Deseja-se que o círculo contenha informações de posicionamento no plano cartesiano (coordenadas não negativas no eixo x e y)
# dado por um ponto central, além do raio associado. Deve ser possível, calcular a área do círculo, o seu diâmetro, o comprimento da circunferência
# mudar a posição do círculo no plano cartesiano. Por fim, crie um objeto a partir da classe e teste o funcionamento dos métodos implementados.

import math
from idlelib.MultiCall import r


class Círculo:
    def __init__(self,y ,x ,r):
        self.y = y
        self.x = x
        self.r = r

    def obty (self):
        return self.y

    def obtx (self):
        return self.x

    def obtr(self):
        return self.r


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