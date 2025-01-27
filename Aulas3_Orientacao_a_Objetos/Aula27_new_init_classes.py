#__new__ Deve retornar o novo objeto!
#__new__ responsável por criar e retornar o novo object. Por isso recebe cls
#__init__ Deve retornar None

class A:

  def __new__(cls, x):
    # print("Antes de criar a instância")
    instancia =  super().__new__(cls)
    # print("depois")
    # instancia.x = 123
    return instancia


  def __init__(self, x):
    self.x = x
    print("Sou o init")

  def __repr__(self):
    return "A()"
  

a = A(123)
print(a.x)

# a = object.__new__(A)
# a.__init__()