# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
#Composição - É dono de, Herança - É um


#classe principal (Pessoa)
# -> SUper class, base class, parent class
#classes filhas (Cliente)
# Sub class, child class, derived class


class Pessoa:
  def __init__(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome

  def falar_nome_classe(self):
    print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):

  def falar_nome_classe(self):
    print("Nem saí da classe cliente")
    print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
  ...



c1 = Cliente("Daniel", "Angelus")

print(c1.nome)
c1.falar_nome_classe()

a1 = Aluno("Maria", "Teste")
print(a1.nome)
a1.falar_nome_classe()


