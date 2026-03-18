import pandas as pd
data = {'Name': ['Hafiya', 'Zaid'], 'Job': ['Engineer', 'Dev'], 'Salary': [28800, 25000]}
df = pd.DataFrame(data)

# Selecting only 'Name' and 'Salary'
filtered_df = df[['Name', 'Salary']]
print(filtered_df)
