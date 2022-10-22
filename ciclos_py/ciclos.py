'''
#validacion de datos de entrada con for


email = False

miMail = input('Ingrese su direccion de email')

for i in miMail:
  if i == '@':
    email += 1 
  
if email==1:
  print('El correo electronico ingresado es correcto')
  
else:
    print('El correo electronico ingresado no es correcto')


for i in range(5):
  print('Esta es la vuelta: ' + str(i))

range = 'el primer parametro es la cantidad de veces que se resuelve o en el caso que tenga un segundo parametro desde donde inicia, el segundo es hasta dónde y el tercero de cuanto en cuanto  ejemplo range(5,10,2)'
'''
#validacion de datos de entrada con range

valido=False

email1=input('Ingrese un email: ')
for i in range(len(email1)):
  if email1[i] == '@':
    valido=True
if valido:
  print('El correo electronico es valido')
else:
  print('El correo no es valido')