
lista1 = [1, 2, 1, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4, 5]

def construct_func(func):
  def intern(*args, **kwargs):
    is_array_values_int(*args)
    res = func(*args, **kwargs)
    return res
  return intern



def is_array_values_int(*args):
  for arrays in args:
    for item in arrays:
      i = 0
      if not isinstance(item, int):
        i += 1
        raise TypeError("O tipo dos valores não são inteiros") 


@construct_func
def soma_listas(lista1, lista2):
  interval = min(len(lista1), len(lista2))

  return [
    lista1[i] + lista2[i] for i in range(interval)
  ]


#func para qualquer linguagem:
lista_soma = []
def somando_listas(lista1, lista2):
  for i in range(len(lista2)):
    lista_soma.append(lista1[i] + lista2[i])
  return lista_soma


#modo mais "pythonico"
lista_soma2 = []
def somando_listas2(lista1, lista2):
  for i, _ in enumerate(lista2):
    lista_soma.append(lista1[i] + lista2[i])
  return lista_soma2

#outro modo "pythonico"
def somando_lista3(lista1, lista2):
  lista_soma = [x + y for x, y, in zip(lista1, lista2) ]
    

soma_lista1_lista2 = soma_listas(lista1, lista2)

print(soma_lista1_lista2)