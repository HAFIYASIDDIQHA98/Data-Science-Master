import pandas as pd
# Using our previous 'df' logic
data = {'ID': range(1, 21), 'Val': range(101, 121)}
df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())
