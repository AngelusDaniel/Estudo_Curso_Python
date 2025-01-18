

def criar_saudacao(saudacao):
  def saudar(nome):
    return f'{saudacao}, {nome}'
  return saudar


def fabrica_carro(marca):
  def carro(carro):
    return f"{marca} : {carro}"
  return carro


falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

print(falar_bom_dia("Daniel"))
print(falar_boa_noite("Daniel"))


Nissan = fabrica_carro("Nissan")

print(Nissan("Skyline"))