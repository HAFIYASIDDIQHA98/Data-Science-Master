import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

# XGBoost model train karein
xg_model = xgb.XGBClassifier()
xg_model.fit(X_train, y_train)

y_pred = xg_model.predict(X_test)
print(f"XGBoost Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
