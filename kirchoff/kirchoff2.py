import numpy as np
R1 = 10  # [ohm]
R2 = 20  # [ohm]
R3 = 30  # [ohm]
R4 = 40  # [ohm]
R5 = 50  # [ohm]
R6 = 60  # [ohm]
U1 = 10  # [V]
U2 = 5   # [V]
U3 = 12  # [V]
U4 = 24   # [V]
A = np.array([[R1, 0, R3, 0, 0, 0], 
              [0, -R2, R3, 0, 0, 0], 
              [1, -1, -1, 0, 0, 0],
              [0, 0, 0,-R4, 0, 0], 
              [0, 0, 0, R4, -R5, 0], 
              [0, 0, 0, 0, -R5, R6]])
#inverting the matrix A
Ainv = np.linalg.inv(A)

B = np.array([U1, U2, 0, U4, 0, U2-U3])
#finding the solution
C = np.dot(Ainv, B)
print(C)
