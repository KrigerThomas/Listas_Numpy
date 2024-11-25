import numpy as np

dados = np.random.rand(50, 3)

media = np.mean(dados, axis=0)
desvio = np.std(dados, axis=0)

maximo = np.max(dados, axis=0)
minimo = np.min(dados, axis=0)

dados_normalizados = (dados - minimo) / (maximo - minimo)



print("Dados originais (50 amostras x 3 caracteristicas):")
print(dados)
print("\nMedia de cada coluna:")
print(media)
print("\nDesvio padrao de cada coluna:")
print(desvio)
print("\nValor maximo de cada coluna:")
print(maximo)
print("\nValor minimo de cada coluna:")
print(minimo)
print("\nDados normalizados (intervalo [0, 1]):")
print(dados_normalizados)