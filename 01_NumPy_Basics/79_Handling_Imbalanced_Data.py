from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
from collections import Counter

# Imbalanced data banayein
X, y = make_classification(n_samples=1000, weights=[0.95], flip_y=0)
print(f"Before SMOTE: {Counter(y)}")

# Oversampling karna
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

print(f"After SMOTE: {Counter(y_res)}")
