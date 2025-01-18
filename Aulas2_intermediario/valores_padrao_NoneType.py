


def soma(a, b, z=None):
  
  if z is not None:
    print(f"{a=} {b=} {z=}", a + b + z)
  else:
    print(f"{a=} {b=}", a + b)


soma(6, 3, 4)