"""Cost Function for Particle Swarm Optimization.
The Sphere Cost Function is used, which returns
the square of the argument passed."""

# Importing the required library
import numpy as np

# Cost Function
def cost_function(x):
    return np.sum(x**2)