#Metodos de classe + Factories
#São metodos onde "self" será "cls" ou seja,
#ao invés de receber a instancia no primeiro parâmetro,
#receberemos a pŕopria classe


class Pessoa:

  ano = 2025

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade=idade

  @classmethod
  def metodo_de_classe(cls): #tem que passar a propria classe/ serve para chamar o método sem precisar instanciar
    print("Hey")

  @classmethod
  def criar_com_30_anos(cls, nome): 
    return cls(nome, 30) 

  @classmethod
  def criar_sem_nome(cls, idade): 
    return cls("Anônima", idade) 


print(Pessoa.ano)
p1 = Pessoa("Daniel", 22)
p2 = Pessoa.criar_com_30_anos("Maria")
p3 = Pessoa.criar_sem_nome(21)
print(p3.nome, p3.idade)
print(p2.nome, p2.idade)
p1.metodo_de_classe()
print(Pessoa.ano)
Pessoa.metodo_de_classe()

