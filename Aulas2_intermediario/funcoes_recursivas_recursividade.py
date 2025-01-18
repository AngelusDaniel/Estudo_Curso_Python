

# def recursiva(inicio=0,  fim=10):

#   print(inicio, fim)
#   #caso base

#   if inicio >= fim:
#     return fim
  

#   #caso recursivo: contar até chegar ao final
#   inicio +=1
#   return recursiva(inicio, fim)


# print(recursiva(0, 1000))


def factorial(n):
  if n <= 1:
    return 1
  
  return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(100))


def factorial_for(n):
  if n <= 1:
    return 1
  i = n
  while n >1:
    i *= n - 1
    n -= 1
    print(n)
  return i

print(factorial_for(3))

  

