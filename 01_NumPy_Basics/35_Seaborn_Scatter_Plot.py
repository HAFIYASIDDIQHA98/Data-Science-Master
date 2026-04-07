import seaborn as sns
import matplotlib.pyplot as plt

# Load sample data
tips = sns.load_dataset("tips")

# Create plot
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time")

plt.title("Total Bill vs Tip (by Time)")
plt.show()
