import numpy as np

# arange: (start, stop, step)
# Example: 0 se 10 tak, har number mein 2 ka gap
seq1 = np.arange(0, 10, 2) 

# linspace: (start, stop, number of elements)
# Example: 0 se 1 ke beech barabar 5 points
seq2 = np.linspace(0, 1, 5)

print(f"Arange Sequence: {seq1}")
print(f"Linspace Sequence: {seq2}")
