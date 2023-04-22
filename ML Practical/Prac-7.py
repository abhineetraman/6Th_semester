import numpy as np

# Define a matrix
mat = np.array([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]])

# Convert matrix data to absolute values
mat_abs = np.abs(mat)

# Display the result
print(mat_abs)

# Take the negative of matrix values
mat_neg = -mat

# Display the result
print(mat_neg)

# Define a matrix
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Add a row to the matrix
new_row = np.array([10, 11, 12])
mat_new_row = np.vstack((mat, new_row))

# Remove a column from the matrix
mat_remove_col = np.delete(mat, 1, axis=1)

# Display the results
print(mat_new_row)
print(mat_remove_col)

# Find the maximum value in the matrix
max_val = np.max(mat)

# Find the minimum value in the matrix
min_val = np.min(mat)

# Find the maximum value in each column
max_col = np.max(mat, axis=0)

# Find the minimum value in each row
min_row = np.min(mat, axis=1)

# Display the results
print(max_val)
print(min_val)
print(max_col)
print(min_row)

# Find the sum of all elements in the matrix
sum_all = np.sum(mat)

# Find the sum of elements in each row
sum_row = np.sum(mat, axis=1)

# Find the sum of elements in each column
sum_col = np.sum(mat, axis=0)

# Display the results
print(sum_all)
print(sum_row)
print(sum_col)