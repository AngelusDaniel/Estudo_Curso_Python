import os
import json


tarefas = []
tarefas_refazer = []


def listar(tarefas):
  print()
  if not tarefas:
    print("Nenhuma tarefa para listar")
    return
  print("\nListando: ")
  for tarefa in tarefas:
    print(tarefa)
  return


def desfazer(tarefas, tarefas_refazer):
  if not tarefas:
    print("Nenhuma tarefa para desfazer")
    return
  tarefa = tarefas.pop()
  tarefas_refazer.append(tarefa)
  return


def refazer(tarefas, tarefas_refazer):
  if not tarefas:
    print("Nenhuma tarefa para refazer")
    return
  tarefa = tarefas_refazer.pop()
  tarefas.append(tarefa)
  return

def adicionar_tarefa(tarefas, tarefa):
  tarefa = tarefa.strip()
  if not tarefa:
    print("Você não digitou nada")
    return
  tarefas.append(tarefa)
  return

def salvar_tarefas_txt(tarefas):
  with open("tarefassalvas.txt", "w") as arquivo:
    # json.dump(tarefas, arquivo, indent=2)
    for tarefa in tarefas:
      arquivo.write(f"{tarefa}\n")


def salvar_tarefas_json(tarefas):
  with open("tarefassalvas.json", "w") as arquivo:
    json.dump(tarefas, arquivo, indent=2)


while True:
  print("comandos: listas, desfazer, refazer")
  tarefa = input("Digite uma tarefa ou comando: ")
  
  comandos = {
    "listar": lambda: listar(tarefas),
    "desfazer": lambda: desfazer(tarefas, tarefas_refazer),
    "refazer": lambda: refazer(tarefas, tarefas_refazer),
    "adicionar": lambda: adicionar_tarefa(tarefas, tarefa),
    "salvar texto": lambda: salvar_tarefas_txt(tarefas),
    "salvar json": lambda: salvar_tarefas_json(tarefas),
    # "clear": os.system("clear")
  }

  comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
    comandos["adicionar"]
  comando()


  # if tarefa == "listar":
  #   listar(tarefas)
  #   continue

  # elif tarefa == "desfazer":
  #   desfazer(tarefas, tarefas_refazer)
  #   continue
  # elif tarefa == "refazer":
  #   refazer(tarefas, tarefas_refazer)
  #   continue
  # else: 
  #   adicionar_tarefa(tarefas, tarefa)
  #   continue
  








