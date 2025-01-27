from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
  try:
    print("Abrindo Arquivo")
    arquivo = open(caminho_arquivo, modo, encoding="utf8")
    yield arquivo
  # except Exception as e:
  #   print("Ocorreu um Erro")
  finally:
    print("Fechando Arquivo")
    arquivo.close()

with my_open("aula29OO.txt", "w") as arquivo:
  arquivo.write("Linha1\n")
  arquivo.write("Linha2\n", 123)
  arquivo.write("Linha3\n")
  print("WITH", arquivo)