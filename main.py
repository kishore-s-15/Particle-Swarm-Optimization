"""This file implements the Particle Swarm Optimization"""

# Importing the required libraries and modules
import numpy as np
import matplotlib.pyplot as plt
from cost_function import cost_function
from contrictions import *
from PSO import PSO

if __name__ == "__main__":
    
    # Initialization
    # Instantiating PSO objecy
    pso = PSO()

    # Select the type of PSO (normal / constricted)
    # Constricted PSO implements constrictions on PSO parameters
    # mode = "normal"
    mode = "constricted"

    if mode == "constricted":
        # If constriction mode is enabled, 
        # constrictions are applied on the parameters
        pso.w = chi
        pso.c1 = chi * phi1
        pso.c2 = chi * phi2

    # Creating Population Array
    pso.pop_array()

    # Initializing Global Best
    GlobalBest = {}
    
    # Initializing Global Best Cost
    GlobalBest["Cost"] = np.inf

    # Array to hold best cost value on each iteration
    BestCosts = np.zeros((pso.maxIter, 1))

    # Initialize Population Members
    for i in range(pso.nPop):
        
        # Generate Random Solution
        pso.particles[i]["Position"] = np.random.uniform(pso.varMin, pso.varMax, pso.varSize)
        
        # Initialize Velocity
        pso.particles[i]["Velocity"] = np.zeros(pso.varSize)

        # Evaluation
        pso.particles[i]["Cost"] = pso.costFunction(pso.particles[i]["Position"])

        # Initalize the Personal Best
        pso.particles[i]["Best"]["Position"] = pso.particles[i]["Position"]
        pso.particles[i]["Best"]["Cost"] = pso.particles[i]["Cost"]

        # Update Global Best
        if pso.particles[i]["Best"]["Cost"] < GlobalBest["Cost"]:
            GlobalBest = pso.particles[i]["Best"]

    # Main Loop of PSO

    # Looping through number of iterations
    for iter in range(pso.maxIter):
        
        # Looping through number of particles
        for i in range(pso.nPop):
            pso.particles[i]["Velocity"] = (pso.w * pso.particles[i]["Velocity"]) + ((pso.c1 * np.random.rand(*pso.varSize)) * pso.particles[i]["Best"]["Position"] - pso.particles[i]["Position"]) + (pso.c2 * np.random.rand(*pso.varSize) * (GlobalBest["Position"] - pso.particles[i]["Position"]))

            # Apply Velocity Limits
            pso.particles[i]["Velocity"] = np.maximum(pso.particles[i]["Velocity"], pso.MinVelocity)
            pso.particles[i]["Velocity"] = np.minimum(pso.particles[i]["Velocity"], pso.MaxVelocity)

            # Update Position
            pso.particles[i]["Position"] += pso.particles[i]["Velocity"]

            # Apply Lower and Upper Bound Limits
            pso.particles[i]["Position"] = np.maximum(pso.
            particles[i]["Position"], pso.varMin)
            pso.particles[i]["Position"] = np.minimum(pso.
            particles[i]["Position"], pso.varMax)

            # Evaluation
            pso.particles[i]["Cost"] = pso.costFunction(pso.particles[i]["Position"])

            # Update Personal Best
            if pso.particles[i]["Cost"] < pso.particles[i]["Best"]["Cost"]:
                pso.particles[i]["Best"]["Position"] = pso.particles[i]["Position"]
                pso.particles[i]["Best"]["Cost"] = pso.particles[i]["Cost"]

                # Update Global Best
                if pso.particles[i]["Best"]["Cost"] < GlobalBest["Cost"]:
                    GlobalBest = pso.particles[i]["Best"]

        # Stores the Best Cost Value
        BestCosts[iter] = GlobalBest["Cost"]

        # Display Iteration Information
        if pso.ShowIterInfo:
            print(f"Iteration: {iter + 1} - Best Cost = {BestCosts[iter][0]}")

        # Applying Damping Coefficient to Inertia Coefficient 'w'
        pso.w *= pso.wdamp

    # Results
    print("\n---------------Summary---------------")
    print(f"\nBest Cost afer {pso.maxIter} Iterations = {GlobalBest['Cost']}")

    # Plotting Iterations vs Best Cost
    plt.figure().canvas.set_window_title("Particle Swarm Optimization")
    # plt.plot(BestCosts)
    plt.semilogy(BestCosts)
    plt.xlabel("Iterations")
    plt.ylabel("Best Cost")
    plt.title("Sphere Cost Function")
    plt.show()