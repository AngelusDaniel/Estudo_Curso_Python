# numero = input("");

# if numero.isdigit():

#   numero_float = float(numero);

#   print(f"O dobro do seu numero é {numero_float * 2:.2f}");

# else:

#   print("não é um numero");



numero = input("");

try:

  numero_float = float(numero);
  print(f"O dobro do seu numero é {numero_float * 2:.2f}");

except:
  
  print("não é um numero");


