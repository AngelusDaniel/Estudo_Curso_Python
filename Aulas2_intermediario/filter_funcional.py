from dados.lista_produtos import produtos


def print_iter(iterator):
  print(*list(iterator), sep="\n")
  print()


novos_produtos = [
  p for p in produtos
  if p["preco"] > 100
]

novos_produtos = filter(
  lambda p: p["preco"] > 90,
  produtos
)

print_iter(produtos)
print_iter(novos_produtos)




