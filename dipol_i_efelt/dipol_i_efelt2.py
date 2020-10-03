import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

theta = np.pi/6         # intial angle of displacement (degres)
q = 1.0e-19             # Charge on dipole in Coulombs
d = 3.0e-9              # distance separating the charges (m)
p = q*d                 # electric moment
m = 3.0e-5              # mass of a single charge (kg)
E = 1000                # magnitude of the electric field
I = 2*m*(d/2)**2        # moment of inertia
omega = np.sqrt(p*E/I)  #angle velocity
T = 2*np.pi/omega       # period

# number of time intervals
N = int(1e4)
# set the times to evaluate
t = np.linspace(0, 4*T, N)

# compute approximate theta values on the time intervals
Approx_Solution = theta*np.cos(omega*np.array(t))


def torque(x0, t, p, I, E):
    dfdt = np.zeros(2)
    dfdt[0] = x0[1]
    dfdt[1] = -p*E*np.sin(x0[0])/I
    return dfdt

# Set the intial condition [initial angle, initial velocity]
x0 = [theta, 0.0]

# numerically solve the real solution using odeint
sol2 = odeint(torque, x0, t, args=(p, I, E))

# Plot the two solutions
# plt.plot(t, Approx_Solution)
# plt.plot(t, sol2[:, 0])
# plt.grid()
# plt.xlabel("time (s)")
# plt.ylabel("angle (rads)")
# plt.show()

# compute the difference between approx and actual on intervals
diff = np.abs(Approx_Solution-sol2[:,0])

# Plot the difference vs time
plt.plot(t, diff)
plt.xlabel("time (s)")
plt.ylabel("Difference")
plt.show()

#finding where the error is bigger than 0.05 rad
index = np.where(diff>0.05)
# Plot the red dots
plt.plot(t, sol2[:,0], label='numeric solution')
plt.scatter(t[index], sol2[index,0], color='r', label='error>0.05 rad')
plt.xlabel("time (s)")
plt.ylabel("angle (rads)")
plt.legend(loc=1)
plt.grid()
plt.show()

