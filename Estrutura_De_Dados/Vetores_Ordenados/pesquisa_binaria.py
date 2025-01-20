#Pesquisa Linear
#O(n)
import numpy as np
import timeit

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
        break
      elif i == self.ultimaposicao:
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
      
  #O(Log n)
  def pesquisa_binaria(self, value):
    limite_inferior = 0
    limite_superior = self.ultimaposicao

    while True:
      posicao_atual = int((limite_inferior + limite_superior)/2)
      if self.valores[posicao_atual] == value:
        return posicao_atual
      elif limite_inferior > limite_superior:
        return -1
      else:
        if self.valores[posicao_atual] < value:
          limite_inferior = posicao_atual + 1
        else:
          limite_superior = posicao_atual - 1 



    
  def excluir(self, value):
    retorno = self.pesquisa(value)
    if retorno == -1:
      return -1
    for i in range(retorno, self.ultimaposicao):
      self.valores[i] = self.valores[i + 1]
    self.ultimaposicao -= 1



vetor = VetorOrdenado(10000)


for i in range(9000):
  vetor.inserir(i)

      
vetor.imprime()

time = timeit.timeit(lambda: vetor.pesquisa_binaria(30), number=1000)
print(vetor.pesquisa_binaria(30), time)

time2 = timeit.timeit(lambda: vetor.pesquisa(30), number=1000)
print(vetor.pesquisa(30), time2)

      


