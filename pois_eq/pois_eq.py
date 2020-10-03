import numpy as np
import matplotlib.pyplot as plt
# Radius
r = 1
# circumference
o = 2*np.pi*r
# The area we are looking at
N = int(1e3)
h = np.linspace(0, 1, N)
x = np.linspace(0, o, N)
X, Y = np.meshgrid(x, h)
V = np.zeros((N, N))

# Setting initial conditions
V[0, :] = 10
# Potential at the end of the sylinder
V_end = 0
# The potential we are going to test
Vtest = np.linspace(10, 9, 100)
# Empty list we are going to fill with results
result = []

#Here we test for the different initial conditions
for v in Vtest:
    V[1, :] = v
    for i in range(N-2):
        #Calculating the result given the initial conditions
        V[i+2, :] = 2*V[i+1, :] - V[i, :]
    #Fill list with results compered with actual solution
    result.append(abs(V[-1, 0] - V_end))
#Find the best match
index = np.where(np.array(result) == min(result))
#Set best initial conditions
V[1, :] = Vtest[index]
#Find solution with best initial conditions
for i in range(N-2):
    V[i+2, :] = 2*V[i+1, :] - V[i, :]
result.append(abs(V[-1, 0] - V_end))

#Plot the result
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, V, levels=100, cmap='cool')
fig.colorbar(CS)
plt.show()
