class Pessoa:
  
  def __init__(self, nome, sobrenome):  #todo metodo que for tratar das instancias geradas precisa receber no primeiro parâmetro self
    self.nome = nome
    self.sobrenome = sobrenome


p1 = Pessoa("Daniel", "Angelus")  #gerando nova instancia da classe Pessoa / criando um novo objeto e inserindo na variavel p1
# p1.nome = "Daniel"
# p1.sobrenome = "Angelus"

p2 = Pessoa("Maria", "Joana")  #gerando nova instancia da classe Pessoa
# p2.nome = "Teste"
# p2.sobrenome = "teste"

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
