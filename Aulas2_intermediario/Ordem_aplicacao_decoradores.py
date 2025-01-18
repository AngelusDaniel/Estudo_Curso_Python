

def param_decorador(nome):
  def decorador(func):
    print("Decorador: ", nome)
    def intern(*args, **kwargs):
      res = func(*args, **kwargs)
      final = f"{res} {nome}"
      return final
    return intern
  return decorador

@param_decorador(nome="Terceiro")
@param_decorador(nome="Segundo")
@param_decorador(nome="Primeiro")
def soma(x, y):
  return x+y

dez_mais_cinco = soma(3, 2)
print(dez_mais_cinco)