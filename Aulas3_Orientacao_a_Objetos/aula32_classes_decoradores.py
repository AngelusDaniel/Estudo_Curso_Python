

class Multiplicar:
  def __init__(self, args):
    print("INIT", args)

@Multiplicar
def soma(x,y):
  return x * y


dois_mais_dois = soma(2, 3)

print(dois_mais_dois)