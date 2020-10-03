import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

theta0 = (10.0/180)*np.pi   # initial displacement in radians

q = const.e                 # charge on dipole in Coulombs
d = 1e-20                   # distance separating the charges (m)
m = const.m_e               # mass of a single charge (kg)
E = 1e-3                    # magnitude of the electric field
I = 2*m*(d/2)**2            # moment of inertia
p = q*d                     # electric moment

omega = np.sqrt(p*E/I)      # angular frequency
T = 2*np.pi/omega           # period

t = np.linspace(0, 2*T, 2000)  # time interval from t = 0 to t = 2T
theta = theta0*np.cos(omega*t) # solution for Simple harmonic motion

#Plot
plt.plot(t, theta)
plt.title("Simple Harmonic Motion - dipole in an Electric field")
plt.xlabel("time (s)")
plt.ylabel("angle (radians)")
plt.grid()
plt.show()
