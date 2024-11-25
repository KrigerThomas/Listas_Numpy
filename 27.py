import numpy as np

matriz_transformacao = np.array([[2, 1], [1, 3]])

vetor_v = np.array([1, 2])

vetor_transformado = np.dot(matriz_transformacao, vetor_v)

print("Matriz de transformacao:")
print(matriz_transformacao)

print("\nVetor v:")
print(vetor_v)

print("\nVetor transformado (multiplicacao da matriz pelo vetor):")
print(vetor_transformado)