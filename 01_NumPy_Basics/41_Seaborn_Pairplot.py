import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# Pairplot se saare variables ka relation ek saath dikhta hai
sns.pairplot(iris, hue="species", markers=["o", "s", "D"])

plt.show()
