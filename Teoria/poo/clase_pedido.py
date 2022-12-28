from signal import raise_signal
from poo.clase_producto import Producto


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
      indice = self.productos.index(productos)
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
    