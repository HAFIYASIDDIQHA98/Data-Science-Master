import numpy as np

# Creating an array and checking its default data type
arr1 = np.array([1, 2, 3])
print(f"Default Type (Integer): {arr1.dtype}")

# Explicitly defining a float data type to save decimal values
arr2 = np.array([1, 2, 3], dtype='float32')
print(f"Specified Type (Float32): {arr2.dtype}")
print(f"Array values: {arr2}")

# Converting an existing array to a different type
arr3 = arr1.astype('float64')
print(f"Converted Type: {arr3.dtype}")
