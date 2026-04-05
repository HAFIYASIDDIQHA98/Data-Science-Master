import pandas as pd
df = pd.DataFrame({'Name': ['  hafiya  ', 'ZAID', 'ayesha ']})

# Cleaning whitespace and fixing case
df['Name'] = df['Name'].str.strip().str.capitalize()
print(df)
