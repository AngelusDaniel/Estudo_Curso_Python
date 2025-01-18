#decoradores com parâmetros 

def fabrica_de_decoradores(a=None, b=None, c=None):

  def fabric_functions(func):

    print("Decoradora 1")


    def aninhada(*args, **kwargs):  #inner function, nested function
      print("parâmetros do decorador ", a, b, c)
      print("Aninhada")
      res = func(*args, **kwargs)
      return res
    return aninhada
  return fabric_functions


#@fabric_functions
@fabrica_de_decoradores(1,2,3)
def soma(x, y):
  return x + y

dez_mais_cinco = soma(5, 5)
print(dez_mais_cinco)

decoradora = fabrica_de_decoradores()

#multiplica = fabric_functions(lambda x, y: x * y)
multiplica = decoradora(lambda x, y: x * y)

dez_vezes_cinco = multiplica(10, 5)
print(dez_vezes_cinco)




