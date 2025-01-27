

class MeuError(Exception):
  pass


class OutroError(Exception):
  pass






def levantar():

  exception_ = MeuError("a", "b", "c")
  exception_.add_note("Olha a nota 1, comunicando")
  exception_.add_note("Você errou isso")
  raise exception_

try:  
  levantar()

except (MeuError, ZeroDivisionError )as error:
  print(error.__class__.__name__)
  print(error.args)
  exception_ = OutroError("Lançando de novo")
  #exception_.__notes__ += error.__notes__.copy()
  exception_.add_note("Outra nota")
  raise exception_ from error

