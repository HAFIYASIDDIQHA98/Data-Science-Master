import numpy as np

original = np.array([1, 2, 3])

# View: Changing it affects the original
view_arr = original.view()
# Copy: Changing it does NOT affect original
copy_arr = original.copy()

view_arr[0] = 99
print(f"Original after view change: {original}") # Will change
copy_arr[1] = 88
print(f"Original after copy change: {original}") # Won't change
