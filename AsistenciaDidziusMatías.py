class Cubo:

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad


ancho = int(input('Ingrese el ancho: '))
altura = int(input('Ingrese la altura: '))
profundidad = int(input('Ingrese la profundidad: '))

cubo1 = Cubo(ancho, altura, profundidad)
print(f'El volumen es: {cubo1.calcular_volumen()}')
