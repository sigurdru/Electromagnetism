import numpy as np
from progress.bar import IncrementalBar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rc("text", usetex=True)
class paul_trap_single_particle:
    def __init__(self, total_time, Nsteps):
        self.total_time = total_time
        self.Nsteps = Nsteps
        self.dt = total_time/Nsteps
        self.dt_squared = 0.5*self.dt**2
        elementary_charge = 1e-19
        #self.q = 10000.*elementary_charge
        self.g = 9.81           #m/s^2
        self.ke = 1./(4*np.pi*8.85e-12)         #Coulomb constant

        self.q_over_m = 1e-4             #C/kg
        self.m = 5e-5                  #Roughly the mass of a grain of cinnamon
        self.q = self.m*self.q_over_m    #Charge of a grain of cinnamon.
        print(self.q)


        self.v = np.zeros((Nsteps, 3))
        self.r = np.zeros((Nsteps, 3))
        self.a = np.zeros(3)
        self.t = np.zeros(Nsteps)

        #Trap dimensions
        self.z0 = 0.005
        self.r0 = np.sqrt(2)*self.z0

        #AC source
        self.Omega = 2*np.pi*50         #50 Hz AC voltage.
        self.V0 = 4000                  #Volts
        self.r[0, :] = np.random.uniform(-0.5*self.z0, 0.5*self.z0, size=3)
    def solve_euler_cromer(self):
        bar = IncrementalBar("Progress", max = self.Nsteps)
        for k in range(self.Nsteps-1):
            bar.next()
            self.t[k+1] = self.t[k] + self.dt
            omega_z = 4*self.q_over_m/self.r0**2*self.V0*np.cos(self.Omega*self.t[k])
            omega_xy = 0.5*omega_z
            self.a[0] = omega_xy*self.r[k, 0]
            self.a[1] = omega_xy*self.r[k, 1]
            self.a[2] = -omega_z*self.r[k, 2] - self.g
            self.v[k+1, :] = self.v[k, :] + self.a[:]*self.dt
            self.r[k+1, :] = self.r[k, :] + self.v[k+1, :]*self.dt
        bar.finish()


    def plot_trajectory(self):
        self.r[:,:]/self.z0
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel(r"$x/z_0$", fontsize=14)
        ax.set_ylabel(r"$y/z_0$", fontsize=14)
        ax.set_zlabel(r"$z/z_0$", fontsize=14)
        ax.plot(self.r[:,0], self.r[:,1], self.r[:,2])
        l = ["paul_trap", "particles", "only_one", "total_time", str(self.total_time)]
        plt.savefig("_".join(l) + ".pdf")
        plt.show()
        plt.close()
