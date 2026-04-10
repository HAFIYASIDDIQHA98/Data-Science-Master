import pandas as pd

df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green']})

# Text ko numbers mein badalna
df_encoded = pd.get_dummies(df, columns=['Color'])
print(df_encoded)
