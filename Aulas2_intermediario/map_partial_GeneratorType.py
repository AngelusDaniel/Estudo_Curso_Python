from dados.lista_produtos import produtos
from functools import partial
from types import GeneratorType

def print_iter(iterator):
  print(*list(iterator), sep="\n")
  print()

def aumentar_porcentagem(valor, porcentagem):
  return round(valor * porcentagem, 2)

def mudar_nome(chave, *args):
  chave = args
  return chave

def altera_chave(product, chave, func, *args):
  return {**product,
           chave: func(product[chave], *args)}

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

# novos_produtos = [
#   altera_chave(p, "nome", mudar_nome, "teste") for p in produtos
# ]

def altera_chave_product(product):
  return {**product,
          "preco": aumentar_dez_porcento(product["preco"])} #{**p, "preco": aumentar_dez_porcento(p["preco"])}

novos_produtos = map(
  altera_chave_product, produtos
)

novos_produtos = list(map(
  altera_chave_product, produtos
)) #para reutilizar

#novos_produtos = (x for x in produtos)

print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
print(hasattr(novos_produtos, "__iter__"))
print(hasattr(novos_produtos, "__next__"))
print(isinstance(novos_produtos, GeneratorType))


print(
    list(map(
      lambda x: x*3,
    [1, 2, 3, 4]
    ))
  )