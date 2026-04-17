from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# Parameters to test
param_grid = {'C': [0.1, 1, 10], 'kernel': ['rbf', 'linear']}

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=0)
grid.fit(iris.data, iris.target)

print(f"Best Parameters: {grid.best_params_}")
