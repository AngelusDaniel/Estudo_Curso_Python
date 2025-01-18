from sys import path

from modulo_package.modulo import soma_modulo
from modulo_package.modulo import *  #má pratica
from modulo_package import modulo
import modulo_package.modulo

print(path, __name__)

print(soma_modulo(2, 1))
print(modulo.soma_modulo(1, 5))
print(modulo_package.modulo.soma_modulo(1, 5))
