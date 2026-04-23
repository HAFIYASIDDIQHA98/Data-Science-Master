from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()
model1 = LogisticRegression(max_iter=200)
model2 = DecisionTreeClassifier()
ensemble = VotingClassifier(estimators=[('lr', model1), ('dt', model2)], voting='hard')
ensemble.fit(iris.data, iris.target)
print("Voting Classifier trained successfully.")
