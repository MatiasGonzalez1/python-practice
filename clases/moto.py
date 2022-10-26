#se define la clase
class Moto:
  Marca = ''
  Modelo = ''
  Patente = ''
  Kilometraje = 0
  AñoPatentamiento = 0
  Color = ''
  CapacidadDeTanque = 0 
  #se define el constructor
  def __init__(self, marca, modelo, patente, kilometraje, añoPatentamiento, color, capacidadDeTanque):
    self.Marca = marca
    self.Modelo = modelo
    self.Patente = patente
    self.Kilometraje = kilometraje
    self.AñoPatentamiento = añoPatentamiento
    self.Color = color
    self.CapacidadDeTanque = capacidadDeTanque
  
  #retorno el valor de Marca
  def get_Marca(self):
    return self.Marca
  #asigno a Marca el valor de marca
  def set_Marca(self, marca):
    self.Marca = marca
  
  def get_Modelo(self):
    return self.Modelo
  
  def set_Modelo(self, modelo):
    self.Modelo = modelo
    
  def get_Patente(self):
    return self.Patente
  
  def set_Patente(self, patente):
    self.Patente = patente
  
  def get_Kilometraje(self):
    return self.Kilometraje
  
  def set_Kilometraje(self, kilometraje):
    self.Kilometraje = kilometraje

  def get_Color(self):
        return self.Color

  def set_Color(self, color):
        self.Color = color

  def get_CapacidadTanque(self):
        self.CapacidadTanque

  def set_CapacidadTanque(self, capacidadTanque):
        self.CapacidadTanque= capacidadTanque

  def getAñoPatentamiento(self):
        return self.AñoPatentamiento

  def set_AñoPatentamiento(self,añoPatentamiento):
        self.AñoPatentamiento = añoPatentamiento
      
  def __str__(self):
    return('La marca de la moto es: ' + self.Marca + ' modelo ' + str(self.Modelo) + ' su patente es ' + str(self.Patente) + ' y el kilometraje es de: ' + str(self.Kilometraje) + 'su color es: ' + self.Color + ' y el año de patentamiento es: ' + str(self.AñoPatentamiento) + ' y la capacidad de tanque es: ' + str(self.CapacidadDeTanque))
  
# marca= input('Ingrese la marca de la moto.')
# modelo= input('Ingrese el modelo de la moto.')
# patente= input('Ingrese la patente de la moto.')
# kilometraje= input('Ingrese el kilometraje de la moto.')

# def MotosConMenosDe1000km(self):
#   for i in zip(self):
#     if(self.kilometraje < 1000):
#       menos1000km = menos1000km + 1
#   return menos1000km

# def Patentes2021(self):
        
#   for i in zip(self):
#     if(self.añoPatentamiento == 2021):
#       patentadasEn2021= patentadasEn2021 + 1      
#   return patentadasEn2021

# miMoto= Moto(marca,modelo,patente,kilometraje)

# print(miMoto)
