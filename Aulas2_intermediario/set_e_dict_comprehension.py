produto = {
  "nome": "Caneta Azul",
  "preco": 2.5,
  "categoria": "Escritório"
}

print(produto.items())


#for chave, valor in produto.items():
 # ...

dc = {

    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != "categoria"
}

print(dc)


#set comprehension

s1 = {i for i in range(10)}
print(s1)