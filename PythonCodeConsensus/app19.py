"""Python Code 19: Discrete Consensus on a Balanced Digraph."""

import numpy as np
import matplotlib.pyplot as plt


# Directed cycle: 1 -> 2 -> 3 -> 4 -> 1.
A = np.array([[0, 0, 0, 1],
              [1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0]], dtype=float)

D = np.diag(np.sum(A, axis=1))
L = D - A

epsilon = 0.35
P = np.eye(4) - epsilon * L

x = np.array([-2, 4, 8, 2], dtype=float)
initial_average = np.mean(x)
steps = 50

history = [x.copy()]

for k in range(steps):
    x = P @ x
    history.append(x.copy())

history = np.array(history)

print("Initial average:", initial_average)
print("Final values:", np.round(x, 3))

plt.plot(history)
plt.axhline(initial_average, color="black", linestyle="--")
plt.xlabel("k")
plt.ylabel("x_i[k]")
plt.title("Balanced digraph: discrete average consensus")
plt.grid()
plt.show()
