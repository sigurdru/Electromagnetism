import numpy as np
R1 = 10  # [ohm]
R2 = 20  # [ohm]
R3 = 30  # [ohm]
U1 = 10  # [V]
U2 = 5   # [V]
A = np.array([[R1, 0, R3],[0, -R2, R3],[1, -1, -1]])
#inverting the matrix A
Ainv = np.linalg.inv(A)

B = np.array([U1, U2, 0])
#finding the solution
C = np.dot(Ainv,B)
print(C)