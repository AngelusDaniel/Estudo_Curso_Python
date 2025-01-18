from itertools import count


#iterator infinito
c1 = count(step=10, start=5)

r1 = range(10,100, 5)

print("c1", hasattr(c1, "__iter__"))
print("c1", hasattr(c1, "__next__"))
print("")
print("r1", hasattr(r1, "__iter__"))
print("r1", hasattr(r1, "__next__"))

for i in c1:
  if i >= 100:
    break
  print(i)

print()

print("range")
for i in r1:
  print(i)
