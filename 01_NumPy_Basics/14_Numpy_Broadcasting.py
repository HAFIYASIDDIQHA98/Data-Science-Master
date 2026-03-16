import numpy as np

matrix = np.array([[1, 1, 1], [2, 2, 2]])
scalar = 10

# The scalar '10' is added to every single element (Broadcasting)
result = matrix + scalar

print(f"Matrix:\n{matrix}")
print(f"Result (Matrix + 10):\n{result}")
