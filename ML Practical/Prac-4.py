import numpy as np

# Define a single dimension array
arr1 = np.array([1, 2, 3, 4, 5])

# Display the array
print(arr1)

# Define a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Display the array
print(arr2)

# Define a single dimension array of all ones
arr_ones = np.ones(5)

# Display the array
print(arr_ones)

# Define a 2D array of all zeros
arr_zeros = np.zeros((3, 4))

# Display the array
print(arr_zeros)

# Define a single dimension array with random values between 0 and 1
arr_random = np.random.rand(5)

# Display the array
print(arr_random)

# Define a 2D array with random values between -1 and 1
arr_random2 = np.random.uniform(low=-1, high=1, size=(3, 4))

# Display the array
print(arr_random2)

# Define a diagonal matrix
arr_diag = np.diag([1, 2, 3, 4])

# Display the matrix
print(arr_diag)