#pra saber se o objeto é de determinado tipo 


lista = [
  "a", 1, 1.1, True, [0, 1, 2], (1,2), {0,1}, {"nome": "Daniel"}
]



# for item in lista: 
#   print(item, isinstance(item, set))

for item in lista:
  if isinstance(item, set):
    print("SET")
    item.add(5)
    print(item, isinstance(item, set))

  if isinstance(item, str):
    print("STR")
    print(item.upper(), isinstance(item, set))

  
  if isinstance(item, (int, float)):
    print("NUM")
    print(item, item * 2)