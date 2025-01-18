a = "A"
b = "B"
c = 1.111

c = 1.1

string = "a={1} b={2:.2f} c={0}"

formato = string.format(a, b, c)

print(formato)


#formatação com fstring

variavel = "ABC"

print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10} .")
print(f"{variavel:e<10} .")

print(f"{1000.23872734198192:0>10.2f}")

print(f"O hexadecimal de 1500 é {1500:08x}")
print(f"O hexadecimal de 1500 é {1500:08X}")