

p1 = {
  "nome": "Daniel",
  "sobrenome": "Angelus",
}


# p1.update({
#   "nome": "Novo valor",
#   "idade": 21,

# })

#tupla = ('sobrenome', 'novovalor') não ta funfando
#p1.update(tupla) não ta funfando

estilolista = [["nome", "valor"], ["idade", 30]]
p1.update(estilolista)

p1.update(sobrenome="new value")





print(p1) 