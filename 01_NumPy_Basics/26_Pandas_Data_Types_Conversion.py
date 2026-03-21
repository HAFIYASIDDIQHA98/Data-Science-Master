import pandas as pd
# Salary is currently stored as a String (Text)
df = pd.DataFrame({'Salary': ['28800', '25000', '30000']})

# Converting to Numeric for calculations
df['Salary'] = df['Salary'].astype(int)
print(f"Average Salary: {df['Salary'].mean()}")
