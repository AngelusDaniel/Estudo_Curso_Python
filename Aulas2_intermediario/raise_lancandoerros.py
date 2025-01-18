

# def divide(n, d):
#   try:
#     return n / d
#   except ZeroDivisionError:
#     print("___")
#     raise

def nao_aceito_zero(d):
  if d == 0:
    raise ZeroDivisionError("Você está tentando dividir por zero") #redundante
  return True

def dever_ser_int_ou_float(n):

  tipo_n = type(n)

  if not isinstance(n, (float, int)):
    raise TypeError(
      f"{n} deve ser int ou float."
      f"{tipo_n.__name__} enviado"
    )


def divide(n, d):

  dever_ser_int_ou_float(n)
  dever_ser_int_ou_float(d)

  nao_aceito_zero(d)
  return n/d


print(divide("3", 1))