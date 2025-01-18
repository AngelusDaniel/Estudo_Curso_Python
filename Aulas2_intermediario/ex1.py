

def multi1(*args):

  total = 1
  i = 0
  while i < len(args):
    total = total * args[i]
    i += 1
  return total

def multi2(*args):

  total = 1
  for num in args:
    total *= num

  return total

#total=1 (0 = 2, 1 = 5, 2 = 6)  total = total * num

def parimpar(num):
  if num % 2 == 0:
    return "Par"
  return "impar"



calculo = multi1(2,4,6)

print("Multi-1: ",calculo)

calculo = multi2(2, 3, 6)

print("Multi-2: ", calculo)

print(parimpar(2))

