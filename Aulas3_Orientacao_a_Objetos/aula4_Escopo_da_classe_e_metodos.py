

class Animal:
  

  def __init__(self, nome):
    self.nome = nome

    variavel = "Valor"
    print(variavel)


  def comendo(self, alimento):
    print(f"{self.nome} comendo {alimento}")

  def andando_local(self, local):
    print(f"{self.nome} está andando pela(o) {local}")


leao = Animal(nome="Leão")

print(leao.nome)

leao.comendo("Pizza")

leao.andando_local("Praia")