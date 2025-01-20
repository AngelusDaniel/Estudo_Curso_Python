import random
#Vetor não ordenado
#pesquisa linear
#pesquisa média de n/2
#mover elementos restantes (n/2 passos)
#Big-O - O(2n) =  O(n)  linear
#duplicatas -> pesquisa se encontra o valor (N passos), insercão (N passos)
#exclusão primeiro item : N/2 comparações e N/2 movimentos
#exclusão de mais itens: Verificar N células e mais de N/2 celulas

import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=float)

  #O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print("O vetor está vazio")
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, "-", self.valores[i])

  #O(1) - #O(2)
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade -1:
      print("Capacidade maxima atingida")
    else:
      self.ultima_posicao += 1
      self.valores[self.ultima_posicao] = valor

  #O(n)
  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1
  
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1 
    for i in range(posicao, self.ultima_posicao):
      self.valores[i] = self.valores[i + 1]
    self.ultima_posicao -= 1





elementos =[]

for _ in range(10000):
  elementos.append(round(random.random(), 4))


def insere_nao_ordenado(lista):
  vetor = VetorNaoOrdenado(len(lista))
  for i in lista:
    vetor.insere(i)
  return vetor


vetor = insere_nao_ordenado(elementos)
vetor.imprime()

