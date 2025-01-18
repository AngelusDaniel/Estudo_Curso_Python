
import decimal  #para numero com muitas casas decimais

numero1 = 0.1

numero2 = 0.7

numero3 = numero1 + numero2

print(numero3)

print(f"{numero3:.2f}")

print(round(numero3, 3)) #zero não aparece
print(round(5.321234, 3))


numero4 = decimal.Decimal("0.1")

numero5 = decimal.Decimal("0.7")

numero6 = numero4 + numero5

print(numero6)

