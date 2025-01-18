
x = 2

def escopo():
  x = 1
  print(x)
  def outra_func():
    y = 3
    print(x)
    print(y)
  outra_func()
  

print(x)
escopo()

print(x)
