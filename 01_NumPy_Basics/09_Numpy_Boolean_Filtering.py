import numpy as np

arr = np.array([10, 55, 22, 80, 15, 90])

# Condition: Elements greater than 50
filtered_data = arr[arr > 50]

print(f"Original Data: {arr}")
print(f"Values > 50: {filtered_data}")
