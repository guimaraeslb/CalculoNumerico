import numpy as np

A = np.array([[4, -1, 1],[2, 5, 2],[1, 2, 4]])
A1 = np.array([[8, -1, 1],[3, 5, 2],[11, 2, 4]])
A2 = np.array([[4, 8, 1],[2, 3, 2],[1, 11, 4]])
A3 = np.array([[4, -1, 8],[2, 5, 3],[1, 2, 11]])

detA = np.linalg.det(A)
detA1 = np.linalg.det(A1)
detA2 = np.linalg.det(A2)
detA3 = np.linalg.det(A3)


x1 = detA1 / detA
x2 = detA2 / detA
x3 = detA3 /detA

print(x1, x2, x3)
