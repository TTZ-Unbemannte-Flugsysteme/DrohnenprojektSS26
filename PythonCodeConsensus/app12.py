"""Python Code 12: Average Consensus on an Undirected Path."""

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


# Undirected path: 1--2--3--4.
N = [[2], [1, 3], [2, 4], [3]]
x0 = [-2, 4, 8, 2]
t = np.arange(0, 12, 0.01)

# Calculate the initial average before adding the dummy agent.
initial_average = np.mean(x0)
print("Initial average:", initial_average)

N.insert(0, [])
x0.insert(0, 0)

x = odeint(MAS, x0, t, args=(N,))

print("Final values:", np.round(x[-1, 1:], 3))

plt.plot(t, x[:, 1:])
plt.axhline(initial_average, color="black", linestyle="--",
            label="initial average")
plt.xlabel("t")
plt.ylabel("x_i")
plt.title("Average consensus on an undirected graph")
plt.grid()
plt.legend()
plt.show()
