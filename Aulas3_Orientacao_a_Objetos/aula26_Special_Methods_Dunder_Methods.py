#Special Methos, Magic Methods ou Dunder Methods

#__repr__     => mais para desenvolvedor, comunicação

class Ponto:
  def __init__(self, x, y, z="string"):
    self.x = x
    self.y = y
    self.z = z

  # def __str__(self):
  #   return f"{self.x}, {self.y}"

  def __add__(self, other):
    novo_x = self.x + other.x
    novo_y = self.y + other.y
    return Ponto(novo_x, novo_y)
  
  def __gt__(self, other):
    ponto_self = self.x + self.y
    ponto_other = other.x + other.y
    return ponto_self > ponto_other


  def __repr__(self):
    # class_name = self.__class__.__name__
    class_name = type(self).__name__
    return f"{class_name}(x={self.x}, y={self.y}, z={self.z!r})"



p1 = Ponto(1, 2)
p2 = Ponto(6, 4)

# p3 = p1 + p2    #__add__
# print(p3)

p4 = p2 > p1 
print(p4)
# print(p1)
# print(p2)
# print(repr(p1))
# print(repr(p2))
# print(f"{p2!r}")