import pandas as pd
from sklearn. preprocessing import StandardScaler

# Sample data
data = {'Age': [25, 30, 35, 40], 'Salary': [50000, 80000, 120000, 150000]}
df = pd.DataFrame(data)

# Scaler object banayein
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print("Standardized Data (Mean=0, Std=1):\n", df_scaled)
