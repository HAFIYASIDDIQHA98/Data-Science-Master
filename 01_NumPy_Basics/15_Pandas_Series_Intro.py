import pandas as pd

# A Series is like a column in Excel
data = [10, 20, 30, 40]
labels = ['a', 'b', 'c', 'd']
s = pd.Series(data, index=labels)

print("Pandas Series:")
print(s)
print(f"Value at index 'c': {s['c']}")
