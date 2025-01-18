lista = [1, 4,33, 6,34,677,43,23]

#modifica lista original
lista.sort(reverse=True)

#sorted(lista) copia rasa


print(lista)


lista_nomes = [
  {"nome": "Daniel", "sobrenome": "Angelus"},
  {"nome": "Carlos", "sobrenome": "Almeida"},
  {"nome": "Lucas", "sobrenome": "Visconde"},
  {"nome": "Lara", "sobrenome": "Paiva"},
]



# def ordena(item):
#   return item["nome"]

# lista_nomes.sort(key=ordena)
#lista_nomes.sort(key=lambda item: item["nome"])  #funcao lambda

def exibir(lista):
  for item in lista:
    print(item)
  print("\n")


l1 = sorted(lista_nomes,key=lambda item: item["nome"], reverse=True)  #funcao lambda com copia rasa da lista com reverse
l2 = sorted(lista_nomes,key=lambda item: item["nome"])  #funcao lambda com copia rasa da lista


for item in lista_nomes:
  print(item, )

print("\n")

exibir(l1)
exibir(l2)

