import joblib
from sklearn.linear_model import Ridge

model = Ridge().fit([[0, 0], [1, 1]], [0, 1])
joblib.dump(model, 'model.joblib')
print("Model saved using joblib.")
