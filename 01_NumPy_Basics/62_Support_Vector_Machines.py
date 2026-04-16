from sklearn.svm import SVC
from sklearn.datasets import load_iris

iris = load_iris()
# SVM with Linear Kernel
svm_model = SVC(kernel='linear')
svm_model.fit(iris.data, iris.target)

print("SVM Model trained successfully.")
