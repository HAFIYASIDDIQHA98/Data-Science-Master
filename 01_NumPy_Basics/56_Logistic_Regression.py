import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample: Study Hours vs Pass(1)/Fail(0)
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# Predict: Agar koi 3.5 hours padhega toh kya wo pass hoga?
prediction = model.predict([[3.5]])
print(f"Prediction for 3.5 hours: {'Pass' if prediction[0] == 1 else 'Fail'}")
