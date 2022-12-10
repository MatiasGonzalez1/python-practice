
# def suma():
#   a = int(input('Ingrese el primer numero: '))
#   b = int(input('Ingrese el segundo numero: '))
#   return a + b

# print(suma())


# Ejercicio 1

# Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio

def area(base, altura):
  return base * altura

def circulo(radio):
  calculo = radio **2 * 3.14
  return calculo
print(area(2, 2))

print(circulo(3))
# Ejercicio 2

# Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

def list(*num):
  print(len(num))
  
list(1, 2, 3, 4, 5)