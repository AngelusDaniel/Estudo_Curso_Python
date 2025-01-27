"""Este é um módulo de exemplo
"""

variavel_1 = 1

def soma(x:int | float, y:int | float) -> int | float:
  """
  soma x e y

  descrição longa blablablablalcasodkosadkaspodkpoads
  aisjdisajdioasdjidjasidjasdisadsdasdiaidjsaidas

  :param x: numero 1
  :type x: int or float
  :param y: numero 2
  :type y: int or floar
  :return: A soma entre x e y
  :rtype: int or float
  """

  return x + y



def multiplica(
    x: int | float,
    y: int | float,
    z: int | float | None = None,
)-> int | float :
  
  """Multiplica x, y e/ou z

  Multiplica x e y. Se z for enviador, multiplica x, y e z.
  """

  if z is None:
    return x * y
  return x * y * z


variavel_2 = 2

variavel_3 = 3

