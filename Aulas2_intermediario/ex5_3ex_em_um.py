import copy
from dados.lista_produtos import produtos

print(*produtos,  sep="\n", end="\n\n")

novos_produtos = copy.deepcopy(produtos)

#novos_produtos = [
#   {**item, "preco": round(item["preco"]*1.1, 2)} 
#   for item in copy.deepcopy(produtos)
#]

for item in novos_produtos:
  item["preco"] *= 1.10   
  item["preco"] = round(item["preco"], 3)



print(*novos_produtos, sep="\n",  end="\n\n")


produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

produtos_ordenados_por_nome.sort(key=lambda item: item["nome"], reverse= True)

print(*produtos_ordenados_por_nome, sep="\n",  end="\n\n")

produtos_ordenados_por_preco = copy.deepcopy(
    novos_produtos
  )

produtos_ordenados_por_preco.sort(key=lambda item: item["preco"])


print(*produtos_ordenados_por_preco, sep="\n",  end="\n\n")


