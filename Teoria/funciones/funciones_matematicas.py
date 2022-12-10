import math
import random

#imprime elevado al cuadrado
print(math.pow(10, 2))
#imprime la raiz flotante
print(math.sqrt(64))
#imprime la raiz entera 'int'
print(math.isqrt(64))
#imprime el seno
print(math.sin(90))
#imprime el coseno
print(math.cos(90))
#imprime la tangente
print(math.tan(90))
#imprime el factorial
print(math.factorial(10))

#imprime un numero al azar
print(random.randint(1, 100))

def entero():
  print('Este es un dato entero: ')
  return 10

entero()