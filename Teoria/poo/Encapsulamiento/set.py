class A():
  def __init__(self):
    self._contador = 0
    self._cuenta = 0
  
  #decorador para que el metodo sea llamado como un atributo
  #metodo get
  @property
  def cuenta(self):
    return self._cuenta

  #metodo set
  @cuenta.setter
  def cuenta(self, cuenta):
    #nombre del atributo = nuevo valor
    self._cuenta = cuenta    
  
  #metodo get
  @property
  def contador(self):
    return self._contador
  
  @contador.setter
  def contador(self, contador):
    self._contador = contador
  # def incrementar(self):
  #   self._contador += 1
  
  
  
  
a = A()
print(a.cuenta, a.contador)
a.cuenta = 20
print(a.cuenta)
    