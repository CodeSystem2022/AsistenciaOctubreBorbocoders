class Cubo:  
  """
 Crear la clase Cubo con los atributos ancho, alto y profundidad utilizando el método calcular_volumen que tendrá la fórmula:
  volumen = ancho * altura * profundidad.
  Valores ingresados por el usuario.
  """
  def __init__(self, ancho, altura, profundidad): 
   self.ancho = ancho
   self.altura = altura 
   self.profundidad = profundidad
  
  def calcular_volumen(self):
   return self.ancho * self.altura * self.profundidad
  
  ancho = int(input('Digite el ancho del cubo: '))
  altura = int(input('Digite la altura del cubo: ')) 
  profundidad = int(input('Digite la profundidad del cubo: '))   
  
  Cubo1 = Cubo(ancho, altura, profundidad)
  print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')  
}
  
  
