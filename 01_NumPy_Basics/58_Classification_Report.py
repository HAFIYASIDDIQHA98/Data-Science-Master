from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# 1. Dummy classification data banayein
X, y = make_classification(n_samples=100, n_features=4, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Model train karein
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Predictions lein
y_pred = model.predict(X_test)

# 4. Classification Report print karein
report = classification_report(y_test, y_pred)
print("Classification Report:\n")
print(report)
