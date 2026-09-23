"""Python Code 16: Consensus Control in Discrete Time."""

import numpy as np
import matplotlib.pyplot as plt


# N[i] contains the agents that send information to agent i.
N = [[], [2], [3, 5], [4], [1, 2], [6], [2]]

# Agent 0 is a dummy agent. The real agents are 1 to 6.
x = np.array([0, -1, 2, 6, 3, -3, 1], dtype=float)

# Step size and number of iterations.
epsilon = 0.2
steps = 60

# Store all values for plotting.
history = np.zeros((steps + 1, len(x)))
history[0] = x

for k in range(steps):
    x_new = x.copy()

    for i in range(1, len(N)):
        u = 0

        for j in N[i]:
            u = u + x[j] - x[i]

        x_new[i] = x[i] + epsilon * u

    x = x_new
    history[k + 1] = x

print("Final values:", np.round(x[1:], 3))

plt.plot(history[:, 1:])
plt.xlabel("k")
plt.ylabel("x_i[k]")
plt.title("Discrete-time consensus")
plt.grid()
plt.show()
