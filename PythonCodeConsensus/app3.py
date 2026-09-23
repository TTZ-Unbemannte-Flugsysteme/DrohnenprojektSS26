"""Python Code 3: Adjacency Matrix."""

import numpy as np


# List of directed connections (sender, receiver).
edges = [(2, 1), (1, 4), (2, 4), (4, 3),
         (3, 2), (2, 6), (6, 5), (5, 2)]

# There are six agents.
n = 6

# Start with a matrix of zeros.
A = np.zeros((n, n))

# Consensus convention:
# A[i-1, j-1] = 1 means that j sends information to i.
for j, i in edges:
    A[i - 1, j - 1] = 1

print("Adjacency matrix A:")
print(A)

# Read the first row.
print("Agent 1 receives information from:")
for j in range(n):
    if A[0, j] == 1:
        print("Agent", j + 1)
