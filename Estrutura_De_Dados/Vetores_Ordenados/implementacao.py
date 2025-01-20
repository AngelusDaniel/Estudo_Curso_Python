#Pesquisa Linear
#O(n)
import numpy as np


class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultimaposicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  # O(n)
  def imprime(self):
    if self.ultimaposicao == -1:
      print("O vetor está vazio")
    else:
      for i in range(self.ultimaposicao + 1):
        print(f"{i} - {self.valores[i]}" )


  #O(n)
  def inserir(self, value):
    if self.ultimaposicao == self.capacidade -1:
      print("Capacidade máxima atingida.")
      return
    
    posicao = 0
    for i in range(self.ultimaposicao + 1):
     
      if self.valores[i] > value:
        posicao = i
        print(self.valores[i], value)
        break
      elif i == self.ultimaposicao:
        print("a")
        posicao = i + 1

    x = self.ultimaposicao 
    while x >= posicao:
      self.valores[x + 1] = self.valores[x] 
      x -= 1
    self.valores[posicao] = value
    self.ultimaposicao += 1

  #O(n)
  def pesquisa(self, value):

    for i in range(self.ultimaposicao+1):
      if self.valores[i] > value:
        return -1
      if self.valores[i] == value:
        return i
      
  def excluir(self, value):
    retorno = self.pesquisa(value)
    if retorno == -1:
      return -1
    for i in range(retorno, self.ultimaposicao):
      self.valores[i] = self.valores[i + 1]
    self.ultimaposicao -= 1

      


      






vetor = VetorOrdenado(5)

vetor.inserir(6)
vetor.imprime()
print()
vetor.inserir(10)
vetor.imprime()
print()
vetor.inserir(8)
vetor.imprime()
print()
vetor.inserir(1)
vetor.imprime()
print()
vetor.inserir(21)
vetor.imprime()
print()

print(vetor.pesquisa(10))
vetor.excluir(8)
vetor.imprime()
vetor.inserir(4)
vetor.imprime()




