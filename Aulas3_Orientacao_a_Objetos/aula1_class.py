
#por convenção se usa PascalCase para nome de classes



# string = "Daniel"
# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
  ...


p1 = Pessoa()  #gerando nova instancia da classe Pessoa / criando um novo objeto e inserindo na variavel p1
p1.nome = "Daniel"
p1.sobrenome = "Angelus"

p2 = Pessoa()  #gerando nova instancia da classe Pessoa
p2.nome = "Teste"
p2.sobrenome = "teste"

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

