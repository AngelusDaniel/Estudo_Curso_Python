


def generator(n=0, maximum=1000):
  while True:
    yield n

    n+=1

    if n > maximum:
      return
    


gen = generator(n=5, maximum=11)

for n in gen:
  print(n)
