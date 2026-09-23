"""Python Code 22: Leader-Follower Consensus."""

import numpy as np
import matplotlib.pyplot as plt


# Agent 1 is the leader.
# Agent 2 follows 1, agent 3 follows 2, and agent 4 follows 3.
N = [[], [], [1], [2], [3]]

# Agent 0 is a dummy agent.
x = np.array([0, 5, -4, 8, 0], dtype=float)

epsilon = 0.3
steps = 40

history = np.zeros((steps + 1, len(x)))
history[0] = x

for k in range(steps):
    x_new = x.copy()

    # Start at agent 2 because agent 1 is the fixed leader.
    for i in range(2, len(N)):
        u = 0

        for j in N[i]:
            u = u + x[j] - x[i]

        x_new[i] = x[i] + epsilon * u

    x = x_new
    history[k + 1] = x

print("Leader value:", x[1])
print("Final follower values:", np.round(x[2:], 3))

plt.plot(history[:, 1:])
plt.xlabel("k")
plt.ylabel("x_i[k]")
plt.title("Followers converge to the leader")
plt.grid()
plt.show()
