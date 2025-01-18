

lista = ["daniel", "teste", "um"]

lista.append("dois")

lista_enumerada = enumerate(lista)

print(next(lista_enumerada))


# for itens in lista_enumerada:

#   print(itens)

# for itens1 in lista_enumerada:

#   print(itens1)

for item in enumerate(lista):
  indice, nome = item
  print(indice, nome)

for indice1, nome1 in enumerate(lista):
  print(indice1, nome1)
  

lista_enumerada = list(enumerate(lista))

print(lista_enumerada[2][1])

lista_enumerada1 = list(enumerate(lista, start= 19))

print(lista_enumerada1)


listateste= ["danielteste", "testeteste", "umteste"]

lista_enum1 = enumerate(listateste);

for i, item in lista_enum1:

  print(i+1, item);







