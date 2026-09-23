"""Python Code 25: Continuous and Discrete Consensus."""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def continuous_MAS(x, t, L):
    """Continuous model: x_dot = -Lx."""

    dxdt = -L @ x
    return dxdt


# Undirected path: 1--2--3--4.
A = np.array([[0, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)

D = np.diag(np.sum(A, axis=1))
L = D - A

x0 = np.array([-2, 4, 8, 2], dtype=float)

# Continuous-time simulation.
t = np.arange(0, 12, 0.01)
x_continuous = odeint(continuous_MAS, x0, t, args=(L,))

# Discrete-time simulation.
epsilon = 0.25
P = np.eye(4) - epsilon * L
steps = 48

x = x0.copy()
x_discrete = [x.copy()]

for k in range(steps):
    x = P @ x
    x_discrete.append(x.copy())

x_discrete = np.array(x_discrete)

print("Initial average:", np.mean(x0))
print("Continuous final values:",
      np.round(x_continuous[-1], 3))
print("Discrete final values:",
      np.round(x_discrete[-1], 3))

plt.subplot(1, 2, 1)
plt.plot(t, x_continuous)
plt.xlabel("t")
plt.ylabel("x_i(t)")
plt.title("Continuous time")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x_discrete)
plt.xlabel("k")
plt.ylabel("x_i[k]")
plt.title("Discrete time")
plt.grid()

plt.tight_layout()
plt.show()
