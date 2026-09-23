"""Python Code 24: Consensus with Switching Graphs."""

import numpy as np
import matplotlib.pyplot as plt


# Topology A connects the pairs 1--2 and 3--4.
N_A = [[], [2], [1], [4], [3]]

# Topology B connects the pairs 1--4 and 2--3.
N_B = [[], [4], [3], [2], [1]]

x = np.array([0, -2, 4, 8, 2], dtype=float)

epsilon = 0.3
steps = 50

history = np.zeros((steps + 1, len(x)))
history[0] = x

for k in range(steps):

    # Use topology A at even iterations.
    if k % 2 == 0:
        N = N_A

    # Use topology B at odd iterations.
    else:
        N = N_B

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
plt.title("Consensus under two switching topologies")
plt.grid()
plt.show()
