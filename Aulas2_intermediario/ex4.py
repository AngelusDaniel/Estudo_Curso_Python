

lista_de_lista_inteiros = [
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,3,2,1,1,5,6],
  [2,5,4,7,8,3,2,9,9]
]


def encontra_primeiro_duplicado(lista_de_inteiros):

  numeros_checados = set()
  primeiro_duplicado = -1

  for numero in lista_de_inteiros:
    if numero in numeros_checados:
      primeiro_duplicado = numero
      break


    numeros_checados.add(numero)


  return primeiro_duplicado

for lista in lista_de_lista_inteiros:
  print( 
    lista, 
    encontra_primeiro_duplicado(lista)
  )