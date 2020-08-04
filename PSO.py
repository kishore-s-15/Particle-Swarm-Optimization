"""Defining the PSO Class for Particle Swarm Optimization"""

# Importing the required modules
from particle import Particle
from parameters import Parameters

# Particle Swarm Optimization Class
class PSO(Particle, Parameters):

    def __init__(self):
        # Parent Classes initialized by __init__() method
        Particle.__init__(self)                             # Particle Class Inherited
        Parameters.__init__(self)                           # Parameters Class Inherited

        # emptyParticle Template for Particle Initialization
        self.emptyParticle = {}
        self.emptyParticle["Position"] = None               # Particle Position
        self.emptyParticle["Velocity"] = None               # Particle Velocity
        self.emptyParticle["Cost"] = None                   # Particle Cost
        self.emptyParticle["Best"] = {}                     # Particle Personal Best
        self.emptyParticle["Best"]["Position"] = None       # Particle Personal Best Position
        self.emptyParticle["Best"]["Cost"] = None           # Particle Personal Best Cost

    # Method for Creating Population Array
    def pop_array(self):

        # Particles dictionary for storing all the initialized emptyParticles
        self.particles = {}

        for i in range(self.nPop):
            self.particles[i] = self.emptyParticle