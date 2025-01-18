

pessoa = {

  "nome": "Daniel",
  "sobrenome": "Angelus",
  "idade": 21,
  "emails": [
    "daniel@gmail.com",
    "teste@gmail.com"
  ],
  "enderecos": [
    {"Rua" : "teste", "numero": 20},
    {"Rua": "Teste2", "numero": 60},
  ],
  
}


print(pessoa["enderecos"][1]["Rua"])

for chave in pessoa:
  print(chave, pessoa[chave])

#pessoa = dict(nome="Daniel", sobrenome="Angelus")