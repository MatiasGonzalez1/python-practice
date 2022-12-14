class Animales():
  def habla(self):
    print('Soy un animal')
  
  def descripcion(self):
    print('Yo soy un {}'.format(self.animal))
#herencia de clase Animales
class Perro(Animales):
  pass

class Abeja(Animales):
  def __init__(self, animal):
    self.animal = animal
    
animal = Animales()
animal.habla()
#la clase se hereda de animales
perro = Perro()
perro.habla()

abeja = Abeja('Abeja')
abeja.descripcion()