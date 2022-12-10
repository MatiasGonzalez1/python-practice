# Ejercicio 1

# Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0

# def valor():
#  a=int(input('Ingrese el primer valor: '))
#  b=int(input('Ingrese el segundo valor: '))
#  if a > b:
#    return 1
#  elif a == b:
#    return 0
#  else:
#    return -1

# valor()

# Ejercicio 2

# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def cantidad():
  monto = float(input('Ingrese el monto: '))
  
  iva = int(input('Ingrese el valor del iva: '))
  
  if iva != 0:
    if iva > 0:
      totalPagar = ((monto * iva) / 100) + monto
      return totalPagar
    else:
      return 'El monto de iva es negativo'
  else:
    totalPagar = (monto * 0.21) + monto
    return totalPagar
  
print('El total de su monto es: ',cantidad())
