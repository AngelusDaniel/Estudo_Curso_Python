



condicao = False;
passou_no_if = None;

if condicao:

  passou_no_if = True;
  print("faça algo")

# else:
#   passou_no_if = None;
#   print("Não faça algo");


print(passou_no_if, passou_no_if is None);
print(passou_no_if, passou_no_if is not None);

if passou_no_if is None:
  print("Não passou no if");