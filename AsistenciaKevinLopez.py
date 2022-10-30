    '''
Ejercicio Rectangulo
por Lopez Cordoba Kevin
crear una clase rectángulo, con los atributos base y altura, calcular el área mediante un método,
pedir al usuario que ingrese por teclado base y altura
'''
class Rectangulo:
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base

    def area(self):
        area = self.altura*self.base
        return area

base = int(input('Ingrese la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))
rectangulo1 = Rectangulo(base,altura)
print(f'el area del rectangulo es: {rectangulo1.area()}')

