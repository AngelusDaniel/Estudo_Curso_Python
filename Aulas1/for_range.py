
numeros = range(0,10, 2)


for valor in numeros:
  print(valor)


for i in range(10):
  print("teste")

  if i == 5:
    print("O else não executará")
    break

  for j in range(1,3):
    print(i, j)

else: 

  print("for completo com sucesso");
