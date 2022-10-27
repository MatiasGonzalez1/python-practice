
#definicion de clase
from typing import NewType


class Coche():
  #funcion
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
        
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")
        
class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

#definicion de accion
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
        
#instancio

miVehiculo = Coche()
# input('Ingrese un vehiculo, opciones \n1: Coche\n2: Moto\n3:Camion\n')

desplazamientoVehiculo (miVehiculo)