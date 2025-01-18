# @property - um getter no modo Pythonico
#getter - um metodo para obter um atributo

# @property - propriedade do objeto -  um método que se comporta como atributo



class Caneta:
  def __init__(self, cor, cor_tampa):
    #private protected public
    self.cor_tinta = cor
    self.cor_tampa = cor_tampa


  # def get_cor(self):
  #   return self.cor_tinta

  @property
  def cor(self):
    return self.cor_tinta

  @property
  def cor_tampa(self):
    return self.cor_tampa
  

caneta = Caneta("Azul")
# print(caneta.get_cor())
print(caneta.cor)



