

#Funções de primeira classe
#Higher Order

def saudacao(texto, nome):
  return f"{texto}, {nome}"

saudacao_2 = saudacao


def executar(funcao, *args):
  return funcao(*args)

msg = executar(saudacao_2, "alou", "Daniel")


print(msg)



