import numpy as np

arr1 = np.array([1, 2])
arr2 = np.array([3, 4])

# Horizontal join
combined = np.concatenate((arr1, arr2))

print(f"Combined Array: {combined}")
