"""This Module implements the contriction coefficients for Particle Swarm Optimization parameters as stated by Maurice Clerc and James Kennedy in their paper.

   Paper Title: The particle swarm - explosion, stability, and convergence in a multidimensional complex space
"""

# Constriction Coefficients
kappa = 1
phi1 = 2.05
phi2 = 2.05
phi = phi1 + phi2
chi = (2 * kappa) / abs(2 - phi - ((phi**2 - (4 * phi))**0.5))