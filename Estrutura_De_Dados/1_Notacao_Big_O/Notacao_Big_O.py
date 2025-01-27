#comparação de algoritmos
#compara complexidade, e o quanto as operações aumentam de acordo com as entradas


import timeit

def soma(x):
  soma = 0
  for i in range(x+1):
    print(i)
    soma += i

  return soma



print(soma(5))


def soma2(n):
  total = 0
  for n in range(n+1):

    total += n
    n -= 1
  return total

print(soma2(5))


def soma3(n):
  return (n*(n+1))/ 2

print(soma3(5))

