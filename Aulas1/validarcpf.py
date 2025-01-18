import re

# cpf = "908.412.180-56" \
# .replace(".","") \
# .replace("-","") \
# .replace(" ","")


entrada =  input("Insira o CPF: ")

cpf = re.sub(r"[^0-9]", "", entrada)

# primeiro_caractere_entrada = entrada[0]
# primeiro_caractere_repetido = primeiro_caractere_entrada * \
#   len(entrada)
# print(entrada, primeiro_caractere_repetido)

entrada_repetida = entrada == entrada[0] * len(entrada);

nove_digitos = cpf[:9]

contador = 10
soma_digitos = 0

for digito in nove_digitos:
  soma_digitos += int(digito) * contador
  contador -= 1

resultado_multi_resto = (soma_digitos * 10) % 11



if resultado_multi_resto > 9:
  digito_1 = 0
else:
  digito_1 = resultado_multi_resto

print(digito_1)

#----------- Digito 2 ------------

cpf_com_digito = nove_digitos + str(digito_1)

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


if cpf_gerado == cpf:

  print("O CPF é válido");

else:

  print("O cpf é inválido")





