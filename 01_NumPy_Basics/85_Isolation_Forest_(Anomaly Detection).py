from sklearn.ensemble import IsolationForest
import numpy as np

X = np.array([[1, 1], [1.1, 1], [0.9, 1], [10, 10]]) # 10,10 is an outlier
clf = IsolationForest(contamination=0.2)
print("Anomalies (-1):", clf.fit_predict(X))
