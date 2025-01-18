
lista1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
lista2 =["BA", "SP", "MG", "RJ"]




def factory_func(func):
  def intern(*args, **kwargs):
    res = func(*args, **kwargs)
    return res
  return intern


# @factory_func
# def zipper(lista1, lista2):
#   lista_nova = []
#   i = 0
#   for item in lista1:
#     lista_nova.append((item, lista2[i]))
#     i += 1
#   return lista_nova

@factory_func
def zipper(lista1, lista2):
  intervalo_maximo = min(len(lista1), len(lista2))
  return [
    (lista1[i], lista2[i]) for i in range (intervalo_maximo)
  ]


zipper_lista1_lista2 = zipper(lista1, lista2)

print(zipper_lista1_lista2)

