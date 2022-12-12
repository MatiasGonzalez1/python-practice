class A():
  def __init__(self):
    self._contador = 0
    self._cuenta = 0
  
  #decorador para que el metodo sea llamado como un atributo
  #metodo get
  @property
  def cuenta(self):
    return self._cuenta
  
  #metodo get
  @property
  def contador(self):
    return self._contador
  # def incrementar(self):
  #   self._contador += 1
a = A()
print(a.cuenta, a.contador)
    