def adiciona_repr(cls):
  def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr  
  cls.__repr__ = meu_repr # a função meu_repr poderia estar fora
  return cls


def meu_planeta(metodo):
  def interno(self, *args, **kwargs):
    resultado = metodo(self, *args, **kwargs)

    if "Terra" in resultado:
      return "Terra. Esse é um planeta dos humanos"
    
    return resultado
  return interno
  

class MyReprMixin:
  def __repr__(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr
  

@adiciona_repr
class Time():
  def __init__(self, nome):
    self.nome = nome


class Planeta(MyReprMixin):
  def __init__(self, nome):
    self.nome = nome

  @meu_planeta
  def falar_nome(self):
    return f"O planeta é {self.nome}"



brasil = Time("Brasil")
portugal = Time("Portugal")


terra = Planeta("Terra")
centauri = Planeta("Proxima Centauri B")


print(brasil)
print(portugal)

print(terra)
print(centauri)

print(terra.falar_nome())
print(centauri.falar_nome())



