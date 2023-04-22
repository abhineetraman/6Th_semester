import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Transpose of a matrix
A_T = A.T
print("Transpose of matrix A:\n", A_T)

# Adding two matrices
C = A + B
print("Sum of matrices A and B:\n", C)

# Subtracting two matrices
D = A - B
print("Difference of matrices A and B:\n", D)

# Multiplying two matrices
E = A.dot(B)
print("Product of matrices A and B:\n", E)
