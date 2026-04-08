import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Violin plot banayein (Split=True se comparison asan hota hai)
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True, inner="quart")

plt.title("Bill Density: Male vs Female")
plt.show()
