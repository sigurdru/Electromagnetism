
from particle_system import paul_trap
import sys
Nparticles = 15
total_time = float(sys.argv[1])
Nsteps = int(1e5)
my_trap = paul_trap(Nparticles, total_time, Nsteps)
my_trap.solve_euler_cromer()
my_trap.plot_trajectory()

#my_trap.animate_trajectory()


"""
from one_particle import paul_trap_single_particle
import sys
total_time = float(sys.argv[1])
Nsteps = int(1e5)
my_trap = paul_trap_single_particle(total_time, Nsteps)
my_trap.solve_euler_cromer()
my_trap.plot_trajectory()
"""

#my_trap.animate_trajectory()
