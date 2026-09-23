"""Python Code 4: Degree and Laplacian Matrices."""

import numpy as np


# Adjacency matrix of a simple undirected path: 1--2--3--4.
A = np.array([[0, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)

# The degree of each agent is the sum of its row.
degree = np.sum(A, axis=1)

# Put the degrees on the diagonal.
D = np.diag(degree)

# The graph Laplacian is L = D - A.
L = D - A

print("Adjacency matrix A:")
print(A)
print("\nDegree matrix D:")
print(D)
print("\nLaplacian matrix L:")
print(L)
