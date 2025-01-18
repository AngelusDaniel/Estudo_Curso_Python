
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


def inverte_string(string):
  return string[::-1]

def is_string(param):
  if not isinstance(param, str):
    raise TypeError("param deve ser uma string")

inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida = inverte_string_checando_parametro("123")
print(invertida)



