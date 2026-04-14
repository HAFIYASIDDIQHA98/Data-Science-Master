from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

# Digits dataset (Handwritten numbers)
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)

# Random Forest Model
rf_model = RandomForestClassifier(n_estimators=100) # 100 trees
rf_model.fit(X_train, y_train)

print(f"Random Forest Accuracy: {rf_model.score(X_test, y_test)*100:.2f}%")
