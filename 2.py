import numpy as np 

array1 = np.random.randint(1, 101, size=10)
array2 = np.random.randint(1, 101, size=10)

soma = array1 + array2
subtracao = array1 - array2
multplicacao = array1 * array2
divisao = np.round(array1 / array2, 2)

print(array1)
print(array2)

print(soma)
print(subtracao)
print(multplicacao)
print(divisao)