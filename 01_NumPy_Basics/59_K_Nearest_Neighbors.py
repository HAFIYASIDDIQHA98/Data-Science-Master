import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn. datasets import load_iris
from sklearn. metrics import accuracy_score

# 1. Iris dataset load karein (Phoolon ki categories)
iris = load_iris()
X = iris.data  # Features (length, width)
y = iris.target # Species (target)

# 2. Data ko Train aur Test mein split karein
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. KNN Model banayein (K=3)
# Iska matlab hai ki ye har point ke 3 sabse kareebi padosi dekhega
knn = KNeighborsClassifier(n_neighbors=3)

# 4. Model ko train karein
knn.fit(X_train, y_train)

# 5. Predictions karein
y_pred = knn.predict(X_test)

# 6. Accuracy check karein
accuracy = accuracy_score(y_test, y_pred)
print(f"KNN Model Accuracy (K=3): {accuracy * 100:.2f}%")

# 7. Ek naya data point predict karke dekhein
new_sample = [[5.1, 3.5, 1.4, 0.2]] # Example measurement
prediction = knn.predict(new_sample)
print(f"Predicted Species for new sample: {iris.target_names[prediction][0]}")
