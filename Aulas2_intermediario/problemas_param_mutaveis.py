

# def adiciona_clientes(nome, lista=[]):   #evitar usar valor padrão em mutaveis
#   lista.append(nome)
#   return lista


# cliente1 = adiciona_clientes("daniel")
# adiciona_clientes("Joana", cliente1)
# print(cliente1)


# cliente2 = adiciona_clientes("Helen")
# adiciona_clientes("Maria", cliente2)
# print(cliente2)



def adiciona_clientes(nome, lista=None):  #resolução
  if lista is None:
       lista = []
  lista.append(nome)
  return lista



cliente1 = adiciona_clientes("daniel")
adiciona_clientes("Joana", cliente1)
adiciona_clientes("Fernando", cliente1)
cliente1.append("Edu")
print(cliente1)


cliente2 = adiciona_clientes("Helen")
adiciona_clientes("Maria", cliente2)
print(cliente2)