from dados.lista_produtos import produtos
from functools import reduce


# def funcao_de_reducao(acumulador, produto):
#   print(acumulador)
#   print(produto)
#   return acumulador + produto["preco"]


# total = reduce(
#   funcao_de_reducao,
#   produtos,
#   0
# )

total = reduce(
  lambda ac, p: ac + p["preco"],
  produtos,
  0
)

print("Total é:", total)

# total = 0

# for p in produtos:
#   total += p["preco"]

# print(total)

#print(sum([p["preco"] for p in produtos]))

