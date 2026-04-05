import pandas as pd
df = pd.DataFrame({'Price': [100, 200, 300]})

# Adding 10% tax using a function
def add_tax(x):
    return x * 1.1

df['Price_with_Tax'] = df['Price'].apply(add_tax)
print(df)
