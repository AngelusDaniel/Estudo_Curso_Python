

nome = input("Escreva seu nome:\n ")

idade = input("Escreva sua idade:\n ")

if not nome or not idade:
  print("Algum dos campos está vazio")
else:
  print(f"Seu nome é {nome} ")
  print(f"seu nome invertido é {nome[::-1]}")

  n = len(nome)
  
  print(f"Seu nome tem {n} letras")
  print(f"A primira letra do seu nome é {nome[0]}")
  print(f"A ultima letra do seu nome é {nome[n-1]}")  
