

def gen1():
  yield 1
  yield 2
  yield 3


def gen2():
  yield from gen1()
  yield 4
  yield 5
  yield 6



def gen3(gen):
  yield from gen()
  yield 7
  yield 8
  yield 9


g = gen3(gen2)


for num in g:
  print(num)

