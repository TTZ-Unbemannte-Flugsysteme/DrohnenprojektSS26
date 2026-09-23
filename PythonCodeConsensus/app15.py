"""Python Code 15: Failure Without a Spanning Tree."""

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


# Two disconnected groups: 1--2 and 3--4.
N = [[2], [1], [4], [3]]
x0 = [-2, 4, 8, 2]
t = np.arange(0, 8, 0.01)

N.insert(0, [])
x0.insert(0, 0)

x = odeint(MAS, x0, t, args=(N,))

print("Final values:", np.round(x[-1, 1:], 3))
print("The two groups reach two different values.")

plt.plot(t, x[:, 1:])
plt.xlabel("t")
plt.ylabel("x_i")
plt.title("No global consensus without a spanning tree")
plt.grid()
plt.show()
