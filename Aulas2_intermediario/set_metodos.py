s1 = set()

s1.add("Teste")
s1.add(1)

s1.update(("Olá mundo", 2, 3, 4))
#s1.clear()
s1.discard(2)
print(s1)



#operadores importantes

# | união
# & intersecção
# - diferença : Os presentes apenas no conj da esquerda
# ^ difereça simétrica - itens que não então em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 =  s1 - s2
s5 = s1 ^ s2

print(s3) #União dos dois conj
print(s4) #que esta presente nos dois conj
print(s5)