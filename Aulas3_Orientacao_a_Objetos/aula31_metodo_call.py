# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".



class CallMe:
  def __init__(self, phone):
    self.phone = phone

  def __call__(self, nome, *args, **kwargs):
   print(f"Chamando {self.phone} de {nome}")
   return 1234



call1 = CallMe("2345654345678")

retorno = call1("Daniel")
print(retorno)