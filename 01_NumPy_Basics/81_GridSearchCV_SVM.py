from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris

iris = load_iris()
param_grid = {'C': [0.1, 1, 10], 'kernel': ['rbf', 'linear']}

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)
grid.fit(iris.data, iris.target)

print(f"Best Parameters: {grid.best_params_}")
print(f"Best Score: {grid.best_score_}")
