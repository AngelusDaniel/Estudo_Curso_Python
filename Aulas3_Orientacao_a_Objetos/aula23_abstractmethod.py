

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
  def __init__(self, name):
    self._name = None
    self.name = name


  @property
  def name(self):
    return self._name
  
  @name.setter
  @abstractmethod
  def name(self, value): ...
    
  


class Foo(AbstractFoo):
  

  def __init__(self, name):
    super().__init__(name)
    # print("blablalba")

  # @property
  # def name(self):
  #   return self._name

  @AbstractFoo.name.setter
  def name(self, value):
    self._name = value

foo = Foo("Bar")

print(foo.name)