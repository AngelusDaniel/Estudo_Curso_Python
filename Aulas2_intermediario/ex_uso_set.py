

letras = set()

while True:
  letra = input("Digite: ")
  letras.add(letra.lower())

  if "1" in letras:
    print("Parabens")
    break

  print(letras)