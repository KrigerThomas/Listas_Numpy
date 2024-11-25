import numpy as np 

x = np.arange(0, 51)

#Elementos pares

pares = x[x % 2 == 0]

# Multiplos de 5

multiplos = x[x % 5 == 0]

print(x)
print(pares)
print(multiplos)
