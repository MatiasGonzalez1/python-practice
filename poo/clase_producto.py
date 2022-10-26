#DEFINICION DE CLASE PRODUCTO
class Producto:
  Codigo = 0
  Nombre = ''
  Precio = 0
  #DEFINICION DEL CONSTRUCTOR
  def __init__(self, codigo, nombre, precio):
    self.Codigo = codigo  
    self.Nombre = nombre
    self.Precio = precio
    
  def get_Codigo(self):
    return self.Codigo
  
  def set_Codigo(self, codigo):
    self.Codigo = codigo
    
  def get_Nombre(self):
    return self.Nombre
  
  def set_Nombre(self, nombre):
    self.Nombre = nombre
  
  def get_Precio(self):
    return self.Precio
  
  def set_Precio(self, precio):
    self.Precio = precio
    
  def __str__(self):
    return ('El codigo del producto es: ' + str(self.Codigo) + ' su nombre es: ' + str(self.Nombre) + ' y su precio es: ' + str(self.Precio)) 
  
  def calcular_total(self, unidades):
    print (self.Precio * unidades)

#objeto instanciado de clase producto
# miPrimerProducto = Producto

# miPrimerProducto.Codigo = 15
# miPrimerProducto.Nombre = 'Kevin Kessler'
# miPrimerProducto.Precio = 500
# miPrimerProducto.calcular_total(miPrimerProducto, 3)



class Pedido:
  productos = []
  cantidades = []
  
  def __init__(self):
    self.productos = []
    self.cantidades = []
  
  def añadir_producto(self, producto, cantidad):
    if not isinstance(producto, Producto):
      raise Exception('añadir_producto: producto debe ser de la clase Producto')
    if not isinstance(cantidad, int):
      raise Exception('añadir_producto: cantidades debe ser un número')
    if cantidad <= 0:
      raise Exception('añadir_producto: cantidades debe ser un número mayor a cero')
    if producto in self.productos:
      indice = self.productos.index(producto)
      self.cantidades[indice] += cantidad
      
    else:
      self.cantidades.append(cantidad)
      self.productos.append(producto)
    
  def eliminar_producto(self, producto):
      if not isinstance(producto, Producto):
        raise Exception('eliminar_producto: producto debe ser de la clase Producto')
      if producto in self.productos:
        indice = self.producto.index(producto)
        del self.productos[indice]
        del self.cantidades[indice]
      else:
        raise Exception('eliminar_producto: El producto no existe')
    
  def total_pedido(self):
      total = 0
      
      for(p,c)  in zip(self.productos, self.cantidades):
        total += total + p.calcular_total(c)
        
        return total
    
  def mostrar_producto(self):
    for (p,c) in zip(self.productos, self.cantidades):
      print('Producto:' + p.get_nombre() + ', Cantidad:' + str(c))

    p1 = Producto(1, 'producto 1', 5)
    p2 = Producto(2, 'producto 2', 15)
    p3 = Producto(3, 'producto 3', 25)
    
    pedido = Pedido()
    
    try:
      pedido.añadir_producto(p1, 9)
      pedido.añadir_producto(p2, 5)
      pedido.añadir_producto(p3, 14)
      
      print('Total pedido: ' + str(pedido.total_pedido()))
      
      pedido.mostrar_producto()
      
      pedido.eliminar_producto(p2)
      
      pedido.mostrar_producto()
      
    except Exception as e:
      print(e)
      