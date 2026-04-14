from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

# 1. Iris dataset load karein
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# 2. Decision Tree Model banayein
dt_classifier = DecisionTreeClassifier(criterion='entropy', max_depth=3)
dt_classifier.fit(X_train, y_train)

# 3. Model accuracy check karein
accuracy = dt_classifier.score(X_test, y_test)
print(f"Decision Tree Accuracy: {accuracy * 100:.2f}%")

# 4. Tree ko visualize karein (Optional)
plt.figure(figsize=(12, 8))
tree.plot_tree(dt_classifier, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()
