


frase = "O Python é uma linguagem de programação " \
  "Multiparadigma. " \
    "Python foi criado por Guido Von Rossum."

frase = frase.replace(" ", "")

i = 0

letra_anterior = "";
letra_apareceu_mais_vezes = "";

while i < len(frase):

 
  letra_atual = frase[i]

  #quantas_vezes_letra_apareceu = frase.count(letra_atual);

  if frase.count(letra_apareceu_mais_vezes) < frase.count(letra_atual) or letra_apareceu_mais_vezes == "":
    letra_apareceu_mais_vezes = letra_atual

  #letra_anterior = letra_atual;

  i+=1

contagem_vezes = frase.count(letra_apareceu_mais_vezes)

print(f"A letra que mais apareceu: {letra_apareceu_mais_vezes} apareceu {contagem_vezes} vezes ");