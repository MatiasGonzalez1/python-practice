import math

#se usa ciclo while para calcular una raiz cuadrada y validar los intentos

print('Calculo de una raiz cuadrada')

numero= int(input('Ingrese un numero: '))

intentos=0

while numero<=0:
  print('No se puede hallar la raiz de un numero negativo')
  
  if intentos==2:
    print('Te quedaste sin intentos, prueba nuevamente mas tarde')
    break   
  else:
    numero= int(input('Ingrese un numero'))

  if numero<0:
    intentos+=1
    
if intentos<2:
  solucion=math.sqrt(numero)
  print('La raiz cuadrada de ' +str(numero)+ ' es ' + str(solucion)) 