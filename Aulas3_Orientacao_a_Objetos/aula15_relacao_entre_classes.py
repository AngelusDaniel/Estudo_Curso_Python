#associação, agregação, composição


class Escritor:
  def __init__(self, nome) -> None:
    self.nome = nome
    self._ferramenta = None

  @property
  def ferramenta(self):
    return self._ferramenta
  
  @ferramenta.setter
  def ferramenta(self, value):
    self._ferramenta = value


class FerramentaDeEscrever:
  def __init__(self, nome):
    self.nome = nome


  def escrever(self):
    return f"{self.nome} está escrevendo"
  

escritor = Escritor("Daniel")
caneta = FerramentaDeEscrever("Caneta Bic")
maquina = FerramentaDeEscrever("Maquina de Escrever")

escritor.ferramenta = maquina

print(caneta.escrever())
print(maquina.escrever())
print(escritor.ferramenta.escrever())

