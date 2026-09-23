"""Python Code 17: Perron Matrix and Average Consensus."""

import numpy as np
import matplotlib.pyplot as plt


# Undirected path: 1--2--3--4.
A = np.array([[0, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)

D = np.diag(np.sum(A, axis=1))
L = D - A

# P is the discrete update matrix.
epsilon = 0.25
P = np.eye(4) - epsilon * L

print("Perron matrix P:")
print(P)
print("Row sums of P:", np.sum(P, axis=1))

x = np.array([-2, 4, 8, 2], dtype=float)
initial_average = np.mean(x)
steps = 40

history = np.zeros((steps + 1, 4))
history[0] = x

for k in range(steps):
    x = P @ x
    history[k + 1] = x

print("Initial average:", initial_average)
print("Final values:", np.round(x, 3))

plt.plot(history)
plt.axhline(initial_average, color="black", linestyle="--")
plt.xlabel("k")
plt.ylabel("x_i[k]")
plt.title("Discrete average consensus")
plt.grid()
plt.show()
