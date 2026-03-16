import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extract second row
row2 = matrix[1, :]

# Extract last two elements of the first two rows
sub_matrix = matrix[0:2, 1:3]

print(f"Full Matrix:\n{matrix}")
print(f"Second Row: {row2}")
print(f"Sub-matrix:\n{sub_matrix}")
