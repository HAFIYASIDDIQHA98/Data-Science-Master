import pandas as pd

# Creating data using a dictionary
data = {
    'Name': ['Hafiya', 'Ayesha', 'Zaid'],
    'Score': [95, 88, 92],
    'City': ['Pedana', 'Hyderabad', 'Bangalore']
}

df = pd.DataFrame(data)
print("My First DataFrame:")
print(df)
