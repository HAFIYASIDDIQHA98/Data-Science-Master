import pandas as pd
data = {'Age': [23, 25, 22, 30, 28, 24], 'Score': [88, 92, 95, 70, 85, 90]}
df = pd.DataFrame(data)

print("Statistical Summary:")
print(df.describe())
