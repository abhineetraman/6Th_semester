import numpy as np

# Define a 3x4 matrix
mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Compute the size of the matrix
mat_size = mat.shape

# Display the size of the matrix
print(mat_size)

# Compute the length of the first row
row_len = len(mat[0])

# Compute the length of the second column
col_len = len(mat[:, 1])

# Display the length of the row and column
print(row_len, col_len)

# Load data from a text file
data = np.loadtxt('data.txt')

# Display the loaded data
print(data)

# Save the matrix to a text file
np.savetxt('mat.txt', mat)

# Load the matrix from the text file
loaded_mat = np.loadtxt('mat.txt')

# Display the loaded matrix
print(loaded_mat)

def current_scope():
    var1 = 10
    var2 = 'hello'
    var3 = np.array([1, 2, 3, 4])

    for name, val in locals().items():
        print(name, type(val))

current_scope()