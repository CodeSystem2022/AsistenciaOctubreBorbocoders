class Rectangulo:

    """
    Crear una clase llamada rectangulo,, debe tener 2 atributos: altura y base el nombre del metodo sera calcular area
    utilizando la formula: area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y
    los objetos deben ser 3.
    """
       
    def __init__(self, altura, base):
        self.atri_altura = altura
        self.atri_base = base

    def area(self):
        return self.atri_altura * self.atri_base

atri_base = int(input('Digite el numero para la base del rectangulo: '))
atri_altura = int(input('Digite el numero para la altura del rectangulo: '))
rectangulo0 = Rectangulo(atri_base, atri_altura)
print(f'El area del rectangulo es: {rectangulo0.area()}')


    
