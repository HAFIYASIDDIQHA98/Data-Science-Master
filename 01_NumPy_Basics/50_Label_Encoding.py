import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {'Height': [150, 160, 170, 180], 'Weight': [50, 60, 70, 80]}
df = pd.DataFrame(data)

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print("Scaled Data (Mean=0, Std=1):\n", df_scaled)
