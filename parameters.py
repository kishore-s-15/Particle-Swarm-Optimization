"""Defining the Parameters Class for Particle Swarm Optimization"""

# Parameter Class
class Parameters:
    
    def __init__(self):
        self.maxIter = 1000                                       # Maximum Number of Iterations
        self.nPop = 50                                              # Population (or) Swarm Size
        self.w = 1                                                  # Inertia Coefficient
        self.wdamp = 0.99                                           # Damping Ratio of Inertia Coefficient
        self.c1 = 2                                                 # Personal Acceleration Coefficient
        self.c2 = 2                                                 # Social (or) Global Acceleration Coefficient
        self.ShowIterInfo = True                                    # Flag for Showing Interation Information
        self.MaxVelocity = 0.2 * (self.varMax - self.varMin)        # Maximum Velocity of Particles
        self.MinVelocity = -self.MaxVelocity                        # Minimum Velocity of Particles