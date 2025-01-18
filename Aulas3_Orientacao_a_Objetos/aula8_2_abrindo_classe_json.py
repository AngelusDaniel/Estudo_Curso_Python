import json
from aula8_salvando_classe_json import caminho_arquivo, Pessoa, fazer_dump

fazer_dump()

with open(caminho_arquivo, "r") as arquivo:
  dados = json.load(arquivo)
  print(dados)

  p1 = Pessoa(**dados[0])
  p2 = Pessoa(**dados[1])
  p3 = Pessoa(**dados[2])

  print(p1.nome)
  print(p2.nome)
  print(p3.nome)

  print(__name__)
