import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# 1. Model train karein
iris = load_iris()
model = RandomForestClassifier(n_estimators=10)
model.fit(iris.data, iris.target)

# 2. Model ko file mein save karein
filename = 'finalized_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print(f"Model successfully saved as {filename}")
