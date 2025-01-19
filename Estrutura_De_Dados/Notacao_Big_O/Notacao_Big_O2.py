

def lista():
  lista = []
  for i in range(1000):
    lista += [i]
  return lista 

print(lista())


def lista1():
  lista = []
  for i in range(1000):
    lista.append(i)
  return lista 

print(lista1())


def lista2():
  return range(1000)

lista2 = lista2()

for i in lista2:
  print(i)