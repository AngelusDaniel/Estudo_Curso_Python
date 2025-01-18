
try:
  a = 10
  b = 0
  d = {}
  #print("Linha 1"[1000])
  c = a / b
  print("Linha 2")

  print("teste" + d)

except ZeroDivisionError as e:
  print(e.__class__.__name__)
  print(e)

except NameError:

  print("Variavel não declarada")

except (TypeError, IndexError) as error:
  print("Erro de tipo ou index")
  print("MSG: ",error)
  print("Nome:", error.__class__.__name__)

except Exception:
  print("Erro desconhecido")

print("CONTINUAR")