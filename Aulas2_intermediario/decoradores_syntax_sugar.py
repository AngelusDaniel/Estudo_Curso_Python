
def criar_funcao(func):
  def intern(*args, **kwargs):

    print("Vou te decorar")

    for arg in args:
      is_string(arg)

    resultado = func(*args, **kwargs)

    print("O seu resultado foi: ", resultado)
    print("Decorado")

    return resultado
  return intern


@criar_funcao
def inverte_string(string):
  print(f"{inverte_string.__name__}")
  return string[::-1]

def is_string(param):
  if not isinstance(param, str):
    raise TypeError("param deve ser uma string")



invertida = inverte_string("123")
print(invertida)



