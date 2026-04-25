from sklearn.metrics import make_scorer, f1_score
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

scorer = make_scorer(f1_score, average='weighted')
# Use this 'scorer' in cross_val_score
print("Custom F1 scorer created.")
