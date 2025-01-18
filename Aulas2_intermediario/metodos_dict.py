pessoa = {

  "nome": "Daniel",
  "sobrenome": "Angelus",
  #"idade": 21,
  "emails": [
    "daniel@gmail.com",
    "teste@gmail.com"
  ],
  "enderecos": [
    {"Rua" : "teste", "numero": 20},
    {"Rua": "Teste2", "numero": 60},
  ],
  
}


print(len(pessoa))
print(pessoa.keys())
print(pessoa.items(),"\n")

for key, item in pessoa.items():
  print(key, item)

print("\n")

for key in pessoa.keys():
  print(key)

print("\n")

pessoa.setdefault("idade", None)
print(pessoa["idade"])