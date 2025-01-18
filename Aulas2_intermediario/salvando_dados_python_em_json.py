import json

pessoa = {
  "nome": "Daniel Angelus",
  "sobrenome": "Alves",
  "enderecos": [
    {"rua:": "R1", "numero": 60},
    {"rua:": "R2", "numero": 61},
  ],
  "altura": 1.70,
  "numeros_preferidos": (2, 4, 6, 8, 10),
  "dev": True,
  "nada": None

}

# with open("arquivojson.json", "w") as arquivo:  #salvando
#   json.dump(pessoa, arquivo, indent=2)

with open("arquivojson.json", "r") as arquivo:  #lendo
  pessoa = json.load(arquivo)
  print(pessoa)
  print(pessoa["nome"])