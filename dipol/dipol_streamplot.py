import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

mu0 = const.mu_0

def dipole(m, r, r0):
    """
    This function take the magnetic dipole m, with position r0, 
    and returnsthe magnetic field in postion r.
    """
    #np.subtract allows r0 to be a list and not an array
    R = np.subtract(np.transpose(r), r0).T
    #Finding the length of the vector
    norm_R = np.linalg.norm(R, axis=0)
    #Tensordot allows us to dotproduct along an axis
    m_dot_R = np.tensordot(m, R, axes=1)
    #calculatig the magnetic field
    B = 3*m_dot_R*R/norm_R**5 - np.tensordot(m, 1/norm_R**3, axes=0)
    #multiplying with the physical constant
    B *= mu0/(4*np.pi)
    return B
    
xa = np.linspace(-1, 1)
ya = np.linspace(-1, 1)

Bx, By = dipole(m = [0, 0.1], r = np.meshgrid(xa, ya),\
     r0=[-0.2, 0.1])

plt.streamplot(xa, ya, Bx, By)
plt.show()