

pessoa = {

}


chave = "nome"

pessoa[chave] = "Daniel"
pessoa["sobrenome"] = "teste"

print(pessoa)
print(pessoa[chave])

pessoa[chave] = "teste"
del pessoa["sobrenome"]

print(pessoa)

if pessoa.get("sobrenome") is None:
  print("Não existe")

