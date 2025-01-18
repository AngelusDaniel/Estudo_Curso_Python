

#controlando a quantidade de argumentos posicionais e nomeados em funções

# *args (ilimitado de argumentos posicionais)

#kwargs (ilimitado de argumentos nomeados)

#Positional-only Paramters (/) - tudo antes da barra deve ser apenas posicional

#pep 570 - Python positional-Only paramters


#Keyword-only Arguments (*) - sozinho NÃO SUGA valores.

#PEP 3102 - Keyword-only Arguments

# def soma(a, b, /, x, y):  #antes da barra tem que ser posicional, depois pode ser nomeado ou não
#   print(a + b + x + y)


# soma(1,2, y=3, x=4)


def soma(a, b, *, c):  #antes do asterisco deve ser posicional e depois nomeado
  print(c)
  print(a + b + c)


soma(1,2, c=3)


