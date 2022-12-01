
x = int(input('Ingrese la cantidad de lapices que desea comprar:  '))

if x >= 1000:
  pag = x *160
elif x < 1000:
  pag = x * 210
else:
  pag = 0
  
print('Tiene que pagar', pag)
