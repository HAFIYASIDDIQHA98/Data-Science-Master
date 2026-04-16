import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Dataset load karein
iris = load_iris()
X = iris.data
y = iris.target

# 2. Data split karein
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Naive Bayes Model banayein (GaussianNB numeric data ke liye best hai)
nb_model = GaussianNB()

# 4. Model train karein
nb_model.fit(X_train, y_train)

# 5. Prediction karein
y_pred = nb_model.predict(X_test)

# 6. Results check karein
accuracy = accuracy_score(y_test, y_pred)
print(f"Naive Bayes Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix dekhne ke liye
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
