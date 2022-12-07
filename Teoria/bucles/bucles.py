# Ejercicio 1

# Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

numero = int(input('Ingrese un numero: '))
i = 0

while i < 10:
  i += 1
  print(f"{numero} x {i} =", numero*i)
  




# Ejercicio 2

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input('Ingrese su edad: '))
i = 0

while i < edad:
  i += 1
  print('Tienes',i, 'años')