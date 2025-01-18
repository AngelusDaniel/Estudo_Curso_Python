
#combinação - Ordem não importa - iteravel + tamanho do grupo
#permutação - Ordem importa
#produto - ordem importa e repete valores unicos

from itertools import combinations, permutations, product

def print_iter(iterator):
  print(*list(iterator), sep="\n")
  print()

pessoas =[
  "joão", "Joana", "Daniel", "Letícia"
]

camisetas = [
  ["preta", "branca"],
  ["p", "m", "g"],
  ["masculino", "feminino", "unisex"],
  ["algodão", "poliester"]
]


print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))