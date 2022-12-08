# Ejercicio 1

# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1,11):
  print(i)

numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numeero: '))

for i in range(numero1, numero2 + 1):
  print(i)
  
# Ejercicio 2

# Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numeero: '))

for i in range(numero1, numero2 +1):
  if i % 2 == 0:
    continue
  print(i)