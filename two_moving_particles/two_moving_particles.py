import numpy as np
import matplotlib.pyplot as plt

mu0 = 1 #Permeability of vaccum [H/m] (scaled to get better sizes)

def Magnetic_force(r1, r2, v1, v2, Q1, Q2):
    #Returns the magnetic force from between two moving particles
    r = r2 - r1
    R = np.linalg.norm(r)
    part1 = mu0/(4*np.pi*R**2)*Q2*v2
    part2 = np.cross(Q1*v1,r/R)
    F = np.cross(part1,part2)
    return F
    
#Complicated initial conditions
v1_0 = np.array([1,2,3]) #initial velocity of particle 1
v2_0 = np.array([-1,-5,5]) #initial velocity of particle 2
r1 = np.array([0,0,0]) #initial position of particle 1
r2 = np.array([1,0,0]) #initial position of particle 2

#Easy initial conditions
# v1_0 = np.array([0, -4, 0])  # initial velocity of particle 1
# v2_0 = np.array([0, 4, 0]) #initial velocity of particle 2
# r1 = np.array([0, 0, 0]) #initial position of particle 1
# r2 = np.array([1, 0, 0]) #initial position of particle 2

Q1 = 1 #charge of particle 1
Q2 = 2 #charge of particle 2


#calculate the magnetic force between particle 1 and 2
F12 = Magnetic_force(r1, r2, v1_0, v2_0, Q1, Q2)

#The data we are going to plot
positions = np.array([r1,r2,r2])
vectors = np.array([v1_0, v2_0, F12])
#labels and colors we are going to use
labels = ['Velocity particle 1', 
          'Velocity particle 2',
          'Magnetic force on particle 2']
colors = ['r', 'g', 'b']

#creating the figure we are going to use
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
#Plotting velocity and force vectors
for i in range(3):
    ax.quiver(positions[i, 0], positions[i, 1], positions[i, 2],
              vectors[i, 0], vectors[i, 1], vectors[i, 2], 
              color=colors[i], label=labels[i])
#Plotting the postions of the particles
ax.scatter(r1[0], r1[1], r1[2], color='r', label='Position particle 1')
ax.scatter(r2[0], r2[1], r2[2], color='g', label='Position particle 2')
#setting the axis
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
#labeling the axis
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
#showing the plot
ax.legend()
plt.show()

