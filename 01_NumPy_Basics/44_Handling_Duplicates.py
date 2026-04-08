import pandas as pd

data = {'ID': [1, 2, 2, 3, 4, 4], 'Item': ['Saree', 'Watch', 'Watch', 'Lamp', 'Mobile', 'Mobile']}
df = pd.DataFrame(data)

# Duplicate check
print("Before:", len(df))
df = df.drop_duplicates()
print("After:", len(df))
