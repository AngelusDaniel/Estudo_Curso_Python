import sys   #para usar o getsizeof

iterable = ["Eu", "tenho", "__iter__"]

iterator = iter(iterable)#tem __iter__ e __next_

#generator é também um iterator, mas iterator não é generator


lista = [n for n in range(1000000)] #fica na memória
generator = (n for n in range(1000000)) #não fica na memória, mostra 1 por vez
print(sys.getsizeof(lista))

print(sys.getsizeof(generator)) #mostra o tamanho em bytes

for num in generator:
  print(num)