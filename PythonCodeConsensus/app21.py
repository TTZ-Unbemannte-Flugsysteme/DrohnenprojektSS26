"""Python Code 21: Measuring the Consensus Error."""

import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)

D = np.diag(np.sum(A, axis=1))
L = D - A

epsilon = 0.25
P = np.eye(4) - epsilon * L

x = np.array([-2, 4, 8, 2], dtype=float)
steps = 40

error = []

for k in range(steps):
    # Consensus error = largest value - smallest value.
    error.append(np.max(x) - np.min(x))

    # One discrete consensus update.
    x = P @ x

print("Final consensus error:", error[-1])

plt.semilogy(error)
plt.xlabel("k")
plt.ylabel("max(x) - min(x)")
plt.title("Consensus error approaches zero")
plt.grid()
plt.show()
