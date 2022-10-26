from moto import *

class Triciclomotor(Moto):
  def __init__(self, marca, modelo, patente, kilometraje, añoPatentamiento, color, capacidadDeTanque, capacidadDeCarga, cantidadDeRuedas):
    Moto.__init__(self, marca, modelo, patente, kilometraje, añoPatentamiento, color, capacidadDeTanque)
    self.capacidadDeCarga = capacidadDeCarga
    self.cantidadDeRuedas = cantidadDeRuedas
    
  def __str__(self):
    return Moto.__str__(self) + ' Este tipo de vehiculo tiene una capacidad de carga de: ' + str(self.capacidadDeCarga) + ' y tiene un total de: ' + str(self.cantidadDeRuedas) + ' ruedas'
  
trici = Triciclomotor('Zanella', 2000, 'jhk1123', 1000, 1990, 'verde', 200, 500, 3)

print(trici)