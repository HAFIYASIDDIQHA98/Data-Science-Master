from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
model = LogisticRegression(max_iter=200)

# 5-Fold Cross Validation
scores = cross_val_score(model, iris.data, iris.target, cv=5)

print(f"All Scores: {scores}")
print(f"Average Accuracy: {scores.mean()*100:.2f}%")
