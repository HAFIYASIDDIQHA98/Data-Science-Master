from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Actual labels vs Predicted labels
y_true = [0, 1, 0, 1, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]

cm = confusion_matrix(y_true, y_pred)

sns.heatmap(cm, annot=True, cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
