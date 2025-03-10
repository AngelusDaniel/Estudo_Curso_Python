import numpy as np

class Pilha:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.topo = -1
    # Array de chars
    self.valores = np.empty(self.capacidade, dtype=str)

  def __pilha_cheia(self):
    if self.topo == self.capacidade - 1:
      return True
    else:
      return False

  # Mudança para método público
  def pilha_vazia(self):
    if self.topo == -1:
      return True
    else:
      return False

  def empilhar(self, valor):
    if self.__pilha_cheia():
      print('A pilha está cheia')
    else:
      self.topo += 1
      self.valores[self.topo] = valor

  # Retorno do valor desempilhado
  def desempilhar(self):
    if self.pilha_vazia():
      print('A pilha está vazia')
      return -1
    else:
      valor = self.valores[self.topo]
      self.topo -= 1
      return valor

  def ver_topo(self):
    if self.topo != -1:
      return self.valores[self.topo]
    else:
      return -1
    
#----------------------END CLASS------------------------------------------------------------



def ValidarExpressao(expressao):
  for i in range(len(expressao)):
    ch = expressao[i]
    if ch == '{' or ch == '[' or ch == '(':
      pilha.empilhar(ch)
    elif ch == '}' or ch == ']' or ch == ')':
      if not pilha.pilha_vazia():
        chx = str(pilha.desempilhar())
        if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
          return f"'Erro: ', {ch}, ' na posição ', {i}"
        else:
          return "Expressão correta"
      else:
          return f"'Erro: ', {ch}, ' na posição ', {i}"
  if pilha.pilha_vazia():
      return "nenhuma expressão encontrada!"

expressao = str(input('Digite uma expressão: '))
pilha = Pilha(len(expressao))

resultado = ValidarExpressao(expressao)


print(resultado)
