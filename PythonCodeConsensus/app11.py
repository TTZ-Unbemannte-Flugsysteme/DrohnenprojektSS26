"""Python Code 11: Consensus Control in Continuous Time."""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def MAS(x, t, N):
    """Dynamics of all agents."""

    dxdt = [0] * len(N)
    u = [0] * len(N)

    # Definition of agent i.
    for i in range(len(N)):

        # Compute the control input of agent i.
        difference = []

        for j in N[i]:
            difference.append(x[j] - x[i])

        u[i] = sum(difference)

        # Dynamics of agent i.
        dxdt[i] = u[i]

    return dxdt


# N[i] contains the agents that send information to agent i.
N = [[2], [3, 5], [4], [1, 2], [6], [2]]
x0 = [-1, 2, 6, 3, -3, 1]
t = np.arange(0, 5, 0.001)

# Add a dummy agent 0 so that the labels start at 1.
N.insert(0, [])
x0.insert(0, 0)

# Solve the differential equations.
x = odeint(MAS, x0, t, args=(N,))

# Do not plot the dummy agent 0.
plt.plot(t, np.delete(x, 0, 1))
plt.xlabel("t")
plt.ylabel("x_i")
plt.title("Continuous-time consensus")
plt.grid()
plt.show()
