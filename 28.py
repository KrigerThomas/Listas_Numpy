import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4])
y = np.array([1,2,0,2,1])

x_novo = np.arange(0, 4.1, 0.1)

y_novo = np.interp(x_novo, x, y)

plt.plot(x, y, 'o', label='Dados originais', color='red')  # Pontos originais
plt.plot(x_novo, y_novo, '-', label='Interpolação', color='blue')  # Curva interpolada
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolação dos Dados') #Titulo
plt.grid(True) #Mostra grade 
plt.show()