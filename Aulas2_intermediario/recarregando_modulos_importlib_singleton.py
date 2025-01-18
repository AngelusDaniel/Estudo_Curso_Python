import importlib


import modularizacao_import  #singleton: O python salva na memoria, mesmo que importe 10 vezes, só será importado uma vez para eficiencia.

print(modularizacao_import.variavel_modulo)


for i in range(10):
  importlib.reload(modularizacao_import)  #recarregando o modulo. Não é comum!
  print(i)

print("fim")