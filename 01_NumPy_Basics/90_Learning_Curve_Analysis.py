import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits
import numpy as np

digits = load_digits()
train_sizes, train_scores, test_scores = learning_curve(GaussianNB(), digits.data, digits.target)

plt.plot(train_sizes, np.mean(train_scores, axis=1), label='Train')
plt.plot(train_sizes, np.mean(test_scores, axis=1), label='Test')
plt.legend()
plt.show()
