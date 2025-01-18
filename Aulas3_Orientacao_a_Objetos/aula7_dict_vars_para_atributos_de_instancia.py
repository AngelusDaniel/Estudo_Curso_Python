#__dict__ e vars            __ dunder

class Pessoa:
  ano_atual = 2025  #atributo de classe

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade


  def get_ano_nascimento(self):
    return Pessoa.ano_atual - self.idade
  
dados = {'nome': 'João', 'idade': 21}
p1 = Pessoa(**dados)
print(p1.nome)
# p1.nome = "EITA"
# del p1.nome
# p1.__dict__["outra"] = "coisa"
# p1.__dict__["nome"] = "EITA"
# del p1.__dict_["nome"]
# print(p1.__dict__)
print(vars(p1))


