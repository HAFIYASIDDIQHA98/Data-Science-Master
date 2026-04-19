import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score

# 1. Dataset load karein
data = load_breast_cancer()
X = data.data
y = data.target

# 2. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Pipeline banayein
# Isme pehle 'StandardScaler' chalega, fir 'RandomForest'
pipeline = Pipeline([
    ('scaler', StandardScaler()), 
    ('classifier', RandomForestClassifier(n_estimators=100))
])

# 4. Sirf pipeline ko fit karein (ye scaler aur model dono ko train kar dega)
pipeline.fit(X_train, y_train)

# 5. Predict karein
y_pred = pipeline.predict(X_test)

# 6. Accuracy check karein
print(f"Pipeline Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
