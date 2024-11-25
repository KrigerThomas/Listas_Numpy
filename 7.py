import numpy as np

notas = np.random.randint(0, 11, size=(5, 4))

media_alunos = np.mean(notas, axis= 1)

media_provas = np.mean(notas, axis= 0)

print("Matriz de notas (alunos x provas):")
print(notas)
print("\nMedia de cada aluno:")
print(media_alunos)
print("\nMedia de cada prova:")
print(media_provas)