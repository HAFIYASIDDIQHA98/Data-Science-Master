import pandas as pd
data = {'Name': ['A', 'B', 'C'], 'Salary': [30000, 25000, 28800]}
df = pd.DataFrame(data)

# Sorting by Salary (Highest to Lowest)
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)
