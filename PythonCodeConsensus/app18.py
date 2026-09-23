"""Python Code 18: Effect of the Discrete Step Size."""

import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)

D = np.diag(np.sum(A, axis=1))
L = D - A

x0 = np.array([-2, 4, 8, 2], dtype=float)
steps = 25

# Safe step size.
epsilon_safe = 0.25
P_safe = np.eye(4) - epsilon_safe * L
x_safe = x0.copy()
safe_history = [x_safe.copy()]

for k in range(steps):
    x_safe = P_safe @ x_safe
    safe_history.append(x_safe.copy())

# Step size that is too large.
epsilon_large = 0.8
P_large = np.eye(4) - epsilon_large * L
x_large = x0.copy()
large_history = [x_large.copy()]

for k in range(steps):
    x_large = P_large @ x_large
    large_history.append(x_large.copy())

safe_history = np.array(safe_history)
large_history = np.array(large_history)

plt.subplot(1, 2, 1)
plt.plot(safe_history)
plt.title("epsilon = 0.25")
plt.xlabel("k")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(large_history)
plt.title("epsilon = 0.8")
plt.xlabel("k")
plt.grid()

plt.tight_layout()
plt.show()
