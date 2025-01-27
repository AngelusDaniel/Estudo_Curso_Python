
def meu_repr(self):
  return f"{type(self).__name__}({self.__dict__})"



class Meta(type):
  def __new__(mcs, name, bases, dct):
    print("META CLASS New")
    cls = super().__new__(mcs, name, bases, dct)
    cls.attr = 1234
    cls.__repr__ = meu_repr

    print(cls.__dict__)

    if "falar" not in cls.__dict__ or \
      not callable(cls.__dict__['falar']):
      raise NotImplementedError("Implemente Falar")

    return cls
  

  def __call__(self, *args, **kwargs):
    instancia = super().__call__(*args, **kwargs)
    if "nome" not in instancia.__dict__ :
      raise NotImplementedError("Crie o atributo nome")
    print("call", instancia.__dict__)
    return instancia
  


class Pessoa(metaclass=Meta):

  def __new__(cls, *args, **kwargs):
    print("Meu New")
    instancia = super().__new__(cls)
    return instancia
  

  def __init__(self, nome):
    print("MEU INIT")
    self.nome = nome


  def falar(self):
    print("Falando")




p1 = Pessoa("Daniel")
print(p1)
p1.falar()
print(p1.attr)
print(Pessoa.attr)

