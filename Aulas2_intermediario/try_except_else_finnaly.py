try:

  print(1)
  5/0

except ZeroDivisionError:

  print("Dividiu por 0")

else:

  print("Não deu erro")

finally:   #finnaly é executado mesmo com erro

  print(2)