"""Python Code 5: Important Laplacian Properties."""

import numpy as np


# Adjacency matrix of the path 1--2--3--4.
A = np.array([[0, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)

D = np.diag(np.sum(A, axis=1))
L = D - A

# Vector of ones.
one = np.ones(4)

# Every row of L sums to zero.
print("L times one:")
print(L @ one)

# The Laplacian always has an eigenvalue at zero.
eigenvalues = np.linalg.eigvals(L)
print("\nEigenvalues of L:")
print(np.round(eigenvalues, 4))
