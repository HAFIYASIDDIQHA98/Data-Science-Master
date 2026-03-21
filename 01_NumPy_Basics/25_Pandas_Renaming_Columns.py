import pandas as pd
df = pd.DataFrame({'old_col': [1, 2], 'name_val': ['A', 'B']})

# Renaming for clarity
df = df.rename(columns={'old_col': 'ID', 'name_val': 'User_Name'})
print(df.columns)
