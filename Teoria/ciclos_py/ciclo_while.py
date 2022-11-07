'''i=0
while i<=10:
  print('Ejecucion N°: ' + str(i))
  i+=1
  
print('Finish')'''

#validando edad

intentos=3
edad = int(input('Introduce tu edad: '))

while edad<10 or edad>110:
  intentos-=1
  print(f'Te quedan {intentos} intentos')
  if intentos == 0:
    break
  print('Introduce una edad correcta. Vuelve a intentar')
  edad = int(input('Introduce tu edad: '))
  
if intentos > 0:
  print('Gracias por colaborar, puedes pasar')
  print('Edad del aspirante ' + str(edad) + ' años')
else:
      print('Prueba nuevamente más tarde')

  

