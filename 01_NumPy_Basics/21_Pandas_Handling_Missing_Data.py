import pandas as pd
import numpy as np

data = {'Name': ['Hafiya', 'Zaid', np.nan], 'Age': [23, np.nan, 25]}
df = pd.DataFrame(data)

# isnull() returns True for missing values
print("Missing Value Map:")
print(df.isnull())
print(f"\nTotal Nulls:\n{df.isnull().sum()}")
