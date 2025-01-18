import re
import random




nove_digitos = ""

for i in range(9):
  nove_digitos += str(random.randint(0,9))

contador = 10
soma_digitos = 0

for digito in str(nove_digitos):
  soma_digitos += int(digito) * contador
  contador -= 1

resultado_multi_resto = (soma_digitos * 10) % 11



if resultado_multi_resto > 9:
  digito_1 = 0
else:
  digito_1 = resultado_multi_resto

print(digito_1)

#----------- Digito 2 ------------

cpf_com_digito = str(nove_digitos) + str(digito_1)

dez_digitos = cpf_com_digito[:10]

contador = 11
soma_digitos = 0

for digito in dez_digitos:
  soma_digitos += int(digito) * contador
  contador -= 1

resultado_multi_resto = (soma_digitos * 10) % 11

if resultado_multi_resto > 9:
  digito_2 = 0
else:
  digito_2 = resultado_multi_resto


  print(digito_2)


cpf_gerado = f"{nove_digitos}{digito_1}{digito_2}"

print(cpf_gerado)






