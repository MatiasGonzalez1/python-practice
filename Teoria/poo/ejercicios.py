# Ejercicio 1

# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

# class Alumno():

#   def __init__(self, nombre, nota):
#     self._nombre = nombre
#     self._nota = nota
  
#   @property
#   def nombre(self):
#       return self._nombre
    
#   @nombre.setter
#   def nombre(self, nombre):
#     self._nombre = nombre 
  
#   def imprimir(self):
#     print(f"El nombre es {self._nombre} y su nota {self._nota}")   

#   def resultado(self):
#     if self._nota < 7:
#       print('Has reprobado')
#     else:
#       print('Has aprobado')
      
# pedro = Alumno('Pedro', 9)
# pedro.imprimir()
# pedro.resultado()

# Ejercicio 2

# Escribir una clase en python que calcule pow(x, n)

# x = es la base

# n = es el exponente

# class Calcular():
#   def pow(self, x, n):
#     self.n = n
#     self.x = x

# Ejercicio 1

# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

# class Calculadora():
#   def __init__(self):
#     #se pide al usuario que ingrese los datos
#     self.num1 = float(input('Ingrese un valor: '))
#     self.num2 = float(input('Ingrese un valor: '))
  
#   def suma(self):
#     self.suma = self.num1 + self.num2
#     print('La suma da como resultado', self.suma)
  
#   def resta(self):
#     self.resta = self.num1 - self.num2
#     print('La resta da como resultado', self.resta)

#   def multi(self):
#     self.multi = self.num1 * self.num2
#     print('La multiplicacion da como resultado', self.multi)
  
#   def resta(self):
#     self.division = self.num1 / self.num2
#     if self.num1 == 0 or self.num2 == 0:
#       print('No se puede dividir entre 0')
#     else:
#       print('La division da como resultado', self.division)

# calcular = Calculadora()
# calcular.suma()
# calcular.resta()
# calcular.multi()
# calcular.division()

# Ejercicio 2

# Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. Luego, se debe calcular area de un cuadrado, triangulo y pentagono
    
    
# Ejercicio 1

# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

# class Fabrica():
#   def __init__(self, llantas, color, precio):
#     self.llantas = llantas
#     self.color = color
#     self.precio = precio
  
#   def datos(self):
#     print('El vehiculo tiene', self.llantas, 'llantas')
#     print('El vehiculo es del color', self.color)
#     print('El vehiculo cuesta', self.precio)
    
# class Carro(Fabrica):
#   pass

# class Moto(Fabrica):
#   pass

# moto = Moto(2,'azul', 3)
# moto.datos()

###################################POLIMORFISMO########################################
# Ejercicio 1

# Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro
  
# class Marino():
#   def hablar(self):
#     print('Hola...')
    
# class Pulpo(Marino):
#   def hablar(self):
#     print('Hola soy un Pulpo')

# class Foca(Marino):
#   def hablar(self, mensaje):
#     self.mensaje = mensaje
#     print(self.mensaje)

    
# marino = Marino()
# marino.hablar()

# pulpo = Pulpo()
# pulpo.hablar()

# foca = Foca()
# foca.hablar('Hola soy una foca')

# Ejercicio 1

# Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
  def __init__(self, Nombre):
    self.Nombre = Nombre

class Carrera():
  def carrera(self, especialidad):
    self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
  def datos(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    print(f'Mi nombre es {self.nombre}, tengo {self.edad} años, mi especialidad es {self.especialidad} y mi universidad es {self.Nombre}')
    
persona = Estudiante('Aconcagua')
persona.carrera('Licenciatura en asdm')
persona.datos('Carlos', 20)