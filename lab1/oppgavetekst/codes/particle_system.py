import numpy as np
from progress.bar import IncrementalBar
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
plt.rc("text", usetex=True)

import matplotlib
matplotlib.use("TkAgg")

class paul_trap:
    def __init__(self, Nparticles, total_time, Nsteps):
        self.Nparticles = Nparticles
        self.total_time = total_time
        self.Nsteps = Nsteps
        self.dt = total_time/Nsteps
        self.dt_squared = 0.5*self.dt**2
        elementary_charge = 1e-19
        self.g = 9.81           #m/s^2
        self.ke = 1./(4*np.pi*8.85e-12)         #Coulomb constant

        self.q_over_m = 1e-4             #C/kg
        self.m = 5e-5                  #Roughly the mass of a grain of cinnamon
        self.q = self.m*self.q_over_m    #Charge of a grain of cinnamon.

        self.v = np.zeros((Nparticles, Nsteps, 3))
        self.r = np.zeros((Nparticles, Nsteps, 3))
        self.a = np.zeros((Nparticles,3))
        self.t = np.zeros(Nsteps)

        #Trap dimensions
        self.z0 = 0.005
        self.r0 = np.sqrt(2)*self.z0

        #AC source
        self.Omega = 2*np.pi*50         #50 Hz AC voltage.
        self.V0 = 4000                  #Volts
        for i in range(Nparticles):
            self.r[i, 0, :] = np.random.uniform(-0.5*self.z0, 0.5*self.z0, size=3)
    def solve_euler_cromer(self):
        bar = IncrementalBar("Progress", max = self.Nsteps)
        for k in range(self.Nsteps-1):
            bar.next()
            self.t[k+1] = self.t[k] + self.dt
            omega_z = 4*self.q_over_m/self.r0**2*self.V0*np.cos(self.Omega*self.t[k])
            omega_xy = 0.5*omega_z
            for i in range(self.Nparticles):
                self.a[i, 0] = omega_xy*self.r[i, k, 0]
                self.a[i, 1] = omega_xy*self.r[i, k, 1]
                self.a[i, 2] = -omega_z*self.r[i, k, 2] - self.g
                #Add acceleration from interaction term:
                F = np.zeros(3)
                for j in range(self.Nparticles):
                    r_diff = np.zeros(3)
                    if i != j:
                        r_diff = self.r[i,k,:] - self.r[j,k,:]
                        rnorm = np.linalg.norm(r_diff)
                        F += r_diff/rnorm**1.5

                F *= self.q*self.q_over_m*self.ke
                self.a[i,:] += F


                self.v[i, k+1, :] = self.v[i, k, :] + self.a[i, :]*self.dt
                self.r[i, k+1, :] = self.r[i, k, :] + self.v[i, k+1, :]*self.dt
        bar.finish()


    def plot_trajectory(self):
        self.r[:,:,:]/self.z0
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel(r"$x/z_0$", fontsize=14)
        ax.set_ylabel(r"$y/z_0$", fontsize=14)
        ax.set_zlabel(r"$z/z_0$", fontsize=14)
        for i in range(self.Nparticles):
            l = ["particle nr", str(i)]
            ax.plot(self.r[i,:,0], self.r[i,:,1], self.r[i,:,2], label=" ".join(l))
        #plt.legend()
        l = ["paul_trap", "particles", str(self.Nparticles), "total_time", str(self.total_time)]
        plt.savefig("_".join(l) + ".pdf")
        #plt.show()
        plt.close()


    def animate_trajectory(self):
        fps = 60
        n_frames = 50
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel(r"$x/z_0$", fontsize=14)
        ax.set_ylabel(r"$y/z_0$", fontsize=14)
        ax.set_zlabel(r"$z/z_0$", fontsize=14)
        sct, = ax.plot([], [], [], "o", markersize=2)

        def update(i):
            sct.set_data(self.r[:,i,0], self.r[:,i,1])
            sct.set_3d_properties(self.r[:,i,2])

        ax.set_xlim(-2*self.z0, 2*self.z0)
        ax.set_ylim(-2*self.z0, 2*self.z0)
        ax.set_zlim(-2*self.z0, 2*self.z0)
        anim = animation.FuncAnimation(fig, update, frames=self.Nsteps, interval=1, blit=False)
        anim.save("animated_trajectory.mp4", writer="ffmpeg", fps=500)
        plt.show()
