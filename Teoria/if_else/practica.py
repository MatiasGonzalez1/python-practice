# letra = input('Ingrese una letra: ')
# if letra.lower() in 'aeiou':
#   print('Es vocal')
# else:'No es una vocal'
  
  
# numero = int(input('Ingrese un numero'))

# if numero > 0:
#   print('El numero es {} y su numero absoluto es {}'.format(numero, numero))
# else:
#   print('El valor absoluto de {} es:'.format(numero), abs(numero))

# palabra1 = input('Ingrese la primer palabra: ')
# palabra2 = input('Ingrese la segunda palabra: ')

# if len(palabra1) < 3 or len(palabra2) < 3:
#   print('Para rimar deben tener al menos 3 carácteres')
# elif palabra1[-3:] == palabra2[-3:]:
#   print('Estás rimando')
# elif palabra1[-2:] == palabra2[-2:]:
#   print('Las palabras riman un poco')
# else: print('Las palabras no riman')


A = 'Usted escogió el Partido Rojo'
B = 'Usted escogió el Partido Verde'
C = 'Usted escogió el Partido Azul'

opcion = input('Ingresa la opcion (ABC): ')

if opcion.upper() == 'A':
  print(A)
elif opcion.upper() == 'B':
  print(B)
elif opcion.upper() == 'C':
  print(C)
else: print('Usted ingresó un candidato no válido')
