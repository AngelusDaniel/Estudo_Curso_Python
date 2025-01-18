string = "Daniel"
metodo = "upper"

if hasattr(string, "upper"):
  print(string, hasattr(string, "upper"))
  print(string.upper())
  print(getattr(string, metodo)())