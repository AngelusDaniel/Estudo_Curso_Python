

class Animal:
  

  def __init__(self, nome):
    self.nome = nome

    variavel = "Valor"
    print(variavel)


  def comendo(self, alimento):
    print(f"{self.nome} comendo {alimento}")


leao = Animal(nome="Leão")

print(leao.nome)

leao.comendo("Pizza")