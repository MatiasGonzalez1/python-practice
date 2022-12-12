# class FabricaTelefono():
#   marca = 'Samsung'
  
#   def elaborarHuawei(self):
#     self.marca = 'Huawei'
    
# telefono = FabricaTelefono()
# telefono.elaborarHuawei()
# print(telefono.marca)

class FabricaTelefono():
  def __init__(self, marca, color):
    self.marca = marca
    self.color = color
    print('Estoy ejecutando el metodo init', marca,color)
    
telefono = FabricaTelefono('Galaxi', 'Negro')