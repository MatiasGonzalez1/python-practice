# Ejercicio 1

# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas


lista = []

def agregar():
  i = 1
  while i == 1:
    numero = int(input('Ingrese un numero: '))
    lista.append(numero)
    i= int(input('¿Desea seguir ingresando? 1- Si   2- No \n'))


def ordenar():
  lista.sort()
  par = []
  impar = []
  for i in lista:
     if i % 2 == 0:
      par.append(i)
     else:
      impar.append(i)
  print(par,impar)
  
agregar()
print(lista)
ordenar()

  # Ejercicio 2

# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial():
  numero = int(input('Ingresa un numero entero y positivo: '))
  if numero > 0:
    factorial = 1
    for i in range(1, numero +1):
      factorial *= i  
    print(f"El factorial de {numero} es:", factorial)
  else:
    print('El numero es negativo y no podemos proceder')

factorial()