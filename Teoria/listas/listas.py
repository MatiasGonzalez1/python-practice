"""Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]



Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos"""


"""usuario = []

print(usuario)

continuar = int(input('Ingrese 1 para ingresar un dato 0 para salir: '))
while continuar == 1:  
  ingreso = input('Ingrese su dato: ')
  usuario.append(ingreso)
  print(usuario)
  continuar = int(input('Ingrese 1 para ingresar un dato 0 para salir: '))"""
  
  
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros[4] *= 2

numeros[7] *=2

numeros[9]*=2


print(numeros)