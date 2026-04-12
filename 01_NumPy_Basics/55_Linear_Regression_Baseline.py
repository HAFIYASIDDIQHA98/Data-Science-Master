import numpy as np
from sklearn.linear_model import LinearRegression

# X = Experience (Years), y = Salary (in Lakhs)
X = np.array([[1], [2], [3], [5], [10]]) 
y = np.array([3, 5, 7, 12, 25])

# Model train karein
model = LinearRegression()
model.fit(X, y)

# Predict karein 4 saal ke experience ki salary
prediction = model.predict([[4]])
print(f"Predicted Salary for 4 years experience: {prediction[0]:.2f} Lakhs")
