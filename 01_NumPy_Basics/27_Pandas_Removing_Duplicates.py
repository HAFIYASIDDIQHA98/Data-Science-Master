import pandas as pd
data = {'ID': [1, 2, 2, 3], 'Name': ['Hafiya', 'Zaid', 'Zaid', 'Ayesha']}
df = pd.DataFrame(data)

# Removing duplicate entries
clean_df = df.drop_duplicates()
print(f"Cleaned Data (No Duplicates):\n{clean_df}")
