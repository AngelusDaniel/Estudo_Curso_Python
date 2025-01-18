from itertools import groupby

alunos = [
  {"nome": "Daniel", "nota": "A"},
  {"nome": "Leticia", "nota": "B"},
  {"nome": "Fabrício", "nota": "A"},
  {"nome": "Rosemary", "nota": "C"},
  {"nome": "Joana", "nota": "D"},
  {"nome": "João", "nota": "A"},
  {"nome": "Eduardo", "nota": "B"},
  {"nome": "André", "nota": "A"},
  {"nome": "Anderson", "nota": "C"},
]

def ordena(aluno):
  return aluno["nota"]

alunos_ordenados = sorted(alunos, key=ordena)

for items in alunos_ordenados:
  print(items)

grupos = groupby(alunos_ordenados, key=ordena)

for chave, grupo in grupos:
  print(chave)
  for aluno in grupo:
    print(aluno)