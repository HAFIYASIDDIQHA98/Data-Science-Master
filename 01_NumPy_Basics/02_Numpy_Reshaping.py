import numpy as np

# Creating a 1D array with 6 elements
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape it to 2 rows and 3 columns
reshaped_mat = arr.reshape(2, 3)

print(f"Original 1D Array: {arr}")
print(f"Reshaped 2D Matrix:\n{reshaped_mat}")
print(f"New Shape: {reshaped_mat.shape}")
