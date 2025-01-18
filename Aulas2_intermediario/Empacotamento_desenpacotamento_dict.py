
a, b = 1, 2

a, b = b, a 

print(a, b)

pessoa = {
  "nome": "Aline",
  "sobrenome": "Souza"
}

print(pessoa)

a, b = pessoa.values()

print(a, b)


a, b = pessoa.items()

print(a, b)

#desempacotamento
(a1, a2), (b1,b2) = pessoa.items()

print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
  print(chave, valor)


#--------------

dados_pessoa = {
  "idade": 19,
  "altura": 1.7
}

pessoas_completa = {**pessoa, **dados_pessoa}

print(pessoas_completa)


def mostro_argumentos_nomeados(*args, **kwargs):
  print("Não nomeados:",args)

  for chave, valor in kwargs.items():
    print(chave, valor)


mostro_argumentos_nomeados("a", nome ="Daniel", qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)

def mostro_argumentos_nomeados_var(vari):
  print(vari)
  for chave, valor in vari.items():
    print(chave, valor)



configuracoes = {

  "arg1": 1,
  "arg2": 2,
  "arg3": 3,
  "arg4": 4,
  "arg5": 5,

}

mostro_argumentos_nomeados(**configuracoes)
mostro_argumentos_nomeados_var(configuracoes)
