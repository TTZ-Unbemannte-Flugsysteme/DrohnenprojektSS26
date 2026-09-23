"""Python Code 13: Continuous Consensus on a Balanced Digraph."""

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


# Directed cycle: 1 -> 2 -> 3 -> 4 -> 1.
# Every agent has one incoming and one outgoing edge.
N = [[4], [1], [2], [3]]
x0 = [-2, 4, 8, 2]
t = np.arange(0, 10, 0.01)

initial_average = np.mean(x0)

N.insert(0, [])
x0.insert(0, 0)

x = odeint(MAS, x0, t, args=(N,))

print("Initial average:", initial_average)
print("Final values:", np.round(x[-1, 1:], 3))

plt.plot(t, x[:, 1:])
plt.axhline(initial_average, color="black", linestyle="--")
plt.xlabel("t")
plt.ylabel("x_i")
plt.title("Balanced directed graph: average is preserved")
plt.grid()
plt.show()
