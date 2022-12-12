class FabricaTelefonos():
  def __init__(self, marca, *colores, **modelo):
    self.marca = marca
    self.colores = colores
    self.modelo = modelo
    
telefono = FabricaTelefonos('Alcatel', 'Negro', 'Azul', 'Rojo', a1 = 'v3', a2 = 'v3black')
print(telefono.marca)
print(telefono.colores)
print(telefono.modelo)
telefono.memoria = 512
print(telefono.memoria)