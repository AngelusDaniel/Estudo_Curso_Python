import pprint as p

p = p.pprint
#print(list(range(10)))

lista=[]
for numero in range(10):
  lista.append(numero)
#print(lista)


#lista = [1 for numero in range(10)]

lista = [numero * 2 for numero in range(10)]

print(lista)


#mapeamento de dados em list comprehension
produtos = [
  {"nome": "p1", "preco": 20},
  {"nome": "p2", "preco": 10},
  {"nome": "p3", "preco": 30},
]

novos_produtos = [
 {**produto, "preco": produto["preco"] * 1.05}
 if produto["preco"] > 20 else {**produto}
 for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep="\n")



#filtro de dados em list comprehension

lista = [n for n in range(10) if n < 5]
print(lista)


novos_produtos = [
 {**produto, "preco": produto["preco"] * 1.05}
 if produto["preco"] > 20 else {**produto}
 for produto in produtos
 if produto["preco"] * 1.05 > 10
]

p(novos_produtos)


