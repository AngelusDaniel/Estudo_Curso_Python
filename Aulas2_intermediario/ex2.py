

def criarfuncmulti(multiplicador):
  def multi(num):
    return num * multiplicador
  return multi


duplicar = criarfuncmulti(2)

triplicar = criarfuncmulti(3)

print(duplicar(5))

print(triplicar(9))




numero1 = input("Insira um numero: ")
multinum = input("Quantas vezes que multiplicar o numero: ")

def dobrarnumero(num, multi):
  return int(num) * int(multi)

result = dobrarnumero(numero1, multinum)

print(result)
