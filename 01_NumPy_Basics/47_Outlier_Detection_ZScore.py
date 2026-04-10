import pandas as pd
import numpy as np

# Sample data with an extreme outlier (5000)
df = pd.DataFrame({'Sales': [100, 110, 105, 120, 115, 5000]})

# Z-Score calculate karna
df['Z-Score'] = (df['Sales'] - df['Sales'].mean()) / df['Sales'].std()

# Rule: Agar Z-Score > 3 ya < -3 hai, toh wo outlier hai
outliers = df[abs(df['Z-Score']) > 2] # Sample data kam hai isliye 2 use kiya hai
print("Detected Outliers:\n", outliers)
