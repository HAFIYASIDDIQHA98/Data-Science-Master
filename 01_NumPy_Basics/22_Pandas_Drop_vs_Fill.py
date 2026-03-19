import pandas as pd
import numpy as np

df = pd.DataFrame({'Score': [90, 85, np.nan, 70]})

# Option 1: Filling NaN with mean
df_filled = df.fillna(value=df['Score'].mean())

# Option 2: Dropping rows with NaN
df_dropped = df.dropna()

print(f"Original:\n{df}")
print(f"Cleaned (Filled):\n{df_filled}")
