#mutaveis [] {} set()

#imutaveis () "" 0 0.0 None False range(0, 10)

lista = [] 
dicionario = {} #falsy
conjunto = set() #falsy
tupla = () #falsy
string = "" #falsy
inteiro = 0 #falsy
flutuante = 0.0 #falsy
nada = None #falsy
falso = False #falsy
intervalo = range(0) #falsy

def falsy(valor):
  return "falsy" if not valor else "truthy"

print(f"TESTE", falsy("TESTE"))
print(f"{lista=}",  falsy(lista))
print(f"{dicionario=}",  falsy(dicionario))
print(f"{conjunto=}",  falsy(conjunto))
print(f"{string=}",  falsy(string))
print(f"{inteiro=}",  falsy(inteiro))
print(f"{flutuante=}",  falsy(flutuante))
print(f"{nada=}",  falsy(nada))
print(f"{falso=}",  falsy(falso))
print(f"{intervalo=}",  falsy(intervalo))
