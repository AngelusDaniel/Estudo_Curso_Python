#composição é uma especialidade da gregação, mas quando o objeto "pai" for apagado,
#todas as referencias dos objetos filhos também são apagadas

class Cliente:
  def __init__(self, nome):
    self.nome = nome
    self.enderecos = []

  def inserir_indereco(self, rua, numero):
    self.enderecos.append(Endereco(rua, numero))

  def inserir_indereco_externo(self, endereco):
    self.enderecos.append(endereco)
  
  def listar_enderecos(self):
    for endereco in self.enderecos:
      print(endereco.rua, endereco.numero)

  def __del__(self):
    print("Apagando: ", self.nome)



class Endereco:
  def __init__(self, rua, numero):
    self.rua = rua
    self.numero = numero

  def __del__(self):
    print("Apagando: ", self.rua, self.numero)


cliente = Cliente("Maria")

cliente.inserir_indereco("Rua patati pataspolekseu", 26)
cliente.inserir_indereco("av pataspolekseu", 19)
endereco_externo =  Endereco("Av teste", 3762)
cliente.inserir_indereco_externo(endereco_externo)
cliente.listar_enderecos()

del cliente

print(endereco_externo.rua, endereco_externo.numero)

print("Aqui termina meu codigo")

