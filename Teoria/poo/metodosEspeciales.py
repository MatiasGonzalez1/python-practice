class FabricaTelefono():
  def __init__(self, marca, color):
    self.marca = marca
    self.color = color
    print(f'El objeto {self.marca} ha sido creado')
  
  def __str__(self):
    return 'El objeto es {}'.format(self.marca)
  
  def __del__(self):
    print(f'El objeto {self.marca} ha sido destruido')
    
telefono = FabricaTelefono('Nokia', 'Negro')
print(telefono.marca)
print(telefono)