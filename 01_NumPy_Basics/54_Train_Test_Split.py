from sklearn.model_selection import train_test_split

# Features (X) aur Target (y)
X = iris.drop('species', axis=1)
y = iris['species']

# Split karna
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training Data Size: {len(X_train)}")
print(f"Testing Data Size: {len(X_test)}")
