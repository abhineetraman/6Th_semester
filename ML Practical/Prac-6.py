import numpy as np

# Define two matrices
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

# Add the matrices
mat_sum = mat1 + mat2

# Display the result
print(mat_sum)

# Subtract the matrices
mat_diff = mat1 - mat2

# Display the result
print(mat_diff)

# Multiply the matrices
mat_prod = np.dot(mat1, mat2)

# Display the result
print(mat_prod)

# Define a matrix
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Display the second row
print(mat[1, :])

# Display the third column
print(mat[:, 2])