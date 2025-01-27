
frase = " Frase programação python, teste"

#lista_palavras_crua = frase.split(",")
lista_palavras_crua = frase.split()

lista_palavras = []
lista_palavras2 = []

print(lista_palavras_crua)

# for plv in lista_palavras_crua:
#   lista_palavras2.append(plv.strip());

# print(lista_palavras2)

for i, plv in enumerate(lista_palavras_crua):
  lista_palavras.append(plv.strip())  #retira os espaços inicio e final, tem o rstrip e o lstrip

print(lista_palavras)
# print(lista_palavras_crua)

frases_unidas = "-".join("abc")

print(frases_unidas)

lista_palavras_sem_virgula = []
for i, frase in enumerate(lista_palavras_crua):
  lista_palavras_sem_virgula.append(lista_palavras[i].replace(",", "")) #tirando virgulas

frases_unidas2 = "-".join(lista_palavras_sem_virgula)

print(frases_unidas2)