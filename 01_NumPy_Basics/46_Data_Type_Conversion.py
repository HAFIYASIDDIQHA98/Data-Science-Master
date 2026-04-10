import pandas as pd

# Sample data: 'Price' yahan strings hain
data = {'Item': ['Saree', 'Watch', 'Lamp'], 'Price': ['340', '999', '500']}
df = pd.DataFrame(data)

# String ko numeric (float) mein convert karna
df['Price'] = df['Price'].astype(float)

print("Data Types after conversion:\n", df.dtypes)
print("\nSum of Prices:", df['Price'].sum())
