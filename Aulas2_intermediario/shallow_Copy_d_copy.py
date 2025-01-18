
#shallow copy e  deep copy


#deep copy
import copy

d1 = {
  "c1": 1,
  "c2": 2,
  "l1": [0, 1, 2]

}


#d2 = d1  isso não copia, apenas aponta pro mesmo

d2 = d1.copy()

#não fica linkado a lista como o copy
d3 = copy.deepcopy(d1)


d2["c1"] = 1000

#shallow copy, mesmo com .copy() as listas ficam linkadas uma na outra

d2["l1"][1] = 99

print(d1)
print(d2)
print(d3)