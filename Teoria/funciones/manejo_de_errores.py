while True:
  try:
    edad = int(input('Ingrese su edad: '))
    print('Tu edad es ', edad)
    break
  except:
    print('Debes ingresar tu edad con numeros')
    break
  finally:
    print('Gracias por utilizar nuestro servicio')