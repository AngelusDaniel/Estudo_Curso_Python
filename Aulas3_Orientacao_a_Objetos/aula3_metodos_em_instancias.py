#instancia e objeto se referem geralmenta a mesma coisa
#Uma classe pode gerar varias instâncias
#Na classe o self é a própria instância

class Carro: 
  def __init__(self, nome):
    self.nome = nome

  def acelerar(self):
    print(f"O {self.nome} está acelerando...")

  


fusca = Carro("Fusca")

print(fusca.nome)
fusca.acelerar()

Type_R = Carro("Type_R")

print(Type_R.nome)

Type_R.acelerar()