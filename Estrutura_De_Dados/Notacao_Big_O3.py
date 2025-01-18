from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)


print(n)

print(n.shape) #formato da lista
print(np.ones(n.shape))

print(np.log(n)) #logaritmo

labels = ["Constant", "Logarithmic", "Linear", "Log linear", "Quadratic", "Cubic", "Exponential"]

big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]


plt.figure(figsize=(10, 8)) #gerando gráfico  figsize = tamanho
plt.ylim(0, 100) #limite do eixo y
for i in range (len(big_o)):
  plt.plot(n, big_o[i], label=labels[i])
plt.legend()
plt.ylabel("Runtime")
plt.xlabel("n")
  
plt.show()

