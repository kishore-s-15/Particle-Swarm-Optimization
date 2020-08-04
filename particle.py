"""Defining the Particle Class for Particle Swarm Optimization"""

# Importing the required module
from cost_function import cost_function

# Particle Class
class Particle:
    
    def __init__(self):
        self.costFunction = cost_function       # Cost Function
        self.nVar = 5                           # Number of unkown (or) Decision Variables
        self.varSize = (1, self.nVar)           # Matrix Size of Decision Variables
        self.varMin = -10                       # Lower Bound of the Decision Variables
        self.varMax = 10                        # Upper Bound of the Decision Variables