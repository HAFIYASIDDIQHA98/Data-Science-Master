import pandas as pd
import numpy as np

# Sample data banayein jisme missing values (NaN) hon
data = {'Product': ['Saree', 'Watch', 'Lamp', 'Mobile'],
        'Price': [340, np.nan, 500, np.nan]}
df = pd.DataFrame(data)

# Task 42: Missing values check karna
print("Missing values count:\n", df.isnull().sum())

# Task 43: Missing values ko average (mean) se fill karna
df['Price'] = df['Price'].fillna(df['Price'].mean())

print("\nCleaned Data:\n", df)
