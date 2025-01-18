

#com while

while True:

  entrada1 = input("Insira o primeiro numero: ");
  entrada2 = input("Insira o segundo numero: ");
  operador = input("Insira o operador (+-/*)");

  numero1 = 0
  numero2 = 0

  try:
    
    numero1 = float(entrada1)
    numero2 = float(entrada2)

    if operador == "+":
      resultado = numero1 + numero2
    
    elif operador == "-":
      resultado = numero1 - numero2

    elif operador == "*":
      resultado = numero1 * numero2

    elif operador == "/":
      resultado = numero1 / numero2


    print(f"O resultado de {numero1}{operador}{numero2} é:", resultado)

    sair = input("Quer sair?").lower();

    if sair == "sair" or sair == "s":
      break
    else: 
      continue
  except:

    operadores_permitidos = "+-*/";

    if not entrada1.isdigit() or not entrada2.isdigit():

      print("Ocorreu um erro, insira apenas números\n")
      sair = input("Quer sair? [s/sim]").lower();

      if sair == "sair" or sair == "s":
        break
      else: 
        continue

    elif operador not in operadores_permitidos:

      print("Ocorreu um erro. Operador incorreto\n")
      sair = input("Quer sair? [s/sim]").lower();

      if sair == "sair" or sair == "s":
        break
      else: 
        continue

    elif len(operador) > 1:

      print("Ocorreu um erro.Insira apenas um operador\n")
      sair = input("Quer sair? [s/sim]").lower();

      if sair == "sair" or sair == "s":
        break
      else: 
        continue

    else: 
      print("Ocorreu um erro\n")
      sair = input("Quer sair? [s/sim]").lower();

      if sair == "sair" or sair == "s":
        break
      else: 
        continue

