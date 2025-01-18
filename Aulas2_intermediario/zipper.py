
from itertools import zip_longest

lista1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
lista2 =["BA", "SP", "MG", "RJ"]

print(list(zip(lista1,lista2)))
print(list(zip_longest(lista1,lista2, fillvalue="SEM CIDAD")))