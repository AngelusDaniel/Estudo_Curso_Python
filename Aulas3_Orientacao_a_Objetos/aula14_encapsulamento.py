
#Encapsulamento(modificadores de acesso: publix, protected, private)
#Python não tem modificadores de acesso

#sem underline = public
#um underline = protected #usado na classe e subclasses
#dois underlines = private # só deve ser acessado dentro da classe em que foi declarado.


class Foo:
  def __init__(self):
    self.public = "Isso é publico"
    self._protected = "Isso é um atributo protected"
    self.__private = "Isso é um atributo private"
    self._metodo_protected()

  @property
  def protected(self):
    return self._protected
  
  @protected.setter
  def protected(self, value):
    self._protected = value

  @property
  def private(self):
    return self.__private
  
  @private.setter
  def private(self, value):
    self.__private = value


  def metodo_publico(self):
    self._metodo_protected()
    return "Método publico"

  def _metodo_protected(self):
    print("Metodo protegido")
    return "_Metodo_protected"
  



f = Foo()

f.metodo_publico()