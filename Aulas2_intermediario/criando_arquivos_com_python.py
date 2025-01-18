import os

# r (leitura), w(escrita), x(criação), a(escreve no final), b(binario),  t(modo texto), +(leitura e escrita)

#modulo os 

caminho_arquivo = "arquivo_criado.txt" #na mesma pasta que esta usando

caminho_arquivo = "/home/daniel/Documentos/pythonStudy/arquivo_criado.txt"


# arquivo = open(caminho_arquivo, "w")

# arquivo.close()#ao abrir um arquivo, sempre feche (ja insere o close após abrir pra garantir)

# with open(caminho_arquivo, "w+") as arquivo:    #with open fecha o arquivo automaticamente
#   arquivo.write("Linha 1\n")
#   arquivo.write("Linha 2\n")
#   arquivo.writelines(
#     ("linha 3\n", "linha 4\n")
#   )
#   arquivo.seek(0, 0) #move o cursor para o começo
#   print(arquivo.read()) #tem que usar w+ ou r+ para escrever no arquivo e ler
#   print("lendo")
#   arquivo.seek(0, 0) 
#   print(arquivo.readline(), end="") #tipo next #ja quebra linha
#   print(arquivo.readline().strip())
#   print(arquivo.readlines())
#   for linha in arquivo.readlines():
#     print(linha.strip())


# with open(caminho_arquivo, "r") as arquivo:    
#   print(arquivo.read())
  
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:    #w apaga tudo do arquivo e escreve de novo
  arquivo.write("Atenção\n")
  arquivo.write("Linha 2\n")
  arquivo.writelines(
    ("linha 3\n", "linha 4\n")
  )

#os tem que importar
# os.unlink(caminho_arquivo) #apaga o arquivo
# os.remove(caminho_arquivo) #apaga o arquivo
os.rename(caminho_arquivo, "arquivo_alterado.txt") #para mudar nome do arquivo ou mover arquivo