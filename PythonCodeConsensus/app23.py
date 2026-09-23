"""Python Code 23: Consensus of Two-Dimensional Positions."""

import numpy as np
import matplotlib.pyplot as plt


# Complete undirected graph with four agents.
A = np.ones((4, 4)) - np.eye(4)
D = np.diag(np.sum(A, axis=1))
L = D - A

epsilon = 0.2
P = np.eye(4) - epsilon * L

# Initial x- and y-coordinates.
x = np.array([-3, 4, 5, -2], dtype=float)
y = np.array([4, 3, -3, -4], dtype=float)

steps = 20
x_history = [x.copy()]
y_history = [y.copy()]

for k in range(steps):
    x = P @ x
    y = P @ y

    x_history.append(x.copy())
    y_history.append(y.copy())

x_history = np.array(x_history)
y_history = np.array(y_history)

print("Final x-coordinates:", np.round(x, 3))
print("Final y-coordinates:", np.round(y, 3))

# Plot the path of every agent in the plane.
for i in range(4):
    plt.plot(x_history[:, i], y_history[:, i], marker="o",
             label="agent " + str(i + 1))

plt.xlabel("x")
plt.ylabel("y")
plt.title("Two-dimensional position consensus")
plt.grid()
plt.axis("equal")
plt.legend()
plt.show()
