"""Python Code 14: Continuous Consensus on an Unbalanced Digraph."""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def MAS(x, t, N):
    dxdt = [0] * len(N)

    for i in range(len(N)):
        u = 0

        for j in N[i]:
            u = u + x[j] - x[i]

        dxdt[i] = u

    return dxdt


# Agent 1 is the root. It sends information but receives none.
N = [[], [1], [1], [2, 3]]
x0 = [5, -2, 8, 0]
t = np.arange(0, 10, 0.01)

initial_average = np.mean(x0)
root_value = x0[0]

N.insert(0, [])
x0.insert(0, 0)

x = odeint(MAS, x0, t, args=(N,))

print("Initial average:", initial_average)
print("Initial value of the root:", root_value)
print("Final values:", np.round(x[-1, 1:], 3))

plt.plot(t, x[:, 1:])
plt.axhline(initial_average, color="black", linestyle="--",
            label="initial average")
plt.axhline(root_value, color="red", linestyle=":",
            label="root value")
plt.xlabel("t")
plt.ylabel("x_i")
plt.title("Unbalanced graph: consensus is not the average")
plt.grid()
plt.legend()
plt.show()
