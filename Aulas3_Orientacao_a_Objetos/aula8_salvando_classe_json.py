import json

caminho_arquivo = "classesalva.json"


class Pessoa:
  def __init__(self, nome, sobrenome, idade):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade

  def cantar(self):
    print(f"{self.nome} está cantando")



pessoa1 = Pessoa("Daniel", "Angelus", "22")
pessoa2 = Pessoa("Maria", "teste", "21")
pessoa3 = Pessoa("Harry", "Angelus", "22")
bd = [vars(pessoa1), pessoa2.__dict__, vars(pessoa3)]

def fazer_dump():
  with open(caminho_arquivo, "w") as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == "__main__":
  fazer_dump()