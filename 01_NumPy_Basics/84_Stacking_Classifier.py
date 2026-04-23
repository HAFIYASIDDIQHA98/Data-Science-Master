from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

estimators = [('rf', RandomForestClassifier()), ('svc', SVC())]
stack_model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
print("Stacking model initialized.")
