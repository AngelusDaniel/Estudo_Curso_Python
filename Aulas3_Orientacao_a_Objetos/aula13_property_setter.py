# @property + @setter um setter no modo Pythonico


# @property - propriedade do objeto -  um método que se comporta como atributo

#atributos que começam com _ ou __ não devem ser usados fora da classe





class Caneta:
  def __init__(self, cor):
    #private protected
    self._cor = cor
    self._cor_tampa = None


  # def get_cor(self):
  #   return self.cor_tinta

  @property
  def cor(self):
    return self._cor
  
  @cor.setter
  def cor(self, valor):
    valor = valor.capitalize()
    if valor == "Rosa":
      raise ValueError("Não permitido mudar para cor Rosa")
    self._cor = valor

  @property
  def cor_tampa(self):
    return self._cor_tampa
  
  @cor_tampa.setter
  def cor_tampa(self, value):
    self._cor_tampa = value

  
def mostrar(caneta):
  return caneta.cor

caneta1 = Caneta("Azul")
# print(caneta.get_cor())
print(caneta1.cor)

caneta1.cor = "Pink"

print(caneta1.cor_tampa)

caneta1.cor_tampa = "Azul"
print(caneta1.cor_tampa)





