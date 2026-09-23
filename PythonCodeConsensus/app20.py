"""Python Code 20: Discrete Consensus on an Unbalanced Digraph."""

import numpy as np
import matplotlib.pyplot as plt


# Agent 1 is the root and does not receive information.
N = [[], [], [1], [1], [2, 3]]
x = np.array([0, 5, -2, 8, 0], dtype=float)

epsilon = 0.25
steps = 60

initial_average = np.mean(x[1:])
root_value = x[1]

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

print("Initial average:", initial_average)
print("Root value:", root_value)
print("Final values:", np.round(x[1:], 3))

plt.plot(history[:, 1:])
plt.axhline(initial_average, color="black", linestyle="--",
            label="initial average")
plt.axhline(root_value, color="red", linestyle=":",
            label="root value")
plt.xlabel("k")
plt.ylabel("x_i[k]")
plt.title("Unbalanced graph: consensus is not the average")
plt.grid()
plt.legend()
plt.show()
