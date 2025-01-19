# super( é a super classe na sub classe)


# class MinhaString(str):
#   def upper(self):
#     print("CHAMOU UPPER")
#     retorno = super(MinhaString, self).upper()
#     print("Depois do upper")
#     return retorno


# string = MinhaString("Daniel")


# print(string.upper())


class A:
  atributo_a = "valora"

  def __init__(self, atributo):
    self.atributo = atributo

  def metodo(self):
    print("a")


class B(A):
  atributo_b = "valorb"

  def __init__(self, atributo):
    super().__init__(atributo) #para passar o valor para o init A

  def metodo(self):
    print("B")


class C(B):
  atributo_c = "valorc"

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    print("Burlei o sistema")

  def metodo(self):
    super(B, self).metodo()
    super().metodo()
    print("C")



# b = B()
# print(b.atributo_a, b.atributo_b)

c = C("Teste");
print(c.atributo_a, c.atributo_b, c.atributo_c)

c.metodo()

print(C.mro())

print(c.atributo)